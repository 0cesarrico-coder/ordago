# DEBATE ETAPA 2 — ASIENTO: DIRECTOR DE DISEÑO/SISTEMAS (Opus)
Tu ventaja: razonamiento profundo de sistemas y rigor de elegancia (A1). Lidera la PALANCA 2 (el
generador de bifurcación + instrumentación del foso vivo): diséñalo como invariante, no como esperanza.
Pero pronúnciate en las tres y en C-1. Sé el más duro con que la "entrega" no vuelva a ser promesa hueca.

---

=== GDD v1.1 (estado actual) ===

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

---

=== REPORTE DE HUECOS (diagnóstico del workflow; tu insumo) ===

# ÓRDAGO — Huecos de Clase Mundial (Plan de Mejora hacia el #1)

> Árbitro estratégico sobre el GDD v1.1 (`ORDAGO_Macro_GDD.md`).
> Insumo: 93 huecos confirmados (sobrevivieron verificación adversarial).
> Fecha: 2026-06-25 · Estado: priorizado y listo para changelog v1.2.

---

## Resumen ejecutivo

**¿Qué tan lejos está ÓRDAGO del #1 del mundo?** El GDD v1.1 ya tiene un **núcleo de clase mundial defendible**: el sistema dual (Trampa↔Fullería), la economía de Maña de slot único, la Mesa viva adversarial y el Diablo Fantasma social son decisiones correctas, falsadas con kill-tests duros antes de gastar arte. El motor del *foso de diseño* está bien. **Lo que está lejos del #1 no es el verbo: es la CAPA DE ENTREGA.** El documento repite cinco veces "foso viral / CAC~0 / le gané al Diablo de tu primo" y **nunca define el objeto que lo dispara**; declara color funcional pero no lo prueba; invoca cartas de ética/distribución/audio por nombre sin construir el instrumento falsable. El patrón dominante de los huecos de mayor severidad es **valor declarado sin máquina detrás** — exactamente el pecado que la propia v1.1 juró no repetir (la "fantasía hueca" de v1.0).

Tras deduplicar los 93 huecos en **22 temas**, la distribución por prioridad es:

- 🔴 **P1 (mueve la aguja al #1 mundial): 8 temas**
- 🟡 **P2 (pulido fuerte de clase mundial): 9 temas**
- ⚪ **P3 (nice-to-have / refinamiento): 5 temas**

### Las 3 palancas mayores (donde está el #1)

1. **EL ARTEFACTO-PUENTE CANÓNICO (Distribución).** Es el hueco de mayor severidad confirmada (5) y aparece en ~8 huecos distintos. El GDD apuesta TODO su CAC~0 a un motor viral pero el único output especificado es "código de run/build" — el antipatrón literal de D1 (no cruza ningún chat). Sin un artefacto dual (emoji-grid copiable estilo Wordle + clip 6-8s con audio), todo el foso de distribución es humo. **Definir §8.3 "El artefacto-puente de ÓRDAGO" es la mayor palanca de crecimiento del proyecto.**

2. **EL GENERADOR DE BIFURCACIÓN + LA INSTRUMENTACIÓN DEL FOSO (Elegancia/Perdurabilidad).** El foso de elegancia entero descansa en una promesa ("la siembra del Diablo produce ≥2 jugadas correctas") tratada como kill-test a-posteriori, no como invariante diseñada. Hay que (a) diseñar el generador de tensión tempo-vs-escala, y (b) **vigilar la entropía de builds como foso VIVO** en EA (hoy solo se mide una vez en papel). Sin esto, la dominante oculta colapsa el meta a D7-D14 y nadie lo sabe hasta que la retención cae.

3. **LA RECONCILIACIÓN PLATAFORMA↔VIRALIDAD↔ECONOMÍA (Modelo de negocio).** El GDD promete "CAC~0 vía WhatsApp" + "premium Steam $14.99-19.99" sin reconciliar que un link de WhatsApp aterriza en un paywall, sin un solo número de unit-economics (LTV/CAC/payback/neto-tras-30%), y sin auditar la dependencia de plataforma. Es la sección donde el rigor del resto del doc se rompe. **Esto contiene decisiones de César de fondo (web-native vs Steam-first).**

---

## DECISIONES DE CÉSAR (trade-offs reales, no ejecutables sin él)

Antes de la tabla: estos huecos NO se cierran escribiendo texto — implican un trade-off estratégico que solo César decide.

| # | Decisión | Trade-off | Recomendación del árbitro |
|---|---|---|---|
| **C-1** | **Plataforma: web-native-first vs Steam-first** (§15/§16) | Web-native enciende el motor viral real (link→juega), evita 30% de Steam, pero un card-game 2D web es pirateable y pierde el descubrimiento orgánico de Steam. Steam-first da credibilidad premium y descubrimiento pero hace el "CAC~0 WhatsApp" físicamente imposible. | **Híbrido:** Steam como producto premium + **DEMO web gratis ligera** (1 mano contra el Diablo de la semilla) como artefacto-puente jugable que canaliza a wishlist/compra Steam. NO construir el juego entero en web (rompe scope/premium). Resuelve la contradicción sin abandonar el linaje Balatro. |
| **C-2** | **Bajar la promesa vs construir el canal** (§3/§8/§16/§17) | Si C-1 = Steam puro, hay que **borrar "CAC~0"** y reformular como "motor de wishlists / CAC bajo". No se pueden prometer las dos cosas con un stack que entrega una. | Reformular lenguaje (la mitad editorial es gratis). El clip mueve wishlists, no instalaciones gratis. |
| **C-3** | **Multi-nodo cultural vs profundidad mono-nodo MX** (§8.1/§10/§11) | Multi-nodo (Caribe/Cono-Sur) captura 2/3 del corredor hispano-USA Tier-1 pero diluye la identidad ownable y multiplica scope de arte. 1 nodo MX profundo es mayor ROI cultural pero deja afinidad sin capturar. | **Interfaz multi-nodo como DATA desde día 1 + 1 pack MX profundo al lanzamiento.** Construir el slot antes de llenarlo (`cultural_packs[]`). Registrar code-switching como riesgo DISTINTO del blanqueamiento. Packs no-MX = post-EA con consultores del nodo. |
| **C-4** | **Modo run-corta / largo de run por Codicia** (§7.10/§13.1) | Servir a Submission/Relax (run corta) y a la curva de fatiga choca con la "UNA sola escalera comparable" del Diablo Fantasma (decisión LOCK). | NO fragmentar la tabla canónica. Gradar la siembra por Manga (valle Serious Fun) sí; modo separado con su propia tabla, NO. |
| **C-5** | **Título** (§19.3-2) | ÓRDAGO (ownable, España/Euskadi) vs EL ENVITE/LA PARTIDA (pan-hispano). Ya abierto en el GDD. | Sopesar resonancia LatAm + hispanos-USA; cruza con C-3. |
| **C-6** | **Recuperabilidad de Pactos** (§19.3-4) | Variante que suaviza el fausto. Ya abierto. | Mantener como Pacto raro, no regla base. |

---

## Tabla priorizada

### 🔴 P1 — Mueve la aguja al #1 mundial

| # | Tema (huecos fusionados) | § | Por qué NO es clase mundial | Fix concreto al GDD | Carta (confianza) | Sev | Kill / test barato |
|---|---|---|---|---|---|---|---|
| **P1-1** | **El artefacto-puente canónico nunca se define como objeto** (fusiona ~8 huecos: D1 santo grial, share mudo, recall sin artefacto, awe no ionizado, K=i×c, output-no-cruza, doble output grafo/broadcast) | §8.1, §8.2, §18 → **nuevo §8.3** | Declara "CAC~0 / foso viral" 5 veces pero el único output es "código de run/build" = antipatrón D1 literal (necesita explicación, no cruza). Sin artefacto, ninguna capa llega a un jugador nuevo. | Crear **§8.3 "El artefacto-puente de ÓRDAGO"**: DOS outputs <2s/1-tap. (a) **Emoji-grid copiable** estilo Wordle, 0 servidor: fila de palos 🪙🍷⚔️🌳 + Escobas/Trampas-rotas + "le robé el alma a [primo] por X", legible para el grupo, sin spoiler de semilla. (b) **Clip 6-8s/imagen <500KB CON AUDIO** del barrido de Escoba + "¡tramposo!" + firma sonora + handle. Degradar "código de build" a profundidad opt-in del 5%. KPI = **k-factor por segmento**, no MAU. | D1 🟢 + C2 🟢 (K=i×c) + D3 🟢 (audio embebido) | **5** | Prueba del puente: mostrar 0.5s a no-jugador → ¿pregunta "cómo se hizo?". Prueba de spoiler. Correr ANTES de construir. K_grafo<0.2 = el artefacto no cruza → arreglar output antes de gastar en marketing. |
| **P1-2** | **El generador de bifurcación: la emergencia ≥2-jugadas es promesa, no invariante** | §7.3, §14 | Apuesta el foso de elegancia entero a un kill-test a-posteriori ("si no aparece, pivotar"). A1: diseñas el espacio de decisión, no lo esperas emerger. "Sumar 15" sin generador = aritmética de solución casi-única. | En §7.3 documentar **"el generador de bifurcación"** (no como resultado esperado): (1) cada 15 captura un conjunto con VALOR FUTURO divergente → decisión = tempo-vs-escala, no "cuál suma 15"; (2) regla de siembra dura: el algoritmo del Diablo DEBE dejar ≥2 jugadas Pareto-no-dominadas, verificable por solver en papel ANTES del playtest. | A1 🟢/⚪ | **4** | Solver de papel: en 100 tableros sembrados, ≥2 jugadas Pareto-no-dominadas en cada uno. Si converge a 1 dominante → reestructurar siembra. |
| **P1-3** | **El sistema dual no tiene legibilidad visual diseñada** | §7.6, §13.1 | El corazón de v1.1 entrega su estado solo en prosa/diégesis. "Oros no cuentan" debe LEERSE en el tablero (Oros muertos), no memorizarse. A5: fantasía entregada en texto = el cerebro la lee como barata. | Diseñar **lenguaje visual de estado dual**: (1) Trampa activa se manifiesta SOBRE la Mesa (Oros se agrietan/desaturan; "suma 13" reescribe el número-objetivo del HUD); (2) ranuras de Maña distinguen Fullería (forma "tuya") vs Pacto (forma "corrupta") por silueta, y disponible/gastada por estado; (3) el TELL del riesgo como objeto legible (mirada del Diablo, carta que tiembla) que sube ANTES de jugar. | A5 🟢 + C1 🟢 | **4** | Añadir a §14: ¿el tester identifica la Trampa activa y su Fullería disponible **sin leer texto**? |
| **P1-4** | **Cero diseño de la "inversión" Hook + sin trigger de retorno D1/D7 (incl. no-competitivo)** | §8, §8.1, §13 → **nuevo §8.3/§8.4** | Documenta a fondo la COMPRENSIÓN del loop pero nunca cierra el ciclo Hook hacia el retorno. La run reinicia saldo (sin ratchet), el Codex es pasivo, el Diablo Fantasma solo engancha al que YA compite. El KPI "retención 20h+/50h+" no lo entrega ningún sistema. El espinazo Mastery/Submission no tiene trigger. | (1) **"La Cantina del Tahúr"**: guarida persistente amueblada con trofeos diegéticos (expresión-no-poder, inmune a overjustification, crea endowment), sin tocar la pureza de la run; (2) **"El Romancero de hoy"** auto-generado en 1 tap; (3) **"El Diablo de hoy"** reto SOLITARIO diario con sabor (Trampa rara + Pacto), trofeo no ranking; (4) racha **opt-in/rollover** (nunca punitiva, anti-reactancia). | 08-hook 🟢/🟡 + 02-SDT 🟢 | **4** | KPI segmentado por cluster: % retorno D1 atribuible a trofeo vs artefacto vs nada. Si Mastery D7 sin trigger → hábito al azar. |
| **P1-5** | **El test "quita-el-símbolo" (A3, la falsable canónica cultural) ausente del plan de kill** | §14, §18 | El GDD declara "reskin de póker" como su Riesgo nº1 y construye kill-tests para TODO menos para la tesis central de ese riesgo: ¿el mito es carga o decoración? Es posible que la cantina-Posada sea pintura sobre un verbo que viralizaría igual con arte neutro. | Añadir **5º criterio de kill (§14)**: A/B clip mito-ON (cantina+Diablo+folk) vs mito-OFF (mismo loop, arte neutro), midiendo share-rate y deseo de reenvío. Si OFF reenvía igual → el foso vive en el VERBO, recargar identidad en audio/dichos/Diablo. KPIs nuevos §18: "time-to-symbol" y "lift de reenvío mito-on vs mito-off" **por nodo** (piso por nodo, no promedio). | A3 🟡/⚪ | **4** | Reusar el aparato de "test de 3s en feed" de §11: clip temático vs clip neutro del MISMO loop. Barato. |
| **P1-6** | **Steam premium contradice el motor viral WhatsApp/CAC~0 + cero unit-economics** | §15, §16, §3.3 → **nuevo §16.1** | (a) El link de WhatsApp aterriza en paywall de $15-20: el peor CAC, no CAC~0. (b) Cero cifras de física financiera: ni neto-tras-30%, ni refund, ni conversión wishlist→venta, ni payback. El precio de góndola se confunde con un modelo. **DECISIÓN DE CÉSAR (C-1, C-2).** | **§16.1 "Unit economics B2P de 3 columnas"** (USA/hispanos-USA/LATAM): precio NETO (-30% Steam), refund ~8-12%, conversión wishlist→venta (10-20% launch), CAC-por-wishlist por canal, payback. Separar **loop social intra-juego** (retención) de **loop de adquisición** (wishlists con CAC>0). Resolver C-1 (demo web ligera). Reescribir §18 KPIs a B2P. | L3 🟢/⚪ + L7 🟢 + D1 🟢 + B5 🟢 | **4** | Gate L4: no se sube a vertical slice sin modelo de payback escrito y **LTV/CAC ≥3 proyectado por columna**. |
| **P1-7** | **El foso de elegancia se valida en papel pero no se vigila como foso VIVO** | §14, §18 | A1 exige medir el foso EN EL TIEMPO. §14 mata una vez en prototipo; §18 mide retención pero NINGÚN KPI mide entropía de builds por cohorte ni brecha skill. La dominante oculta colapsa el meta a D7-D14 sin alarma. | Añadir 2 KPIs de foso a §18 desde EA: (1) **Entropía de builds por cohorte semanal** (combinaciones de Maña + rama de Jugada); salud = estable/creciente D7→D14→D30; colapso = pasada de balance (matar dominante con trade-off, no nerf). (2) **Test del experto** en vertical slice: mismo seed/build a novato y experto deben divergir en score; si convergen, no hay techo. Usar el Diablo Fantasma (banda 5-12%) como proxy de brecha-skill (descartar solver completo, intratable). | A1 🟢 | **3→ P1 por apalancamiento** | Entropía cae bajo umbral = alarma de elegancia. Novato vs experto convergen = añadir profundidad oculta (lenticular). |
| **P1-8** | **El "discovery frame"/key-art no es spec del día 0 + A/B decide paleta sin gate de legibilidad de estado** | §11, §13, §18 | El único crux (arte) se zanja por CTR de feed pero NUNCA prueba si la paleta ganadora deja LEGIBLE Suerte/Puntos/Manos ni si sobrevive daltonismo/downscale. Una Mesa viva densa se vuelve papilla a 100x100px. Para un card-game (peor caso C1: acción no legible como en un runner) esto mata la ignición broadcast. | Convertir el A/B de §11 en **test de 2 ejes con gate gatekeeper**: cada paleta debe PASAR primero un **glance/colorblind gate** (HUD + frame a 100x100px gris + simulación protan/deutan/tritan; juez nuevo nombra Puntos/Suerte/Manos/Reales <0.5s) como requisito de elegibilidad; solo las que pasan compiten por CTR. Restricción dura al lado B maximalista: jerarquía de valor (saturado solo en lo accionable). Definir el key-art/capsule canónico de Steam. | C1 🟢/🟡 + A5 🟡 | **3→ P1 por apalancamiento** | Glance gate verde/amarillo/rojo: <90% reconocimiento de estado = rediseñar. KILL si el HUD no es legible en gris (estado depende solo de color). |

### 🟡 P2 — Pulido fuerte de clase mundial

| # | Tema | § | Por qué NO es clase mundial | Fix concreto | Carta (confianza) | Sev | Kill / test |
|---|---|---|---|---|---|---|---|
| **P2-1** | **Color funcional es punto único de fallo para daltónicos + acento de palo colisiona con los 4 colores de estado** | §10, §7.1, §13, §14 | "color = etiqueta sin labels" mapea 4 canales críticos a color puro. Rojo(Suerte)/Verde(Manos) = el peor par deuteranopía (~8% de hombres = millones del sweet-spot). Y Oros/Espadas/Bastos reusan los hues de estado → ambigüedad cromática en máxima carga cognitiva. | Reescribir §10: **"color = canal REDUNDANTE, nunca único"**. Doble-codificación: Puntos=azul+glifo moneda; Suerte=rojo+aspa "×"; Manos=verde+pips contables; Reales=oro+"R". ≥3 paletas con tokens (separación de LUMINANCIA ≥40). Regla dura: los 4 hues funcionales son sagrados; el palo vive en FORMA/icono, no en re-teñir. Glance/colorblind gate en CI (§15). | A5 🟡 + C1 🟢 | 3+3+3+2 | Render HUD a gris + simulación daltónica: juez nombra los 4 canales y lee valor de carta. |
| **P2-2** | **El "pillado" 15% es dado plano, no arco de tensión/near-miss; azar punitivo en core loop** | §7.6b, §6.2 | El "te pillé" es emoción declarada central pero se entrega como coin-flip oculto. Carta 10: el arco tensión→alivio exige riesgo LEGIBLE construido como curva, no RNG instantáneo. Carta 05: azar va en META, no en CORE. Falta el 3er estado: "casi te pilla". | Convertir la Fullería en **mini-arco de 3 tiempos**: (1) ANTES — barra de **Sospecha** visible que sube con señales que el jugador controla (cuántas Fullerías usaste, repetir truco, ir ganando mucho); riesgo DECIDIBLE; (2) DURANTE — 1-2s diegéticos (el Diablo entrecierra ojos); (3) DESPUÉS — incluir estado **near-miss** ("te la paso, tahúr") mostrando cuán cerca estuvo. El % = función de Sospecha, no dado fijo. **Descartar** escalado punitivo de Sospecha (death-spiral). | 10 🟢/🟡 + 05 🟢 + 01 🟢 | 2+3+3 | Si testers usan Fullería en >90% de Trampas-que-muerden → decisión muerta. Subir escala hasta ~50-70% de uso. |
| **P2-3** | **El castigo del pillado no escala ni ancla a dotación; falta el ALIVIO recompensado** | §7.6b, §7.6d, §10 | "Pierdes la mano / carta corrupta" es plano: trivial en Manga 4 (sumas miles). Carta 06: la pérdida muerde 2× y exige DOTACIÓN (perder algo que SIENTES tuyo). Y el resultado dominante (~85% colar la Fullería) se vive como no-evento en baseline (carta 00). | (1) Castigo anclado a dotación: confiscar la mejor carta capturada del Envite / corromper un Pacto equipado, no "la mano" abstracta. (2) **"Cobro con dignidad"**: opción de SACRIFICAR algo voluntario para que cuele ("le tapas la boca al Diablo") = decisión faustiana. (3) Diseñar el **ALIVIO como evento de juice** (no ausencia de castigo): guiño cómplice, exhalación de cantina, escalado por la Sospecha aguantada. | 06 🟢 + 10 🟡 + 00 🟢 | 3+3 | (Cuidado: % del score escalado choca con Puntos×Suerte limpio y arriesga death-spiral; preferir ancla a dotación + sacrificio voluntario.) |
| **P2-4** | **Andamiaje meta-lúdico C3: seed reproducible + verbos conmutables + sello de reto** | §8.2, §13.1, §14 → **§8.3** | C3 (la comunidad genera el D30+) es LA palanca de un premium sin treadmill. Falta: seed 100% determinista (misma semilla → misma siembra del Diablo), verbos como flags verificables ("0 Fullerías"), sello de reto legible. La Mesa viva con estado, si no es determinista, hace los retos infalsables. | Requisitos duros desde el prototipo: (1) **siembra 100% determinista por seed** (RNG del Diablo derivado de la semilla) — test: 2 runs misma seed = mismo tablero turno a turno; (2) estado-de-run serializable (el código reconstruye la partida exacta); (3) verbos/Fullerías como flags conmutables para verificar retos por código + sello compartible. Separar **2 planos de tabla**: canónica (intacta) + "Retos del Romancero" (tablas ortogonales auto-verificadas). 3-5 retos-semilla oficiales del estudio. | C3 🟢 + A1 🟢 | 3+3+3 | MUST-FIX: determinismo de siembra + run-state serializable. El resto (sello, retos oficiales) = post-1.0. |
| **P2-5** | **Audio como sistema de marca: falta firma sonora + grito imitable** | §10, §11, §5 → **§10.1** | Todo el audio vive en el juice stack (frame), no en identidad/transmisión. Cero firma sonora (audio logo 2-3 notas), cero grito imitable. D3: el audio icónico es el foso más barato/perdurable; en LATAM el juego es SONORO antes que visual. El clip viral se comparte mudo (§18 mide share, no share_with_audio). | **§10.1 "Firma sonora"**: 2-3 notas ≤3s sobre timbre folk-barroco (campana grave + jarana), CONGELADA como activo de marca, suena en splash + Última Mano + final del clip. **Grito imitable** ≤1.5s ligado al verbo de trampa (que RIME con "hacerle trampa", NO "¡ÓRDAGO!" que significa all-in en Mus) + canto del Diablo-gritón al imponer Trampa. Exportador de clip SIEMPRE con audio. KPI: share_with_audio. | D3 🟢 + 🟡 | 3+3+3 | Test de earworm: 24-48h ≥30% tararea la firma sin pista. Test del chat de voz: ≥50% repite el grito al 1er intento. |
| **P2-6** | **People Fun (co-op/colaboración) y reciprocidad social ausentes; capa social = 100% competición** | §8.1, §8.2 | Ambas patas de Action-Social son la MISMA competición vestida distinto. People Fun (1.8× shares LATAM) y reciprocidad ("pase y devuelve", Fehr&Gachter) sin sistema. Regalar-sin-devolver = deuda en el grafo LATAM. | (1) **"Pasar la Mano"**: heredas la mesa/semilla donde un amigo perdió; si la ganas, AMBOS reciben recompensa (cooperación asíncrona). (2) Objetivo de gremio/familia compartido semanal (barra común). (3) Contador de reciprocidad + cosmético de cantina COMÚN para el par. **Podar** el "amuleto regalable" que altera la run del amigo (choca con scores reales/UNA escalera). | LD4 🟢/🟡 + 03 🟢 | 2+2 | El clip colaborativo ("mira lo que me dejó mi primo") debe viajar distinto al de dominancia. |
| **P2-7** | **Curiosidad/SEEKING: el Codex no muestra huecos visibles + secretos sin gap cerrable + onboarding no enciende antes de enseñar** | §8, §7.6c, §13 | "Mapa de Discovery" que solo lista lo hallado = trofeo retrospectivo, no motor SEEKING (Loewenstein: sin hueco percibido no hay curiosidad). Secretos "estilo Soul/Legendary" sin pista = secreto-wiki. Onboarding optimiza velocidad pero no abre info-gap antes de enseñar (Gruber). | (1) Codex como **GRID DE HUECOS**: silueta ennegrecida + 1 pista diegética + condición aproximada (no receta). (2) Arquitectura de revelación en 3 escalones: hueco mostrado → pista near-miss al rozar la condición ("el gap es cerrable") → revelación juicy. Regla dura: **prohibido el secreto-wiki** (todo deducible de pistas in-game). (3) Onboarding: elevar la siembra-como-tell del Diablo (carnada §7.3, ya existe) a gancho de curiosidad explícito antes del 1er "sumar 15". | LD5 🟢 | 3+3+2+2 | KPI: % que abre Codex y luego intenta cerrar un hueco concreto en la run siguiente (intencionalidad SEEKING). |
| **P2-8** | **Juice estratificado por frecuencia + tope anti-Extremo + responsividad como gate + accesibilidad de motion** | §10, §7.7 | §10 es catálogo de efectos sin jerarquía por rareza (si todo tiembla, nada importa). Cascadas exponenciales sin techo de juice (U-invertida Kao: el Extremo PERJUDICA/marea). Cero presupuesto de latencia (Vlambeer #1: ningún juice salva un control flojo). Sin reduce-motion/flashing (cert. de consola, WCAG 2.3.1). | (1) **Escala de juice de 4 tiers** anclada a frecuencia (T0 selección sutil → T3 cascada/Mata <5% de eventos; ~80% en T0-T1). (2) **Coalescencia + techo duro** de shake/flash en cascadas (crescendo, no N golpes; x100 y x10000 difieren en sonido, no en temblor). (3) **Presupuestos de latencia**: tocar <50ms, suma/preview <80ms, Escoba <100ms. (4) **Panel de accesibilidad de feel** (slider shake, reduce flashing WCAG, reduce motion) — solo cosmético, cero impacto en score. | 09 🟢 (Kao/Vlambeer/Swink) | 3+3+3+3 | Smoke-test de frame-time del ciclo selección→suma antes del arte. Si testers reportan mareo en cascadas → bajar de Extremo a Alto. |
| **P2-9** | **Curva de fatiga/arco de sesión macro: presupuesto de run + telemetría de fatiga + cierre digno** | §6.2, §6.3, §7.10, §18 | Micro-ritmo definido (30-45s) pero cuánto dura la Partida (12 apuestas) nunca se declara: ~40-70min sin curva de fatiga. §7.10 sube apuesta y Trampa monotónicamente. Sin estado terminal/anti-burnout en los loops infinitos (Condena endless, escalera "siguiente Diablo"). | (1) Declarar **presupuesto de run** (~25-35min/Partida ganada) y curva serrada (Cantina = valle real; Envite = pico; Manga 4 = pico máximo audible). (2) **Telemetría de fatiga** en §18: abandono por apuesta#, degradación de decisión/seg intra-run. (3) **Cierre digno**: beat de catarsis post-victoria que da permiso de PARAR; en Condena, celebrar antes de ofrecer reintento; racha opt-in/rollover; KPI-centinela de saciedad (% para satisfecho vs encadena). | 10 🟢/🟡 + 04 🟢 + 06 🟢 + LD7/M1 | 3+2+2 | (Mucho ya cubierto: run finita, valles existen, M1/LD7 en borde de run. El delta real = telemetría de fatiga + cierre como momento de 1ª clase.) |

### ⚪ P3 — Nice-to-have / refinamiento

| # | Tema | § | Por qué | Fix | Carta | Sev | Kill |
|---|---|---|---|---|---|---|---|
| **P3-1** | **Economía de Maña: build dominante latente + el 15% como decisión dominante** | §7.6b, §7.6d | Pactos (poder compuesto) dominan EV de Fullerías (utilidad puntual). El §14 YA testea diversidad de builds (kill #2). Riesgo real de números, pero el detector ya está cableado. | Hacer Fullerías y Pactos NO comparables (se necesiten mutuamente: Pacto auto-saboteador ↔ Fullería que lo destraba) y Fullerías escalables. Riesgo escalado por uso (5%→20%→40%). | A1 🟢 | 3+2 | Solver mide entropía de builds ganadoras; si converge a "max Pactos" → reestructurar antes del arte (kill #2 §14, ya existe). |
| **P3-2** | **Las Jugadas excluyentes podan combinatoria en vez de abrirla** | §7.4 | Excluir tipos de Jugada es el movimiento opuesto al de Balatro (cualquier Joker combina con cualquiera). §7.6d ya cubre la firma vía slot scarcity → la exclusión de §7.4 es redundante además de dañina. | Mover la exclusividad del nivel Jugada al nivel **Pacto/ranura** (ya escaso). Jugadas todas combinables = sustrato multiplicativo. Añadir Pactos que premian MEZCLAR Jugadas. | A1 🟢 | 3 | Test del experto: mismo set de reglas, ≥2 builds distinguibles divergentes por skill. |
| **P3-3** | **Endgame (Codicia + Condena) sub-especificado para las 50h+; balance exponencial sin techo** | §7.10, §8, §9 | KPI 50h+ entregado por una línea cada uno. "Trampas más crueles" sin especificar = escalado aritmético (falsa competencia). Pero §14 lo difiere a post-EA conscientemente. | Codicia como **ladder cualitativa** (cada escalón = regla nueva que cambia la DECISIÓN, no +%): I=1 Bloqueo extra, III=2 Trampas apiladas, V=Fullerías +Sospecha, etc. Soft-cap diegético al runaway ("el Diablo iguala la apuesta"). Cada escalón = desbloqueo de Codex. | 01 🟢 | 3+2 | Kill cuantitativo: ningún arquetipo >X% de runs ganadoras a Codicia alta. Atar a UNA tabla comparable (no fragmentar). |
| **P3-4** | **Modo Condena endless + Diablos del Romancero sin motor de renovación ni mitología** | §7.10, §8.1 | Condena = "más de lo mismo infinito" (consume vs renueva). Diablos del Romancero = nombre+rostro sin mundo (lore sin cohesión = decorado, no A4). Ambos diferidos a post-EA. | (1) Condena: cada nivel = modificación ESTRUCTURAL del espacio (nuevo patrón de siembra / Trampa compuesta), no +dificultad. (2) Diablos del Romancero = **bestiario de ~12-20 arquetipos** (memory palace tipo Lotería) con flavor ambiguo + Trampa-firma + entrada de Codex + relaciones insinuadas. Reusa pipeline Posada. | A1 🟢 + A4 🟢 + C3 🟢 | 2+2 | Si entropía de builds en Condena colapsa → la modificación estructural de ese nivel falló. |
| **P3-5** | **Onboarding/retención no-hispano: doble alcance afirmado, nunca diseñado** | §13, §7.5, §3.2, §18 | Audiencia SECUNDARIA (China >1/3 del género aprende sistemas ajenos), riesgo "Baja" auto-declarado. Pero la baraja desconocida se trata como FRICCIÓN, no como info-gap a explotar; competencia cultural se ENTREGA (overjustification) en vez de ganarse; doble alcance solo se mide (§18) sin canal broadcast. | (1) First-contact no-hispano: cold-open de 8s con UNA trampa absurda visible + Matas como siluetas-fantasma desde el min 1 (segmentado/skippable). (2) Matas se DESCUBREN por captura (competencia informacional), no por tooltip. (3) Convertir el KPI §18 en objetivo con kill-criterion: si retención D7 no-hispano < X% del hispano → replegarse a "el Balatro hispano". | LD5 🟢 + 02-SDT 🟢 | 3+3+3 | % no-hispanos que nombran espontáneamente una Mata tras 3 runs (competencia ganada, no dada). |

---

## Temas de PROCESO/ARQUITECTURA transversales (integrar en v1.2, no son filas sueltas)

Estos huecos sobreviven pero son **contratos de diseño/instrumentación** más que features:

- **Tabla de asignación 3-motores/3-frecuencias (Ley 1)** → nuevo **§4.1**: una fila por sistema (Escoba/ASMR, duelo de trampas, economía de Maña, Pactos/cascada, Diablo Fantasma, Codex, Última Mano) × (frecuencia D1-D7/D7-D14/D30+ × superficie × peso 90/10). Contrato: ninguna feature pasa code-review si viola su fila. *(Sev 3)*
- **Los dos relojes de retención** → nota de arquitectura en **§19**: Reloj A (D1-D7 = Diablo Fantasma + daily, ya existe) ≠ Reloj B (D30+ = profundidad/Codicia/Codex/Condena, también existe). Regla: NO pedirle al Diablo Fantasma el trabajo D30+, NO meter profundidad de 30 días en la cita diaria. *(Sev 2 — es articulación, no sistema faltante; NO importar temporadas live-ops a un premium)*
- **T0/time-to-first-value instrumentado + linter anti-gate (Ley 2)** → **§13/§15**: renombrar "comprensión <90s" a `time_to_first_escoba` (ms hasta el primer juice), gate por percentil; linter de build que falle si hay cutscene/lore/tutorial no-skippable antes de la 1ª mano (materializa "cero lore dump" como regla verificable). *(Sev 2)*
- **Money-shot de temporada reutilizable (A2)** → post-1.0: presentador de money-shot con SLOT de contenido rotado por calendario latino (Día de Muertos, etc.), disparador espaciado (NO onRunWin), reusa el motor. *(Sev 2 — enriquecimiento post-lanzamiento; la perdurabilidad real ya vive en Diablo Fantasma + seeds, no en la animación de victoria)*
- **Físca del loop viral K=i×c instrumentada (C2)** → **§18/§14**: 4 eventos con referrer broadcast-vs-grafo, objetivo K_grafo 0.3-0.7, tiempo de ciclo, gate de retención D1-D7 de los traídos por share ANTES de escalar UA (anti-fuego-de-paja). Traducir a premium: evento terminal = clip→wishlist→compra, no install gratis. *(Sev 3)*
- **Matriz de UA por segmento (C2)** → **§17**: USA→broadcast/Shorts; LATAM→fricción-cero WhatsApp; hispanos-USA→"Instagram enciende / WhatsApp quema". No asumir piso eCPM LATAM para todo el corredor. *(Sev 2)*
- **Estado de ventana del subgénero (L6)** → **§3.2.1**: clasificar el roguelike-deckbuilder como "abierto-pero-comoditizándose post-Balatro"; articular por qué la puerta sigue abierta PARA ÓRDAGO (cultura+verbo, no skin) y cruzar con el break-even. Riesgo "saturación de Balatro-likes" en §19. *(Sev 2)*
- **Mapa de dependencias de plataforma (L7)** → **§15**: por cada apoyo (descubrimiento/pago/leaderboards), "¿qué pasa si la regla cambia mañana?". Leaderboards en backend propio (no solo Steamworks) para que el Diablo Fantasma funcione fuera de Steam. Añadir "dependencia de plataforma" a §19.1. *(Sev 3)*
- **Overjustification en el meta-loop (02-SDT/CET)** → **§6.4/§18**: autonomía sobre la recompensa (elegir entre 3), recompensas inesperadas vs contingentes, extender "sin ratchet ni FOMO" explícitamente al Diablo Fantasma/daily, KPI-centinela "reclamar puesto" vs "jugar otra mano". *(Sev 3)*
- **FTUE: graduar la incertidumbre por Manga + guion de primer contacto RPE+** → **§13/§14**: gatear Bloqueo (solo desde Manga 2) y la 1ª inversión de regla (tras superar el 1er Envite), documentar curva de incertidumbre por Manga; guion de casi-fracaso→golpe de suerte en sesión 1 (reconciliar con la cohorte de falsación del recall §14). *(Sev 3 — descartar "regalar la 1ª Fullería / sacar Maña de la run 1", retrasa la fantasía core)*
- **Rival sintético de cold-start con etiquetado honesto (M1/LD7)** → **§8.1**: vencer un Diablo del Romancero es flavor-only (NO cuenta como "liberaste el alma de [humano]" ni entra en la tabla comparable); "score de percentil" derivado de curva pública documentada en el Codex. *(Sev 2 — descartar la saciedad terminal forzada que daña el cold-start)*

---

## Changelog sugerido para GDD v1.2

**Nuevas secciones:**
- **§4.1** — Tabla de asignación de motores (contrato de frecuencia/superficie).
- **§8.3** — El artefacto-puente de ÓRDAGO (P1-1, el santo grial) + andamiaje meta-lúdico C3 (P2-4) + loop de retorno D1/D7 (P1-4).
- **§10.1** — Firma sonora + grito imitable (P2-5).
- **§16.1** — Unit economics B2P de 3 columnas (P1-6).
- **§3.2.1** — Estado de ventana y capturabilidad (L6).

**Reescrituras:**
- **§7.3** — Documentar "el generador de bifurcación" como invariante diseñada, no resultado esperado (P1-2).
- **§7.6 / §13.1** — Lenguaje visual de estado del sistema dual + barra de Sospecha (P1-3, P2-2, P2-3).
- **§10** — "color = canal REDUNDANTE, nunca único" + escala de juice de 4 tiers + techo anti-Extremo + presupuestos de latencia + panel de accesibilidad de feel (P2-1, P2-8).
- **§11** — A/B de 2 ejes con glance/colorblind gate como gatekeeper + discovery frame/key-art canónico + (decisión C-3) interfaz cultural multi-nodo como data (P1-8).
- **§8 / §8.1** — Codex como grid de huecos + arquitectura de revelación de secretos (P2-7) + People Fun/reciprocidad (P2-6) + etiquetado honesto del rival sintético + ADN narrativo en el artefacto.
- **§15 / §16** — Reconciliar plataforma↔viralidad (C-1/C-2), mapa de dependencias (L7), demo web ligera, leaderboards en backend propio.
- **§13** — `time_to_first_escoba` + linter anti-gate + curva de incertidumbre por Manga + onboarding no-hispano/curiosidad (P3-5).

**Ampliaciones de §14 (criterios de kill):** +legibilidad del sistema dual sin texto · +5º criterio cultural quita-el-símbolo · +glance/colorblind gate.

**Ampliaciones de §18 (KPIs):** entropía de builds por cohorte · brecha skill/test del experto · time-to-symbol + lift mito-on/off por nodo · k-factor por segmento · share_with_audio · telemetría de fatiga · KPI-centinela de saciedad · KPIs B2P (wishlist→venta, refund, CAC/payback).

**Decisiones a marcar para César en §19.3:** C-1 plataforma (web-native vs Steam-first), C-2 bajar promesa vs construir canal, C-3 multi-nodo cultural, C-4 run-corta/largo por Codicia.

---

## FRAMEWORKS / DOCTRINA (anclas verificadas — cítalas con su confianza 🟢/🟡/⚪)

> Fuente: game-design-brain (biblioteca de diseño verificada). Cada juicio de craft/valor debe
> citar la carta que lo respalda (A1–A5, LD0–LD7, M1) o declararse opinión sin respaldo (⚪).
> Disciplina epistémica: 🟢 literatura verificada · 🟡 canónico/señal · ⚪ razonamiento. Jamás
> ascender un 🟡 a 🟢. Todo 🟡/⚪ empírico lleva "validar en cohorte propia".

### Cartas de diseño (capa Craft)
- **A1 — Elegancia / emergencia (🟢🟡):** diseñas el *espacio de decisión, no el contenido*.
  Pocas reglas con **trade-offs reales** y consecuencia perceptible (<1 s) → profundidad
  emergente que se renueva gratis cada partida. Es el ÚNICO foso anti-envejecimiento que un
  estudio pequeño puede pagar. Test: ¿mata la opción dominante? ¿la decisión se renueva cada run?
- **A2 — Asombro / awe (🟡):** el awe **se habitúa** al repetirse → NO es motor diario; es un
  *money-shot de temporada*, espaciado, diseñado para GRABARSE/compartirse, nunca en el T0. En
  el pico de awe el call-to-action es compartir, no comprar.
- **A3 — Mito comprimido (🟡⚪):** un juego de clase mundial **invoca** su mito, no lo narra. Un
  símbolo pre-cacheado (La Muerte, el Diablo, el tahúr) carga siglos de connotación en <1 s. Carga
  cultural en la SUPERFICIE (skin/carta/grito), lore como profundidad opcional. "Si necesitas
  tutorial de mito, muere en WhatsApp." Reconocible <1 s o falla.
- **A4 — Narrativa embebida (🟢🟡):** el mundo cuenta por disposición/objetos/causa-efecto; la
  **ambigüedad deliberada** es feature (obliga a teorizar → UGC). Regla inviolable de no-peaje:
  CERO lore obligatorio antes del primer momento jugable; lore = capa opcional para el ~5%.
- **A5 — Estética-sistema (🟡):** la estética clase-mundial es un **sistema de legibilidad**
  (silueta → valor → color), no fidelidad: comunica qué-es/qué-hace antes de procesar color/detalle.
  Gate: test de silueta en negro puro. Foso que se gana con criterio, no con presupuesto.

### Lentes (cobertura emocional — jerarquía dura)
- **LD0 (🟡):** una lente es una **pregunta-checklist de cobertura**, NO una teoría que predice
  diversión. Jerarquía: **Quantic Foundry (🟢) primaria → Lazzaro (🟡) check de experiencia →
  MDA (🟡) checklist final**. Nunca cites MDA/Bartle como ciencia.
- **LD3 — tipos de jugador (🟢):** el modelo válido es **Quantic Foundry** (Yee, N>466k, factorial,
  replicación cross-regional): **12 motivaciones / 6 pares / 3 clusters**. **Bartle está muerto
  factorialmente** ("Explorer" no se reproduce) — úsalo solo como léxico. Discovery vive bajo
  **Creativity**, no Immersion. Los 3 clusters: **Action-Social** (Destruction/Excitement +
  Competition/Community), **Mastery-Achievement** (Challenge/Strategy + Completion/Power),
  **Immersion-Creativity** (Fantasy/Story + Design/Discovery).
- **LD4 — lente de cobertura (🟡):** audita en 3 pasos (rejilla primaria QF-clusters → Lazzaro →
  MDA). Hueco = cluster sin sistema. Cobertura **"amplia pero superficial"** (cada jugador ≥1
  motivación servida). En LATAM/hispanos-USA: **Submission/Relax RETIENE el core loop; Competición
  social asíncrona es CO-DRIVER**, no extra. Datos de engagement MX 2025-26: Action-Social 41% >
  Submission/Relax 32% > Mastery-Achievement 27% > Discovery 24% > Immersion-Creativity 18%.
- **LD2 — Lazzaro 4 Keys (🟡/🟢):** Hard Fun (Fiero, orgullo de triunfar) · Easy Fun (curiosidad) ·
  Serious Fun (relajación/cambio de estado) · People Fun (socialización).
- **LD1 — MDA 8 estéticas (🟡):** checklist final de "¿olvidé un tipo de placer?", no modelo.
- **LD5 — curiosidad/SEEKING (🟢):** la curiosidad es driver neuroquímico primario
  (SEEKING/Panksepp → information-gap/Loewenstein). Engancha el hueco de descubrimiento.
- **LD6 — competición/dominancia (🟢/🟡):** en LATAM/hispanos-USA la competición social
  asíncrona/familiar es CO-DRIVER (64-71% de comentarios de contenido viral = rivalidad). Base
  Festinger: motiva cuando el gap es cerrable. Diseñar async/bucket leaderboards.

### Gates éticos (piso inviolable del valor)
- **M1 — Goodwill como cuenta con saldo (🟢🟡⚪):** cada mecánica deposita (generosidad, ritual,
  transparencia) o retira (FOMO fabricado, mito-peaje, ad forzado); el saldo NETO de cada sistema
  debe ser positivo. Monetizas por pertenencia, no por adicción.
- **LD7 — curiosidad vs compulsión (🟢/🟡):** la frontera es la **saciedad alcanzable**. Sana =
  gap cerrable + cierre que satisface + estado terminal (Kang 2009). Compulsión = diseño que
  IMPIDE la saciedad (re-abre el gap con FOMO/timers explotando "wanting > liking"). Ninguna
  propuesta de valor puede basarse en violar M1 ni LD7: eso no es valor, es extracción.

---

## DEBATE ETAPA 2 — Afilar los FIXES de clase mundial (eje: DISEÑO + ENTREGA, no research de negocio)

Un workflow de 135 agentes ya cazó 93 huecos de clase mundial en el GDD v1.1 de ÓRDAGO (roguelike
deckbuilder con baraja española; verbo = hacerle trampa al Diablo en una Mesa viva). El diagnóstico:
el VERBO ya es clase mundial; lo que está lejos del #1 es la CAPA DE ENTREGA — "valor declarado sin
máquina detrás". Tu trabajo NO es re-encontrar huecos: es **debatir y converger en los MEJORES FIXES**
para las 3 palancas mayores, a vara de "el mejor juego del mundo". Aprovecha tu ventaja de datos/prior.

### LAS 3 PALANCAS A AFILAR (+ 1 decisión de César)
1. **PALANCA 1 — El artefacto-puente canónico (§8.3 nuevo).** El GDD apuesta TODO su CAC~0 a la
   viralidad pero el único output hoy es "código de build" (antipatrón D1: no cruza ningún chat). Hay
   que definir el OBJETO exacto que dispara el crecimiento. Pregunta dura: ¿qué se comparte y se GUARDA
   de verdad en WhatsApp/IG/TikTok entre hispanos (LATAM + hispanos-USA)? ¿Un emoji-grid copiable estilo
   Wordle (0 servidor)? ¿Un clip 6-8s con audio del barrido + "¡tramposo!"? ¿Ambos, y cuál primero?
   ¿Cómo se evita el spoiler de semilla? ¿Cómo se ata a "le robé el alma a [tu primo]"? (Cartas D1, C2 K=i×c, D3 audio.)
2. **PALANCA 2 — El generador de bifurcación + el foso VIVO.** La elegancia (A1) hoy es una promesa
   ("la siembra del Diablo produce ≥2 jugadas correctas") tratada como kill-test a-posteriori, no como
   invariante diseñada; y nadie vigila la entropía de builds en el tiempo (la dominante oculta colapsa
   el meta a D7-D14 sin alarma). ¿Cómo se DISEÑA el generador (tempo-vs-escala, valor futuro divergente
   de cada captura) para garantizar ≥2 jugadas Pareto-no-dominadas? ¿Qué instrumentación vigila el foso
   vivo en EA (entropía de builds por cohorte, test del experto)? (Carta A1.)
3. **PALANCA 3 — Reconciliar plataforma↔viralidad↔economía (§16.1).** "CAC~0 vía WhatsApp" + "premium
   Steam $15-20" se contradicen (el link aterriza en paywall) y no hay un solo número de unit-economics.
   ¿Cuál es el modelo que de verdad cierra para LATAM + USA + hispanos-USA? Aterriza cifras realistas:
   precio neto (-30% Steam), conversión wishlist→venta, refund, CAC por canal, payback, LTV/CAC por
   columna (USA / hispanos-USA / LATAM). (Cartas L3 unit-economics, L7 plataforma, D1, B5 fricción-cero.)
4. **DECISIÓN DE CÉSAR C-1 (informarla, no zanjarla):** web-native-first vs Steam-first vs híbrido
   (Steam premium + demo web ligera de 1 mano como artefacto-puente jugable). ¿Cuál maximiza llegar al
   #1 sin romper el linaje premium ni el motor viral? Da tu recomendación con su porqué y su trade-off.

### REGLAS
- Especificidad obligatoria: cifras, rangos, ejemplos concretos; si no tienes un dato, dilo.
- Jerarquía de evidencia: L1 data real de plataforma (Meta Ads/analytics) > L2 industria citable >
  L3 patrón de entrenamiento > L4 razonamiento. Etiqueta tus afirmaciones empíricas 🟢/🟡/⚪ y marca
  el nivel; "validar en cohorte propia" donde aplique. No fabriques certeza.
- Ancla los juicios de diseño a las cartas (A1, D1, C2, D3, L3, L7, B5, M1·LD7) con confianza.
- Mercado: LATAM + USA general + hispanos-USA (sweet spot). Modela por segmento, no asumas piso LATAM.
- Piso ético M1/LD7 inviolable (nada de FOMO fabricado / compulsión como motor de viralidad).
- Falsabilidad: cada fix con (a) el cambio concreto al GDD, (b) criterio de kill, (c) el test más barato.

### FORMATO DE SALIDA — RONDA 1
Para CADA palanca (1, 2, 3): tu **mejor fix de clase mundial** (concreto, anclado, con cifras donde
puedas), el **riesgo principal + mitigación**, y el **test/kill más barato**. Luego tu **recomendación
sobre C-1** (web/Steam/híbrido) con porqué y trade-off. Cierra con tu **apuesta falsable**: "ÓRDAGO no
llegará al #1 a menos que ___." Sé un red-team honesto, no un validador.
