# Quality bar for weekly-market-scan-web (match 2026-05-08 hand-written)

Reference report: `/workspace/reports/2026-05-08-body.md` + `2026-05-08-payload.json`

## Must match quality of reference (NOT the batch template)

1. **Executive summary**: 5 concrete bullets with real numbers, named catalysts, actionable playbook.
2. **Cross-asset dashboard**: Fill 1W/YTD with real closes; write a 2–4 sentence **Cross-asset read** that tells a correlation story (事实/解读/判断).
3. **Macro**: Real event rows with **actual vs consensus** when researchable; next-week calendar with H/M/L; a narrative paragraph — not “见官方发布”.
4. **Equity structure**: Style/factor call + breadth vs index divergence judgment.
5. **Sectors**: Full GICS table with 1W rel vs SPX; name leaders/laggards; **FROM → TO** with evidence.
6. **Step 4.5 AI**: Real HBM/API/GPU/capex context when available for that week; otherwise explicit “no new print this week” + last known; synthesis paragraph linking SOX/XLK/MU/NVDA.
7. **Events**: Transmission matrix with price-in status.
8. **Watchlist**: Concrete tickers with 1W, S/R levels, views — especially names with |1W|>5%.
9. **Risk**: HY OAS + 10Y-2Y from FRED data JSON; alerts; watch levels.
10. **Regime**: Named regime + H/M/L + falsifiers + vs last week.
11. **Playbook**: Base case paragraph; Bull/Base/Bear probabilities; ≤3 conviction setups with invalidation; positioning.

## Hard rules

- **Cutoff**: never use information dated after `weekEnding`.
- `meta.weekEnding` = last trading day (Good Friday week = `2026-04-02`).
- Numbers: every price has as-of date; FRED from `/workspace/reports/data/{weekEnding}.json`.
- Label 事实 / 解读 / 判断.
- Do **not** invent consensus prints; if unknown, omit the consensus figure or say “共识不可得”.
- Language: 中文为主, bilingual headers as in template.
- After writing: save payload + POST immediately.

## POST

```bash
# WEEKLY_REPORT_INGEST_TOKEN must be set in the environment (never commit the token)
python3 /workspace/scripts/post_weekly_report.py /workspace/reports/hq/{weekEnding}-payload.json
```

Expect HTTP 200 or 201.
