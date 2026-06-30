# Opus — Ronda 1 · Clúster E (a ciegas)

**Asiento:** Diseñador de Sistemas + sustracción/elegancia (A5, A1). Lidero PODA y JERARQUÍA Z.

Premisa-marco (mi sesgo, declarado): no se diseña contenido, se diseña el **espacio de decisión**. "≥6-7 capas sobre la misma pantalla" no es problema si todas comparten **un solo verbo (sumar 15)** y una sola moneda de decisión (Maña). El riesgo real no es cantidad de sistemas: es **cuántas REGLAS distintas debe verbalizar el jugador antes de su 1ª victoria** y **cuántos canales visuales compiten en el mismo frame**. Ataco ambos por sustracción.

---

## SUB-TEMA 1 — Jerarquía Z y poda (#5, #6, #3) — LIDERO

**(a) Steelman.** #5 acierta en que el anti-papilla ya está doble-gateado (§11 glance gate + §14) 🟢 pero las reglas de saliencia están **dispersas**; un árbitro Z nombrado (Z1>Z2>…) en §10.2 es el costo mínimo correcto: no añade sistema, **renombra y ordena** lo existente. #3 acierta en exigir un recuento jugadas÷reglas que **ninguna sección hace hoy** 🟡. #6 acierta en sospechar que la complementariedad Pacto↔Fullería puede estar **decretada**, no demostrada 🟡.

**(b) Ataque/mejora por sustracción.**
- **#5 infla si Z se vuelve una tabla de N capas.** No quiero "presupuesto de saliencia" como inventario. Quiero **una sola regla dura jerárquica heredada de la baraja física**: `Z1 silueta(palo/figura) > Z2 valor(número) > Z3 estado(Trampa/Sospecha) > Z4 cascada/feedback`. Todo lo demás se **serializa en el tiempo, no se apila en el espacio**: dos eventos Z3+ NUNCA comparten frame (pillado-Sospecha y cascada-T3 se encolan, no se superponen). Eso mata "papilla" sin añadir UI: es una **regla de scheduler**, no de render.
- **#3 decreta el techo ≤7±2 sin definir el denominador.** Inútil sin lista nominal. Lo aporto abajo.
- **#6 "contar reglas verbalizadas ≤5" es buen gate pero el *kill* es flojo.** "¿Siguen distintos sin el auto-sabotaje?" no es binario. Lo endurezco: la complementariedad es real **solo si existe ≥1 estado de Mesa donde la elección óptima Pacto vs Fullería se invierte** según el tablero. Si Fullería domina a Pacto en >85% de seeds, el trade-off es falso (es un impuesto disfrazado de elección).

**Lista nominal de reglas-CORE de la 1ª victoria (denominador A1) — objetivo-a-falsar:**
1. Sumar 15 = Escoba (verbo).
2. La Mesa tiene cartas sembradas que puedes capturar.
3. El Diablo impone 1 Trampa que altera la regla.
4. Rompes la Trampa con 1 Fullería.
5. Romper sube Sospecha (riesgo).
6. Tienes ~3 ranuras de Maña.
7. Maña: Fullería **o** Pacto (trade-off).

= **7 reglas-core.** **Pactos-cascada, Codex, Romancero, Diablo Fantasma, artefacto-puente, firma-social = META/DELIVERY gateados → NO cuentan** para el ≤7±2 porque NO son necesarios para la 1ª victoria. Método de conteo falsable: el tester **verbaliza en voz alta** las reglas que cree necesitar antes de jugar la Manga 1; si nombra ≥1 sistema meta, ese sistema **entró demasiado pronto** (bug de onboarding, no de diseño).

**(c) Resolución FALSABLE.**
- **Gate Z (extiende §11/§14):** render de peor-caso combinado — Trampa activa + barra Sospecha subiendo + cascada T3 — a **100×100px, escala de grises, simulación daltónica (deuteranopia)**: silueta y valor de cada carta siguen identificables por **≥9/10 testers** y los dos eventos Z3+ **no coinciden en el mismo frame** (verificable por log de scheduler: `Δt(evento_Z3_a, evento_Z3_b) > 0`). MUERE si <9/10 o si el log muestra solape.
- **Gate de complejidad (extiende §14):** `reglas_core ≤ 9` (7±2, techo duro). MUERE si la lista nominal pasa de 9, **o** si un subsistema de delivery entra sin podar uno de core (regla de conservación: +1 delivery ⇒ −1 carga core percibida, no necesariamente −1 regla).
- **Gate de complementariedad (#6):** existe ≥1 estado de Mesa donde Pacto > Fullería en EV, y la frecuencia de "Fullería siempre óptima" ≤85% sobre 1000 seeds del solver §14. MUERE si Fullería domina >85%.

**(d) Decisión de César.** ¿El ≤7±2 **incluye o excluye la economía de Maña** como regla única (mi lista la cuenta como 2: ranuras + trade-off)? Si la cuenta como 1, hay holgura para 1 regla más; si como 2, estamos al borde. Y: **¿cuánta elegancia (techo de combo emergente) sacrifica por legibilidad** al prohibir 2 eventos Z3 en el mismo frame? Serializar baja el "wow" de la cascada simultánea a cambio de claridad. Solo César fija ese cambio.

---

## SUB-TEMA 2 — Presupuesto temporal (#48) — contribuyo fuerte

**(a) Steelman.** #48 🟢 es correcto: la contradicción solo aparece **apilando peor-caso**; con valores centrales cierra (~31.5 min). Una tabla de presupuesto en §9 validada por el solver §14 es el fix correcto y barato (no añade sistema, **cierra una cuenta abierta**).

**(b) Ataque.** El fix nombra "variable de pacing indeterminada (sin manos/blind)" pero no la **resuelve**: sin definir manos-por-diente, la tabla es decorativa. Sustracción: el pacing no debe tener su propia variable libre; **derívalo del único recurso ya existente (Maña)**. Duración de un diente ≈ f(ranuras de Maña gastadas + Escobas necesarias). Una variable menos.

**(c) FALSABLE.** Invariante de presupuesto: **Σ(duración de los 12 dientes) ∈ [25,35] min en p50; techo p90 ≤ 40 min**; banda por diente declarada (p.ej. Manga ~6-8 min, Cantina ≤90s). El solver §14 lo valida sobre 1000 runs simuladas. MUERE si **p90 > 40 min** o si la **Cantina percibida > 90s**.

---

## SUB-TEMA 3 — Micro-frecuencias intra-sesión (#49) — contribuyo

**(a) Steelman.** El prompt admite que la premisa es **mayormente falsa** (el Envite con Trampa ya está en M1) 🟢. Residual real: falta el KPI de *time-to-first-trap-break*, no solo *time-to-first-escoba*.

**(b) Ataque.** No inventar "nota de micro-frecuencia" como prosa; basta **un KPI**. Sustracción: cero diseño nuevo, solo instrumentación.

**(c) FALSABLE.** KPI `time_to_first_fullería_jugada` con objetivo **p50 ≤ 120s** (el duelo de Trampas se SIENTE jugado dentro de los 2 primeros min). MUERE si p50 > 120s.

---

## Opinión sobre los demás clústers (huecos asignados parcialmente)

- **#24 Codex sin estado terminal.** A favor con matiz de mi gremio: cardinalidad conocida **"X/N huecos" SANA el wanting, no lo mata** — el SEEKING saludable (LD5) necesita un objeto *cerrable*; el FOMO tóxico nace del gap *infinito/temporizado*. Diseño que satisface ambos: **N conocido + beat de catarsis al 100% de cada sección + el grid revela el siguiente hueco como silueta al cerrar uno** (el wanting se renueva por *profundidad*, no por *infinitud*). FALSABLE: alarma si ratio abiertos:cerrados crece monótonamente (señal de gap diseñado-para-no-cerrarse). Es de Gemini liderar la cardinalidad; yo solo aporto que **terminal ≠ saciado** si cada cierre destapa una silueta nueva. ⚪ confianza en el número de N.
- **#12 Pre-mostrar el hueco de mañana.** Coherente con #24: cerrar sesión mostrando el hueco de MAÑANA como **silueta cerrable-pero-bloqueada, opt-in, SIN timer** (sin timer = no es live-ops, respeta B2P). FALSABLE: % retorno D7 atribuible al tease (A/B). 🟡
- **#26 Biblia de 1 pág + #39 firma social.** Fuera de mi gremio (Gemini lidera narrativa). Mi única nota de sistemas: el linkeo Diablo→hecho/ambigüedad es **coherencia falsable barata** (cada Diablo cita 1 hecho o 1 ambigüedad de la biblia) y **es el costo mínimo**; no veo sustituto más barato que no sea "no escribir 20 Diablos", lo cual contradice el Romancero. En #39, de mi lado: separar **identidad-de-build (siluetas de 3 Pactos)** de **solución-de-seed (la secuencia)** — exhibir lo primero, ocultar lo segundo, protege el foso sin matar la expresión social. 🟡

---

## Lo que solo yo aporto
1. **Jerarquía Z como regla de scheduler, no de render** (Z1 silueta > Z2 valor > Z3 estado > Z4 feedback; dos eventos Z3+ se SERIALIZAN, nunca comparten frame). Mata "papilla" con cero UI nueva.
2. **Lista nominal de las 7 reglas-core** y el principio de que **meta/delivery gateado NO cuenta** para el ≤7±2 — con método de conteo por verbalización del tester.
3. **Regla de conservación de complejidad:** +1 sistema de delivery ⇒ −1 unidad de carga core (no se acumula).
4. **Complementariedad falsable, no decretada:** Pacto vs Fullería es real solo si su EV se invierte en ≥1 estado de Mesa y Fullería no domina >85% de seeds.

## Vacíos (qué necesito del panel)
- **De Gemini:** la **cardinalidad N del Codex/Romancero** (¿12? ¿20?) y si la coherencia narrativa soporta linkear cada Diablo a la Biblia sin inflar scope; si "terminal + silueta nueva" sostiene el wanting narrativamente (#24/#12/#26).
- **De Meta AI (data L1 móvil):** **carga cognitiva REAL** — ¿7 reglas-core son demasiadas para onboarding móvil de hispanos-USA/LATAM? ¿el peor-caso visual @100×100px daltónico es legible en pantallas reales de gama media? Benchmarks de *time-to-first-meaningful-decision* en deckbuilders móviles para calibrar mis 120s. Y red-team del ≤7±2: ¿qué juego real escaló a 8-9 reglas-core y aún convirtió?

*Todos los números (≤9, 85%, 120s, p90≤40, X/N) son **objetivos-a-falsar**, no datos. No inventé contenido del GDD; donde el N del grid o las cifras de §9 no constan, lo marco ⚪.*
