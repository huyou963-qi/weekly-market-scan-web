# 周度市场检测报告 | Weekly Market Scan

**报告周期**: Week ending 2026-07-24  
**生成时间**: 2026-07-25 08:15 CST  
**覆盖范围**: Global macro + US equities（不含 A股、港股）  
**数据截止**: 权益/商品/VIX as-of 2026-07-24 close（Yahoo）；FRED HY OAS / DGS2 / DGS10 as-of 2026-07-23；T10Y2Y as-of 2026-07-24

---

## 执行摘要 | Executive Summary

1. **Regime**: Stagflation-lite / AI Capex Digestion（置信度 M）— 油价与 AI 资本开支叙事同时施压估值。
2. **Top move**: WTI 周涨约 +9.7% 至 ~90.5；Brent 周四一度站上 100；TSLA 周跌约 −18% 领跌 Mag7。
3. **Rotation**: FROM Mega-cap growth（TSLA/GOOGL/META/AMZN）→ TO Energy / Utilities / Industrials；Memory（MU）逆势走强。
4. **Key risk**: FOMC（07-29）沟通 + 油价/关税通胀再定价；CME FedWatch 显示加息概率由约 12% 升至约 1/3。
5. **Playbook**: 下周以 FOMC + MSFT/META/AAPL/AMZN 财报为轴；保持对 AI Capex 指引差敏感，能源多头需设无效位。

---

## 1. 大类资产仪表盘 | Cross-Asset Dashboard

| 资产 | 标的 | 1W | MTD | YTD | 52W区间位置 | 驱动 |
|------|------|-----|-----|-----|-------------|------|
| 美股 | SPX | −0.61% | −1.17% | +8.28% | ~86% | Mag7 财报/油价；连跌两周 |
| | NDX | −1.62% | −7.09% | +11.4% | ~68% | Growth 估值压缩 |
| | RUT | −1.09% | −3.12% | +18.1% | ~89% | 风险偏好降温 |
| 利率 | UST 10Y (FRED `DGS10`) | 4.71%（+14bp） | — | — | — | as-of 07-23；油价→term premium |
| | UST 2Y (FRED `DGS2`) | 4.37%（+21bp） | — | — | — | as-of 07-23；加息再定价 |
| | **10Y-2Y (FRED `T10Y2Y`)** | **0.36%（−1bp）** | +6bp/1M | — | — | as-of 07-24；略 flatten |
| 信用 | **HY OAS (FRED `BAMLH0A0HYM2`)** | **277bp（+6bp）** | +6bp/1M | — | — | as-of 07-23；温和 widening |
| 外汇 | DXY | +0.71% | +0.27% | +3.24% | ~97% | 实际利率上行 |
| 商品 | WTI | +9.67%（90.47） | +30.2% | +57.6% | ~61% | Hormuz/Red Sea 风险溢价 |
| | Gold | +1.07%（4055.7） | +0.82% | −6.24% | ~38% | 避险与实际利率对冲 |
| | Copper | +1.92%（6.34） | +2.37% | +12.6% | ~87% | 供给/周期混合 |
| 波动 | VIX | 18.58（−0.19） | +13.0% | +24.3% | ~29% | 高位震荡，未 panic spike |

*来源：Yahoo Finance daily close（07-17→07-24）；FRED `scripts/fetch_fred.py --json`（fetched 2026-07-24T23:52Z）。*

**Cross-asset read**（事实/解读）:  
事实：权益连跌第二周，同时油价、美元与名义利率同步上行，HY OAS 仅温和走阔。  
解读：这是“增长仍在但通胀再定价”的组合，而非全面 risk-off；VIX 未显著走高说明对冲需求有限、定价更偏利率与板块轮动。  
判断：若油价继续向 Brent 持续收盘 >100 推进，FOMC 沟通风险会主导下周 beta。

---

## 2. 宏观与政策 | Macro & Policy

### 2.1 本周回顾

#### 2.1.1 数据发布

| 日期 | 事件/数据 | 实际 vs 预期 | 市场反应 | 解读 |
|------|-----------|--------------|----------|------|
| 07-23 | Initial Jobless Claims（周至 07-18） | **187K** vs 共识 ~212K；前值修订 209K（DOL） | UST 收益率偏强；劳动力韧性强化“Fed 更关注通胀侧”叙事 | 事实：近约 60 年低位附近；解读：layoffs 受限，削弱降息/宽松期权价值 |
| 07-24 | S&P Global US Flash PMI（7月） | Composite **53.6**（前 51.9）；Services **53.6**（前 51.2）；Mfg **53.8**（前 53.9，预期约 54.3） | 美元偏强；对“软着陆仍在”提供支持 | 事实：服务业加速；制造略低预期但仍扩张。解读：供给扰动（中东）延长交期，输入通胀需盯 |
| 本周 | 无重磅 CPI/NFP/FOMC 决议 | — | 定价主轴转向油价、关税与财报 | 数据空窗放大事件驱动波动 |

#### 2.1.2 要闻、讲话与政策动态

| 日期 | 类型 | 事件/讲话人 | 核心要点 | 市场反应 | 解读 |
|------|------|-------------|----------|----------|------|
| 07-20~24 | 地缘 | 美伊冲突升级 / Hormuz + Red Sea | 美军连续打击；Houthi 袭击沙特油轮；特朗普威胁“massive attack”；伊朗拒绝对 Hormuz 管控的停火方案（多源：NBC/CNBC/Reuters 系） | WTI 周 +~10%；Brent 周四结算 ~100.69 后周五回落；XLE 领涨 | 事实：双海峡风险溢价上升。判断：escalate-to-negotiate 仍是基准，但尾部（航运实质中断）未消 |
| 07-23 | 讲话/政策预期 | Fed Chair Kevin Warsh 框架预热（FOMC 下周） | Warsh “少 forward guidance”；同僚偏 hawkish（Waller 等）；油价抬升使 7 月加息概率升温 | 2Y +21bp（FRED 07-23 vs 一周前）；CME 显示加息概率约 1/3（vs 一周前 ~12%） | 解读：沟通风险 > 决议本身；hold 仍是基准但措辞敏感 |
| 07-23~24 | 政策 | USTR Section 301：对 60 个贸易伙伴 10%/12.5% 关税（forced-labor 调查终裁） | 临时 10% 全球关税到期后接棒；07-24 00:01 ET 生效（USTR/White House） | 周五风险资产谨慎；通胀预期与供应链成本再议 | 事实：法定文本落地。判断：对短期成长股贴现率偏负面 |
| 07-24 | 政策 | ECB 维持利率不变 | 欧央行按兵不动（路透系） | EURUSD 周约 −0.6% | 跨市场：美元相对优势延续 |

### 2.2 下周日历

| 日期 | 事件 | 影响等级 H/M/L | 关注资产/行业 |
|------|------|----------------|---------------|
| 07-28~29 | **FOMC** 决议 + Warsh 发布会（07-29 14:00 ET） | **H** | UST 2Y/10Y、DXY、SPX/NDX、XLU/XLK |
| 07-29 | META、MSFT 财报（盘后） | **H** | XLK/XLC、SOXX、AI Capex 叙事 |
| 07-30 | AAPL、AMZN 财报（盘后）；Initial Claims | **H** / M | XLY/XLK、Consumer、云业务 |
| 07-31 | Core PCE（若按日历发布，以官方为准） | **H** | 实际利率、成长股倍数 |
| 07-27~31 | 财报密集周（LRCX 等半导体设备） | M | SOXX、MU、AVGO |

**Macro narrative**:  
软劳动力数据与扩张 PMI 并存，但油价与关税把叙事从“软着陆+估值扩张”推向“通胀再定价+贴现率上行”。FOMC hold 仍是基准（ING 等机构），但市场已把 2026 加息路径重新抬高——这是下周最大的跨资产催化剂。

---

## 3. 股市结构 | Equity Market Structure

| 指标 | 数值 | 1W Δ | 信号 |
|------|------|------|------|
| 指数表现 | SPX −0.61% / NDX −1.62% / RUT −1.09% | 连跌第二周 | Mega-cap 拖累指数 |
| 日内结构（路透 07-24 盘中引用） | SPX 新高/新低偏窄；Nasdaq 新低多于新高 | — | 成长内部恶化 |
| Mag7 离散 | TSLA −17.8% ↔ NVDA +2.0% | 扩大 | 指数掩盖个股危机 |
| Top10 权重贡献 | GOOGL/META/AMZN/TSLA 明显负贡献 | — | 权重股主导下行 |
| >50DMA / >200DMA | 未获统一权威周度快照 | — | 标注数据缺口；以相对强弱替代 |

**Style / factor**: Large Growth 受创（XLY/XLC 弱势）；Energy / Low-vol（XLU）相对占优；Small（RUT）同步走弱但未崩。  
**Flow / positioning**: 无高频官方 ETF 流量数据；价格行为显示从高估值 AI 平台股向能源与防御轮动。  
**Structure read**: 指数跌幅温和掩盖 Mag7 内部崩盘式离散——这是“窄卖出/叙事冲击”，不是 2008 式全面去杠杆（HY OAS 仅 +6bp 支持该判断）。

---

## 4. 行业轮动 | Sector & Industry Rotation

### 4.1 GICS 一级 — 相对 SPX

| 行业 | ETF | 1W abs | 1W rel SPX | MTD rel | 驱动标签 | RS趋势 |
|------|-----|--------|------------|---------|----------|--------|
| Energy | XLE | +3.36% | **+3.97%** | +13.4% | 油价/地缘 | ↑ |
| Utilities | XLU | +2.48% | +3.09% | +3.3% | 利率波动中的防御 | ↑ |
| Industrials | XLI | +1.81% | +2.42% | −0.2% | 周期/防御混合 | ↑ |
| Materials | XLB | +1.44% | +2.05% | +2.0% | 商品 | →/↑ |
| Real Estate | XLRE | +1.17% | +1.78% | +5.5% | 周内反弹 | → |
| Health Care | XLV | +0.92% | +1.53% | +3.6% | 防御 | → |
| Semiconductors | SOXX | +1.00% | +1.61% | **−16.6%** | 反弹但 MTD 仍深伤 | → |
| Technology | XLK | +0.17% | +0.78% | −6.5% | 指数钝化、个股分化 | → |
| Financials | XLF | +0.09% | +0.70% | +6.2% | 曲线/净息差观望 | → |
| Staples | XLP | −1.24% | −0.63% | +2.5% | 防御失效一周 | ↓ |
| Comm Services | XLC | −3.93% | −3.32% | +0.4% | META/GOOGL | ↓ |
| Discretionary | XLY | −5.22% | **−4.61%** | −5.5% | TSLA 权重重创 | ↓ |

### 4.2 细分行业亮点

**领涨**: Energy（XLE）— WTI/Brent 风险溢价；Memory（MU +8.5%）— HBM/DRAM 紧缺定价延续。  
**领跌**: Autos/EV 叙事（TSLA）、广告/云平台（GOOGL/META）、部分软件（NOW 周内大幅波动后仍弱）。

### 4.3 轮动结论

**资金方向**: FROM Mega-cap Growth / Communication → TO Energy + Utilities + select Cyclicals；半导体内部 **Memory > Broad Tech**。  
**证据**: 相对收益表 + Mag7 收益离散 + 油价/利率同向。

---

## 4.5 AI 产业链 & Capex | AI Supply Chain Tracker

### 4.5.1 HBM / 内存价格

| 指标 | 本期 | 1W/1M Δ | 来源 | 解读 |
|------|------|---------|------|------|
| HBM3e | 供应仍紧；3Q26 合约涨幅预期约 **+8–13% QoQ**（前值框架） | vs 上周报告：无新大幅改价；涨幅较 2Q 的 +53–58% 显著放缓 | TrendForce 3Q26 Memory Price Forecast / 7月新闻稿 | 紧缺未解，但涨价斜率进入“高基数减速” |
| DRAM（conventional / server） | 3Q26 合约 **+13–18% QoQ**；server DRAM 受 LTA 约束 | vs 上周：方向一致，本周无推翻性新 print | TrendForce（2026-07-03 / 07-09） | AI server 支撑，消费端承受力见顶 |
| HBM supply commentary | 三大厂扩产与先进制程并行；2027 供给仍可能不足 | 本周无新财报推翻 | TrendForce DRAM Bulletin 07-22 | 卖方市场延续 |

### 4.5.2 云 GPU 租赁价格 ($/GPU-hr)

| 厂商 | SKU | On-demand | 1W Δ | 信号 |
|------|-----|-----------|------|------|
| AWS | p5.48xlarge (H100) | ~**$6.88**/GPU-hr | unchanged vs last run | 稳定；quota gated |
| GCP | a3-highgpu-8g (H100) | ~**$10.98–11.06** | unchanged | 高价带 |
| Azure | ND96isr H100 v5 | ~**$6.98–12.29**（SKU/区域） | unchanged | 区间宽 |
| CoreWeave | HGX H100 8-GPU | ~**$6.16**/GPU-hr | unchanged（ComputeTape 观测至 07-17/20） | 相对 hyperscaler 中位 |

*来源：ComputeTape H100 July 2026 report、Silicon Analysts / D-Central 汇总；access date 2026-07-25。vs last-run memory：无显著 list-price 变动。*

### 4.5.3 AI API 定价 ($/1M tokens)

| 厂商 | Model | Input | Output | 本周变动? |
|------|-------|-------|--------|-----------|
| OpenAI | GPT-5.6 Sol | $5.00 | $30.00 | N（官方页；与上周一致） |
| OpenAI | GPT-5.6 Terra / Luna | $2.50 / $1.00 | $15 / $6 | N |
| OpenAI | GPT-5.5 | $5.00 | $30.00 | N |
| Anthropic | Claude Sonnet 5（intro）/ Opus 4.8 | $2/$10 · $5/$25（上周基线） | — | 本周无新官宣降价（沿用上周 memory；待官网复核） |
| Google | Gemini 2.5 Pro / 3.1 Pro | $1.25/$10 · $2/$12（上周基线） | — | 本周无新官宣 |

*OpenAI 官方定价页（developers.openai.com/api/docs/pricing）交叉验证 2026-07-25。*

### 4.5.4 Hyperscaler AI Capex

| 公司 | Capex / Guide | YoY | AI 评论 | 1W 更新 |
|------|---------------|-----|---------|---------|
| GOOGL | **CY2026 $195–205B**（前值 $180–190B）；Q2 capex $44.9B | 大幅上修 | Cloud +82% YoY 至 $24.8B；Q2 FCF **−$5.9B** | **新 print（07-22）** — 市场负向定价 |
| MSFT | 市场跟踪约 ~$190B CY（二手汇总） | 高增 | Azure/AI 需求仍是主线 | 不变；**07-29 财报**将重置 |
| AMZN | 待 07-30 更新 | — | AWS capex 关注点 | 预告周 |
| META | 指引带 $125–145B（4月框架，二手） | 高增 | AI infra | 不变；**07-29 财报** |
| Hyperscaler sum | 讨论带仍约 **$650–725B** CY2026；GOOGL 上修使上沿更“实” | — | — | 上沿压力↑ |

**AI stack synthesis**:  
成本曲线：HBM/DRAM 仍在涨但斜率放缓；云 GPU list price 周环比持平；API 旗舰价未降——整体 **“贵且稳”**。Capex 周期：GOOGL 二次上修 + 负 FCF 把市场从“demand 验证”推向“funding cost / free-cash-flow 纪律”。利润链：Memory（MU）继续吃到紧缺溢价，而平台股（GOOGL/META）因支出被贴现。市场联动：SOXX 本周小幅反弹但 MTD 仍深跌；XLK 接近持平掩盖内部撕裂——**AI 叙事从“增速”切换到“回报期”**。

---

## 5. 重点事件与传导 | Events & Transmission

### 5.1 事件传导矩阵

| 日期 | 事件 | 一阶影响 | 二阶影响 | 定价状态 |
|------|------|----------|----------|----------|
| 07-22~23 | GOOGL/TSLA 财报 | 个股暴跌；NDX 承压 | AI Capex 折现率↑；XLY/XLC 拖累 | 部分 price-in，下周其他 Mag7 仍 debatable |
| 07-23 | 油价冲高 / 航运袭击 | WTI/Brent↑、XLE↑ | 通胀预期→UST 收益率↑→成长股承压 | 地缘溢价 **仍 debatable** |
| 07-24 | Section 301 关税生效 | 成本与政策不确定性 | 企业毛利/供应链再议 | 初期定价，路径依赖谈判 |
| 07-29 | FOMC | 利率路径波动 | 美元、黄金、估值倍数 | **未 price-in 完整沟通** |

### 5.2 重要公司财报与预期差

#### 5.2.1 本周已发布

| 日期 | Ticker | EPS 实际 vs 共识 | 营收 实际 vs 共识 | 指引/关键点 | 预期差 | 股价反应 | 板块含义 |
|------|--------|------------------|------------------|------------|--------|----------|----------|
| 07-22 | **GOOGL** | Diluted EPS **$9.11**（含约 $99B 股权证券收益）；Visible Alpha 共识约 **$2.90**（经营口径需区分） | **$119.8B** vs ~$117.2B（+约 2%） | Capex 指引上修至 **$195–205B**；Cloud +82% 至 $24.8B；Q2 FCF −$5.9B | **指引差 + 定价差**（基本面强 vs 现金流弱） | 周 −7.8%；07-23 单日约 −7% | 强化“AI 支出疲劳”；XLC/XLK 承压 |
| 07-22 | **TSLA** | Non-GAAP EPS **$0.33** vs 共识约 **$0.50–0.55**（大幅 miss） | **$28.24B** vs ~$26.3–26.7B（beat） | Op. income −57%；毛利率承压；capex $5.79B（+142% YoY）；FCF −$1.09B；>\$25B AI/机器人开支重申 | **共识差（利润）+ 叙事差（robotaxi/Optimus）** | 周 **−17.8%**；07-23 约 −12%~−15% | XLY 重挫；高 beta 成长去杠杆 |
| 07-22 | TXN | EPS **$2.14**；收入 **$5.46B**（+23% YoY） | — | Q3 收入指引 $5.65–6.15B | 周期复苏信号 | 周 −1.6%（跟大盘波动） | 模拟芯片温和 |
| 07-22 | IBM | 收入约 **$17.2B** 量级；上调全年 CC 收入增速至 4–5% | — | FCF +约 $1B YoY 目标重申 | 指引偏正 | 周 +0.7%（周五反弹） | 企业 IT 稳健但非主驱动 |
| 07-22 | NOW | 订阅收入 **$3.88B**（+24.5% YoY），超指引上沿 | Total **$3.99B** | 上调全年订阅收入指引 | 共识差偏正但估值敏感 | 周 −4.3%（高位消化） | 软件“好消息坏涨” |

*共识数字来自 Visible Alpha / StreetAccount / 公司 IR 与两家以上 mainstream 报道交叉；GOOGL GAAP EPS 含巨额 other income，交易上更盯 Cloud/Capex/FCF。*

#### 5.2.2 下周预告

| 日期 | Ticker | 共识 EPS / 营收 | 隐含波动/关注点 | 为何重要 | 预期差观察点 |
|------|--------|-----------------|-----------------|----------|--------------|
| 07-29 | **MSFT** | EPS ~$4.2–4.3 / 收入 ~$87–89B（日历汇总，口径有差） | AI Capex、Azure 增速、毛利率 | 市值权重 + AI 开支标尺 | 指引差：capex/cloud growth |
| 07-29 | **META** | EPS ~$7.1–7.4 / 收入 ~$60–61B | Reality Labs 亏损、ads、capex 带 | 广告周期 + AI infra | 定价差：是否重演 4 月 capex 冲击 |
| 07-30 | **AAPL** | EPS ~$1.88–1.89 / 收入 ~$108–109B | iPhone/Services、中国需求（宏观，不涉及 A/H 股） | 防御型科技锚 | 服务业韧性 vs 硬件 |
| 07-30 | **AMZN** | EPS ~$1.81 / 收入 ~$197B | AWS 增速与 capex | 云资本开支闭环 | 指引差：AWS + retail margin |
| 07-29 | LRCX 等 | 设备订单/中国出口管制敏感 | SOXX beta | 半导设备景气 | 订单 vs 出货 |

#### 5.2.3 预期差摘要

| Ticker | 市场定价/共识 | 实际结果 | 预期差类型 | 反应是否匹配 | 交易含义 |
|--------|---------------|----------|------------|--------------|----------|
| GOOGL | 预期 Cloud 强、capex 已偏高 | Cloud 超预期但 capex 再上修、FCF 转负 | 指引差 / 定价差 | **匹配**（跌） | 财报季主矛盾=支出纪律 |
| TSLA | 交付复苏可支撑利润 | 收入可以、利润与 FCF 不行 | 共识差 / 叙事差 | **匹配且过度**（需防空头拥挤） | 反弹需看到 margin 或 robotaxi 硬指标 |
| NOW | 高增速已定价 | 增速仍强但杀估值 | 定价差 | 匹配 | 软件多重杀 |

**Earnings tone**: Mag7 开季即显示“收入可以、现金流/利润质量被质疑”；下周 MSFT/META/AMZN 将决定 AI Capex 叙事是扩散还是收敛。

---

## 6. 重点股票 | Watchlist & Systemic Names

### 6.1 观察列表

| Ticker | 1W | 催化剂 | 技术位 | 观点 |
|--------|-----|--------|--------|------|
| NVDA | +2.0% | 供应链/GPU 需求；同业财报溢出 | S/R: 关注 200–212 近周区间 | 相对 Mag7 抗跌；若 MSFT capex 不崩可持有相对多头 |
| MU | +8.5% | HBM/DRAM 涨价 | 波动剧烈（周内冲高回落） | HBM 受益；注意获利回吐 |
| GOOGL | −7.8% | Capex/FCF 消化 | 07-23 缺口压力 | 等 FCF 路径澄清再右侧 |
| TSLA | −17.8% | 利润率/叙事重估 | 明显破位 | 反弹 trading only；无效看再创新低 |
| META | −7.9% | 07-29 财报 | 弱于大盘 | 事件驱动；盯 capex 带 |
| MSFT | −3.1% | 07-29 财报 | 相对抗跌于 META/GOOGL | 质量标的，但是定价锚 |
| AMZN | −6.1% | 07-30 财报 | 走弱 | AWS 指引=关键 |
| AAPL | −0.2% | 07-30 财报 | 相对强 | 防御科技仓位候选 |
| XLE / CVX-proxy | ETF +3.4% | 油价 | 趋势多 | 地缘缓和则减仓 |

### 6.2 系统性/指数权重异动

| Ticker | 1W | 原因 | 板块含义 |
|--------|-----|------|----------|
| TSLA | −17.8% | 利润 miss + AI 开支 | XLY 系统性拖累 |
| META | −7.9% | AI 支出传染 + 财报前减仓 | XLC |
| GOOGL | −7.8% | Capex/FCF | XLC/XLK |
| ORCL | −9.0% | 云/AI 估值压缩外溢 | 软件/云 beta |
| JPM | +3.6% | 利率上移/金融相对收益 | XLF 支撑 |

---

## 7. 风险与流动性 | Risk Dashboard

| 指标 | 现值 | 1W Δ | 解读 |
|------|------|------|------|
| VIX / term structure | **18.58** | −0.19 | 偏高但非危机；事件溢价在 FOMC/财报 |
| **HY OAS (FRED)** | **277bp** | **+6bp** | 温和恶化，未触发 >25bp 警报 |
| **10Y-2Y (FRED)** | **0.36%** | **−1bp** | 曲线近似走平；2Y 上行更快 |
| UST 10Y / 2Y | 4.71% / 4.37% | +14 / +21bp | 紧缩金融条件方向 |
| DXY | 101.47 | +0.71% | USD 流动性略紧 |
| WTI | 90.47 | +9.7% | 通胀冲击主通道 |
| SPX–TLT | TLT −1.5% 与 SPX 同跌 | — | 股债双杀一周（利率驱动） |

**Triggered alerts**:  
- 油价周涨 >5%（触发地缘/通胀警报）  
- Mag7 单周 |move| >8%：TSLA/GOOGL/META/AMZN  
- HY OAS |1W| = 6bp < 25bp 阈值 → **未触发信用压力旗标**

**Watch levels next week**:  
- WTI 能否站稳 88–92；Brent 是否再度日收 >100  
- UST 10Y 4.70–4.80% 区间  
- SPX 7400 保卫；失守看 7300 叙事区（经验位，非精确模型）  
- VIX >22 作为风险偏好破坏信号

---

## 8. 市场 Regime | Regime Classification

**Primary regime**: Stagflation-lite / AI Capex Digestion  
**Confidence**: **M**  
**Falsifiers**:  
1) Brent 快速回到 <90 且航运风险缓和；  
2) MSFT/META 给出“开支可控 + 云增速不塌”组合并引发成长股拓宽反弹；  
3) FOMC 明确压低近月加息概率、2Y 回落 >15bp。

**vs last week**:  
上周核心是 AI/semi derating + 油价初升。本周油价二次加速，同时 GOOGL/TSLA 把 derating 从芯片扩展到 **平台股现金流**；曲线仍正但 2Y 急升改变贴现率。Regime 标签从 “AI Derating / Stagflation-lite Overlay” 升级为以 **Capex 消化 + 能源通胀** 双主轴。

---

## 9. 异常与背离 | Anomalies

| # | 观察 | 可能解释 | 交易含义 |
|---|------|----------|----------|
| 1 | SPX 仅 −0.6% 但 TSLA −18%、数只 Mag7 −6%~−8% | 权重分散与非 Mag7 对冲（能源/工业） | 看指数易误判风险；交易需下沉到个股/行业 |
| 2 | VIX 略降而收益率大涨、油价大涨 | 市场用利率而非纯 vol 重新定价 | 对冲优选用 duration/能源，而非只买 VIX |
| 3 | SOXX 周 +1% 但 MTD −18%；MU 大涨 | 芯片内部记忆体 vs GPU/设备分化 | 选股 > 买贝塔 |
| 4 | HY OAS 仅 +6bp vs 股债商品巨震 | 信用尚未确认风险off | 若 HY OAS 单周 >+15–25bp，则升级为系统性 |

---

## 10. 下周策略 | Next-Week Playbook

### Base case
FOMC **持息**（3.50–3.75%），但声明/发布会偏“数据依赖 + 抗通胀决心”，因油价与关税使点阵图叙事继续 hawkish。美股高波动、板块分化：能源与质量现金流相对占优，高 Capex 成长股跟随个股指引剧烈波动。AI 叙事继续从“需求证明”切换到“回报与 FCF”。

### Scenarios

| 情景 | 概率 | 触发条件 | 资产表现 |
|------|------|----------|----------|
| Bull | 25% | 油价回落 + FOMC 压低加息概率 + MSFT/META capex 可控 | NDX 反弹、XLE 回调、HY 收窄 |
| Base | 50% | Hold + 偏鹰沟通；财报分化 | SPX 高波动区间；Energy/Quality > Spec Growth |
| Bear | 25% | 加息或极鹰 + Brent 站稳 >100 + Mag7 指引差扩散 | NDX 深调、VIX>22、HY OAS 走阔加速 |

### Conviction setups (≤3)

1. **FOMC 沟通波动率** — Direction: long event-vol / barbell（短久期 + 价值/能源）· Instrument: 2Y 利率敏感资产 / XLE vs QQQ pair · Trigger: 决议日前后 · Invalidation: 2Y 收益率单日回落 >15bp 且 NDX 放量收复 · Horizon: 1 周  
2. **AI Capex 指引差** — Direction: 财报后反应交易 · Instrument: MSFT/META/AMZN 个股期权或股票 · Trigger: capex 上修且 FCF 指引恶化 → fade；云增速超预期且开支路径清晰 → dip-buy 质量标的 · Invalidation: 与价格行为相反的二次指引澄清 · Horizon: 3–10 个交易日  
3. **能源风险溢价** — Direction: 趋势多但降杠杆 · Instrument: XLE / WTI 结构 · Trigger: Hormuz/Red Sea 头条未缓和 · Invalidation: Brent 日收回到 <92 且航运新闻缓和 · Horizon: 1–2 周

### Positioning
- **Risk budget**: hold / 略减（事件密集）  
- **Overweight**: Energy、高 FCF 质量科技（相对）、Memory（MU 波段）  
- **Underweight / avoid**: 高叙事、低利润 EV/AI 应用层；盲目追 SOXX 贝塔  
- **Thesis reset if**: FOMC 后 2Y −20bp 且 WTI <85 同时出现

---

## 附录 | Appendix

- **Sources**: FRED（`BAMLH0A0HYM2`,`T10Y2Y`,`DGS2`,`DGS10` via `scripts/fetch_fred.py`）；Yahoo Finance；USTR / White House Section 301；Alphabet / Tesla / TI / IBM / ServiceNow IR & SEC exhibits；TrendForce；DOL Claims；S&P Global PMI；CME FedWatch（二手引用 Reuters/Forbes）；CNBC/NBC/Reuters 地缘报道；OpenAI API pricing page  
- **Disclaimer**: Research for informational purposes; not investment advice. Verify prices before trading.  
- **Changes vs prior report**（week ending 2026-07-17）:  
  - HY OAS 271→277bp（+6）；10Y-2Y 0.37%→0.36%；VIX 18.77→18.58  
  - SPX 7458→7412；油价从 ~82 再冲至 ~90  
  - 轮动从“Semi 单边 derating”扩展为“平台股 Capex/FCF 冲击 + 能源通胀”  
  - 新触媒：GOOGL capex $195–205B；Section 301 关税生效；FOMC 本周决战  
