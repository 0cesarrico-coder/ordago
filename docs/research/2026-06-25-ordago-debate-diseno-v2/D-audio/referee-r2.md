# REFEREE R2 — Clúster D (Audio) · Medición de convergencia

Contexto fresco, no debatiente. Mido convergencia, no opino de diseño. Comparo R2 vs R1 de las 3 IAs (Opus, Gemini, Meta AI).

---

## 1. CONSENSO 3/3 (las tres IAs convergen, R2)

Tras R2 las tres IAs declaran explícitamente convergencia en estos puntos (citados en sus secciones CONVERGENCIA):

1. **#22 — Primer contacto es mudo por física de plataforma.** El audio debe armarse en el primer gesto (`AudioContext.resume()` en el handler), con fallback visual+vibración si `play()` falla (low-power/data-saver). Las 3 lo marcan 🟢. (Opus r2 §CONVERGENCIA; Gemini r2 #22; Meta r2 §3.)

2. **#23 — Sticker viaja siempre mudo; gemelo visual onomatopéyico obligatorio.** No existen stickers sonoros nativos en WhatsApp. El grito viaja como glifo tipográfico. 🟢 las 3.

3. **#67 — Ninguna señal de juego vive solo en audio (gate simétrico).** Emisor estructural (`emitStateCue`/`emitGameplayEvent` con visual no-nullable), QA mute-total 100% por build. 🟢 las 3.

4. **#17 — Emoji-artefacto es red de seguridad, NO canal primario.** Línea Unicode client-side, medida aparte, se mantiene si supera umbral. 🟢 las 3.

5. **#32 (principio) — El audio porta estado, pero NUNCA solo; presupuesto visual≈audio.** Las 3 aceptan que el estado debe ser legible en mute. 🟢 en principio.

6. **NUEVO consenso R2 — Mute es DEFAULT (85-90% feed LATAM), no caso de accesibilidad.** Aporte L1 de Meta; Opus lo acepta y reescala a "visual-primario, audio-amplificador"; Gemini lo lista como contestado-aceptado ("100% jugable en mute"). Convergencia fuerte nacida en R2.

7. **NUEVO consenso R2 — Techo de frecuencia: el audio de Sospecha evita 500Hz-2kHz** (banda voz/música de fondo). Aporte de Gemini, adoptado explícitamente por Opus ("incorporo a Gemini") y Meta ("toma de Gemini"). Las 3 lo integran en R2.

8. **NUEVO consenso R2 — eyes_closed_test ≥75% como gate de #32.** En R1 los umbrales divergían (Meta pedía >80%). En R2 Meta "adopto umbral Opus, realista" (≥75%) y Gemini usa ≥80% en eyes-closed pero con mute-total ≥85% como complemento. Convergencia casi total (ver contestado residual).

---

## 2. CONTESTADOS (postura de cada IA, estado R2)

**C1 — Nº de nodos de grito al lanzamiento (#31).**
- Opus: **2** (Norte MX/US-hispano + Sur/Caribe).
- Gemini: **2** pero redefine cuáles → MX + **AR/Rioplatense** (corrige su "Nodo Sur=España+Cono Sur" de R1 tras ataque de Opus-r2).
- Meta: **3** (mx "¡No manches!", caribe "¡Échale!", us-centroamericano "¡Dale!"), con dato L1 (frases locales +2.1x share).
- Estado: **NO resuelto por evidencia.** Las 3 lo marcan como decisión de César. Divergencia 2 vs 2 vs 3, y además desacuerdo sobre CUÁLES nodos (Caribe vs Rioplatense). Persiste de R1 a R2.

**C2 — Umbral de repetición del grito mudo (#23).**
- Opus R1: ≥40% → **Opus R2 no lo redefine explícito** pero su #23 r2 ya no insiste en 40%; Meta lo atacó como irreal.
- Meta: ≥18% (R1) → **≥20%** (R2, "ajustado tras ver datos Opus"), con L1 (imitación vocal real 18-22%).
- Gemini: no define umbral de repetición.
- Estado: **CONVERGIENDO.** Meta aporta L1 dura (18-22% real); el 40% de Opus quedó sin defender en R2. Lo zanja la data de Meta, no más debate. Cuasi-resuelto hacia ~18-20%.

**C3 — Disparo en cualquier tap vs evento semántico (#22).**
- Opus: primer evento **semántico** (primera carta jugada), no tap accidental.
- Meta R1: cualquier primer tap → **R2 hace STEELMAN del semántico de Opus** ("evita desperdiciar la ventana en scroll accidental", 🟢). Acercamiento.
- Gemini: primer tap en pantalla inicio (cualquiera).
- Estado: **CONVERGIENDO.** Meta se movió hacia Opus en R2; solo Gemini sigue en "cualquier tap". Resoluble.

**C4 — Peso máximo de la firma de audio (#22).**
- Gemini: <40KB inline. Opus R2: <35KB (lo adopta, afina). Meta R2: <35KB Opus codec (lo adopta).
- Estado: **RESUELTO en R2** (convergió a <35-40KB; Opus y Meta adoptaron el aporte de Gemini). Ya no contestado.

**C5 — KPIs de release: comprensión vs negocio.**
- Opus: dos capas → GATE=comprensión (eyes_closed/mute_total/repetición), NORTH-STAR=negocio (no bloqueante).
- Gemini: KPIs de negocio (hold_rate, click_thru_steam, +12/+15%).
- Meta: ataca números de negocio de Gemini como ⚪ sin fuente L1; acepta lift moderado (+12% no +15%).
- Estado: **CONVERGIENDO** hacia el marco de Opus (gate vs north-star). Meta valida el ataque de Opus a los números ⚪ de Gemini. Cuasi-resuelto.

---

## 3. CAMBIOS R1 → R2 (movimiento de posiciones)

**Opus (el mayor cambio del clúster):**
- R1: audio de estado tratado como audio-primario; mute como caso de accesibilidad (~5%).
- R2: **invierte la doctrina rectora** a "visual-primario, audio-amplificador" tras el dato L1 de Meta (mute=default 85-90%). Invariante `state_is_visual_complete` antes de añadir audio.
- Adopta el techo de BANDA de Gemini (500Hz-2kHz) sumándolo a su techo de gain.
- #23: reemplaza su invariante de bounding-box (15-30% área) por legibilidad OCR a 96×96px (≤2 palabras) — adopta el cuello de botella real de Meta.

**Gemini:**
- R1: "Nodo Sur" = España + Cono Sur (agrupados).
- R2: **corrige** tras ataque de Opus → separa, escoge MX + **Rioplatense (AR)** como los 2 nodos foso. Abandona el grito "universal/teatral" de R1.
- Mantiene sus números de negocio (+12%/+15%) pese a ser atacados como ⚪ por Opus y Meta — endurecimiento parcial aquí.

**Meta AI:**
- Hace steelman explícito del semántico-tap de Opus y del techo de capas (≤2) → se acerca.
- Ajusta umbral repetición 18%→20% reconociendo datos de Opus.
- Adopta eyes_closed ≥75% de Opus (abandona su 80% de R1) y la banda de frecuencia de Gemini.
- Ajusta lift de sesión +15%→+12% por prevalencia de mute.
- Mantiene **3 nodos** (no cede a 2): único punto donde se sostiene firme con L1.

**Patrón global:** R2 muestra fuerte convergencia por absorción mutua (Opus absorbe mute-default+banda; Meta absorbe semántico+eyes_closed+banda; Gemini absorbe separación cultural). Net: contestados de R1 (≥6 dispersos) se redujeron a 1 duro (C1 nodos) + 2-3 convergiendo. Casi ningún endurecimiento salvo Gemini con sus KPIs de negocio ⚪.

---

## VEREDICTO

Consenso amplió de ~5 a ~8 puntos. De los contestados, C4 quedó resuelto; C2/C3/C5 están convergiendo (zanjados por data L1 de Meta o por absorción, no requieren más debate). Solo **C1 (nº de nodos: 2 vs 2-redefinido vs 3)** queda como genuina decisión de César sin evidencia que lo zanje — es 1 contestado duro. Cae en CONVERGED (≤1 contestado real; el resto lo zanja data/experimento).

SCORE-INPUT: contested=1 flipped=3 consensus=8 total=9 verdict=CONVERGED
