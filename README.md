# lehmanbear — 雷曼 / 贝尔斯登 破产危机原始素材库

> 本仓库搜集 2008 年全球金融危机中 **雷曼兄弟（Lehman Brothers）** 与 **贝尔斯登（Bear Stearns）** 两宗标志性崩盘事件的原始公开材料，作为**小说 / 非虚构写作的基本素材**。
> 每份材料均保留**原始 PDF（一手证据）** 与 **转换后的 Markdown（可检索文本层）** 两套，便于引用与检索。
> 📦 **一键下载全部 33 个原始 PDF（≈41 MB）**：[GitHub Release v1.0](https://github.com/bitiworm/lehmanbear/releases/tag/v1.0)

---

## 一、素材来源与主题

### A. 雷曼兄弟 — Valukas 破产审查官报告（9 卷）
破产法院任命审查官 **Anton R. Valukas** 强制调取约 3500 万页材料后出具的审查报告。公开版含海量 Fuld、Lowitt 等人邮件、融资 / 会计造假文档，并通过脚注超链接到原始邮件 / 备忘录。

| 卷 | Markdown | 原始 PDF | 主题 |
|----|----------|----------|------|
| 第1卷 | `md/lehman_valukas_vol1_intro_execsummary_risk.md` | `pdfs/lehman_valukas_vol1_intro_execsummary_risk.pdf` | 引言 / 执行摘要 / 程序背景 / 风险（Section I–III.A.1） |
| 第2卷 | `md/lehman_valukas_vol2_valuation_survival.md` | `pdfs/lehman_valukas_vol2_valuation_survival.pdf` | 估值 / 生存能力（III.A.2–III.A.3） |
| 第3卷 | `md/lehman_valukas_vol3_repo105.md` | `pdfs/lehman_valukas_vol3_repo105.pdf` | **Repo 105**（III.A.4）— 「window dressing」会计手法核心证据 |
| 第4卷 | `md/lehman_valukas_vol4_lenders_govt.md` | `pdfs/lehman_valukas_vol4_lenders_govt.pdf` | 担保贷款人 / 政府（III.A.5–III.A.6，含 2008年9月 与摩根大通 / 美联储敏感往来） |
| 第5卷 | `md/lehman_valukas_vol5_avoidance_barclays.md` | `pdfs/lehman_valukas_vol5_avoidance_barclays.pdf` | 撤销权诉讼 / 巴克莱交易（III.B–III.C） |
| 第6卷 | `md/lehman_valukas_vol6_appendix1.md` | `pdfs/lehman_valukas_vol6_appendix1.pdf` | 附录 1 |
| 第7卷 | `md/lehman_valukas_vol7_appendices2-7.md` | `pdfs/lehman_valukas_vol7_appendices2-7.pdf` | 附录 2–7（部分页为扫描件） |
| 第8卷 | `md/lehman_valukas_vol8_appendices8-22.md` | `pdfs/lehman_valukas_vol8_appendices8-22.pdf` | 附录 8–22（含大量高管邮件；多页为扫描件） |
| 第9卷 | `md/lehman_valukas_vol9_appendices23-34.md` | `pdfs/lehman_valukas_vol9_appendices23-34.pdf` | 附录 23–34（含 JP Morgan / 美联储 2008年9月通讯等） |

> 原始镜像：Stanford（`web.stanford.edu/~jbulow/Lehmandocs/`）+ Yale EliScholar（`elischolar.library.yale.edu/ypfs-documents/678`）。
> 众议院听证会摘要（审查官 Valukas 2009-04-20 作证）：`md/lehman_house_hearing_valuks_2009.md` / `pdfs/lehman_house_hearing_valuks_2009.pdf`。

### B. 贝尔斯登 — Cioffi / Tannin 对冲基金崩盘邮件（最早一批次贷内部邮件）
两只基金在 2007 年春明知恶化、对外仍称健康；SEC 起诉 + FCIC 存档放出大量私人 / 工作邮件，含那句著名的风险警示。

> 全部 23 份均来自 Yale YPFS / FCIC 存档（`elischolar.library.yale.edu/ypfs-documents/<编号>/`，直连受 WAF 限制，经 Wayback 存档抓取）。括号内为 FCIC 存档编号。

| FCIC# | 主题（简） | Markdown | 原始 PDF |
|------|-----------|----------|----------|
| 4183 | Crystal→Cioffi 等（SRP 二月回报） | `md/bear_stearns_crystal_to_cioffi.md` | `pdfs/bear_stearns_crystal_to_cioffi.pdf` |
| 4184 | Tannin→Borg-Brenner | `md/bear_stearns_tannin_to_borg_brenner.md` | `pdfs/bear_stearns_tannin_to_borg_brenner.pdf` |
| 4185 | **Tannin→Cioffi 风险警示（2007-04-22）** | `md/bear_stearns_email_4185_tannin_to_cioffi_2007-04-22.md` | `pdfs/bear_stearns_email_4185_tannin_to_cioffi_2007-04-22.pdf` |
| 4186 | Tannin→Chavanne (MEAG) | `md/bear_stearns_tannin_to_chavanne_meag.md` | `pdfs/bear_stearns_tannin_to_chavanne_meag.pdf` |
| 4187 | Tannin→Van Solkema | `md/bear_stearns_tannin_to_van_solkema.md` | `pdfs/bear_stearns_tannin_to_van_solkema.pdf` |
| 4188 | Cioffi→Tannin | `md/bear_stearns_cioffi_to_tannin.md` | `pdfs/bear_stearns_cioffi_to_tannin.pdf` |
| 4189 | **Cioffi→Mobasheri "fear" 预警** | `md/bear_stearns_cioffi_to_mobasheri_fear.md` | `pdfs/bear_stearns_cioffi_to_mobasheri_fear.pdf` |
| 4190 | Cioffi→Mak (BNP Paribas) | `md/bear_stearns_cioffi_to_mak_bnp_paribas.md` | `pdfs/bear_stearns_cioffi_to_mak_bnp_paribas.pdf` |
| 4191 | Ervin 邮件 | `md/bear_stearns_ervin.md` | `pdfs/bear_stearns_ervin.pdf` |
| 4192 | Van Solkema 邮件 | `md/bear_stearns_van_solkema.md` | `pdfs/bear_stearns_van_solkema.pdf` |
| 4193 | BSAM 估值标记 (Goldman) | `md/bear_stearns_bsam_marks_goldman_sachs.md` | `pdfs/bear_stearns_bsam_marks_goldman_sachs.pdf` |
| 4194 | Kerr→Dibari (HGEL 问答) | `md/bear_stearns_kerr_to_dibari_hgel_qa.md` | `pdfs/bear_stearns_kerr_to_dibari_hgel_qa.pdf` |
| 4195 | Cioffi ABACUS 估值标记 | `md/bear_stearns_cioffi_abacus_marks.md` | `pdfs/bear_stearns_cioffi_abacus_marks.pdf` |
| 4196 | 固定收益概览 | `md/bear_stearns_fixed_income_overview.md` | `pdfs/bear_stearns_fixed_income_overview.pdf` |
| 4197 | Quental 信函 | `md/bear_stearns_quental_letter.md` | `pdfs/bear_stearns_quental_letter.pdf` |
| 4198 | HGEL 增强杠杆基金文件 | `md/bear_stearns_hgscs_enhanced_leverage.md` | `pdfs/bear_stearns_hgscs_enhanced_leverage.pdf` |
| 4199 | **Tannin 日记（2006-11-23）** | `md/bear_stearns_tannin_diary_entry.md` | `pdfs/bear_stearns_tannin_diary_entry.pdf` |
| 4200 | Cioffi→Kugler | `md/bear_stearns_cioffi_to_kugler.md` | `pdfs/bear_stearns_cioffi_to_kugler.pdf` |
| 4180 | Cioffi 4/30 回报邮件 | `md/bear_stearns_cioffi_re_0430_returns.md` | `pdfs/bear_stearns_cioffi_re_0430_returns.pdf` |
| 4181 | Friedman→Alix 流动性指引 | `md/bear_stearns_friedman_to_alix_wsj_liquidity.md` | `pdfs/bear_stearns_friedman_to_alix_wsj_liquidity.pdf` |
| 4182 | Quental→Donnellan | `md/bear_stearns_quental_to_donnelan.md` | `pdfs/bear_stearns_quental_to_donnelan.pdf` |
| 5388 | **Cioffi 等 HGEL 股权分配邮件链（扫描件 OCR）** | `md/bear_stearns_email_5388_cioffi_to_cummins_tannin_geissinger_2007-04-01.md` | `pdfs/bear_stearns_email_5388_cioffi_to_cummins_tannin_geissinger_2007-04-01.pdf` |
| — | SEC 诉 Cioffi 与 Tannin 证券欺诈投诉全文（LR-20625，2008-06-19） | `md/bear_stearns_sec_complaint_lr20625_2008.md` | `pdfs/bear_stearns_sec_complaint_lr20625_2008.pdf` |

> 重点三封：**4185**（Tannin 风险警示）、**4189**（Cioffi "fear" 邮件）、**4199**（Tannin 日记）——三者是 SEC 指控与媒体报道中反复引用的"对内悲观"铁证；**5388** 为 OCR 转写的 7 封合规争议邮件链。

---

## 二、关键词检索速查

- **Repo 105 / 「window dressing」**：雷曼第3卷（`lehman_valukas_vol3_repo105`）。
- **2008 年 9 月 与摩根大通 / 美联储的敏感邮件往来**：雷曼第4卷（政府章节）与第9卷附录。
- **贝尔斯登著名风险警示**（Tannin 邮件）：在 `bear_stearns_email_4185_*` 中搜索 `sub-prime market looks pretty damn ugly` / `entire sub-prime market is toast`。
- **基金恶化却对外称健康**：SEC 投诉（`bear_stearns_sec_complaint_lr20625_2008`）+ 上述两封 FCIC 邮件。

---

## 三、著名原文片段（Tannin → Cioffi，2007-04-22，OCR 噪点已尽量保留原貌）

> "The sUb-prime market looks pretty damn ugly. CPR/CDR tells us we are looking at major write-downs across the board. If we believe the runs Steve has been doing are ANYWHERE CLOSE to aCCJrale I think we should close the Funds now. ... if CPR/CDR is correct then the entire sub-prime market is toast."

---

## 四、目录结构

```
lehmanbear/
├── README.md                 # 本索引
├── convert.py                # PDF → Markdown 转换脚本（可复现）
├── ocr_5388_run.js           # 5388 扫描件 OCR 脚本（tesseract.js）
├── pdfs/                     # 原始 PDF（一手证据）
├── md/                       # 转换后的 Markdown（可检索文本层）
│   └── _conversion_log.json  # 转换日志（页数 / 文件大小 / 低文本页）
├── rendered_5388_hi/         # 5388 扫描件高清渲染图（4× ≈288 DPI，供 OCR / 核对）
├── ocr_5388/                 # 5388 OCR 逐页原始文本 + combined.txt
├── rendered_lehman/          # 雷曼 Vol7/Vol8 扫描页 3× 渲染图（本地，未纳入版本库）
├── ocr_lehman_results.json   # 雷曼扫描页 OCR 结果（已嵌入 MD，本地未入库）
├── *.py / *.js               # 下载 / 渲染 / OCR / 转换可复现脚本
└── logs/                     # 抓取日志（未纳入版本库）
```

---

## 五、转换说明与质量备注

- 工具：`pypdf` 提取文本，低文本页用 `pdfplumber` 兜底；纯扫描页在 Markdown 中标注「疑似扫描图片 / 无可用文本」并**已由 tesseract.js OCR 补正**。
- **雷曼第1–5卷（叙述正文）文本干净**，可直接引用；第6–9卷附录含大量原始 exhibit。其中 **第7卷 24 页、第8卷 83 页**为纯扫描件（共 107 页），已全部用 **tesseract.js** 对 PyMuPDF 3× 渲染图做 OCR 并嵌入对应 Markdown（替换原占位符）。表格/数字页 OCR 可能有个别错认，精确数据请以 `pdfs/` 原始 PDF 为准。
- **雷曼第9卷附录**：无扫描页（文本层完整）。
- **贝尔斯登 4185 邮件**：源 PDF 文字层本身带 OCR 噪点（个别字母错认），大意完整可读。
- **贝尔斯登 5388 邮件**：纯扫描件，无文本层；已用 **tesseract.js（Node/WASM，无需原生二进制）** 对 PyMuPDF 4× 渲染图做 OCR，转写出完整 7 封邮件链正文（含原始交易记录表），人工校正了明显识别错误（如 `io`→`to`、字母错认）。OCR 原始逐页文本存于 `ocr_5388/`，高清渲染图存于 `rendered_5388_hi/`。
- 所有原始 PDF 均保留于 `pdfs/`，如需精确原文以 PDF 为准。

---

## 六、来源（Provenance）

- Valukas 报告 9 卷：Stanford 镜像 `web.stanford.edu/~jbulow/Lehmandocs/`（Yale EliScholar / Jenner & Block 同源）。
- 众议院听证摘要：U.S. House Financial Services Committee。
- Bear Stearns 邮件：Yale Program on Financial Stability (YPFS) FCIC 存档，经 Wayback Machine 获取（elischolar 主站对自动化访问启用 WAF 挑战）。
- SEC 投诉：U.S. Securities and Exchange Commission。
