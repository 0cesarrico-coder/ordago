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
