"""Genera mockups de CLASE MUNDIAL de ÓRDAGO (dirección B ya elegida) con Nano Banana Pro.
Image-to-image desde el mockup B aprobado (B1.1-game-B.png) + el Diablo, para cohesión.
3 variantes de pantalla de juego (que el usuario elija el look de ejecución) + 1 hoja de cartas.
Salida en design/concepts/wc/. Uso: python gen_worldclass.py [--only ID]"""
import os, sys, time, argparse
from google import genai
from google.genai import types

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, "concepts", "wc")
os.makedirs(OUT, exist_ok=True)
KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=KEY)
MODEL = "gemini-3-pro-image"

ANCHOR_GAME = os.path.join(HERE, "concepts", "B1.1-game-B.png")   # composición/layout aprobado
ANCHOR_DIABLO = os.path.join(HERE, "..", "game", "assets", "diablo.png")

STYLE = ("ART DIRECTION (LOCKED) — 'Maximalismo identitario folk mexicano', Day-of-the-Dead cantina, "
 "Posada engraving, dirty antique gold, marigold cempasúchil orange, magenta and teal accents, papel picado, "
 "warm candlelight, worn green felt, calacas. Charismatic trickster Devil croupier (NOT gore). "
 "CRITICAL: clear VALUE HIERARCHY — saturate only what's actionable; readable at 100x100px grayscale; "
 "the game state must be 100% legible in silence. WORLD-CLASS studio polish, cohesive with the anchor image.")

COMMON = ("Subject: ÓRDAGO, a Spanish-deck roguelike where a gambler cheats the Devil at cards. "
 "Spanish playing cards — suits Oros (gold coins), Copas (cups), Espadas (swords), Bastos (wooden clubs). "
 "MOBILE GAME SCREEN mockup, PORTRAIT 9:16, SAME LAYOUT as the anchor: TOP a HUD bar (bet name left, "
 "gold 'Reales' counter right, a progress bar toward the Devil's threshold), a row of 3 'Maña' amulet "
 "slot-cards; CENTER a cantina felt table 'LA MESA DEL DIABLO' with 5 face-up Spanish cards and the "
 "Devil-croupier looming behind; BOTTOM the player's HAND of 3 cards and two buttons 'PASAR' and a glowing "
 "gold 'ESCOBA'. Each playing card shows its game VALUE as a BIG legible number plus a small suit glyph; "
 "face cards (Sota/Caballo/Rey = 8/9/10) have a traditional illustrated figure behind the big number. "
 "Devil does NOT cover the cards. No gibberish text; keep UI labels minimal and legible.")

VARIANTS = {
 "wc1-naipe-ilustrado": (
   "EXECUTION LOOK A — 'Naipe ilustrado pleno': fully ILLUSTRATED playing cards with ornate folk-Posada "
   "engraved borders, aged paper texture, hand-painted suit emblems; rich carved-wood + green felt table "
   "with deep candle pools; the Devil integrated as a painted backdrop figure. Lush, painterly, premium "
   "hand-illustrated like a top-tier mobile card game. Cozy warm cantina."),
 "wc2-papel-picado-teatral": (
   "EXECUTION LOOK B — 'Teatro de papel picado': bold graphic FOLK look, the whole screen framed like a "
   "cantina puppet-theater / proscenium with papel-picado garlands, flat saturated magenta/teal/marigold "
   "shapes, thick Posada line-art on cards, ornamental gold filigree HUD frame. Iconic, high-contrast, "
   "screen-printed poster energy — instantly readable, very shareable thumbnail."),
 "wc3-grabado-premium-oscuro": (
   "EXECUTION LOOK C — 'Grabado Posada premium (cálido-oscuro)': dramatic chiaroscuro WITHIN the folk "
   "direction — deep shadows, strong pools of candle-gold light, fine gold-line engraving on cards over "
   "dark aged paper, the Devil emerging from darkness. Moody, expensive, cinematic but still folk and warm "
   "(not boutique-bleached). Inscryption-grade craft with Mexican Posada soul."),
}

CARD_SHEET = (STYLE + "\n\nDESIGN SHEET, NOT a screen. SQUARE 1:1. A neat grid showing the ÓRDAGO Spanish-card "
 "design system: one example card per suit (Oros gold-coin, Copas cup, Espadas sword, Bastos wooden club) "
 "plus the three figures Sota/Caballo/Rey rendered as illustrated folk-Posada characters with the big game "
 "VALUE numbers 8, 9, 10, plus a special glowing 'Mata' legendary card and a cracked 'Marcada' cheated card. "
 "Each card: rounded corners, aged paper, ornate engraved border, BIG legible value number, small suit glyph "
 "in the corner. Consistent set, world-class card-art, readable at small size. Folk maximalist, warm.")

def load(p):
    return types.Part.from_bytes(data=open(p, "rb").read(), mime_type="image/png")

def gen(cid, prompt, anchors, aspect, retries=3):
    out = os.path.join(OUT, f"{cid}.png")
    parts = [load(a) for a in anchors if os.path.exists(a)] + [prompt]
    for attempt in range(retries):
        try:
            cfg = types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"],
                image_config=types.ImageConfig(aspect_ratio=aspect))
            r = client.models.generate_content(model=MODEL, contents=parts, config=cfg)
            for part in r.candidates[0].content.parts:
                if getattr(part, "inline_data", None) and part.inline_data.data:
                    open(out, "wb").write(part.inline_data.data)
                    print(f"  OK {cid}.png ({os.path.getsize(out)//1024} KB)")
                    return out
            print(f"  . sin imagen ({attempt+1}): {(r.candidates[0].content.parts[0].text or '')[:120]}")
        except Exception as e:
            print(f"  ! {cid} intento {attempt+1}: {str(e)[:160]}"); time.sleep(3)
    return None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--only", default=None); a = ap.parse_args()
    jobs = []
    for cid, look in VARIANTS.items():
        prompt = f"{STYLE}\n\n{COMMON}\n\n{look}"
        jobs.append((cid, prompt, [ANCHOR_GAME, ANCHOR_DIABLO], "9:16"))
    jobs.append(("wc-card-sheet", CARD_SHEET, [ANCHOR_GAME], "1:1"))
    if a.only: jobs = [j for j in jobs if j[0] == a.only]
    for cid, prompt, anchors, aspect in jobs:
        print(f"[{cid}]"); gen(cid, prompt, anchors, aspect)

if __name__ == "__main__":
    main()
