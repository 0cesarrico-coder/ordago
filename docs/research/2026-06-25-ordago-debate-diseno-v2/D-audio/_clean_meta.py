import json, re, sys
src, out = sys.argv[1], sys.argv[2]
raw=open(src).read()
try: txt=json.loads(raw)
except Exception: txt=raw
txt=re.sub(r'^\s*Mostrar razonamiento\s*\n','',txt).strip()
if len(txt) < 500:
    print("FALLO_VALIDACION", len(txt)); sys.exit(1)
open(out,"w").write(txt)
print("OK", len(txt), "->", out)
