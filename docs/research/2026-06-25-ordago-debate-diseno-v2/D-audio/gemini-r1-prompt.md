# CLÚSTER D — "Audio como sistema de orden superior" · RONDA 1 · Asiento GEMINI

## Tu rol
Eres **Estratega de Valor**: tu lente es *¿el audio MUEVE retención y marca, o es decoración cara?* Una de 3 IAs que investigan el mismo clúster; las otras son Opus (diseñador de sistemas/accesibilidad) y Meta AI (data L1 de plataforma). **Lidera con lo que SOLO tú aportas:** datos del ecosistema Google/YouTube (Search Trends de "sonido de [juego]", trending sounds en Shorts, watchability de audio en clips), análisis de referentes cuya **firma sonora VIAJA** y razonamiento estratégico profundo sobre el ROI del audio como foso perdurable.

## El juego (no tienes el GDD — esto es lo que necesitas)
**ÓRDAGO** es un roguelike deckbuilder con baraja española; fantasía: *"le haces trampa al Diablo"*. Foso = un **sistema dual** Trampa↔Fullería: el Diablo impone reglas-trampa ("suma 13", "Oros no cuentan"); tú juegas **Fullerías** que rompen la regla, con un **arco de Sospecha de 3 tiempos** (sube riesgo → el Diablo duda → cuela / near-miss / te pilla). Modelo: **premium B2P en Steam ($14.99), sin MTX, sin live-ops/temporadas**, + demo web jugable como mitad física del artefacto-puente. Mercado: LATAM + USA + hispanos-USA (sweet spot). Adquisición canónica: deep-link → demo web móvil → wishlist Steam. Objeto-puente PRIMARIO = un **sticker-imagen** que cruza WhatsApp.

**La carta D3 (lo que ya está comprometido):** el audio es FOSO, no polish — (1) una **firma sonora** de 2-3 notas ≤3 s (sonic branding tipo Intel, earworm de Jakubowski 2017, Zeigarnik) + (2) un **grito imitable** ≤1.5 s reproducible con la boca (el "¡LOTERÍA!" es el caso de estudio LATAM). El audio es "el foso más barato y perdurable" (se produce una vez, rinde para siempre) Y un motor de transmisión sin costo (se canta, entra como nota de voz, se vuelve trending sound). Caveat: autoplay bloqueado en móvil; mucha sesión LATAM es muda → el grito necesita gemelo visual. Cita confianza 🟢/🟡/⚪.

## Los 6 huecos del clúster D (resumen autocontenido — §GDD / por qué NO es clase mundial / fix propuesto)
1. **#22 — Firma muere en 1er contacto (§10.1+§15).** El deep-link→demo web móvil es MUDO en el momento de máxima carga de marca (autoplay bloqueado). *Fix:* el **primer TAP dispara la firma**; KPI `firma_heard_first_session`.
2. **#23 — El sticker PRIMARIO viaja MUDO (§8.3+§10.1).** El objeto que más cruza el grafo no porta el grito ni su gemelo visual. *Fix:* **gemelo visual onomatopéyico** estampado en el sticker (copiable en caption); campo `grito_glifo`. Kill: ¿el receptor REPITE el grito tras ver el sticker mudo?
3. **#31/#21/#34 — Grito mono-MX (§10.1+§11/§8).** Firma global, pero el grito (lingüístico) no se versiona por nodo cultural ni usa la infra `cultural_packs[]`. *Fix:* grito LOCALIZABLE (grito.mx, grito.caribe…); "test de chat de voz" POR NODO.
4. **#32/#13/#33 — El audio no porta ESTADO, es branding (§7.6e+§10).** El sistema dual se resuelve 100% visual; falta canal sonoro de estado (audio decodifica más rápido que texto). *Fix:* leitmotiv de Trampa sostenido + textura de Sospecha + 3 firmas de resultado. Kill: identificar Trampa+resultado con ojos cerrados.
5. **#67 — Tells de audio sin redundancia para sordos (§10.1+§7.6b).** ~5% sordos pierden el tell. *Fix:* gate 'ninguna señal vive solo-audio' + equivalente visual + QA mute total.
6. **#17 — Emoji-artefacto bandwidth-independent relegado (§8.3).** El artefacto Unicode/emoji copiable (estilo Wordle, 0 servidor) es red de seguridad para superficies sin preview / datos agotados. *Fix:* una línea de glifo client-side garantizada + medir su `share_rate` aparte.

## PREGUNTA CENTRAL
¿Cómo entregar el **foso de audio (D3) en TODOS los touchpoints y con redundancia accesible** — primer TAP arma la firma (#22); grito DUAL con gemelo visual en el sticker mudo (#23); grito localizable por nodo (#31); audio que PORTA el estado dual (#32); tells con redundancia para sordos (#67); emoji-artefacto (#17)? Tu ángulo: **¿cuáles de estos fixes mueven de verdad la aguja de retención/marca/transmisión, y cuáles son audio-teatro caro?**

## Lo que tú DEBES producir (para cada uno de los 6 huecos, y como sistema)
Para CADA hueco, en este orden:
- **(a) Steelman** — la versión más fuerte: ¿qué evidencia de VALOR (Search Velocity, trending-sound reach, completion-rate de clips con audio, retención atribuible a marca sonora) respalda que este fix es clase mundial? Cita referentes concretos.
- **(b) Ataque / mejora** — ¿dónde el fix es valor marginal o ilusorio? (p.ej. localizar el grito por nodo: ¿el lift de transmisión justifica el costo de N grabaciones?; el emoji #17: ¿es nicho?). Mejora con datos.
- **(c) Resolución de clase mundial con CRITERIOS FALSABLES** — KPIs de VALOR medibles con umbrales (p.ej. % de shares con audio, correlación búsqueda-de-sonido↔clicks entrantes, lift de wishlist/retención de la variante con-firma vs sin-firma, hold-rate de clip con vs sin grito). Números, no adjetivos.
- **(d) Decisión de César** — el trade-off de valor que él decide (p.ej. ¿cuánto presupuesto a localización de grito al lanzamiento vs post-EA?; ¿el emoji-artefacto #17 merece inversión o se mide y se mata?).

## Referentes que DEBES traer (lidera con esto)
- Juegos cuya **firma sonora VIAJA fuera del juego** (Balatro: el audio/feel del scoring y su rol en clips de Shorts/Twitch; Tetris/Korobeiniki; Intel; Among Us; Geometry Dash; Friday Night Funkin'). ¿Qué hizo que el sonido se volviera trending sound y eso convirtiera en wishlist/venta?
- **Balatro audio específicamente:** cómo el feedback sonoro del scoring (el crescendo de mults) es parte de la watchability/clipeabilidad y del foso de "una mano más". ¿Hay data de Search Velocity / clips con su audio?
- Casos de **localización de audio** que escalaron transmisión por mercado (o que NO valió la pena).

## Requisito de especificidad
Cada hallazgo lleva dato concreto (número/rango/ejemplo) + fuente (YouTube Ads / Search Trends / training data del ecosistema Google) + confianza Alta/Media/Baja. "El audio ayuda" NO es aceptable. Usa tu razonamiento extendido al máximo. NO inventes contenido del GDD más allá del resumen.

## Formato
Markdown. Por hueco: (a)(b)(c)(d). Cierra con **Lo que sé que las otras IAs probablemente no** (insights Google/YouTube/Search) y **Vacíos** (qué necesitas de Opus/Meta AI). ≤900 palabras de cuerpo analítico.
