# CLÚSTER D — "Audio como sistema de orden superior" · RONDA 1 · Asiento META AI

## Tu rol
Eres analista con **datos L1 reales de las plataformas de Meta** (Instagram, WhatsApp, Facebook, Messenger, Meta Ads) **+ Red Team**. Una de 3 IAs que investigan el mismo clúster; las otras son Opus (diseñador de sistemas/accesibilidad) y Gemini (estratega de valor / referentes). **Lidera con lo que SOLO tú tienes:** comportamiento real de **autoplay e in-app browsers**, **audio en WhatsApp/IG** (sesiones mudas LATAM, notas de voz, stickers sonoros), tasas de reenvío de stickers, y un ataque adversarial honesto a los supuestos del clúster.

## El juego (no tienes el GDD — esto es lo que necesitas)
**ÓRDAGO** es un roguelike deckbuilder con baraja española; fantasía: *"le haces trampa al Diablo"*. Foso = un **sistema dual** Trampa↔Fullería (el Diablo impone reglas-trampa; tú las rompes con Fullerías en un arco de Sospecha de 3 tiempos). Modelo: **premium B2P en Steam ($14.99), sin MTX**, + demo web jugable como mitad física del artefacto-puente. Mercado: LATAM + USA + hispanos-USA (sweet spot). Adquisición canónica: **deep-link → demo web móvil → wishlist Steam**, normalmente abierto **dentro del in-app browser de WhatsApp/Instagram**. Objeto-puente PRIMARIO = un **sticker-imagen** que cruza WhatsApp (data L1 previa: stickers personalizados 56% / animados 52% / predeterminados 12%; WhatsApp ≈ 12.4% del consumo de info en MX).

**La carta D3 (lo que ya está comprometido):** el audio es FOSO — una **firma sonora** de 2-3 notas ≤3 s + un **grito imitable** ≤1.5 s reproducible con la boca (vector de transmisión: se canta, entra como nota de voz, se vuelve trending sound). Caveat ya de TU lente en una ronda previa: Chrome/Safari móvil BLOQUEAN autoplay; **mucha sesión LATAM es SILENCIOSA** (transporte/trabajo) → el grito necesita **GEMELO VISUAL** (sticker + frase/onomatopeya copiable), y el "grito" a menudo no es musical sino FRASE ("¡No manches!", "¡Échale!") que se vuelve sticker. Cita confianza Alta/Media/Baja.

## Los 6 huecos del clúster D (resumen autocontenido — §GDD / por qué NO es clase mundial / fix propuesto)
1. **#22 — Firma muere en 1er contacto (§10.1+§15/§8.3).** El deep-link→demo web móvil es MUDO en máxima carga de marca (autoplay bloqueado en el in-app browser). *Fix:* el **primer TAP dispara la firma**; KPI `firma_heard_first_session`.
2. **#23 — El sticker PRIMARIO viaja MUDO y sin grito imitable (§8.3+§10.1).** El objeto que más cruza el grafo no porta el grito ni su gemelo visual. *Fix:* **gemelo visual onomatopéyico** estampado GRANDE en el sticker, copiable en caption; campo `grito_glifo`. Kill: ¿el receptor REPITE el grito tras ver el sticker mudo?
3. **#31/#21/#34 — Grito mono-MX (§10.1+§11/§8).** El grito (lingüístico) no se versiona por nodo cultural. *Fix:* grito LOCALIZABLE por nodo (grito.mx, grito.caribe, centroamericano-US…); "test de chat de voz" POR NODO.
4. **#32/#13/#33 — El audio no porta ESTADO, es branding (§7.6e+§10).** Falta canal sonoro de estado (audio decodifica más rápido que texto para baja alfabetización). *Fix:* leitmotiv de Trampa sostenido + textura de Sospecha + 3 firmas de resultado. Kill: identificar Trampa+resultado con ojos cerrados.
5. **#67 — Tells de audio sin redundancia para sordos (§10.1+§7.6b).** ~5% sordos pierden el tell. *Fix:* 'ninguna señal vive solo-audio' + equivalente visual + QA mute total.
6. **#17 — Emoji-artefacto bandwidth-independent relegado (§8.3).** El artefacto Unicode/emoji copiable (estilo Wordle, 0 servidor) es red de seguridad para superficies sin preview / datos agotados. *Fix:* una línea de glifo client-side garantizada + medir su `share_rate` aparte.

## PREGUNTA CENTRAL
¿Cómo entregar el **foso de audio (D3) en TODOS los touchpoints y con redundancia accesible** — primer TAP arma la firma (#22); grito DUAL con gemelo visual en el sticker mudo (#23); grito localizable por nodo (#31); audio que PORTA el estado dual (#32); tells con redundancia para sordos (#67); emoji-artefacto (#17)?

## Lo que tú DEBES producir (para cada uno de los 6 huecos, y como sistema)
Para CADA hueco, en este orden:
- **(a) Steelman** — la versión más fuerte respaldada por TU data de plataforma: ¿qué comportamiento real (sesiones mudas, reenvío de stickers, notas de voz, frases-sticker) hace que este fix sea clase mundial en WhatsApp/IG LATAM?
- **(b) Ataque / Red Team** — el modo de fallo REAL que tu data expone (autoplay también bloqueado tras el 1er tap en algunos in-app browsers; stickers de WhatsApp NO reproducen audio; el grito localizado puede leerse como cliché/forzado en un nodo; el gemelo visual choca con el límite de texto del sticker; fatiga de sticker en 2-3 semanas). Sé adversarial.
- **(c) Resolución de clase mundial con CRITERIOS FALSABLES** — la spec que sobrevive a tu Red Team, con KPIs de plataforma y umbrales (% de receptores que repite el grito tras ver el sticker mudo; `share_with_audio` vs share mudo; tasa de reenvío del sticker con grito_glifo vs sin; tasa de bloqueo/reporte como techo ético). Números reales, no adjetivos.
- **(d) Decisión de César** — el trade-off que él decide a partir de TUS datos (p.ej. cuántos nodos de grito al lanzamiento dado el costo/beneficio de transmisión por nodo; si el grito debe ser FRASE-sticker en vez de vocalización musical; si el emoji #17 merece existir dado stickers 56% vs grids 12%).

## Lo que SOLO tú puedes responder (prioriza esto)
- **Autoplay / in-app browser:** ¿el audio realmente se desbloquea con el 1er tap dentro del navegador embebido de WhatsApp/IG en Android/iOS? ¿Hay restricciones extra (modo de ahorro de datos, políticas del WebView) que matarían `first_tap_arms_audio`?
- **Audio en WhatsApp/IG:** % real de sesiones SILENCIADAS en LATAM, peso de las NOTAS DE VOZ vs texto, si los **stickers sonoros** existen/se reenvían en WhatsApp, y cómo viaja una FRASE-sticker vs una onomatopeya.
- **Stickers sonoros + Red Team:** comportamiento de reenvío, fatiga, y qué frases/gritos se vuelven trending en el grafo familiar LATAM vs cuáles caen.

## Requisito de especificidad
Cada hallazgo lleva dato concreto (número/rango/ejemplo) + fuente ("datos de WhatsApp Business", "comportamiento de Instagram", "Meta Ads") + confianza Alta/Media/Baja. "El audio es importante" NO sirve. Si no tienes el dato exacto, dilo y da tu confianza. NO inventes contenido del GDD más allá del resumen.

## Formato
Markdown. Por hueco: (a)(b)(c)(d). Cierra con **Lo que yo sé y las otras IAs probablemente no** y **Vacíos** (qué necesitas de Opus/Gemini). ≤900 palabras de cuerpo analítico.
