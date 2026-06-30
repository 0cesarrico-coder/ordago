# PANEL ÓRDAGO — RONDA 3 · TU ASIENTO: ESTRATEGA DE PROPUESTA DE VALOR + VOZ DEL JUGADOR

---

## 1. RESOLUCIÓN DE CRUXES

*   **CRUX 1: ¿La Mesa (§7.3) tiene un poblador ACTIVO que genera decisiones de tablero, o es estática/decorativa?**
    *   **CIERRO hacia Postura A (Active Populator).** No es negociable para la supervivencia del juego. Jugar "solo contra tu mazo" en un tablero estático destruye el juego de posición (A1 🟢🟡). En la Escoba real, tu oponente "puebla" la mesa con sus descartes fallidos, creando la tensión de *"¿le dejo un 15 servido o me arriesgo?"*. **Resolución de sistema:** El Diablo debe jugar cartas a la mesa desde su mazo corrupto al final de cada una de sus fases. Esto transforma la aritmética lineal en un juego de bloqueo, control de tempo y lectura de tablero.
*   **CRUX 2: La causa de la fricción del verbo "sumar 15" ¿es PERCEPTUAL (UI assist) o ESTRUCTURAL (trade-offs)?**
    *   **CIERRO en una postura de convergencia táctica (Asistencia Pasiva sin Solucionador).** Gemini tiene razón en que el "efecto examen" mata el cluster *Submission/Relax* (LD4 🟡), pero su solución de "glowing 15s al hover" liquida la Maestría (A1) y reduce el juego a un clicker. **Resolución:** La UI *no* debe sugerir soluciones automáticas (no brilla nada al pasar el ratón de forma pasiva). En su lugar, el jugador selecciona cartas de su mano y, al hacerlo, la UI resalta de manera clara la *suma acumulada temporal* en la pantalla y destaca los naipes de la mesa que *completarían* el 15. El jugador sigue haciendo el avistamiento cognitivo (*Fiero*, Lazzaro 🟢), pero la UI elimina el cálculo de acarreo y la disonancia de los valores de las figuras.
*   **CRUX 3: ¿"Le hice trampa al Diablo" necesita su propio sistema (Fullerías) o basta con la asimetría de los Pactos?**
    *   **CIERRO hacia Postura A (Sistemas Diferenciados).** La fantasía del "tahúr astuto" (A4 🟢🟡) se desmorona si el jugador solo escala multiplicadores de forma pasiva (fantasía del alquimista de *Balatro*). Necesitamos las **Fullerías** (§7.6) como un conjunto de verbos activos de manipulación de reglas con riesgo (ej. *"Cambiar el valor de una sota a 5 por esta mano"* o *"Ocultar un naipe en la manga"*). Si el Diablo te pilla (un porcentaje de riesgo base mitigable por builds), el Envite se duplica. Esto separa mecánicamente la "optimización pasiva" (Pactos) de la "trampa activa" (Fullerías).
*   **CRUX 4: ¿La estética de claroscuro (Posada-Vela) es un activo (Mito A3) o un pasivo (Fatiga/Apropiación)?**
    *   **DECLARO IRREDUCIBLE.** No hay datos de diseño puros que zanjen esto. El mercado de Steam devora roguelikes de folclore oscuro y claroscuro premium (*Cult of the Lamb*, *Darkest Dungeon*, * Inscryption*) porque convierten muy bien visualmente en la tienda (CTR alto en trailers, "watchability" en YouTube). Sin embargo, el público joven mexicano e hispanohablante muestra una fatiga creciente hacia la "estetización minimalista" de sus tradiciones (ej. el backlash contra marcas boutique en TikTok/Instagram en 2024), exigiendo un maximalismo colorido, ruidoso e identitario. **Solo un test de humo de conversión publicitaria (Meta/TikTok Ads) con ambos artes resolverá esta disonancia.**

---

## 2. POSICIÓN DEFINITIVA SOBRE LAS 5 PREGUNTAS CENTRALES

### Propuesta de valor central (1 línea)
> **"ÓRDAGO es el roguelike de cartas donde juegas con la baraja de tu abuelo, pero ganas haciéndole trampa al Diablo al reescribir las leyes de la mesa."**

### Jerarquía de propuestas secundarias (Segmentada)

#### Para el Jugador Hispano (Nostalgia y Pique):
1.  **Las Matas como Rareza Nativa (§7.5) [Confianza: 🟢]:** El As de Espadas y el Siete de Oros cargan con un peso emocional instantáneo y un estatus de poder sin necesidad de tutoriales (A3 🟡).
2.  **El Diablo Fantasma (§8) [Confianza: 🟡]:** El pique asíncrono y la humillación de ver el avatar de tu amigo convertido en tu demonio opresor dentro del juego sirve al potente motor social-competitivo de LATAM (Quantic Foundry: Action-Social 41% MX).

#### Para el Fan Global de Roguelikes (Mecánica y Novedad):
1.  **La Dinámica del Tramposo (Pactos + Fullerías, §7.6) [Confianza: 🟡]:** Un deckbuilder donde el "break-the-game" no es solo aditivo/multiplicativo, sino que requiere violar las reglas de la baraja activamente y gestionar el riesgo de ser descubierto.
2.  **La Tensión del Envite (§7.10) [Confianza: 🟡]:** Estructura de apuestas por rondas que emula la tensión psicológica del Truco/Mus dentro de un bucle de juego en solitario.

---

### Propuestas a MATAR (Huecas/Indefendibles) y por qué

*   **MATAR: "La Escoba tradicional en solitario como nuevo verbo global de relax" (§6.1, §7.3).**  
    *   *Por qué:* Jugar a la Escoba pura contra la nada es un rompecabezas aritmético plano de baja emergencia (A1). Si no hay un oponente activo en la mesa y el juego no introduce la manipulación de reglas, el jugador global rebotará a los 5 minutos debido a la fatiga cognitiva de sumar constantemente.
*   **MATAR: "La UI auto-asistida con resplandores para los 15s" (Rec. Gemini R1).**  
    *   *Por qué:* Elimina por completo la agencia del jugador (LD4 🟡). Convierte un juego de astucia mental en un simulador de "hacer clic en la carta que brilla".
*   **MATAR: "La identidad visual neutra/boutique de hotel" (§11).**  
    *   *Por qué:* La paleta ultra-minimalista de "oro vela y negro cálido" arriesga alienar al público nativo que percibe el Día de Muertos como una festividad de color, ruido y maximalismo popular.

---

### Entrega de propuestas supervivientes e intervenciones GDD

#### 1. Las Matas como Rareza Nativa (§7.5)
*   **¿La entrega hoy?** SÍ. El diseño se apoya perfectamente en el sesgo cognitivo cultural del jugador hispano (A3 🟡). No requiere cambios.

#### 2. El Diablo Fantasma como Competencia Asíncrona (§8)
*   **¿La entrega hoy?** PARCIALMENTE. Falta especificar el sistema de emparejamiento.
*   **Cambio concreto al GDD (§8.4):** Implementar **Bucket Leaderboards** (sistema de emparejamiento por percentiles de habilidad). El "Diablo Fantasma" que te atormenta no será el récord mundial inalcanzable (que causaría frustración y abandono, LD6), sino el fantasma del jugador que está exactamente un 5% por encima de tu puntuación histórica en esa semilla diaria (gap de Festinger cerrado).

#### 3. La Dinámica del Tramposo (Fullerías vs. Trampas del Diablo, §7.6)
*   **¿La entrega hoy?** NO. El GDD actual depende de multiplicadores numéricos pasivos estilo *Balatro*.
*   **Cambio concreto al GDD (§7.6 y §10.3):** Convertir las **Fullerías** en un slot de equipo activo e independiente de los Pactos. El jugador puede equipar hasta 2 Fullerías por run. 
    *   *Ejemplo de mecánica:* "La Sota de Bastos se lee como un 5". Al usarla, hay un 15% de probabilidad de que el Diablo active una reacción diegética (§10), te "pille" e imponga una penalización en forma de carta corrupta en tu mazo.

#### 4. El Poblamiento de La Mesa (§7.3)
*   **¿La entrega hoy?** NO. El GDD deja la mesa como un elemento estático de origen difuso.
*   **Cambio concreto al GDD (§7.3.1):** Introducir **"La Mano del Diablo"**. Al inicio de cada turno de la Manga, el Diablo descarta una carta boca arriba en la mesa desde su mazo sombrío. Esta carta define el rango de juego: si el Diablo tira un 7, está bloqueando combinaciones bajas y obligando al jugador a recalcular su mano de forma activa.

---

### Calidad de diseño del GDD: El cambio de mayor apalancamiento

*   **Intervención prioritaria:** Rediseño completo de la interacción de **La Mesa Activa (§7.3) + Sistema de Fullerías (§7.6)**.
*   **Anclaje metodológico:** **Carta A1 (Cuerpo Elegante/Emergencia)** + **Lente LD4 (Sub-cluster Mastery)**. Al obligar al Diablo a jugar sobre la mesa y permitir al jugador romper el valor físico de sus cartas con las Fullerías, transformamos un examen de matemáticas en un duelo táctico asimétrico de baja fricción y alta rejugabilidad.
*   **Criterio de Kill:** Si durante el playtest de rectángulos en papel (§14), los jugadores del grupo de control (que juegan solo con sumas puras y modificadores numéricos de Pactos) muestran una tasa de aburrimiento y abandono un 40% superior a los del grupo experimental (que usan Fullerías para alterar las sumas), se cancela el desarrollo de la Escoba como motor y se pivota el proyecto hacia un deckbuilder tradicional de póker con skin español.
*   **Test más barato:** Un prototipo en papel (Pilar 4, §14) con una baraja española normal de 40 cartas y post-its. Sienta a dos amigos de confianza. Uno juega como el jugador (con 3 cartas en mano y 2 Fullerías escritas en papel de borrador); tú actúas como el Diablo (lanzando cartas a la mesa y aplicando "trampas" predefinidas según un dado). Mide la frecuencia de risas espontáneas, insultos lúdicos hacia ti ("¡maldito tramposo!") y el deseo inmediato de repetir la partida. Coste: $0 y 2 horas de diseño analógico.

---

## 3. ELEVATOR PITCH FINAL (1 línea)

> **"ÓRDAGO es un roguelike de cartas en el que utilizas la baraja española para engañar, robar y reescribir las reglas matemáticas de una mesa viva en un duelo de astucia pura contra el Diablo."**

---

## 4. LISTA DE LO QUE SIGUE CONTESTADO (Irreducible)

*   **LADO A (Estética Premium de Exportación):** La atmósfera mística de claroscuro (negros profundos, oro vela, arte estilo Posada trágico) es un gancho comercial infalible en Steam a nivel global para destacar entre la marea de juegos casuales coloridos de móvil.
*   **LADO B (Autenticidad Cultural Local):** El público nativo de LATAM puede rechazar la paleta sombría y minimalista por considerarla una versión gentrificada y "blanqueada" del Día de Muertos, exigiendo el maximalismo, el color chillón y el caos de las cantinas populares.