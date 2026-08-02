#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert Lehman/Bear Stearns source PDFs into structured Markdown."""
import glob, os, re, sys, json
from datetime import datetime, timezone
from pypdf import PdfReader

VENV = "/Users/bitiworm/.workbuddy/binaries/python/envs/default"
# make pdfplumber importable from venv
sys.path.insert(0, os.path.join(VENV, "lib"))

PDF_DIR = "/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/pdfs"
MD_DIR  = "/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/md"
os.makedirs(MD_DIR, exist_ok=True)

META = {
 "lehman_valukas_vol1_intro_execsummary_risk.pdf": {
   "title": "Valukas 破产审查官报告 · 第1卷（引言 / 执行摘要 / 风险）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%201.pdf",
   "desc": "Lehman Brothers Holdings Inc. 第11章破产程序审查官报告（Anton R. Valukas 著）第1卷：Section I–II 引言与执行摘要、程序背景；Section III.A.1 风险。",
 },
 "lehman_valukas_vol2_valuation_survival.pdf": {
   "title": "Valukas 破产审查官报告 · 第2卷（估值 / 生存能力）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%202.pdf",
   "desc": "第2卷：Section III.A.2 估值；Section III.A.3 生存能力分析。",
 },
 "lehman_valukas_vol3_repo105.pdf": {
   "title": "Valukas 破产审查官报告 · 第3卷（Repo 105）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%203.pdf",
   "desc": "第3卷：Section III.A.4 Repo 105 —— 本卷是『window dressing』会计手法的核心证据，含 Fuld、Lowitt 等人邮件与融资/会计造假文档。",
 },
 "lehman_valukas_vol4_lenders_govt.pdf": {
   "title": "Valukas 破产审查官报告 · 第4卷（担保贷款人 / 政府）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%204.pdf",
   "desc": "第4卷：Section III.A.5 担保贷款人；Section III.A.6 政府与监管机构（含 2008 年 9 月与摩根大通 / 美联储的敏感往来）。",
 },
 "lehman_valukas_vol5_avoidance_barclays.pdf": {
   "title": "Valukas 破产审查官报告 · 第5卷（撤销权诉讼 / 巴克莱交易）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%205.pdf",
   "desc": "第5卷：Section III.B 撤销权诉讼；Section III.C 巴克莱交易。",
 },
 "lehman_valukas_vol6_appendix1.pdf": {
   "title": "Valukas 破产审查官报告 · 第6卷（附录1）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%206%20-%20APPENDIX%201.pdf",
   "desc": "第6卷：附录1（原始材料 /  exhibit）。",
 },
 "lehman_valukas_vol7_appendices2-7.pdf": {
   "title": "Valukas 破产审查官报告 · 第7卷（附录2–7）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%207%20-%20APPENDICES%202-7.pdf",
   "desc": "第7卷：附录2–7（原始邮件、备忘录等 exhibit）。",
 },
 "lehman_valukas_vol8_appendices8-22.pdf": {
   "title": "Valukas 破产审查官报告 · 第8卷（附录8–22）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%208%20-%20APPENDICES%208-22.pdf",
   "desc": "第8卷：附录8–22（含大量高管邮件、融资与会计文档）。",
 },
 "lehman_valukas_vol9_appendices23-34.pdf": {
   "title": "Valukas 破产审查官报告 · 第9卷（附录23–34）",
   "source": "http://web.stanford.edu/~jbulow/Lehmandocs/VOLUME%209%20-%20APPENDICES%2023-34.pdf",
   "desc": "第9卷：附录23–34（最大一卷 exhibit，含 JP Morgan / 美联储 2008 年 9 月通讯等）。",
 },
 "lehman_house_hearing_valuks_2009.pdf": {
   "title": "美国众议院金融服务委员会 · Valukas 听证摘要（2009-04-20）",
   "source": "https://financialservices.house.gov/media/file/hearings/111/valuks_4.20.10.pdf",
   "desc": "众议院金融服务委员会就 Valukas 报告举行的听证会摘要 PDF（审查官 Anton R. Valukas 作证）。",
 },
 "bear_stearns_email_4185_tannin_to_cioffi_2007-04-22.pdf": {
   "title": "贝尔斯登内部邮件 · Matthew Tannin → Ralph Cioffi（2007-04-22）",
   "source": "https://elischolar.library.yale.edu/ypfs-documents/4185/ （存档：web.archive.org/web/20240708085456/...article=5233）",
   "desc": "FCIC 存档的贝尔斯登对冲基金崩盘早期内部邮件之一，发件人 Matthew Tannin 致 Ralph Cioffi。次贷危机最早一批内部预警邮件。",
 },
 "bear_stearns_email_5388_cioffi_to_cummins_tannin_geissinger_2007-04-01.pdf": {
   "title": "贝尔斯登内部邮件 · Ralph Cioffi → Cummins / Tannin / Geissinger（2007-04-01，关于 HGEL 股权交易）",
   "source": "https://elischolar.library.yale.edu/ypfs-documents/5388/ （存档：web.archive.org/web/20240817153358/...article=6436）",
   "desc": "FCIC 存档邮件：Ralph Cioffi 致 Gerald Cummins、Matthew Tannin、John Geissinger，主题为 HGEL（High-Grade Enhanced Leverage）基金股权交易。",
 },
 "bear_stearns_sec_complaint_lr20625_2008.pdf": {
   "title": "SEC 诉讼投诉 · 诉 Cioffi 与 Tannin 证券欺诈（LR-20625，2008-06-19）",
   "source": "https://www.sec.gov/files/litigation/complaints/2008/comp20625.pdf",
   "desc": "美国证券交易委员会对前贝尔斯登对冲基金经理 Ralph R. Cioffi 与 Matthew M. Tannin 提起的证券欺诈诉讼投诉全文（Civil Action No. 08-2457, E.D.N.Y.）。",
 },
}

def clean_text(t):
    if not t:
        return ""
    # normalize whitespace
    t = t.replace("\u00a0", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()

def extract_page_pypdf(page):
    try:
        return page.extract_text() or ""
    except Exception:
        return ""

def extract_page_pdfplumber(pdf_path, idx):
    try:
        import pdfplumber
        with pdfplumber.open(pdf_path) as pdf:
            if idx < len(pdf.pages):
                return pdf.pages[idx].extract_text() or ""
    except Exception:
        pass
    return ""

def convert(pdf_path, md_path):
    base = os.path.basename(pdf_path)
    meta = META.get(base, {})
    reader = PdfReader(pdf_path)
    n = len(reader.pages)
    parts = []
    low_text_pages = []
    for i, page in enumerate(reader.pages, 1):
        txt = clean_text(extract_page_pypdf(page))
        if len(txt) < 30:
            # fallback to pdfplumber
            fb = clean_text(extract_page_pdfplumber(pdf_path, i-1))
            if len(fb) > len(txt):
                txt = fb
        if len(txt) < 15:
            low_text_pages.append(i)
            txt = f"［第 {i} 页：疑似扫描图片 / 无可用文本，建议核对原始 PDF］"
        parts.append(f"［第 {i} 页］\n\n{txt}" if txt else f"［第 {i} 页］")
    body = "\n\n".join(parts)
    title = meta.get("title", base)
    source = meta.get("source", "")
    desc = meta.get("desc", "")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    md = f"""---
title: {title}
source_url: {source}
original_file: {base}
pages: {n}
converted_at: {now}
converted_by: WorkBuddy (pypdf + pdfplumber)
description: {desc}
---

# {title}

> **来源**：{source}
> **原始文件**：`{base}`
> **页数**：{n}
> **说明**：{desc}

---

{body}
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)
    return n, low_text_pages

def main():
    results = []
    for pdf in sorted(glob.glob(os.path.join(PDF_DIR, "*.pdf"))):
        base = os.path.basename(pdf)
        md_name = os.path.splitext(base)[0] + ".md"
        md_path = os.path.join(MD_DIR, md_name)
        n, low = convert(pdf, md_path)
        sz = os.path.getsize(md_path)
        results.append({"pdf": base, "md": md_name, "pages": n, "md_bytes": sz, "low_text_pages": low})
        print(f"OK  {md_name:55} pages={n:4}  md={sz:>9} bytes  low_text_pages={len(low)}")
    with open(os.path.join(MD_DIR, "_conversion_log.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\n=== DONE ===")

if __name__ == "__main__":
    main()
