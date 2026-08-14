#!/usr/bin/env python3
"""Fetch S&P 500 breadth metrics for weekly-market-scan-web §3.

Computes from constituent daily closes (Yahoo chart API):
  - advancing / declining / unchanged
  - 52-week new highs / new lows
  - % of members above 50-DMA and 200-DMA
  - Top 10 weight contribution to the 1W index move (Slickcharts weights)

Cross-checks % above MA vs historyofmarket.com when reachable.

Usage:
  python scripts/fetch_breadth.py
  python scripts/fetch_breadth.py --json
  python scripts/fetch_breadth.py --as-of 2026-08-07 --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, datetime, timedelta, timezone
from statistics import mean
from typing import Any

USER_AGENT = (
    "Mozilla/5.0 (compatible; weekly-market-scan-web/1.0; "
    "+https://github.com/huyou963-qi/weekly-market-scan-web)"
)
WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
DATASETS_CSV = (
    "https://raw.githubusercontent.com/datasets/s-p-500-companies/master/data/constituents.csv"
)
YAHOO_CHART = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
HOM_BREADTH = "https://historyofmarket.com/api/sp500/breadth.json"
SLICKCHARTS_SPX = "https://www.slickcharts.com/sp500"
MIN_OK = 400
WORKERS = 8
SMA_50 = 50
SMA_200 = 200
LOOKBACK_52W = 252


def _http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _yahoo_symbol(ticker: str) -> str:
    return ticker.replace(".", "-")


def _parse_wiki_tickers(html: str) -> list[str]:
    start = html.find('id="constituents"')
    if start < 0:
        return []
    end = html.find("</table>", start)
    chunk = html[start:end] if end > start else html[start:]
    tickers: list[str] = []
    seen: set[str] = set()
    for row in re.finditer(r"<tr[^>]*>(.*?)</tr>", chunk, re.S | re.I):
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row.group(1), re.S | re.I)
        if not cells:
            continue
        text = re.sub(r"<[^>]+>", "", cells[0])
        text = re.sub(r"&amp;", "&", text).strip().upper()
        if not re.fullmatch(r"[A-Z]{1,5}(?:[.-][A-Z]{1,2})?", text):
            continue
        if text not in seen:
            seen.add(text)
            tickers.append(text)
    return tickers


def _parse_csv_tickers(text: str) -> list[str]:
    lines = text.strip().splitlines()
    if not lines:
        return []
    header = [c.strip().strip('"') for c in lines[0].split(",")]
    try:
        idx = next(i for i, h in enumerate(header) if h.lower() in ("symbol", "ticker"))
    except StopIteration:
        idx = 0
    tickers: list[str] = []
    seen: set[str] = set()
    for line in lines[1:]:
        cols = [c.strip().strip('"') for c in line.split(",")]
        if len(cols) <= idx:
            continue
        text = cols[idx].strip().upper()
        if not re.fullmatch(r"[A-Z]{1,5}(?:[.-][A-Z]{1,2})?", text):
            continue
        if text not in seen:
            seen.add(text)
            tickers.append(text)
    return tickers


def load_constituents() -> tuple[list[str], str]:
    try:
        html = _http_get(WIKI_URL).decode("utf-8", "replace")
        tickers = _parse_wiki_tickers(html)
        if len(tickers) >= 490:
            return tickers, "wikipedia"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        wiki_err = str(exc)
    else:
        wiki_err = f"parsed {len(tickers)} tickers"

    try:
        csv_text = _http_get(DATASETS_CSV).decode("utf-8", "replace")
        tickers = _parse_csv_tickers(csv_text)
        if len(tickers) >= 490:
            return tickers, "datasets/s-p-500-companies"
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        raise RuntimeError(
            f"constituent list failed (wiki: {wiki_err}; csv: {exc})"
        ) from exc

    raise RuntimeError(f"constituent list too short (wiki: {wiki_err})")


def _ts_to_date(ts: int) -> date:
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).date()


def fetch_chart(ticker: str) -> tuple[str, list[tuple[date, float]] | None, str | None]:
    url = (
        f"{YAHOO_CHART.format(symbol=urllib.parse.quote(_yahoo_symbol(ticker)))}"
        "?interval=1d&range=1y&events=history"
    )
    last_err = "unknown"
    for attempt in range(3):
        try:
            payload = json.loads(_http_get(url, timeout=25))
            result = (payload.get("chart") or {}).get("result")
            if not result:
                err = (payload.get("chart") or {}).get("error")
                return ticker, None, f"no result {err}"
            timestamps = result[0].get("timestamp") or []
            closes = (
                ((result[0].get("indicators") or {}).get("quote") or [{}])[0].get("close")
                or []
            )
            pairs = [
                (_ts_to_date(ts), float(close))
                for ts, close in zip(timestamps, closes)
                if close is not None
            ]
            if not pairs:
                return ticker, None, "empty closes"
            return ticker, pairs, None
        except urllib.error.HTTPError as exc:
            last_err = f"HTTP {exc.code}"
            time.sleep(0.35 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, ValueError) as exc:
            last_err = str(exc)
            time.sleep(0.35 * (attempt + 1))
    return ticker, None, last_err


def _idx_on_or_before(days: list[date], target: date) -> int | None:
    for i in range(len(days) - 1, -1, -1):
        if days[i] <= target:
            return i
    return None


def _sma(closes: list[float], end_idx: int, window: int) -> float | None:
    start = end_idx - window + 1
    if start < 0:
        return None
    return mean(closes[start : end_idx + 1])


def snapshot_one(
    closes: list[float],
    idx: int,
) -> dict[str, Any] | None:
    if idx < 1:
        return None
    last = closes[idx]
    prev = closes[idx - 1]
    lookback_start = max(0, idx - LOOKBACK_52W + 1)
    prior = closes[lookback_start:idx]
    sma50 = _sma(closes, idx, SMA_50)
    sma200 = _sma(closes, idx, SMA_200)
    return {
        "advance": last > prev,
        "decline": last < prev,
        "unchanged": last == prev,
        "new_high": bool(prior) and last >= max(prior),
        "new_low": bool(prior) and last <= min(prior),
        "above_50": None if sma50 is None else last > sma50,
        "above_200": None if sma200 is None else last > sma200,
        "close": last,
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    adv = sum(1 for r in rows if r["advance"])
    dec = sum(1 for r in rows if r["decline"])
    unch = sum(1 for r in rows if r["unchanged"])
    nh = sum(1 for r in rows if r["new_high"])
    nl = sum(1 for r in rows if r["new_low"])
    a50 = [r["above_50"] for r in rows if r["above_50"] is not None]
    a200 = [r["above_200"] for r in rows if r["above_200"] is not None]
    pct50 = round(100.0 * sum(1 for x in a50 if x) / len(a50), 1) if a50 else None
    pct200 = round(100.0 * sum(1 for x in a200 if x) / len(a200), 1) if a200 else None
    ratio = round(adv / dec, 2) if dec else None
    return {
        "n": len(rows),
        "advancers": adv,
        "decliners": dec,
        "unchanged": unch,
        "ad_ratio": ratio,
        "new_highs": nh,
        "new_lows": nl,
        "nh_nl_net": nh - nl,
        "pct_above_50dma": pct50,
        "pct_above_50dma_n": len(a50),
        "pct_above_200dma": pct200,
        "pct_above_200dma_n": len(a200),
    }


def fetch_hom_cross_check(as_of: date) -> dict[str, Any] | None:
    try:
        payload = json.loads(_http_get(HOM_BREADTH, timeout=20))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError):
        return None
    series = payload.get("series") or []
    picked = None
    for row in series:
        try:
            d = datetime.strptime(row["date"], "%Y-%m-%d").date()
        except (KeyError, ValueError, TypeError):
            continue
        if d <= as_of:
            picked = {**row, "date": row["date"]}
        else:
            break
    if not picked:
        return None
    return {
        "source": "historyofmarket.com/api/sp500/breadth.json",
        "as_of": picked["date"],
        "pct_above_50dma": picked.get("pct50"),
        "pct_above_200dma": picked.get("pct200"),
        "updated": payload.get("updated"),
        "members": payload.get("members"),
    }


def _pp_delta(now: float | None, then: float | None) -> float | None:
    if now is None or then is None:
        return None
    return round(now - then, 1)


def load_spx_weights() -> tuple[list[dict[str, Any]] | None, str]:
    try:
        html = _http_get(SLICKCHARTS_SPX).decode("utf-8", "replace")
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
        return None, f"slickcharts fetch failed: {exc}"
    rows: list[dict[str, Any]] = []
    for match in re.finditer(
        r'href="/symbol/([A-Z][A-Z0-9.\-]*)">\1</a></td><td>([0-9.]+)%</td>',
        html,
    ):
        rows.append({"ticker": match.group(1), "weight_pct": float(match.group(2))})
    if len(rows) < 10:
        return None, f"slickcharts parsed {len(rows)} weights"
    return rows, "slickcharts.com/sp500"


def _lookup_chart(
    ticker: str,
    charts: dict[str, list[tuple[date, float]]],
) -> list[tuple[date, float]] | None:
    if ticker in charts:
        return charts[ticker]
    alt = ticker.replace(".", "-") if "." in ticker else ticker.replace("-", ".")
    return charts.get(alt)


def _close_on(
    pairs: list[tuple[date, float]],
    session: date,
    *,
    allow_lag: int = 4,
) -> float | None:
    days = [p[0] for p in pairs]
    idx = _index_on_date(days, session)
    if idx is None:
        idx = _idx_on_or_before(days, session)
        if idx is None or (session - days[idx]).days > allow_lag:
            return None
    return pairs[idx][1]


def _period_return(
    pairs: list[tuple[date, float]] | None,
    start: date,
    end: date,
) -> float | None:
    if not pairs:
        return None
    start_px = _close_on(pairs, start)
    end_px = _close_on(pairs, end)
    if start_px is None or end_px is None or start_px == 0:
        return None
    return end_px / start_px - 1.0


def _top10_for_week(
    weights: list[dict[str, Any]],
    charts: dict[str, list[tuple[date, float]]],
    index_pairs: list[tuple[date, float]] | None,
    start: date,
    end: date,
) -> dict[str, Any] | None:
    index_r = _period_return(index_pairs, start, end)
    names: list[dict[str, Any]] = []
    contrib_sum = 0.0
    contrib_n = 0
    weight_sum = 0.0
    for row in weights[:10]:
        ticker = row["ticker"]
        weight_pct = float(row["weight_pct"])
        weight_sum += weight_pct
        stock_r = _period_return(_lookup_chart(ticker, charts), start, end)
        contrib = None if stock_r is None else round(weight_pct / 100.0 * stock_r * 100.0, 2)
        names.append(
            {
                "ticker": ticker,
                "weight_pct": weight_pct,
                "return_1w_pct": None if stock_r is None else round(stock_r * 100.0, 2),
                "contrib_ppt": contrib,
            }
        )
        if contrib is not None:
            contrib_sum += contrib
            contrib_n += 1
    if contrib_n < 8:
        return None
    index_ppt = None if index_r is None else round(index_r * 100.0, 2)
    share = None
    if index_ppt is not None and abs(index_ppt) >= 0.05:
        share = round(contrib_sum / index_ppt * 100.0, 1)
    leaders = sorted(
        [n for n in names if n["contrib_ppt"] is not None],
        key=lambda n: abs(n["contrib_ppt"]),
        reverse=True,
    )[:3]
    return {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "weight_sum_pct": round(weight_sum, 2),
        "contrib_ppt": round(contrib_sum, 2),
        "index_return_pct": index_ppt,
        "share_of_index_move_pct": share,
        "names": names,
        "leaders": [{"ticker": n["ticker"], "contrib_ppt": n["contrib_ppt"]} for n in leaders],
    }


def compute_top10_contribution(
    constituent_charts: dict[str, list[tuple[date, float]]],
    index_pairs: list[tuple[date, float]] | None,
    as_of: date,
    week_as_of: date,
    prior_week_as_of: date | None,
) -> dict[str, Any]:
    weights, source = load_spx_weights()
    if not weights:
        return {"error": source}
    now = _top10_for_week(weights, constituent_charts, index_pairs, week_as_of, as_of)
    if not now:
        return {"error": "top10 returns unavailable", "weights_source": source}
    prior = None
    if prior_week_as_of:
        prior = _top10_for_week(
            weights, constituent_charts, index_pairs, prior_week_as_of, week_as_of
        )
    share_delta = None
    contrib_delta = None
    if prior:
        if now.get("share_of_index_move_pct") is not None and prior.get(
            "share_of_index_move_pct"
        ) is not None:
            share_delta = round(
                now["share_of_index_move_pct"] - prior["share_of_index_move_pct"], 1
            )
        contrib_delta = round(now["contrib_ppt"] - prior["contrib_ppt"], 2)
    leader_s = "、".join(
        f"{n['ticker']} {n['contrib_ppt']:+.2f}ppt" for n in now.get("leaders") or []
    )
    index_ppt = now.get("index_return_pct")
    index_s = f"{index_ppt:+.2f}%" if index_ppt is not None else "指数 —"
    share = now.get("share_of_index_move_pct")
    share_s = f"（占变动 {share:.0f}%）" if share is not None else ""
    report = (
        f"{now['contrib_ppt']:+.2f}ppt / {index_s}{share_s}；"
        f"Top10 权重 {now['weight_sum_pct']:.1f}%"
        + (f" — {leader_s}" if leader_s else "")
    )
    report_1w = "—"
    if contrib_delta is not None:
        report_1w = f"贡献 {contrib_delta:+.2f}ppt"
        if (
            share_delta is not None
            and abs(share_delta) <= 40
            and now.get("share_of_index_move_pct") is not None
            and prior
            and prior.get("index_return_pct") is not None
            and abs(prior["index_return_pct"]) >= 0.5
        ):
            report_1w += f"；占变动 {share_delta:+.0f}ppt"
    return {
        "weights_source": source,
        "weight_as_of": "current slickcharts snapshot (applied to the week)",
        "now": now,
        "week_ago": prior,
        "change_1w": {"contrib_ppt": contrib_delta, "share_of_index_move_pct": share_delta},
        "report": report,
        "report_1w": report_1w,
    }


def build_report_strings(
    now: dict[str, Any],
    delta: dict[str, Any],
    top10: dict[str, Any] | None = None,
) -> dict[str, str]:
    ratio = now.get("ad_ratio")
    ratio_s = f"{ratio:.2f}" if isinstance(ratio, (int, float)) else "—"
    return {
        "advance_decline": f"{now['advancers']} / {now['decliners']}（A/D {ratio_s}）",
        "nh_nl": f"{now['new_highs']} / {now['new_lows']}（净 {now['nh_nl_net']:+d}）",
        "pct_above_50dma": f"{now['pct_above_50dma']}%"
        if now.get("pct_above_50dma") is not None
        else "—",
        "pct_above_200dma": f"{now['pct_above_200dma']}%"
        if now.get("pct_above_200dma") is not None
        else "—",
        "advance_decline_1w": (
            f"涨 {delta['advancers']:+d} / 跌 {delta['decliners']:+d}"
            if delta.get("advancers") is not None
            else "—"
        ),
        "nh_nl_1w": f"净 {delta['nh_nl_net']:+d}" if delta.get("nh_nl_net") is not None else "—",
        "pct_above_50dma_1w": (
            f"{delta['pct_above_50dma']:+.1f}ppt"
            if delta.get("pct_above_50dma") is not None
            else "—"
        ),
        "pct_above_200dma_1w": (
            f"{delta['pct_above_200dma']:+.1f}ppt"
            if delta.get("pct_above_200dma") is not None
            else "—"
        ),
        "top10_contrib": (top10 or {}).get("report")
        or (top10 or {}).get("error")
        or "—",
        "top10_contrib_1w": (top10 or {}).get("report_1w") or "—",
    }


def _session_dates(charts: dict[str, list[tuple[date, float]]], target: date) -> tuple[date, date]:
    """Pin as-of and week-ago to SPY (fallback: modal last date)."""
    spy = charts.get("SPY")
    if spy:
        days = [p[0] for p in spy]
        as_of_idx = _idx_on_or_before(days, target)
        if as_of_idx is None:
            raise RuntimeError("SPY chart has no bar on or before as-of")
        as_of_used = days[as_of_idx]
        week_idx = _idx_on_or_before(days, as_of_used - timedelta(days=7))
        if week_idx is None:
            raise RuntimeError("SPY chart has no bar for week-ago snapshot")
        return as_of_used, days[week_idx]
    last_dates = [pairs[-1][0] for pairs in charts.values()]
    as_of_used = max(d for d in last_dates if d <= target)
    week_target = as_of_used - timedelta(days=7)
    week_dates = []
    for pairs in charts.values():
        idx = _idx_on_or_before([p[0] for p in pairs], week_target)
        if idx is not None:
            week_dates.append(pairs[idx][0])
    if not week_dates:
        raise RuntimeError("no week-ago session date")
    return as_of_used, max(week_dates)


def _index_on_date(days: list[date], session: date) -> int | None:
    for i in range(len(days) - 1, -1, -1):
        if days[i] == session:
            return i
        if days[i] < session:
            return None
    return None


def run(as_of: date | None) -> dict[str, Any]:
    tickers, universe_source = load_constituents()
    charts: dict[str, list[tuple[date, float]]] = {}
    failures: list[dict[str, str]] = []
    fetch_list = list(tickers)
    if "SPY" not in fetch_list:
        fetch_list.append("SPY")
    if "^GSPC" not in fetch_list:
        fetch_list.append("^GSPC")

    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = [pool.submit(fetch_chart, t) for t in fetch_list]
        for fut in as_completed(futs):
            ticker, pairs, err = fut.result()
            if err or not pairs:
                failures.append({"ticker": ticker, "error": err or "empty"})
            else:
                charts[ticker] = pairs

    spy_pairs = charts.pop("SPY", None) if "SPY" not in tickers else charts.get("SPY")
    gspc_pairs = charts.pop("^GSPC", None)
    ticker_set = set(tickers)
    constituent_charts = {t: p for t, p in charts.items() if t in ticker_set}
    fail_constituents = [f for f in failures if f["ticker"] not in {"SPY", "^GSPC"}]

    if len(constituent_charts) < MIN_OK:
        raise RuntimeError(
            f"only {len(constituent_charts)}/{len(tickers)} Yahoo charts ok "
            f"(need ≥{MIN_OK}); sample errors: {fail_constituents[:8]}"
        )

    latest_available = max(pairs[-1][0] for pairs in constituent_charts.values())
    target = as_of or latest_available
    if target > latest_available:
        target = latest_available

    calendar_charts = dict(constituent_charts)
    if spy_pairs:
        calendar_charts["SPY"] = spy_pairs
    as_of_used, week_as_of = _session_dates(calendar_charts, target)
    prior_week_as_of = None
    if spy_pairs:
        prior_idx = _idx_on_or_before([p[0] for p in spy_pairs], week_as_of - timedelta(days=7))
        if prior_idx is not None:
            prior_week_as_of = spy_pairs[prior_idx][0]

    now_rows: list[dict[str, Any]] = []
    week_rows: list[dict[str, Any]] = []
    skipped_as_of = 0
    skipped_week = 0

    for pairs in constituent_charts.values():
        days = [p[0] for p in pairs]
        closes = [p[1] for p in pairs]
        idx = _index_on_date(days, as_of_used)
        if idx is None:
            skipped_as_of += 1
            continue
        snap = snapshot_one(closes, idx)
        if snap:
            now_rows.append(snap)
        widx = _index_on_date(days, week_as_of)
        if widx is None:
            widx = _idx_on_or_before(days, week_as_of)
            if widx is None or (week_as_of - days[widx]).days > 4:
                skipped_week += 1
                continue
        wsnap = snapshot_one(closes, widx)
        if wsnap:
            week_rows.append(wsnap)

    now = aggregate(now_rows)
    week = aggregate(week_rows) if week_rows else None

    delta = {
        "advancers": (now["advancers"] - week["advancers"]) if week else None,
        "decliners": (now["decliners"] - week["decliners"]) if week else None,
        "nh_nl_net": (now["nh_nl_net"] - week["nh_nl_net"]) if week else None,
        "pct_above_50dma": _pp_delta(
            now.get("pct_above_50dma"), (week or {}).get("pct_above_50dma")
        ),
        "pct_above_200dma": _pp_delta(
            now.get("pct_above_200dma"), (week or {}).get("pct_above_200dma")
        ),
    }

    index_pairs = gspc_pairs or spy_pairs
    top10 = compute_top10_contribution(
        constituent_charts,
        index_pairs,
        as_of_used,
        week_as_of,
        prior_week_as_of,
    )
    if top10.get("error"):
        warnings_pre = [f"top10 contribution: {top10['error']}"]
    else:
        warnings_pre = []

    hom = fetch_hom_cross_check(as_of_used)
    warnings: list[str] = list(warnings_pre)
    if hom:
        for key, hom_key in (
            ("pct_above_50dma", "pct_above_50dma"),
            ("pct_above_200dma", "pct_above_200dma"),
        ):
            ours = now.get(key)
            theirs = hom.get(hom_key)
            if isinstance(ours, (int, float)) and isinstance(theirs, (int, float)):
                if abs(ours - theirs) >= 15:
                    warnings.append(
                        f"{key} computed {ours} vs historyofmarket {theirs} "
                        f"(hom as_of {hom.get('as_of')}; methodology gap is normal below ~15ppt)"
                    )

    return {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "universe": "S&P 500 constituents",
        "universe_source": universe_source,
        "universe_n": len(tickers),
        "ok_n": len(constituent_charts),
        "fail_n": len(fail_constituents),
        "failures_sample": fail_constituents[:12],
        "skipped_as_of": skipped_as_of,
        "skipped_week_ago": skipped_week,
        "price_source": "Yahoo Finance chart v8 (daily close)",
        "as_of": as_of_used.isoformat(),
        "week_ago_as_of": week_as_of.isoformat() if week_as_of else None,
        "index_proxy": "^GSPC" if gspc_pairs else "SPY",
        "now": now,
        "week_ago": week,
        "change_1w": delta,
        "top10_contribution": top10,
        "cross_check": hom,
        "warnings": warnings,
        "report": build_report_strings(now, delta, top10),
        "notes": [
            "A/D and NH/NL are S&P 500 members, not NYSE composite.",
            "New high/low: close at/through the max/min of the prior 252 sessions.",
            "DMA% uses simple moving average of daily closes.",
            "StockCharts/Barchart/historyofmarket DMA series can differ by several ppt; use this script as source of record.",
            "Top10 contribution uses current Slickcharts weights × 1W returns (weight snapshot is not point-in-time).",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch S&P 500 breadth for weekly scan §3")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument(
        "--as-of",
        dest="as_of",
        default=None,
        help="Session date YYYY-MM-DD (default: latest Yahoo bar)",
    )
    args = parser.parse_args()

    as_of = None
    if args.as_of:
        try:
            as_of = datetime.strptime(args.as_of, "%Y-%m-%d").date()
        except ValueError:
            print("Error: --as-of must be YYYY-MM-DD", file=sys.stderr)
            sys.exit(1)

    try:
        results = run(as_of)
    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    now = results["now"]
    delta = results["change_1w"]
    print(f"S&P 500 breadth (UTC {results['fetched_at']})")
    print(f"  universe={results['universe_n']} ok={results['ok_n']} as_of={results['as_of']}")
    print(
        f"- Advancers/decliners: {now['advancers']} / {now['decliners']}"
        f"  A/D={now['ad_ratio']}  1W Δ 涨{delta['advancers']:+d}/跌{delta['decliners']:+d}"
        if delta.get("advancers") is not None
        else f"- Advancers/decliners: {now['advancers']} / {now['decliners']}  A/D={now['ad_ratio']}"
    )
    print(
        f"- NH/NL: {now['new_highs']} / {now['new_lows']}  net={now['nh_nl_net']:+d}"
        + (
            f"  1W Δ net {delta['nh_nl_net']:+d}"
            if delta.get("nh_nl_net") is not None
            else ""
        )
    )
    p50 = now.get("pct_above_50dma")
    p200 = now.get("pct_above_200dma")
    d50 = delta.get("pct_above_50dma")
    d200 = delta.get("pct_above_200dma")
    print(
        f"- >50DMA: {p50}%  1W Δ {d50:+.1f}ppt"
        if d50 is not None
        else f"- >50DMA: {p50}%"
    )
    print(
        f"- >200DMA: {p200}%  1W Δ {d200:+.1f}ppt"
        if d200 is not None
        else f"- >200DMA: {p200}%"
    )
    top10 = results.get("top10_contribution") or {}
    if top10.get("report"):
        print(f"- Top10 contrib: {top10['report']}")
        if top10.get("report_1w") and top10["report_1w"] != "—":
            print(f"  1W Δ {top10['report_1w']}")
    elif top10.get("error"):
        print(f"- Top10 contrib: ERROR — {top10['error']}")
    hom = results.get("cross_check")
    if hom:
        print(
            f"- Cross-check (historyofmarket {hom.get('as_of')}): "
            f">50DMA {hom.get('pct_above_50dma')}%  >200DMA {hom.get('pct_above_200dma')}%"
        )
    for warn in results.get("warnings") or []:
        print(f"WARNING: {warn}")


if __name__ == "__main__":
    main()
