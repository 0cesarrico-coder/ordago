# PANEL ÓRDAGO — RONDA 1

**Silla ocupada:** Estratega de Propuesta de Valor (Rol Eje) + Voz del Jugador  
**Perspectiva combinada:** El ojo clínico que busca la trampa aritmética tras el romanticismo cultural, aliado con la visceralidad del jugador que no quiere hacer deberes de matemáticas el viernes por la noche tras salir de trabajar.

---

## 1. Propuestas de valor que LEES en el diseño (Real vs. Hueca)

Tras destripar el macro GDD v0.1, separo el humo de la pólvora. Esto es lo que tu diseño realmente entrega hoy, no lo que declara tu entusiasmo:

1. **La fantasía del "Trickster" contra el Diablo (REAL):**
   * *Sistema que la entrega:* **§4 y §8 (El Diablo Fantasma)** y **§10 (El Diablo Reacciona)**. 
   * *Análisis:* Esta es tu propuesta más robusta. El "Diablo Fantasma" no es un menú estático de leaderboard; convierte el high-score asíncrono de un desconocido en el rostro de tu opresor. El juego cumple la promesa de "pactar y timar" gracias al diseño de la capa social embebida en la ficción (A4 🟢🟡).
2. **El "Balatro Hispano" por nostalgia/identidad (REAL, pero acotada):**
   * *Sistema que la entrega:* **§7.2 (Baraja de 40 cartas)** y **§7.5 (Las Matas como rarezas)**.
   * *Análisis:* Para el público nativo (LATAM/España), ver el As de Espadas o el Siete de Oros con arte estilo Posada despierta un disparador emocional inmediato (A3 🟡 - Mito comprimido). El valor estético y la familiaridad del "macho" de espadas son reales y propios.
3. **El verbo del "Suma 15" (Escoba) como motor de dopamina exponencial (HUECA / EN RIESGO CRÍTICO):**
   * *Sistema que la entrega:* **§6.1 (El verbo core)** y **§7.3 (La Mesa)**.
   * *Análisis:* El GDD confunde la *simplicidad* de la regla ("sumar 15") con la *satisfacción cinética* del gameplay. El póker (Balatro) funciona porque es un sistema de **reconocimiento de patrones pasivos** (color, escalera, par); el cerebro humano detecta un "Color" en milisegundos. El "Suma 15" de la Escoba es un **problema de optimización aritmética activo** (búsqueda de subconjuntos). Si tengo 4 cartas en mano y 4 en mesa, calcular mentalmente qué combinaciones suman exactamente 15 es trabajo de procesador, no relajación (Falla la Lente LD4 🟡 en su cluster de *Submission/Relax*). 
4. **La "Doble Ola" de mercado: Nativo + Exótico Global (HUECA):**
   * *Sistema que la entrega:* **§3.2 y §3.3 (Doble alcance / Localización inversa)**.
   * *Análisis:* El GDD asume que el jugador no hispano adoptará el juego por "exotismo bello". Sin embargo, el "Suma 15" introduce una fricción cognitiva brutal para el extranjero: las figuras tradicionales (Sota, Caballo, Rey) no tienen su valor impreso en el naipe clásico de forma intuitiva, y su valor de juego (8, 9, 10) no coincide con su orden físico en barajas de 40 cartas donde el 8 y el 9 no existen. Para un jugador de Ohio, calcular por qué un Caballo (que parece un 11 o un 12) sumado a un 6 da 15 es una barrera insalvable en los primeros 3 minutos (Pilar 2 - Mental Model roto).

---

## 2. Fortalezas (Top 3)

* **F1: El Diablo Fantasma como motor social asíncrono (§4, §8) [Lente LD6 🟢🟡 - Competición/Dominancia / A4 🟢🟡]:**  
  Es brillante. En LATAM, el "pique" familiar y la rivalidad son motores primarios de retención (64-71% de engagement en redes, LD6). Traducir el score a batir de la semilla en "el Diablo toma la forma de tu amigo Juan que hizo 50,000 puntos" aterriza la fantasía de burlar al demonio sin la fricción de un servidor PvP en tiempo real.
* **F2: La jerarquía nativa de "Las Matas" como rareza natural (§7.5) [A3 🟡 - Mito Comprimido]:**  
  No tienes que educar al jugador sobre qué carta es épica. El "ancho de espadas" ya carga con siglos de respeto cultural en el Cono Sur y España. Usar este sistema de rareza pre-grabado en el subconsciente ahorra UI, ahorra explicaciones y genera un momento de "Fiero" (LD2 🟡/🟢) instantáneo al robarlas.
* **F3: La estructura de "El Envite" como Boss Fight con reglas modificadoras (§7.10) [A1 🟢🟡 - Elegancia/Emergencia]:**  
  La división de la Manga en *chica, grande y envite* emula perfectamente la tensión del Truco/Mus. Introducir "reglas trampa" temáticas del Diablo en el Envite es un tiro certero para romper las builds dominantes del jugador y obligarlo a re-adaptarse (A1).

---

## 3. Fallas fatales (Top 3)

* **FF1: La trampa de la "calculadora mental" en el core loop (§6.1, §6.2) [Pilar 2 / Lente LD4 🟡 - Cluster Submission/Relax]:**  
  *La Voz del Jugador ruge:* "Vengo de trabajar 8 horas. Abro el juego. Tengo que mirar una mesa con 5 cartas y mi mano de 5. Tengo que empezar a sumar mentalmente: '7+5 es 12, no llega... 7+sota(8) es 15, ¡espera! ¿la sota valía 8 o 10? Ah, vale 8. Ok, 7 de oros y sota de bastos... ¿tengo algo más?'. Para cuando he hecho mi jugada, me duele la cabeza. Desinstalo. Prefiero jugar Balatro donde solo arrastro cinco cartas del mismo color."  
  *El Estratega advierte:* Si el core loop se siente como un examen de aritmética de primaria, pierdes el flujo zen. La Escoba tradicional es divertida porque juegas contra alguien físicamente y hay juego psicológico; en solitario, sin la tensión del rival real en la mesa, es solo cálculo de combinatorias.
* **FF2: El vacío del "Tablero Solitario" (§7.3) [A1 🟢🟡 - Emergencia]:**  
  ¿De dónde salen las cartas de "La Mesa"? En la Escoba real, la mesa se alimenta de las cartas que los jugadores descartan porque no pudieron sumar 15. Si en ÓRDAGO juegas solo contra un score: ¿cómo se puebla la mesa? Si solo robas de tu mazo y juegas de tu mano, no estás haciendo "Escoba" (barrer la mesa), estás haciendo Blackjack modificado de tu propia mano. El GDD no define el sistema de interacción con la mesa del Diablo. Si el Diablo no juega cartas físicamente para "ensuciar" o "poblar" la mesa, el verbo de *capturar* cartas pierde toda su profundidad estratégica y se convierte en un reskin plano.
* **FF3: El colapso del onboarding global por disonancia de índices (§7.2, §13) [A5 🟡 - Estética-Sistema]:**  
  La baraja española tradicional de 40 cartas salta del 7 a la Sota (10), Caballo (11) y Rey (12). Pero para el "Suma 15", la Sota vale 8, el Caballo 9 y el Rey 10. Para un jugador hispano que lo mamó de niño, esto es memoria muscular. Para el resto del planeta (y para los jóvenes hispanos que solo juegan póker en el móvil), es una disonancia cognitiva destructiva. Ver un "11" (Caballo) impreso en la esquina pero que el juego te diga que vale "9" viola la regla de oro de la Estética-Sistema (A5): el visual debe comunicar la función antes de procesar el adorno.

---

## 4. Recomendación #1 (Mayor apalancamiento)

### El Cambio en el GDD (§6.2, §7.3, §10): El sistema de "La Mesa Activa" y "Dopamina Auto-Aritmética"

Para matar el "efecto calculadora" y resolver el vacío de la mesa en solitario, propongo reformular el sistema de juego de la siguiente manera:

1. **La Mesa del Diablo es un ente vivo:** Al inicio de cada turno, el Diablo "escupe" (reparte) 4 cartas boca arriba en la mesa desde su propio mazo corrupto.
2. **La UI como aliada del flujo zen:** El juego debe contar con un **"Motor de Reconocimiento de Patrones Activo"**. Al pasar el ratón por encima de tus cartas, el juego resalta automáticamente con un destello dorado y un sonido de monedas (juice stack, §10) qué combinaciones de la mesa suman 15 con tu carta seleccionada. El jugador no *calcula*; el jugador *detecta y ejecuta* con un clic satisfactorio.
3. **El rediseño híbrido de los naipes (A5 🟡):** Las cartas del juego deben rediseñarse para mostrar de forma masiva su **valor de juego (8, 9, 10)** en el centro/esquina para legibilidad del gameplay, manteniendo la ilustración tradicional de la Sota/Caballo/Rey como fondo estético secundario.

* **Criterio de Kill:** Si tras implementar el resaltado visual y los índices funcionales, los playtesters de fuera de LATAM tardan más de 60 segundos en realizar su primera "Escoba" sin dudar de los valores de las cartas, el verbo "Suma 15" se declara inviable para mercado masivo.
* **El Test más barato (⚪):** Crea un prototipo físico con una baraja española real. Pega post-its en las figuras con sus valores de juego (8, 9, 10). Pon a un amigo que no juegue cartas a hacer combinaciones de 15 contra reloj. Mide cuántas veces se equivoca sumando o se queda paralizado mirando la mesa.

---

## 5. Apuesta falsable

> "ÓRDAGO no entregará su valor a menos que logre transformar la matemática activa de la Escoba ('sumar 15') en un sistema de reconocimiento visual pasivo asistido por la interfaz, evitando que el jugador sienta que está haciendo un examen de cálculo mental en lugar de timar al Diablo."

---

## 6. Rúbrica de evaluación (1-5)

* **Claridad de propuesta central:** **4/5** (El concepto "Balatro con baraja española contra el Diablo" es un gancho comercial potentísimo y claro).
* **Entrega del valor:** **2/5** (El core loop actual de la Escoba en solitario genera más fatiga cognitiva que diversión; la mesa está vacía mecánicamente).
* **Cuerpo elegante (A1):** **3/5** (La estructura de apuestas escala bien, pero la interacción de los Pactos con la suma de 15 puede volverse puramente matemática y lineal sin "breaking mechanics" claras).
* **Originalidad del verbo core:** **4/5** (Es genuinamente diferente al póker, pero esa diferencia hoy es su mayor peligro de retención).
* **Fantasía/Tema (A2-A4):** **5/5** (Impecable. El folclore barroco, Posada, las calacas y el pacto con el Diablo es una de las mejores sinergias estéticas del género en años).
* **Mito en 1s (A3):** **5/5** (Para el público objetivo, la baraja española y el Diablo es una imagen grabada en el ADN cultural).
* **Cobertura emocional (LD4):** **2/5** (Falla en el cluster de *Submission/Relax* debido a la carga aritmética, y el cluster *Action-Social* está demasiado apoyado en el leaderboard sin interacción reactiva real en la mesa).
* **Verdad del jugador (VJ):** **2/5** (El jugador promedio rebotará a los 5 minutos cuando se canse de sumar números en su cabeza para ver si llega a 15 mientras las figuras le mienten con su iconografía).