# 周度市场检测报告 | Weekly Market Scan

**报告周期**: Week ending 2026-07-17  
**生成时间**: 2026-07-18 08:15 CST  
**覆盖范围**: Global macro + US equities（不含 A股、港股）  
**数据截止**: 权益/商品/波动 as-of 2026-07-17 close（Yahoo）；FRED 信用/曲线 as-of 2026-07-16/17

---

## 执行摘要 | Executive Summary

1. **Regime**: AI Derating / Stagflation-lite Overlay（置信度 M）— 软通胀数据被原油地缘溢价与科技估值重定价对冲。
2. **Top move**: WTI 周涨约 +14.5%（至 ~$81.8），同期 NDX −4.1%、SOXX −10.2%；VIX 自 15.03 升至 18.77。
3. **Rotation**: FROM XLK/SOXX/Growth → TO XLE/XLRE/XLP/XLF（能源 + 防御/价值）。
4. **Key risk**: 霍尔木兹/红海供应链若持续中断 → 油价冲向 $100 叙事再定价；FOMC（7/28–29）前政策路径分歧扩大。
5. **Playbook**: 降低 AI/半导体重仓 beta，保留能源相对多头与防御对冲；下周以 GOOGL/TSLA 验证 AI capex 叙事是否破裂。

---

## 1. 大类资产仪表盘 | Cross-Asset Dashboard

| 资产 | 标的 | 1W | MTD | YTD | 52W区间位置 | 驱动 |
|------|------|-----|-----|-----|-------------|------|
| 美股 | SPX | −1.55% (7457.69) | −0.6% | +8.9% | 高位回撤 | Mag7/半导体重压指数 |
| | NDX | −4.13% (28592.66) | −5.6% | +13.2% | 自高点显著回撤 | AI 估值与 capex 质疑 |
| | RUT | −0.52% (2962.22) | −2.1% | +19.4% | 相对抗跌 | 指数集中度拖累 vs 广度 |
| 利率 | UST 10Y (FRED `DGS10`) | 4.57% (+1bp vs 07-10；as-of 07-16) | — | — | — | CPI 偏软但油价对冲降息预期 |
| | UST 2Y (FRED `DGS2`) | 4.16% (−5bp vs 07-10；as-of 07-16) | — | — | — | 前端利率回落 |
| | **10Y-2Y (FRED `T10Y2Y`)** | **0.37% (+2bp vs 07-10；as-of 07-17)** | +8bp (1M) | — | 正斜率 | 略 steepening |
| 信用 | **HY OAS (FRED `BAMLH0A0HYM2`)** | **271bp (+2bp vs 07-10；as-of 07-16)** | 0bp (1M) | — | 仍紧 | 轻微 widening，非压力飙升 |
| 外汇 | DXY | −0.22% (100.75) | — | — | 中位震荡 | 收益率回落与风险偏好博弈 |
| 商品 | WTI | **+14.5% (~$81.77)** | +17.7% | +42.4% | 冲高 | 美伊冲突 / 霍尔木兹流量骤降 |
| | Gold | −1.98% (~$4023) | ~flat | −7.0% | 高位整理 | 油价通胀预期 vs 实际利率 |
| | Copper | +0.64% (~$6.27/lb) | — | — | — | 需求信号弱于油价供给冲击 |
| 波动 | VIX | **18.77 (+3.74)** | +14.1% | +25.6% | 自低波抬升 | 科技抛售 + 地缘；仍非恐慌区 |

**Cross-asset read**（事实→解读）: 本周是典型的 **“软数据 + 硬冲击”** 组合——6 月 CPI/PPI 显著低于预期，但美伊冲突再升级推动原油周涨双位数，形成 stagflation-lite 定价。权益端呈现 **指数跌、广度尚可**（Morningstar 覆盖样本约 57% 上涨）：抛售高度集中在 AI/半导体（SOXX −10%），而非全面 risk-off。信用 HY OAS 仅 +2bp，说明资金在做 **估值与 beta 再定价**，而非信用危机。曲线略陡（10Y-2Y +2bp）与 2Y 下行一致：前端定价更鸽，长端被能源溢价托住。

---

## 2. 宏观与政策 | Macro & Policy

### 2.1 本周回顾

#### 2.1.1 数据发布

| 日期 | 事件/数据 | 实际 vs 预期 | 市场反应 | 解读 |
|------|-----------|--------------|----------|------|
| 07-14 | CPI (Jun) | Headline −0.4% m/m / 3.5% y/y vs ~−0.1%/3.8%；Core 0.0% / 2.6% vs ~0.2%/2.9%（BLS / CNBC） | 初期利率下挫、风险资产获支撑；但周内被油价与科技抛售覆盖 | **事实**: 最大单月跌幅之一（自 2020-04）；能源回落主导。**解读**: 为 Warsh/FOMC 提供喘息，但样本期早于本周油价再冲高 |
| 07-15 | PPI (Jun) | −0.3% m/m / 5.5% y/y vs ~−0.15%/6.2%（日历汇总） | 延续“降温”叙事 | 生产端同步放缓，强化近端 disinflation 证据 |
| 07-16 | Retail Sales (Jun) | +0.2% vs ~0.3%；ex-auto −0.2% vs ~−0.1% | 温和负面 | 消费动能略软，配合“增长放缓 + 油价上行”的 stagflation 想象 |
| 07-16 | Initial Claims (w/e 07-11) | 208k vs ~216–217k；续请 1.805M | 债市/股指反应有限 | 劳动力市场仍低解雇；“招聘弱、解雇也弱”格局延续 |
| 07-17 | Industrial Production (Jun) | +0.1% vs ~0.2%；制造业持平 | 边缘负面 | 工业温和，无衰退信号 |
| 07-17 | U.Mich Sentiment (Jul prelim) | 54.4 vs ~51.3；前值 49.5 | 美元/黄金波动有限 | **解读**: 调查窗口多在 7/7 打击升级前完成；官方亦提示油价回升或令改善难持续 |

#### 2.1.2 要闻、讲话与政策动态

| 日期 | 类型 | 事件/讲话人 | 核心要点 | 市场反应 | 解读 |
|------|------|-------------|----------|----------|------|
| 07-13 | 讲话 | Waller 等 FOMC 官员 | Waller：若通胀再“热”需考虑近端加息 | 为 CPI 定调；利率波动加大 | 黑出期前最后一轮发言窗口 |
| 07-14/15 | 讲话 | **Fed Chair Kevin Warsh** Humphrey-Hawkins（众/参） | 重申 2% 目标、“对持续高通胀零容忍”；刻意不给 7/28–29 路径暗示；批评过度 forward guidance | 收益率震荡；美元未单边走强 | **事实**: 新主席首次国会听证。**判断**: 委员会内部分歧大，主席选择“少说”抬升事件风险溢价 |
| 07-15 | 讲话 | Gov. Lisa Cook | 数据中心/芯片/公用事业等 AI 相关支出或推升广义物价；通胀风险权重上升 | 助推“AI→通胀”叙事 | 与科技股估值压力形成共振 |
| 07-13–17 | 地缘 | **美伊冲突再升级**；霍尔木兹流量大幅下滑（媒体引 Kpler：确认原油过境约 −62%）；红海/Bab el-Mandeb 风险再提 | WTI/Brent 周涨约 +12–15%；能源股领涨 | **一阶**: 能源通胀溢价。**二阶**: 软 CPI 的政策红利被部分对冲 |
| 07-16 | 监管/产业 | TSMC 上修 2026 capex 至 $60–64B（自 $52–56B 上沿） | 盘前/盘中半导体连锁下跌 | 需求确认 vs FCF/利润率稀释的定价冲突 |

### 2.2 下周日历

| 日期 | 事件 | 影响等级 H/M/L | 关注资产/行业 |
|------|------|----------------|---------------|
| 07-20 | Leading Indicators；区域银行财报（ZION 等） | L–M | XLF / 区域银行 |
| 07-21 | GM、SCHW、KEY 等财报 | M | XLY / XLF |
| 07-22 | **GOOGL、TSLA、INTC、NOW、T** 等 | **H** | NDX / XLK / XLC / SOXX |
| 07-23 | Claims；VZ、HBAN 等 | M | 利率 / 电信 |
| 07-24 | PMI / New Home Sales（视发布） | M | 增长敏感板块 |
| 07-28–29 | **FOMC**（再下周） | **H** | 全市场；当前市场基线偏 hold |

**Macro narrative**: 数据面给了 “inflation cooling” 的战术窗口，但 **能源地缘把 7 月通胀路径重新打开**。Warsh 拒绝路径承诺，叠加委员会分歧，使得 7/28–29 FOMC 的沟通风险上升。权益定价主线已从“软着陆叙事”切换到 **“AI ROI 质询 + 能源冲击”**。

---

## 3. 股市结构 | Equity Market Structure

| 指标 | 数值 | 1W Δ | 信号 |
|------|------|------|------|
| 上涨/下跌家数（Morningstar 覆盖样本） | ~57% 上涨 / ~42% 下跌 | 指数跌而多数上涨 | **广度好于指数** — 集中抛售 |
| Large vs Small | Large −1.90% / Small −0.15%（Morningstar） | 大盘更弱 | Mega-cap / 成长拖累 |
| Growth vs Value | Growth −4.12% / Value +0.54% | 显著风格切换 | 反转上周 XLK 领涨 |
| NH/NL / >50DMA / >200DMA | 本周未获统一权威日更 | — | 标注数据缺口；以风格/板块代理 |
| 指数涨幅中 Top 权重贡献 | NVDA/半导体权重为主要拖累；AAPL 对冲部分跌幅 | — | 集中度风险显性化 |

**Style / factor**: Value > Growth；Small 相对 Large 抗跌；Low-vol/防御（XLP、XLRE）获资金。

**Flow / positioning**: 期权月度到期（07-17）叠加芯片波动，放大盘中振幅（Saxo 等指出 dealer hedging 可能加剧尾盘波动）。**解读**: 位置拥挤的 AI 多头在去杠杆。

**Structure read**: 这是 **窄基下跌（narrow selloff）**：指数因科技权重受损，但等权/多数个股并未崩溃。若下周 GOOGL 能稳住 AI capex→收入映射，则更像 consolidation；若 hyperscaler 指引令人失望，则广度优势可能消退。

---

## 4. 行业轮动 | Sector & Industry Rotation

### 4.1 GICS 一级 — 相对 SPX（SPX 1W = −1.55%）

| 行业 | ETF | 1W abs | 1W rel SPX | 驱动标签 | RS趋势 |
|------|-----|--------|------------|----------|--------|
| Energy | XLE | **+4.72%** | **+6.3pp** | 地缘油价 | ↑ |
| Real Estate | XLRE | +2.18% | +3.7pp | 利率回落+防御 | ↑ |
| Consumer Staples | XLP | +1.27% | +2.8pp | 防御轮动 | ↑ |
| Financials | XLF | +0.99% | +2.5pp | 价值/曲线 | ↑ |
| Health Care | XLV | +0.16% | +1.7pp | UNH 财报支撑 | →/↑ |
| Utilities | XLU | −0.53% | +1.0pp | 防御但弱于 staples | → |
| Materials | XLB | −0.71% | +0.8pp | 铜弱于油 | → |
| Communication | XLC | −0.89% | +0.7pp | NFLX 拖累 | ↓ |
| Industrials | XLI | −1.38% | +0.2pp | 跟随大盘 | → |
| Discretionary | XLY | −1.54% | ~0pp | TSLA 疲软 | → |
| **Technology** | **XLK** | **−5.48%** | **−3.9pp** | AI/半导体重估 | ↓ |

### 4.2 细分行业亮点

**领涨**: Energy / Refiners（如 DINO 周涨约 +13%）— 油价与裂解逻辑。  
**领跌**: Semiconductors（SOXX −10.2%）；个股极端：SNDK ≈−29%、IBM ≈−26%、MRVL ≈−20%、MU ≈−13%、SKHY ≈−8%。

### 4.3 轮动结论

**资金方向**: FROM XLK/SOXX/高估值 AI → TO XLE + 防御（XLRE/XLP）+ 部分金融。  
**证据**: 绝对收益分化 >5pp；Morningstar 行业排序一致；与上周 “XLK 领涨、XLV/XLP 落后” **方向反转**（carry-over theme 翻转）。

---

## 4.5 AI 产业链 & Capex | AI Supply Chain Tracker

### 4.5.1 HBM / 内存价格

| 指标 | 本期 | 1W/1M Δ | 来源 | 解读 |
|------|------|---------|------|------|
| HBM（HBM3e / blended） | 供给仍紧；TrendForce：3Q26 HBM 价格预计 +8–13% QoQ（vs 2Q26 +53–58%） | 本周无新周度 spot 打印；QoQ 涨幅预期 **放缓** | TrendForce / InfotechLead 综述（Jul 2026） | 紧平衡持续，但涨价斜率见顶 |
| DRAM（conventional / server） | 3Q26 合约价预期 +13–18% QoQ（vs 2Q26 +58–63%）；server DRAM 受 LTA 约束 | vs last report：叙事从“暴涨”切到“减速上涨” | TrendForce 07-03 / 07-09 | LTA 限制对 CSP 提价空间 |
| HBM 可投资性 | SKHY ADR 本周 ≈−8.3%；MU ≈−13.3% | 股价领先基本面回撤 | Yahoo 07-17 | 市场在交易 “稀缺溢价是否过度” |

### 4.5.2 云 GPU 租赁价格 ($/GPU-hr)

| 厂商 | SKU | On-demand | 1W Δ | 信号 |
|------|-----|-----------|------|------|
| AWS | p5 / H100 | ~$6.88 | unchanged vs last run | 列表价稳定 |
| GCP | a3-highgpu-8g (H100) | ~$10.98–11.06 | unchanged | 高位稳定 |
| Azure | ND H100 v5 | ~$6.98–12.29（SKU 依赖） | unchanged | 区间报价不变 |
| CoreWeave | H100 HGX | ~$6.16 | unchanged | 专业云仍折价于部分 hyperscaler |
| 参考 | Crusoe / Lambda | ~$3.90 / ~$4.29（07-17 观测） | — | 现货竞争层更便宜 |

**解读**: 租赁列表价 **WoW 无显著变动**；本周科技抛售由 **估值/ROI/开源模型冲击叙事** 驱动，而非云算力现货崩价。

### 4.5.3 AI API 定价 ($/1M tokens)

| 厂商 | Model | Input | Output | 本周变动? |
|------|-------|-------|--------|-----------|
| OpenAI | GPT-5.5 | $5.00 | $30.00 | N（延续） |
| OpenAI | GPT-5.6 Sol / Terra / Luna | $5 / $2.50 / $1.00 | $30 / $15 / $6 | 上周五 GA 后本周无新降价；GPT-5.4 计划 07-23 退役 |
| OpenAI | GPT-4o | $2.50 | $10.00 | N |
| Anthropic | Claude Sonnet 5 | $2.00 | $10.00 | N（intro 至 2026-08-31，其后 $3/$15） |
| Anthropic | Claude Opus 4.8 | $5.00 | $25.00 | N |
| Google | Gemini 2.5 Pro | $1.25 | $10.00 | N |
| Google | Gemini 3.1 Pro | $2.00 | $12.00 | N |

**解读**: API 价格层稳定；周五有关开源模型（如 Moonshot Kimi）逼近前沿基准的报道，强化 “模型层护城河变薄 → 训练资本开支回报不确定” 的交易叙事（事实为舆情催化，因果为解读）。

### 4.5.4 Hyperscaler AI Capex

| 公司 | Capex / Guide | YoY | AI 评论 | 1W 更新 |
|------|---------------|-----|---------|---------|
| MSFT | 维持高 capex 指引（待月末财报验证） | 高增 | Azure/AI 变现仍是市场焦点 | 股价周 +2.3%，相对抗跌 |
| GOOGL | Q1 曾上修 FY capex 至 $180–190B 量级（待 07-22 更新） | 显著 | Cloud/TPU/Gemini | **下周关键验证点** |
| AMZN | AWS 支撑 AI 投入 | 高 | — | 周 +0.8%，跟随大盘 |
| META | Hyperion/LA 项目扩容叙事（媒体：$50B+ / 5GW） | 上修预期 | “Capex→可出租算力”叙事 | 周 −3.5%，回吐部分涨幅 |
| TSMC（供应链） | **2026 capex $60–64B**（上修） | 上修 | AI 需求强但利润率稀释担忧 | 触发连锁半导体抛售 |
| Hyperscaler 合计 | 记忆基线仍约 $650–725B CY2026 讨论区间 | — | — | 无新官方合计；**vs last report: unchanged aggregate band** |

**AI stack synthesis**: 成本曲线（HBM/GPU 租用/API）本周 **价格层稳定**，但 **权益风险溢价上升**——市场质疑的是 ROI 与拥挤交易，而非现货算力崩盘。Capex 周期仍在加速（TSMC 上修、META 扩容），却同步触发 “支出过大/回报滞后” 定价，SOXX/XLK 周度大幅跑输。利润池短期仍偏内存与先进代工，但 MU/SKHY 股价显示 **稀缺溢价亦可快速压缩**。下周 GOOGL（及随后 MSFT 等）指引将决定该 derating 是健康换手还是趋势反转。

---

## 5. 重点事件与传导 | Events & Transmission

### 5.1 事件传导矩阵

| 日期 | 事件 | 一阶影响 | 二阶影响 | 定价状态 |
|------|------|----------|----------|----------|
| 07-14 | 软 CPI + Warsh 听证 | 实际利率预期下修 | 政策路径不确定性↑ | 数据利好部分被地缘对冲 |
| 07-13–17 | 美伊升级 / 霍尔木兹 | 油价 +12–15% | stagflation-lite、能源股、通胀预期 | **仍 debated**（de-escalate 期权未关闭） |
| 07-16 | TSMC capex 上修 | 半导体重挫 | AI capex 担忧扩散至 Mag7 | 定价差：基本面强 vs 股价弱 |
| 07-16/17 | NFLX 指引失望 | NFLX ≈−6～−9% | XLC 情绪、成长股风险偏好 | 指引差已部分 price-in 于周五 |
| 07-17 | 期权月度到期 | 波动放大 | 技术性抛压 | 周末后需观察真实需求 |

### 5.2 重要公司财报与预期差

#### 5.2.1 本周已发布

| 日期 | Ticker | EPS 实际 vs 共识 | 营收 实际 vs 共识 | 指引/关键点 | 预期差 | 股价反应 | 板块含义 |
|------|--------|------------------|------------------|------------|--------|----------|----------|
| 07-16 | **NFLX** | $0.80 vs ~$0.79 | $12.56B vs ~$12.58–12.59B | Q3 收入指引 ~$12.86B / EPS ~$0.82 **低于** 街预期 ~$13.0B / $0.84；收窄 FY 收入区间；观看时长报告降频 | **指引差 + 定价差** | 约 −7% 至 −9%（07-17） | 成长股容错率下降；XLC 承压 |
| 07-16 | **UNH** | Adj $6.38（公司披露）大幅好于情境预期 | 收入 $112.0B | FY26 adj EPS 指引上修至 $19.50–$20.00 | **共识差/指引差正** | 盘前大涨，全周约 +0.3%（涨幅回吐） | 支撑 XLV；医保成本叙事缓解 |
| 07-16 | **TSM**（ADR 链） | EPS ~$4.31 vs ~$3.80 | 创纪录利润（+77% y/y 量级） | **Capex 上修至 $60–64B**；2nm 利润率稀释讨论 | **定价差**（好财报+坏反应） | 连锁拖累 NVDA/AMD/MU 等 | AI 供应链 “好消息即坏消息” |

#### 5.2.2 下周预告

| 日期 | Ticker | 共识 EPS / 营收 | 隐含波动/关注点 | 为何重要 | 预期差观察点 |
|------|--------|-----------------|-----------------|----------|--------------|
| 07-21 | GM | ~$3.13 / ~$46.0B（Zacks） | 汽车需求/库存 | 周期消费 | 北美利润 vs 中国重组 |
| 07-22 | **GOOGL** | ~$2.86–2.89 / ~$114–117B | Cloud ~+63% 预期；capex 轨迹 | **首家大权重 hyperscaler 验证 AI 抛售后叙事** | Cloud 增速、capex 指引、广告韧性 |
| 07-22 | **TSLA** | ~$0.52 / ~$26.0B（TipRanks 等） | 高 IV | Mag7 + 可选消费风险资产 | 交付/利润率/机器人叙事 |
| 07-22 | INTC / NOW | 视街预期 | 半导体重估 / 软件倍数 | 板块情绪 | 指引是否确认 capex 放缓担忧 |
| 07-23 | VZ 等 | — | 防御电信 | 轮动确认 | 相对 XLK 资金是否停留 |

#### 5.2.3 预期差摘要

| Ticker | 市场定价/共识 | 实际结果 | 预期差类型 | 反应是否匹配 | 交易含义 |
|--------|---------------|----------|------------|--------------|----------|
| NFLX | 要增长再加速 | 季度大致符合，前瞻偏低 | 指引差 | 匹配（下跌） | 成长股“符合不够” |
| TSM | AI 需求强应上涨 | 需求确认但 capex↑ | 定价差 | 背离（利好→下跌） | 交易拥挤，利好出尽 |
| UNH | 医保成本担忧 | 业绩与指引双强 | 共识差正 | 部分匹配（周涨有限） | 防御配置有基本面支撑 |

**Earnings tone**: 仍处财报季早期；本周基调是 **“前瞻与资本开支 > 当期 beat”**。淡季已过，下周 Mag7 启动（GOOGL/TSLA）为高影响窗口。

---

## 6. 重点股票 | Watchlist & Systemic Names

### 6.1 观察列表（Mag7 + HBM + 本周异动）

| Ticker | 1W | 催化剂 | 技术位 | 观点 |
|--------|-----|--------|--------|------|
| NVDA | −3.9% (202.81) | AI ROI 质疑；开源模型舆情 | 失守周初区间，关注能否站回 ~210 | 核心 beta；等 GOOGL/MSFT 验证 |
| META | −3.5% (646.01) | Compute/云叙事回吐 | 自 680+ 回落 | 叙事未死，波动加大 |
| AAPL | **+5.8%** (333.74) | 相对避风港；07-30 财报 | 强势 | Mag7 内部分化多头 |
| MSFT | +2.3% (393.82) | Azure 验证临近 | 相对抗跌 | 观察能否延续相对强度 |
| AMZN | +0.8% (247.23) | AWS | 跟随 | 中性 |
| GOOGL | −2.9% (346.77) | **07-22 财报** | 预减仓后波动 | 下周最重要单点 |
| TSLA | −6.6% (380.84) | **07-22 财报** | 偏弱 | 高 beta 风险资产 |
| MU | −13.3% (848.95) | HBM 溢价压缩 | 大幅回撤 | 内存周期交易降温 |
| SKHY | −8.3% (154.03) | 上市后波动 | — | HBM 可投资性代理 |
| NFLX | −6.0% (68.95) | 指引差 | 新低区附近 | 避免接刀直至预期重置 |

### 6.2 系统性/指数权重异动

| Ticker | 1W | 原因 | 板块含义 |
|--------|-----|------|----------|
| NVDA | −3.9% | AI 估值重压主因 | 对 SPX/NDX 贡献显著为负 |
| AAPL | +5.8% | 防御性成长 | 部分对冲 Mag7 拖累 |
| IBM | −26.0% | 公司特定/指引冲击（Morningstar） | 软件/服务情绪 |
| MRVL | −20.0% | 半导体 beta | SOXX 杀估值 |
| SNDK | −29.3% | 存储器高位回撤 | 投机拥挤解除 |

---

## 7. 风险与流动性 | Risk Dashboard

| 指标 | 现值 | 1W Δ | 解读 |
|------|------|------|------|
| VIX / term structure | 18.77；此前 contango 仍在（周中 Saxo：VIX3M > spot） | +3.74 | 风险溢价抬升，尚未 panic（>25） |
| **HY OAS (FRED)** | **271bp** (as-of 07-16) | **+2bp** | 信用稳健；未触发 >25bp 警报 |
| **10Y-2Y (FRED)** | **0.37%** (as-of 07-17) | **+2bp** | 缓陡；非衰退倒挂 |
| Financial conditions | HY 紧 + 股指回撤 + 油价冲高 | 混合 | 金融条件未全面收紧，但增长/通胀组合恶化 |
| SPX–TLT | TLT 周约 +0.1%，股债同向保护有限 | — | 股跌债未大涨 → 通胀/油价干扰久期对冲 |

**Triggered alerts**:  
- 原油周涨 >10% + 地缘（自定义高影响）  
- SOXX 周跌 >10%（拥挤交易去化）  
- HY OAS 未触发（仅 +2bp）

**Watch levels next week**:  
- WTI $78 / $85 / $100 叙事阈值  
- VIX 20 整数  
- NDX 能否守住 ~28,300–28,500 支撑带  
- GOOGL 财报后 XLK/SOXX 方向确认

---

## 8. 市场 Regime | Regime Classification

**Primary regime**: AI Derating / Stagflation-lite Overlay（Geopolitical Energy）  
**Confidence**: **M**  
**Falsifiers**:  
1) 霍尔木兹实质性复航且 WTI 回落至 $75 下并带动实际利率预期下降；  
2) GOOGL/MSFT 上修 Cloud/AI 变现并安抚 capex ROI，带动 SOXX 周度反弹 >5%；  
3) HY OAS 单周走阔 >25bp（则升级为真正 risk-off）。

**vs last week**: 上周 = Risk-on Mega-cap / Geopolitical Energy Overlay（Mag7 反弹、XLK 领涨）。本周 **风格与板块完全反转**：Mega-cap/AI 成为供给冲击，能源溢价从“叠加”变为“主导叙事之一”。

---

## 9. 异常与背离 | Anomalies

| # | 观察 | 可能解释 | 交易含义 |
|---|------|----------|----------|
| 1 | 指数下跌但 ~57% 个股上涨 | 抛售集中在 AI 权重 | 等权/breadth 策略相对占优；勿线性外推全面熊市 |
| 2 | 软 CPI vs 油价暴涨 | 数据滞后 vs 实时冲击 | 7 月通胀预期重置；淡化单一 CPI 交易 |
| 3 | TSMC 业绩大超但股价链下跌 | capex/利润率担忧 + 拥挤 | fade 短期超跌需等待指引，不宜追空基本面强者 |
| 4 | HY OAS 仅 +2bp 而 VIX +3.7 | 股权波动 ≠ 信用压力 | 信用尚未确认 risk-off；更偏估值调整 |
| 5 | 金价周跌而地缘升温 | 实际利率/仓位拥挤/油价挤出 | 金的对冲效率本周下降；能源更直接 |

---

## 10. 下周策略 | Next-Week Playbook

### Base case
基准情形（约 45%）：油价在高位震荡（WTI $78–86），美伊冲突维持 “escalate-to-negotiate” 预期；GOOGL 交出“够用”的 Cloud 增速但不大幅上修 capex 焦虑 → XLK 企稳但反弹受限；SPX 周度震荡偏弱。FOMC 前波动抬升，VIX 维持 16–22。

### Scenarios

| 情景 | 概率 | 触发条件 | 资产表现 |
|------|------|----------|----------|
| Bull | 25% | 地缘缓和信号 + GOOGL Cloud/广告双强 + capex ROI 表述积极 | NDX/SOXX 反弹；WTI 回落；VIX→15 |
| Base | 45% | 油价高位震荡；财报喜忧参半 | 板块轮动延续；指数 ±1.5% |
| Bear | 30% | 霍尔木兹实质中断延长 / GOOGL capex 再上修且利润率指引差 / VIX>22 | 股债双杀风险；XLE 独强；HY 开始走阔 |

### Conviction setups (≤3)

1. **能源相对科技（XLE vs XLK）** — Direction: 多相对价差 · Instrument: XLE long / XLK short 或已有组合内倾斜 · Trigger: WTI>$80 且 SOXX 反弹乏力 · Invalidation: WTI 收于 $76 下且 GOOGL 后 SOXX 单日 +4% · Horizon: 1–3 周  
2. **GOOGL 事件驱动** — Direction: 波动收割或财报后方向跟随 · Instrument: GOOGL 或 QQQ · Trigger: Cloud 增速显著低于 ~60% 预期或 capex 再大幅上修 · Invalidation: Cloud 超预期且管理层强化变现 · Horizon: 事件周  
3. **防御对冲保留** — Direction: 持有 XLP/XLRE 相对超配 · Trigger: VIX>18 维持 · Invalidation: VIX 回<15 且 XLK 重新领涨 · Horizon: FOMC 前

### Positioning
- **Risk budget**: **reduce** AI/半导体 beta；总体风险中性偏低  
- **Overweight**: Energy、部分 Staples/REITs、相对强势的 AAPL/MSFT（选择性）  
- **Underweight / avoid**: 高估值无现金流转折的半导体卫星票；追空 TSM/NVDA 基本面强者需谨慎  
- **Thesis reset if**: WTI 周线收于 $75 下 **且** GOOGL/MSFT 明确 AI 变现 → 回到风险偏好/AI 领导体制

---

## 附录 | Appendix

- **Sources**: FRED (`BAMLH0A0HYM2`,`T10Y2Y`,`DGS2`,`DGS10` via `scripts/fetch_fred.py`); Yahoo Finance (equities/sectors/commodities 07-17 close); BLS CPI; AP / Morningstar weekly wrap; CNBC/LSEG (NFLX); UnitedHealth IR; TrendForce; vendor GPU/API pricing pages (Silicon Analysts / ComputeTape / OpenAI / Anthropic); Fed / press (Warsh testimony).  
- **Disclaimer**: Research for informational purposes; not investment advice. Verify prices before trading.  
- **Changes vs prior report** (week ending 2026-07-10):  
  - Regime: Risk-on Mega-cap → **AI Derating / Stagflation-lite**  
  - Rotation 反转: 上周 TO XLK → 本周 **FROM XLK TO XLE/防御**  
  - VIX 15.03→18.77；HY OAS 269→271bp；10Y-2Y 0.35%→0.37%  
  - AI: GPU/API 价格层 unchanged；HBM/DRAM 叙事转为 QoQ 涨幅放缓；TSMC capex 上修成新催化剂  
  - 地缘溢价升级：WTI 由上周约 +4% 升至本周约 +15%
