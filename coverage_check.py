import fitz, os, glob, re

STOP = set("the a an and or of to in for on with by from at as is are was were be been being this that these those it its their his her our your their which who whom whose what when where why how not no nor so than then if then into onto upon over under between among during before after against through during about above below off near per each every both either neither such same other another more most less least very can could may might must shall should will would do does did done has had having will also any all some one two three first second third page report pursuant section paragraph exhibit schedule note see table figure appendix volume part chapter company companies lehman brothers inc bank holding creditor court board march april may june july august september october november december 2008 2007 2006 2009 2010 united states district southern new york judge barclays jefferson asset management high grade enhanced leverage fund srp hgel hg hgscs bsam fcic sec fdic frb fed federal reserve pursuant".split())

def words(text):
    return [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{4,}", text)]

print(f"{'PDF':52s} {'PDFtxt':>9} {'sigW':>6} {'inMD':>6} {'cov%':>6}  flag")
print("-"*95)
worst=[]
for pf in sorted(glob.glob("pdfs/*.pdf")):
    base=os.path.basename(pf)[:-4]
    md=f"md/{base}.md"
    d=fitz.open(pf)
    pdftext="".join((p.get_text() or "") for p in d)
    if len(pdftext)<5000:
        # scanned/OCR'd or tiny: skip ratio (MD may exceed via OCR)
        print(f"{base[:52]:52s} {len(pdftext):9d} {'-':>6} {'-':>6} {'skip':>6}  (scanned/tiny)")
        continue
    mdtext=open(md,encoding="utf-8").read()
    ws=set(w for w in words(pdftext) if w not in STOP)
    if not ws:
        print(f"{base[:52]:52s} {len(pdftext):9d} {'0':>6} {'-':>6} {'-':>6}  (no sig words)")
        continue
    mdwords=set(words(mdtext))
    inter=ws & mdwords
    cov=100.0*len(inter)/len(ws)
    flag = "OK" if cov>=95 else ("WARN" if cov>=85 else "LOW")
    worst.append((base,cov,len(ws)))
    print(f"{base[:52]:52s} {len(pdftext):9d} {len(ws):6d} {len(inter):6d} {cov:6.1f}  {flag}")

worst.sort(key=lambda x:x[1])
print("\n=== lowest coverage (potential silent drops) ===")
for b,c,n in worst[:8]:
    print(f"  {b}: {c:.1f}% ({n} sig words)")
