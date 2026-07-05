# Macro News & Speech Recall — Section 2.1

Section **2.1 本周回顾** must cover **both** scheduled macro data **and** market-moving news that occurred during the reporting week. Data-only recaps are incomplete.

---

## Why this exists

Scheduled releases (NFP, CPI, FOMC) are necessary but not sufficient. Traders also need same-week recall of:

- **Central bank / official speeches** at forums (ECB Forum Sintra, Jackson Hole, BOE/BoJ pressers, Fed speakers)
- **Surprise policy headlines** (tariffs, sanctions, fiscal packages, emergency liquidity)
- **Geopolitical shocks** with cross-asset transmission (energy, shipping, FX)
- **Regulatory / antitrust** actions on systemic sectors (banks, mega-cap tech, pharma)
- **Sovereign / credit headlines** (downgrades, bank stress, EM policy pivots)

Example (week ending 2026-07-03): **Kevin Warsh** remarks at the **ECB Forum** mid-week moved rates, USD, and gold intraday — must appear in **2.1.2**, not only in narrative prose elsewhere.

---

## Inclusion threshold (2.1.2 row required)

Add a row when **any** of the following hold on the event day:

| Signal | Threshold |
|--------|-----------|
| UST 10Y | \|intraday\| ≥ 8bp or \|1D close\| ≥ 5bp |
| DXY | \|1D\| ≥ 0.5% |
| SPX / NDX | \|1D\| ≥ 1% |
| VIX | \|1D\| ≥ 2 pts |
| Gold / WTI | \|1D\| ≥ 1.5% |
| Sector ETF | \|1D rel SPX\| ≥ 1% with clear headline link |

If the headline is **Tier 1** by nature (Fed chair, tariff announcement, war escalation) → include even when the move is modest.

---

## Event types (column `类型`)

| 类型 | Examples |
|------|----------|
| 讲话 | Fed/ECB/BOJ/PBoC officials; Treasury Secretary; candidate for policy role |
| 政策 | Tariffs, export controls, fiscal cliff/deal, emergency facilities |
| 地缘 | Conflict escalation/de-escalation, sanctions, Strait/shipping |
| 监管 | Antitrust ruling, bank resolution, capital rules |
| 信用 | Large default, sovereign downgrade, regional bank stress |
| 其他 | Only if cross-asset impact meets threshold |

---

## Research workflow (mandatory for Step 2)

Run **after** anchoring the week (Mon–Fri) and **before** writing 2.1:

1. **Calendar scan** — central bank speaker schedules, forum agendas (ECB Forum, BoE, IMF/World Bank, G7/G20 side events).
2. **Web search** — `"week ending [date]" Fed speech OR ECB forum OR tariff OR geopolitical` plus ticker-level movers (yields, DXY, gold).
3. **Cross-check** — at least **2 independent sources** (official transcript/central bank site + reputable press). Prefer primary text for quotes.
4. **Same-day market link** — note which assets moved and direction; use **事实** for prices, **解读** for causality.
5. **De-dupe with §5** — 2.1.2 is **recap** (what happened + immediate reaction); §5 is **transmission** (1st/2nd order, pricing status). Brief in 2.1.2, expand in §5 if Tier 1.

---

## Row format (2.1.2 table)

| 日期 | 类型 | 事件/讲话人 | 核心要点 | 市场反应 | 解读 |
|------|------|-------------|----------|----------|------|

Column guidance:

- **核心要点**: 1–3 bullets — who, where, what was new vs prior stance (not full transcript).
- **市场反应**: Same-day or session-close move in rates / FX / equities / vol — with **as-of date**.
- **解读**: Why markets cared; label 事实 vs 解读 vs 判断.

Data releases stay in **2.1.1** — do not duplicate full NFP/CPI rows in 2.1.2 unless a **speech on the same day** materially changed the read (then cross-reference in 解读).

---

## Silence rule

If no item meets the threshold:

```text
本周除已列数据发布外，无达到纳入阈值的独立新闻/讲话驱动；大类资产波动主要由 [X] 数据与 [Y] 仓位/流动性因素解释。
```

Do **not** omit the **2.1.2** subsection header.

---

## Source priority

1. Official transcripts (Fed, ECB, Treasury, White House, central bank YouTube/PDF)
2. Major newswires / financial press (Reuters, Bloomberg, FT, WSJ)
3. Cross-asset price data (FRED, index closes) for reaction column
4. Do **not** fabricate quotes, "market expected X" without source, or attribute moves without same-day evidence
