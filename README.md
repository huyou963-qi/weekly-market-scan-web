# weekly-market-scan-web

Cursor Agent Skill：生成交易员级**周度跨资产市场扫描**，并 **POST 到 finance-site** 的「AI周度观察」页面（`/weekly`）。

基于 [weekly-market-scan](https://github.com/huyou963-qi/weekly-market-scan)，去掉 Slack / 微信等通道，仅保留网站投递（Demo B：`meta` + `bodyMarkdown`）。

## 安装（Cursor）

克隆到本机 skills 目录，例如：

```bash
git clone https://github.com/huyou963-qi/weekly-market-scan-web.git \
  ~/.cursor/skills/weekly-market-scan-web
```

或在 Cursor Settings → Rules / Skills 中指向该目录。Skill 入口文件为根目录 `SKILL.md`。

## 输出

| 部分 | 说明 |
|------|------|
| `meta` | 列表页：weekEnding、title、regime、KPI chips（见 `templates/report-meta.json`） |
| `bodyMarkdown` | 完整周报 Markdown（见 `templates/weekly-report.md`） |

入库 API：`POST /api/weekly-reports`（Bearer `WEEKLY_REPORT_INGEST_TOKEN`）。详见 `reference/web-delivery.md`。

## 环境变量（Automation Secrets）

| 变量 | 用途 |
|------|------|
| `FRED_API_KEY` | HY OAS、10Y-2Y 等（MCP 或 `scripts/fetch_fred.py`） |
| `WEEKLY_REPORT_INGEST_TOKEN` | 与 finance-site 服务端 `.env.local` 一致 |
| `WEEKLY_REPORT_API_URL` | 可选，默认 `https://hblook.com` |

## 目录

```
SKILL.md                 # Skill 主文档
templates/
  weekly-report.md       # 正文模板
  report-meta.json       # meta 示例
  automation-prompt.md   # Cursor Automation 提示词
reference/
  web-delivery.md        # POST 规范
  fred-data.md
  coverage-matrix.md
  ai-supply-chain.md
scripts/
  fetch_fred.py          # FRED 拉取（需 FRED_API_KEY）
```

## 相关仓库

- [finance-site](https://github.com/huyou963-qi/finance-site) — 站内 `/weekly` 页面与 ingest API
- [weekly-market-scan](https://github.com/huyou963-qi/weekly-market-scan) — 原版（含 Slack / 微信）

## License

与 weekly-market-scan 相同，内部使用；勿将 API Key 提交到仓库。
