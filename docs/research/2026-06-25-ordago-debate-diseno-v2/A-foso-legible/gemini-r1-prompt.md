# Debate ÓRDAGO · Clúster A "El foso es invisible" · RONDA 1 · ASIENTO GEMINI

## Tu asiento
Eres el **Estratega de Valor + señal de mercado**. Tu pregunta: **¿la ilegibilidad del foso mata la percepción de profundidad/valor del juego — o la opacidad ES parte del atractivo?** Y sobre todo: **¿qué hacen los referentes que SÍ resuelven esto** (Balatro, Slay the Spire, e Into the Breach que hace el futuro literalmente legible)? Eres uno de 3 asientos (los otros: un Diseñador de Sistemas con rigor de elegancia y un Red-Team con data de plataforma). Lidera con lo que SOLO tú aportas: comparativa de referentes, percepción de valor/profundidad, señales de mercado del subgénero deckbuilder/roguelike. Usa web research donde puedas y marca confianza.

## Contexto del juego (no tienes el GDD; esto es lo esencial)
ÓRDAGO = **roguelike deckbuilder** sobre **baraja española**, fantasía *"le haces trampa al Diablo"*. Verbo base = **Escoba** (capturar cartas que suman 15) sobre una **Mesa adversarial** que el Diablo **siembra con intención**. Sistema dual: **Trampas** del Diablo (alteran el verbo) ↔ **Fullerías** tuyas + **Pactos** pasivos, todos compitiendo por **~3 ranuras de "Maña"** (trade-off faustiano tipo Joker-slots de Balatro pero con costo estructural recurrente). Modelo de negocio: **B2P premium en Steam ($14.99), sin MTX**, + demo web jugable. Mercado: LATAM + USA general + **hispanos en USA (el sweet spot)**.

**El cambio de v1.2 (§7.3) y el problema central del clúster:** el foso se reescribió de *"¿cuál suma 15?"* (puzzle de solución casi-única) a **"¿qué FUTURO capturo?"**. Cada captura se evalúa en **3 ejes que no se maximizan a la vez**:
- **Tempo** — puntúa ya, barato.
- **Escala** — alimenta tu motor de Pacto (menos ahora, más después).
- **Defensa** — niega al Diablo una carta.

El problema: **estos ejes son vocabulario del DISEÑADOR. El jugador no los VE.** Si captura sin entender por qué una jugada importa más que otra, el foso central **se siente como RNG** (puro azar). Y la banda de "spread de EV" entre la mejor y la 2ª jugada está en disputa: **~8-15%** (la mayoría del panel: spreads >20-25% son trampa de novato que mata el foso) vs **15-20%** (la postura que tú representaste antes: por debajo de eso *"se siente ajedrez seco y se evapora la dopamina de suerte"*).

**La navaja (§317):** existe un "modo aprendiz" que resalta la solución, pero el GDD lo gatea porque *"el resaltado de Mesa cruza a solucionador parcial en maestría"* — es decir, **mostrar demasiado mata el foso** (le das la respuesta al jugador). Entonces la tensión es: *hacer visible el VALOR-FUTURO de una jugada sin REGALAR cuál es la jugada óptima.*

## Los huecos del Clúster A (resumen)
- **#2** — Ejes tempo/escala/defensa sin máquina de legibilidad <1s → se siente RNG. Fix: **tells de eje** (forma+color) gateados + kill **≥70% testers nombran su eje**.
- **#4** — La asistencia gratis enseña el verbo VIEJO (sumar 15, = tempo, el eje declarado *irrelevante*), dejando invisible el foso real (escala/defensa). Fix: resaltar las ~2 jugadas Pareto por color de eje; kill **≥60% think-aloud menciona un eje de futuro**.
- **#35** — El glance gate valida el SCORE, no el espacio de DECISIÓN. Fix: el juez también lee Trampa activa + función-de-palo <0.5s.
- **#1** — La build dominante (0F/3P) no tiene test que la false → riesgo de meta de un solo carril (mata la percepción de profundidad). Fix: test de dominancia de Maña en el solver.
- **#50** — Sin curva de escalado del umbral del Diablo → la run se trivializa o se vuelve muro.
- **#53** — Nadie verifica que la **brecha de skill experto-vs-intermedio CREZCA** con las horas (la promesa de "400h de Balatro").
- **#8 / #6 / #3** — FTUE con incertidumbre≈0 vs invariante de bifurcación; ratio jugadas/reglas sin recuento.

## Cartas-lente (cítalas con confianza)
- **A1🟢🟡 (elegancia):** *profundidad ≠ complejidad*; **Balatro** descarta combate complejo y la profundidad emerge de **sinergias de Jokers que "ningún jugador mapea en sus primeras 50h" — y esa brecha entre skill percibido y real impulsa partidas de 400h** (el "400h" es 🟡[L3] estimación de comentaristas). **Threes vs 2048:** *"si 2048 es damas, Threes es ajedrez"* — la elegancia gana el **respeto y la cola larga**, NO garantiza viralidad; el clon simple puede ganar la distribución a corto plazo. **Refinamiento "Cognitive INP":** el **INPUT debe ser 0% carga cognitiva** (el espectador lo entiende en <450ms), la **elegancia vive en el OUTPUT tardío** — así legibilidad/viralidad y profundidad **no compiten** (viven en momentos distintos del eje temporal).
- **01🟢 (competencia):** mejorar *se siente* recompensante; el feedback de maestría debe ser legible o no hay recompensa de competencia.

## Lo que debes entregar (en este orden, con NIVEL DE EVIDENCIA L1 plataforma > L2 industria > L3 training > L4 razonamiento, y confianza 🟢/🟡/⚪ por claim)
1. **STEELMAN del fix del clúster** — la versión más fuerte de "hacer legible el valor-futuro con tells de eje gateados". ¿Por qué la legibilidad del *espacio de decisión* (no solo del score) es lo que separa "tiene profundidad percibida" de "se siente RNG", y por qué eso impacta wishlists/reviews/retención D7+?
2. **ATAQUE / MEJORA desde el mercado** — ¿es cierto que la ilegibilidad mata el valor, o **Balatro prospera PRECISAMENTE porque el jugador NO mapea las sinergias** (la opacidad ES el motor de las 400h)? ¿Hacer "demasiado legible" el futuro convierte a ÓRDAGO en un puzzle resuelto (mata la rejugabilidad)? ¿El kill "≥70% nombran su eje" es el umbral correcto, o un juego de clase mundial *quiere* que el jugador medio juegue subóptimo sin saberlo (la brecha de skill de #53)?
3. **REFERENTES — la pieza que SOLO tú traes** — compara cómo resuelven "futuro legible sin regalar la jugada":
   - **Into the Breach** — telegrafía el futuro del enemigo de forma **perfecta y determinista** (sabes exactamente qué hará cada enemigo) y aun así es profundísimo. ¿Qué patrón de legibilidad-de-consecuencia roba ÓRDAGO de ahí, y dónde NO aplica (ITB es de información perfecta; ÓRDAGO tiene azar)?
   - **Slay the Spire** — legibilidad de intención del enemigo + planificación multi-turno; ¿cómo comunica "valor futuro" sin resolver el turno por ti?
   - **Balatro** — la opacidad deliberada de las sinergias; ¿cuánto debe ÓRDAGO **ocultar** a propósito?
   Da números/señales de mercado donde puedas (ventas, retención, reviews, longevidad) y marca confianza.
4. **RESOLUCIÓN DE CLASE MUNDIAL con criterios falsables** — propón **dónde poner el dial** entre "legible" (Into the Breach) y "opaco" (Balatro) para ÓRDAGO: qué se telegrafía (valor-futuro del eje) y qué se oculta (la jugada óptima exacta). Da un criterio de A/B o test de mercado falsable (p.ej. percepción de profundidad en encuesta post-demo, o retención D7 con tells-on vs tells-off). Toma postura sobre la banda de EV (~8-15% vs 15-20%) con argumento de **percepción de valor**, no solo de feel.
5. **QUÉ DECISIÓN ES DE CÉSAR** — explícitalo (cuánto ocultar vs revelar es un trade-off de identidad de producto, no lo zanja el debate).

**Densidad:** concreto, numérico, con referentes citados. ≤ ~900 palabras.
