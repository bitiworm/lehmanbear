import fitz, os

# (pdf base, [0-based page indices to render])
jobs = [
    ("lehman_valukas_vol1_intro_execsummary_risk", [1]),   # PDF p2
    ("lehman_valukas_vol2_valuation_survival",     [1]),
    ("lehman_valukas_vol3_repo105",                [1]),
    ("lehman_valukas_vol4_lenders_govt",           [1]),
    ("lehman_valukas_vol5_avoidance_barclays",     [1, 81]), # p2 + p82
]
out = "rendered_fixup"
os.makedirs(out, exist_ok=True)
mat = fitz.Matrix(3.0, 3.0)
for base, idxs in jobs:
    d = fitz.open(f"pdfs/{base}.pdf")
    for idx in idxs:
        pg = idx + 1
        pix = d[idx].get_pixmap(matrix=mat)
        fn = f"{out}/{base.replace('lehman_valukas_','')}_p{pg:03d}.png"
        pix.save(fn)
        # also report whether page has real extractable text
        t = (d[idx].get_text() or "").strip()
        print(f"{fn}  {pix.width}x{pix.height}  pdf_text_chars={len(t)}")
