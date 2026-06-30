"""Genera los ASSETS del sistema de cartas + escena teatro (dirección B + calidez A) para ÓRDAGO.
Clase-mundial, anclado a STYLE-BIBLE + la hoja de cartas wc-card-sheet. Salida en game/assets/.
Compositables en el DOM (fondo transparente donde aplica). Uso: python gen_assets.py [--only ID]"""
import os, sys, time, argparse
from google import genai
from google.genai import types

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "..", "game", "assets", "art")
os.makedirs(OUT, exist_ok=True)
KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=KEY)
MODEL = "gemini-3-pro-image"

FOLK = ("Mexican folk Posada engraving style, Day-of-the-Dead, warm hand-painted, aged-paper card art, "
 "dirty antique gold + magenta + teal + marigold accents, ornate but clean and readable. World-class game asset.")
TRANSP = " Isolated on a FULLY TRANSPARENT background (PNG alpha), object centered with clear margin, no scene, no frame around the edge."

ASSETS = {
 # --- Emblemas de palo (esquinas + pips) — transparentes, icónicos a 24px ---
 "suit-oros":    (FOLK+" A single ÓRDAGO suit emblem: a golden coin (Oros) embossed with a tiny calaca skull, "
                  "Posada filigree rim. Bold iconic, recognizable at 24px."+TRANSP, "1:1"),
 "suit-copas":   (FOLK+" A single ÓRDAGO suit emblem: an ornate golden chalice/cup (Copas) with folk enamel "
                  "decoration. Bold iconic, recognizable at 24px."+TRANSP, "1:1"),
 "suit-espadas": (FOLK+" A single ÓRDAGO suit emblem: a straight steel sword (Espadas) with engraved gold hilt, "
                  "blade pointing up. Bold iconic, recognizable at 24px."+TRANSP, "1:1"),
 "suit-bastos":  (FOLK+" A single ÓRDAGO suit emblem: a knotted wooden club/cudgel (Bastos) with bark texture. "
                  "Bold iconic, recognizable at 24px."+TRANSP, "1:1"),
 # --- Figuras (8/9/10) — ilustración folk, agnóstica de palo (el palo lo da el emblema de esquina) ---
 "fig-sota":   (FOLK+" Full-body ÓRDAGO face-card character: the SOTA (jack) as a folk Mexican page — a young "
                "woman in traditional embroidered dress holding up a club, confident pose, traditional Spanish-deck "
                "illustration reinterpreted folk-Posada. Card portrait, vertical."+TRANSP, "3:4"),
 "fig-caballo":(FOLK+" Full-body ÓRDAGO face-card character: the CABALLO (knight) — a charro rider on a "
                "prancing horse, traditional Spanish-deck illustration reinterpreted folk-Posada. Card portrait, vertical."+TRANSP, "3:4"),
 "fig-rey":    (FOLK+" Full-body ÓRDAGO face-card character: the REY (king) — a crowned folk king holding a sword, "
                "ornate robe, traditional Spanish-deck illustration reinterpreted folk-Posada. Card portrait, vertical."+TRANSP, "3:4"),
 # --- Marco de carta (borde grabado, centro transparente para overlay sobre papel CSS) ---
 "card-border":(FOLK+" An ornate ENGRAVED CARD BORDER FRAME only: thin gold+brown Posada filigree border running "
                "along the four edges of a vertical playing card, rounded corners. The CENTER is completely empty/"
                "transparent (just the border ring). No text, no number, no illustration inside."+TRANSP, "3:4"),
 # --- Mata: marco legendario dorado brillante (overlay) ---
 "card-mata":  (FOLK+" An ornate GLOWING LEGENDARY golden card border frame (the 'Mata'): radiant gold filigree "
                "with warm light glow along the four edges of a vertical card, rounded corners. CENTER empty/transparent. "
                "No text inside."+TRANSP, "3:4"),
 # --- Escena teatro: marco de proscenio (cortinas+papel picado+madera), centro-escenario transparente ---
 "teatro-frame":(FOLK+" A MOBILE GAME stage PROSCENIUM frame, PORTRAIT 9:16: deep magenta theater curtains down the "
                "LEFT and RIGHT edges tied with gold, a papel-picado paper-cut garland across the TOP, a dark carved-"
                "wooden base across the BOTTOM, ornate gold filigree corners. The entire CENTER is empty/transparent "
                "(the open stage where the game board will show through). Only the border/frame is drawn."+TRANSP, "9:16"),
 # --- Diablo de escenario (al fondo del escenario, tras el fieltro) ---
 "diablo-stage":(FOLK+" The charismatic trickster Devil croupier (calaca-charro: skull face, curved horns, magenta "
                "charro suit with skull epaulets, skeletal hands) seated behind a table DEALING Spanish playing cards "
                "with a sly grin, upper body only, symmetric, looking at the viewer. NOT gore. Recognizable silhouette."+TRANSP, "1:1"),
}

def gen(cid, prompt, aspect, retries=3):
    out = os.path.join(OUT, f"{cid}.png")
    for attempt in range(retries):
        try:
            cfg = types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
                image_config=types.ImageConfig(aspect_ratio=aspect))
            r = client.models.generate_content(model=MODEL, contents=[prompt], config=cfg)
            for part in r.candidates[0].content.parts:
                if getattr(part, "inline_data", None) and part.inline_data.data:
                    open(out, "wb").write(part.inline_data.data)
                    print(f"  OK {cid}.png ({os.path.getsize(out)//1024} KB)")
                    return out
            print(f"  . sin imagen ({attempt+1}): {(r.candidates[0].content.parts[0].text or '')[:100]}")
        except Exception as e:
            print(f"  ! {cid} intento {attempt+1}: {str(e)[:140]}"); time.sleep(3)
    return None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only", default=None); a = ap.parse_args()
    items = list(ASSETS.items())
    if a.only: items = [(k, v) for k, v in items if k == a.only]
    for cid, (prompt, aspect) in items:
        print(f"[{cid}] {aspect}"); gen(cid, prompt, aspect)

if __name__ == "__main__":
    main()
