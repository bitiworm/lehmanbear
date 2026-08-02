import urllib.request, urllib.parse, json, ssl, os, time, re
ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
H={"User-Agent":"Mozilla/5.0 (research; contact 2230329550@qq.com)"}

# YPFS id -> (internal article id, slug)
M = {
 4180:("5228","cioffi_re_0430_returns"),
 4181:("5229","friedman_to_alix_wsj_liquidity"),
 4182:("5230","quental_to_donnelan"),
 4183:("5231","crystal_to_cioffi"),
 4184:("5232","tannin_to_borg_brenner"),
 4186:("5234","tannin_to_chavanne_meag"),
 4187:("5235","tannin_to_van_solkema"),
 4188:("5236","cioffi_to_tannin"),
 4189:("5237","cioffi_to_mobasheri_fear"),
 4190:("5238","cioffi_to_mak_bnp_paribas"),
 4191:("5239","ervin"),
 4192:("5240","van_solkema"),
 4193:("5241","bsam_marks_goldman_sachs"),
 4194:("5242","kerr_to_dibari_hgel_qa"),
 4195:("5243","cioffi_abacus_marks"),
 4196:("5244","fixed_income_overview"),
 4197:("5245","quental_letter"),
 4198:("5246","hgscs_enhanced_leverage"),
 4199:("5247","tannin_diary_entry"),
 4200:("5248","cioffi_to_kugler"),
}
OUT="/Users/bitiworm/WorkBuddy/2026-08-02-14-34-15/lehmanbear/pdfs"
os.makedirs(OUT, exist_ok=True)

def cdx_pdf_ts(target):
    api="https://web.archive.org/cdx/search/cdx?url="+urllib.parse.quote(target,safe="")+"&output=json&fl=timestamp,statuscode,mimetype&filter=statuscode:200&collapse=digest"
    try:
        data=json.load(urllib.request.urlopen(urllib.request.Request(api,headers=H),timeout=30,context=ctx))
    except Exception as e:
        return None
    pdfs=[r for r in data[1:] if len(r)>=3 and r[2].startswith("application/pdf")]
    if not pdfs: return None
    return pdfs[-1][0]  # latest

def download(ypid, art, slug):
    target=f"https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article={art}&context=ypfs-documents"
    ts=cdx_pdf_ts(target)
    if not ts:
        print(f"[{ypid}] NO PDF snapshot"); return False
    url=f"https://web.archive.org/web/{ts}id_/{target}"
    try:
        data=urllib.request.urlopen(urllib.request.Request(url,headers=H),timeout=90,context=ctx).read()
    except Exception as e:
        print(f"[{ypid}] DL ERR {e}"); return False
    if data[:4]!=b"%PDF":
        print(f"[{ypid}] NOT PDF ({len(data)} bytes, magic {data[:8]})"); return False
    fn=f"bear_stearns_{slug}.pdf"
    open(os.path.join(OUT,fn),"wb").write(data)
    print(f"[{ypid}] OK {fn}  {len(data)} bytes")
    return True

ok=0; fail=0
for yp, (art, slug) in M.items():
    if download(yp, art, slug): ok+=1
    else: fail+=1
    time.sleep(0.4)
print(f"\nDONE ok={ok} fail={fail}")
