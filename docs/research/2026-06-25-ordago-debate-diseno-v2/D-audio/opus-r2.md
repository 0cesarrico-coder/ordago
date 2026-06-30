# CLÚSTER D — Audio · RONDA 2 · CROSS-REVIEW · ASIENTO OPUS

Mantengo mi tesis R1: dos sistemas (IDENTIDAD↔ESTADO) × {viral, in-game, accesibilidad}, con dos límites duros (U-invertida #09 y gate simétrico #67 estructural). La R2 me obliga a corregir UN número clave: mi umbral de mute estaba implícito; Meta AI lo vuelve explícito y eso cambia la doctrina rectora.

---

## STEELMAN de lo que difiere de mí

**Meta AI — "mute no es accesibilidad, es default" (85-90% feed LATAM).** 🟢 Es el aporte L1 más fuerte del clúster y refuta mi marco: yo traté el mute como caso de accesibilidad (#67, ~5% sordos). Meta AI demuestra que el caso silencioso es la MAYORÍA. Consecuencia: el sistema de ESTADO (#32) no puede ser "audio-primario con respaldo visual" — debe ser **visual-primario con audio como amplificador**. Mi presupuesto estaba invertido.

**Meta AI — "el grito no será musical, será frase-sticker; priorizar legibilidad" + "WhatsApp recorta texto en stickers, ~2 palabras máx legibles".** 🟡 Steelman: ataca mi invariante de composición (#23, glifo 15-30% del área) con dato de plataforma — el cuello de botella no es el área, es la LEGIBILIDAD a tamaño preview. Es más falsable que mi bounding-box.

**Gemini — banda de frecuencias: el audio de Sospecha debe evitar 500Hz-2kHz (voz/música de fondo) y vivir en los extremos.** 🟡 Es un criterio de mezcla concreto que yo NO tenía. Mejora real mi techo-de-gain (#32): no basta limitar volumen, hay que limitar BANDA para no competir con el podcast del jugador (que es la causa nº1 de mute total → pierdes el canal entero).

**Gemini/Meta — peso de Steam/wishlist y CTR (#22 hold-rate +12%, click_thru_steam).** Steelman: mis KPIs eran de comprensión (firma_heard, eyes_closed); ellos atan a NEGOCIO (retención→wishlist). Ambos niveles importan.

---

## ATAQUE (cito)

- **Gemini #22 — "incremento ≥12% en retención… +8% click_thru_steam".** ⚪ Números inventados sin fuente; "Among Us +22% hold-rate" no es citable. Útiles como hipótesis, NO como umbral de release. Y choca con su propio ataque (latencia 3G): si exiges firma <40KB precargada en primer frame, el +12% no es atribuible a la firma sino al tiempo de carga. Confunde variables.

- **Gemini #32 — "Avg_Session_Length +15%" y "Cheating_Success_Rate +10% más balanceada".** ⚪ KPI mal diseñado: el audio NO debe cambiar la tasa de éxito de fullerías (eso sería el audio dando ventaja mecánica = pay-to-hear, rompe fairness). Medir session-length confunde "decodifica estado" con "engancha más". Mi `eyes_closed_test` mide la causa real (decodificación), no un proxy contaminado.

- **Meta AI #32 — "audio +12% comprensión en tutoriales (Meta Ads)".** 🟡 Dato de tutoriales-video ≠ decodificación-de-estado-en-loop. Transferencia no demostrada. No invalida la capa, pero no es la evidencia que aparenta.

- **Gemini #67 — "diferencia retención D1 mute vs sound <3%".** Bien dirigido pero INSUFICIENTE como gate: un juego puede tener D1 igual y aun así perder partidas por tells no percibidos. Mi `mute_total` (binario, 100% eventos con equivalente visual, oracle de diff visual) es el gate duro; el ≤3% es KPI complementario, no sustituto.

- **Toda IA — saturación.** Ni Gemini ni Meta ponen TECHO en código al nº de capas sonando a la vez. Sin mi `audio_layers_active ≤ 2`, la suma de sus fixes (firma + leitmotiv + Sospecha + 3 firmas resultado) es la sopa ansiógena que viola #09. Sigue siendo mi aporte no replicado.

---

## CONVERGENCIA

- **#22:** primer tap arma audio; es física de plataforma, no preferencia. Fallback visual+vibración si `play()` falla (low-power/data-saver). CONVERGE 🟢 (las 3).
- **#23:** glifo onomatopéyico obligatorio + grito imitable. CONVERGE 🟢.
- **#67:** "ninguna señal vive solo-audio"; QA mute-total por build. CONVERGE 🟢.
- **#17:** red de seguridad, NO motor; medir aparte; mantener si supera umbral. CONVERGE 🟢.
- **#32:** el audio porta estado PERO nunca solo; presupuesto ≈50/50 visual/audio (Meta lo formula, yo lo acepto: corrige mi sesgo audio-primario). CONVERGE en principio 🟢.

- **CONTESTADO — mute como default vs accesibilidad:** Meta (default 85-90%) vs mi marco R1 (caso de ~5%). ACEPTO la corrección: reescalo a visual-primario.
- **CONTESTADO — nº nodos de grito #31:** Gemini=2 (Norte/Sur por IP), Meta=3 (mx/caribe/us-centroamericano), yo=2. No resuelto por evidencia → decisión de César.
- **CONTESTADO — grito musical vs frase-sticker #23:** Meta=frase legible; yo/Gemini=DUAL (sonoro 1-3s + glifo). No es excluyente: el activo es dual, pero en el CANAL sticker prevalece el glifo legible. Refino abajo.
- **CONTESTADO — KPIs de release:** comprensión (mío) vs negocio (Gemini/Meta). Ambos, en capas distintas (gate vs north-star).

---

## REFINA — resolución falsable

1. **Doctrina rectora corregida (mi mayor cambio R2):** **visual-primario, audio-amplificador.** Invariante `state_is_visual_complete`: el `mute_total` oracle debe pasar al 100% ANTES de que cualquier capa de audio de estado entre a producción. El audio se construye SOBRE un juego ya 100% legible en silencio. (Mata el riesgo de Meta de "pierdes partida en mute".)

2. **#23 — legibilidad como gate, no área.** Reemplazo mi invariante de bounding-box por: `grito_glifo ≤ 2 palabras`, legible a **96×96 px** (tamaño preview sticker WhatsApp) verificado por OCR automático en el render (linter `glifo_ocr_legible`). El activo sigue siendo DUAL; en canal sticker manda el glifo.

3. **#32 — techo de gain + techo de BANDA (incorporo a Gemini):** invariante `suspicion_audio_gain ≤ 0.8*master` Y `suspicion_freq ∉ [500Hz, 2kHz]` (vive en sub-200Hz o >4kHz). Máximo `audio_layers_active ≤ 2`. Gate de release = `eyes_closed_test ≥75%` (kill <60%) SOBRE base visual ya validada. KPI ético: `quit_rate` en Sospecha-alta ≤ baseline (gate 12). NO medir Cheating_Success_Rate (rechazo el KPI de Gemini).

4. **#31 — 2 grabaciones canónicas al lanzamiento** (Norte: MX/US-hispano; Sur/Caribe), resto post-EA por data de share. Kill por nodo: bloqueo/reporte WhatsApp **>0.25%** (Meta L1) O repetición <25%.

5. **KPIs en dos capas:** GATE de release = comprensión (eyes_closed 75%, mute_total 100%, repetición ≥25%). NORTH-STAR de negocio = hold_rate/wishlist (Gemini/Meta), medido pero NO bloqueante (números sin fuente, ⚪).

**Lo PRIMERO a falsar por centavos (sin cambios):** test de repetición del grito mudo (#23) + eyes_closed_test (#32). n≥15-20 humanos, cero código de producción. Deciden si "audio de orden superior" es real o aspiracional.

---

## Decisiones de César (acotadas)
1. **Nodos de grito al lanzamiento: 2 o 3** (mi reco: 2; Meta empuja 3 con frases L1 concretas — defendible).
2. **grito_glifo en caption copiable además del sticker-imagen** (sí/no; reco: ambos).
3. **#17 con medición propia o solo línea garantizada** (reco: línea + 1 evento analítico, sin pipeline).
