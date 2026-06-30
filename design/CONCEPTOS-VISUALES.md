# ÓRDAGO — Catálogo de Conceptos Visuales (Concept-Visual-First)

> Entregable del `visual-concept-director`, anclado a `design/STYLE-BIBLE.md` (PASO 0 ✓) y a la
> **composición del prototipo jugable** (`game/`, live). Define QUÉ mockups generar con el modelo
> de imagen de FRONTERA (**Nano Banana Pro = `gemini-3-pro-image`**) y los genera en `design/concepts/`.
> **Objetivo nº1: que el usuario ELIJA la dirección de arte (Lado A vs Lado B) antes de reemplazar
> los rectángulos por arte.** Cada concepto P0 se genera en AMBAS direcciones (A/B).

## Perfil inferido
Roguelike deckbuilder web-native, retrato móvil-first, premium B2P. Identidad: cantina barroca
folk-Posada, Diablo-tahúr tramposo carismático (no terror). Mercado LATAM+USA+hispanos. Bloques
aplicables priorizados al objetivo de DECISIÓN DE ARTE: **B0** (anclas/capsule), **B1/B2** (pantalla
de juego = donde más se nota amateur vs estudio), **B9/B2** (el Diablo), luego B3/B10 (victoria/sticker).
No-aplican ahora: B6 IAP (premium sin MTX), B5 battle-pass (sin live-ops).

## Las dos direcciones (el crux §11 — lo decide el usuario con estos mockups)
- **A — Claroscuro boutique premium:** negro + oro-vela, luz dramática, grabado Posada contenido
  (tipo Inscryption / Cult of the Lamb). Alto CTR en trailer. *Riesgo: blanqueamiento.*
- **B — Maximalismo identitario:** oro sucio + cempasúchil + papel picado, color y textura folk
  Día de Muertos, maximalista con jerarquía de valor. *Autenticidad, mitiga apropiación.*

## Catálogo (oleada 1 = P0, lo que decide la dirección)
| ID | Concepto | Prio | Propósito | Variantes |
|---|---|---|---|---|
| B1.1 | **Pantalla de juego** (HUD+Mesa+mano+Diablo) | P0 | la composición que separa amateur de estudio; ancla = prototipo | A claroscuro / B maximalista |
| B0.1 | **Key-art / capsule** | P0 | superficie de conversión más cara; hook "trampa al Diablo" | A / B |
| B2.1 | **El Diablo-tahúr** (reparte y te pilla) | P0 | el personaje; money-shot §10.2; reacción legible muda | A / B |
| B3.1 | **Victoria + ficha-sticker** (§8.3) | P1 | artefacto-puente; chisme legible @100px grises | A / B (oleada 2) |
| B5.1 | **La Cantina** (tienda de Maña) | P1 | trade-off faustiano legible (Pacto corrupto vs Fullería tuya) | oleada 2 |
| B2.2 | **Trampa sobre la Mesa** (Oros agrietados, HUD reescribe 13) | P1 | el corazón dual debe LEERSE | oleada 2 |
| B6.x | set de cartas (número/figura 8-9-10/Mata/Marcada) | P2 | legibilidad del valor; palo por forma | oleada 3 |

## Gate de validación (todos): silueta · glance 100×100 grises · legible mudo · cohesión Bloque 0 · composición no-calcomanía.

---

## Fichas P0 (con prompts listos — el texto exacto que se envía al modelo)

### B1.1 — Pantalla de juego (la decisión central)
- **Composición (anclada al prototipo):** retrato 9:16. Arriba HUD: nombre de apuesta ("LA CHICA")
  a la izquierda, Reales en oro a la derecha; barra de progreso al umbral del Diablo. Fila de **3
  ranuras de Maña** (cartas-amuleto: Pacto del Oro 🪙, Pacto del Bosque 🌳, Fullería "Lectura
  Falsa" 👁). Centro: **tapete de fieltro verde gastado de cantina** ("LA MESA DEL DIABLO") con
  **5 naipes de baraja española boca arriba** (Oros/Copas/Espadas/Bastos visibles). Detrás del
  tapete asoma **el Diablo-tahúr** (croupier) observando. Abajo: **mano de 3 naipes**; botones
  "PASAR" y "ESCOBA" (oro). Velas, oro sucio. **Estado 100% legible (visual-primario §3.4).**
- **Aceptación:** legible @100×100 grises; Puntos/Suerte/Manos distinguibles por forma+color; el
  Diablo no tapa las cartas; composición = la del prototipo (verificable con screenshot).

### B0.1 — Key-art / capsule
- **Composición:** 16:9. El **Diablo-tahúr** carismático repartiendo naipes españoles sobre el
  tapete, una mano del jugador haciéndole **trampa** (carta escondida en la manga / guiño cómplice).
  Título **ÓRDAGO** integrado (no pegado). Hook visual: "le haces trampa al Diablo". Velas, cantina.
- **Aceptación:** el gancho ("trampa al Diablo con cartas") se entiende <1.2 s; glance-gate ≥90%.

### B2.1 — El Diablo-tahúr
- **Composición:** 3:4. Retrato del Diablo como tahúr de cantina estilo **grabado Posada/calaca**,
  cuernos, sonrisa pícara, repartiendo o pillándote; líneas de grabado/filigrana, reconocible a
  100 px. Dos beats: (a) reparte con intención, (b) te pilla ("¡tramposo!").
- **Aceptación:** silueta reconocible; reacción física legible muda; no gore.
