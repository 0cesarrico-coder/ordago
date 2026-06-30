"""Genera los conceptos visuales de ÓRDAGO con Nano Banana Pro (gemini-3-pro-image).
Anclado a design/STYLE-BIBLE.md + composición del prototipo. Salida en design/concepts/.
Uso: python gen_concepts.py [--only ID] [--test]"""
import os, sys, time, argparse
from google import genai
from google.genai import types

OUT = os.path.join(os.path.dirname(__file__), "concepts")
os.makedirs(OUT, exist_ok=True)
KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=KEY)
MODEL = "gemini-3-pro-image"

# --- Preámbulos de estilo por dirección (el crux §11) ---
DIR_A = ("ART DIRECTION A — 'Claroscuro boutique premium': dramatic chiaroscuro lighting, deep "
  "blacks with warm candle-gold highlights, restrained Mexican Posada engraving linework, "
  "moody premium hand-painted look like Inscryption and Cult of the Lamb, baroque cantina at night.")
DIR_B = ("ART DIRECTION B — 'Maximalismo identitario folk': vibrant Mexican Day-of-the-Dead folk art, "
  "dirty antique gold, marigold cempasúchil orange, papel picado paper-cut textures, magenta and teal "
  "accents, ornate Posada engraving, rich textured maximalist but with clear value hierarchy (saturated "
  "only on what matters), warm cantina with candles, calacas.")

COMMON = ("Subject: ÓRDAGO, a Spanish-deck roguelike card game where a gambler cheats the Devil. "
  "Spanish playing cards (suits: Oros=gold coins, Copas=cups, Espadas=swords, Bastos=clubs/wood), "
  "a charismatic trickster Devil-croupier (horns, sly grin, NOT gory horror). Warm cantina, candles, "
  "worn felt table, dirty gold. The state must be 100% readable in silence. No real text gibberish; "
  "keep any UI labels minimal and legible. High craft, game-ready key composition.")

CONCEPTS = {
  "B1.1-game": dict(aspect="9:16", comp=(
    "A complete MOBILE GAME SCREEN mockup (portrait), UI composition matching this layout: "
    "TOP a HUD bar with the bet name 'LA CHICA' on the left and 'Reales' gold counter on the right, "
    "below it a horizontal progress bar toward the Devil's threshold; then a row of 3 'Maña' amulet "
    "slot-cards (a gold-coin Pacto, a green-tree Pacto, an eye Fullería). CENTER: a worn green cantina "
    "felt table labeled 'LA MESA DEL DIABLO' with 5 face-up Spanish playing cards; behind the table "
    "the Devil-croupier looms watching. BOTTOM: the player's HAND of 3 Spanish cards, and two buttons "
    "'PASAR' and a glowing gold 'ESCOBA'. Clean readable HUD, cards crisp, devil doesn't cover the cards.")),
  "B0.1-capsule": dict(aspect="16:9", comp=(
    "KEY ART / store capsule (landscape). The charismatic Devil-croupier deals Spanish playing cards "
    "across the felt table while the gambler's hand secretly CHEATS him (a card hidden up the sleeve, a "
    "sly complicit wink). The title 'ÓRDAGO' integrated into the composition (engraved, not pasted). "
    "The hook reads instantly: 'you cheat the Devil at cards'. Candlelit cantina, dramatic, premium.")),
  "B2.1-diablo": dict(aspect="3:4", comp=(
    "Character portrait of the Devil as a cantina card-sharp (tahúr), Mexican Posada engraving / calaca "
    "skull style, horns, sly cheating grin, dealing Spanish cards with intent, ornate filigree linework, "
    "recognizable silhouette at 100px, candlelit. Charismatic trickster, not gore.")),
}

def gen(cid, direction, aspect, prompt, retries=3):
    out = os.path.join(OUT, f"{cid}-{direction}.png")
    for attempt in range(retries):
        try:
            cfg = types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
                image_config=types.ImageConfig(aspect_ratio=aspect),
            )
            r = client.models.generate_content(model=MODEL, contents=prompt, config=cfg)
            saved = False
            for part in r.candidates[0].content.parts:
                if getattr(part, "inline_data", None) and part.inline_data.data:
                    with open(out, "wb") as f:
                        f.write(part.inline_data.data)
                    saved = True
            if saved:
                print(f"  ✓ {os.path.basename(out)} ({os.path.getsize(out)//1024} KB)")
                return out
            print(f"  · sin imagen (intento {attempt+1}) — texto: "
                  f"{(r.candidates[0].content.parts[0].text or '')[:120] if r.candidates[0].content.parts else ''}")
        except Exception as e:
            print(f"  ! intento {attempt+1}: {str(e)[:160]}")
            time.sleep(3)
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default=None)
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    items = list(CONCEPTS.items())
    if a.only: items = [(k, v) for k, v in items if k == a.only]
    dirs = {"A": DIR_A, "B": DIR_B}
    if a.test: items = items[:1]; dirs = {"A": DIR_A}
    for cid, spec in items:
        print(f"[{cid}] aspect={spec['aspect']}")
        for dlabel, dpre in dirs.items():
            prompt = f"{dpre}\n\n{COMMON}\n\n{spec['comp']}"
            gen(cid, dlabel, spec["aspect"], prompt)

if __name__ == "__main__":
    main()
