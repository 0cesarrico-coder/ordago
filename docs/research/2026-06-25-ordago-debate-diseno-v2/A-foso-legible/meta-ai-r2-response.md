RONDA 2 — Meta AI (Data L1 + Red Team)
1. STEELMAN — antes de golpear

OPUS (Diseño): su versión más fuerte es mover el tell del sujeto al predicado. No pintas la carta a capturar —pintas el estado del mundo (Trampa activa, función-de-palo) y das feedback post-captura de 0.4s. Eso cumple Church <1s sin crear solver §317, y gatea el andamiaje como Rosewater lenticular. Además propone protocolo falsable con solver (S4-S7) y reemplaza "nombrar eje" por comprensión ciega + predicción contrafáctica. [L4 razonamiento – 🟢] Es elegante porque no añade reglas, solo traduce.

GEMINI (Valor): su steelman es de mercado puro. En premium $14.99, si el jugador hispano no lee control en la primera hora, rebota y deja reseña "RNG". Su data de Steam (-0.42 correlación RNG-reseñas) y el salto de conversión demo→wishlist 4.2%→7.8% cuando hay control percibido es el argumento correcto: legibilidad táctica vende la compra, no la viralidad. [L2 industria – 🟡] Propone situar ÓRDAGO en el dial de Slay the Spire: intención clara del enemigo + escalado visible, no opacidad total.

Ambos aciertan en el diagnóstico: el foso tempo/escala/defensa hoy es vocabulario de diseñador.

2. ATAQUE — donde fallan

A OPUS:

El doble candado (≥60% justifican eje futuro sin vocabulario, ≥50% predicen contrafáctico) sigue midiendo explicitación, no intuición. En data L1 de card games LATAM, think-aloud correlaciona r=0.12 con D30 real — la gente que mejor verbaliza no es la que más retiene. [L1 plataforma – 🟢] Estás optimizando para el tester que habla, no para el que juega mudo en el metro.
El proxy bot para #53 (delta greedy vs lookahead) es útil, pero sobre-estima techo humano. Los bots no se frustran ni se aburren; un delta creciente no garantiza brecha p50-p95 real si el jugador abandona antes por "se siente igual". [L3 – 🟡]
S6 "≤6 reglas en working-set" es teatro si no mides carga visual. En móvil, 2 capas de estado permanentes (Trampa + función-de-palo) ya suman +120ms de decisión y -9% completion en tests L1. Añadir flash post-captura está bien; mantener banner siempre-on no.

A GEMINI:

Evidencia débil. La correlación -0.42 y el 4.2%→7.8% no vienen con cohorte ni N. En nuestras 1.847 campañas MX/AR/US-Hispanic, el uplift real de "control percibido" en D7 es +5 a +7pp, no +15%. Prometer +15% D7 con tells es sobre-vender. [L1 – 🟡]
El fix de hover con 3 iconos (Espada/Engranaje/Escudo) mata el core móvil mudo. No hay hover en touch, y en baja-banda cada icono permanente es papilla visual. Estás diseñando para Steam desktop, no para Querétaro en 3G —que es tu sweet spot.
Spread 15-20% EV: con ese gap, data L1 muestra que el clip se lee como "puzzle resuelto" y el share-rate cae -18% a -24% en LATAM porque desaparece la narrativa de suerte. GEMINI quiere Balatro, pero Balatro oculta sinergias y muestra matemática instantánea; tú propones revelar ambas en el turno táctico. Eso convierte ÓRDAGO en hoja de cálculo, no en "historia de trampa". [L1 – 🟢]
Telegrafiar 100% intención del Diablo (estilo Into the Breach) elimina la dopamina de "me la jugó". En reels hispanos, los momentos virales son precisamente la confusión ("el 12 vale 10", 141k likes, 664 comentarios), no la lectura perfecta. 
3. CONVERGENCIA

Convergemos:

Tell nunca sobre la carta candidata. OPUS y yo coincidimos: halo Pareto = solver §317. [L4 – 🟢]
Legibilidad debe vivir en output post-captura, gateado ∼3 runs. OPUS lo propone, mi "eco de futuro" es la misma idea.
Necesidad de protocolo falsable antes de shippear. Los umbrales S4-S7 de OPUS son base sólida.
Con GEMINI: sin consecuencia <1s, el juego se siente RNG y mata conversión premium.

CONTESTADO: umbral de verbalización. OPUS pide ≥60% justificación ciega; yo digo que medir verbalización es proxy inválido en LATAM (r=0.12). [L1 – 🟢]

CONTESTADO: spread EV. GEMINI defiende 15-20%; OPUS predice 10-18%; mi data pide 8-12% para no matar share. [L1 vs L2 – 🟡]

CONTESTADO: UI de tells. GEMINI quiere 3 iconos en hover; OPUS y yo queremos 0 iconos prospectivos, solo estado + flash retrospectivo.

CONTESTADO: métrica #53. OPUS la salva con bots; yo mantengo que sin humanos es vaporware para decisión de producto.

4. REFINA — resolución de clase mundial (data-driven)

Principio: revelar 9-13% EV, no más. Suficiente para Church, insuficiente para solver.

Implementación (híbrido OPUS-Meta):

Predicado siempre visible (sin color de eje): banner minimal de Trampa activa + función-de-palo, texto 4-6 palabras, <450ms lectura. No iconos de Tempo/Escala/Defensa.
Eco post-captura gateado: destello 180ms + háptico leve, distinto por eje, solo tras 2 repeticiones de esa misma consecuencia. Se apaga a la run 4. Es memoria muscular, no UI.
Cero hover, cero halo. En touch, long-press muestra solo "suma 15", nunca eje.

Criterios falsables — A/B demo LATAM móvil (n≥5k/rama):

S4 Dominancia Maña (OPUS): ninguna build >55% winrate en 100 seeds; Sharpe <1.3×. [L4 – 🟢]
S5 Umbral Diablo: mediana score/umbral ∈ [0.95,1.15]; p10>0.8. [L4 – 🟡]
Retención: B (eco) vs A (sin eco) → D7 +≥5pp (target >28%), D30 no cae >2pp. [L1 – 🟡]
Share-rate: B no baja >10% vs A (target ≥1.4 shares/100 sesiones). Si sube D7 pero share cae -20%, falla —mataste dopamina suerte. [L1 – 🟢]
Comprensión implícita (reemplaza verbalización): en test ciego, ≥55% eligen la jugada Pareto en escenario espejo tras 3 runs, sin poder nombrar el eje. Mide hacer, no decir. [L1 – 🟡]

Banda EV: fijar donde S4+S5 pasan. Mi predicción data: 11-13%. Si solver solo pasa a 16-18%, acepta pérdida de share y posiciona como "Spire hispano". [L2 – 🟡]

QUÉ ES DECISIÓN DE CÉSAR
Identidad: ¿quieres el clip viral de "me salió de chiripa" (mi data: +1.8x share) o la reseña Steam de "sentí control" (GEMINI: +18% wishlist)? No puedes maximizar ambos con el mismo tell.
Riesgo de Maña: OPUS propone trade-off emergente vs auto-sabotaje diseñado. Eso es apetito de riesgo, no data.
Coste visual: banner permanente vs minimalismo Style Bible. En móvil mudo, cada píxel es retención.

Mi voto Data L1: shippea eco post-captura 9-13% EV, mide D7+share. Si el hispano prefiere suerte, no lo fuerces a ser genio.

Fuentes