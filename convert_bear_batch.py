import os, re, fitz, glob

OUT_MD="/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/md"
PDF="/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/pdfs"

# slug -> (ypfs_id, title, zh_desc)
M = {
 "cioffi_re_0430_returns":(4180,"Bear Stearns Cioffi Email re 4/30 Returns","Cioffi 关于 4/30 基金回报的邮件"),
 "friedman_to_alix_wsj_liquidity":(4181,"Bear Stearns Email from Friedman to Alix re WSJ-Liquidity Guidelines","Friedman 致 Alix：关于《华尔街日报》流动性指引"),
 "quental_to_donnelan":(4182,"Bear Stearns Email from Greg Quental to Andrew Donnellan et al","Greg Quental 致 Andrew Donnellan 等"),
 "crystal_to_cioffi":(4183,"Bear Stearns Email from Jim Crystal to Ralph Cioffi and others","Jim Crystal 致 Cioffi 等（SRP 二月回报，要求'以最佳面貌示人'）"),
 "tannin_to_borg_brenner":(4184,"Bear Stearns Email from Matt Tannin to Bella Borg-Brenner","Tannin 致 Bella Borg-Brenner"),
 "tannin_to_chavanne_meag":(4186,"Bear Stearns Email from Matthew Tannin to Klaus Chavanne MEAG New York","Tannin 致 MEAG 纽约 Klaus Chavanne"),
 "tannin_to_van_solkema":(4187,"Bear Stearns Email from Matthew Tannin to Steven Van Solkema","Tannin 致 Steven Van Solkema"),
 "cioffi_to_tannin":(4188,"Bear Stearns Email from Ralph Cioffi to Matt Tannin","Cioffi 致 Tannin"),
 "cioffi_to_mobasheri_fear":(4189,"Bear Stearns Email from Ralph Cioffi to Ardavan Mobasheri","Cioffi 致 Mobasheri 的'fear'邮件——著名悲观预警"),
 "cioffi_to_mak_bnp_paribas":(4190,"Bear Stearns Email from Ralph Cioffi to Ken Mak re BNP Paribas Arbitrage SNC (UNFC, LLC)","Cioffi 致 Ken Mak：关于 BNP Paribas Arbitrage"),
 "ervin":(4191,"Bear Stearns Email from Robert Ervin","Robert Ervin 邮件"),
 "van_solkema":(4192,"Bear Stearns Email from Steven Van Solkema","Steven Van Solkema 邮件"),
 "bsam_marks_goldman_sachs":(4193,"Bear Stearns Email re BSAM Marks from Goldman Sachs","关于 BSAM 估值标记（来自 Goldman Sachs）"),
 "kerr_to_dibari_hgel_qa":(4194,"Bear Stearns Email Kerr to Dibari re High Grade Enhanced Leverage Q and A","Kerr 致 Dibari：关于 HGEL 增强杠杆基金问答"),
 "cioffi_abacus_marks":(4195,"Bear Stearns Emails from Cioffi re ABACUS marks","Cioffi 关于 ABACUS 估值标记的邮件"),
 "fixed_income_overview":(4196,"Bear Stearns Fixed Income Overview","贝尔斯登固定收益业务概览"),
 "quental_letter":(4197,"Bear Stearns Gregory Quental letter","Gregory Quental 信函"),
 "hgscs_enhanced_leverage":(4198,"Bear Stearns High Grade Structured Credit Strategies Enhanced Leverage","高评级结构化信用策略增强杠杆基金（HGEL）文件"),
 "tannin_diary_entry":(4199,"Bear Stearns Matt Tannin email diary entry","Tannin 邮件日记条目（2006-11-23，著名悲观记录）"),
 "cioffi_to_kugler":(4200,"Bear Stearns Ralph Cioffi e-mail message to Adam Kugler","Cioffi 致 Adam Kugler"),
}

def clean_body(txt):
    # collapse 3+ newlines to 2, strip trailing spaces
    txt=re.sub(r"[ \t]+\n", "\n", txt)
    txt=re.sub(r"\n{3,}", "\n\n", txt)
    return txt.strip()

for slug,(ypid,title,zh) in M.items():
    pdfp=os.path.join(PDF,f"bear_stearns_{slug}.pdf")
    if not os.path.exists(pdfp):
        print("MISSING",pdfp); continue
    d=fitz.open(pdfp)
    body=clean_body("\n".join((p.get_text() or "") for p in d))
    url=f"https://elischolar.library.yale.edu/ypfs-documents/{ypid}/"
    md=f"""---
title: {title}
zh: {zh}
source_url: {url}
original_file: bear_stearns_{slug}.pdf
pages: {d.page_count}
fcic_id: {ypid}
converted_by: WorkBuddy (PyMuPDF text extraction)
description: >
  {zh}。FCIC（金融危机调查委员会）存档的贝尔斯登内部邮件/文件，YPFS # {ypid}。
---

# {title}

> 来源：{url}
> 原始 PDF：`bear_stearns_{slug}.pdf`（{d.page_count} 页，FCIC 存档 # {ypid}）
> 转换：PyMuPDF 提取文本层；如需精确原文以 PDF 为准。

---

{body}
"""
    outp=os.path.join(OUT_MD,f"bear_stearns_{slug}.md")
    open(outp,"w").write(md)
    print(f"wrote {os.path.basename(outp)}  ({d.page_count}p, {len(body)} chars)")
