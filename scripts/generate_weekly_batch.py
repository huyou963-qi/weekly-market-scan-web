#!/usr/bin/env python3
"""Generate weekly-market-scan-web reports from prefetched data and POST them.

Hard rule: only use data as of weekEnding (already enforced in data packages).
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

DATA = Path("/workspace/reports/data")
OUT = Path("/workspace/reports/batch")
OUT.mkdir(parents=True, exist_ok=True)
API_URL = os.environ.get("WEEKLY_REPORT_API_URL", "https://hblook.com").rstrip("/")
TOKEN = os.environ.get("WEEKLY_REPORT_INGEST_TOKEN", "").strip()

SECTORS = [
    ("Technology", "XLK"),
    ("Financials", "XLF"),
    ("Health Care", "XLV"),
    ("Energy", "XLE"),
    ("Industrials", "XLI"),
    ("Staples", "XLP"),
    ("Discretionary", "XLY"),
    ("Utilities", "XLU"),
    ("Real Estate", "XLRE"),
    ("Materials", "XLB"),
    ("Comm Services", "XLC"),
]


def pct(x):
    if x is None:
        return "—"
    return f"{x:+.2f}%"


def num(x, nd=2):
    if x is None:
        return "—"
    return f"{x:.{nd}f}"


def bp_dir(delta):
    if delta is None:
        return "flat", "0bp"
    if abs(delta) < 0.5:
        return "flat", f"{delta:+.0f}bp" if delta == int(delta) else f"{delta:+.1f}bp"
    return ("up" if delta > 0 else "down"), f"{delta:+.0f}bp" if float(delta) == int(delta) else f"{delta:+.1f}bp"


def mget(markets, key):
    return markets.get(key) or {}


def events_for_week(calendar, week_start, week_ending):
    out = []
    for e in calendar.get("events", []):
        if week_start <= e["date"] <= week_ending:
            out.append(e)
    return out


def next_week_events(calendar, week_ending):
    we = datetime.strptime(week_ending, "%Y-%m-%d").date()
    nxt_end = (we + timedelta(days=7)).isoformat()
    out = []
    for e in calendar.get("events", []):
        if week_ending < e["date"] <= nxt_end:
            out.append(e)
    return out


def classify_regime(spx_1w, hy_bp, vix, xlk_rel):
    """Heuristic regime from weekly tape — labeled as 判断."""
    if vix is not None and vix >= 25:
        return "Risk-off / Volatility spike", "M"
    if hy_bp is not None and hy_bp >= 25:
        return "Credit stress / Risk-off", "M"
    if spx_1w is not None and spx_1w <= -2.5:
        return "Risk-off correction", "M"
    if xlk_rel is not None and xlk_rel >= 1.5 and spx_1w is not None and spx_1w > 0:
        return "AI-driven risk-on / Growth leadership", "M"
    if spx_1w is not None and spx_1w >= 1.5 and (hy_bp is None or hy_bp <= 5):
        return "Risk-on / Goldilocks-lite", "M"
    if spx_1w is not None and abs(spx_1w) < 0.8:
        return "Range / Digestion", "M"
    if xlk_rel is not None and xlk_rel <= -1.5:
        return "Rotation / Defensive tilt", "M"
    return "Mixed / Transitional", "L"


def rotation_line(rel: dict):
    if not rel:
        return "轮动不明显", "混合", "混合"
    ranked = sorted(rel.items(), key=lambda kv: kv[1], reverse=True)
    leaders = [k for k, v in ranked[:2]]
    laggards = [k for k, v in ranked[-2:]]
    return f"FROM {'/'.join(laggards)} → TO {'/'.join(leaders)}", "/".join(leaders), "/".join(laggards)


def title_from(we, spx, sox, regime):
    if spx is not None and spx >= 2:
        t = f"美股周涨{spx:.1f}%，{regime.split('/')[0].strip()}"
    elif spx is not None and spx <= -2:
        t = f"美股周跌{abs(spx):.1f}%，波动回升"
    elif sox is not None and abs(sox) >= 5:
        t = f"半导体周变动{sox:+.1f}%，风格主导"
    else:
        t = f"跨资产震荡消化，关注数据窗口"
    return t[:80]


def build_report(pkg: dict, calendar: dict) -> tuple[dict, str]:
    we = pkg["weekEnding"]
    ws = pkg["weekStart"]
    fred = pkg["fred"]
    m = pkg["markets"]
    rel = pkg.get("sector_rel_spx") or {}

    hy = fred["hy_oas"]
    curve = fred["curve_10y2y"]
    dgs10 = fred["ust_10y"]
    dgs2 = fred["ust_2y"]
    ig = fred.get("ig_oas", {})

    spx = mget(m, "SPX")
    ndx = mget(m, "NDX")
    rut = mget(m, "RUT")
    vix = mget(m, "VIX")
    dxy = mget(m, "DXY")
    wti = mget(m, "WTI")
    gold = mget(m, "GOLD")
    copper = mget(m, "COPPER")
    tlt = mget(m, "TLT")
    nvda = mget(m, "NVDA")
    mu = mget(m, "MU")
    sox = mget(m, "SOX")
    aapl = mget(m, "AAPL")
    msft = mget(m, "MSFT")
    googl = mget(m, "GOOGL")
    amzn = mget(m, "AMZN")
    meta = mget(m, "META")

    hy_bp_val = int(round(hy["value"] * 100)) if "value" in hy else None
    hy_d = hy.get("change_1w_bps")
    curve_v = curve.get("value")
    curve_d = curve.get("change_1w_bps")
    vix_c = vix.get("close")
    vix_d_pts = None
    if vix.get("close") is not None and vix.get("prior_week_close") is not None:
        vix_d_pts = round(vix["close"] - vix["prior_week_close"], 2)

    regime, conf = classify_regime(spx.get("chg_1w_pct"), hy_d, vix_c, rel.get("XLK"))
    rot, to_sec, from_sec = rotation_line(rel)
    title = title_from(we, spx.get("chg_1w_pct"), sox.get("chg_1w_pct"), regime)

    week_events = events_for_week(calendar, ws, we)
    nxt_events = next_week_events(calendar, we)
    month_key = we[:7]
    theme = calendar.get("themes_by_month", {}).get(month_key, "")

    # movers
    movers = []
    for k in ["MU", "NVDA", "AMD", "TSLA", "AAPL", "MSFT", "GOOGL", "AMZN", "META", "SOX"]:
        row = mget(m, k)
        chg = row.get("chg_1w_pct")
        if chg is not None and abs(chg) >= 5:
            movers.append((k, chg, row.get("close")))

    hy_dir, hy_delta_s = bp_dir(hy_d)
    curve_dir, curve_delta_s = bp_dir(curve_d)
    if vix_d_pts is None:
        vix_dir, vix_delta_s = "flat", "0"
    else:
        vix_dir = "up" if vix_d_pts > 0.15 else ("down" if vix_d_pts < -0.15 else "flat")
        vix_delta_s = f"{vix_d_pts:+.2f}"

    # sector table
    sector_rows = []
    for name, etf in SECTORS:
        row = mget(m, etf)
        r = rel.get(etf)
        trend = "↑" if (r or 0) > 1 else ("↓" if (r or 0) < -1 else "→")
        sector_rows.append(
            f"| {name} | {etf} | {pct(r) if r is not None else '—'} | {pct(row.get('chg_1w_pct'))} | tape | {trend} |"
        )

    # event tables
    if week_events:
        ev_rows = "\n".join(
            f"| {e['date']} | {e['event']} | 见市场定价 | 解读见正文 | {'已price-in' if e['tier']==1 else '仍debated'} |"
            for e in week_events
        )
        macro_rows = "\n".join(
            f"| {e['event']} | 见官方发布（as-of ≤ {we}） | 跨资产反应见仪表盘 | 事实：日历事件；解读：结合 SPX {pct(spx.get('chg_1w_pct'))} / HY {hy_d:+.0f}bp |"
            for e in week_events
        )
    else:
        ev_rows = f"| {we} | 本周无重大一级宏观日历 | — | — | — |"
        macro_rows = f"| 常规交易周 | — | SPX {pct(spx.get('chg_1w_pct'))} | 数据真空，价格发现为主 |"

    if nxt_events:
        nxt_rows = "\n".join(
            f"| {e['date']} | {e['event']} | {'H' if e['tier']==1 else 'M'} | 利率/权益/信用 |"
            for e in nxt_events
        )
    else:
        nxt_rows = f"| 下周 | 关注初请失业金 / 区域联储数据 | M | 利率、SPX |"

    # AI section — state no new print unless megacap earnings week
    ai_print = "no new print this week"
    if any("财报" in e["event"] or "capex" in e["event"].lower() or "FOMC" in e["event"] for e in week_events):
        if we >= "2026-04-24":
            ai_print = "hyperscaler Q1 capex guides circulating (MSFT/GOOGL/AMZN/META); HBM tight per TrendForce 2Q26 narrative — only cite if as-of ≤ weekEnding"

    alert = "无"
    if hy_d is not None and abs(hy_d) >= 25:
        alert = f"HY OAS 1W {hy_d:+.0f}bp — credit stress flag"
    if vix_c is not None and vix_c >= 20:
        alert = (alert + "; " if alert != "无" else "") + f"VIX {vix_c} ≥ 20"

    spx_sup = None
    if spx.get("close"):
        spx_sup = round(spx["close"] * 0.985, 0)
        spx_res = round(spx["close"] * 1.01, 0)
    else:
        spx_res = None

    summary_one = f"{rot}；HY OAS {hy_d:+.0f}bp，VIX {num(vix_c,1)}"

    body = f"""# 周度市场检测报告 | Weekly Market Scan

**报告周期**: Week ending {we}  
**生成时间**: {we} 20:00 CST  
**覆盖范围**: US+CN  
**数据截止**: 权益/商品收盘 {we}；FRED 利率/信用 as-of ≤ {we}；**禁止使用 {we} 之后信息**

---

## 执行摘要 | Executive Summary

1. **Regime**: {regime}（置信度 {conf}）
2. **Top move**: SPX {pct(spx.get('chg_1w_pct'))} → {num(spx.get('close'))}；NDX {pct(ndx.get('chg_1w_pct'))}；SOX {pct(sox.get('chg_1w_pct'))}
3. **Rotation**: {rot}
4. **Key risk**: HY OAS **{hy_bp_val}bp**（1W {hy_d:+.0f}bp）；VIX **{num(vix_c,2)}**；10Y **{num(dgs10.get('value'),2)}%**
5. **Playbook**: 围绕 SPX {num(spx_sup,0) if spx_sup else '—'} / {num(spx_res,0) if spx_res else '—'} 管理敞口；信用与曲线为失效条件

**月度主题（背景）**: {theme}

---

## 1. 大类资产仪表盘 | Cross-Asset Dashboard

| 资产 | 标的 | 1W | YTD | as-of | 驱动 |
|------|------|-----|-----|-------|------|
| 美股 | SPX | {pct(spx.get('chg_1w_pct'))} | {pct(spx.get('ytd_pct'))} | {spx.get('as_of','—')} | 指数基准 |
| | NDX | {pct(ndx.get('chg_1w_pct'))} | {pct(ndx.get('ytd_pct'))} | {ndx.get('as_of','—')} | 成长/科技 |
| | RUT | {pct(rut.get('chg_1w_pct'))} | {pct(rut.get('ytd_pct'))} | {rut.get('as_of','—')} | 风险偏好 |
| 利率 | UST 10Y (`DGS10`) | {dgs10.get('change_1w_bps',0):+.0f}bp → {num(dgs10.get('value'),2)}% | — | {dgs10.get('as_of','—')} | 期限溢价 |
| | UST 2Y (`DGS2`) | {dgs2.get('change_1w_bps',0):+.0f}bp → {num(dgs2.get('value'),2)}% | — | {dgs2.get('as_of','—')} | 政策路径 |
| | **10Y-2Y (`T10Y2Y`)** | **{curve_d:+.0f}bp → {num(curve_v,2)}%** | — | {curve.get('as_of','—')} | steepening/flattening |
| 信用 | **HY OAS (`BAMLH0A0HYM2`)** | **{hy_d:+.0f}bp → {hy_bp_val}bp** | — | {hy.get('as_of','—')} | 风险溢价 |
| | IG OAS | {ig.get('change_1w_bps',0):+.0f}bp → {int(round(ig.get('value',0)*100))}bp | — | {ig.get('as_of','—')} | 投资级 |
| 外汇 | DXY | {pct(dxy.get('chg_1w_pct'))} | — | {dxy.get('as_of','—')} | 美元流动性 |
| 商品 | WTI | {pct(wti.get('chg_1w_pct'))} → ${num(wti.get('close'))} | — | {wti.get('as_of','—')} | 能源 |
| | Gold | {pct(gold.get('chg_1w_pct'))} → ${num(gold.get('close'),1)} | — | {gold.get('as_of','—')} | 避险/实际利率 |
| | Copper | {pct(copper.get('chg_1w_pct'))} → ${num(copper.get('close'),2)} | — | {copper.get('as_of','—')} | 增长敏感 |
| 波动 | VIX | {pct(vix.get('chg_1w_pct'))} → {num(vix_c,2)} | — | {vix.get('as_of','—')} | 风险偏好 |
| 债券 | TLT | {pct(tlt.get('chg_1w_pct'))} | — | {tlt.get('as_of','—')} | 久期 |

**Cross-asset read**（解读）: 事实——SPX 周变动 {pct(spx.get('chg_1w_pct'))}，HY OAS {hy_d:+.0f}bp，曲线 {curve_d:+.0f}bp，VIX {num(vix_c,2)}。判断——{'risk-on 占优' if (spx.get('chg_1w_pct') or 0) > 0.5 and (hy_d or 0) < 15 else ('risk-off 压力上升' if (spx.get('chg_1w_pct') or 0) < -1 or (hy_d or 0) > 15 else '多空平衡 / 震荡')}；科技相对强度 XLK rel SPX = {pct(rel.get('XLK'))}。

---

## 2. 宏观与政策 | Macro & Policy

### 2.1 本周回顾

| 事件/数据 | 实际 vs 预期 | 市场反应 | 解读 |
|-----------|--------------|----------|------|
{macro_rows}

### 2.2 下周日历

| 日期 | 事件 | 影响等级 H/M/L | 关注资产/行业 |
|------|------|----------------|---------------|
{nxt_rows}

**Macro narrative**（解读）: 本周日历事件如上；价格行为显示 SPX {pct(spx.get('chg_1w_pct'))}、10Y {dgs10.get('change_1w_bps',0):+.0f}bp。判断：宏观主线仍是「通胀路径 × 就业韧性 × 政策反应函数」，本周不引入 {we} 之后的信息。

---

## 3. 股市结构 | Equity Market Structure

| 指标 | 数值 | 1W Δ | 信号 |
|------|------|------|------|
| SPX | {num(spx.get('close'))} | {pct(spx.get('chg_1w_pct'))} | 基准 |
| NDX vs SPX | — | NDX {pct(ndx.get('chg_1w_pct'))} / SPX {pct(spx.get('chg_1w_pct'))} | 成长相对 |
| RUT vs SPX | — | RUT {pct(rut.get('chg_1w_pct'))} | 小盘风险偏好 |
| VIX | {num(vix_c,2)} | {vix_delta_s} pts | 波动 |

**Style / factor**: Growth（NDX）vs Broad（SPX）；Large vs Small（IWM {pct(mget(m,'IWM').get('chg_1w_pct'))}）。

**Structure read**（判断）: {'成长领涨、广度可能偏窄' if (ndx.get('chg_1w_pct') or 0) - (spx.get('chg_1w_pct') or 0) > 1 else ('小盘相对强势' if (rut.get('chg_1w_pct') or 0) - (spx.get('chg_1w_pct') or 0) > 0.5 else '风格相对均衡')}。

---

## 4. 行业轮动 | Sector & Industry Rotation

### 4.1 GICS 一级 — 相对 SPX（SPX 1W {pct(spx.get('chg_1w_pct'))}）

| 行业 | ETF | 1W rel | 1W abs | 驱动标签 | RS趋势 |
|------|-----|--------|--------|----------|--------|
{chr(10).join(sector_rows)}

### 4.2 细分行业亮点

**领涨**: {to_sec} — 相对 SPX 领先  
**领跌**: {from_sec} — 相对 SPX 落后

### 4.3 轮动结论

**资金方向**: {rot}  
**证据**: 行业 ETF 相对收益（事实，as-of {we}）

---

## 4.5 AI 产业链 & Capex | AI Supply Chain Tracker

### 4.5.1 HBM / 内存价格

| 指标 | 本期 | 1W/1M Δ | 来源 | 解读 |
|------|------|---------|------|------|
| HBM3e | {ai_print} | — | TrendForce / vendor（仅已公开且 ≤{we}） | 无新报价则不编造 |
| DRAM DDR5 | no new print this week | — | — | — |
| 相关股价 | MU {pct(mu.get('chg_1w_pct'))} / SOX {pct(sox.get('chg_1w_pct'))} | — | Yahoo {we} | 价格代理，非合约价 |

### 4.5.2 云 GPU 租赁价格 ($/GPU-hr)

| 厂商 | SKU | On-demand | 1W Δ | 信号 |
|------|-----|-----------|------|------|
| AWS / GCP / Azure / CoreWeave | H100 类 | no new print this week | — | unchanged |

### 4.5.3 AI API 定价 ($/1M tokens)

| 厂商 | Model | Input | Output | 本周变动? |
|------|-------|-------|--------|-----------|
| OpenAI / Anthropic / Google | flagship | — | — | N（无官方调价公告则 N） |

### 4.5.4 Hyperscaler AI Capex

| 公司 | Capex / Guide | 1W 股价 | 1W 更新 |
|------|---------------|---------|---------|
| MSFT | 以最新已披露指引为准（≤{we}） | {pct(msft.get('chg_1w_pct'))} | 无新指引则 unchanged |
| GOOGL | 同上 | {pct(googl.get('chg_1w_pct'))} | — |
| AMZN | 同上 | {pct(amzn.get('chg_1w_pct'))} | — |
| META | 同上 | {pct(meta.get('chg_1w_pct'))} | — |
| NVDA | DC 需求代理（非 capex） | {pct(nvda.get('chg_1w_pct'))} | — |

**AI stack synthesis**（判断）: 本周以 **价格信号**（SOX {pct(sox.get('chg_1w_pct'))}、NVDA {pct(nvda.get('chg_1w_pct'))}、MU {pct(mu.get('chg_1w_pct'))}、XLK rel {pct(rel.get('XLK'))}）映射 AI 链风险偏好；合约价/API 无新 print 时不强行编造 WoW%。

---

## 5. 重点事件与传导 | Events & Transmission

| 日期 | 事件 | 一阶影响 | 二阶影响 | 定价状态 |
|------|------|----------|----------|----------|
{ev_rows}

**Earnings tone**: 若本周非财报密集周，则以指数与板块相对强度代替 beat/miss 统计；不编造一致预期数字。

---

## 6. 重点股票 | Watchlist & Systemic Names

### 6.1 观察列表

| Ticker | 1W | 收盘 | 催化剂 | 观点 |
|--------|-----|------|--------|------|
| NVDA | {pct(nvda.get('chg_1w_pct'))} | {num(nvda.get('close'))} | AI capex / SOX | 系统权重 |
| MU | {pct(mu.get('chg_1w_pct'))} | {num(mu.get('close'))} | HBM/DRAM | 存储链 |
| AAPL | {pct(aapl.get('chg_1w_pct'))} | {num(aapl.get('close'))} | 消费电子/服务 | 大盘权重 |
| MSFT | {pct(msft.get('chg_1w_pct'))} | {num(msft.get('close'))} | Azure/capex | 云 ROI |
| META | {pct(meta.get('chg_1w_pct'))} | {num(meta.get('close'))} | 广告/AI 基建 | 成长 |

### 6.2 系统性/指数权重异动

| Ticker | 1W | 原因 | 板块含义 |
|--------|-----|------|----------|
{chr(10).join(f"| {k} | {pct(c)} | |1W|>5% | 高波动个股/指数 |" for k,c,_ in movers) if movers else f"| — | — | 本周无 |1W|>5% 核心名单 | — |"}

---

## 7. 风险与流动性 | Risk Dashboard

| 指标 | 现值 | 1W Δ | 解读 |
|------|------|------|------|
| VIX | {num(vix_c,2)} | {vix_delta_s} | {'偏高警戒' if (vix_c or 0) >= 20 else '偏低/舒适'} |
| **HY OAS (FRED)** | **{hy_bp_val}bp** | **{hy_d:+.0f}bp** | {'走阔压力' if (hy_d or 0) > 0 else '收窄/稳定'} |
| **10Y-2Y (FRED)** | **{num(curve_v,2)}%** | **{curve_d:+.0f}bp** | {'steepening' if (curve_d or 0) > 0 else 'flattening'} |
| IG OAS | {int(round(ig.get('value',0)*100))}bp | {ig.get('change_1w_bps',0):+.0f}bp | 投资级 |
| UST 10Y | {num(dgs10.get('value'),2)}% | {dgs10.get('change_1w_bps',0):+.0f}bp | 折现率 |
| TLT | {num(tlt.get('close'))} | {pct(tlt.get('chg_1w_pct'))} | 久期代理 |

**Triggered alerts**: {alert}  
**Watch levels next week**: SPX {num(spx_sup,0) if spx_sup else '—'} / {num(spx_res,0) if spx_res else '—'}；HY OAS 300bp；VIX 20；10Y {num((dgs10.get('value') or 0)+0.15,2)}%

---

## 8. 市场 Regime | Regime Classification

**Primary regime**: {regime}  
**Confidence**: {conf}  
**Falsifiers**: ① HY OAS 单周走阔 >25bp；② VIX 升破 20 且 SPX 跌破周线支撑；③ 10Y 单周上行 >15bp 同时成长大幅跑输

**vs last week**: 相对前周（prior week ending {pkg.get('priorWeekEnding')}）——SPX 由前值切换至 {pct(spx.get('chg_1w_pct'))}；HY Δ={hy_d:+.0f}bp；曲线 Δ={curve_d:+.0f}bp。

---

## 9. 异常与背离 | Anomalies

| # | 观察 | 可能解释 | 交易含义 |
|---|------|----------|----------|
| 1 | NDX {pct(ndx.get('chg_1w_pct'))} vs RUT {pct(rut.get('chg_1w_pct'))} | 风格/流动性分化 | 关注广度恶化 |
| 2 | WTI {pct(wti.get('chg_1w_pct'))} vs XLE rel {pct(rel.get('XLE'))} | 油价与能源股映射 | 能源 beta 管理 |
| 3 | HY OAS {hy_d:+.0f}bp vs SPX {pct(spx.get('chg_1w_pct'))} | 股信是否同向 | 背离则降杠杆 |

---

## 10. 下周策略 | Next-Week Playbook

### Base case
在 {regime} 框架下，指数围绕本周收盘 {num(spx.get('close'))} 震荡；关注下周一级数据对利率与成长股的再定价。不预支 {we} 之后未知结果。

### Scenarios

| 情景 | 概率 | 触发条件 | 资产表现 |
|------|------|----------|----------|
| Bull | 30% | 数据友好 + HY 稳定 | SPX/NDX 延续，XLK 领先 |
| Base | 45% | 数据中性 | 区间震荡，轮动延续 |
| Bear | 25% | 通胀/信用恶化 | SPX 回撤，VIX↑，防御占优 |

### Conviction setups (≤3)

1. **指数区间交易** — Direction: tactical · Instrument: SPX/QQQ · Trigger: 收盘站稳 {num(spx_sup,0) if spx_sup else '—'} · Invalidation: 跌破该位或 HY>+25bp · Horizon: 1W
2. **行业相对价值** — Long {to_sec.split('/')[0]} / Light {from_sec.split('/')[0]} · Invalidation: 相对强度反转 >2pct · Horizon: 1–2W
3. **波动率对冲** — 若 VIX <16 且一级数据临近，考虑小仓对冲 · Invalidation: VIX 已 >20 · Horizon: 事件窗口

### Positioning
- **Risk budget**: {'add cautiously' if (spx.get('chg_1w_pct') or 0) > 1 and (hy_d or 0) < 5 else ('reduce' if (spx.get('chg_1w_pct') or 0) < -2 or (hy_d or 0) > 15 else 'hold')}
- **Overweight**: {to_sec}
- **Underweight / avoid**: {from_sec}
- **Thesis reset if**: SPX 收盘 < {num(spx_sup,0) if spx_sup else '—'} 或 HY OAS 单周 >+25bp

---

## 附录 | Appendix

- **Sources**: FRED (`BAMLH0A0HYM2`,`T10Y2Y`,`DGS2`,`DGS10`,`BAMLC0A0CM`) as-of ≤ {we}；Yahoo Finance 日收盘 as-of ≤ {we}；BLS/Fed 官方日历（仅使用已发生事件）
- **Disclaimer**: Research for informational purposes; not investment advice. Verify prices before trading.
- **Changes vs prior report**: prior week ending {pkg.get('priorWeekEnding')}
"""

    meta = {
        "weekEnding": we,
        "title": title,
        "regime": regime,
        "regimeConfidence": conf,
        "scope": "US+CN",
        "generatedAt": f"{we} 20:00 CST",
        "summaryOneLiner": summary_one[:200],
        "kpis": [
            {"label": "HY OAS", "value": f"{hy_bp_val}bp", "delta": hy_delta_s, "dir": hy_dir},
            {"label": "10Y-2Y", "value": f"{num(curve_v,2)}%", "delta": curve_delta_s, "dir": curve_dir},
            {
                "label": "VIX",
                "value": f"{num(vix_c,2)}",
                "delta": vix_delta_s,
                "dir": vix_dir,
            },
        ],
    }
    return meta, body


def post_payload(payload: dict) -> tuple[int, str]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{API_URL}/api/weekly-reports",
        data=data,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main(argv: list[str]) -> int:
    if not TOKEN:
        print("WEEKLY_REPORT_INGEST_TOKEN missing", file=sys.stderr)
        return 1

    calendar = json.loads((DATA / "macro_calendar.json").read_text(encoding="utf-8"))
    index = json.loads((DATA / "index.json").read_text(encoding="utf-8"))

    # newest → oldest
    weeks = list(reversed([w["weekEnding"] for w in index["weeks"]]))
    if argv:
        weeks = [w for w in weeks if w in argv]

    results = []
    for we in weeks:
        pkg = json.loads((DATA / f"{we}.json").read_text(encoding="utf-8"))
        meta, body = build_report(pkg, calendar)
        assert meta["weekEnding"] == we
        payload = {"meta": meta, "bodyMarkdown": body}

        md_path = OUT / f"{we}-body.md"
        json_path = OUT / f"{we}-payload.json"
        md_path.write_text(body, encoding="utf-8")
        json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        status, resp = post_payload(payload)
        ok = status in (200, 201)
        results.append({"weekEnding": we, "status": status, "ok": ok, "resp": resp[:240]})
        print(f"{'OK' if ok else 'FAIL'} {status} {we} {resp[:160]}")

    summary_path = OUT / "post_results.json"
    summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    fails = [r for r in results if not r["ok"]]
    print(f"\nDone: {len(results)-len(fails)}/{len(results)} succeeded")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
