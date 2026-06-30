# ÓRDAGO — Macro Game Design Document

> *La partida contra el Diablo.* Un roguelike deckbuilder con baraja española.
> Working title: **ÓRDAGO** · Alternativas: *EL ENVITE*, *LA PARTIDA*, *NAIPE*
> Versión: 0.1 (macro / north-star) · Autor: César · Estado: propuesta para validación

> **Nota — documento hermano de AZOTH.** ÓRDAGO comparte la *doctrina de diseño* de AZOTH: el juice stack como producto, el marco Bartle×MDA, el modelo premium sin MTX, la filosofía "rectángulos primero", la cobertura asíncrona de arquetipos sociales y la decisión de engine. Aquí se detalla **solo lo propio de ÓRDAGO**; donde la doctrina es idéntica se referencia y no se re-deriva. Son dos apuestas distintas dentro del mismo lenguaje de diseño.

---

## 1. Vision Statement

**ÓRDAGO es el Balatro del mundo hispano.**

Donde Balatro tomó la baraja francesa (póker) y AZOTH tomó un sistema no-de-cartas (alquimia), ÓRDAGO toma **la baraja española** — el mazo de la mesa de cocina de México, LatAm y España — y le aplica el motor que define al género: score-chase exponencial, estructura roguelite y feedback hiper-juicy.

Pero su verbo central **no son manos de póker**: es el **Escoba** — formas jugadas que suman **15** para hacer *Escobas* (barridas) que puntúan, mientras encadenas combinaciones y capturas las cartas mayores. Sumar 15 es tan inmediato como el 21 del blackjack, y es una mecánica genuinamente distinta a la de las manos.

Todo envuelto en un cuento folk: **una partida de naipes contra el Diablo por tu alma**, ambientada en una cantina barroca a la luz de velas. Cada *run* es una mano contra el Diablo; cada umbral es el Diablo subiendo la apuesta; ganar la Partida es recuperar tu alma. El número-que-sube tiene aquí un significado de cuento popular: el del **tahúr/pícaro que vence al Diablo con maña y agallas**.

**La tesis comercial (lo que lo distingue de AZOTH):** AZOTH compite por white space *estético* global. ÓRDAGO compite por white space *cultural y de mercado*: el género, en pleno boom, está dominado por la baraja francesa, lo abstracto y lo anglo. El mundo hispano —cientos de millones— **no tiene su Balatro**, pese a que su shared mental model (baraja española, Escoba/Truco/Mus) es, para ese público, **más fuerte** que el del póker. ÓRDAGO es "ser el Balatro de una cultura que aún no lo tiene". Y alinea con el perfil del autor: mexicano, español-first, mercado LatAm.

**Elevator pitch:** *"Balatro con baraja española. Suma 15 para hacer Escobas en cascadas exponenciales y gánale tu alma al Diablo, en un roguelike deckbuilder de cantina barroca y estética de calaca."*

---

## 2. Design Pillars

Comparte los 6 pilares de AZOTH (rectángulos primero · mental model en 60s · romper tus propias reglas · el juice es el producto · el tema significa · amplitud de estéticas sin traicionar el género). Especificidades de ÓRDAGO:

- **Pilar 2 (mental model) — aquí es una ventaja, no un riesgo.** A diferencia de AZOTH (donde la alquimia es *un poco* menos instantánea que el póker), el "sumar 15" del Escoba es **tan inmediato como el blackjack**, y para el mercado hispano la baraja española es intuición de infancia. El onboarding es más fácil que el de Balatro para ese público.
- **Pilar 5 (significado) — el tono es cálido, no frío.** ÓRDAGO se diferencia deliberadamente de AZOTH: donde AZOTH es liminal, austero y contemplativo, ÓRDAGO es **barroco, folk, teatral y vivo** (cantina, velas, calacas, cempasúchil). Mismo lenguaje de diseño, paleta emocional opuesta.

---

## 3. Posicionamiento de mercado

### 3.1 La tesis de diferenciación (¿no es esto solo un reskin de póker?)
Riesgo legítimo, dada la advertencia del género: hacer "otro juego de cartas" sin internalizar por qué los buenos funcionan es la trampa de los 2,800 clones. **Por qué ÓRDAGO no cae ahí:**

1. **El verbo core no es el póker.** Es el Escoba (sumar 15 / capturar), una mecánica aritmética distinta a la jerarquía de manos. (Beyond Words es "solo Scrabble" mecánicamente y es un hit porque remixa un sistema familiar con ejecución y motor de Jokers; ÓRDAGO remixa un sistema familiar *aún más arraigado* para su mercado.)
2. **La especificidad cultural ES la diferenciación.** No compite por novedad mecánica abstracta sino por un mercado masivo desatendido. La baraja española es el mental model más fuerte que existe para cientos de millones de hispanohablantes en un género donde nadie se los ofrece.
3. **Estética y tema 100% propios.** Cantina barroca + calaca + pacto con el Diablo no se parece a ningún competidor.

### 3.2 El mercado hispano como cuña
- El género roguelike está en su pico (~$400M en Steam 2025, +80% YoY) y **China pesa >1/3** en los grandes éxitos del subgénero — prueba de que un mercado culturalmente alineado y bien servido es oro.
- El mundo hispano es el segundo idioma nativo más hablado del planeta y **carece de un score-chase deckbuilder propio**. Es una asimetría de mercado explotable.
- **Doble alcance:** ÓRDAGO funciona como "el Balatro hispano" para su mercado nativo *y* como una curiosidad exótica y bella para el mercado global (igual que jugadores no-hispanos disfrutarían la estética y aprenderían el "sumar 15" en minutos).

### 3.3 Audiencia objetivo (Bartle, ver §4)
- **Primaria:** el mercado hispano (México, LatAm, España) que conoce la baraja española de toda la vida — onboarding casi nulo. Perfiles **Logrador** y **Explorador**.
- **Secundaria:** fans globales del género que quieren un sabor fresco y una estética distintiva.
- **El núcleo competitivo/social** (Asesino/Socializador) se captura asíncronamente: el Diablo como rival fantasma, leaderboards de "almas ganadas", semillas diarias (§4, §8).
- **Localización inversa:** aquí el español NO es localización — es el idioma nativo del producto. El inglés y el chino son la localización de expansión.

---

## 4. Arquetipos y estéticas (Bartle × MDA) — versión ÓRDAGO

Mismo método que AZOTH (cadena Jugador→Estética→Mecánica; cobertura del espectro completo de estéticas; arquetipos sociales servidos asíncronamente, nunca multijugador en vivo). Lo propio de ÓRDAGO:

| Estética / Arquetipo | Mecánica ÓRDAGO | Nota |
|---|---|---|
| **Sensación** | Juice stack de cartas: barajeo, barridas (Escobas) explosivas, monedas de oro saltando, campanazo del Diablo | Misma doctrina de juice que AZOTH (§10) |
| **Reto** (Logrador) | Apuestas crecientes del Diablo, Mangas, niveles de "Codicia" (= stakes/Ascension), El Envite del Diablo (bosses) | El espinazo |
| **Sumisión** | Loop "una mano más", sesiones cortas | El zen del juego de cartas |
| **Fantasía** | Ser el tahúr que reta al Diablo; romper la banca del infierno | Frame Faustiano |
| **Narrativa** | El cuento folk del que le gana al Diablo; viñetas de cantina (opt-in) | Trickster, no individuación |
| **Descubrimiento** (Explorador) | Pactos secretos (Arcana Oculta equiv.), jugadas no documentadas, el *Romancero* (lore folk a excavar), el Codex como mapa | Reforzado de origen |
| **Expresión** | Build-as-signature (arquetipos de juego: secuencias / pares / matas / Escobas), personalización de la baraja y la cantina | Cosmético + identidad de build |
| **Compañerismo** (Socializador, async) | Semillas diarias compartidas, builds compartibles, watchability/streaming | Sin co-op en vivo |
| **Competición** (Asesino, async) | **El Diablo Fantasma**: el high-score de otro jugador en tu semilla se encarna como el "Diablo" a vencer; leaderboards de almas; ranking de la semilla diaria | Hook competitivo temáticamente integrado |

> **Ventaja temática (nuevo respecto a AZOTH):** el frame "partida contra el Diablo" da una **encarnación natural del oponente asíncrono**. El Diablo Fantasma —el score a batir, vestido de Diablo— convierte el leaderboard en parte de la ficción, no en un menú aparte. Sirve al Asesino sin PvP en vivo y refuerza la fantasía.

---

## 5. La fantasía / experiencia del jugador

Eres un **tahúr** (un pícaro, un jugador de naipes) que se sienta a la mesa del Diablo en una cantina fuera del tiempo. Apostaste tu alma. La única salida es ganarle. El Diablo reparte, sube la apuesta, hace trampa — y tú tienes que ser más astuto y más rápido. El arco de una run ganada:

1. **Primera Manga:** jugadas torpes, apenas alcanzas la apuesta, el Diablo sonríe condescendiente.
2. **El primer Pacto que rima:** una Escoba dispara otra. Ves la primera cascada. El Diablo deja de sonreír.
3. **La máquina:** encadenas Escobas, las matas multiplican, los Pactos cascadean. Pasas de sumar 15 a sumar miles.
4. **La Última Mano:** rompes la banca del infierno. El Diablo pierde. Recuperas tu alma.

El sentimiento no es "gané una partida de cartas". Es: *le hice trampa al Diablo y gané.*

---

## 6. Core Loop

### 6.1 El verbo central — el Escoba ("sumar 15")
El núcleo legible, en una frase: **formas jugadas cuyo valor suma 15 (o múltiplos: 15, 30, 45…) para hacer una *Escoba* (barrida); cada Escoba puntúa Puntos × Suerte; los Pactos encadenan Escobas en cascadas.**

Es solitario contra el Diablo (no el Escoba 2-jugadores literal), adaptado a score-chase:

### 6.2 El loop de mano (segundos)
```
1. El Diablo reparte cartas a tu mano (de tu Baraja/mazo).
2. Seleccionas cartas para formar una JUGADA.
3. Si la jugada suma 15 (o múltiplo), haces una ESCOBA (barrida) → evento de puntuación.
4. La Escoba produce Puntos base × Suerte (mult).
5. Los PACTOS activos modifican/encadenan el resultado (cascada).
6. Las cartas capturadas y las matas añaden valor; los Puntos se suman a tu Codicia del turno.
7. Repites hasta agotar tus "Manos" (≈ las manos de Balatro) o alcanzar la apuesta del Diablo.
```
Ritmo objetivo: **30–45 s/mano**. Decisión en la Cantina entre mangas: **3–5 min**.

### 6.3 El loop de run (minutos)
```
La apuesta (= "blind"): supera el umbral de Puntos que pone el Diablo.
   → 3 apuestas por Manga (chica / grande / El Envite del Diablo con regla trampa).
La Cantina (shop) entre apuestas: compras Pactos, naipes, mejoras, rerolls; gestionas Reales.
4 Mangas = La Partida completa. Ganar la 4ª = recuperar tu alma (run ganada).
```

### 6.4 El loop de meta (horas/semanas)
```
Cada run → desbloqueos en el Codex + nuevos Pactos/naipes + progreso de Tahúres + posición en leaderboards.
Más Tahúres (mazos/personajes) → estilos de juego distintos.
Más niveles de Codicia (stakes) → la misma Partida más dura.
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

### 7.2 La baraja (los valores)
Baraja de **40 cartas**: 1–7 + Sota (10), Caballo (11), Rey (12) por palo (sin 8 ni 9). Para el motor de Escoba, las figuras valen **8/9/10** (Sota/Caballo/Rey) al sumar 15 — la convención clásica del Escoba, instantánea para el público hispano.

### 7.3 La Mesa y el motor de Escoba
La acción ocurre sobre **La Mesa del Diablo**. Sumar 15 con tu jugada = Escoba (barrida) = evento de puntuación. Múltiplos (30, 45) = Escobas mayores con multiplicadores crecientes. Las cartas capturadas se acumulan en tu **Baza**, que aporta valor. Es el equivalente legible y aritmético de "la mano de póker", pero con un verbo propio.

### 7.4 Las Jugadas (combinaciones — la jerarquía)
Sobre el "sumar 15", la profundidad viene de las combinaciones nativas de los juegos de baraja española, como capas de bonus/multiplicador:

| Jugada | Origen | Efecto |
|---|---|---|
| **Escoba** | Escoba | El evento base: sumar 15 |
| **Pares / Medias / Duples** | Mus | Pares, trío, dos pares → tiers de mult |
| **Secuencia / Liga** | Chinchón/Tute | Corrida en un palo → bonus |
| **Envido** | Truco | Dos cartas del mismo palo que suman alto → bonus de palo |
| **Las Matas** | Truco | Las 4 cartas legendarias (§7.5) |

### 7.5 Las Matas (las cartas legendarias — rareza ya integrada)
Truco trae un sistema de rareza *gratis* y culturalmente icónico: la jerarquía de las **matas**, las cuatro cartas más poderosas de la baraja, en orden:
1. **As de Espadas** (el macho / ancho de espadas)
2. **As de Bastos** (ancho de bastos)
3. **Siete de Espadas**
4. **Siete de Oros**

En ÓRDAGO son cartas de **Puntos base enormes y efectos únicos** — las "doradas" que el jugador sueña con capturar. Sistema de rareza/poder que el público hispano ya reconoce sin explicación.

### 7.6 Pactos (los "Jokers" — el motor)
Modificadores permanentes ocupando slots, enmarcados como **tratos con el Diablo**. Tipos (paralelos a los catalizadores de AZOTH):
- **De Puntos** (aditivos): "+30 Puntos por cada Oro en la jugada".
- **De Suerte** (multiplicativos): "×1.5 Suerte si haces Escoba con Espadas".
- **De Reales** (economía): "gana 1 Real por Escoba".
- **En cadena** (cascadas): "cuando puntúa una mata, repite el Pacto a su izquierda".
- **Build-defining**: "las Secuencias cuentan ahora como Escobas".
- **Pactos Oscuros (Arcana Oculta equiv.):** Pactos secretos, no listados, que se desbloquean por descubrimiento — y **algunos con un costo** (poder enorme a cambio de una penalización: el precio de tratar con el Diablo). El eje riesgo/recompensa temáticamente perfecto.

> Posible sistema dual (decisión §19): **Fullerías** (trampas del tahúr — tu maña, sin costo) vs **Pactos** (poder del Diablo — con costo/riesgo). Duálidad temáticamente riquísima; evaluar si añade profundidad sin romper el Pilar 2.

### 7.7 La matemática: Puntos × Suerte
**Puntos (azul, base)** × **Suerte (rojo, mult)**. Los **+Suerte** y **×Suerte** crean el escalado exponencial; el orden izquierda→derecha importa (rompecabezas de secuenciación de Pactos); las cascadas nacen de Pactos que disparan Pactos (loops anidados). Idéntico en estructura al motor de AZOTH y de Balatro.

### 7.8 Naipes Marcados (mejoras — el equivalente Foil/Glass)
El tahúr marca las cartas. Mejoras con textura + luz propia al hover:
- **Marcada** (×Suerte fijo — Holo/Polychrome).
- **Dorada** (genera Reales — Gold).
- **Encerada/Resbaladiza** (se juega y vuelve a la mano — efecto de repetición).
- **De Cristal** (×Suerte alto pero se rompe — Glass).
- **Cargada/Trucada** (un solo uso, efecto brutal — Volátil).

### 7.9 Economía: La Cantina
- Moneda: **Reales** (moneda histórica española), ganados por mangas + **interés** sobre lo guardado (misma tensión gastar/acumular de Balatro).
- En **La Cantina** (la taberna donde el Diablo atiende la barra) compras: Pactos, naipes, mejoras, **reroll**, **slots** extra.
- Gestión de Reales = capa estratégica completa.

### 7.10 La estructura: La Partida contra el Diablo (antes/acts)
- **4 Mangas** (la apuesta sube en cada una), cada una con **3 apuestas**: chica, grande, y **El Envite del Diablo** (un boss con regla trampa: "el Diablo se queda con tus Oros esta mano", "la primera Escoba no cuenta", "las matas valen la mitad"…).
- Ganar la 4ª Manga = **recuperar tu alma** = run ganada.
- **Modo Condena** (endless) post-victoria para los hardcore.

---

## 8. Progresión, meta y capa social asíncrona

Misma arquitectura que AZOTH (§8 de aquel doc). Específico de ÓRDAGO:
- **Tahúres (= decks/personajes):** cada uno con un palo de afinidad, condición inicial y estilo de juego (el de Espadas agresivo, el de Oros económico, etc.). Combustible para el Explorador y la Expresión.
- **Niveles de Codicia (= stakes/Ascension):** el Diablo apuesta más fuerte, hace más trampa.
- **El Codex / Romancero:** colección de Pactos, naipes y jugadas + el *lore* folk (el Romancero del Diablo — cuentos de cantina a excavar). Mapa del Explorador.
- **Capa social asíncrona (mismo enfoque que AZOTH):**
  - **El Diablo Fantasma:** el high-score de otro jugador en tu semilla diaria aparece *como el Diablo* al que debes superar. Competición (Asesino) integrada en la ficción.
  - **Semillas diarias/semanales ("La mesa del Diablo de hoy"):** ranking global.
  - **Tablas de Almas (leaderboards):** rankings de "almas ganadas" globales/amigos/por Tahúr.
  - **Compartir la mano:** código de run/build para presumir engines rotos.
  - **Diseño para watchability/streaming.**
  - Stretch post-1.0: **duelo asíncrono / carrera de semilla** (NO co-op ni PvP en vivo).

---

## 9. Filosofía de dificultad y balance
Idéntica a AZOTH: easy to learn / hard to master; curva que **fuerza** combos rotos; variance controlada (reroll + descarte como válvulas); balance por spreadsheet + telemetría. Aquí el "easy to learn" es aún más fuerte por el shared mental model del Escoba.

---

## 10. Game Feel / Juice
Mismo juice stack que AZOTH (animación → partículas → screen effects → audio → háptica; "el número grande es objeto de gameplay"; color = etiqueta sin labels). Sabor específico de ÓRDAGO:
- **Feel de naipe:** el peso del barajeo, el chasquido al repartir, el *barrido* satisfactorio de la Escoba (las cartas vuelan de la mesa a tu baza).
- **El Diablo reacciona:** micro-reacciones del Diablo al otro lado de la mesa (frunce el ceño, golpea la mesa, ríe) — feedback diegético del progreso.
- **Audio:** guitarra/jarana, palmas, campana de iglesia grave en cada ×Suerte, el rumor de la cantina que crece con la cascada.
- **Color funcional:** Azul = Puntos · Rojo = Suerte · Oro = Reales · Verde = Manos restantes · y un acento por palo.

---

## 11. Dirección de arte y audio (el diferenciador estético)

**Pilar estético: barroco folk latinoamericano — la antítesis cálida de AZOTH.**

- **Escenario:** una **cantina a la luz de velas**, fuera del tiempo; el Diablo como un *tahúr* elegante y carismático al otro lado de la mesa de madera.
- **Cartas y UI:** **grabados estilo Posada** (las calaveras de José Guadalupe Posada), iconografía de la baraja española reinterpretada, filigrana barroca. Calacas, cempasúchil (flor de muerto), veladoras, exvotos, mezcal.
- **Paleta:** negros cálidos y maderas, estallidos de **rojo cantina, oro de vela y naranja de cempasúchil**; los Pactos y las Escobas brillan saturados sobre el fondo oscuro (mismo principio de contraste de Balatro, paleta cálida).
- **Tono:** teatral, vivo, folk, ominoso-pero-festivo. La energía del Día de Muertos: la muerte tratada con humor, color y respeto, no con frío. **Inquietante sin gore** (clave para rating, ver §16).
- **Audio:** son jarocho / guitarra / jarana, palmas, coros, campanas; un soundtrack folk-barroco hipnótico. (El soundtrack es parte del legend status del género — invertir aquí.)

> **Pipeline AI-augmented:** el estilo grabado-Posada, filigrana y iconografía de naipes es **muy favorable a generación 2D asistida por IA** + retoque. Ventaja de scope.
>
> ⚠️ **Cuidado de IP/estética (decisión §19):** inspirarse en el *estilo* de Posada (dominio público, grabados de fines del s. XIX) y en el imaginario folk del Día de Muertos es seguro; **evitar** copiar diseños registrados (p. ej. personajes de películas, la "Catrina" de marcas específicas) y respetar la línea entre homenaje cultural y apropiación. El diseño de cartas debe ser original, no calcar barajas comerciales existentes.

---

## 12. Narrativa y worldbuilding
- **Premisa:** un tahúr apostó su alma y se sienta a la mesa del Diablo en una cantina fuera del tiempo. La salida es ganarle.
- **Entrega:** 100% ambiental y opcional — viñetas de cantina, flavor de Pactos, el arco de las 4 Mangas, el *Romancero del Diablo* (cuentos folk para quien excava). Cero lore dump.
- **El subtexto:** el arquetipo del **trickster** — el pícaro que vence al poder superior con maña, no con fuerza. Es Jungian-adjacent (como AZOTH) pero **otro arquetipo**: trickster vs. individuación. Raíz folk pan-hispana del "engañar al Diablo" (el cuento del jugador que le gana las cartas al demonio).

---

## 13. UX / Onboarding (aquí es una fortaleza)
- **"Sumar 15" es instantáneo** — como el 21 del blackjack; para el público hispano la baraja española no necesita tutorial.
- **Jugadas telegrafiadas:** la UI muestra la suma y el score previo antes de confirmar (como Balatro).
- **Codex como tutorial pasivo.**
- **Métrica de control:** comprensión del loop en <90 s de telemetría (objetivo más agresivo que AZOTH por el mental model más fuerte).

---

## 14. Scope y MVP
Misma filosofía "rectángulos primero" que AZOTH.
- **Prototipo (rectángulos):** 1 Tahúr, motor de Escoba + Puntos×Suerte, ~25 Pactos, 1 Manga (3 apuestas + 1 Envite del Diablo), Cantina básica con Reales e interés. Filtro: ¿divertido con cuadros? ¿"una mano más"?
- **Vertical slice:** las 4 Mangas, ~80–120 Pactos (incl. primeros Pactos Oscuros), 1 Tahúr pulido con juice + audio, UI/color final, esqueleto de semilla/leaderboard. Es la demo de Next Fest.
- **Cortes (igual que AZOTH):** core single-player definitivo; capa social **asíncrona sí** (incl. el Diablo Fantasma); **multijugador en vivo NO** (rompe la fantasía de la mesa íntima con el Diablo y trae el costo de equilibrio de poblaciones; ese terreno lo ocupan los party deckbuilders). Múltiples Tahúres, Codicia alta, Modo Condena → post-EA/1.0.

---

## 15. Tecnología y plataforma
Misma decisión que AZOTH (🔶 **DECISIÓN — Engine**): **validar el loop con rectángulos en lo más rápido a la mano (Godot/Love2D, un fin de semana); decidir Unreal solo si el juice justifica la fricción de un 2D card-game en un engine 3D.** Niagara + material system de Unreal son armas de clase mundial para el juice si vas por ahí. PC/Steam primero; ports post-1.0. Datos data-driven (JSON/Data Tables); Steamworks leaderboards para la capa asíncrona.

---

## 16. Modelo de negocio
Misma doctrina que AZOTH: **premium buy-to-play, $14.99–$19.99, sin MTX, updates gratis, colaboraciones estilo "Friends of Jimbo", la confianza/comunidad como activo, ruta Steam → suscripciones → ports → long tail.** Diferencias propias de ÓRDAGO:
- **El español es el idioma nativo, no la localización.** Eso te da un **mercado primario gigante y desatendido** desde el día uno, con CAC bajo vía contenido en español (tu fortaleza). El inglés y el chino son expansión.
- **Ventaja de rating:** el Escoba y la baraja española **no evocan gambling de casino** como el póker/slot que metió a Balatro en líos de PEGI. Mantén el tono folk sin gore → rating accesible (12+/T). El frame "Diablo" es folk-cultural, no de apuestas reales.

---

## 17. Roadmap de producción
Mismo esquema de 5 fases que AZOTH (Prototipo → Vertical slice → Demo/Next Fest → Early Access → 1.0+post-launch), con modelo EA transparente y manejo de crisis rápido. Hito propio: una **campaña de marketing en español/LatAm** (creators de habla hispana, nostalgia de la baraja española) como motor de wishlists barato y diferenciado.

---

## 18. KPIs
Mismos KPIs por arquetipo que AZOTH (wishlists, conversión, % reseñas positivas; por arquetipo: compleción/Codicia para Logrador, ritmo de descubrimiento de Pactos Oscuros para Explorador, participación en semillas/Diablo Fantasma para Asesino, runs compartidas para Socializador; session length, CCU, retención 20h+/50h+; salud del loop). Métrica propia: **penetración por geografía hispana** (¿está funcionando la tesis de mercado nativo?) y **conversión del público no-hispano** (¿el "sumar 15" cruza fronteras?).

---

## 19. Riesgos y decisiones abiertas

| Riesgo | Severidad | Mitigación |
|---|---|---|
| **Percepción de "reskin de póker"** | Media-Alta | El verbo core es Escoba (no manos); la especificidad cultural y el tema propio son la diferenciación; comunicar el ángulo "Balatro hispano" con claridad |
| **Mercado primario hispano: ¿paga en Steam como el global?** | Media | Precio ajustado por región (Steam regional pricing); doble alcance (nativo + exótico global); no depender solo del mercado hispano |
| **IP/estética (Posada, Día de Muertos, Catrina)** | Media | Inspirarse en estilo de dominio público; diseños de carta originales; respetar homenaje vs. apropiación (§11) |
| **Onboarding fuera del mundo hispano** | Baja | "Sumar 15" es universal (blackjack); jugadas telegrafiadas |
| **Rating/gambling** | Baja (ventaja) | Escoba no evoca casino; tono folk sin gore |
| (Comparte los riesgos transversales de AZOTH: tema sobre loop, saturación, sobre-ampliar arquetipos, fricción de Unreal, scope, balance exponencial) | — | Ver AZOTH §19 |

### Decisiones abiertas (para César)
1. 🔶 **Título:** ÓRDAGO (Mus, "ir con todo" — muy ownable pero más España/Euskadi) vs **EL ENVITE** / **LA PARTIDA** (más pan-hispano). *Dado tu mercado LatAm, sopesar resonancia regional.*
2. 🔶 **Verbo core:** ¿el Escoba "sumar 15" puro, o un híbrido que dé más peso a las combinaciones de Mus/Truco (pares, envido)? *(Rec.: Escoba puro como ancla legible; combinaciones como capa de bonus.)*
3. 🔶 **Sistema dual Fullerías vs Pactos:** ¿una sola categoría de "Jokers" (Pactos) o el dual maña-vs-Diablo? *(Rec.: empezar con Pactos; evaluar el dual en vertical slice.)*
4. 🔶 **Tono regional de la estética:** ¿Día de Muertos / Posada (muy mexicano, tu tierra) o un barroco hispano más pan-regional (cantina/venta picaresca)? *Define identidad y mercado.*
5. **Cosmología de palos:** ¿las afinidades de palo (Oros=economía, Espadas=mult…) son fuertes o ligeras? Afecta la profundidad de build.
6. **¿AZOTH o ÓRDAGO primero?** Dos apuestas válidas: AZOTH (white space estético global) vs ÓRDAGO (white space de mercado hispano, onboarding más fácil, alineado a tu perfil). *Mi lectura: ÓRDAGO tiene una cuña comercial más clara y barata para ti; AZOTH tiene un techo de distinción global mayor. Prototipa el que más te jale en un fin de semana de rectángulos y deja que el "una más" decida.*

---

*Fin del macro GDD v0.1. Siguiente paso lógico: micro GDD del prototipo — los ~25 Pactos concretos (incl. 2–3 Pactos Oscuros), las fórmulas exactas de Puntos×Suerte, las matas con sus valores, y los umbrales de la primera Manga.*
