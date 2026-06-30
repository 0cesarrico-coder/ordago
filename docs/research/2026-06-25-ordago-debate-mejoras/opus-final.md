# RONDA 3 — CIERRE · ASIENTO: DIRECTOR DE DISEÑO/SISTEMAS (Opus)

> Tres cruxes, una postura final. Regla de cierre que me autoimpongo: **data L1 > mi razonamiento**, y donde el dato del otro es más fuerte, concedo sin pelear. Donde el dato no existe todavía, marco IRREDUCIBLE y nombro el test que lo zanja — porque la lección de toda la Etapa 2 es que un número en una tabla no es una máquina, y un crux "resuelto por argumento" sin test es exactamente el PowerPoint que vinimos a matar.

---

## CRUX 1 — Formato del objeto-puente: texto vs imagen-sticker vs ambos

**CIERRO hacia: AMBOS, pero con jerarquía invertida respecto a mi R1 — la IMAGEN-sticker es el objeto PRIMARIO que cruza, el TEXTO es el fallback universal, y el deep-link va EMBEBIDO en los dos.**

**El dato decisivo (cedido a Meta-AI, data L1):** stickers personalizados 56% + animados 52% vs predeterminados 12%, y la etnografía del family-group-chat ("about to send one of those to my tías") muestra que lo que cruza es una IMAGEN que se entiende en 0.5s, no un string. En R1 yo defendí el emoji-grid de texto como objeto-A primario por "0 peso / 0 servidor / 1-tap". **Concedo: ese argumento es de ingeniería, no de comportamiento.** El comportamiento de reenvío hispano premia lo visual-personal. Mi argumento de "0 servidor" se preserva igual — un PNG/WebP de <80KB se renderiza **en cliente** con sprites pre-cargados (el ajuste que Gemini ya aceptó en R2): sigue siendo 0 servidor, 0 dependencia de red para generarlo. Perdí el formato, no el principio.

**Por qué NO texto-solo:** el grid de texto se lee como "predeterminado genérico" (la franja del 12%), pierde la tipografía Posada y la cara del Diablo que son el verbo visual de ÓRDAGO. Cruza, pero como commodity Wordle — mi propio Riesgo de R1 ("otro Wordle clone").

**Por qué NO imagen-sola:** la imagen no es copiable-degradable. En un chat con conexión basura o un cliente viejo, el texto plano SIEMPRE llega; la imagen puede fallar al cargar. El texto es el **piso de accesibilidad**, no el techo viral. Por eso: imagen primaria + caption de texto que contiene la línea-verbo-nominal y el link (así, aunque la imagen no cargue, el verbo y el reto sobreviven).

**Lo que NO cedo (🟢):** el **deep-link jugable embebido en ambos**. Meta-AI/Gemini centran el viral en "se entiende en 0.5s" (eso mueve `i`, la invitación). Pero comprensión sin acción es K de un solo salto. El receptor necesita QUÉ hacer → juega la mano → genera SU sticker → reenvía. Eso compone K. La imagen gana el `i`; el deep-link gana la segunda `i`. Son capas distintas del mismo K = i × c (C2 🟡), no rivales.

**Cambio al GDD:** §8.3 — objeto-puente = **sticker-imagen <80KB renderizado en cliente** (verbo nominal + score + cara del Diablo, tipografía Posada) **con caption de texto** (misma línea + `ordago.gg/d/<seedhash>`). El "código de build" alfanumérico → opt-in del ~5% en el Codex (A4 🟢).

**Kill/test (el de Meta-AI, lo suscribo y lo afilo con mi corrección de R2):** A/B en 20 grupos familiares MX — sticker-imagen vs texto-plano, mismo mensaje. Métrica DOBLE (mi corrección de R2): (1) reenvío sin explicación en 24h ≥30%, Y (2) comprensión <2s ≥70%. **Kill del formato si el ganador no supera ambos umbrales.** Confianza en el veredicto: **🟡** — es data L1 de plataforma (fuerte) pero el A/B propio aún no se corrió; el dato de stickers es direccional, no específico de ESTE artefacto.

---

## CRUX 2 — Soporte del clip: co-primario móvil vs exclusivo PC vs diferir

**CIERRO hacia: el clip es PRE-RENDERIZADO en servidor (no codificado en el navegador móvil), entregado como MP4/WebP <500KB; co-primario en alcance, generado fuera del cliente móvil.** Esto disuelve el crux en vez de elegir un lado — porque el crux estaba mal planteado.

**El dato decisivo (cedo a Gemini, restricción de hardware = data L1 dura):** el hardware móvil medio-bajo LATAM (MediaTek/Snapdragon antiguos) NO codifica MP4 a 60fps en navegador sin destruir la fricción-cero (B5 🟢). Eso es físico, no opinable. **Gemini tiene razón en que el cliente móvil no debe CODIFICAR el clip.**

**Pero Meta-AI también tiene razón (data L1):** los Reels tienen 2-12x alcance y en LATAM el clip con audio ES el chiste — degradarlo a "feature exclusiva de PC" tira a la basura el motor de alcance broadcast justo en el segmento que más comparte video. Mandar el clip solo a PC es resolver un problema de codificación amputando el canal.

**La síntesis de sistemas (mi aporte): separar GENERAR de CODIFICAR.** El clip no tiene que renderizarse en el dispositivo. La run produce un `RunDigest` serializado (la fuente de verdad única que defendí en R1); ese digest se manda a un **render-worker en servidor** (o función serverless barata) que devuelve el MP4 <500KB con la firma sonora. Costo de servidor real pero acotado (solo runs que el jugador ELIGE compartir, no todas) — y aquí el clip vive correctamente en el **loop de ADQUISICIÓN** (CAC>0, Palanca 3), no en el loop social CAC~0. Cuadra con la economía: el clip cuesta servidor, su producto es alcance/wishlists, su costo entra en el CAC. El sticker-imagen (CRUX 1) se queda 0-servidor en cliente porque vive en el loop social.

**Por qué esto es clase mundial y no las tres opciones del crux:** "co-primario en móvil" (Meta) chocaba con el hardware; "exclusivo PC" (Gemini) chocaba con el alcance; "diferir" (mi R1) era cobardía de diseño. El render server-side satisface las tres restricciones — móvil recibe y reenvía el clip (no lo genera), el hardware no sufre, el alcance se preserva, y el costo se contabiliza honestamente donde toca.

**Cambio al GDD:** §8.3 — clip = **render server-side desde `RunDigest`** (no codificación en cliente), <500KB, 9:16, **audio activado por defecto** (la firma sonora — campana grave + jarana + "¡tramposo!" — es el foso barato, D3 🟡). Construir en vertical slice (no prototipo): el sticker-imagen valida el grafo primero; el clip multiplica alcance después.

**Kill/test:** el de Meta-AI — CTR a demo desde clip-con-audio vs clip-mudo en cohorte hispana-USA; **kill del audio-por-defecto si la diferencia <20%** (si el audio no mueve CTR, es peso muerto). Y un gate de costo: si el render server-side por share supera ~$0.02, re-evaluar (rompería el CAC de Palanca 3). Confianza: **🟡** en el alcance del clip (data L1 de Reels es fuerte), **⚪** en que el server-side render se mantenga bajo el techo de costo (validar en vertical slice).

---

## CRUX 3 — Banda de spread de EV: ≤15% vs 15-25%

**CIERRO hacia: banda DUAL operativa — regenerar si la dominancia >25% EV (liveness), y contar un tablero como "duda real" solo si existen ≥2 jugadas con spread ≤15% a 2-3 turnos (foso). Objetivo de salud: que la MAYORÍA de tableros entregados caigan en 8-15%.** No es 15-25 ni ≤15 a secas; es un piso y un techo con funciones distintas.

**Esto es lo más cercano a IRREDUCIBLE-por-ahora de los tres, y soy honesto: el número exacto es ⚪.** Pero la ESTRUCTURA del desacuerdo sí se puede cerrar con argumento, y la magnitud con un test concreto. Desgloso:

**Concedo a Gemini un punto real (no es solo razonamiento suyo, apela a la psicología del género):** por debajo de ~8-10% el juego se siente "ajedrez seco" — la suerte percibida (la dopamina de "casi la salvo") se evapora y ÓRDAGO deja de sentirse baraja y empieza a sentirse solver. Eso es un riesgo genuino que mi "≤15%" de R1 no acotaba por abajo. **Acepto un PISO ~8%.** No bajamos de ahí a propósito.

**No cedo el TECHO (🟡, contra el 25% de Gemini):** un spread del 25% NO es una decisión, es una trampa de novato. A1 🟢 exige que el jugador DUDE; nadie con 2 runs duda entre A y B cuando B rinde 25% menos — la toma mal una vez, aprende, y la decisión muere. El propio Gemini quiere vigilar el colapso de entropía con $H_{builds}$ — pero un techo de generación del 25% **siembra** la dominancia que su alarma luego declarará emergencia. Liveness y salud-del-meta no pueden calibrarse a bandas que se contradicen. El 25% es liveness sin foso.

**Por qué la banda dual y no un punto único:** el error de todo el debate (incluido mi R1) fue tratar esto como UN umbral. Son DOS funciones: (1) el **techo de regeneración** (>25% domina → re-siembra) protege que SIEMPRE haya dos caminos viables — es liveness, lo de Gemini, y 25% está bien AHÍ. (2) El **criterio de calidad** (¿este tablero produce duda real?) solo lo cumplen los ≤15%. Un tablero entre 15-25% es legal (no se regenera) pero NO cuenta para la métrica de "foso vivo". Así Gemini gana el piso y la liveness; yo gano que la SALUD se mida en la banda estricta. Ambos teníamos media razón.

**El dato decisivo que lo zanja (ya está en mi crux de R2, lo confirmo):** el **solver de papel sobre 100 tableros cruzado con el test del experto.** Dar al novato y al experto el mismo seed/build en tableros que pasan cada banda. Si en los tableros de 20-25% los scores **convergen** (<15% de brecha novato↔experto) → esa banda NO produce techo de maestría → no es foso → gana el ≤15%. Si incluso ≤15% converge → el verbo no tiene profundidad y caemos al CRUX-cimiento (el de "¿es puzzle?", ya consensuado como el que se resuelve primero). **Eso es lo que convierte el número de opinión en medición.**

**Cambio al GDD:** §7.3 — el generador del Diablo opera con **postcondición dual verificada por solver**: rechaza+re-siembra (≤8 intentos, sobre ejes tempo/escala/defensa) si alguna jugada domina por >25% EV; **mide salud del foso solo sobre tableros con ≥2 jugadas en banda 8-15% EV a 2-3 turnos.** Foso vivo: entropía de Shannon de builds ganadores por cohorte semanal (alarma si cae sostenido D7→D14→D30) + test del experto vía Diablo Fantasma. Respuesta a dominancia = **matar con trade-off, no nerf de número** (A1 🟢).

**Estado: IRREDUCIBLE en el número exacto hasta correr el solver** (🟡 en la estructura dual / ⚪ en piso y techo precisos). Pero esto es lo BUENO del crux: no se lleva a síntesis como opinión, se lleva como **el test más barato y de mayor apalancamiento del proyecto** — baraja + hoja de cálculo, un fin de semana, antes de un píxel.

---

## POSICIÓN DEFINITIVA

### Palanca 1 — Artefacto-puente (fusión de los tres)
**Sistema dual desde un único `RunDigest` serializado:** (A) **sticker-imagen <80KB renderizado en cliente** (verbo nominal "le robé el alma a @primo por +X%" + score + cara del Diablo en tipografía Posada) con **caption de texto** que lleva la misma línea + deep-link jugable; (B) **clip 6-8s <500KB con audio por defecto, renderizado server-side** desde el mismo digest. Anti-fatiga: **generador procedural de variantes** (≈12 clips / 20 plantillas) como invariante, no como pulido — el K se mantiene por una máquina, igual que el foso. Confianza: 🟡 (data L1 de formato es fuerte; el A/B propio falta).

### Palanca 2 — Generador de bifurcación + foso vivo (mi liderazgo)
**El generador como INVARIANTE verificado por solver ANTES de un píxel:** postcondición dual — re-siembra si dominancia >25% EV (liveness), salud del foso medida solo en tableros con ≥2 jugadas a 8-15% EV a 2-3 turnos (calidad). Re-siembra acotada sobre ejes (tempo/escala/defensa). Foso vivo instrumentado: entropía de builds ganadores + test del experto vía Diablo Fantasma (proxy gratis de brecha-skill). Confianza: 🟢 en que debe ser invariante-no-esperanza; ⚪ en los números exactos hasta el solver.

### Palanca 3 — Plataforma ↔ viralidad ↔ economía
**Separar quirúrgicamente loop de ADQUISICIÓN (CAC>0: clip→wishlist→compra; aquí vive el costo del render server-side) del loop SOCIAL intra-juego (CAC~0 real, producto = retención, no instalaciones).** Borrar "CAC~0" del lenguaje de adquisición (corrección editorial gratis). Modelo B2P de 3 columnas con gate duro **LTV/CAC ≥ 3 por columna** antes del vertical slice; **precio regional LATAM ~$7.49 (149 MXN), no $15** (concedido a Gemini — Balatro $7.50, Inscryption $9: $15 en LATAM es suicidio comercial, data L1). Leaderboards en **backend propio** (desacopla el foso social de Steam, L7 🟢). Confianza: 🟡 (cifras de industria; validar en cohorte propia).

### C-1 — Voto final
**HÍBRIDO. Convergencia total de los cuatro asientos.** Steam = producto premium ($14.99 base, regional LATAM, protege linaje Balatro/sin-MTX). **La demo web NO es marketing: es la primera mitad física del artefacto-puente** — "La Mesa del Diablo de hoy", 1 mano/1 Manga contra el Diablo de la semilla, jugable en navegador móvil <3s desde el deep-link, cerrando el loop que el GDD prometía y nunca entregó. Rechazo web-native-full-first (mata premium, invita piratería, desliza a F2P/MTX → choca con M1/LD7 🟢).
**Trade-off que ACEPTO:** +scope real (demo web delgada + render-worker server-side del clip + backend propio de leaderboards) y un costo de servidor distinto de cero por cada clip/leaderboard. Lo acepto porque sin ese puente jugable la economía B2P de bajo precio NO cierra LTV/CAC≥3: el motor viral no es nice-to-have, es el único camino al ratio. La demo regala el VERBO; cobra el FOSO.

### El cambio de MAYOR apalancamiento al GDD v1.2
**Construir el solver de papel del generador de bifurcación (banda dual: re-siembra >25%, foso medido en 8-15%) y correrlo sobre 100 tableros cruzado con el test del experto ANTES de un solo píxel de arte** — porque valida o MATA el foso entero (y con él toda la economía y la viralidad, que descansan en que el verbo sea decisión y no puzzle) por el costo de un fin de semana con baraja y hoja de cálculo. Es la entrega; todo lo demás es PowerPoint hasta que el solver hable.
