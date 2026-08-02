import json, re, os
BASE="/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear"
r=json.load(open(os.path.join(BASE,"ocr_lehman_results.json")))

def clean(t):
    t=t.replace("\r","")
    t=re.sub(r"\n{3,}","\n\n",t)
    return t.strip()

def embed(vol, mdfile):
    path=os.path.join(BASE,"md",mdfile)
    s=open(path,encoding="utf-8").read()
    pages=r.get(vol,{})
    replaced=0; missing=0
    for p, txt in pages.items():
        ph=f"［第 {p} 页：疑似扫描图片 / 无可用文本，建议核对原始 PDF］"
        if ph in s:
            block=f"［第 {p} 页］\n\n{clean(txt)}"
            s=s.replace(ph, block)
            replaced+=1
        else:
            missing+=1
    open(path,"w",encoding="utf-8").write(s)
    print(f"{mdfile}: replaced {replaced}, missing {missing}")
    return replaced

embed("vol7","lehman_valukas_vol7_appendices2-7.md")
embed("vol8","lehman_valukas_vol8_appendices8-22.md")
