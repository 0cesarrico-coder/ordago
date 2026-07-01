"""ÓRDAGO v2: pintas limpias del naipe español (para repetir N veces) + arte hero de inicio.
Salida: game/assets/art/pip/ y game/assets/art/. Uso: python gen_v2.py"""
import os, time
from google import genai
from google.genai import types
HERE=os.path.dirname(__file__); ART=os.path.join(HERE,"..","game","assets","art")
PIP=os.path.join(ART,"pip"); os.makedirs(PIP,exist_ok=True)
c=genai.Client(api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
MODEL="gemini-3-pro-image"
# PINTAS: emblema SIMPLE e icónico de cada palo, legible al repetirse pequeño (como el naipe español real)
FOLK=("Traditional SPANISH PLAYING CARD suit pip (baraja española), SINGLE clean iconic emblem, flat folk "
 "illustration with a bold dark outline, warm colors, subtle Mexican Posada flavor but SIMPLE and clearly "
 "readable when repeated small (like real Spanish deck pips). Centered, symmetric.")
TR=" Isolated on a FULLY TRANSPARENT background, one single emblem centered, generous margin, no frame, no number, no text."
PIPS={
 "oros":FOLK+" The emblem is a single golden COIN (Oro) — a round gold coin with a simple engraved rim and a small star or face."+TR,
 "copas":FOLK+" The emblem is a single golden CHALICE/CUP (Copa) — an ornate goblet, symmetric, gold with red accents."+TR,
 "espadas":FOLK+" The emblem is a single straight SWORD (Espada) — a vertical steel sword with a gold hilt, blade up."+TR,
 "bastos":FOLK+" The emblem is a single wooden CLUB/BATON (Basto) — a vertical knotted wooden cudgel with bark texture, green-brown."+TR,
}
# HERO de inicio: retrato 9:16, Diablo + título ÓRDAGO integrado. Full-bleed (sin knockout).
HERO=("ART DIRECTION 'Maximalismo identitario folk mexicano' (Day-of-the-Dead cantina, Posada engraving, dirty "
 "antique gold, magenta/teal/marigold, papel picado, candlelight, calacas). TITLE SPLASH SCREEN, PORTRAIT 9:16. "
 "HERO COMPOSITION: the charismatic trickster Devil-croupier (calaca-charro skull, curved horns, magenta charro "
 "suit, sly cheating grin) at center-lower, dealing Spanish playing cards across a worn green cantina felt, one "
 "card hidden up his sleeve. ABOVE him the big ornate engraved GOLD TITLE 'ÓRDAGO' (spell EXACTLY Ó-R-D-A-G-O), "
 "and a small ribbon subtitle 'le haces trampa al Diablo'. Papel-picado garland at top, candles, dramatic warm "
 "light, deep vignette at edges so UI buttons read at the bottom. Leave some clear darker space at the very bottom "
 "third for menu buttons. World-class premium key art, high craft.")
def gen(path, prompt, aspect):
    for a in range(3):
        try:
            cfg=types.GenerateContentConfig(response_modalities=["TEXT","IMAGE"],image_config=types.ImageConfig(aspect_ratio=aspect))
            r=c.models.generate_content(model=MODEL,contents=[prompt],config=cfg)
            for p in r.candidates[0].content.parts:
                if getattr(p,"inline_data",None) and p.inline_data.data:
                    open(path,"wb").write(p.inline_data.data); print("OK",os.path.basename(path),os.path.getsize(path)//1024,"KB"); return
            print("noimg",os.path.basename(path),(r.candidates[0].content.parts[0].text or "")[:90])
        except Exception as e: print("!",os.path.basename(path),a,str(e)[:120]); time.sleep(3)
for k,pr in PIPS.items(): gen(f"{PIP}/{k}.png",pr,"1:1")
gen(f"{ART}/hero-inicio.png",HERO,"9:16")
print("DONE v2")
