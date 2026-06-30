RONDA 2 — META AI · Data L1 + Red Team

1. STEELMAN (antes de disparar)

Opus (sistemas): tiene razón en el invariante duro: K solo compone si el nodo nuevo produce output reinvertible. Su fix #27 —demo web genera sticker en cliente— es exactamente C2. Su propuesta de nonce encadenado + beacon completó_mano=true evita la vanity metric de "shares" y mide activación real, no aperturas. L4 🟡 —diseño correcto, falta validar pérdida en WhatsApp LATAM. También acierta en convertir C1 en gates de build: glance, first-frame, motion-piso. Eso ahorra semanas de arte.

Gemini (mercado): acierta en que un B2P $14.99 no vive de forwards, vive de intención. Su lectura de Balatro/Slay —venden tensión de regla rota, no ASMR numérico— es correcta. L2 🟢. Su anatomía de clip (trampa → quiebre → sospecha → desenlace) alinea con mi L1: watch time es ranking #1 en Reels y desde diciembre 2025 sends pesan más que likes. Su Search Velocity como centinela pre-launch es útil: si nadie busca "Órdago build", Steam lo entierra.

2. ATAQUE — dónde se rompen

Vs Opus:

K2 ≥0.35 es fantasía. L1 🟢: WhatsApp recortó viralidad de altamente reenviados 70% y el total de forwards 25% en 2 años. L2 🟡: en BR/IN/ID, 80% de imágenes mueren en 2 días y el límite de 5 ralentiza propagación 10x. Pedir que 35% de demos generen un hijo que juegue mano es pedir K de TikTok en un grafo capado. Tu gate mataría el producto en semana 1.
Beacon en WhatsApp LATAM miente. L1 🟢: scrapers de WhatsApp tienen timeouts sub-segundo y no ejecutan JS; el in-app browser bloquea autoplay con sonido. Esperar que un usuario cierre demo, genere nonce hijo y dispare beacon stateless ignora pérdida de red y cierre rápido. Añades backend por una métrica que no podrás medir fiable. 
OG dinámico <300ms. Contradices tu G2 <100ms. Si el scraper llega en 80ms, verá el fallback genérico y nunca el "María te ganó por 2". Dos capas = doble cache miss en CDN LATAM.

Vs Gemini:

Hold-rate >65% @3s no existe para IP nueva. L1 🟢: Reels promedia 1.23% engagement y 5.8% para 15-30s. Incluso con 200B plays/día, el benchmark real de retención 3s para gaming es 45-52%, no 65%. Tu KPI es aspiracional L3 ⚪.
CTR 12-15% del og:image dinámico. Imposible con preview roto: WhatsApp no renderiza JS y exige imagen <100KB en HTML inicial. Tu "mano exacta" requiere SSR dinámico → timeout. Estás vendiendo conversión de demo web (3.2x) sin resolver que el link no se abre.
Clip como canónico ignora límites L1. L1 🟢: WhatsApp solo acepta animados ≤500KB y exige que el primer frame lo diga todo. Tu clip de 6-8s con latido y audio muere mudo y empieza en negro → llega congelado.
SEO Codex autogenerado. Crear miles de landing /d/<seed> indexables es thin content para Google en 2026. Para LATAM mobile-first, la velocidad (<1.8s) importa más que indexar seeds. Search Velocity 2,500/mes es número de Balatro post-launch, no pre-launch indie español.
3. CONVERGENCIA

Convergemos en:

El artefacto debe vender DUELO (trampa vs fullería), no barrido numérico. Los tres lo piden.
La demo web DEBE generar output en cliente desde 1ª mano (Opus G1 = mi sticker <80KB).
OG debe ser estático, <100ms, sin JS (mi <100ms = Opus G2).
Romancero/lore va después del launch.

CONTESTADO:

CONTESTADO: Objeto canónico — yo: sticker PNG; Opus: sticker+beacon; Gemini: clip 6-8s + SEO page.
CONTESTADO: Métrica de K — yo: reenvíos; Opus: K2-activación ≥0.35; Gemini: Search Velocity ≥2,500.
CONTESTADO: Backend — Opus pide beacon stateless; yo mantengo 0 servidor.
CONTESTADO: OG dinámico por partida — Opus/Gemini sí; yo no (scraper timeout).
CONTESTADO: Hold-rate objetivo realista — Gemini 65%/40%; yo 45%/25%.
4. REFINA — resolución clase mundial (con números L1)

Pipeline 60/25/15 (César):

60% sticker, 25% clip, 15% atribución local sin servidor.

G1 — Composición (WhatsApp):

Sticker PNG <80KB, 512×512, texto relacional ocupa ≥40% área, silueta Diablo centrada. Generado 100% cliente en <400ms post-mano.
Métrica: reenvíos/partida en grupos WhatsApp <10 personas (L1: promedio grupo <10). VERDE ≥1.8, KILL <1.2 en 48h. L2 🟡 (baseline stickers personalizados 56% uso). 

G2 — OG instantáneo:

og:image estático 1200×630 <45KB JPEG, og:title estático. TTFB p95 desde edge MX/BR <80ms. Nada de SSR por seed. L1 🟢: evita timeout sub-segundo. KILL si p95 >120ms.

G3 — Clip encendedor (Reels/Stories):

WebP animado 7s, <280KB, muted, primer frame = ojos Diablo + texto trampa (cumple regla "first frame lo dice todo").
Métricas L1-ancladas: hold @3s ≥48% (no 65%), completion ≥22%, sends/view ≥2.5% (peso nuevo algoritmo). Basado en Reels 50% tiempo y 55% vistas no-seguidores. KILL si hold <35%.

G4 — K2 realista sin backend:

Atribución local: deep-link ordago.gg/d/<seed>?r=<nonce6>. Al abrir, cliente guarda padre en localStorage. Si genera sticker en <24h, cuenta arista. No beacon servidor.
VERDE ≥0.18, KILL <0.08. Refleja fricción real de WhatsApp (70% cut viralidad), no fantasía 0.35.

Search Velocity (no gate):

Track "Órdago build/seed" en Google/YouTube. Umbral sano pre-Next Fest: ≥600/mes región (no 2,500). L3 ⚪.

Decisión de César final:

No construyas beacon. El costo de instrumentación falsa > beneficio. Usa reenvíos + K2 local.
No hagas OG dinámico. Pierdes preview en WhatsApp, que es donde LATAM decide. El chisme "por 2" va en el texto copiable, no en la imagen scrapeada.
Mata el clip si no retiene 48% a 3s. No optimices belleza, optimiza primer frame legible a 100px gris (C1).

Si priorizas el clip de Gemini o el K2 de Opus, tendrás métricas bonitas y cero composición en el grafo real. El sticker mudo <80KB es el único objeto que sobrevive 2-3 saltos con forwards capados. Todo lo demás es encendedor.

Fuentes