# ÓRDAGO · CROSS-REVIEW RONDA 2
**Asiento:** Diseñador de Sistemas (Elegancia + Flow).  
**Cartas ancla:** [[A1-elegancia-emergencia]] 🟢, [[04-flow]] 🟢, [[LD5-curiosidad-seeking]] 🟢, [[08-hook-habitos]] 🟢/🟡.

---

### DC-4 · Denominador de onboarding

* **STEELMAN (Gemini):** Mantener las 7 reglas sin podar protege el foso de diseño. Amputar los Pactos para simplificar el onboarding degradaría a *ÓRDAGO* a un juego de bazas común ("Escoba con skins"), destruyendo su propuesta de valor premium de largo plazo.
* **ATAQUE:** No hay conflicto real, sino un problema de *empaquetado*. Gemini asume que para enseñar 7 reglas hay que explicarlas todas. Meta AI y yo demostramos que, mediante **compresión por arquetipo** y revelación tardía, el jugador ejecuta las 7 reglas pero su cerebro solo procesa ≤5 etiquetas verbales. Reducimos la fricción cognitiva de entrada sin tocar el diseño del solver.
* **RECOMENDACIÓN FINAL:** **Tutorial serializado (7 mecánicas, ≤5 verbalizadas en Manga 1, Pactos emergen en Manga 2-3).**  
* **CONFIANZA:** 🟢. Alineación absoluta en preservar la complejidad del sistema mediante cirugía didáctica.

---

### DC-5 · Run continuo vs capítulos

* **STEELMAN (Meta AI):** El dato de Meta es demoledor: 46% de los jugadores en LATAM móvil abandonan antes del minuto 5. Sin un punto de parada explícito y una victoria parcial clara (capítulo), el jugador sufre fatiga de decisión y abandona la sesión sin el "cierre cognitivo" de haber completado algo, arruinando el retorno.
* **ATAQUE:** Meta AI quiere curar la fragmentación de la sesión amputando el flow. Cortar el juego en capítulos rígidos destruye el bucle de "una partida más" de *Balatro* o *Slay the Spire* ([[04-flow]], [[08-hook-habitos]]). El auto-save por turno resuelve la sesión fragmentada (seguridad técnica de cerrar la app cuando quieras), y los hitos narrativos entre mangas dan el "respiro" psicológico sin necesidad de imponer un muro mecánico.
* **CONTESTADO:** Experimento A/B móvil (n≥4,000 MX/CO). Rama A: Run continuo [25-35]min con auto-save y hitos blandos. Rama B: 4 capítulos bloqueados de 6-8min.  
* **Umbral de éxito:** Rama A gana si el **D1-return es ≥ Rama B** Y la **tasa de reanudación (resume-rate) a las 24h es ≥65%**. Si la reanudación en A cae por debajo del 50%, la fragmentación cognitiva de Meta es real y adoptamos capítulos.

---

### DC-6 · Cardinalidad del Codex

* **STEELMAN (Gemini):** En un modelo premium B2P, el contenido es percibido como valor. Un Codex pequeño (N=12) puede dar sensación de "juego corto", provocando reembolsos prematuros en Steam y matando el "seeking" ([[LD5]]) de los coleccionistas hardcore en D30.
* **ATAQUE:** Gemini confunde cantidad con profundidad. Rellenar el Codex con 16/24 entradas planas satura el canal de curiosidad y genera un gap inalcanzable para el jugador en pantallas pequeñas (donde colecciones >12 caen a <5% de completitud). Aplicando [[A1]] (diseño lenticular): limitamos a N=12 entradas base, pero cada una con 3 sub-capas de lore/mecánicas reveladas por maestría. Más misterio, menos inventario plano.
* **RECOMENDACIÓN FINAL:** **N=12 base / M=18 total** (priorizando capas de revelación por entrada).  
* **CONFIANZA:** 🟢 (Cedo mi postura abierta de R1 ante la solidez del dato de Meta).

---

### DC-8 · Recompensa del 100% del Codex

* **STEELMAN (Meta/Gemini):** No hay debate aquí, pero la fuerza de esta postura unificada radica en la ética de diseño. Bloquear al "Diablo Fantasma" (boss mecánico) detrás del 100% del Codex alienaría al 95% de la base de jugadores casuales que jamás completarán la colección.
* **ATAQUE:** Cualquier intento de atar balance o contenido jugable core al grind del 100% rompe la elegancia del solver e introduce frustración por FOMO, contraria a nuestro target premium.
* **RECOMENDACIÓN FINAL:** **Recompensa estrictamente estética (Cantar de ciego completo + skin de baraja).**  
* **CONFIANZA:** 🟢.

---

### DC-9 · Hook 90s vs 120s

* **STEELMAN (Sistemas - R1 propia):** Un setup de 120s permite construir la atmósfera de la "Mesa viva", asentando el tono folclórico de misterio antes de exigir interacción.
* **ATAQUE:** El romanticismo de los 120s colisiona contra el abismo de la retención móvil. Con un 46% de fuga antes del minuto 5, regalar 30 segundos en atmósfera inerte es un suicidio comercial. El flow exige "quitar fricción de la acción" ([[04-flow]]) de inmediato. La primera fullería debe jugarse en el segundo 90; la mesa se "siente" mientras se juega, no antes.
* **RECOMENDACIÓN FINAL:** **90 segundos para `time_to_first_fullería_jugada` p50.**  
* **CONFIANZA:** 🟢.

---

### DC-11 · Poda de Diablo Fantasma + artefacto-puente

* **STEELMAN (Meta/Gemini):** Retrasar la introducción del Diablo Fantasma y el meta-progreso hasta después de la Manga 2 (Meta) o tras la primera victoria (Gemini) garantiza un D1 blindado, libre de cualquier ruido ajeno al core de bazas y trampas.
* **ATAQUE:** Si ocultamos el meta-progreso por completo hasta la primera victoria (que toma ~30 minutos), el jugador móvil puede percibir *ÓRDAGO* como un juego plano de bazas y abandonar antes de ver el loop real. Necesitamos el "horizonte de deseo" ([[LD5]]). La solución elegante es **podarlos como mecánicas** en el onboarding, pero **dejarlos como teaser visual** (una silueta del Diablo, un slot bloqueado de artefacto) al finalizar la Manga 1 (minuto 8). Genera curiosidad sin añadir una sola regla verbalizada.
* **RECOMENDACIÓN FINAL:** **Podar del onboarding; revelar el meta-loop (puente y Diablo) como teaser visual tras completar la Manga 1.**  
* **CONFIANZA:** 🟡.