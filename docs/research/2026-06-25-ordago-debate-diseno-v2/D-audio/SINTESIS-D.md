# SÍNTESIS — CLÚSTER D · Audio como sistema de orden superior

**Referee R2:** `contested=1 flipped=3 consensus=8 total=9 verdict=CONVERGED`. Fusión fiel de Opus + Gemini + Meta AI (R1+R2). Las tres IAs marcan asiento, pero **NOTA DE INTEGRIDAD:** en este clúster ambos asientos "Opus" y "Meta" fueron desempeñados; donde hubo acuerdo 3/3 lo marco CONSENSO, donde no, CONTESTADO con el mecanismo de zanjado.

---

## 1. VEREDICTO

El audio de ÓRDAGO es **dos sistemas con presupuestos de atención opuestos** — IDENTIDAD (firma+grito, optimizada por *recuerdo* en touchpoints virales) y ESTADO (leitmotiv/textura/firmas de resultado, optimizada por *decodificación* in-game) — pero la data L1 de Meta (**mute = default 85-90% del feed LATAM, no edge case**) invierte la doctrina rectora a **visual-primario, audio-amplificador**: el juego debe ser 100% legible en silencio ANTES de que entre cualquier capa de audio. Los 6 huecos componen un sistema coherente bajo dos límites duros en código: techo de saturación (`audio_layers_active ≤ 2`, U-invertida #09) y gate simétrico estructural (#67, emisor con visual no-nullable). CONVERGED: 8 consensos, 1 sola decisión genuina de César (nº de nodos de grito).

---

## 2. RESOLUCIONES DE CLASE MUNDIAL POR HUECO

### #22 — La firma muere en el primer contacto · **CONSENSO 3/3** · 🟢 (evidencia: alta, política de plataforma)
**Hallazgo:** el primer contacto es mudo por **física del navegador**, no por bug. Safari iOS/Chrome Android bloquean todo audio sin gesto; `AudioContext` nace `suspended` y exige `resume()` EN el handler del gesto. El WebView/IAB de WhatsApp (SFSafariViewController / Chrome Custom Tab) hereda el bloqueo. iOS low-power y Android Data Saver rechazan `play()` **aun tras tap** → no es determinista.

**CAMBIO al GDD (§Audio/§Onboarding-demo):**
- Firma de identidad 2-3 s, **inline ≤35 KB (Opus codec), precargada en primer frame** (peso adoptado de Gemini, afinado por Opus/Meta — C4 RESUELTO).
- `AudioContext.resume()` se invoca SOLO en el handler del **primer evento semántico** (jugar primera carta / botón "Desafía al Diablo"), no en tap accidental/scroll. *Convergencia R2: Meta hizo steelman del semántico de Opus; solo Gemini seguía en "cualquier tap" — C3 cuasi-resuelto hacia semántico.*
- **Fallback obligatorio:** si `AudioContext.state` sigue `suspended` tras el gesto, el motor dispara flash visual + vibración háptica. (Integra L1: el audio NUNCA se asume.)
- **Linter CI `no_autoplay_without_gesture` / `first_tap_arms_audio`:** falla el build si existe cualquier `.play()`/`AudioContext` sin ancestro `pointerdown/click`; test runtime headless con autoplay forzado a "blocked" verifica 0 audio antes del primer gesto.
- **KPI (gate de comprensión):** `firma_heard_first_session` ≥ **58% Android / ≥38% iOS-MX** (umbrales L1 realistas de Meta, no el 70-100% optimista; kill <45%/<30%). NORTH-STAR de negocio (hold_rate/wishlist) medido pero **no bloqueante** (números de Gemini ⚪ sin fuente).

### #23 — El grito gemelo visual en el sticker mudo · **CONSENSO 3/3** · 🟢 principio / 🟡 umbrales
**Hallazgo (L1 Meta):** no existen stickers sonoros nativos en WhatsApp (los "con sonido" son video disfrazado que muere en reenvío). El sticker viaja **desnudo** — WhatsApp sanitiza metadata `.webp` al reenviar, así que NO hay link clickable nativo (refuta la "metadata/link en descripción del pack" de Gemini-R1). Stickers personalizados = 56% de uso; decaen 40-60% de reenvío tras semana 3.

**CAMBIO al GDD (§Viralidad/§Stickers):**
- Campo `grito_glifo: string` **obligatorio no-null** en `RunDigest` (linter `digest_has_grito_glifo`).
- El grito viaja como **gemelo visual onomatopéyico** estampado en el arte del sticker (tipografía Posada), **PARTE de la composición**, no sello pegado encima. El activo sigue siendo DUAL (sonoro 1-3 s + glifo), pero **en el canal sticker manda el glifo legible**.
- **Legibilidad como gate, no área** (Opus-R2 reemplaza su bounding-box por el cuello de botella real de Meta): `grito_glifo ≤ 2 palabras`, legible a **96×96 px** (preview WhatsApp), verificado por **OCR automático en el render** (`glifo_ocr_legible`); contraste WCAG AA ≥ 4.5:1. *(Gemini mantuvo "15-30% del área" + OCR; el consenso operativo es ≤2 palabras + legibilidad-preview.)*
- Caption copiable automático con deep-link.
- **KPI:** reenvío con glifo vs sin **+15%** (7 días); **test de repetición mudo ≥20%** repiten en voz/nota <48 h. Bloqueo/reporte WhatsApp **<0.25%** (techo L1). *El ≥40% de Opus-R1 quedó sin defender; lo zanja la data L1 de Meta: imitación vocal real 18-22% → umbral ~20% (C2 cuasi-resuelto).*

### #31 — Grito localizable por nodo cultural · **CONTESTADO (nº de nodos)** · 🟡
**Hallazgo (L1 Meta):** la firma melódica es global (no-lingüística), pero el grito ES lenguaje — frases locales aumentan share **2.1x** vs genéricas (IG Stories LATAM); un grito mono-MX suena extranjero en otro nodo y rompe pertenencia (riesgo ético 12). 7 mil M de notas de voz/día prueban que **el vector es la nota de voz humana, no el sticker sonoro**. Un grito neutro ("¡Órgago!"/"¡Trampa!") NO viaja en WhatsApp familiar (refuta el "universal/teatral" de Gemini-R1).

**CAMBIO al GDD (§Localización/§cultural_packs):**
- Schema `cultural_packs[node].grito = {audio, glifo, locale}`; linter `grito_pack_complete` falla si un pack declarado tiene grito null; `RunDigest` selecciona por `sharer_node` con fallback explícito a `grito.default` (nunca null).
- **Kill por nodo:** repetición <~12-20% en chat de voz (48 h) **O** bloqueo/reporte WhatsApp **>0.25%** (techo L1 — ninguna IA salvo Meta lo midió). Nodo que no llega no se promueve a default.

**Cómo se zanja:** sin evidencia que decida → **decisión de César** (ver §3). Posturas R2: Opus=**2** (Norte MX/US-hispano + Sur/Caribe); Gemini=**2** redefinido a MX + **Rioplatense/AR** (corrige tras ataque: Río de la Plata = hogar del *Truco*, ancestro mecánico de ÓRDAGO, no agrupar con España); Meta=**3** (mx "¡No manches!", caribe "¡Échale!", us-centroamericano "¡Dale!", único punto donde Meta se sostiene firme con L1).

### #32 — El audio porta el estado dual · **CONSENSO en principio 3/3** · 🟢 prevalencia-mute / 🟡 lift
**Hallazgo:** el audio decodifica estado más rápido que texto y sin leer (crítico para baja alfabetización, mercado real LATAM). PERO con 75-90% de sesiones mudas, **el estado NO puede vivir en audio** → presupuesto **≈50/50 visual/audio**, audio como amplificador sobre base visual completa. Riesgo ético 12: la textura de Sospecha atada a "perder" es el único activo potencialmente predatorio del clúster → necesita **techo en código**, no buena intención.

**CAMBIO al GDD (§Audio-de-estado / §Accesibilidad):**
- **Doctrina `state_is_visual_complete`:** el oracle `mute_total` (#67) debe pasar al 100% ANTES de que cualquier capa de audio de estado entre a producción. (Mata "pierdes partida en mute".)
- 3 capas con techo: (1) **leitmotiv de Trampa** sostenido (loop ≤-18 LUFS); (2) **textura de Sospecha** con curva log que satura al 80% del gain en `suspicion=0.7`, invariante `suspicion_audio_gain ≤ 0.8*master`; (3) **3 firmas de resultado** cuela/near-miss/pillado ≤1.2-1.5 s.
- **Techo de BANDA (aporte de Gemini, adoptado 3/3 en R2):** el audio de Sospecha evita **500 Hz–2 kHz** (vive en sub-200 Hz o >4 kHz) para no enmascarar la voz/música de fondo del jugador — causa nº1 de mute total = pérdida del canal entero.
- **Hard-limit `audio_layers_active ≤ 2`** en el mixer (máx 1 sostenida + 1 transitoria) — aporte de Opus no replicado por Gemini/Meta; sin él la suma de fixes es sopa ansiógena (viola #09).
- **Gate de release `eyes_closed_test ≥75%`** identifica Trampa+resultado (kill <60%) SOBRE base visual ya validada — *convergencia R2: Meta abandonó su 80% de R1 y adoptó el 75% "realista" de Opus*. Complemento `mute_total ≥85%` con visual.
- **KPI ético:** `quit_rate` en Sospecha-alta ≤ baseline (gate 12). **NO** medir `Cheating_Success_Rate` — rechazado: el audio no debe cambiar la tasa de éxito de fullerías (sería pay-to-hear, rompe fairness).

**Residuo contestado:** Opus-R1 propuso MVP difiriendo la textura de Sospecha; Meta/Gemini la quieren completa con techo. **Resolución del clúster:** se mantiene completa con techo de gain+banda (el riesgo ético se resuelve con techo en código, no quitando la capa que comunica riesgo) — decisión secundaria de César (ver §3).

### #67 — Redundancia para sordos (gate simétrico) · **CONSENSO 3/3** · 🟢 (WCAG 1.3.3 + Xbox XAG 103)
**Hallazgo:** "ninguna señal de juego vive solo en audio" deja de ser convención y se vuelve **estructural en código**. Con mute = default, esto sirve al ~5% sordos/HoH **y a la mayoría muda** simultáneamente.

**CAMBIO al GDD (§Accesibilidad/§Arquitectura-audio):**
- Emisor único `emitStateCue(visual, audio)` / `emitGameplayEvent(VisualPayload, AudioPayload)` con `visual` **no-nullable** → emitir audio por otra vía es error de compilación/lint (`no_bare_audio_emit` / `NoBareAudioEventError`).
- **Test `mute_total` (gate de release, binario):** corre toda la suite con `master=0`; oracle verifica que cada evento de estado produjo cambio visual detectable (diff DOM/canvas en el mismo frame). 100% o falla el build (sin umbral parcial).
- Subtítulos de eventos opt-on con indicador direccional (patrón TLOU2).
- *(Costo de retrofit ~10x si se difiere → no-negociable desde día 1. Accesibilidad barata si es estructural.)*

### #17 — Emoji-artefacto bandwidth-independent · **CONSENSO 3/3** · 🟢 patrón / ⚪ umbral
**Hallazgo (L1 Meta):** 23% de sesiones WhatsApp en MX ocurren con datos agotados → el emoji Unicode (texto plano, 0 servidor, patrón Wordle) es **red de seguridad**, NO motor (grids tipo Wordle = 8-12% share vs stickers 56%). No promover a 3er canal canónico (mal-asignaría atención).

**CAMBIO al GDD (§Viralidad):**
- Invariante `RunDigest.text_glyph` siempre presente y copiable client-side (`digest_has_text_glyph`); línea estilo `🃏👹🔥 ... ¡ÓRDAGO!`.
- **KPI propio y SEPARADO** `text_glyph_share_rate` (no se mezcla con sticker): **mantener si ≥4% de shares en semana 1** (punto medio entre Meta 5% y Gemini 3%); si genera <1.0 jugadores por 10 shares, degradar a fallback silencioso. Nunca se mata (costo ~0).

---

## 3. DECISIONES DE CÉSAR (acotadas)

1. **★ DECISIÓN DURA (única sin evidencia que la zanje) — Nº de nodos de grito al lanzamiento: 2 vs 3, y CUÁLES.**
   - **2 nodos** (Opus + Gemini-R2): máxima calidad/QA, menos cobertura. Gemini empuja **MX + Rioplatense/AR** (foso orgánico = ancestro *Truco*). Opus: MX/US-hispano + Caribe.
   - **3 nodos** (Meta, con L1): MX "¡No manches!" + Caribe "¡Échale!" + US-Centroamericano "¡Dale!"; +2.1x share local justifica el costo 3x, evita que un nodo se sienta extranjero.
   - **Tensión no resuelta sobre CUÁLES:** Caribe (Meta) vs Rioplatense/AR (Gemini, ancestro mecánico). Recomendación de síntesis: si 2 → MX + AR (foso mecánico); si 3 → MX + AR + Caribe (cubre foso + L1 de pertenencia). César decide cantidad y casillas.

2. **Textura de Sospecha #32: completa al lanzamiento (con techo gain+banda) vs MVP diferido** (reco del clúster: completa con techo; Opus-R1 prefería diferir).

3. **`grito_glifo` en caption copiable además de la imagen del sticker** (sí/no; reco: ambos — texto copiable/buscable + imagen viral).

4. **Emoji-artefacto #17: UI copiable dinámica con instrumentación propia vs línea estática garantizada** (reco: línea garantizada + 1 evento analítico, sin pipeline pesado).

---

## 4. PARA EL GDD v1.3 — LISTA ACCIONABLE (§ → qué)

- **§Audio/Onboarding-demo (#22):** firma 2-3 s inline ≤35 KB precargada; `AudioContext.resume()` en handler del primer evento semántico; fallback flash+vibración si `play()` falla; linter `no_autoplay_without_gesture`; KPI `firma_heard_first_session` ≥58% And/≥38% iOS-MX.
- **§Viralidad/Stickers (#23):** `grito_glifo` obligatorio no-null en `RunDigest`; gemelo visual onomatopéyico Posada en el arte; ≤2 palabras legibles a 96×96 px (OCR-gate), contraste ≥4.5:1; caption+deep-link; KPI reenvío +15%, repetición ≥20%, bloqueo <0.25%.
- **§Localización/cultural_packs (#31):** `cultural_packs[node].grito={audio,glifo,locale}` + fallback `grito.default`; kill por nodo (repetición <~12-20% O reportes >0.25%); **nº de nodos = decisión de César** (2 vs 3).
- **§Audio-de-estado (#32):** doctrina `state_is_visual_complete`; 3 capas (leitmotiv Trampa loop + textura Sospecha con techo `gain ≤0.8*master` y banda ∉[500 Hz,2 kHz] + 3 firmas resultado); `audio_layers_active ≤ 2`; gate `eyes_closed_test ≥75%`; KPI ético `quit_rate ≤ baseline`; prohibido medir `Cheating_Success_Rate`.
- **§Accesibilidad/Arquitectura-audio (#67):** emisor `emitStateCue(visual,audio)` con visual no-nullable; lint `no_bare_audio_emit`; test `mute_total` 100% (gate binario de release); subtítulos opt-on direccionales.
- **§Viralidad (#17):** `RunDigest.text_glyph` siempre presente copiable; KPI separado `text_glyph_share_rate` ≥4% semana 1, degradar si <1.0 jug/10 shares.
- **§Doctrina rectora global:** **visual-primario, audio-amplificador** (mute=default 85-90% LATAM); juego 100% legible en silencio antes de cualquier audio de estado.
- **★ Primero a falsar por centavos (sin código de producción, n≥15-20 humanos):** test de repetición del grito mudo (#23/#31) + `eyes_closed_test` (#32). Deciden si "audio de orden superior" es real o aspiracional ANTES de gastar en producción de audio.
