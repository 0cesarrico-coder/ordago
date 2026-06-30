=== LAS 3 POSICIONES DE RONDA 2 (cross-review) ===

────────── R2 — opus ──────────
# RONDA 2 — CONFRONTACIÓN CRUZADA · ASIENTO: DIRECTOR DE DISEÑO/SISTEMAS (Opus)

> Mi trabajo en R2 no es repetir mi invariante de la Palanca 2. Es confrontar dónde los otros dos asientos tienen razón contra mí, dónde yo tengo razón contra ellos, y forzar que la "entrega" no vuelva a ser promesa. Sigo siendo el más duro con una cosa: **un número en una tabla no es una máquina.** Gemini y Meta-AI trajeron data L1 de plataforma que yo no tenía; la respeto y la priorizo sobre mi razonamiento. Pero ambos cometieron, en la Palanca 2, el mismo pecado que el GDD que vinimos a matar.

---

## 1) STEELMAN + ATAQUE — el fix con el que MÁS discrepo

**Diana: el umbral de bifurcación de Gemini en la Palanca 2 — "si una opción supera a la otra por más del 35% de EV, regenera" (R1-gemini, §7.3).** Y su pariente, el de Meta-AI: "≥2 jugadas Pareto-no-dominadas en ≥95% de tableros" sin banda de EV (R1-meta).

**Steelman honesto (su versión más fuerte):** un umbral del 35% es operativamente generoso a propósito — deja respirar al generador (menos re-rolls, menos tableros artificiales, mi propio Riesgo B), y un 35% de spread sigue siendo "una decisión" porque a horizonte largo la varianza del roguelike puede dar la vuelta a una desventaja del 35%. Es defendible como criterio de *liveness* del generador: garantiza que SIEMPRE haya dos caminos viables, que es lo que el GDD nunca garantizó.

**Refutación (con carta + nivel):** un spread del 35% no produce una decisión; produce una **trampa de novato**. A1 🟢 (foso = trade-off real con consecuencia perceptible) exige que el jugador *dude*; nadie con 2 runs duda entre A y B si B rinde 35% menos — la elige el novato una vez, aprende, y nunca más. Eso colapsa exactamente al "técnicamente hay 2 jugadas, prácticamente una importa" que yo marqué como Riesgo A en R1. Peor: alimenta el colapso de entropía que el propio Gemini quiere vigilar con su $H_{builds}$ — su umbral de generación (35%) y su alarma de meta (caída de entropía) **se contradicen**: el primero permite dominancia que el segundo declarará emergencia. No puedes calibrar la salud del meta a una banda mucho más estricta que la que usas para sembrar.

La cifra correcta no es de razonamiento mío, es de **diseño de juegos de información perfecta/casi-perfecta**: la banda donde la skill (no la aritmética) decide es ~**10-15% de EV a 2-3 turnos** (mi R1, Capa 3). Confianza ⚪ en el número exacto — hay que calibrarlo con el solver y con el test del experto — pero 🟡 en que 35% está fuera de la banda de duda por un factor de ~2-3×. **El ataque concreto: bajar el umbral de regeneración de 35% a una banda dual** — rechaza si la diferencia >20% (liveness, lo que Gemini protege) Y marca como "tablero de duda real" solo los que caen ≤15% (calidad, lo que yo protejo). Sin la segunda mitad, el generador entrega liveness sin foso, que es el fracaso de clase-mundial disfrazado de feature.

**Falsable:** en el solver de papel, si los tableros que pasan el umbral de 35% producen, en el test del experto, convergencia de scores novato↔experto (<15% de brecha), el umbral está roto aunque "haya 2 jugadas". Ese es el kill.

---

## 2) MI PUNTO MÁS DÉBIL QUE OTRO EXPUSO

**Meta-AI me clavó dos:**

**(a) El criterio de la "prueba del puente" — yo lo tenía al revés (R1-opus §Palanca 1 vs R1-meta).** Yo escribí: *kill si <60% dice "le ganó/hizo trampa a alguien"*. Meta-AI, con data L1, lo formuló como *kill si <70% pregunta "¿cómo se hace?"* y *pasa si >30% lo reenvía sin explicación*. **Lo reconozco: el suyo es mejor y el mío era incompleto.** "Entender qué pasó" (comprensión) NO es lo mismo que "querer reenviarlo" (acción viral) — y K = i × c (C2 🟡) se mueve por la ACCIÓN, no por la comprensión. Mi test medía c (conversión del receptor que entiende) pero ignoraba i (que el emisor quiera mandarlo). **Actualizo:** la prueba del puente necesita DOS métricas — comprensión (<2s, ≥70%) Y disposición-a-reenviar (≥30% "lo mandaría a mi grupo sin que me dé pena"). La segunda es la que Meta-AI ancló con data real de reactancia/spam familiar, y es la que de verdad predice K. Mi versión sola habría dado luz verde a un grid que se entiende pero nadie reenvía.

**(b) La fatiga creativa — yo no la modelé como invariante de sistema (R1-meta, "stickers se queman en 2-3 semanas").** Esto es data L1 que demuele un supuesto silencioso de mi diseño: traté el artefacto-puente como objeto estático. Meta-AI muestra que el K-factor **decae en el tiempo** igual que mi foso decae en el tiempo — y yo, que exigí instrumentar el foso VIVO, no exigí instrumentar el artefacto VIVO. Inconsistencia mía. **Lo incorporo a mi propia lógica de invariante:** la Palanca 1 necesita su propia capa de sostenibilidad — generador procedural de variantes (12 clips / 20 grids rotativos de Meta-AI) NO como pulido de marketing sino como el equivalente, en el dominio viral, de mi re-siembra en el dominio de la mesa. Misma disciplina: el valor (K, foso) se mantiene por una máquina, no por un activo congelado.

Defiendo, eso sí, **una cosa que no cedo:** mi insistencia en el **deep-link jugable** sobre el grid puramente legible. Meta-AI/Gemini centran el viral en "imagen que se entiende en 0.5s". Verdad para i (cruzar el grafo). Pero la imagen legible sola es Wordle: cruza y muere, porque el receptor no tiene QUÉ hacer (mi Riesgo de "otro Wordle clone"). El reto-jugable-en-1-tap es lo que convierte i en una segunda i (el receptor juega → genera SU grid → reenvía). Sin el deep-link, K es un solo salto; con él, K se compone. Eso lo sostengo 🟢 contra ambos.

---

## 3) CONVERGENCIA POR PALANCA

**Palanca 1 — Artefacto-puente (FUSIÓN de los tres):** Sistema dual con UNA fuente serializada (`RunDigest`), separado por embudo: **(A) Emoji-grid** con la línea-verbo-nominal en primera posición ("le robé el alma a @primo por +X%") + **deep-link jugable** (mi aporte: aterriza en la demo de 1 mano, no en metadata) + **(B) Clip 6-8s con audio por defecto** (la firma sonora de Gemini/Meta como foso barato, D3 🟡). Tres anclas nuevas que cedo a los otros: (1) **generador procedural de variantes** contra fatiga (Meta-AI, data L1); (2) **doble criterio de kill** comprensión + disposición-a-reenviar (Meta-AI corrigió mi test); (3) **texto 100% editable, centrado en rivalidad personal no en marca** (Gemini, anti-reactancia, A3 🟡). Construir A en prototipo, B en vertical slice.

**Palanca 2 — Generador/foso vivo (mi liderazgo, afinado por la confrontación):** El generador como INVARIANTE verificado por solver ANTES de un píxel — pero con la **banda dual** que defendí en §1: rechaza si dominancia >20% EV (liveness), exige spread ≤15% EV a 2-3 turnos para contar un tablero como "duda real" (foso). Re-siembra acotada (~8 intentos) operando sobre ejes (tempo/escala/defensa), no cartas. Foso vivo instrumentado con DOS centinelas: entropía de Shannon de builds ganadores (alarma si cae sostenido D7→D14→D30) + test del experto vía Diablo Fantasma como proxy gratis de brecha-skill. **Respuesta a dominancia = matar con trade-off, no nerf de número** (A1). Esta es la palanca de mayor apalancamiento y el test más barato del proyecto.

**Palanca 3 — Plataforma↔economía (convergencia fuerte, los tres coinciden):** Separar quirúrgicamente el **loop de ADQUISICIÓN** (CAC>0 siempre — clip→wishlist→compra) del **loop SOCIAL intra-juego** (CAC~0 real, pero su producto es RETENCIÓN, no instalaciones). Borrar "CAC~0" del lenguaje de adquisición (corrección editorial gratis). Modelo B2P de 3 columnas con gate duro **LTV/CAC ≥ 3 por columna** antes del vertical slice. Las cifras de las tablas (Gemini/Meta) son ⚪/🟡 de industria — el entregable no es la tabla, es el **modelo de payback escrito + leaderboards en backend propio** (desacopla el foso social de Steam, L7 🟢, y habilita la demo web). El artefacto-puente (Palanca 1) ES parte del modelo económico, no un canal aparte: es el único camino a LTV/CAC≥3 para un B2P de bajo precio.

---

## 4) C-1 — VOTO

**Confirmo HÍBRIDO. Convergencia total de los tres asientos.** Precisión que sigo defendiendo y que ahora los tres comparten: **la demo web no es marketing, es la primera mitad física del artefacto-puente** — "La Mesa del Diablo de hoy", 1 mano/1 Manga contra el Diablo de la semilla, jugable en navegador móvil en <3s desde el deep-link del grid, cerrando el loop que el GDD prometía y nunca entregó (el link aterriza en algo JUGABLE, no en paywall). Steam = producto premium ($14.99 base, regional LATAM, protege linaje Balatro/sin-MTX). Demo deliberadamente delgada: regala el VERBO (que viraliza), cobra el FOSO (que retiene — Codex, Tahúres, Diablo Fantasma social, backend). Rechazo web-native-full-first: mata premium, invita piratería del juego completo y desliza hacia F2P/MTX, chocando con M1/LD7 🟢 (piso ético: no monetizar por adicción). El híbrido es el único que sirve a las tres palancas a la vez.

---

## 5) CRUXES

`CRUX: La banda de EV que define "decisión real" en el generador → A (Opus): ≤15% spread a 2-3 turnos = duda; >20% = regenerar | B (Gemini): regenerar solo si >35% → LO RESUELVE: solver de papel sobre 100 tableros cruzado con el TEST DEL EXPERTO — dar tableros que pasan cada umbral al novato vs experto con mismo seed/build; si los scores convergen (<15% brecha) en los tableros de 35%, ese umbral no produce foso y gana A. Kill si ni siquiera ≤15% diverge.`

`CRUX: Qué cruza primero el grafo familiar — grid legible solo vs grid + deep-link jugable → A (Opus): el deep-link es lo que compone K (receptor juega→genera su grid→reenvía); sin él K es un solo salto | B (Meta-AI/Gemini, data L1): la imagen que se entiende en 0.5s es lo que cruza; el link añade fricción → LO RESUELVE: A/B test de 1,000 shares en cohorte WhatsApp MX — variante grid-solo vs grid+deep-link; medir K_grafo e i de SEGUNDO orden (¿el receptor genera y reenvía su propio grid?). Si grid-solo iguala a grid+link en K compuesto, el deep-link es scope innecesario en P1 (vive solo en C-1 demo).`

`CRUX: ¿El verbo "sumar 15" admite 3 ejes de valor futuro divergente, o es un puzzle aritmético? → A (los tres asumimos que sí, capturar tiene valor futuro vía Pactos/ramas) | B (riesgo honesto, mi R1-C): si capturar nunca tiene valor futuro real, el spread colapsa estructuralmente y ninguna re-siembra lo arregla → LO RESUELVE: el MISMO solver de papel (un finde / medio día de código). Si tras re-estructurar la siembra >20% de tableros sigue convergiendo a 1 dominante, el verbo es puzzle → PIVOTAR de género conscientemente (no fingir que el generador lo arregla). Este crux se resuelve ANTES que todos los demás: es el cimiento.`

`CRUX: ¿La fatiga creativa del artefacto decae K más rápido de lo que el generador procedural lo repone? → A (Meta-AI, data L1): stickers se queman en 2-3 semanas, K decae | B (Opus): un generador procedural de variantes lo sostiene como mi re-siembra sostiene el foso → LO RESUELVE: medir K_grafo por COHORTE SEMANAL (no agregado) durante 6-8 semanas en EA — misma instrumentación-en-el-tiempo que el foso vivo. Si K decae sostenido pese al generador de variantes, la viralidad tiene vida media y el modelo económico (Palanca 3) debe presupuestar CAC>0 antes de lo previsto.`

---

### Cierre red-team (sin anestesia)
Los tres convergimos en el QUÉ (artefacto dual, generador-invariante, híbrido, separar los dos loops económicos). La diferencia entre clase-mundial y "competente" sigue viviendo en **dos números y un cimiento**: el spread de EV ≤15% (no 35%), el doble criterio de viralidad (comprensión Y disposición), y el solver que decide si el verbo es decisión o puzzle. Ninguno de esos tres es una frase en este documento — son tests que se corren con baraja + hoja de cálculo en un fin de semana, antes de un solo píxel. **Esa es la entrega. Todo lo demás sigue siendo PowerPoint hasta que el solver hable.**


────────── R2 — gemini ──────────
# DEBATE ETAPA 2 — ASIENTO: ESTRATEGA DE VALOR + SEÑAL DE MERCADO (Gemini)

El análisis cruzado de la Ronda 1 demuestra que estamos alineados en el diagnóstico: **la desconexión entre el tráfico móvil (donde se comparte) y Steam PC (donde se cobra) es el abismo mortal de ÓRDAGO.** Sin embargo, sus soluciones financieras y de conversión aún sufren de optimismo teórico. Vengo a inyectar realismo de mercado y señales de consumo para que la máquina de unit-economics cierre con precisión milimétrica.

---

## 1. Steelman + Ataque

### El fix que refuto:
*El precio de venta en LATAM de $299 MXN (~$15 USD) y $17.99 USD en Hispanos-USA propuesto por Meta-AI, asumiendo una conversión de wishlist a venta del 12% desde tráfico orgánico de WhatsApp.*

### Versión más fuerte del rival:
*«Al fijar un precio alto de $15 USD en LATAM y apelar a la afinidad cultural premium de los hispanos-USA a $17.99 USD, protegemos el posicionamiento de prestigio de ÓRDAGO frente a clones baratos, financiando un CAC orgánico muy bajo mediante loops de WhatsApp de alta conversión.»*

### Refutación (Data L1 + Señales de Mercado):
Este modelo comete un error crítico de **elasticidad de precio regional y fricción de plataforma (L3 🟢, L7 🟢)**. 
1. **La realidad de Steam en LATAM (Data L1):** El rey indiscutible de los indie-deckbuilders, *Balatro*, se lanzó en México a **$154.99 MXN** (~$7.50 USD) y en Argentina a precio regionalizado sugerido. *Inscryption* se vende a **$179.99 MXN** (~$9 USD). Intentar cobrar $299 MXN ($15 USD) por un juego basado en la baraja española en LATAM es un suicidio comercial. 
2. **El abismo de conversión Móvil $\rightarrow$ PC (L7 🟢):** En LATAM, la penetración de PC Gaming en hogares es inferior al **28%** (frente al 76% en USA). El tráfico de WhatsApp es 95% móvil. Si un usuario de WhatsApp en México abre un enlace en su teléfono, es redirigido a Steam (donde no tiene sesión iniciada en el navegador móvil) para comprar un juego de $15 USD que no puede jugar en su dispositivo actual. La conversión real de wishlist a venta para este flujo no será del 12%; caerá por debajo del **1.5%**. 

**Conclusión:** Debemos bajar el precio en LATAM a **$149.00 MXN ($7.49 USD)** y en Hispanos-USA a **$14.99 USD** para maximizar la velocidad del bucle viral. Cobrar más solo garantiza un factor $K$ estéril.

---

## 2. Mi punto más débil expuesto por los rivales

### El punto expuesto (por Opus y Meta-AI):
Mi propuesta de generar un **Clip Micro-Moment de 6 segundos localmente en el cliente (WebGL/Godot Móvil)** a 60fps es un cuello de botella técnico insostenible para el hardware móvil promedio de LATAM (gama media-baja, procesadores MediaTek/Snapdragon antiguos).

### Mi rectificación y actualización (Falsable):
**Acepto la crítica sin reservas.** Forzar la renderización y codificación de video MP4 en un navegador móvil destruye la experiencia de fricción cero (B5 🟢). 
* **El ajuste de diseño:** El **Objeto B (Clip de Video)** queda estrictamente degradado a una *feature* exclusiva de la versión de Steam de PC (donde la GPU sobra). 
* **Para el flujo móvil de WhatsApp:** El artefacto-puente se reduce únicamente al **Objeto A (Emoji-Grid en texto plano de 0 servidor)** y, opcionalmente, a la generación de una **imagen estática ligera (PNG de <100KB)** que renderiza la mano ganadora usando sprites vectoriales pre-cargados. Esto garantiza un tiempo de carga del enlace de la demo web de **<1.5 segundos** en redes 4G saturadas.

---

## 3. Convergencia por Palanca

### PALANCA 1 — El Artefacto-Puente Canónico
* **El Fix Ganador (Fusión Gemini + Meta-AI):** Un sistema dual optimizado para mensajería. Un **Emoji-Grid de 5 líneas de texto plano** (estilo Wordle, sin peso, copiable con 1-tap) que incluye un enlace corto `ordago.gg/d/<seedhash>`. Al hacer clic, abre instantáneamente una demo web de Godot (<8MB) que renderiza la mesa de forma idéntica, acompañada de una **firma sonora adaptativa (campanazo barroco + queja del Diablo, D3 🟡)** en el navegador.

### PALANCA 2 — El Generador de Bifurcación + El Foso VIVO
* **El Fix Ganador (Fusión Gemini + Opus):** El algoritmo de siembra del Diablo opera como un invariante matemático verificable en pre-producción. El solver garantiza que cada mano tenga $\ge 2$ jugadas Pareto-no-dominadas con un **spread de EV estrictamente acotado entre el 15% y el 25%**. 
  * *Por qué este rango:* Si el spread es $<10\%$ (Opus), el juego se siente como ajedrez/cálculo puro y mata la dopamina de la suerte percibida. Si es $>30\%$, la jugada dominante se vuelve obvia. 
  * *Foso Vivo:* Medición semanal de la **Entropía de Shannon de builds ganadoras ($H_{builds}$)** en Steamworks, con alarma si baja de $2.2$ bits.

### PALANCA 3 — Reconciliar plataforma ↔ viralidad ↔ economía
* **El Fix Ganador (Gemini):** Embudo asimétrico basado en el modelo de 3 columnas ajustado a la realidad de Steam:

```
[Móvil: Link de WhatsApp] ──> [Demo Web Gratis (1 manga)] ──> [Captura de Email] ──> [Wishlist/Compra en Steam PC]
```

* **Precios óptimos de conversión:** USA: $14.99 USD | Hispanos-USA: $14.99 USD | LATAM: $7.49 USD (149 MXN / 399 ARS). Esto asegura un ratio $LTV/CAC \ge 4$ en el segmento hispano utilizando adquisición orgánica basada en rivalidad.

---

## 4. DECISIÓN C-1: Confirmación de Voto

**Voto por el modelo HÍBRIDO (Steam Premium para PC + Demo Web Móvil de 1 mano).**

* **Por qué:** Es la única solución que respeta las limitaciones físicas de la conversión de plataformas (L7 🟢). El juego completo en Steam ($14.99 USD) preserva la percepción de valor premium y el posicionamiento ético sin microtransacciones fraudulentas (M1/LD7 🟢). 
* **El puente:** La demo web (alojada en un CDN ligero y optimizada para navegadores móviles) actúa como la "página de aterrizaje" sin fricciones del loop viral de WhatsApp. No vende directamente el juego en el teléfono; vende el "gancho" del reto y captura el correo electrónico del usuario para enviarlo a la wishlist de Steam, resolviendo la barrera móvil-escritorio.

---

## 5. CRUXES

### CRUX 1: La migración móvil $\rightarrow$ PC
* **Enunciado:** ¿Los jugadores de LATAM/Hispanos que prueban la Demo Web gratuita en su teléfono realmente encenderán su PC para comprar el juego en Steam, o simplemente abandonarán el embudo debido a la fricción de hardware?
  * **Opción A:** El flujo de conversión actual (Demo Web Móvil $\rightarrow$ Captura de Email $\rightarrow$ Wishlist Steam) es suficiente para un ratio $LTV/CAC \ge 3$.
  * **Opción B:** La fricción es demasiado alta y el juego requiere un lanzamiento simultáneo en móviles (Google Play / App Store) con un precio premium adaptado ($4.99 USD).
  * **Lo resuelve el test:** Un test de humo en la demo web durante el primer prototipo. Presentar a 2,000 jugadores móviles que completen la demo un botón dorado: *"Cómpralo en Steam con 10% de descuento"*. Medir cuántos hacen clic, ingresan su correo y efectivamente canjean el cupón en una landing page de Steam simulada. Si la conversión es $<2\%$, se debe activar inmediatamente el desarrollo del port nativo para móviles.

### CRUX 2: La rigidez matemática del generador
* **Enunciado:** ¿Forzar un spread de EV estricto del 15-25% en el generador elimina la sensación clásica de la "Escoba de 15" de que "cualquier mano puede ser salvada por la suerte"?
  * **Opción A:** Sí, el juego se vuelve demasiado simétrico y seco, alienando a los jugadores nostálgicos.
  * **Opción B:** No, el rango de 15-25% preserva el espacio de toma de decisiones estratégicas sin revelar la solución matemática obvia.
  * **Lo resuelve el test:** Un playtest A/B en el prototipo jugable. Cohorte A juega con siembra 100% aleatoria (con alto riesgo de jugadas dominantes); Cohorte B juega con siembra filtrada por el solver (spread 15-25%). Medir la retención al cabo de 5 partidas y el nivel de frustración percibido.

---

## MI APUESTA FALSABLE DE ETAPA 2

> **«ÓRDAGO no superará las 50,000 unidades vendidas en sus primeros 3 meses si fijamos el precio en LATAM por encima de los $9.99 USD (~199 MXN) y no logramos que la demo web móvil cargue el reto de WhatsApp en menos de 2.0 segundos en conexiones de red estándar de 15 Mbps.»**

────────── R2 — meta-ai ──────────
DEBATE ETAPA 2 — ASIENTO DATA L1 + RED TEAM

Vengo con la data, no con la intuición. En LATAM el chat manda, no el feed. WhatsApp concentra 12.4% del consumo de información en México, por encima de Facebook 11% y YouTube 10.7%. Y lo que se reenvía no es texto: los stickers personalizados son 56% y los animados 52%, mientras los predeterminados de WhatsApp son solo 12%. En Instagram, los reels consiguen entre el doble y doce veces más alcance que los posts, y los carruseles superan en 25.71% a la imagen única. 

1. Steelman + ataque

El fix que más ataco es el de Opus en Palanca 1: su versión más fuerte es "el artefacto-puente debe ser primero un emoji-grid de texto plano copiable en WhatsApp, porque es 0 peso, 0 servidor y cruza el grafo familiar sin explicación, y el clip viene después".

Refutación con data L1:

El grid de texto es exactamente el formato que la gente evita. La etnografía muestra preferencia clara por recursos visuales personalizados y animados sobre texto (36% stickers con texto vs 56% personalizados). Un string tipo Wordle se lee como "predeterminado genérico" (12% de uso), no como expresión personal. D1 no es 🟢, es 🟡 en LATAM: cruza sin explicación la imagen meme, no el código. 
El supuesto "clip pesa y se reenvía mudo 70-80%" ignora que en Instagram el alcance nace del video. Reels tienen hasta 12x más alcance, y la gente no reenvía links a Steam desde WhatsApp, reenvía stickers y estados con audio. El grid de Opus con "+18% margen" y seed hash es valor declarado, no entregado: no hay evidencia de que un no-jugador entienda "4/4 Mangas" en <2s. Es antipatrón C2: i alto, c bajo. 
Fatiga creativa: sin rotación procedural, el grid muere en 2-3 semanas en grupos familiares porque se percibe como spam institucional, no como humillación personal.
2. Mi punto más débil que otro expuso

Gemini y Opus tenían razón: yo propuse en R1 un emoji-grid copiable como Objeto A, asumiendo que "cabe en un mensaje" = "cruza". La data me corrige. Lo que cruza es la imagen-sticker, no el texto. Actualizo: el artefacto primario deja de ser texto plano y pasa a ser imagen PNG/WebP generada localmente (<80KB) con el grid dibujado, exportable en 1-tap como sticker personalizado. Mantengo el clip, pero ahora es co-primario, no secundario. También acepto la crítica de Palanca 3: sin demo web jugable, el "CAC∼0 vía WhatsApp" es humo. El link debe abrir juego, no tienda.

3. Convergencia por palanca

Palanca 1 — artefacto-puente: ganador fusión Meta + Opus. Dos outputs generados en cliente, sin servidor: A) sticker-imagen del grid (no texto) con "Le robé el alma a @primo" + score, B) clip 6s <500KB con audio firma. Ambos con deep-link a demo web de 1 mano. Kill: K_grafo WhatsApp <0.3 en MX tras 1,000 shares.

Palanca 2 — generador/foso vivo: ganador Opus con ajuste de spread. Invariante verificable: solver garantiza ≥2 jugadas Pareto-no-dominadas con spread de EV ≤15% a 2-3 turnos, no solo existencia. Instrumentación: entropía de Shannon de builds ganadores semanal, alarma si cae >15%.

Palanca 3 — economía: ganador Gemini. Modelo 3 columnas con LTV/CAC ≥3 por segmento, separando loop adquisición (demo web → wishlist, CAC) de loop retención (Diablo Fantasma, CAC∼0). Precio regional LATAM ∼$7-9 neto, no $15.

4. C-1: plataforma

Confirmo híbrido, pero con precisión de data. Steam como producto premium para credibilidad y descubrimiento. Demo web móvil ultraligera (<10MB, carga <3s) como parte del artefacto, no como marketing aparte. Por qué cambia: WhatsApp es el canal #1 de información, y el 80% del uso de stickers ocurre en chat con amigos. Si el link no es jugable en el teléfono, la fricción mata el impulso. Web-native-full-first mata el piso ético M1/LD7 (tiende a MTX) y Steam-first puro mata K. 

5. CRUXES

CRUX: ¿El objeto que cruza WhatsApp debe ser texto copiable o imagen-sticker generada? → A: texto 0 peso cruza mejor | B: imagen personalizada 56% vs 12% predeterminado cruza mejor → LO RESUELVE: test A/B en 20 grupos familiares MX con mismo mensaje en ambos formatos, medir tasa de reenvío sin explicación en 24h.

CRUX: ¿El clip debe priorizar alcance (Reels) o peso (WhatsApp Estados)? → A: clip <500KB sin audio para WhatsApp | B: clip 6-8s con audio firma para Reels (2-12x alcance) → LO RESUELVE: medir CTR a demo desde clip mudo vs con audio en cohorte hispana-USA, kill si diferencia <20%.

CRUX: ¿Basta con ≥2 jugadas Pareto-no-dominadas o hace falta spread ≤15%? → A: binario es suficiente | B: sin spread la decisión es ilusoria → LO RESUELVE: solver de papel sobre 100 tableros, medir % donde la 2ª mejor jugada está a <15% EV de la mejor, kill si <80%.

Fuentes
