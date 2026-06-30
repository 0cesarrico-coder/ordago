## TABLA-RESUMEN

| DC | Opción | Confianza | Gate / Experimento |
| :--- | :--- | :---: | :--- |
| **DC-1** | Acoplado-a-mano (Pacto + Auto-sabotaje explícito) | 🟢 | Ratio de abandono de runs con pactos vs. sin pactos |
| **DC-3** | Skill-dominant (70% Skill / 30% Suerte) | 🟢 | % de reseñas en Steam que mencionen "unfair/injusto" |
| **DC-28**| Umbral de reciprocidad: **0.25** | 🟡 | Test A/B (0.20 vs. 0.25 vs. 0.30) |
| **DC-29**| Mid-run silencioso (*"¿La querías, tahúr?"* ~0.5s) | 🟢 | Tiempo de lectura en pantalla de arrepentimiento |
| **DC-30**| Bloqueante (Veto estricto de goodwill) | 🟢 | Evolución de la nota de Steam (Reviews positivas) |
| **DC-31**| No-atenuar (Rigor narrativo desde Run 1) | 🟡 | Churn de D1 a D3 por cohorte (LATAM vs. US) |
| **DC-32**| Sí (Delay forzado de 1.5s en derrota) | 🟢 | Ratio de Rage-quits (Alt+F4) vs. Re-run |

---

## DECISIONES RESUELTAS

### DC-1 · Apetito de auto-sabotaje en Pactos
* **(a) COMPROMISO:** Acoplado-a-mano.
* **(b) PORQUÉ + confianza (🟢):** Un trato con el Diablo no es una optimización de stats; es una herida autoinfligida. Como el ojo sacrificado en *Inscryption*, el jugador debe recordar exactamente qué entregó a cambio del poder. El diseño emergente diluye la culpa; el acoplado-a-mano personaliza la tragedia. Si usas una Fullería para romperlo, la victoria se siente como un robo magistral al Diablo, no como un bug del sistema.
* **(c) CRITERIO QUE LA FALSARÍA:** Si el ratio de selección de Pactos cae por debajo del 15% en runs ganadores (señal de que el coste es percibido como un castigo insalvable y no como un riesgo emocionante).
* **(d) EXPERIMENTO:** Análisis de cohortes: medir si los jugadores que ganan usando al menos un Pacto acoplado muestran un 20% más de menciones al "riesgo" en feedback cualitativo que los que ganan con builds "limpias".

### DC-3 · Dial suerte↔skill (PESO)
* **(a) COMPROMISO:** **70% Skill / 30% Suerte**.
* **(b) PORQUÉ + confianza (🟢):** El "feel" de *Slay the Spire* radica en que el jugador asuma la total responsabilidad de la derrota. Si la suerte domina, la pérdida se siente como una estafa del algoritmo; si la skill domina, el arrepentimiento es honesto (*"debí haber pickeado esa carta de defensa en el piso 2"*). Ese 30% de suerte es el folclore, el "viento de la baraja" que da la chiripa compartible en redes, pero el 70% de skill es lo que sostiene la cola larga en Steam y el respeto de la comunidad de cartas.
* **(c) CRITERIO QUE LA FALSARÍA:** Que el ratio de victorias de jugadores expertos en los primeros 10 runs supere el 80% (demasiado determinista, mata la mística del azar del "truco").
* **(d) EXPERIMENTO:** Simulación de Montecarlo + Testeo cerrado con pro-players: forzar escenarios de "mano pésima" y medir si el 15% superior de los jugadores puede resolverlos mediante mecánicas de descarte o engaño.

### DC-28 · Umbral de reciprocidad / ratio para-satisfecho
* **(a) COMPROMISO:** Umbral de **0.25**.
* **(b) PORQUÉ + confianza (🟡):** Un umbral de 0.25 (1 victoria parcial/satisfactoria por cada 4 runs) es el punto dulce de la "sed de revancha". Menos de 0.20 se siente punitivo e injusto para el público americano e hispano que busca progreso; más de 0.35 abarata la victoria y diluye la opresión de la atmósfera del Romancero.
* **(c) CRITERIO QUE LA FALSARÍA:** Churn prematuro en D3 superior al 30% en la cohorte LATAM (más sensible a la falta de progreso percibido).
* **(d) EXPERIMENTO:** Test A/B balanceando el matchmaking/recompensa para fijar el ratio en 0.20, 0.25 y 0.30 de manera oculta. Medir la métrica de re-run inmediato.

### DC-29 · Susurro del arrepentimiento: mid-run silencioso vs epitafio post-run
* **(a) COMPROMISO:** Mid-run silencioso.
* **(b) PORQUÉ + confianza (🟢):** El arrepentimiento post-run es una autopsia fría. El susurro *mid-run* (ver la carta sacrificada translúcida en tu descarte por 0.5s con el susurro *"¿La querías, tahúr?"*) ocurre cuando todavía hay pulso. Duele en tiempo real. Respeta al jugador porque no detiene el flujo de la partida, pero planta la semilla de la duda de forma puramente diegética, al estilo de las cartas parlantes de *Inscryption*.
* **(c) CRITERIO QUE LA FALSARÍA:** Incremento en el tiempo medio de turno (AP - Analysis Paralysis) provocado por la distracción visual o cognitiva del susurro.
* **(d) EXPERIMENTO:** Medir si el grupo expuesto al flash mid-run tiene un tiempo de re-run post-derrota más reflexivo (entre 3s y 6s) en comparación con el re-run instantáneo y compulsivo (<1.5s) del grupo sin estímulo.

### DC-30 · Veto goodwill: bloqueante
* **(a) COMPROMISO:** Bloqueante (Veto estricto).
* **(b) PORQUÉ + confianza (🟢):** Quemar goodwill para inflar la retención a corto plazo es un impuesto invisible que destruye el ciclo premium B2P en Steam. Las comunidades hispanas y americanas de roguelikes son hiper-conectadas; un solo hilo en Reddit o Twitter acusando al juego de "manipular los rates de robo al final de la run" destruye el CAC orgánico para siempre. El veto debe ser un muro de hormigón.
* **(c) CRITERIO QUE LA FALSARÍA:** Ninguno. Es un principio de diseño fundacional para un juego premium.
* **(d) EXPERIMENTO:** No aplica. El guardarraíl de valor perdurable no se somete a test de estrés de monetización.

### DC-31 · ¿Atenuar el arrepentimiento en runs 1–3 de onboarding?
* **(a) COMPROMISO:** No-atenuar (Rigor total).
* **(b) PORQUÉ + confianza (🟡):** Atenuar el tono faustiano al inicio es mentirle al jugador sobre el juego que compró. El "Romancero" y el pacto con el Diablo deben morder desde el primer minuto. Si suavizamos el inicio, creamos una falsa expectativa; el filtro de dificultad e identidad debe ser honesto. La vergüenza de la derrota temprana se mitiga no suavizando la run, sino haciendo que el Diablo se burle del avatar del jugador, nunca del usuario real (humor negro diegético).
* **(c) CRITERIO QUE LA FALSARÍA:** Churn en D1 superior al 40% asociado directamente a derrotas en el Run 1 o 2.
* **(d) EXPERIMENTO:** Test A/B: Cohorte A (onboarding guiado/atenuado en daño) vs. Cohorte B (onboarding crudo con advertencia narrativa). Medir conversión a review positiva en Steam.

### DC-32 · ¿Delay forzado ~1.5s en el epitafio de derrota?
* **(a) COMPROMISO:** Sí (Delay de 1.5s).
* **(b) PORQUÉ + confianza (🟢):** El botón de re-run instantáneo convierte al juego en una máquina tragaperras de dopamina barata. El delay de 1.5s con la frase *"La baraja te espera"* o el crujir de la madera de la mesa de juego ofrece un cierre digno, un momento de silencio para procesar la derrota. Es el respeto que *Slay the Spire* muestra al disolver tu personaje en cenizas. La derrota en ÓRDAGO debe tener peso físico.
* **(c) CRITERIO QUE LA FALSARÍA:** Tasa de Alt+F4 (rage quit) durante ese segundo y medio que supere el 8%.
* **(d) EXPERIMENTO:** Test A/B desactivando el delay. Medir si el grupo "sin delay" muestra signos de fatiga de juego (sesiones más cortas en días posteriores por burnout).

---

## DÓNDE EL FEEL DISCREPA DEL RIGOR DE OPUS

* **En DC-1 (Pactos):** Opus busca la elegancia matemática de sistemas emergentes puros (S4-verde). El *feel* discrepa: los jugadores de roguelikes premium aman la narrativa incrustada en las mecánicas. El auto-sabotaje acoplado-a-mano ofrece una "historia que contar" en foros (ej: *"Tuve que jugar toda la run sin poder ver el valor de mi mano derecha por culpa del pacto de la ceguera"*). La matemática pura es elegante; la cicatriz es memorable.
* **En DC-32 (Delay de Derrota):** La optimización lógica de sistemas tiende a reducir la fricción. El *feel* exige fricción dramática. El delay de 1.5s no es un obstáculo para la retención, es el altar del arrepentimiento digno. Sin él, el pacto con el Diablo carece de gravedad.

---

## QUÉ DATO L1 NECESITO DE META

Necesito de Meta AI el desglose exacto de la **correlación entre el Ratio de Victorias/Derrotas en las primeras 2 horas de juego y la probabilidad de reembolso en Steam** por regiones (LATAM vs. USA). Esto me permitirá calibrar si el umbral de reciprocidad (DC-28) debe ajustarse dinámicamente según la región geográfica para proteger el reembolso sin comprometer la identidad del juego.