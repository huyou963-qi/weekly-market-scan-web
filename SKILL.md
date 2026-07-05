---
name: weekly-market-scan-web
description: >-
  Weekly cross-asset market scan for finance-site web delivery: same trader-grade
  analysis as weekly-market-scan, but outputs bodyMarkdown + list meta and POSTs
  to hblook.com /weekly. Use for Cursor Automation that publishes weekly reports
  to the site (周度市场观察, 每周观察, weekly report ingest, Demo B meta).
disable-model-invocation: true
---

# Weekly Market Scan — Web

Produce a **trader-grade weekly market brief** and **publish it to finance-site** (`/weekly`).

Output is always two parts (Demo B):

| Part | Purpose | Template |
|------|---------|----------|
| `meta` | 列表页：日期、标题、regime、KPI chips | [report-meta.json](templates/report-meta.json) |
| `bodyMarkdown` | 详情页：完整周报正文 | [weekly-report.md](templates/weekly-report.md) |

**Do not** generate Slack summaries, WeChat push copy, or channel-specific formats. The website is the sole delivery channel.

Default market scope: **global macro + US equities**. **Out of scope**: A-share (A股) and Hong Kong equities (港股) — do not fetch, analyze, or report CSI 300, HSI, AH names, or CN/HK-specific narratives unless the user explicitly overrides.

---

## Scan workflow (checklist)

Copy and track progress:

```
Weekly Scan (Web) Progress:
- [ ] 0. Scope & period anchor
- [ ] 1a. FRED pull (HY OAS + 10Y-2Y) — MCP or scripts/fetch_fred.py
- [ ] 1. Cross-asset dashboard
- [ ] 2. Macro & policy recap
- [ ] 2b. Macro news & speeches recall (2.1.2)
- [ ] 3. Equity market structure
- [ ] 4. Sector & industry rotation
- [ ] 4.5. AI supply chain (HBM, cloud GPU, API pricing, capex)
- [ ] 5. Key events & catalyst map
- [ ] 6. Watchlist & systemic names
- [ ] 7. Risk & liquidity dashboard
- [ ] 8. Regime & cross-asset signals
- [ ] 9. Anomalies & divergences
- [ ] 10. Next-week playbook
- [ ] 11. Quality gate
- [ ] 12. Build meta + POST to site
```

### Step 0 — Scope & period anchor

- **Period**: prior trading week (Mon open → Fri close) in user's timezone; if run on weekend, label "week ending [date]".
- **Benchmarks**: S&P 500, Nasdaq, Russell 2000 (or user-specified).
- **Out of scope**: A-share (A股) and Hong Kong equities (港股) — no CSI 300 / HSI coverage, no CN/HK stock narratives.
- **Universe extras**: user watchlist, index top weights, names with >5% weekly move or >2σ volume.
- **Prior week carry-over**: if memory or last report exists, note unresolved themes.

### Step 1a — FRED data pull (mandatory)

Fetch **before** filling credit/curve fields. Full spec: [fred-data.md](reference/fred-data.md).

**Priority**: FRED MCP → `python scripts/fetch_fred.py --json` → FRED REST → proxy (label as proxy).

| Series | FRED ID | Report as |
|--------|---------|-----------|
| HY OAS | `BAMLH0A0HYM2` | level (bp) + 1W Δ (bp) |
| 10Y-2Y spread | `T10Y2Y` | level (%) + 1W Δ (bp) |
| UST 2Y / 10Y | `DGS2` / `DGS10` | context in Step 1 |

**API key**: `FRED_API_KEY` env or MCP server env — never hardcode in skill files or reports.

If FRED unavailable after all paths: write `FRED 未连接` and use HYG/LQD ETF spread as **proxy only**.

### Step 2 — Macro & policy recap

**2.1 本周回顾** has two parts — both mandatory:

| Subsection | Content |
|------------|---------|
| **2.1.1 数据发布** | Scheduled prints (NFP, CPI, PMI, etc.) — actual vs consensus, market reaction |
| **2.1.2 要闻、讲话与政策动态** | Speeches, forums, policy/geopolitical headlines that moved cross-asset prices same day |

Full inclusion rules, thresholds, and research workflow: [macro-news-recall.md](reference/macro-news-recall.md).

Before writing 2.1: web-search the week's **speaker calendars + major headlines**; cross-check ≥2 sources; link same-day moves in rates/FX/vol/equities. Example: Fed official at **ECB Forum** mid-week → row in 2.1.2 even when no data release that day.

**2.1.2 silence**: if nothing meets threshold, state explicitly under the subsection — do not omit the header.

**2.2 下周日历**: upcoming events with H/M/L impact.

### Steps 1–10 — Analysis content (continued)

Same requirements as the core weekly scan. Reference:

- Cross-asset & coverage: [coverage-matrix.md](reference/coverage-matrix.md)
- AI supply chain Step 4.5: [ai-supply-chain.md](reference/ai-supply-chain.md)
- Report structure: [weekly-report.md](templates/weekly-report.md)

Key reminders:

- **Step 4.5** AI tables required when AI/semi/tech is a driver (default: always include).
- **Step 8** Regime must include confidence (H/M/L) and falsifiers — feeds `meta.regime`.
- **Step 10** Playbook must have invalidation levels.
- Label 事实 / 解读 / 判断; every number needs as-of date.
- **Step 2 / 2.1.2**: include market-moving speeches & news per [macro-news-recall.md](reference/macro-news-recall.md); data-only 2.1 is incomplete.

### Step 11 — Quality gate

Before delivery:

- [ ] **2.1.2** filled with news/speeches OR explicit "no threshold event" note
- [ ] **HY OAS + 10Y-2Y** from FRED (or proxy labeled) with 1W Δ in bp
- [ ] **Step 4.5** AI tables filled or explicitly "no new print this week"
- [ ] Every price/level has **as-of date** and source class
- [ ] Facts vs opinions clearly labeled
- [ ] No fabricated consensus numbers
- [ ] Report fits [weekly-report.md](templates/weekly-report.md) structure
- [ ] **meta** fields derived from report (not invented separately)
- [ ] **No A-share / HK** index, ticker, or dedicated narrative sections (unless user explicitly overrides scope)
- [ ] `meta.weekEnding` matches report header Friday date
- [ ] `meta.kpis` includes at least HY OAS, 10Y-2Y, VIX

### Step 12 — Web delivery (mandatory)

Full spec: [web-delivery.md](reference/web-delivery.md).

1. **Write `bodyMarkdown`** — complete report per [weekly-report.md](templates/weekly-report.md). No truncation.
2. **Write `meta`** — JSON per [report-meta.json](templates/report-meta.json). Extract from the report you just wrote:
   - `title`: one-line headline (≤80 chars, 中文)
   - `regime` / `regimeConfidence`: from Step 8
   - `summaryOneLiner`: rotation + top risk in one line
   - `kpis`: HY OAS, 10Y-2Y, VIX (value + 1W delta + dir)
3. **POST** to finance-site:

```http
POST {{WEEKLY_REPORT_API_URL}}/api/weekly-reports
Authorization: Bearer {{WEEKLY_REPORT_INGEST_TOKEN}}
Content-Type: application/json

{
  "meta": { ... },
  "bodyMarkdown": "..."
}
```

4. **Confirm** response `201` or `200` with report `id`. On failure: save JSON + md in run output and report error — do not silently skip.
5. **Run output** — always include `meta` JSON + full `bodyMarkdown` in automation run (archive even after successful POST).

Default API URL: `https://hblook.com` (override via `WEEKLY_REPORT_API_URL`).

---

## Automation mode

When the user wants a **scheduled weekly Cursor Automation**, read the **automate** skill and follow its spine. Use this skill for **content + web ingest** only.

### Recommended automation defaults

| Field | Default | Notes |
|-------|---------|-------|
| Trigger | **Sunday 20:00 Beijing** (`0 20 * * 0`) | Confirm timezone Asia/Shanghai |
| Name | Weekly Market Scan → Web | |
| Memory | Enabled | Track recurring themes & watchlist |
| Tools | **FRED** (MCP or REST) only | **No** Post to Slack / WeChat |
| Prompt body | [automation-prompt.md](templates/automation-prompt.md) | |
| Secrets | `FRED_API_KEY`, `WEEKLY_REPORT_INGEST_TOKEN` | Token on server `.env.local` |

### Automation prompt rules

- Agent **must** run Steps 0–12 checklist
- Agent **must** compare to prior run if memory enabled
- Agent **must** pull HY OAS + 10Y-2Y via FRED before credit/curve fields
- Agent **must** run Step 4.5 AI supply chain tracker
- Agent **must** research **2.1.2** news/speeches (forums, Fed/ECB remarks, policy headlines) per [macro-news-recall.md](reference/macro-news-recall.md)
- Agent **must not** invent data
- Agent **must not** post to Slack, WeChat, or other channels
- Output: `meta` + `bodyMarkdown` in run output **and** POST to site

### User config to collect before drafting automation

1. **Markets**: US only / global (default: US + global macro; **no A-share / HK**) → `meta.scope`
2. **Watchlist**: tickers or "use memory"
3. **API URL**: default `https://hblook.com`
4. **Schedule**: day + time + timezone
5. **Language**: 中文 / English / bilingual

---

## Output summary

| Artifact | Format | Where |
|----------|--------|-------|
| List fields | `meta` JSON | DB + `/weekly` sidebar |
| Full report | `bodyMarkdown` | DB + `/weekly` detail |
| Archive | Both in run output | Cursor Automation history |

**Not in scope for this skill**: Slack parent/thread, WeChat HTML, PushPlus, `push_wechat.py`, `slack-summary.md`.

---

## Additional resources

- Web ingest API: [web-delivery.md](reference/web-delivery.md)
- Meta schema: [report-meta.json](templates/report-meta.json)
- FRED API & MCP: [fred-data.md](reference/fred-data.md)
- AI supply chain: [ai-supply-chain.md](reference/ai-supply-chain.md)
- FRED fetch script: [scripts/fetch_fred.py](scripts/fetch_fred.py)
- Coverage & thresholds: [coverage-matrix.md](reference/coverage-matrix.md)
- Macro news & speeches (2.1.2): [macro-news-recall.md](reference/macro-news-recall.md)
- Automation prompt: [automation-prompt.md](templates/automation-prompt.md)
- Report template: [weekly-report.md](templates/weekly-report.md)
