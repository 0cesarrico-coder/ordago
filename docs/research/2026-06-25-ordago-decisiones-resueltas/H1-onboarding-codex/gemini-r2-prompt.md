# RONDA 2 — CROSS-REVIEW de RESOLUCIÓN · H1 — Onboarding, Codex y progresión · ÓRDAGO

Abajo están las TRES posiciones de Ronda 1 (Opus, Gemini, Meta AI), cada una comprometida con UNA opción por decisión. Tu tarea, manteniendo tu ASIENTO:
1. **STEELMAN** la postura ajena más fuerte en cada decisión donde difieras.
2. **ATAQUE**: por qué tu opción gana (dato/carta), o dónde la ajena es mejor y CAMBIAS.
3. **CONVERGE**: para CADA decisión, da la **recomendación final UNA opción** + confianza 🟢/🟡/⚪. Si genuinamente solo un experimento la cierra, dilo con el experimento + umbral (marca "CONTESTADO:").
4. NO te quedes en "depende de César": comprométete con la mejor recomendación dado lo que sabes.
Evidencia L1-L4. ≤850 palabras.

============================================================

----- R1 · OPUS -----
# Opus R1 — Resolución H1 (Onboarding, Codex y progresión) · ÓRDAGO

> Asiento: Diseñador de Sistemas (elegancia + flow). Cartas ancla cargadas y leídas:
> [[A1-elegancia-emergencia]] 🟢🟡, [[04-flow]] 🟢, [[LD5-curiosidad-seeking]] 🟢, [[08-hook-habitos]] 🟢/🟡.
> Nota transversal: la carta 08 marca que ÓRDAGO puede ser **premium Steam (T1/T2)**, donde D1/D7 no son
> KPI sino proxies de "Playtime Depth → reviews/anti-refund". Donde el panel argumenta "+pp D1", lo leo
> como "+profundidad de sesión y +probabilidad de reseña positiva". No cambia la dirección de mis votos,
> sí su justificación. Aun así, cada decisión la cierro con UNA opción.

---

## DC-4 · Denominador de onboarding

**(a) OPCIÓN ELEGIDA — Tutorial serializado: 7 reglas core descubiertas jugando, pero ≤5 *verbalizadas* por compresión-arquetipo, en 3 micro-mangas.** NO podo los Pactos.

**(b) Porqué (🟢):** [[A1-elegancia-emergencia]] — "Cognitive INP": el **INPUT** debe pedir 0% de carga cognitiva, la elegancia vive en el **OUTPUT tardío**. Podar Pactos baja el techo de profundidad (mata combinatoria, riesgo "Escoba con skins" = pierde el foso anti-envejecimiento que un estudio pequeño *sí* puede pagar). La solución no es quitar reglas, es **mover su aprendizaje al output**: el jugador ejecuta 7 reglas pero solo *nombra* ≤5, porque las otras 2 se comprimen en un arquetipo ("el Pacto siempre cobra después" = una etiqueta, no dos reglas). Diseño lenticular (Rosewater 🟢): superficie de 5 verbos para el novato, profundidad de 7 para el experto. [[LD5]] 🟢: generar curiosidad ANTES de enseñar mejora retención del tutorial → las mangas revelan, no instruyen.

**(c) Falsador:** Si en test de comprensión post-Manga-1 el tester **no puede ejecutar** una jugada de Pacto correctamente (>30% de error en la acción, no en nombrarla), entonces 7-descubiertas falló y debo podar a 5 core reales (opción Meta). El gate es *ejecución correcta*, no *recuerdo verbal*.

**(d) Experimento mínimo:** n≥40 testers nuevos, dos brazos (5-core-podado vs 7-core/5-verbalizado). Métrica gate: **% que ejecuta una fullería con Pacto sin ayuda en Manga 2 ≥80%** Y `reglas_verbalizadas_espontáneas ≤5` (cuenta cuántos sistemas distintos nombra sin prompt). Si el brazo de 7 cae <80% ejecución → cedo a Meta.

---

## DC-5 · Run continuo vs capítulos

**(a) OPCIÓN ELEGIDA — Run continuo [25–35]min con auto-save por turno (reconciliación operacionalizada como UNA cosa).** El "capítulo" es una **etiqueta retrospectiva de pausa**, no una pared mecánica.

**(b) Porqué (🟢/🟡):** [[04-flow]] 🟢 — quitar fricción de la acción y mantener "una más"; una pared de save entre mangas es una *interrupción del canal de flow* en el peor momento (cuando el jugador está absorto). El auto-save por turno **da el beneficio de Meta (cierras la app en cualquier turno, sesión móvil fragmentada LATAM) sin el costo de Gemini** (romper el ritmo). Mecánicamente es una sola decisión: persistir estado cada fin-de-turno; la UI puede *mostrar* un marcador de "Manga 1/4" como hito narrativo/respiro sin bloquear. Una opción, no dos sistemas.

**(c) Falsador:** Si la telemetría muestra que los jugadores que cierran a mitad de manga **no reanudan** (resume-rate <50% a las 24h) mientras los de save-entre-mangas sí reanudan (>70%), entonces el "punto de salida limpio" psicológico importa más que el flow continuo → adopto paredes de capítulo.

**(d) Experimento:** n≥200 sesiones móviles LATAM. Gate: **resume-rate a 24h ≥65%** con auto-save-por-turno Y **mediana de sesión dentro de [25–35]min** (si se desploma a <15min, la fragmentación gana y necesito capítulos como puntos de parada explícitos). Solo este dato (no L1 que yo tenga) lo cierra honestamente.

---

## DC-6 · Cardinalidad del Codex

**(a) OPCIÓN ELEGIDA — N=12 / M=18.** (Postura de Meta L1, no la mía previa ⚪ ni la ambición de Gemini.)

**(b) Porqué (🟢 para el principio, 🟡 para la cifra):** Cedo aquí conscientemente. [[LD5-curiosidad-seeking]] 🟢: el SEEKING se sostiene por **gap CERRABLE** — "gap grande = abandono; gap cerrable = motivación" — y la curiosidad **se SATURA (U-invertida)**. Una colección de 16/24 amplía el gap más allá de lo cerrable en sesión móvil fragmentada; el dato L1 de Meta (colecciones >12 ítems en móvil caen <5% completado) es la evidencia direccional que mi propio principio *predice*. El wanting se renueva por **PROFUNDIDAD revelada por entrada**, no por *cantidad* de entradas → 12 entradas con 2-3 capas de revelación c/u (el "terminal ≠ saciado") sostienen más SEEKING que 16 planas. Poda por sustracción ([[A1]]): cada entrada del Codex debe pagar renta en revelación, no en conteo.

**(c) Falsador:** Si con N=12 el **abandono entre 80–99% de completitud es <5%** PERO el D30 cae por **techo de contenido alcanzado demasiado pronto** (jugadores "terminan" el Codex y se van antes de D30), entonces 12 es muy poco y subo a 16. Es decir: el falsador no es "completan poco" sino "completan y se saturan".

**(d) Experimento:** brazos 12 vs 16, n≥150/brazo. Gates (los del panel): **D30 ≥8% sin timers** Y **abandono en 80–99% de completitud <5%**. Desempate: el brazo con **mayor mediana de profundidad-revelada-por-entrada vista** (¿el jugador abrió las sub-capas?) gana, no el de más entradas.

---

## DC-8 · Recompensa del 100% del Codex

**(a) OPCIÓN ELEGIDA — Estrictamente estética: "cantar de ciego" / skin / título cosmético.** NO desbloquea Diablo Fantasma como boss mecánico.

**(b) Porqué (🟢):** [[A1-elegancia-emergencia]] límite ético + [[LD5]] estado terminal sano. Atar una **recompensa mecánica que afecta el balance/solver (§14)** al 100% de colección crea un *gap no-cerrable para el jugador medio* (la mayoría nunca llega a 100%) → eso es escasez artificial que satura, no SEEKING sano. Y mete una variable de balance dependiente de completitud en el solver — deuda de elegancia (regla que no paga renta en *jugadas*, solo en grind). La recompensa cosmética **cierra el gap con satisfacción sin reabrirlo** (terminal ≠ saciado por profundidad ya revelada). Coherente con premium B2P / anti-FOMO.

**(c) Falsador:** Si la telemetría muestra que el cosmético **no mueve completitud** (los que llegan a 90% no empujan a 100%: tasa 90→100 <20%) y un focus group pide "recompensa con peso", entonces el cosmético es inerte y reconsidero una recompensa *meta no-balance* (p.ej. un modo, no un boss que toque el solver).

**(d) Experimento:** A/B cosmético vs "desbloquea modo opcional fuera-del-solver". Gate: **NPS/review-sentiment del endgame** y tasa 90→100. Nunca un boss dentro del solver: ese es un no-negociable de elegancia, no de dato.

---

## DC-9 · Hook 90s vs 120s

**(a) OPCIÓN ELEGIDA — 90s** (`time_to_first_fullería_jugada` p50 = 90s). Banda-muerte dura >120s.

**(b) Porqué (🟢):** [[04-flow]] 🟢 — en la FTUE (primeros 4–5 min) "quitar fricción de la acción" y la incertidumbre ≈0 para consolidar el modelo mental. El setup de la Mesa viva es *feel*, pero feel que retrasa la **primera jugada con agencia** compite contra el flow inicial. [[LD5]] 🟢: la curiosidad debe poder *cerrarse* pronto (primera fullería = primer cierre dopaminérgico). El dato de Meta (46% se va antes del min5) hace que cada 30s sea caro; 90s deja margen para 2–3 ciclos de cierre antes del minuto 5.

**(c) Falsador:** Si a 90s la **tasa de "primera fullería entendida"** (el jugador sabe *por qué* funcionó, consecuencia perceptible-Church) cae respecto a 120s en >10pp, entonces 90s atropella el modelo mental y la legibilidad pesa más que la velocidad → subo a 120s. Velocidad sin comprensión no es flow, es ansiedad.

**(d) Experimento:** brazos 90s vs 120s, n≥120/brazo. Gate: **D1/sesión-depth a 90s ≥ a 120s** Y **comprensión-de-primera-jugada ≥85%** (mini-quiz o ejecución repetida correcta). Si comprensión <85% a 90s → 120s.

---

## DC-11 · Poda de Diablo Fantasma + artefacto-puente del onboarding

**(a) OPCIÓN ELEGIDA — Podarlos del onboarding; mantenerlos como META GATEADO que aparece DESPUÉS de la Manga 1 (no eliminarlos del juego).**

**(b) Porqué (🟢):** Conecta directo con DC-4 y mi denominador `reglas_verbalizadas ≤5`. [[A1]] "Cognitive INP" 🟢: el INPUT temprano (D1) debe ser 0% carga cognitiva; un sistema meta (Codex/puente/Diablo Fantasma) presente en el frame de la Manga 1 **carga el input** y compite con el flow de la primera fullería. [[04-flow]] 🟢: en la FTUE la incertidumbre ≈0 → lo meta es incertidumbre del meta-loop, va *después*. [[LD5]] 🟢: revelar el meta como gap *después* de que el core esté cementado renueva el wanting por profundidad, en vez de abrumar. El criterio operacional del prompt es perfecto y lo adopto como gate: **si el tester nombra un sistema meta antes de la Manga 1, entró demasiado pronto.**

**(c) Falsador:** Si podar el puente/Diablo Fantasma del onboarding **baja la conversión a segunda sesión** (los testers sin "gancho de qué viene después" no vuelven: D1-return de la rama podada < rama-con-teaser en >8pp), entonces necesito al menos un *teaser* (silueta, no sistema) del meta en el onboarding → reintroduzco como **gap visible cerrable** ([[LD5]]: "haz visible el hueco"), nunca como regla verbalizada.

**(d) Experimento:** brazos onboarding-limpio vs onboarding-con-teaser-de-meta. Gate: **conteo de sistemas-meta nombrados antes de Manga 1 = 0** en la rama limpia (criterio del prompt) Y **D1-return ≥ rama-teaser**. Si D1-return cae >8pp → añado teaser visual (silueta del Diablo Fantasma), no el sistema.

---

## Dónde cedo y dónde no

- **CEDO ya en DC-6 (cardinalidad):** es mi postura más débil — mi previa era ⚪ (abierto). El dato L1 de Meta (>12 ítems caen <5% completado) lo predice mi propia carta LD5 (gap no-cerrable + saturación). Cedo a **N=12** salvo que el experimento muestre saturación-por-techo antes de D30 (entonces 16).
- **CEDO condicionalmente en DC-5 y DC-9:** acepto el flujo continuo y los 90s, pero ambos caen si el dato L1 de Meta muestra que la **legibilidad/punto-de-salida** importa más que la velocidad/continuidad (resume-rate <50% o comprensión <85%). Ahí Meta tiene la data que yo no.
- **NO cedo en DC-8 (boss dentro del solver) ni en el principio de DC-4/DC-11 (`reglas_verbalizadas ≤5`, meta fuera del frame de D1):** son no-negociables de elegancia/flow. Puedo ceder el *cómo* (teaser visual si la conversión lo exige) pero no el *qué*: el core loop queda determinista, legible y sin carga cognitiva de entrada; lo meta vive en el output retrospectivo y gateado. Si Gemini empuja ambición que no paga renta en jugadas, podo.

----- R1 · GEMINI -----
Here is the strategic alignment to maximize long-term retention and value (D7–D30) for *ÓRDAGO*.

---

### DC-4 · Denominador de onboarding
* **(a) Opción elegida:** Tutorial serializado de 7 reglas en 3 micro-mangas.
* **(b) Porqué:** *Inscryption* enseña sus mecánicas por capas (sacrificios, luego huesos, luego tótems) a través de muertes/partidas controladas (Confianza: 🟢). Reducir el tutorial a ≤5 reglas amputando los Pactos destruye el "alma" y la propuesta de valor única de *ÓRDAGO* (la tensión entre la trampa y perder el alma). Serializarlo en 3 mangas cortas mantiene la narrativa sin saturar.
* **(c) Falsador:** Si la tasa de abandono (`churn_rate`) durante la segunda micro-manga supera el 25% en playtests.
* **(d) Experimento:** Test de usabilidad con *n*=40 usuarios de perfil deckbuilder; umbral de éxito: `completion_rate_tutorial` >85% y comprensión de la sinergia Pacto-Fullería en el primer intento libre.

---

### DC-5 · Run continuo vs capítulos
* **(a) Opción elegida:** Run continuo [25–35]min con auto-save por turno.
* **(b) Porqué:** *Balatro* (sesión media de 30-40 min, Confianza: 🟢) demuestra que el "flow" ininterrumpido y la inercia del "una partida más" son los motores del D7-D30. La fragmentación móvil (LATAM/USA) no se soluciona mutilando la estructura en capítulos artificiales (que rompen la tensión de la apuesta), sino garantizando un guardado en la nube asíncrono y ultra-rápido por turno.
* **(c) Falsador:** Si la tasa de runs inconclusas (`unfinished_run_rate`) en dispositivos móviles supera el 30% tras una semana de juego.
* **(d) Experimento:** Soft launch en LATAM con *n*=500; umbral: retención D7 ≥18% usando auto-save instantáneo vs. guardado solo entre mangas.

---

### DC-6 · Cardinalidad del Codex
* **(a) Opción elegida:** N=16 / M=24 (Eje narrativo / Eje mecánico).
* **(b) Porqué:** Al ser un juego premium (B2P), el volumen de contenido percibido justifica el precio. En *Balatro*, la profundidad de la colección (150 comodines, Confianza: 🟡) es el principal motor de D30 (con tasas de retención superiores al 12% en jugadores hardcore). Limitar a N=12 / M=18 abarata la sensación de misterio y "seeking" del folklore del tahúr.
* **(c) Falsador:** Si a D14, el 85% de los jugadores activos reporta "fatiga por grind" o nula progresión en el Codex en las encuestas in-game.
* **(d) Experimento:** AB Test con *n*=1000 usuarios; Rama A (16/24) vs Rama B (12/18). Umbral: Victoria de A si el D30 es ≥2% superior al de B, sin canibalizar la satisfacción de juego.

---

### DC-8 · Recompensa del 100% del Codex
* **(a) Opción elegida:** Estrictamente estética (El "Cantar de ciego" completo + aspecto visual de baraja).
* **(b) Porqué:** *Slay the Spire* no bloquea el Acto 4 detrás del 100% del compendio, sino tras ganar con los 3 personajes iniciales (Confianza: 🟢). Bloquear al "Diablo Fantasma" (un jefe mecánico crucial) tras un grind del 100% del Codex frustrará al 95% de los compradores premium, generando reseñas negativas por "gateo injustificado". El 100% debe ser un trofeo de estatus de nicho.
* **(c) Falsador:** Si el ratio de reviews negativas en Steam/Play Store por "contenido jugable inaccesible" supera el 3% del total.
* **(d) Experimento:** Encuesta a *n*=150 entusiastas del género; umbral: >75% prefiere jefes finales desbloqueables por habilidad/rutas, no por completar colecciones.

---

### DC-9 · Hook 90s vs 120s
* **(a) Opción elegida:** Hook de 90 segundos para la primera Fullería jugada.
* **(b) Porqué:** Incluso en premium, el tiempo de enganche inicial en móviles es implacable. *Inscryption* te obliga a sacrificar tu primera carta en <60s; *Balatro* te tiene descartando en <30s (Confianza: 🟢). Dejar al jugador en fase de "setup narrativo" de la Mesa viva más allá de los 90s destruye el D1 en el mercado móvil hispano-USA.
* **(c) Falsador:** Si el `time_to_first_fullería_jugada` correlaciona con una caída de retención D1 por debajo del 35%.
* **(d) Experimento:** Test A/B con *n*=300; Onboarding rápido (Fullería a los 75s) vs Onboarding lento (Mesa viva a los 120s). Umbral: +10% de retención D1 en el grupo de 75s.

---

### DC-11 · Poda de Diablo Fantasma + artefacto-puente del onboarding
* **(a) Opción elegida:** Podarlos por completo del onboarding y convertirlos en Meta-Progreso Gateado.
* **(b) Porqué:** Mantiene el onboarding en el límite sagrado de ≤5 reglas verbalizadas activas. Al igual que el desbloqueo de las "Ascensiones" en *StS* o los secretos del tablero en *Inscryption* (Confianza: 🟢), el "Diablo Fantasma" y los artefactos rotos deben presentarse como susurros de endgame tras vencer la primera run. Esto dispara la retención D7 al dar un nuevo propósito de juego.
* **(c) Falsador:** Si los jugadores que completan su primera run no inician una segunda partida por percibir que el juego "ya terminó" (D1-after-win <50%).
* **(d) Experimento:** Test con *n*=200 usuarios; habilitar la revelación del Diablo Fantasma mediante cinemática interactiva inmediata post-victoria vs. no mostrar nada. Umbral: +15% de re-run en las siguientes 24 horas para el grupo con revelación.

---

### Dónde mi sesgo de ambición es más riesgoso
Es más riesgoso en **DC-6 (Cardinalidad del Codex N=16 / M=24)**. Si el mercado móvil de LATAM/USA hispano demuestra una fricción extrema hacia el coleccionismo premium de largo aliento en pantallas pequeñas, la ambición de diseño fallará. Cedería a la postura de Meta AI (N=12 / M=18) si la métrica de **`codex_engagement_rate` a D7 cae por debajo del 3%** en los playtests técnicos cerrados de Android.
----- R1 · META AI -----
ÓRDAGO · R1 Debate de Resolución

Asiento Data L1 + Red Team. No buscamos huecos, buscamos números que maten la ambigüedad.

DC-4 · Denominador de onboarding

OPCIÓN ELEGIDA → Tutorial serializado de 7 reglas en 3 micro-mangas, con tope duro de ≤5 reglas verbalizadas en manga 1 (las 2 de Pactos emergen en mangas 2-3 por compresión-arquetipo, no se podan)
→ porqué: Data L1 🟢: cada regla verbalizada extra suma ~+45s a time-to-win y resta ∼6pp D1; D1 industria móvil 2024 está en 26.5–27.7%, "bueno" 40%+. Con 5 verbalizadas iniciales mantenemos TTW <180s (estándar que escala enseña 3 acciones) y capturamos tu +10pp sin convertir ÓRDAGO en "Escoba con skins". Podar era atajo; serializar es la cirugía.
→ falsador: si el serializado no entrega D1 ≥35% en demo LATAM o TTW p50 >180s.
→ : A/B n=5,000 por brazo Android MX/CO/AR. Control=5 reglas podadas. Test=7 serializadas. Gate: test ≥+4pp D1 vs control Y TTW p50 ≤165s.[experimento]

DC-5 · Run continuo vs capítulos

OPCIÓN ELEGIDA → 4 mangas × 6–8min con auto-save por turno. Rechazo run continuo de 25–35min
→ porqué: L1 🟢 sesión fragmentada LATAM: 46% abandona antes del min5; patrón es "abrir en el bus, pocos minutos". Auto-save por turno salva progreso técnico, pero no crea cierre cognitivo. Sin victoria parcial explícita, la tasa de retorno cae. Gemini optimiza para flow Balatro PC; móvil LATAM no respeta maratones.
→ falsador: si run continuo + auto-save iguala o supera al control en % de retoma <24h tras cierre forzado en min 7.
→ : A/B n=4,000. Métricas: retoma 24h y D1. Gate: test continuo debe ganar por ≥3pp para justificarlo.[experimento]

DC-6 · Cardinalidad del Codex

OPCIÓN ELEGIDA → N=12 base / M=18 total. No negocio.
→ porqué: L1 🟢: en móvil LATAM, colecciones >12 ítems caen a <5% completado. Ese es el dato que me diste y es inamovible. Con N=16 de Gemini, matemáticamente sacrificas el gate D30≥8% sin timers y disparas abandono 80–99% por encima del 5% permitido. Opus quiere abierto; eso es ⚪ sin data. Red Team elige el techo que la gente realmente termina.
→ falsador: si una cohorte con N=16 logra ≥7% completado a D30 Y mantiene abandono 80–99% <5%.
→ : A/B n=6,000. N12 vs N16. Gate para subir: N16 debe cumplir ambos umbrales simultáneamente.[experimento]

DC-8 · Recompensa del 100%

OPCIÓN ELEGIDA → Estrictamente estética (skin, marco, taunt del tahúr)
→ porqué: L1 🟡: churn por vergüenza/dificultad en LATAM casual se activa cuando bloqueas poder detrás de metas que <5% alcanza. Con N=12, un "Diablo Fantasma" mecánico sería visto por pocos y resentido por el 95% restante, sin mover D30 agregado. La estética sostiene aspiración sin FOMO funcional, coherente con B2P premium.
→ falsador: si estética pura deja D30 <6% y la variante mecánica sube D30 ≥+3pp sin aumentar abandono 80–99%.
→ : A/B n=3,000 en usuarios con 70%+ Codex. Control=estética. Test=boss mecánico. Gate D30 y abandono.[experimento]

DC-9 · Hook 90s vs 120s

OPCIÓN ELEGIDA → Confirma ancla 90s para time_to_first_fullería_jugada p50
→ porqué: L1 🟢: 46% se va antes de min5 y cada 30s extra cuesta ∼6pp D1. 90s te deja 30s de colchón bajo la banda-muerte de 120s y cumple el <180s para 3 acciones. Mover a 120s es regalar D1 por elegancia de Opus.
→ falsador: si a 90s la comprensión de Pactos básicos post-tutorial cae <70%.
→ : A/B n=5,000. 90s vs 105s. Gate: mantener 90s salvo que comprensión caiga >10pp.[experimento]

DC-11 · Poda Diablo Fantasma + artefacto-puente

OPCIÓN ELEGIDA → Podar SÍ del onboarding. Mantener como meta gateado post-manga 2
→ porqué: L1 🟢: los marcamos sin lift D1 medible y cada elemento añade reglas verbales (+45s/-6pp D1). En minuto 1-3, peso muerto mata. Diferirlos preserva la elegancia de Opus sin pagar el impuesto de D1.
→ falsador: si podarlos reduce engagement con Pactos a D3 en >10pp vs control.
→ : A/B n=4,000. Control=con ambos en tutorial. Test=diferido. Gate: D1 +4pp sin caída D3.[experimento]

Dónde mi data es firme vs dónde es supuesto

Firme 🟢 e inamovible: DC-6 (>12 ítems = <5% completado), DC-4 y DC-9 (costo por regla: +45s/-6pp D1), DC-5 (46% abandono antes de min5). Aquí no cedo, es matemática de sesión LATAM.

Supuesto ⚪/🟡 donde cedo a A/B: DC-8 (impacto real de estética vs mecánico en D30, muestra histórica pequeña) y DC-11 (lift cero de Diablo Fantasma en onboarding es observado pero no a escala). En esos dos, si el experimento me falsifica, adopto la opción de Opus/Gemini sin pelea.