# Debate ÓRDAGO · Clúster A "El foso es invisible" · RONDA 1 · ASIENTO META AI

## Tu asiento
Eres **Data L1 de plataforma + Red Team**. Tu ventaja única: data REAL de comportamiento de jugadores/audiencias (Instagram/WhatsApp/Meta Ads, engagement, retención, qué se comparte, qué se abandona) que ninguna otra IA tiene. Tu trabajo aquí es **doble**: (1) traer lo que dice la data real sobre juegos cuyo verbo se siente "RNG/suerte" vs juegos cuyo verbo se siente "skill/legible" — ¿cuál retiene, cuál se comparte, cuál convierte?; y (2) **atacar el clúster como Red Team**: ¿alguno de estos "huecos" es FALSO, está sobre-vendido, o el fix propuesto EMPEORA el feel del juego? Eres uno de 3 asientos (los otros: un Diseñador de Sistemas con rigor de elegancia y un Estratega de Valor/referentes). Responde en español. Marca cada claim con su nivel de evidencia y confianza.

## Contexto del juego (no tienes el GDD; esto es lo esencial)
ÓRDAGO = **roguelike deckbuilder** sobre **baraja española**, fantasía *"le haces trampa al Diablo"*. Verbo base = **Escoba** (capturar cartas que suman 15) sobre una **Mesa adversarial** que el Diablo **siembra con intención**. Sistema dual: **Trampas** del Diablo ↔ **Fullerías** tuyas + **Pactos**, compitiendo por **~3 ranuras de "Maña"** (trade-off faustiano). **B2P premium en Steam ($14.99) + demo web jugable, sin MTX.** Mercado: LATAM + USA general + **hispanos en USA (sweet spot)**; mucha sesión es **móvil y MUDA** (autoplay bloqueado, baja-banda).

**El cambio de v1.2 (§7.3) y el problema central:** el foso se reescribió de *"¿cuál suma 15?"* a **"¿qué FUTURO capturo?"**, evaluando cada captura en 3 ejes que no se maximizan a la vez:
- **Tempo** — puntúa ya, barato.
- **Escala** — alimenta tu motor de Pacto (más después).
- **Defensa** — niega una carta al Diablo.

El problema declarado: **esos ejes son vocabulario del diseñador; el jugador no los VE → el foso se siente como RNG.** La navaja (§317): hay un "modo aprendiz" que resalta la solución, **gateado porque mostrar demasiado convierte la ayuda en "solucionador parcial" y mata el foso** (le das la respuesta al jugador). Tensión: *hacer visible el valor-futuro sin regalar la jugada óptima.*

## Los huecos del Clúster A (resumen + el fix que debes atacar)
- **#2** — Ejes sin máquina de legibilidad <1s → "se siente RNG". *Fix:* **tells de eje** (forma+color) gateados; kill **≥70% testers nombran su eje**.
- **#4** — La asistencia gratis enseña sumar 15 (= tempo, el eje *irrelevante*), dejando invisible el foso (escala/defensa). *Fix:* resaltar las ~2 jugadas Pareto por color de eje; kill **≥60% think-aloud menciona un eje de futuro**.
- **#35** — El glance gate valida el SCORE, no la DECISIÓN. *Fix:* el juez lee Trampa activa + función-de-palo <0.5s.
- **#1** — La build dominante (0F/3P) sin test que la false. *Fix:* test de dominancia de Maña en el solver de papel.
- **#50** — Sin curva de escalado del umbral del Diablo (la run se trivializa o se vuelve muro).
- **#53** — Nadie verifica que la **brecha de skill experto-vs-intermedio crezca** con las horas.
- **#8 / #6 / #3** — FTUE con incertidumbre≈0 vs invariante de bifurcación; ratio jugadas/reglas sin recuento.

## Cartas-lente (cítalas con confianza)
- **A1🟢🟡 (elegancia):** profundidad ≠ complejidad; **Church 🟢:** sin *consecuencia perceptible <1s* la decisión se siente azar; lección **Threes vs 2048** — el simple gana viralidad, el elegante gana cola larga (NO son lo mismo). Refinamiento "Cognitive INP": el **input debe ser 0% carga cognitiva** (el espectador lo capta <450ms); la profundidad vive en el **output tardío**.
- **01🟢 (competencia):** la sensación de mejorar es recompensa; pero ojo a la **falsa competencia** (hacer creer que mejoró cuando solo subió un número).

## Lo que debes entregar (en este orden, con NIVEL DE EVIDENCIA L1 plataforma > L2 industria > L3 training > L4 razonamiento, y confianza 🟢/🟡/⚪ por claim)
1. **DATA L1 — verbo "RNG" vs verbo "legible/skill"** (lo que SOLO tú sabes): ¿qué dice la data real de jugadores/audiencias sobre juegos cuyo loop se PERCIBE como suerte vs como habilidad? Específicamente: (a) **retención** — ¿los juegos "se siente RNG" retienen peor a D7/D30, o el azar percibido sube el engagement a corto plazo (variable-reward) y lo baja a largo? (b) **compartibilidad** — en LATAM/hispanos-USA, ¿qué se comparte más: el momento de **suerte espectacular** o el de **jugada hábil**? (c) ¿el clip de un deckbuilder convierte mejor cuando se lee "fue suerte/locura" o "fue genio"? Da números/rangos donde puedas (CTR, share-rate, retención, completion) y marca confianza.
2. **STEELMAN del fix del clúster** — la versión más fuerte de "hacer legible el valor-futuro con tells gateados". ¿Por qué, desde la data de comportamiento, un verbo legible importa para la conversión y la cola larga?
3. **RED TEAM — ataca el clúster** (lo más valioso de tu asiento). Sé concreto:
   - **¿Algún hueco es FALSO o sobre-vendido?** P.ej.: ¿de verdad "se siente RNG" si el jugador no nombra el eje, o la mayoría de jugadores de deckbuilder **disfrutan jugar por intuición sin verbalizar** (y el kill "≥70% nombran su eje" castiga un juego que en realidad funciona)? ¿La verbalización think-aloud (#4) correlaciona con retención real o es un proxy de laboratorio que no predice nada en producción?
   - **¿El fix EMPEORA el feel?** ¿Tells de eje siempre presentes vuelven la Mesa **ruidosa/recargada** (papilla visual, peor en móvil mudo de baja-banda)? ¿Convierten un juego de *intuición y vibra* (lo que la audiencia hispana comparte) en una hoja de cálculo fría que **mata la dopamina de suerte** y la compartibilidad? ¿El "tell de eje" cruza la línea de §317 y regala la jugada, matando la rejugabilidad que sostiene las 400h?
   - **¿La métrica #53 (brecha p50-p95 crece) es accionable o vaporware?** ¿Se puede medir antes del lanzamiento?
4. **RESOLUCIÓN DE CLASE MUNDIAL con criterios falsables** — desde la data: ¿cuánto se debe revelar vs ocultar para **maximizar retención D30 + share-rate** sin matar el foso? Propón un test de mercado falsable (A/B tells-on/off en la demo: retención D7, share-rate, % refund) con umbrales numéricos. Toma postura sobre la banda de EV (~8-15% vs 15-20%) desde el ángulo de **feel/dopamina de suerte**.
5. **QUÉ DECISIÓN ES DE CÉSAR** — explícitalo (el dial revelar-vs-ocultar es identidad de producto + apuesta de mercado, no lo zanja el debate).

**Densidad:** concreto, numérico, con data de plataforma donde la tengas. Si no tienes el dato exacto, dilo y baja la confianza. ≤ ~900 palabras.
