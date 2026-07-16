# Earnings Recall — Section 5.2

Section **5.2 重要公司财报与预期差** covers **three** mandatory pieces for the reporting week:

1. **本周已发布** — important company results that printed Mon–Fri
2. **下周预告** — high-impact earnings still ahead
3. **预期差** — where results/guidance diverged from consensus **and/or** from what the stock had priced in

A one-line "earnings tone" blurb is **not** sufficient.

**Scope**: US (and global mega-cap if in universe). **Out of scope**: A-share / HK listings unless the user explicitly overrides.

---

## Why this exists

Weekly cross-asset scans often under-weight single-name earnings even when they drive index/sector moves. Traders need:

- Which **systemic names** reported, and whether EPS/rev/guidance beat or missed
- The **expectation gap** (共识差 + 定价差) — not just "beat/miss" labels
- What is **still ahead** next week (calendar + implied move / why it matters)

---

## Inclusion threshold (row required)

### 5.2.1 本周已发布 — include when **any** hold

| Signal | Threshold |
|--------|-----------|
| Mega-cap / Mag7 | Always (AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA — adjust if universe changes) |
| Index weight | Top ~20 SPX weight, or any name that contributed materially to 1W index move |
| Stock move | \|1D\| ≥ 5% or \|1W\| ≥ 8% around the print |
| Sector impact | Sector ETF \|1D rel SPX\| ≥ 1% clearly tied to the print |
| Guidance / revision | Material guide cut/raise, or street estimate revision cluster |
| User watchlist | Any watchlist name that reported |

Cap table at **~8–12 names**; if many mid-caps reported, keep mega/systemic + largest movers and summarize the rest in **Earnings tone**.

### 5.2.2 下周预告 — include when **any** hold

| Signal | Threshold |
|--------|-----------|
| Mega-cap / Mag7 | Always if scheduled next week |
| High options implied move | Typical ≥ ~4–5% (or top of that week's earnings IV rank) |
| Sector cluster | Banks, semis, retail, etc. with multiple Tier-1 prints same week |
| Macro-sensitive | Names whose guide resets rates/FX/commodity narrative (e.g. money-center banks, energy majors) |
| User watchlist | Scheduled prints on the watchlist |

### 5.2.3 预期差 — include when **any** hold

| Gap type | When to flag |
|----------|--------------|
| 共识差 | EPS or revenue surprise vs consensus ≥ ~3–5% (or clearly material for the sector) |
| 指引差 | Guidance vs street / vs prior guide is the main story (even if EPS beat) |
| 定价差 | Stock reaction **mismatches** the headline beat/miss (e.g. beat + selloff on soft guide) |
| 叙事差 | Street thesis broken or confirmed (capex, margins, AI demand, consumer) with index/sector spillover |

---

## Research workflow (mandatory for Step 5)

Run **after** Step 4 / 4.5 and **before** finalizing §5 / §6:

1. **Calendar scan** — next week's Tier-1 / Tier-2 earnings (IR calendars, earnings aggregators).
2. **This-week results** — web search `"week ending [date]" earnings` + Mag7 / top movers; pull EPS, revenue, guidance vs consensus.
3. **Cross-check** — ≥2 independent sources for consensus and actuals (company IR / 8-K + reputable wire or aggregator). Prefer primary filings for guidance quotes.
4. **Reaction** — same-day / session-close stock move and, if relevant, sector ETF; as-of date required.
5. **Expectation gap** — for each Tier-1 print, state: consensus → actual → what was priced (IV / pre-earnings drift if known) → reaction fit.
6. **De-dupe** — §5.1 is transmission matrix (event → 1st/2nd order); §5.2 owns the earnings tables. Do not duplicate full rows; cross-reference tickers.

---

## Row formats

### 5.2.1 本周已发布

| 日期 | Ticker | EPS 实际 vs 共识 | 营收 实际 vs 共识 | 指引/关键点 | 预期差 | 股价反应 | 板块含义 |
|------|--------|------------------|------------------|------------|--------|----------|----------|

Column guidance:

- **EPS / 营收**: actual, consensus, and surprise % (or beat/miss + magnitude). Never invent consensus.
- **指引/关键点**: 1–2 bullets — next-quarter/FY guide, margin, capex, AI/demand commentary.
- **预期差**: 共识差 / 指引差 / 定价差 — which one drove the tape.
- **股价反应**: 1D (and 1W if useful) with as-of date.
- **板块含义**: peer/sector ETF read in one line.

### 5.2.2 下周预告

| 日期 | Ticker | 共识 EPS / 营收 | 隐含波动/关注点 | 为何重要 | 预期差观察点 |
|------|--------|-----------------|-----------------|----------|--------------|

- **隐含波动/关注点**: options implied move if available; else key KPIs the street will debate.
- **预期差观察点**: what would surprise (guide, margins, capex, unit trends) — not a price target.

### 5.2.3 预期差摘要

| Ticker | 市场定价/共识 | 实际结果 | 预期差类型 | 反应是否匹配 | 交易含义 |
|--------|---------------|----------|------------|--------------|----------|

Keep to **3–6** highest-signal rows. Label 事实 / 解读 / 判断.

---

## Earnings tone (always)

After the tables, 2–4 sentences covering:

- Aggregate beat rate / guide tone if in earnings season (fact, with source/as-of)
- Sector splits (who led revisions)
- Link to §4 rotation and §8 regime when material

---

## Silence rules

**Off-season / thin week** — do not omit §5.2 headers:

```text
本周无达到纳入阈值的系统性/高波动财报；指数波动主要由 [宏观/仓位/流动性] 因素解释。下周关注：[列出预告或写「无 Tier-1 财报」]。
```

If **5.2.1** is empty but **5.2.2** has names → fill preview + note empty reported table.  
If both empty → silence note under 5.2.1 and 5.2.2; 5.2.3 may say "无显著预期差案例".

---

## Source priority

1. Company IR / SEC filings (8-K, press release, transcript)
2. Consensus from reputable aggregators (label source; do not fabricate)
3. Major newswires for reaction narrative
4. Exchange prices for reaction column
5. Options implied move from market data vendors when available

**Do not** invent consensus, surprise %, or "whisper numbers". If consensus unavailable, state `共识不可用` and rely on guidance/reaction facts only.
