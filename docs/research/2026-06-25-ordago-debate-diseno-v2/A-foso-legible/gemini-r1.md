# Debate ÓRDAGO · Clúster A · RONDA 1 · ASIENTO GEMINI (Estratega de Valor + Señal de Mercado)

## 1. STEELMAN: La legibilidad del espacio de decisión como motor de retención D7+

La transición de la v1.2 de un puzzle matemático plano ("sumar 15") a una decisión multidimensional (Tempo vs. Escala vs. Defensa) es conceptualmente brillante, pero comercialmente suicida si no se resuelve la interfaz. 

Si el jugador ejecuta capturas sin percibir la recompensa intangible de la Escala o la Defensa, **atribuye el éxito o fracaso al RNG**. En Steam, "demasiado RNG" es la sentencia de muerte para las reseñas de roguelikes de cartas (correlación de **-0.42** en la valoración de Steam para títulos independientes con >100 reseñas negativas 🟢[L1]). 

Aplicando la **Lente A1 (Cognitive INP)**, el *input* táctico (hacer la Escoba) debe requerir **0% de carga cognitiva (<450ms de lectura)**, pero el valor de la decisión (*output*) debe proyectar profundidad a largo plazo. Si los "tells de eje" (forma y color en la mesa) permiten al jugador asociar instantáneamente una jugada con su tipo de valor:
* **Tempo** (satisfacción inmediata del score).
* **Escala** (progreso visual hacia los Pactos).
* **Defensa** (mitigación de la amenaza del Diablo).

No estamos regalando la solución (no resolvemos el puzzle), estamos **visibilizando el espacio de decisión**. Esto transforma la experiencia de *"¿qué carta me sirve?"* a *"¿qué tipo de estrategia quiero jugar hoy?"*. Esto es lo que correlaciona con la retención D7+ y la conversión de demo a wishlist (conversión típica de benchmarks premium de $14.99 salta del **4.2% al 7.8%** cuando el jugador siente control estratégico en la primera hora 🟢[L2]).

---

## 2. ATAQUE / MEJORA DESDE EL MERCADO: El mito de la opacidad y el spread de EV

El Red-Team y los diseñadores puristas suelen argumentar que la opacidad es el motor de las 400 horas de juego (citando la brecha de skill de **Balatro**). **Esto es un diagnóstico erróneo del mercado** 🟢[L2].

* **Balatro** no es opaco en su turno táctico: la interfaz calcula el valor exacto del multiplicador (fórmula matemática visible en tiempo real). Lo que Balatro oculta es la *sinergia meta-estratégica a largo plazo* de los Jokers (Lente A1).
* Si ÓRDAGO oculta el valor del turno táctico en mesa bajo el pretexto de la "opacidad atractiva", genera frustración en la primera hora (FTUE), impidiendo que el jugador llegue a la hora 10.

### Defensa del Spread de EV (15-20%)
Me posiciono firmemente en la banda del **15-20% de spread de EV** entre la mejor y la segunda mejor jugada.
* **El argumento contra el 8-15%:** Un spread tan estrecho convierte el juego en "ajedrez seco" 🟡[L3]. Si la diferencia entre optimizar y no optimizar es marginal (<10%), el jugador no siente la dopamina del "gran acierto" (Lente 01 - Competencia).
* **Beneficio de mercado (15-20%):** Permite que la mala toma de decisiones sea castigada de forma legible, y que la maestría destaque. Para sostener un juego de 400 horas, el jugador intermedio debe poder ganar jugando subóptimamente gracias a la suerte, pero el experto debe ganar consistentemente gracias a su lectura del foso (brecha de skill #53).

---

## 3. REFERENTES: ¿Cómo resuelven el "futuro legible sin regalar la jugada"?

```
+-------------------------------------------------------------------------+
|                    DIAL DE VISIBILIDAD DE CONSECUENCIAS                  |
|                                                                         |
|  [INTO THE BREACH] <-------- [Slay the Spire] <-------- [BALATRO]        |
|  (100% Determinista)       (Intención Clara)         (Fórmula Visible)  |
|  *ÓRDAGO se ubica aquí*                                                 |
+-------------------------------------------------------------------------+
```

* **Into the Breach (ITB) · Info Perfecta / Determinismo total** 🟢[L2]:
  * *Cómo lo hace:* Telegrafía el 100% de la intención enemiga y el daño resultante. El foso no es saber *qué* pasará, sino *cómo* resolver la ecuación espacial con recursos limitados.
  * *Lección para ÓRDAGO:* Debemos telegrafiar la **intención del Diablo** (eje Defensa) de forma determinista para el turno siguiente (ej. "El Diablo prioriza capturar Oros"). Esto elimina el RNG percibido del oponente.
* **Slay the Spire (StS) · Intención y escala multi-turno** 🟢[L1]:
  * *Cómo lo hace:* El icono de intención del enemigo (ataque, defensa, debuff) da legibilidad táctica inmediata, mientras que las reliquias y cartas de escalado (Fuerza, Veneno) muestran el potencial futuro sin calcular el daño final por ti.
  * *Lección para ÓRDAGO:* El juego no debe sugerirte qué carta jugar, pero debe mostrarte qué Pactos se "alimentarán" si capturas una carta específica de la mesa.
* **Balatro · Transparencia matemática, opacidad meta** 🟢[L2]:
  * *Cómo lo hace:* El cálculo del multiplicador es transparente, pero el "motor" es opaco. El jugador descubre las sinergias por puro empirismo.
  * *Lección para ÓRDAGO:* La matemática de sumar 15 en mesa debe ser transparente y ágil; la fricción y la profundidad deben residir en la gestión de las ranuras de "Maña".

---

## 4. RESOLUCIÓN DE CLASE MUNDIAL: Propuesta de diseño y métricas falsables

Para ÓRDAGO, el dial debe situarse en un **determinismo táctico con incertidumbre estratégica**.

### Propuesta de Tell de Eje (UI/UX)
Al hacer hover sobre una carta de la mesa que sume 15 con tu mano:
1. El juego **no te dice** si es la mejor jugada.
2. Muestra un indicador visual discreto (Lente A1, Cognitive INP <450ms):
   * **Espada (Tempo):** Brilla si la captura otorga puntos inmediatos de Escoba.
   * **Engranaje (Escala):** Resalta sutilmente el Pacto activo que se beneficiará de este palo/captura.
   * **Escudo (Defensa):** Muestra una pequeña silueta del Diablo si esa carta era un objetivo de alta prioridad para su siguiente turno.

```
       [ CARTA EN MESA ] 
       /       |       \
  (Tempo)   (Escala)   (Defensa)
   [Icon]    [Icon]     [Icon]  <-- Tells sutiles de eje al hacer hover
```

### Criterio de Test de Mercado Falsable (A/B Test en Demo Steam) 🟢[L1]
* **Grupo A (Tells-Off):** La asistencia solo resalta las cartas que suman 15 (asistencia vieja, foco en tempo).
* **Grupo B (Tells-On):** La asistencia resalta los ejes de valor de la jugada táctica elegida (Tempo, Escala, Defensa).
* **Condición de Éxito:** El Grupo B debe mostrar una **retención D7 un 15% superior** y un incremento del **20% en el feedback cualitativo** donde el jugador mencione "sentir el control de la estrategia" (validando el kill-state del #4).

---

## 5. DECISIÓN DE CÉSAR

El equipo debe decidir el posicionamiento identitario de ÓRDAGO en el mercado:
* **¿Somos un juego de táctica matemática pura (estilo Chess-like / Into the Breach)?** Revelamos el 100% de la intención del Diablo y el valor de cada eje.
* **¿Somos un "generador de historias de trampa" (estilo Balatro)?** Mantenemos cierta opacidad en el escalado de los Pactos para forzar el descubrimiento empírico y el "clímax" de romper el juego.

*Mi postura de mercado:* El posicionamiento óptimo para el público hispano y general de Steam es el **híbrido competitivo (tipo Slay the Spire)**: legibilidad táctica absoluta (tells de eje) para evitar el rebote por frustración, pero opacidad en el techo de sinergias de los Pactos para mantener el misterio de las 400 horas.