import os, fitz
BASE="/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear"
VOL7=[157, 285, 292, 295, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 320, 332, 341, 351, 352, 353, 354, 356]
VOL8=list(range(54,94))+list(range(445,488))
def render(vol, pages, src):
    out=os.path.join(BASE,"rendered_lehman",vol)
    os.makedirs(out, exist_ok=True)
    d=fitz.open(src)
    n=0
    for p in pages:
        idx=p-1
        if idx<0 or idx>=d.page_count:
            print("skip",vol,p,"out of range"); continue
        pix=d[idx].get_pixmap(matrix=fitz.Matrix(3.0,3.0))
        pix.save(os.path.join(out,f"p{p:03d}.png"))
        n+=1
    print(f"{vol}: rendered {n} pages")
render("vol7", VOL7, os.path.join(BASE,"pdfs","lehman_valukas_vol7_appendices2-7.pdf"))
render("vol8", VOL8, os.path.join(BASE,"pdfs","lehman_valukas_vol8_appendices8-22.pdf"))
