# ÓRDAGO — Macro Game Design Document

> *La partida contra el Diablo.* Un roguelike deckbuilder con baraja española.
> Working title: **ÓRDAGO** · Alternativas: *EL ENVITE*, *LA PARTIDA*, *NAIPE*
> Versión: **1.1** (macro / north-star, post multi-debate) · Autor: César · Estado: validado por panel adversarial, listo para micro-GDD del prototipo

> **Nota — documento hermano de AZOTH.** ÓRDAGO comparte la *doctrina de diseño* de AZOTH: el juice stack como producto, el marco Bartle×MDA, el modelo premium sin MTX, la filosofía "rectángulos primero", la cobertura asíncrona de arquetipos sociales y la decisión de engine. Aquí se detalla **solo lo propio de ÓRDAGO**; donde la doctrina es idéntica se referencia y no se re-deriva.

> ### 🔄 Qué cambió en v1.1 (resumen ejecutivo)
> La v1.0 fue sometida a un **multi-debate adversarial de 3 IAs** (Opus, Gemini 3.5 Flash, Meta AI; 3 rondas + referee + síntesis auditada) anclado a `game-design-brain` (cartas A1–A5, lentes QF→Lazzaro→MDA, gates M1·LD7). El veredicto detonó cinco decisiones de César y un cambio de fondo:
> 1. **La fantasía "le hice trampa al Diablo" pasó de hueca a mecánica.** En la v1.0 ningún sistema modificaba el verbo "sumar 15": el motor entregaba optimización multiplicativa (la fantasía del *ingeniero*, igual que Balatro), no la del *tahúr*. El consenso del panel: *"el Diablo era un leaderboard con sombrero"*. **v1.1 construye el SISTEMA DUAL** que entrega el engaño como verbo jugable.
> 2. **La Mesa pasó de tablero pasivo a adversario vivo:** el Diablo **puebla la Mesa con intención** cada turno (§7.3).
> 3. **Nace la economía de Maña:** Fullerías (tu maña) y Pactos Oscuros (poder del Diablo) compiten por las **mismas ~3 ranuras** — un solo trade-off faustiano (§7.6).
> 4. **El Diablo Fantasma se vuelve humano y social:** rival real priorizado por tu grafo (WhatsApp/región), en banda cerrable (§8).
> 5. **La asistencia de UI se escinde y gradúa** (onboarding↔maestría) sin matar el Fiero ni la tabla (§13).
> El **único crux irreducible** que queda abierto es la **dirección de arte** (§11), que se zanja con un test A/B de feed, no por decisión de escritorio.
> Detalle completo del debate y los anclajes: `docs/research/2026-06-24-ordago-debate-valor/report.md` y `DECISIONES-FINALES.md`.

---

## 1. Vision Statement

**ÓRDAGO es el Balatro del mundo hispano — donde de verdad le haces TRAMPA al Diablo.**

Donde Balatro tomó la baraja francesa (póker) y AZOTH tomó un sistema no-de-cartas (alquimia), ÓRDAGO toma **la baraja española** —el mazo de la mesa de cocina de México, LatAm y España— y le aplica el motor que define al género: score-chase exponencial, estructura roguelite y feedback hiper-juicy.

Pero su verbo central **no son manos de póker ni la mera optimización de multiplicadores**: es el **Escoba contra un Diablo que hace trampa, y al que tú le haces más trampa todavía.** Sumas 15 sobre una **Mesa viva** que el Diablo puebla con intención (te ceba un 15 de carnada o te lo bloquea), él te impone **Trampas** que rompen las reglas ("esta mano suma 13", "los Oros no cuentan"), y tú respondes con tus **Fullerías** —la maña del tahúr— rompiendo *su* regla por una mano, con el riesgo de que te pille.

Todo envuelto en un cuento folk: **una partida de naipes contra el Diablo por tu alma**, en una cantina barroca a la luz de velas. Cada *run* es una mano contra el Diablo; cada umbral es el Diablo subiendo la apuesta y la trampa; ganar la Partida es recuperar tu alma con maña, no con fuerza.

**La propuesta de valor central (refinada por el panel):**
> *"ÓRDAGO te deja VENCER AL DIABLO HACIÉNDOLE TRAMPA —reescribiendo sus reglas en una Mesa viva con tus Fullerías, no acumulando multiplicadores— usando la baraja que ya conoces de la cocina."*

**La tesis comercial (lo que lo distingue de AZOTH):** AZOTH compite por white space *estético* global. ÓRDAGO compite por white space *cultural y de mercado*: el género, en pleno boom, está dominado por la baraja francesa, lo abstracto y lo anglo. El mundo hispano —cientos de millones— **no tiene su Balatro**, pese a que su shared mental model (baraja española, Escoba/Truco/Mus) es, para ese público, **más fuerte** que el del póker. ÓRDAGO es "ser el Balatro de una cultura que aún no lo tiene". Y alinea con el perfil del autor: mexicano, español-first, mercado LatAm + hispanos-USA.

**Elevator pitch:** *"El roguelike de la baraja de tu abuela donde ganas haciéndole TRAMPA al Diablo —rompes sus reglas en una mesa viva con tus Fullerías, no sumando más— y tu mejor partida se vuelve el Diablo que otro tiene que vencer."*

---

## 2. Design Pillars

Comparte los 6 pilares de AZOTH (rectángulos primero · mental model en 60s · romper tus propias reglas · el juice es el producto · el tema significa · amplitud de estéticas sin traicionar el género). Especificidades de ÓRDAGO, **reforzadas en v1.1**:

- **Pilar 2 (mental model) — aquí es una ventaja, no un riesgo.** El "sumar 15" del Escoba es **tan inmediato como el blackjack**, y para el mercado hispano la baraja española es intuición de infancia. Onboarding más fácil que el de Balatro para ese público.
- **Pilar 3 (romper tus propias reglas) — ahora es LITERAL.** El sistema dual (Trampa del Diablo ↔ Fullería del jugador, §7.6) convierte el lema en mecánica: el Diablo reescribe las reglas del Escoba y tú las vuelves a romper con tu maña. El "número que sube" es consecuencia de *ganarle la trampa*, no de apilar mults — ésa es la diferencia de fondo con Balatro y el foso de ÓRDAGO (A1).
- **Pilar 5 (significado) — el tono es cálido, no frío.** Donde AZOTH es liminal, austero y contemplativo, ÓRDAGO es **barroco, folk, teatral y vivo** (cantina, velas, calacas, cempasúchil). Mismo lenguaje de diseño, paleta emocional opuesta. **El tema cambia cómo se JUEGA** (la Mesa viva y la Trampa son diégesis y mecánica a la vez), no solo cómo se ve.

---

## 3. Posicionamiento de mercado

### 3.1 La tesis de diferenciación (¿no es esto solo un reskin de póker / "Balatro con sombrero"?)
Riesgo legítimo, y el más duro que levantó el panel: en la v1.0, vender "el Balatro hispano" *solo* por baraja + calacas era reskin competente con techo de nicho. **Por qué la v1.1 no cae ahí:**

1. **El verbo core no es el póker NI la pura optimización.** Es el Escoba sobre una **Mesa adversarial poblada por el Diablo** + el **duelo de trampas** (Trampa ↔ Fullería, §7.6). El engaño es el verbo, no una skin. (Beyond Words es "solo Scrabble" mecánicamente y es un hit por remixar un sistema familiar con un motor propio; ÓRDAGO remixa un sistema *aún más arraigado* para su mercado y le añade un verbo de trampa que ningún competidor tiene.)
2. **La especificidad cultural ES la diferenciación de entrada (el moat de hoy), y el sistema dual la convierte en foso de diseño (A1).** La baraja española es el mental model más fuerte que existe para cientos de millones de hispanohablantes; el sistema de Maña hace que ese tema produzca decisiones, no solo reconocimiento.
3. **Estética y tema 100% propios.** Cantina barroca + calaca + pacto/trampa con el Diablo no se parece a ningún competidor.

> **Honestidad de diseño (del veredicto):** la v1.0 entregaba la mitad del valor (pertenencia cultural ✓; "le hice trampa" ✗ hueca). La v1.1 existe para **entregar la otra mitad**. Si el sistema dual no pasa su test de kill (§14), ÓRDAGO debe replegarse conscientemente a "pertenencia cultural competente" — no fingir que es clase mundial.

### 3.2 El mercado hispano como cuña
- El género roguelike está en su pico (~$400M en Steam 2025, +80% YoY) y **China pesa >1/3** en los grandes éxitos del subgénero — prueba de que un mercado culturalmente alineado y bien servido es oro.
- El mundo hispano es el segundo idioma nativo más hablado del planeta y **carece de un score-chase deckbuilder propio**. Asimetría de mercado explotable.
- **Doble alcance:** ÓRDAGO funciona como "el Balatro hispano" para su mercado nativo *y* como curiosidad exótica y bella para el mercado global.
- **Señal de plataforma (Meta AI, ⚪ — validar en cohorte propia):** la Escoba en español supera ~4M descargas / 1M+ instalaciones, *"precisamente porque la mesa compartida genera decisión"* — sustento direccional (no prueba) de que el motor del verbo es la **Mesa poblada por un agente**, no la suma en solitario.
- **Localización inversa:** aquí el español NO es localización — es el idioma nativo del producto. El inglés y el chino son la localización de expansión.

### 3.3 Audiencia objetivo (Quantic Foundry primario; Bartle solo léxico)
- **Primaria:** el mercado hispano (México, LatAm, España, **hispanos-USA = sweet spot Tier-1**) que conoce la baraja de toda la vida — onboarding casi nulo. Clusters QF dominantes: **Mastery-Achievement** (el espinazo) + **Action-Social**.
- **Secundaria:** fans globales del género que quieren un sabor fresco y una estética distintiva.
- **El núcleo competitivo/social (cluster Action-Social = 41% del engagement LATAM/MX, QF 🟡)** se captura asíncronamente: el **Diablo Fantasma** como rival humano real, leaderboards de "almas ganadas", semillas diarias (§4, §8).

---

## 4. Arquetipos y estéticas (Quantic Foundry × MDA) — versión ÓRDAGO

Mismo método que AZOTH (cadena Jugador→Estética→Mecánica; cobertura del espectro completo; arquetipos sociales servidos asíncronamente, nunca multijugador en vivo). Jerarquía de lentes **QF (🟢 primaria) → Lazzaro (🟡) → MDA (🟡)**; Bartle solo como vocabulario. Lo propio de ÓRDAGO:

| Estética / Cluster QF | Mecánica ÓRDAGO | Nota |
|---|---|---|
| **Sensación** | Juice stack de cartas: barajeo, barridas (Escobas) explosivas, monedas saltando, campanazo del Diablo, **el "te pillé" cuando una Fullería falla** | Misma doctrina de juice que AZOTH (§10) |
| **Mastery-Achievement (Challenge/Strategy)** | Apuestas y **Trampas** crecientes del Diablo, Mangas, niveles de Codicia, El Envite del Diablo (bosses con regla-trampa) | El espinazo |
| **Submission / Relax** | Loop "una mano más", sesiones cortas | El zen del juego de cartas |
| **Fantasía (Immersion)** | Ser el tahúr que **le hace trampa** al Diablo; romper la banca del infierno con maña | Frame trickster (no Faustiano-trágico: pícaro que GANA) |
| **Narrativa (Immersion)** | El cuento folk del que engaña al Diablo; viñetas de cantina (opt-in); el *Romancero* | Trickster |
| **Creativity — Discovery** | Pactos Oscuros secretos, Fullerías no documentadas, el *Romancero* a excavar, el Codex como mapa | Discovery vive bajo Creativity (QF), reforzado |
| **Creativity — Expresión / build-as-signature** | **Tu set de Fullerías + Pactos en tus ranuras de Maña ES tu firma**; Jugadas como ramas excluyentes (§7.4); personalización de baraja y cantina | Ahora con sistema que lo entrega (antes hueco) |
| **Action-Social — Community (async)** | Semillas diarias compartidas, builds compartibles, watchability/streaming, **"liberé el alma de [tu primo]"** | Sin co-op en vivo |
| **Action-Social — Competition (async)** | **El Diablo Fantasma:** la run de otro jugador real, priorizado por tu grafo social, se encarna como el Diablo a vencer; tablas de almas; ranking de la semilla diaria | Hook competitivo temáticamente integrado (§8) |

> **Ventaja temática:** el frame "partida contra el Diablo" da una **encarnación natural del oponente asíncrono**. El Diablo Fantasma —el score real de otro humano, vestido de Diablo— convierte el leaderboard en parte de la ficción. Sirve al cluster Action-Social (41% del engagement LATAM/MX) sin PvP en vivo y refuerza la fantasía.

---

## 5. La fantasía / experiencia del jugador

Eres un **tahúr** (un pícaro) que se sienta a la mesa del Diablo en una cantina fuera del tiempo. Apostaste tu alma. El Diablo reparte, **siembra la Mesa con intención, sube la apuesta y hace trampa** —y tú tienes que ser más astuto, más rápido, y **hacerle más trampa que él.** El arco de una run ganada:

1. **Primera Manga:** jugadas torpes, apenas alcanzas la apuesta; el Diablo sonríe condescendiente y te marca las cartas ("el Diablo te sopla").
2. **El primer Pacto / la primera Fullería que rima:** rompes una Trampa del Diablo con tu maña y encadenas una Escoba que dispara otra. Ves la primera cascada. El Diablo deja de sonreír y deja de soplarte.
3. **La máquina:** equipas tus ranuras de Maña, decides qué le empeñas al Diablo (Pactos) y qué maña te guardas (Fullerías), encadenas Escobas sobre su Mesa sembrada, las matas multiplican. Pasas de sumar 15 a sumar miles **engañándolo en cada Envite**.
4. **La Última Mano:** rompes la banca del infierno con una trampa final. El Diablo pierde. Recuperas tu alma.

El sentimiento no es "optimicé una build". Es: ***le hice trampa al Diablo y gané.*** (Criterio de éxito del prototipo §14: ≥60% de los testers describe su victoria espontáneamente como "le hice trampa / lo engañé", no como "optimicé números".)

---

## 6. Core Loop

### 6.1 El verbo central — el Escoba ("sumar 15") sobre una Mesa viva
El núcleo legible, en una frase: **formas jugadas cuyo valor suma 15 (o múltiplos) para hacer una *Escoba* (barrida) sobre una Mesa que el Diablo puebla con intención; cada Escoba puntúa Puntos × Suerte; el Diablo impone Trampas que alteran la regla y tú las rompes con Fullerías; los Pactos encadenan Escobas en cascadas.**

Es solitario contra el Diablo (no el Escoba 2-jugadores literal), adaptado a score-chase **pero con un oponente que actúa** (la diferencia clave de v1.1: la Mesa no es un solitario, es un duelo asimétrico).

### 6.2 El loop de mano (segundos)
```
1. El Diablo REPARTE a tu mano Y SIEMBRA la Mesa con intención (te deja un 15 de carnada
   o te bloquea las combinaciones bajas para forzarte a recalcular). [§7.3]
2. (Si hay Envite) una TRAMPA del Diablo altera la regla esta mano ("suma 13", "Oros no cuentan").
3. Seleccionas cartas para formar una JUGADA; la UI muestra la suma acumulada de tu selección
   y (en modo aprendiz) resalta las cartas de la mesa que completan el 15. [§13]
4. Opcional: gastas una FULLERÍA de tus ranuras de Maña para romper la Trampa esta mano,
   con riesgo de que el Diablo te pille (tell visible). [§7.6]
5. Si la jugada suma 15 (o múltiplo), haces una ESCOBA (barrida) → evento de puntuación.
6. La Escoba produce Puntos base × Suerte (mult). Los PACTOS activos modifican/encadenan (cascada).
7. Las cartas capturadas y las matas añaden valor; los Puntos se suman a tu Codicia del turno.
8. Repites hasta agotar tus "Manos" o alcanzar la apuesta del Diablo.
```
Ritmo objetivo: **30–45 s/mano**. Decisión en la Cantina entre mangas: **3–5 min**.

### 6.3 El loop de run (minutos)
```
La apuesta (= "blind"): supera el umbral de Puntos que pone el Diablo.
   → 3 apuestas por Manga (chica / grande / El Envite del Diablo con su TRAMPA).
La Cantina (shop) entre apuestas: compras/equipas Pactos y Fullerías (ranuras de Maña),
   naipes, mejoras, rerolls; gestionas Reales.
4 Mangas = La Partida completa. Ganar la 4ª = recuperar tu alma (run ganada).
```

### 6.4 El loop de meta (horas/semanas)
```
Cada run → desbloqueos en el Codex + nuevos Pactos/Fullerías/naipes + progreso de Tahúres
   + posición en leaderboards + tu mejor run se vuelve Diablo Fantasma de otros.
Más Tahúres (mazos/personajes) → estilos de juego distintos.
Más niveles de Codicia (stakes) → la misma Partida más dura (Trampas más crueles).
Desafíos de Cantina → puzzles de build con reglas fijas.
Semillas diarias (la mesa del Diablo de hoy) → competición y comunidad asíncrona.
```

---

## 7. Sistemas centrales

### 7.1 Los cuatro palos (las "suits")
La baraja española, con identidad mecánica por palo:
- **🪙 Oros** — riqueza/economía. Lean: generación de **Reales** (la moneda) y bonos de Puntos base.
- **🍷 Copas** — fluidez/repetición. Lean: redraws, retención de cartas, efectos de "otra ronda".
- **⚔️ Espadas** — agresión/multiplicador. Lean: ×Suerte, las cartas de mayor poder bruto.
- **🌳 Bastos** — fuerza/escala. Lean: +Puntos en bloque, escalado por cantidad de cartas.

> 🔶 Decisión abierta (§19-5): si las afinidades de palo son fuertes (definen build) o ligeras. El panel recomienda **fuertes** para dar profundidad a la Expresión, pero es tunable en vertical slice.

### 7.2 La baraja (los valores) — con legibilidad de v1.1
Baraja de **40 cartas**: 1–7 + Sota (10), Caballo (11), Rey (12) por palo (sin 8 ni 9). Para el motor de Escoba, las figuras valen **8/9/10** (Sota/Caballo/Rey) al sumar 15 — la convención clásica del Escoba.

> **Cambio v1.1 (legibilidad, A5):** los naipes muestran el **valor de juego 8/9/10 GRANDE** en las figuras (la ilustración tradicional pasa a fondo secundario), eliminando la duda "¿la Sota valía 8 o 10?". Onboarding global sin matar el sabor (ver §13).

### 7.3 La Mesa viva — el Diablo como poblador ACTIVO (núcleo de v1.1)
La acción ocurre sobre **La Mesa del Diablo**, que en v1.1 **deja de ser un tablero pasivo**: cada turno el Diablo **siembra cartas con intención** desde su mazo corrupto. Dos modos de siembra que se alternan:
- **Carnada:** te deja un 15 casi servido para tentarte a una jugada subóptima (que activa una Trampa o desperdicia una Mata).
- **Bloqueo:** descarta boca arriba cartas que cierran las combinaciones bajas y te obligan a **recalcular activamente** (si tira un 7, mata muchos 15 fáciles).

Sumar 15 con tu jugada = **Escoba** (barrida) = evento de puntuación. Múltiplos (30, 45) = Escobas mayores con multiplicadores crecientes. Las cartas capturadas se acumulan en tu **Baza**, que aporta valor.

> **Por qué importa (A1):** sin poblador activo, "sumar 15" con mano + mesa abiertas tiene solución casi-única = puzzle aritmético, no Escoba. El Diablo sembrando con intención crea la **emergencia bilateral** (≥2 jugadas "correctas" por tablero) que hace del verbo una decisión, no un cálculo. **Criterio de kill (§14):** si con poblador NO aparecen ≥2 jugadas correctas en el mismo tablero, el verbo es puzzle → pivotar de género.

### 7.4 Las Jugadas (combinaciones — ahora ramas excluyentes)
Sobre el "sumar 15", la profundidad viene de las combinaciones nativas de los juegos de baraja española. **Cambio v1.1:** se reescriben como **ramas mutuamente excluyentes** (elegir/especializar un arquetipo de Jugada cierra otros en esa run) para que la **Expresión/build-as-signature** sea real (A1: la opción dominante se mata; sin esto, la jerarquía era aditiva y convergía a un único build óptimo).

| Jugada | Origen | Efecto |
|---|---|---|
| **Escoba** | Escoba | El evento base: sumar 15 |
| **Pares / Medias / Duples** | Mus | Pares, trío, dos pares → tiers de mult |
| **Secuencia / Liga** | Chinchón/Tute | Corrida en un palo → bonus |
| **Envido** | Truco | Dos cartas del mismo palo que suman alto → bonus de palo |
| **Las Matas** | Truco | Las 4 cartas legendarias (§7.5) |

### 7.5 Las Matas (las cartas legendarias — rareza ya integrada)
Truco trae un sistema de rareza *gratis* y culturalmente icónico: la jerarquía de las **matas**, las cuatro cartas más poderosas, en orden:
1. **As de Espadas** (el macho / ancho de espadas)
2. **As de Bastos** (ancho de bastos)
3. **Siete de Espadas**
4. **Siete de Oros**

En ÓRDAGO son cartas de **Puntos base enormes y efectos únicos** — las "doradas" que el jugador sueña con capturar. Sistema de rareza/poder que el público hispano reconoce sin explicación (para el jugador global se enseña vía juice y Codex). 🔶 Confianza del peso cultural en mercado global: 🟡 (validar).

### 7.6 El SISTEMA DUAL — Trampa del Diablo ↔ Fullería, y la economía de Maña (corazón de v1.1)
Este es el sistema que entrega la fantasía "le hice trampa al Diablo" como verbo, y el cambio estructural más importante respecto a v1.0.

**(a) Las Trampas del Diablo (en cada Envite, §7.10).** El Envite del Diablo impone una **regla-trampa** que altera el verbo esa apuesta: *"esta mano suma 13, no 15"*, *"los Oros no cuentan"*, *"solo valen pares"*, *"la primera Escoba no puntúa"*, *"las matas valen la mitad"*. La Trampa es el reto (Mastery-Achievement) y la diégesis del Diablo haciendo trampa.

**(b) Las Fullerías (tu maña).** Trucos del tahúr que **rompen la Trampa por una mano**: *"la Sota se lee como 5"*, *"esconder una Mata en la manga"*, *"robar una carta de la Mesa"*, *"forzar un 15 falso"*. Cada Fullería se juega con un **tell/riesgo visible**: hay ~15% de que el Diablo te pille → penalización (carta corrupta a tu mazo / pierdes la mano). Esto es A1🟢🟡 (¿la uso ahora o me la guardo?) + A4🟢🟡 (causa: engañar → efecto: ganar) + LD2 Hard Fun (el Fiero de salirte con la tuya).

**(c) Los Pactos Oscuros (poder del Diablo).** Modificadores pasivos brutales enmarcados como **tratos con el Diablo** (paralelos a los Jokers de Balatro / catalizadores de AZOTH): *"+30 Puntos por cada Oro"*, *"×1.5 Suerte si haces Escoba con Espadas"*, *"cuando puntúa una Mata, repite el Pacto a su izquierda"*. Algunos son **Pactos Oscuros secretos** (Arcana Oculta equiv.), desbloqueados por descubrimiento (Discovery/Creativity).

**(d) La economía de Maña — el trade-off faustiano (DECISIÓN 3, resuelta).** Fullerías y Pactos **compiten por las mismas ~3 ranuras de "Maña"**. Cada ranura equipa **o** una Fullería (maña activa anti-Trampa) **o** un Pacto Oscuro (poder pasivo del Diablo). **Tomar un Pacto ocupa una ranura para toda la run** — ésa es la maña que le vendiste al Diablo. Un build "0 Fullerías / 3 Pactos" es legal (máximo poder) pero **te comes cada Trampa del Envite en crudo**.
- **Por qué es el foso (A1🟢🟡):** convierte dos pilas de Jokers paralelas en **UN solo trade-off** — cambias tu maña (agencia anti-Trampa) por poder bruto del Diablo, y lo pagas en cada Envite. La opción dominante se mata sola. Costo **estructural y recurrente** = fausto, no "Joker renombrado".
- **Ética (M1·LD7🟢🟡):** costo transparente, real durante la run, con **saciedad alcanzable** (se gana con 0/1/2/3 Pactos; la run reinicia el saldo — sin ratchet ni FOMO entre runs). No es extracción.
- **Auto-balance:** la regla-trampa del Envite escala de modo que sin Fullerías la Trampa duele de verdad → el costo del slot se paga en dificultad real, no en un número arbitrario.
- **Descartado del debate:** la quema literal de una Fullería concreta (acantilado binario), el costo genérico de "carta al mazo" como mecánica base (aditivo), y la recuperabilidad plena (deja de ser fausto). *Pueden existir como Pactos concretos raros, no como regla base.*

### 7.7 La matemática: Puntos × Suerte
**Puntos (azul, base)** × **Suerte (rojo, mult)**. Los **+Suerte** y **×Suerte** crean el escalado exponencial; el orden izquierda→derecha importa (rompecabezas de secuenciación de Pactos); las cascadas nacen de Pactos que disparan Pactos. Idéntico en estructura al motor de AZOTH y de Balatro — **pero en ÓRDAGO el número grande es consecuencia de ganarle la trampa al Diablo, no de apilar mults en el vacío.**

### 7.8 Naipes Marcados (mejoras — el equivalente Foil/Glass)
El tahúr marca las cartas. Mejoras con textura + luz propia al hover:
- **Marcada** (×Suerte fijo — Holo/Polychrome).
- **Dorada** (genera Reales — Gold).
- **Encerada/Resbaladiza** (se juega y vuelve a la mano — efecto de repetición).
- **De Cristal** (×Suerte alto pero se rompe — Glass).
- **Cargada/Trucada** (un solo uso, efecto brutal — Volátil).

### 7.9 Economía: La Cantina
- Moneda: **Reales** (moneda histórica española), ganados por mangas + **interés** sobre lo guardado (misma tensión gastar/acumular de Balatro).
- En **La Cantina** (la taberna donde el Diablo atiende la barra) compras/equipas: Pactos, Fullerías, naipes, mejoras, **reroll**, ranuras de Maña extra.
- Gestión de Reales = capa estratégica completa.

### 7.10 La estructura: La Partida contra el Diablo
- **4 Mangas** (la apuesta y la Trampa suben en cada una), cada una con **3 apuestas**: chica, grande, y **El Envite del Diablo** (un boss que impone su **regla-trampa**, §7.6a).
- Ganar la 4ª Manga = **recuperar tu alma** = run ganada.
- **Modo Condena** (endless) post-victoria para los hardcore.

---

## 8. Progresión, meta y capa social asíncrona

Misma arquitectura que AZOTH (§8 de aquel doc). Específico de ÓRDAGO:
- **Tahúres (= decks/personajes):** cada uno con un palo de afinidad, condición inicial y estilo de juego. Combustible para Discovery y Expresión.
- **Niveles de Codicia (= stakes/Ascension):** el Diablo apuesta más fuerte y sus Trampas son más crueles.
- **El Codex / Romancero:** colección de Pactos, Fullerías, naipes y jugadas + el *lore* folk (el Romancero del Diablo). Mapa de Discovery. Cero lore obligatorio (A4: el lore vive como capa opcional para el ~5%).

### 8.1 El Diablo Fantasma (DECISIÓN 4, resuelta) — rival humano real, social, cerrable
El high-score de otro jugador en tu semilla se encarna **como el Diablo** al que debes superar. Reglas de v1.1:
- **Siempre un jugador REAL**, elegido por prioridad: **(1) tu grafo social** (contacto de WhatsApp/amigo que jugó la semilla) → **(2) tu región** (MX/LATAM/hispano-USA) → **(3) global**.
- **Banda cerrable:** su score cae **~5–12% por encima de tu mejor histórico** en esa semilla (Festinger/LD6🟢: gap cerrable pero no trivial → "por poco lo tengo → una mano más").
- **Recompensa al vencerlo:** *"liberaste el alma de [handle]"* + te quedas con sus Reales sobrantes; aparece el siguiente en la escalera.
- **Cold-start** (semilla nueva / sin rival en banda): un **"Diablo del Romancero"** con nombre y rostro estilo Posada ("El Charro Negro", "El Chacho de Cantina") **con score real de tu percentil** — nunca te deja sin rival cerrable.
- **Guardarraíles de integridad (M1🟢🟡):** scores **siempre reales, nunca fudgeados**; **nunca se baja la vara tras una derrota** (eso delata el truco y mata el Fiero); el rubber-band **solo sube**; se muestra siempre handle + margen no trivial.
- **Por qué (clase mundial):** sirve a las DOS mitades del cluster Action-Social (41% del engagement LATAM/MX, QF🟡) — Competición (gap cerrable) **+ Community** (un humano con nombre, no un clon de ti). La prioridad de grafo social es el **foso viral LATAM**: *"mira cómo le gané al Diablo de tu primo"* se comparte solo en el grupo de WhatsApp (artefacto-puente, CAC~0).

### 8.2 Resto de la capa social asíncrona
- **Semillas diarias/semanales ("La mesa del Diablo de hoy"):** ranking global.
- **Tablas de Almas (leaderboards):** rankings de "almas ganadas" globales/amigos/por Tahúr. **Una sola escalera comparable** (ver §13: la asistencia de maestría no fragmenta la tabla).
- **Compartir la mano:** código de run/build para presumir engines rotos.
- **Diseño para watchability/streaming.**
- Stretch post-1.0: **duelo asíncrono / carrera de semilla** (NO co-op ni PvP en vivo).

---

## 9. Filosofía de dificultad y balance
Idéntica a AZOTH: easy to learn / hard to master; curva que **fuerza** combos rotos; variance controlada (reroll + descarte como válvulas); balance por spreadsheet + telemetría. Aquí el "easy to learn" es aún más fuerte por el shared mental model del Escoba; el "hard to master" lo da el **duelo de trampas** y la economía de Maña (decidir qué le empeñas al Diablo).

---

## 10. Game Feel / Juice
Mismo juice stack que AZOTH (animación → partículas → screen effects → audio → háptica; "el número grande es objeto de gameplay"; color = etiqueta sin labels). Sabor específico de ÓRDAGO:
- **Feel de naipe:** el peso del barajeo, el chasquido al repartir, el *barrido* satisfactorio de la Escoba (las cartas vuelan de la mesa a tu baza).
- **El Diablo reacciona y actúa:** micro-reacciones al otro lado de la mesa (frunce el ceño, golpea la mesa, ríe, **siembra la Mesa con un gesto**, **te sopla las cartas en onboarding y deja de hacerlo**, **te pilla una Fullería con un "¡tramposo!"**) — feedback diegético del progreso y del duelo de trampas.
- **Audio:** guitarra/jarana, palmas, campana de iglesia grave en cada ×Suerte, el rumor de la cantina que crece con la cascada.
- **Color funcional:** Azul = Puntos · Rojo = Suerte · Oro = Reales · Verde = Manos restantes · y un acento por palo.

---

## 11. Dirección de arte y audio (🔶 EL ÚNICO CRUX IRREDUCIBLE — se decide por A/B, DECISIÓN 2)

**Pilar estético: barroco folk latinoamericano — la antítesis cálida de AZOTH.** El qué (cantina, Diablo-tahúr, calaca, baraja española reinterpretada) está fijo. El **cómo** (la paleta y el grado de minimalismo vs maximalismo) es la **única disputa que el panel declaró irreducible** y que NO se cierra por intuición — se zanja con un **test A/B de feed** (§14).

- **Escenario:** una **cantina a la luz de velas**, fuera del tiempo; el Diablo como un *tahúr* elegante y carismático al otro lado de la mesa de madera.
- **Cartas y UI:** **grabados estilo Posada** (dominio público), iconografía de la baraja española reinterpretada, filigrana barroca. Calacas, cempasúchil, veladoras, exvotos.

### 🔶 La decisión A/B de paleta (DECISIÓN 2 — abierta, la resuelve el feed)
- **Lado A — Claroscuro boutique premium:** negros cálidos/maderas + oro de vela, saturación selectiva (tipo *Darkest Dungeon* / *Cult of the Lamb* / *Inscryption*). **Pro:** alto CTR en trailers, "watchability", gancho de exportación a Steam global. **Contra (Meta AI, data L1):** arriesga lectura *"hotel boutique en Tulum"* y la crítica de **"blanqueamiento"** que satura redes 2024-25 ("MÉXICO ES MAXIMALISTA: colores, texturas, sabores").
- **Lado B — Maximalismo identitario:** *más es más* — **el oro NO como lujo sino como moneda sucia**, cempasúchil, papel picado, color y textura. **Pro:** autenticidad, evita la acusación de apropiación, lo que se guarda/comparte en LATAM. **Contra:** menos "premium" para el ojo Steam global; riesgo de leerse "casual móvil".
- **Cómo se decide:** **test de 3s en feed real** (IG/TikTok/Reels, cohorte hispana-USA + MX 18-34), A/B maximalista-color vs claroscuro-boutique, midiendo recall ("Diablo/tahúr/baraja"), share/saves y comentarios de autenticidad. **No apostar el arte antes de este test.**

- **Tono:** teatral, vivo, folk, ominoso-pero-festivo. La energía del Día de Muertos: la muerte con humor, color y respeto. **Inquietante sin gore** (clave para rating, §16).
- **Audio:** son jarocho / guitarra / jarana, palmas, coros, campanas; soundtrack folk-barroco hipnótico (parte del legend status del género — invertir aquí).

> **Pipeline AI-augmented:** el estilo grabado-Posada, filigrana e iconografía de naipes es **muy favorable a generación 2D asistida por IA** + retoque. Ventaja de scope.
>
> ⚠️ **IP/estética:** inspirarse en el *estilo* de Posada (dominio público) y el imaginario folk del Día de Muertos es seguro; **evitar** copiar diseños registrados (Catrinas de marcas, personajes de películas) y barajas comerciales. Diseño de cartas 100% original. Respetar homenaje vs apropiación (el lado B del A/B es, además, la mitigación cultural).

---

## 12. Narrativa y worldbuilding
- **Premisa:** un tahúr apostó su alma y se sienta a la mesa del Diablo en una cantina fuera del tiempo. La salida es ganarle **con maña, haciéndole trampa.**
- **Entrega:** 100% ambiental y opcional — viñetas de cantina, flavor de Pactos y Fullerías, el arco de las 4 Mangas, el *Romancero del Diablo*. **Cero lore dump** (A4: regla de no-peaje inviolable — nada de lore obligatorio antes del primer momento jugable).
- **El subtexto:** el arquetipo del **trickster** — el pícaro que vence al poder superior con maña, no con fuerza. Raíz folk pan-hispana del "engañar al Diablo" (el cuento del jugador que le gana las cartas al demonio). El sistema dual (§7.6) **es** ese subtexto hecho mecánica.

---

## 13. UX / Onboarding (DECISIÓN 5, resuelta — asistencia escindida y graduada)
- **"Sumar 15" es instantáneo** — como el 21 del blackjack; para el público hispano la baraja no necesita tutorial.
- **Jugadas telegrafiadas:** la UI muestra la suma y el score previo antes de confirmar (como Balatro).
- **Codex como tutorial pasivo.**
- **Métrica de control:** comprensión del loop en **<90 s** de telemetría (objetivo más agresivo que AZOTH por el mental model más fuerte).

### 13.1 La asistencia de UI al verbo, en TRES capas (DECISIÓN 5)
El verbo tiene dos actos: **aritmética** (acarreo + disonancia de figuras = fatiga estéril, un impuesto) y **búsqueda combinatoria/decisión** (cuál de los muchos 15 hago dada la Trampa, mis Pactos y lo que el Diablo sembró = donde viven el Fiero LD2🟢 y el espacio de decisión A1🟢🟡). La asistencia mata el impuesto sin tocar la decisión:
1. **Siempre ON (gratis, todas las runs):** valor de juego **8/9/10 grande** en figuras (§7.2) + **suma acumulada de tu selección actual.** Mata solo la aritmética estéril.
2. **"Modo aprendiz" (gratis, temporal):** el resaltado de *cartas de la Mesa que completan el 15* está ON las primeras **~3 runs / hasta tu 1ª victoria**, luego **se desvanece gradual** con encuadre diegético (*"el Diablo deja de soplarte"*). Queda un **toggle de accesibilidad permanente**.
3. **En maestría NO es gratis:** quien quiera el resaltado de Mesa en régimen de maestría lo equipa como la Fullería **"Ojo del Tahúr"** (ocupa una ranura de Maña, §7.6, y tiene riesgo de ser pillado). Así cualquier ayuda de maestría **cuesta un slot y entra al trade-off faustiano** — nunca rompe el verbo ni la tabla.

> **Por qué (clase mundial):** bajo la Mesa adversarial poblada (§7.3), el resaltado de Mesa cruza a **solucionador parcial** en maestría → por eso se gatea, no se deja permanente. Onboarding rápido (<90 s) sin dejar una muleta que el jugador resienta (M1🟢🟡); maestría en crudo conserva el foso (A1).
>
> **Conflicto cruzado resuelto:** se descartó la opción "desactivar la ayuda a cambio de un multiplicador de score + categorías de leaderboard" porque **fragmentaba la tabla del Diablo Fantasma** (§8) — que necesita UNA escalera comparable. La asistencia de maestría vive en la economía de slots (capa 3), no en el score.

---

## 14. Scope y MVP
Misma filosofía "rectángulos primero" que AZOTH. **El prototipo de v1.1 está diseñado para falsar el sistema dual antes de gastar arte.**

- **Prototipo (rectángulos / papel):** 1 Tahúr, motor de Escoba + Puntos×Suerte, **Mesa viva (un humano hace de Diablo sembrando)**, **~3 ranuras de Maña**, ~3 Pactos Oscuros + 3 Fullerías + 3 Trampas en post-its, 1 Manga (3 apuestas + 1 Envite del Diablo), Cantina básica con Reales e interés.
  - **Setup analógico:** baraja española de 40 cartas + post-its; el jugador con su mano y 2-3 ranuras; tú actúas de Diablo lanzando cartas a la Mesa y aplicando Trampas según un dado.
  - **Filtros / criterios de kill (de primer nivel):**
    1. ¿Aparece "una mano más" SIN juice/arte? (retención del loop desnudo)
    2. ¿Hay **≥2 builds ganadores distinguibles** y **≥2 jugadas correctas por tablero** con la Mesa poblada? (espacio de decisión, A1)
    3. **Recall de fantasía:** ¿los testers describen su victoria como **"le hice trampa / lo engañé"** (≥60% espontáneo, éxito) o **"optimicé números"** (fallo)?
    4. **Señal viral cualitativa:** ¿risas, insultos lúdicos hacia ti-Diablo ("¡maldito tramposo!"), deseo inmediato de repetir, ganas de compartir el clip?
  - **KILL:** si A (Pactos pasivos solos) y B (con Mesa viva + sistema dual) producen la misma distribución de decisiones, o <60% recall en B → matar el sistema de trampa y replegarse a "pertenencia cultural competente". Si el poblador de Mesa no genera ≥2 jugadas correctas por tablero → pivotar de género.
- **Vertical slice:** las 4 Mangas, ~80–120 Pactos + Fullerías (incl. primeros Pactos/Fullerías secretos), 1 Tahúr pulido con juice + audio, UI/color final (tras el A/B de §11), esqueleto de semilla/Diablo Fantasma. Demo de Next Fest.
- **Cortes:** core single-player definitivo; capa social **asíncrona sí** (incl. el Diablo Fantasma); **multijugador en vivo NO**. Múltiples Tahúres, Codicia alta, Modo Condena → post-EA/1.0.

---

## 15. Tecnología y plataforma
Misma decisión que AZOTH (🔶 **DECISIÓN — Engine**): **validar el loop con rectángulos en lo más rápido a la mano (Godot/Love2D, un fin de semana); decidir Unreal solo si el juice justifica la fricción de un 2D card-game en un engine 3D.** Niagara + material system de Unreal son armas de clase mundial para el juice si vas por ahí. PC/Steam primero; ports post-1.0. Datos data-driven (JSON/Data Tables); Steamworks leaderboards para la capa asíncrona (suficiente para el Diablo Fantasma de §8).

---

## 16. Modelo de negocio
Misma doctrina que AZOTH: **premium buy-to-play, $14.99–$19.99, sin MTX, updates gratis, colaboraciones estilo "Friends of Jimbo", la confianza/comunidad como activo, ruta Steam → suscripciones → ports → long tail.** Diferencias propias de ÓRDAGO:
- **El español es el idioma nativo, no la localización.** Mercado primario gigante y desatendido desde el día uno, con CAC bajo vía contenido en español (tu fortaleza) y el motor viral del Diablo Fantasma social (§8). El inglés y el chino son expansión.
- **Ventaja de rating:** el Escoba y la baraja española **no evocan gambling de casino** como el póker/slot que metió a Balatro en líos de PEGI. Tono folk sin gore → rating accesible (12+/T). El frame "Diablo/trampa" es folk-cultural, no de apuestas reales.

---

## 17. Roadmap de producción
Mismo esquema de 5 fases que AZOTH (Prototipo → Vertical slice → Demo/Next Fest → Early Access → 1.0+post-launch), con modelo EA transparente y manejo de crisis rápido. Hito propio: una **campaña de marketing en español/LatAm** (creators de habla hispana, nostalgia de la baraja española, el clip "le gané al Diablo de tu primo") como motor de wishlists barato y diferenciado.

---

## 18. KPIs
Mismos KPIs por cluster que AZOTH (wishlists, conversión, % reseñas positivas; por cluster: compleción/Codicia para Mastery-Achievement, ritmo de descubrimiento de Pactos/Fullerías secretos para Creativity-Discovery, participación en semillas/Diablo Fantasma para Action-Social, runs compartidas para Community; session length, CCU, retención 20h+/50h+; salud del loop). Métricas propias:
- **Recall de fantasía:** % que describe su victoria como "le hice trampa" (la métrica que valida el sistema dual).
- **Penetración por geografía hispana** y **conversión del público no-hispano** (¿el "sumar 15" cruza fronteras?).
- **Share rate del Diablo Fantasma social** ("vencí al Diablo de [nombre]").

---

## 19. Riesgos y decisiones

### 19.1 Riesgos
| Riesgo | Severidad | Mitigación |
|---|---|---|
| **Percepción de "reskin de póker / Balatro con sombrero"** | Media (bajada en v1.1) | El sistema dual (§7.6) hace del engaño un verbo; criterio de kill de recall ≥60% (§14) |
| **El sistema dual no entrega la fantasía en playtest** | Media-Alta (nuevo, el riesgo clave de v1.1) | Prototipo de papel barato (§14) con criterios de kill duros ANTES de gastar arte; repliegue consciente a "pertenencia cultural" si falla |
| **Mercado primario hispano: ¿paga en Steam como el global?** | Media | Precio regional; doble alcance (nativo + exótico global); motor viral social baja CAC |
| **IP/estética (Posada, Día de Muertos, blanqueamiento)** | Media | Estilo de dominio público; diseños originales; el A/B de §11 (lado maximalista) es la mitigación cultural |
| **Onboarding fuera del mundo hispano** | Baja | "Sumar 15" universal (blackjack); legibilidad 8/9/10 (§7.2); modo aprendiz (§13) |
| **Rating/gambling** | Baja (ventaja) | Escoba no evoca casino; tono folk sin gore |
| **Mesa viva → puzzle de solución única** | Media | Criterio de kill: ≥2 jugadas correctas por tablero (§7.3, §14) |
| (Comparte riesgos transversales de AZOTH: tema sobre loop, saturación, fricción de Unreal, scope, balance exponencial) | — | Ver AZOTH §19 |

### 19.2 Decisiones RESUELTAS por el multi-debate (antes abiertas)
- ✅ **Verbo core:** Escoba "sumar 15" como ancla legible **sobre una Mesa viva adversarial** + combinaciones como capa de bonus. (Era 🔶 dec. 2 de v1.0.)
- ✅ **Sistema dual Fullerías vs Pactos:** **SÍ, es el corazón del juego** — y se unifican en la economía de ~3 ranuras de Maña (§7.6). (Era 🔶 dec. 3 de v1.0.)
- ✅ **Ambición:** ÓRDAGO va por **clase mundial** (construir el dual), no por nicho cultural. (LOCK 1 de César.)
- ✅ **Costo de los Pactos Oscuros:** ocupan una ranura de Maña toda la run (§7.6d). (DECISIÓN 3.)
- ✅ **Bucketing del Diablo Fantasma:** humano real, prioridad de grafo social, banda ~5–12% cerrable (§8.1). (DECISIÓN 4.)
- ✅ **Asistencia de UI:** escindida y graduada en 3 capas (§13.1). (DECISIÓN 5.)

### 19.3 Decisiones aún abiertas (para César)
1. 🔶 **Dirección de arte (§11) — el único crux irreducible:** claroscuro boutique vs maximalismo identitario. **Se decide por el test A/B de feed**, no por escritorio. (LOCK 2: A/B.)
2. 🔶 **Título:** ÓRDAGO (Mus, "ir con todo" — muy ownable pero más España/Euskadi) vs **EL ENVITE** / **LA PARTIDA** (más pan-hispano). *Dado tu mercado LatAm + hispanos-USA, sopesar resonancia regional.*
3. 🔶 **Cosmología de palos (§7.1):** afinidades fuertes (definen build, más profundidad) vs ligeras. *Rec. del panel: fuertes; validar en vertical slice.*
4. 🔶 **Recuperabilidad de Pactos:** ¿algún Pacto raro permite recuperar la Fullería empeñada si ganas el Envite? (Variante, no regla base — §7.6d.)
5. 🔶 **¿AZOTH o ÓRDAGO primero?** *Lectura del panel: ÓRDAGO tiene una cuña comercial más clara y barata (mercado hispano desatendido, onboarding más fácil, motor viral social); AZOTH tiene mayor techo de distinción global. Prototipa el que más te jale en un fin de semana de rectángulos y deja que el "una más" decida.*

---

*Fin del macro GDD v1.1. Siguiente paso lógico: micro GDD del prototipo — las **~3 Trampas + 3 Fullerías + 3 Pactos Oscuros** concretos, las fórmulas exactas de Puntos×Suerte, las reglas de siembra de la Mesa viva, las matas con sus valores, y los umbrales de la primera Manga — todo listo para correr el test de kill de recall ≥60% "le hice trampa".*
