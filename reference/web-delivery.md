# Web Delivery — finance-site `/weekly`

The website **only ingests and renders** reports. It does not fetch FRED or market data at display time. All numbers come from the agent run (this skill).

## Payload shape (Demo B)

```json
{
  "meta": {
    "weekEnding": "YYYY-MM-DD",
    "title": "string",
    "regime": "string",
    "regimeConfidence": "H | M | L",
    "scope": "US | Global",
    "generatedAt": "YYYY-MM-DD HH:MM timezone",
    "summaryOneLiner": "string",
    "kpis": [
      { "label": "HY OAS", "value": "278bp", "delta": "+12bp", "dir": "up" }
    ]
  },
  "bodyMarkdown": "# 周度市场检测报告 | Weekly Market Scan\n\n..."
}
```

### Meta field rules

| Field | Source in report | Notes |
|-------|------------------|-------|
| `weekEnding` | Header「报告周期」Friday date | Unique key; `YYYY-MM-DD` |
| `title` | Synthesize from exec summary | ≤80 chars, 中文 preferred |
| `regime` | Step 8 primary regime | Free text OK (AI may blend labels) |
| `regimeConfidence` | Step 8 H/M/L | |
| `scope` | Header「覆盖范围」 | `US` or `Global` only — no `US+CN`; A-share/HK out of scope |
| `generatedAt` | Header「生成时间」 | |
| `summaryOneLiner` | Exec bullets 3+4 compressed | Rotation + key risk |
| `kpis` | Step 7 risk dashboard | **Minimum 3**: HY OAS, 10Y-2Y, VIX |

`dir` for KPIs: `up` | `down` | `flat` — semantic for display (e.g. HY OAS up = risk-off).

### bodyMarkdown rules

- Full [weekly-report.md](../templates/weekly-report.md) output — **no truncation**
- Markdown tables preserved (site renders them)
- Do not strip sections because meta exists; meta is a **list shortcut**, not a substitute

---

## Ingest API

```http
POST /api/weekly-reports
Authorization: Bearer <WEEKLY_REPORT_INGEST_TOKEN>
Content-Type: application/json
```

| Env (server) | Purpose |
|--------------|---------|
| `WEEKLY_REPORT_INGEST_TOKEN` | Bearer token; agent secret in Automation |
| `WEEKLY_REPORT_API_URL` | Optional override; default `https://hblook.com` |

### Success

- `201 Created` — new report for `weekEnding`
- `200 OK` — updated existing report for same `weekEnding` (idempotent re-run)

Response body (example):

```json
{ "id": "clx...", "weekEnding": "2026-06-26" }
```

### Errors

| Status | Meaning |
|--------|---------|
| `401` | Invalid or missing token |
| `400` | Missing `bodyMarkdown` or invalid `meta.weekEnding` |
| `5xx` | Server error — retain payload in run output, retry manually |

---

## Agent POST example (curl)

```bash
curl -sS -X POST "${WEEKLY_REPORT_API_URL:-https://hblook.com}/api/weekly-reports" \
  -H "Authorization: Bearer $WEEKLY_REPORT_INGEST_TOKEN" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

`payload.json` = `{ "meta": {...}, "bodyMarkdown": "..." }`.

If the agent cannot run shell curl, use any available HTTP tool in the Automation environment. **Always** echo the same JSON in run output as backup.

---

## UI mapping (finance-site `/weekly`)

| UI element | Data source |
|------------|-------------|
| Sidebar list (date, title, regime pill) | `meta` |
| Regime banner + KPI chips | `meta` |
| Report body (tables, playbook, etc.) | `bodyMarkdown` |

---

## Secrets (never commit)

| Secret | Where |
|--------|-------|
| `FRED_API_KEY` | MCP env / Automation Cloud |
| `WEEKLY_REPORT_INGEST_TOKEN` | Automation Cloud secrets |
| `WEEKLY_REPORT_API_URL` | Optional; Automation env |

Do not paste tokens into skill files, reports, or git.
