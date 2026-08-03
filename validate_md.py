import fitz, os, glob, re, json

pdfs = sorted(glob.glob("pdfs/*.pdf"))
PH = re.compile(r"疑似扫描图片|无可用文本")
PM = re.compile(r"［第\s*(\d+)\s*页")

print(f"{'PDF':52s} {'pg':>4} {'PDFtxt':>8} {'scan':>5} {'md?':>4} {'mdtxt':>8} {'ph':>4} {'pgmark':>6}  verdict")
print("-"*110)
gaps = []
for pf in pdfs:
    name = os.path.basename(pf)
    md = "md/" + name[:-4] + ".md"
    d = fitz.open(pf)
    npages = d.page_count
    total_txt = 0
    scanned = []
    for i, page in enumerate(d):
        t = (page.get_text() or "").strip()
        total_txt += len(t)
        if len(t) < 50 and page.get_images():
            scanned.append(i+1)
    md_exists = os.path.exists(md)
    md_text = open(md, encoding="utf-8").read() if md_exists else ""
    md_chars = len(md_text)
    ph = len(PH.findall(md_text))
    pgmark = len(PM.findall(md_text))
    # verdict logic
    flags = []
    if not md_exists:
        flags.append("NO_MD")
    if ph > 0:
        flags.append(f"{ph}_PLACEHOLDER")
    if scanned and ph == 0:
        # scanned pages exist but MD has no placeholder -> assume OCR'd; check md has text
        if md_chars < 200:
            flags.append("MD_EMPTY")
    if pgmark < npages:
        # MD page markers fewer than PDF pages -> possible dropped pages
        flags.append(f"PGMARK {pgmark}/{npages}")
    if total_txt > 5000 and md_chars < total_txt * 0.3:
        flags.append("MD_SHORT")
    verdict = ",".join(flags) if flags else "OK"
    if flags:
        gaps.append((name, scanned, ph, pgmark, npages))
    print(f"{name[:52]:52s} {npages:4d} {total_txt:8d} {len(scanned):5d} {'Y' if md_exists else 'N':>4} {md_chars:8d} {ph:4d} {pgmark:6d}  {verdict}")

print("\n===== GAPS (need fix) =====")
for g in gaps:
    print(f"  {g[0]}  scanned_pages={g[1]}  placeholders={g[2]}  pgmark={g[3]}/{g[4]}")

# dump scanned map for OCR repair
scanned_map = {}
for pf in pdfs:
    name = os.path.basename(pf)[:-4]
    d = fitz.open(pf)
    sc = [i+1 for i,p in enumerate(d) if len((p.get_text() or "").strip())<50 and p.get_images()]
    if sc:
        scanned_map[name] = sc
json.dump(scanned_map, open("scanned_pages_map.json","w"), ensure_ascii=False, indent=2)
print("\nscanned_pages_map.json written (all PDFs with scanned pages)")
