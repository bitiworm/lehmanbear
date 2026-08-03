import re, json, os

ocr = json.load(open("ocr_fixup.json"))

# 1) Vol5 page 82: replace marker+partial with full OCR text
clean82 = """Infusion into LBSF May 2008

Step 1: LBI requests paydown from LBHI for the purpose of infusing capital into LBSF (LBHI).

Step 2: LBHI wires money to LBI (LBI increases cash and credits paid-in capital; LBHI decreases cash and increases investment asset in LBI).

Step 3: LBI wires money to LBSF (LBSF increases cash and credits paid-in capital; LBI decreases cash and increases investment asset in LBSF).

(LBI = subsidiary of LBHI; LBSF = subsidiary of LBI)

1609"""
vol5 = "md/lehman_valukas_vol5_avoidance_barclays.md"
t = open(vol5, encoding="utf-8").read()
# replace from page-82 marker up to page-83 marker
pat = re.compile(r"［第 82 页］.*?(?=［第 83 页］)", re.S)
new = "［第 82 页］\n\n" + clean82 + "\n\n"
t2 = pat.sub(new, t, count=1)
assert t2 != t, "Vol5 p82 replace failed"
open(vol5, "w", encoding="utf-8").write(t2)
print("Vol5 p82 embedded")

# 2) Vols 1-5 page 2: blank-page relabel
for v in ["vol1_intro_execsummary_risk","vol2_valuation_survival","vol3_repo105","vol4_lenders_govt","vol5_avoidance_barclays"]:
    f = f"md/lehman_valukas_{v}.md"
    tt = open(f, encoding="utf-8").read()
    new_tt = re.sub(r"［第 2 页：疑似扫描图片[^\n]*］",
                    "［第 2 页：空白页（原 PDF 该页无文字内容，已核验为全白页）］",
                    tt, count=1)
    if new_tt != tt:
        open(f, "w", encoding="utf-8").write(new_tt)
        print(f"{v}: page-2 placeholder relabeled")
    else:
        print(f"{v}: NO placeholder found (already fixed?)")
