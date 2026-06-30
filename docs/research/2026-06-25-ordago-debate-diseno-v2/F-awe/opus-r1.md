# Opus — Ronda 1 · Clúster F: Awe, money-shot renovable y momento memorable

**Asiento:** Diseñador de Sistemas + lente A2 (asombro). Lidero el **Presentador de Asombro** reutilizable.
**Cartas citadas:** A2🟡 (awe/anti-habituación), C1🟡 (legibilidad del clip), D3🟢 (audio/firma sonora), S5🟢 (artefacto-puente/share).

---

## (a) Steelman — El Presentador de Asombro como SISTEMA

Defino el §10.2 "Presentador de Asombro" como un **motor único, scriptado, con un slot intercambiable**. No es un asset por Diablo; es una sola cámara que se rellena.

**El motor (se construye 1 vez):**
1. **Pull-back cinemático scriptado** — al disparar el hito, la cámara deja de mirar la Mesa y hace un *zoom-out* que revela que tu Última Mano era parte de algo enorme (la sala del Diablo, el Romancero entero como mural, la banca del infierno colapsando). Vastness por **composición + escala súbita**, NO por fidelidad de render [A2🟡: "pull-back que revela que tu acto era parte de algo enorme"]. Esto es web-native barato: es coreografía de cámara sobre arte ya existente.
2. **Slot de contenido** = `{Trampa-firma del Diablo derrotado}` (su sello visual: el icono/skin del arquetipo que ya existe como carta jugable) + `{tema de Codicia/Condena}` en los hitos de maestría. **Lo único que cambia entre dosis es el contenido del slot.**
3. **Cue de audio de orden superior** — un golpe sonoro D3 que "cruza D3" (coro/campana/silencio→estruendo) [A2🟡; D3🟢]. El audio es el multiplicador de awe más barato que existe.
4. **Overlay de share** — anclado a §8.3 (export del clip): en el pico, CTA = **compartir/conectar, NUNCA comprar** [A2🟡, límite ético: awe encoge el yo → prosocialidad, no compra; Piff N=2.078]. El clip auto-exportable es el vehículo S5🟢.

**Disparadores espaciados (el GRID = el calendario):**
- **1er-clear de cada uno de los ~12-20 Diablos del Romancero** = ~12-20 dosis escalonadas (supuesto: el conteo exacto de arquetipos no está fijado en el contexto — lo marco como rango del GDD).
- **Hitos Codicia/Condena (D30+)**: 1er-clear de Codicia, cada N de Condena endless.

**Por qué el GRID reemplaza al live-ops:** en live-ops, la "novedad de temporada" cuesta un equipo permanente. Aquí, cada arquetipo del Romancero **ya es contenido jugable que César produce de todos modos**; el Presentador solo lo **reusa como dosis de awe a costo marginal ≈ swap de slot**. El grid finito de arquetipos sustituye al calendario infinito de eventos: cada Diablo nuevo = un esquema nuevo que volver a exceder [A2🟡: "need for accommodation"].

**Separación taxativa (A2🟡):**
- **(a) Clip DIARIO ASMR (§10.1):** el barrido de la Escoba. Placer cinético sensorial que **PIDE repetición** → motor D1-D7. No es awe.
- **(b) Money-shot RARO espectable (§10.2 nuevo):** el pull-back en hitos espaciados. Autotrascendente, **se apaga al repetirse** → por eso es raro, no diario.
No mezclar: son dos neuroquímicas distintas.

---

## (b) Ataque / mejora (me atico)

1. **"Misma animación, otro Diablo" = reconocimiento, no awe.** Riesgo real: si el motor de cámara es idéntico y solo cambia un icono en el slot, el cerebro del jugador acomoda el *esquema del Presentador* tras 2-3 dosis y el resto son reconocimientos [A2🟡: 90 días = 1 dosis + 89 reconocimientos]. **El slot debe alterar la SORPRESA CONCEPTUAL, no solo la skin** — cada Diablo necesita un *beat* de pull-back distinto (uno revela una multitud, otro revela vacío, otro invierte la cámara), o el sistema colapsa a una sola dosis.
2. **¿12-20 bastan para 50h+?** No, si se consumen jugando. **Pero A2🟡 ya lo resuelve: el awe es ASÍNCRONO.** El veterano (D30 <1.5%) no necesita 50h de awe propio; su awe **se ioniza en el chat** y el espectador D2 lo recibe como gancho de adquisición (patrón Getting Over It). Las 12-20 dosis no son para retener al veterano — son **munición de evangelización** que viaja en S5🟢. Reencuadre: el KPI no es "el veterano sigue asombrado", es "el clip del veterano convierte espectadores".
3. **El pull-back compite con C1🟡 (legibilidad).** Si la cámara se aleja durante el momento jugable, rompe la lectura de la Mesa. **Mitigación: el Presentador se dispara DESPUÉS de resuelta la mano** (post-victoria), nunca durante decisión. El awe vive en el epílogo, no en el gameplay.
4. **Límite donde deja de dar awe:** cuando el espectador puede **predecir el pull-back** antes de que ocurra. Ese es el punto de muerte del sistema, y es medible (gate abajo).

---

## (c) Resolución FALSABLE — Spec §10.2

**Estructura del Presentador:**
```
trigger(hito) →
  freeze post-victoria (0.5s) →
  pull-back cámara [variante_beat[Diablo]]  ← lo que renueva awe
  + render slot{firma_visual[Diablo] | tema[Codicia/Condena]}
  + cue_audio_D3[escala_creciente]
  + overlay_share (CTA: compartir) → export clip §8.3
```
**Qué cambia por slot:** (i) firma visual del Diablo [ya existe], (ii) **beat de pull-back** [≥1 de N plantillas: revela-multitud / revela-vacío / inversión / colapso], (iii) variante de cue D3. Lo demás es fijo.

**Anclaje a §8.3:** el clip se auto-recorta (3s hook + pull-back + sello) y se exporta listo para WhatsApp/Steam = artefacto-puente S5🟢.

**Gates falsables:**
- **G1 (habituación):** share-rate del **N-ésimo** Diablo NO cae vs el 1º (medido en cohortes). Si decae monótonamente → el slot no renueva awe → fail.
- **G2 (awe vs ASMR):** **pico de share 0-72h** del money-shot > clip diario ASMR. Awe = pico pronunciado; reconocimiento = curva PLANA. **El KPI discriminante es la forma de la curva 0-72h, no el volumen total.**
- **G3 (scope):** costo ≤ **1 sprint de artista por dosis** [A2🟡 cap]. Si una dosis exige pipeline de render dedicado → mal diseñado, kill.
- **G4 (predictibilidad / muerte del sistema):** en playtest, si >X% de espectadores anticipan correctamente el beat del pull-back → el motor se volvió esquema → necesita variante nueva.

**KPI que distingue awe de reconocimiento:** **pendiente del pico de share 0-72h** (awe = spike) vs **plano** (reconocimiento). G2 es el árbitro.

---

## (d) Decisión de César

**Trade-off real (solo César decide):**
1. **¿Cuánto presupuesto de arte por arquetipo va al SLOT del Presentador vs al Diablo jugable mismo?** Cada $ que va al beat de pull-back no va a la carta jugable. Mi recomendación: **slot mínimo viable (firma + 1 beat reusado de plantilla), arte al Diablo jugable** — porque G1 dice que lo que renueva awe es el *beat conceptual* (barato, diseño) no la fidelidad (caro, render) [A2🟡]. Pero el reparto exacto es suyo.
2. **¿El money-shot raro se ata SOLO a 1er-clears, o también a hitos de Condena endless?** Recomiendo: **1er-clears = dosis garantizadas (~12-20), Condena = dosis OPCIONAL solo si el costo marginal sigue ≤1 sprint** (G3). Atar awe a un endless infinito arriesga inflar scope sin techo — exactamente lo que el clúster prohíbe.

**Mi recomendación marcada como decisión de César:** construir el motor 1 vez, ~4 plantillas de beat compartidas entre los 12-20 Diablos (no 1 beat único por Diablo → eso sí infla scope), slot mínimo, awe atado a 1er-clears. Condena solo si G3 aguanta. **Decisión final: César.**

---

**Supuestos marcados:** conteo exacto de Diablos (~12-20), existencia de "firma visual" reusable por arquetipo y estructura precisa de §8.3/§10.1 se asumen del contexto; no verifiqué el GDD literal. Confianzas: A2🟡 (heurística anti-habituación, no ley), C1🟡, D3🟢, S5🟢.
