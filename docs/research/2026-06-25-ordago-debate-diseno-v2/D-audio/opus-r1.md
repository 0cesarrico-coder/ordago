# CLÚSTER D — Audio como sistema de orden superior · RONDA 1 · ASIENTO OPUS

**Tesis de sistema:** el audio de ÓRDAGO debe diseñarse como **dos sistemas separados con presupuestos de atención distintos**: (A) un **sistema de IDENTIDAD** (firma + grito) que vive en los touchpoints virales y se optimiza por *recuerdo*; (B) un **sistema de ESTADO** (leitmotiv/textura/firmas de resultado) que vive *in-game* y se optimiza por *decodificación*. Los 6 huecos no son 6 features; son la matriz {identidad, estado} × {touchpoint viral, in-game, accesibilidad}. La doctrina rectora: **ninguna señal de juego vive solo en audio** (gate simétrico), y la validación va en **linters/gates en código**, no en prompts.

**Evidencia base (web, 2025-2026):**
- Autoplay: Safari iOS bloquea TODO audio con sonido sin gesto previo; `AudioContext` creado antes del gesto nace `suspended` y exige `resume()` en el handler del gesto. Chrome Android idéntico salvo "media engagement" de visitas previas — que un deep-link de primera sesión NO tiene. 🟢 (MDN/Chrome Devs). Confirma #22: **el primer contacto es mudo por diseño del navegador, no por bug.**
- WhatsApp In-App Browser (IAB): rollout gradual, cobertura plena ~nov-2025; es un WebView que hereda las MISMAS restricciones de autoplay (gesto requerido). 🟡 (Sprinklr/Flowcart). No hay "sticker sonoro" nativo de WhatsApp explotable client-side. Confirma #23: el sticker viaja mudo *de verdad*.
- Sonic logo: 1-3 s es el rango óptimo (recuerdo sin fatiga); +96% brand recall vs visual solo; familia modular = marca 2-3 s + sting 1 s + micro-cues 200-500 ms. 🟢 (MusicGrid/Audira). Valida la firma D3 y me da los números para el sistema de estado.
- Accesibilidad: WCAG 1.3.3 (no depender solo de pistas sensoriales) + Xbox XAG 103 (multi-sensorial) + captions con indicador direccional (TLOU2). 🟢. Es el estándar contra el que se falsea #67.

---

## #22 — La firma muere en el primer contacto

**(a) Steelman.** "First TAP arma la firma" es la ÚNICA arquitectura compatible con la realidad del navegador (no es preferencia: es física de la plataforma, 🟢). Bien hecho convierte una limitación en *juice*: el primer tap del jugador (repartir, voltear carta) ES el gesto que desbloquea el `AudioContext` y dispara la firma 2-3 s — el momento de máxima carga de marca coincide con la primera acción. Ancla D3 (firma=foso) + 09 (el tap ya tiene juice; sumarle la firma es gratis de atención).

**(b) Ataque.** Riesgo real: si la firma suena en CADA tap se vuelve ruido (fatiga, U-invertida #09). Y "first tap" puede caer en un tap *accidental* (scroll, mistap) → firma desperdiciada en mal contexto. Mejora: la firma se arma en el primer tap pero se **dispara en el primer evento SEMÁNTICO** (primera carta jugada), no en cualquier touch.

**(c) Resolución falsable.**
- Invariante en código: linter `first_tap_arms_audio` — falla el build si existe cualquier `.play()`/`AudioContext` sin un ancestro `pointerdown/click` handler. Grep estático + test runtime headless (autoplay forzado a "blocked") que verifica que 0 audio suena antes del primer gesto sintético.
- KPI `firma_heard_first_session` ≥ **70%** de sesiones de demo (umbral kill < 50%). Medir vía evento analítico `firma_fired` con `context=first_semantic_action`.
- Cooldown: la firma completa suena ≤1 vez/sesión; taps subsecuentes usan el sting de 1 s.

**(d) Decisión de César.** Ninguna — esto lo decide la física del navegador. No hay trade-off real.

---

## #23 — El sticker primario viaja MUDO y sin grito imitable

**(a) Steelman.** El grito como **activo DUAL** (sonoro + gemelo visual onomatopéyico tipo Posada estampado GRANDE) es clase mundial porque ataca el canal real: el sticker cruza WhatsApp mudo (🟢, IAB hereda autoplay-block; no hay sticker sonoro nativo). El gemelo visual hace que el grito sea *reproducible sin audio* — el receptor LEE "¡ÓRRRDAGO!" y lo dice. Ancla D3 (grito imitable ≤1.5 s) + el caveat ya verificado (gemelo visual obligatorio).

**(b) Ataque.** Sobre-ingeniería si el glifo compite con el sticker-imagen por espacio visual y lo ensucia (choca con data L1 stickers 56%). El grito tipográfico debe ser PARTE de la composición del sticker, no un sello pegado encima. Riesgo ético 12: ninguno aquí (identidad/pertenencia, no miedo).

**(c) Resolución falsable.**
- Campo `grito_glifo: string` en `RunDigest` (obligatorio, no-null) — linter `digest_has_grito_glifo` falla si vacío.
- Invariante de composición: el glifo ocupa ≥15% y ≤30% del área del sticker (gate de plantilla, verificable por bounding-box en el render).
- KPI de kill (cualitativo→cuantitativo): **test de repetición** — en n≥20 receptores que ven el sticker MUDO, ≥40% repite el grito en voz alta/nota de voz. Si <25%, el glifo no funciona y se rediseña.

**(d) Decisión de César.** Binaria: **¿el grito_glifo va en el caption copiable (texto) además del sticker-imagen, o solo en la imagen?** (texto = copiable/buscable pero menos viral; imagen = más viral pero no copiable). Recomiendo AMBOS pero es presupuesto de César.

---

## #31 — El grito no se versiona por nodo cultural

**(a) Steelman.** Grito como campo LOCALIZABLE en `cultural_packs[]` (grito.mx, grito.caribe, grito.rioplatense…) es clase mundial: la firma melódica es global (no-lingüística → no se traduce), pero el grito ES lenguaje y un grito mono-MX suena *extranjero* en el Caribe → mata la pertenencia (12: el audio es ético *para identidad*; un grito ajeno la rompe). Reutiliza infra que el GDD ya construyó (costo marginal bajo). 🟡 (depende de que la infra exista como se describe).

**(b) Ataque.** Costo de scope en premium SIN live-ops: cada nodo = grabación + glifo + QA de chat de voz. 5 nodos al lanzamiento puede ser caro y diluir calidad. Mejora: **1 grito canónico pulido al 100% + 1-2 variantes** al lanzamiento; el resto post-EA guiado por dónde se comparte de verdad (data, no especulación).

**(c) Resolución falsable.**
- Schema: `cultural_packs[node].grito = {audio, glifo, locale}`; linter `grito_pack_complete` falla si un pack declarado tiene grito null.
- RunDigest selecciona grito por `sharer_node`; fallback explícito a `grito.default` (nunca null).
- KPI: por nodo activo, "test de chat de voz" — ≥40% de repetición POR NODO (mismo umbral que #23). Nodo que no llega no se promueve a default.

**(d) Decisión de César.** Acotada: **¿cuántos nodos de grito al lanzamiento — 1, 2 o 3 — vs diferir el resto a post-EA según data de share?** (1 = calidad máxima/menos pertenencia regional; 3 = más cobertura/riesgo de calidad). Recomiendo **2** (MX + Caribe/Rioplatense según wishlist temprano).

---

## #32 — El audio NO porta el estado del sistema dual

**(a) Steelman.** ESTE es el hueco de mayor valor: hoy el corazón (Trampa↔Fullería) se resuelve 100% visual. Audio decodifica estado MÁS RÁPIDO que texto y *sin leer* → crítico para baja alfabetización (mercado real LATAM). Tres capas: (1) **leitmotiv SOSTENIDO** por Trampa activa (loop, no one-shot — el estado persiste mientras la regla está activa); (2) **textura creciente** atada a Sospecha; (3) **3 firmas** cuela/near-miss/pillado. Earworm de melodía > lenguaje para memoria (🟢 sonic science). Ancla D3 + 09.

**(b) Ataque — el más serio del clúster.** Esto satura la U-invertida de #09 más rápido que nada: un leitmotiv sostenido POR Trampa + textura de Sospecha + firmas de resultado puede volverse una sopa sonora ansiógena. Y la textura de Sospecha es el **punto de riesgo ético 12**: "textura creciente atada a perder" engancha el miedo de pérdida — exactamente lo que 12 prohíbe si se sobre-explota. Mejora: la textura de Sospecha debe tener **TECHO** (no crescendo infinito) y comunicar *riesgo decidible*, no pánico; corta seco al decidir.

**(c) Resolución falsable — test ojos-cerrados como gate de release.**
- **Gate `eyes_closed_test`:** n≥15 jugadores, pantalla apagada/ojos cerrados. Tras una Trampa+resultado, deben identificar (i) QUÉ Trampa está activa y (ii) el resultado (cuela/near-miss/pillado). Umbral release: **≥75%** correctos en ambos; kill < 60%. Falsable, repetible, barato.
- Presupuesto anti-saturación EN CÓDIGO: máximo **1 capa sostenida + 1 transitoria** sonando simultáneamente (mixer con prioridad; linter `audio_layers_active ≤ 2`).
- Techo de Sospecha: la textura mapea a `suspicion ∈ [0,1]` con curva log que satura al 80% del volumen máximo a `suspicion=0.7` (no lineal hasta clipping). Invariante: `suspicion_audio_gain ≤ 0.8 * master`.
- KPI ético: si `quit_rate` durante Sospecha alta > baseline +X% → la textura es predatoria, se suaviza (gate 12).

**(d) Decisión de César.** El trade-off central del clúster: **¿cuánto presupuesto de audio-de-estado antes de saturar la U-invertida #09?** Formulado binario: **¿las 3 capas completas al lanzamiento, o MVP = solo las 3 firmas de resultado (cuela/near-miss/pillado) + leitmotiv de Trampa, difiriendo la textura de Sospecha (la capa más cara Y más riesgosa éticamente) a iteración post-playtest?** Recomiendo MVP: las firmas de resultado son el 80% del valor de alfabetización al 30% del riesgo.

---

## #67 — Tells en audio sin redundancia para sordos

**(a) Steelman.** El gate simétrico §11 ("ninguna señal de juego vive SOLO en audio") es clase mundial y es la *contraparte obligatoria* de #32: en el momento que el audio sube a foso de ESTADO, crea una deuda de accesibilidad para ~5% sordos/HoH. WCAG 1.3.3 + Xbox XAG 103 lo exigen (🟢). Cada evento sonoro de estado emite equivalente visual + subtítulos opt-on de eventos.

**(b) Ataque.** El gate es fácil de declarar y fácil de violar en la práctica (un dev añade un tell sonoro nuevo y olvida el visual). Mejora: el gate NO puede ser una convención — debe ser **estructural en el código**: el audio de estado no se puede emitir sino a través de un emisor que EXIGE un payload visual.

**(c) Resolución falsable — gate de redundancia simétrico.**
- Arquitectura: un único `emitStateCue(visual, audio)` donde `visual` es **no-nullable**; emitir audio por cualquier otra vía es un error de compilación/lint (`no_bare_audio_emit`: grep que prohíbe `.play()` directo fuera del emisor).
- Test `mute_total`: corre toda la suite de eventos de juego con `master=0`; un oracle verifica que cada evento de estado produjo un cambio visual detectable (diff de DOM/canvas). Falla si algún evento es invisible en mute. **Gate de release.**
- Subtítulos de eventos opt-on con indicador direccional cuando aplique (patrón TLOU2).
- KPI: `mute_total` = 100% de eventos con equivalente visual (no hay umbral parcial; es binario).

**(d) Decisión de César.** Ninguna — accesibilidad es no-negociable y barata si es estructural desde el día 1. (Si se difiere, el costo de retrofit es 10x.)

---

## #17 — Emoji-artefacto bandwidth-independent

**(a) Steelman.** Una línea de glifo/texto client-side (estilo Wordle, 0 servidor) es la **red de seguridad** para superficies sin preview / datos agotados — copia-pega que sobrevive donde la imagen no carga. Garantizada, no "fallback olvidado". 🟢 (Wordle probó el patrón a escala).

**(b) Ataque.** Elevarlo a 3er canal canónico choca con data L1 (stickers 56% vs grids 12%) — sería mal asignar atención. Correcto mantenerlo como red de seguridad medida por separado, NO promoverlo.

**(c) Resolución falsable.**
- Invariante: `RunDigest.text_glyph` siempre presente y copiable client-side (linter `digest_has_text_glyph`).
- KPI propio y SEPARADO: `text_glyph_share_rate` medido aparte del sticker (no se mezcla). Si <2% del share total, se mantiene como seguro silencioso (no se invierte más); no se mata (costo ~0).

**(d) Decisión de César.** Binaria menor: **¿el emoji-artefacto #17 merece pipeline/medición propia, o es solo una línea garantizada sin instrumentación?** Recomiendo: una línea garantizada + 1 evento analítico (costo trivial), sin pipeline propio.

---

## VEREDICTO DE SISTEMA

Los 6 fixes **SÍ componen** un sistema coherente IF se organizan por la matriz {identidad, estado} y se respetan **dos límites duros**: (1) el techo de la U-invertida #09 — por eso el linter `audio_layers_active ≤ 2` y el MVP de #32; (2) el gate simétrico #67 estructural (emisor con visual no-nullable) que evita que el ascenso del audio-de-estado cree deuda de accesibilidad. Sin esos dos límites, #32 (3 capas) + #22 (firma) + leitmotivs se pisan en una sopa ansiógena que viola 09 y 12 a la vez. Riesgo de colisión real: #32-textura-Sospecha vs 12 (miedo de pérdida) — mitigado con techo de gain.

**Lo PRIMERO a falsar por centavos:** el **test de repetición del grito** (#23/#31) y el **eyes_closed_test** (#32). Ambos son baratísimos (n≥15-20 humanos, sin código de producción): si el grito mudo no se repite (<25%) el activo dual no sirve, y si el audio de estado no se decodifica con ojos cerrados (<60%) toda la capa #32 es polish disfrazado de foso. Estos dos tests deciden si el "audio como sistema de orden superior" es real o aspiracional — ANTES de gastar en producción de audio.

---

## Lo que sé que las otras IAs probablemente no
- La **física exacta** del bloqueo: `AudioContext` nace `suspended`, `resume()` debe ir EN el handler del gesto, y el IAB de WhatsApp hereda esto (no hay atajo). Esto convierte #22 de "preferencia de diseño" en "invariante de plataforma" → no es debatible, es linter.
- La **matriz {identidad↔estado}** como descomposición: las otras IAs probablemente tratarán los 6 huecos como lista, no como 2 sistemas con presupuestos de atención opuestos (recuerdo vs decodificación).
- El **riesgo ético específico** de la textura de Sospecha (#32 vs 12): el crescendo atado a perder es el único activo predatorio del clúster; necesita techo de gain en código, no buena intención.

## Vacíos — qué necesito de Gemini / Meta AI
- **Meta AI (L1):** ¿la repetición de notas de voz/trending sounds en WhatsApp/IG tiene data de cuánto sube el share? ¿El sticker con texto estampado convierte mejor o peor que el limpio (riesgo de ensuciar #23)? ¿Hay benchmark de % de sesiones LATAM realmente mudas?
- **Gemini (referentes):** casos de sonic branding en juegos hybrid-casual que funcionaron como vector de transmisión (no solo polish); referentes de grito/onomatopeya regionalizada que NO se sintieron forzados; ¿algún juego resolvió estado-via-audio para baja alfabetización con evidencia de que mejoró comprensión?
- **Número que me falta:** % real de superficies sin image-preview en el grafo de share LATAM (decide si #17 es 2% o 15% del tráfico).
