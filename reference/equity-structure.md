# Equity Market Structure — Breadth Data (Step 3)

Mandatory for **§3 股市结构**: advancing/declining, NH/NL, % of stocks above 50-DMA and 200-DMA, and Top10 contribution to the index move.

These rows are **not optional**. "未拉取" / "不可用（未拉取）" is a process failure, not an acceptable silence note.

**Universe (default)**: **S&P 500 constituents** (currently ~500–503 names). Label this in the table or a footnote. Do **not** silently substitute NYSE composite A/D unless the SPX compute failed and you mark the substitute as NYSE.

**Out of scope**: A-share / HK breadth.

---

## Why this exists

Index level can rise on a handful of mega-caps. Breadth tells whether the tape confirms:

| Metric | What it answers |
|--------|-----------------|
| 上涨/下跌家数 | Is the session/week majority-up or majority-down? |
| NH/NL | Are 52-week highs expanding or is the index making highs without participation? |
| >50DMA 占比 | Short-term trend participation (midline ~50%) |
| >200DMA 占比 | Intermediate bull/bear structure (often >60% in a healthy bull) |
| 指数涨幅中 Top10 贡献 | How much of the SPX 1W move came from the 10 largest weights? |

Style/factor proxies (QQQ vs IWD, SPY vs IWM) **supplement** these rows; they do **not** replace them.

---

## Fetch priority (agent workflow)

```
1. scripts/fetch_breadth.py          → python scripts/fetch_breadth.py --as-of <Friday> --json
2. historyofmarket breadth JSON      → DMA % only (see below)
3. Web (labeled)                     → WSJ Markets Diary / Barchart $S5FI $S5TH / StockCharts $SPXA50R $SPXA200R $NYHL
4. Silence note AFTER all paths      → "数据不可用（已尝试 script / HOM / WSJ / Barchart）"
```

Never write **未拉取**. That string means the agent skipped the pull.

### 1. Script (required first)

From skill root:

```bash
python scripts/fetch_breadth.py --json
python scripts/fetch_breadth.py --as-of YYYY-MM-DD --json
```

`--as-of` = report Friday (`meta.weekEnding`). If omitted, uses the latest Yahoo daily bar.

**No API key.** Constituent list: Wikipedia S&P 500 table, fallback `datasets/s-p-500-companies` CSV. Prices: Yahoo chart v8 daily closes.

Paste `report.*` into the §3 table:

| §3 row | JSON field | 1W Δ field |
|--------|------------|------------|
| 上涨/下跌家数 | `report.advance_decline` | `report.advance_decline_1w` |
| NH/NL | `report.nh_nl` | `report.nh_nl_1w` |
| >50DMA 占比 | `report.pct_above_50dma` | `report.pct_above_50dma_1w` |
| >200DMA 占比 | `report.pct_above_200dma` | `report.pct_above_200dma_1w` |
| 指数涨幅中 Top10 贡献 | `report.top10_contrib` | `report.top10_contrib_1w` |

Also copy `as_of` into the section as-of note. If `warnings` is non-empty, mention the cross-check gap in **Structure read** (do not drop the computed numbers).

Exit code 2 → script failed (too few charts). Continue to path 2–3; do not invent.

### 2. historyofmarket (DMA fallback / cross-check)

```
GET https://historyofmarket.com/api/sp500/breadth.json
```

Fields: `series[].date`, `pct50`, `pct200`. Pick last observation `date ≤ weekEnding`.

Vendor series (StockCharts `$SPXA50R`, Barchart `$S5FI`, historyofmarket `pct50`/`pct200`) can differ from the script by several percentage points (constituent vintage, split/dividend adjustment, MA definition). **Report the script numbers as source of record.** Use a vendor only as a labeled cross-check, or as fallback if the script exits non-zero.

### 3. Web fallback (must name the source)

Try in order until a **numeric** print exists for the missing row:

| Metric | Sources |
|--------|---------|
| A/D | WSJ [Markets Diary](https://www.wsj.com/market-data/stocks/marketsdiary); Barchart market performance |
| NH/NL | WSJ Markets Diary (NYSE + Nasdaq new highs/lows); StockCharts `$NYHL` / `$NAHL`; Barchart `$NYHGH` `$NYLOW` |
| >50DMA | Barchart `$S5FI`; StockCharts `$SPXA50R` |
| >200DMA | Barchart `$S5TH` (S&P 500 stocks above 200-day); StockCharts `$SPXA200R` |
| Top10 贡献 | Slickcharts [S&P 500](https://www.slickcharts.com/sp500) weights + weekly returns; or Mag7/top weights × 1W return as labeled estimate |

If the fallback universe is NYSE/Nasdaq rather than SPX, **say so** in the 数值 cell.

### 4. After all paths fail

Keep the row. Write `数据不可用（已尝试 script / HOM / WSJ / Barchart）` plus which path failed. Still fill **Style / factor** from sector ETFs. Still write **Structure read** using whatever did print (RUT vs SPX is a *proxy comment*, not a substitute for the five rows).

---

## Definitions (script)

- **Advancer / decliner**: Friday close vs prior session close (S&P 500 members). `1W Δ` is that Friday snapshot vs the prior Friday snapshot — not NYSE composite.
- **New high / new low**: Friday close at or through the max/min of the prior 252 sessions (S&P 500 members).
- **% above 50/200 DMA**: last close vs simple moving average of daily closes; members with insufficient history are dropped from that percentage only.
- **Top10 contribution**: current Slickcharts SPX weights × each name's Friday-to-prior-Friday return. Contribution in index ppt ≈ `weight × return`. Share of index move = Top10 contrib ppt / SPX (or SPY) 1W ppt. Weights are **not** point-in-time as-of Monday; label the source.
- **1W Δ** (other rows): same snapshot on the session ≤ Friday−7d.

---

## Signal hints (interpretation, not hard rules)

| Metric | Constructive | Caution |
|--------|----------------|---------|
| A/D ratio | ≥ ~1.5 on up weeks | < ~0.7 while index is up (narrow tape) |
| NH vs NL | NH >> NL, net rising | Index high + NH fading / NL rising |
| >50DMA | Rising through 50–70% | Index high + % falling (divergence) |
| >200DMA | Stable/rising above ~60% | Breaking toward 50% with index still high |
| Top10 占变动 | Share of SPX move well below Top10 weight on an up week (broad tape) | Share >> weight while index makes highs (narrow leadership) |

Index ↑ + breadth ↓ is a Step 9 anomaly candidate.

---

## Quality bar

- Numbers have **as-of date** and source class (`computed Yahoo/SPX` / `historyofmarket` / `WSJ` / `Barchart` / `StockCharts`).
- Do not fabricate NH/NL or DMA percentages from "index at highs → 占比偏高".
- Do not replace Top10 contribution with a Mag7 narrative unless the script/Slickcharts path failed and the estimate is labeled.
- Do not skip the script because FRED / earnings / AI steps already ran.
