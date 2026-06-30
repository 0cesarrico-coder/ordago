# RONDA 1 — Director de Diseño/Sistemas + Analista de Lentes

> Lectura independiente a ciegas del GDD macro de ÓRDAGO v0.1. Red-team honesto, no validación.
> Eje: valor entregado vs declarado; profundidad matemática del motor Puntos×Suerte; cobertura
> emocional QF→Lazzaro→MDA. Anclas: cartas A1–A5, lentes LD0–LD7, gates M1·LD7.

---

## A. Propuestas de valor que LEO en el diseño (entregado, no declarado)

Para cada una: la promesa, y el **sistema-que-la-entrega (§N)** o **HUECA**.

1. **"Nuestra baraja por fin tiene su gran juego" (pertenencia cultural pre-cacheada).**
   Sistema que la entrega: §7.1–7.2 (40 cartas, sin 8/9, figuras 8/9/10), §7.5 (las Matas como
   jerarquía de rareza *gratis* y reconocible), §11 (Posada/Día de Muertos). **ENTREGADA** y es la
   única propuesta verdaderamente defendible. Ancla A3 🟡⚪ (mito comprimido: la baraja española +
   las matas se reconocen en <1 s para el público hispano, sin tutorial) y A5 🟡 (legibilidad por
   familiaridad). Es valor real porque el reconocimiento NO es skin: las Matas son a la vez ficción
   y mecánica de rareza (§7.5). Confianza de que ese público existe y paga: 🟡 "validar en cohorte
   propia" — el GDD afirma "cientos de millones" pero no prueba willingness-to-pay en Steam (§19
   lo admite como riesgo Media).

2. **"Le hice trampa al Diablo y gané" (fantasía del trickster que rompe la banca).**
   Sistema: §5 (arco de 4 fases), §7.6 (Pactos como tratos con el Diablo), §7.10 (El Envite del
   Diablo con regla-trampa), §10 (el Diablo reacciona diegéticamente). **PARCIALMENTE ENTREGADA.**
   El arco emocional está bien especificado (A4 🟢🟡, narrativa embebida sin peaje). PERO la
   fantasía *del trickster* — vencer con **maña/engaño**, no con fuerza bruta (§12 subtexto) — NO
   tiene su sistema propio salvo la propuesta tentativa de **Fullerías** (§7.6, §19 decisión 3),
   que está marcada como decisión abierta, no como sistema. Sin Fullerías, "le hice trampa" es
   idéntico mecánicamente a "optimicé mi build de Jokers" de Balatro: ganas por **acumulación
   multiplicativa**, no por **engaño**. La palabra "trampa" es flavor sobre un motor que no engaña.
   Ver Falla Fatal #2.

3. **"Sumar 15 es un verbo fresco que aprendo en minutos" (onboarding casi-nulo + novedad).**
   Sistema: §6.1–6.2 (loop de mano), §7.3 (motor de Escoba). **ENTREGADA como onboarding; HUECA
   como profundidad diferencial.** El "sumar 15" es genuinamente más legible que la jerarquía de
   manos de póker (A5 🟡, A3 🟡) — eso es real para el hispano y para el global (§3.2 doble
   alcance). PERO como *espacio de decisión* (A1 🟢🟡) "sumar 15" es **más pobre** que la mano de
   póker, no más rico: ver Falla Fatal #1. El valor entregado es accesibilidad; la novedad es de
   superficie aritmética, no de profundidad de decisión.

4. **"Build-as-signature: mi estilo de juego es mi firma" (expresión/dominio).**
   Sistema declarado: §4 (Expresión: "secuencias/pares/matas/Escobas"), §7.4 (jerarquía de
   Jugadas), §7.6 (Pactos build-defining), §8 (Tahúres con afinidad de palo). **PARCIALMENTE
   ENTREGADA / en riesgo de HUECA.** La jerarquía de Jugadas (§7.4) existe pero está descrita como
   "capas de bonus/multiplicador" — es decoración aditiva sobre el mismo evento "sumar 15", no
   ramas de build mutuamente excluyentes. Para que sea firma (A1 🟢🟡) necesita que elegir
   "arquetipo pares" **mate** la opción "arquetipo secuencias" en esa run (test de elegancia A1:
   ¿la opción dominante se mata?). El GDD no especifica ningún trade-off que fuerce esa exclusión.
   Riesgo: todos los builds convergen a "más Escobas + más ×Suerte". Ver Falla Fatal #1.

5. **"El Diablo Fantasma: el leaderboard es parte del cuento" (competición async diegética).**
   Sistema: §4 (Diablo Fantasma), §8 (Tablas de Almas, semillas diarias). **ENTREGADA
   conceptualmente, sub-especificada mecánicamente.** Es la mejor idea de cobertura del cluster
   Action-Social/Competition (LD6 🟢/🟡, LD3 🟢): encarnar el high-score ajeno *como el Diablo*
   convierte el menú de leaderboard en ficción. Excelente. PERO LD6 exige que el gap sea
   **cerrable** (Festinger) → requiere **bucket leaderboards** (te emparejan con un Diablo Fantasma
   a tu alcance, no con el top-0.1%). El GDD dice "el high-score de otro jugador en tu semilla" sin
   especificar matchmaking de skill → si te toca un score imbatible, el co-driver se vuelve
   desaliento. Falla de especificación, no de concepto.

6. **"Pactos Oscuros: poder enorme a cambio de un precio (riesgo/recompensa faustiano)."**
   Sistema: §7.6 (Pactos Oscuros con costo), §8 (Codex/Romancero como descubrimiento).
   **ENTREGADA y es la veta más profunda del diseño.** Es A1 🟢🟡 puro: un trade-off real con
   consecuencia perceptible, temáticamente perfecto (el precio de tratar con el Diablo). Sirve a
   Discovery (LD3 🟢, bajo Creativity) y a SEEKING/curiosidad (LD5 🟢). Único pero: está listado
   como **un subtipo entre seis** (§7.6), no como el eje central. Debería ser un pilar. Ver
   Recomendación.

7. **"Submission/relax: una mano más" (retención del core loop).**
   Sistema: §4 (Sumisión: loop "una mano más", sesiones cortas), §6.2 (30–45 s/mano). **ENTREGADA
   por estructura**, pero es genérica del género (Balatro ya la tiene). En LATAM Submission/Relax
   = 32% de engagement y **retiene el core loop** (LD4 🟡). El ritmo está especificado; el valor es
   real pero no diferencial.

8. **"Cosmología de palos = identidad de build" (Oros=economía, Espadas=mult…).**
   Sistema: §7.1. **HUECA hoy (declarada, no entregada).** §19 decisión 5 ADMITE que no está
   decidido si las afinidades son "fuertes o ligeras". Una propuesta de valor cuyo sistema el
   propio GDD marca como indefinido es, por definición, hueca hasta que se resuelva. Si las
   afinidades son ligeras, los palos son color-coding sin profundidad de build (viola A1).

---

## B. Fortalezas (top 3)

1. **Las Matas como sistema de rareza ya-internalizado (§7.5) — A3 🟡⚪ + A5 🟡.**
   Esto es craft real, no marketing. Balatro tuvo que *enseñar* qué es una carta legendaria; ÓRDAGO
   hereda "As de Espadas > As de Bastos > 7 de Espadas > 7 de Oros" como conocimiento de infancia
   del público hispano. Un símbolo pre-cacheado que carga connotación en <1 s (A3): "la dorada que
   sueñas capturar" ya tiene peso emocional *antes* de jugar. Es el mejor matrimonio ficción↔sistema
   del documento. Confianza 🟡 (canónico cultural, validar reconocimiento en cohorte no-hispana).

2. **El Diablo Fantasma como encarnación diegética del oponente async (§4, §8) — LD6 🟢/🟡, LD3 🟢.**
   Resuelve elegantemente el problema que Balatro NO resuelve: dar competición a Action-Social
   (41% de engagement MX, LD4 🟡) sin PvP en vivo. Vestir el leaderboard de Diablo es coherencia
   tema↔sistema de primer orden. Es la propuesta con mayor techo de viralidad/watchability (§8).
   (Pendiente: bucketing, ver Propuesta #5.)

3. **Pactos Oscuros con costo (§7.6) — A1 🟢🟡 + LD5 🟢 + LD7 🟢/🟡.**
   El único sistema que genera trade-off genuino *y* se mantiene del lado sano de LD7 (la saciedad
   es alcanzable: tomas el Pacto, pagas el precio, cierras el gap — no hay FOMO ni timer que reabra
   el deseo). Deposita en M1 🟢🟡 (Goodwill) porque el costo es transparente y diegético. Es la
   semilla del "rompí mis propias reglas" (Pilar 3) — pero hoy está enterrada como subtipo.

---

## C. Fallas fatales (top 3)

1. **★ El motor "sumar 15" puede ser MÁS POBRE en espacio de decisión que la mano de póker que
   reemplaza (§6.1, §7.3, §7.4) — viola A1 🟢🟡, el foso anti-envejecimiento.**
   Steelman primero: "sumar 15 a target fijo es legible (A5) y deja que los Pactos (§7.6) carguen
   la profundidad, igual que en Balatro la mano es trivial y los Jokers son el juego." Cierto en
   parte. Refutación: en Balatro la **selección de la mano** ES decisión (qué 5 cartas de 8,
   descartes, qué escalera vs full). En ÓRDAGO, "sumar 15" es un **problema aritmético con solución
   a menudo única o casi-única**: dado tu mano, los subconjuntos que suman 15 son pocos y
   computables — la decisión colapsa a "¿hay un 15? sí/no". Eso es un *puzzle de aritmética*, no un
   *espacio de decisión que se renueva cada partida* (test A1: ¿la decisión se renueva cada run?).
   La jerarquía de Jugadas (§7.4) se añade como "bonus" aditivo, no como ramas que se maten entre
   sí. **Riesgo de craft**: el motor depende 100% de los Pactos para tener profundidad, con un verbo
   core que aporta menos decisión que su referente. Si el prototipo de rectángulos (§14) muestra que
   "una mano más" no aparece SIN Jokers, el verbo está hueco. Confianza ⚪ (razonamiento de sistemas,
   falsable en el prototipo).

2. **"Le hice trampa al Diablo" no tiene sistema de trampa (§5, §7.6, §12, §19-dec.3) — promesa
   A4 🟢🟡 no entregada por mecánica.**
   La fantasía declarada (§5, §12) es el **trickster**: vencer con *maña y engaño*, el arquetipo
   pan-hispano del que le hace trampa al Diablo. Pero el motor entrega **optimización
   multiplicativa** (§7.7), que es la fantasía del *ingeniero/alquimista*, no del *tahúr tramposo*.
   Ganas porque tu engine escala, no porque engañaste a nadie. El único sistema que entregaría
   "trampa" — las **Fullerías** (§7.6, §19-dec.3) — está marcado como decisión abierta y como
   "evaluar si añade profundidad". Resultado: la propuesta de valor #2 (la fantasía central del
   §5) es hoy **parcialmente HUECA**: el tema promete engaño, la mecánica entrega aritmética
   escalada. A4 🟢🟡 exige que el mundo cuente por causa-efecto; aquí la causa (trampa) no produce
   el efecto (no hay verbo de engaño). Es el divorcio tema↔mecánica más grande del doc.

3. **Hueco de cobertura: Mastery-Achievement y Discovery están servidos en superficie pero el
   cluster Immersion-Creativity/Expression depende de un sistema indefinido (§4, §7.1, §19-dec.5) —
   LD4 🟡, LD3 🟢.**
   Auditoría QF (LD4 🟡, rejilla de clusters):
   - **Action-Social (41% MX):** Diablo Fantasma (§4) ✔ pero sub-especificado (bucketing).
   - **Mastery-Achievement (27%):** Codicia/stakes (§8), Envites boss (§7.10) ✔ — el espinazo,
     bien cubierto.
   - **Immersion-Creativity (18%, incl. Discovery bajo Creativity, LD3 🟢):** aquí está el hueco.
     **Discovery** ✔ (Pactos Oscuros, Romancero, §8 — fuerte). Pero **Design/Expression**
     ("build-as-signature", §4) descansa sobre (a) jerarquía de Jugadas que es aditiva no
     excluyente (§7.4, ver Falla #1) y (b) afinidades de palo que el GDD admite no haber decidido
     (§19-dec.5). Un cluster cuyo sistema de entrega el propio documento marca como indefinido =
     **hueco de cobertura** (LD4: hueco = cluster sin sistema). El jugador Design/Creativity no
     tiene garantizado un sistema que sirva su motivación.
   No es un hueco letal de *ausencia* (como sería olvidar competición), sino de **entrega
   indefinida**: la firma de build promete expresión que el motor aún no está diseñado para
   producir. Confianza 🟡/⚪.

---

## D. Recomendación #1 (mayor apalancamiento)

**Convertir las Fullerías en el SEGUNDO eje del motor, y rediseñar el verbo core para que las
Jugadas (§7.4) sean ramas mutuamente excluyentes — no bonus aditivos.**

Esto ataca simultáneamente las tres fallas fatales: da sistema a "le hice trampa" (Falla #2),
añade espacio de decisión que el "sumar 15" solo no tiene (Falla #1), y crea las ramas de build
que la Expresión necesita (Falla #3).

- **Cambio concreto al GDD:**
  1. Promover **Fullerías** de "decisión abierta" (§19-dec.3) a sistema confirmado (§7.6): un set
     de verbos de **engaño con riesgo** — robar una carta de la Baza del Diablo, forzar un 15
     falso, esconder una Mata, mirar la siguiente carta — cada uno con un **tell** (si el Diablo te
     "pilla", penalización). Eso entrega la fantasía trickster *mecánicamente* (A4 🟢🟡) y deposita
     en M1 🟢🟡 (transparencia: el riesgo es visible).
  2. Reescribir §7.4 para que **elegir un arquetipo de Jugada cierre otros** en esa run (p. ej. un
     Pacto "las Secuencias cuentan como Escobas" **deshabilita** los bonus de Pares) → fuerza el
     test A1: la opción dominante se mata, la build es firma.
- **Criterio de kill:** si en playtest de rectángulos (§14) los jugadores con Fullerías y los sin
  Fullerías producen la **misma distribución de decisiones** (las Fullerías se ignoran o se toman
  siempre sin tensión), las Fullerías son ruido → matar y volver a Pactos puros (la rec. conservadora
  del §19-dec.3). Igualmente, si los arquetipos de Jugada convergen a un único build óptimo medido
  por win-rate, la jerarquía §7.4 es decorativa → colapsar a "solo Escobas + Pactos".
- **Test más barato:** prototipo de papel/rectángulos de **una sola Manga** (ya en scope §14) con
  dos variantes A/B: (A) Escoba puro + Pactos; (B) Escoba + Fullerías + Jugadas excluyentes. Mide
  (i) ¿aparece "una mano más" sin juice? (ii) ¿hay ≥2 builds ganadores distintos? (iii) ¿los
  testers describen su victoria con el verbo "engañé" o con "optimicé"? Coste: un fin de semana,
  cero arte (coherente con "rectángulos primero", §14/§15).

---

## E. Apuesta falsable

**"ÓRDAGO no entregará su valor a menos que el verbo core 'sumar 15' demuestre, en el prototipo de
rectángulos de UNA Manga (§14), que produce el momento 'una mano más' y al menos dos builds
ganadores distinguibles SIN depender enteramente de los Pactos — es decir, que el motor de
decisión del Escoba sea ≥ al de la selección de mano de póker que reemplaza (A1 🟢🟡). Si la
decisión colapsa a un puzzle aritmético casi-único resuelto por los Jokers, ÓRDAGO es un reskin
cultural de Balatro con un verbo más pobre, y su único valor defendible será la pertenencia
cultural de la baraja/Matas (§7.5) — valioso, pero no 'clase mundial de diseño'."**

---

## F. Rúbrica (1–5)

| Dimensión | Nota | Justificación anclada |
|---|---|---|
| Claridad de propuesta central | **4** | "Balatro hispano + sumar 15 vs el Diablo" es nítido (§1, §3). Penaliza –1 porque mezcla dos propuestas (cultural + verbo) sin jerarquizar cuál es el moat. |
| Entrega del valor | **2.5** | La pertenencia cultural (§7.5) se entrega; la fantasía trickster (§5/§12) NO tiene sistema (Falla #2); la expresión (§4) depende de sistemas indefinidos (§19-dec.5, Falla #3). |
| Cuerpo elegante (A1 🟢🟡) | **2** | El verbo core arriesga colapsar a puzzle aritmético (Falla #1); Jugadas aditivas no excluyentes; afinidades de palo sin decidir. Salvado parcialmente por Pactos Oscuros. |
| Originalidad del verbo core | **3** | "Sumar 15" es fresco en presentación y legibilidad (A5 🟡) pero menos profundo en decisión que su referente (A1). Original de superficie, no de espacio de decisión. |
| Fantasía/tema (A2–A4) | **4** | Arco de 4 Mangas (§5), Diablo diegético (§10), frame faustiano (§7.6) son fuertes (A4 🟢🟡). –1 porque la mecánica no entrega el *engaño* que el tema promete. |
| Mito en 1 s (A3 🟡⚪) | **5** | Diablo + tahúr + baraja española + Matas + calaca Posada (§11) se reconocen <1 s para el público objetivo. Mejor carta del documento. |
| Cobertura emocional (LD3/LD4 🟢/🟡) | **3** | Action-Social y Mastery cubiertos; Discovery fuerte; Expression/Design hueco (Falla #3). Sin huecos de *ausencia* totales, sí de *entrega indefinida*. |
| Verdad del jugador | **3** | "Le hice trampa al Diablo y gané" (§5) es una verdad emocional poderosa, pero hoy el jugador sentirá "optimicé un engine", no "engañé" — la verdad declarada ≠ la entregada hasta resolver Fullerías. |

> **Síntesis R1:** ÓRDAGO tiene el mejor *mito comprimido* del campo (A3, §7.5/§11) y una cuña de
> cobertura async excelente (Diablo Fantasma). Su riesgo de craft no es estético ni de mercado: es
> que el **verbo core "sumar 15" sea más pobre en decisión** que la mano de póker (A1, Falla #1) y
> que la **fantasía trickster carezca de sistema** (Falla #2). Ambas se resuelven con la misma
> palanca: elevar Fullerías + Jugadas excluyentes a ejes del motor. El prototipo de una Manga
> (§14) las falsa por centavos. No asciendo ningún 🟡 a 🟢; toda afirmación de mercado queda
> "validar en cohorte propia".
