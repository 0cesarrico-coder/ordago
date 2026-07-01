"""Íconos de Maña (Pactos/Fullerías) folk-amuleto para ÓRDAGO. Transparentes, salida en game/assets/art/mana/."""
import os, time
from google import genai
from google.genai import types
HERE=os.path.dirname(__file__); OUT=os.path.join(HERE,"..","game","assets","art","mana"); os.makedirs(OUT,exist_ok=True)
c=genai.Client(api_key=os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
FOLK=("Mexican folk Posada amulet ICON, Day-of-the-Dead, ornate gold filigree, magenta/teal/marigold accents, "
 "engraved, bold iconic silhouette recognizable at 40px. Single centered emblem.")
TR=" Isolated on a FULLY TRANSPARENT background, centered, clear margin, no card frame."
ITEMS={
 "P1_oro":FOLK+" A PACTO amulet: a cursed golden coin stamped with a calaca skull and a tiny crown, dark chain. (greed pact)"+TR,
 "P2_filo":FOLK+" A PACTO amulet: a crossed pair of engraved steel daggers/edges with a drop of blood. (edge pact)"+TR,
 "P3_bosque":FOLK+" A PACTO amulet: a sacred tree with deep roots and a small red heart in the trunk. (forest pact)"+TR,
 "F1_lectura_falsa":FOLK+" A FULLERÍA amulet (the player's cheat): a mystic eye peeking, with a sly playing card hidden behind it. (false reading)"+TR,
 "F2_contrabando":FOLK+" A FULLERÍA amulet: a skeletal hand with crossed fingers smuggling a gold coin up a sleeve. (contraband)"+TR,
 "F3_doble_filo":FOLK+" A FULLERÍA amulet: a double-edged sword with a mirror reflection, glowing. (double edge)"+TR,
 "F0_ojo":FOLK+" A FULLERÍA amulet: a glowing all-seeing mystic crystal eye with rays. (the tahúr's eye, mastery)"+TR,
}
for cid,prompt in ITEMS.items():
    out=os.path.join(OUT,f"{cid}.png")
    for a in range(3):
        try:
            cfg=types.GenerateContentConfig(response_modalities=["TEXT","IMAGE"],image_config=types.ImageConfig(aspect_ratio="1:1"))
            r=c.models.generate_content(model="gemini-3-pro-image",contents=[prompt],config=cfg)
            ok=False
            for p in r.candidates[0].content.parts:
                if getattr(p,"inline_data",None) and p.inline_data.data:
                    open(out,"wb").write(p.inline_data.data); ok=True; print("OK",cid,os.path.getsize(out)//1024,"KB")
            if ok: break
        except Exception as e: print("!",cid,a,str(e)[:120]); time.sleep(3)
print("DONE mana")
