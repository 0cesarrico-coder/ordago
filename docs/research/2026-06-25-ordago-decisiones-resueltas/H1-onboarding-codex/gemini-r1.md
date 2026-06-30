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