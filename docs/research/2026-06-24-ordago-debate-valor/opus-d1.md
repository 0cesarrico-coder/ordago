# ÓRDAGO — RONDA 1 · DICTAMEN: Director de Diseño/Sistemas + Analista de Lentes (Opus)

> Marco macro CONVERGIDO. LOCK 1 (sistema dual Mesa-viva + Trampa↔Fullería) y LOCK 2 (arte por A/B de feed) asumidos. Aquí solo las 3 decisiones de mecánica fina, a vara de clase mundial (foso A1, no power-creep, no extracción M1·LD7). Cartas con confianza 🟢/🟡/⚪.

---

## DECISIÓN 3 — Costo de los Pactos Oscuros

**Recomendación (Opción C, refinamiento de A):** el Pacto Oscuro **corrompe permanentemente un *slot* de Fullería** (no una Fullería concreta) — al tomarlo, ese slot deja de equipar maña y pasa a ser Pacto para el resto de la run; apilar un 2º Pacto consume tu 2º slot (build "0 Fullerías, todo Diablo" = legal pero te comes cada Trampa en crudo).

**Por qué es la de clase mundial (anclaje):** convierte dos pilas de Jokers paralelas en **un solo trade-off elegante** — *cambias tu maña (agencia anti-Trampa) por poder bruto del Diablo* — que es literalmente la fantasía del título "le hice trampa… pero el Diablo me cobró" (A1 🟢🟡: la opción dominante se mata sola, porque ir todo-Pacto te deja indefenso ante cada Envite con regla-trampa). El costo es **estructural y recurrente** (lo sientes en cada Envite donde extrañas esa Fullería), no un pellizco único que se olvida — eso es lo que separa fausto de "Joker renombrado" (M1·LD7 🟢🟡: costo transparente, irreversible dentro de la run pero con **saciedad alcanzable** — se puede ganar con 0, 1 o 2 Pactos; la run reinicia el saldo, no hay ratchet entre runs ni FOMO). La quema de *una Fullería específica* (A literal) era un acantilado binario y feo; el **slot** lo vuelve tunable por número de slots y diegéticamente limpio ("el Diablo te compró esa mano").

**Riesgo principal + mitigación:** que emerja un build degenerado "0 Fullerías / 2 Pactos" que trivialice todo el sistema de Trampa (mata LOCK 1). **Mitigación auto-balanceante:** el Envite del Diablo escala su regla-trampa de modo que sin Fullerías comes la Trampa entera — el costo del slot se paga en dificultad, no en un número arbitrario; el sistema se equilibra a sí mismo (A1: el trade-off es real porque ambos lados duelen).

**Test/kill más barato:** prototipo de papel, 1 Manga, 2 slots, 3 Pactos Oscuros en post-its. **Kill si** (a) NADIE toma un Pacto en 10 partidas (costo prohibitivo → bajar el peso de la Trampa o subir el delta de poder del Pacto), **o** (b) el build "0 Fullerías" gana >55% sin sentir la Trampa (costo decorativo → subir escalado del Envite). Confianza 🟡, validar en cohorte propia.

---

## DECISIÓN 4 — Bucketing del Diablo Fantasma

**Recomendación (Opción C, banda híbrida sobre fantasmas REALES):** el Diablo Fantasma es **siempre la run de otro jugador real** (sale del pool de fantasmas cuyo score cae en la banda [tu mejor histórico, tu mejor ×1.10] de esa semilla), eligiendo cerca del borde bajo de la banda en sesiones tempranas y subiendo dentro de la banda conforme ganas; **fallback** a un Diablo sintético a tu-mejor ×1.05 solo si no hay fantasma real en banda (cold-start).

**Por qué es la de clase mundial (anclaje):** sirve a las DOS mitades de Action-Social (41% del engagement LATAM/MX, QF 🟡): **Competición** (gap cerrable) + **Community** (un humano real con handle, no un clon de ti mismo — el delta-puro Opción B es un treadmill solipsista que mata la mitad social del cluster). El borde de banda relativo a TU histórico es Festinger puro (LD6 🟢/🟡): el rival es demostrablemente "casi tú +un poco" → "por poco lo tengo" → "una mano más". Evita el desaliento del percentil-puro (Opción A: ruidoso con población chica, te puede emparejar con una varianza de semilla brutal) y el aburrimiento del rival trivial. La banda, no el delta fijo, da headroom para que ganar **suba** la vara honestamente (Fiero ganado, no regalado — M1 🟢🟡).

**Riesgo principal + mitigación:** que el rubber-band se note → "esto está amañado", condescendiente, mata el Fiero y retira goodwill (M1). **Mitigación:** la banda se llena con scores **reales** (jamás fudgeados), se muestra el **handle + margen no trivial** del rival, y **nunca se baja la vara tras una derrota** (bajar el rival al perder es el gesto paternalista que delata el truco). El rubber-band solo sube, dentro de scores humanos verídicos.

**Test/kill más barato:** A/B de "¿inició otra run en <10 min tras esta?" entre tres brazos: banda-real vs delta-puro vs percentil-puro (Steamworks leaderboards bastan). **Kill si** la banda-real no supera a los otros dos en re-engagement, **o** si encuestas cualitativas detectan "se siente amañado" >20% (entonces colapsar a delta-puro honesto). Confianza 🟡, validar en cohorte propia.

---

## DECISIÓN 5 — Asistencia de UI al verbo "sumar 15"

**Recomendación (Opción D, asistencia ESCINDIDA y gated por onboarding↔maestría):** separar la ayuda por *qué acto cognitivo toca* y graduarla. **Siempre ON (todas las runs):** legibilidad de índices (8/9/10 grande en figuras) + **suma acumulada de TU selección actual**. **NO default permanente:** el resaltado de *cartas de la mesa que completan el 15* es un **"modo aprendiz"** ON por defecto las primeras ~3 runs / hasta tu 1ª victoria, luego se **desvanece con aviso** ("el Diablo ya no te marca las cartas"), y queda como toggle de accesibilidad en opciones.

**Por qué es la de clase mundial (anclaje):** el verbo tiene DOS actos — (1) aritmética (¿suma 15? acarreo, valor de figuras) = **fatiga estéril, un impuesto**; (2) búsqueda combinatoria/decisión (cuál de los muchos 15 hago, dada la Trampa, mis Pactos, lo que el Diablo sembró, qué Mata capturo) = **donde viven el Fiero (LD2 Hard Fun 🟢) y TODO el espacio de decisión (A1 🟢🟡)**. Índices + suma acumulada matan solo (1) — ganancia pura, cero costo (A5 🟡 legibilidad silueta→valor). Pero el resaltado de la mesa de Gemini toca (2): con la **Mesa adversarial poblada (LOCK 1)**, el lado-mesa ES donde la siembra del Diablo crea la decisión; marcar "estas cartas completan tu 15" hace la búsqueda combinatoria por ti → **sí cruza a solucionador parcial** en régimen de maestría (el panel discutió esa ayuda *antes* de poblar la Mesa; bajo el dual es más peligrosa de lo que asumió). Gatearla resuelve onboarding↔maestría explícitamente: el novato aprende el verbo rápido (<90 s, métrica GDD §13); el maestro juega en crudo y conserva el avistamiento (Fiero LD2, foso A1). No deja una muleta permanente que el jugador resienta (M1 🟢🟡) y deja el cierre satisfactorio en manos del jugador (LD7 🟢).

**Riesgo principal + mitigación:** que el desvanecimiento se sienta como un castigo / dificultad súbita ("me quitaron mi ayuda") → frustración en la transición. **Mitigación:** desvanecer **gradual** (resaltado que baja de opacidad a lo largo de la run-3, no corte seco), enmarcarlo diegéticamente ("el Diablo deja de soplarte") y mantener el toggle de accesibilidad permanente para quien lo necesite — la maestría es el default, no una imposición.

**Test/kill más barato:** telemetría de "tiempo a primera Escoba" + "ratio de 15s descubiertos vs confirmados-tras-resaltado". **Kill del resaltado-mesa si** (a) con él ON los jugadores dejan de *buscar* y solo confirman lo iluminado (cae a clicker → retirarlo antes, viola A1), **o** (b) tras el desvanecimiento la retención cae fuerte (la ayuda creó dependencia, no aprendizaje → rediseñar el onboarding del verbo, no reinstaurar la muleta). Índices + suma acumulada se quedan pase lo que pase. Confianza 🟡, validar en cohorte propia.

---

**Interdependencia (nota de sistemas):** las tres se acoplan vía LOCK 1. La #3 (slot corrompido) hace que la maña sea un recurso *con precio*, lo que da peso real al avistamiento de la #5 (cada Fullería que NO quemaste por un Pacto debe ganarse jugando el verbo en crudo). La #5 protege que ese verbo siga siendo decisión (A1) y no clicker, condición sin la cual la #4 (competir por score) compara *skill*, no *quién tiene más automatización*. Resolver las tres en la dirección "el jugador paga, busca y compite de verdad" es lo que mantiene el foso A1 coherente.

**La decisión que más mueve la aguja hacia clase mundial de las tres es la #3 (Pacto Oscuro corrompe un slot de Fullería) porque** es la única que convierte el sistema dual de "dos pilas de Jokers atornilladas" en **un solo trade-off faustiano elegante (A1)** que entrega literalmente la fantasía del título — cambias tu maña por el poder del Diablo y lo pagas en cada Envite — mientras la #4 y la #5, aun siendo de primer nivel, son ejecución excelente sobre un foso que la #3 es la que define.
