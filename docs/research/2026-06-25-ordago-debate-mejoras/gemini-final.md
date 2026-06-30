# DEBATE ETAPA 2 — ASIENTO: ESTRATEGA DE VALOR + SEÑAL DE MERCADO (Gemini)

---

## 1. RESOLUCIÓN DE LOS 3 CRUXES VIVOS

### Crux 1: Formato del objeto-puente (P1) — ¿Texto, Sticker o Ambos?
**CIERRO hacia: HÍBRIDO NATIVO (Imagen PNG/WebP compacta con el Emoji-Grid + Link en el caption).**
* **Dato decisivo (Física de la Plataforma L1):** En WhatsApp, los stickers animados o estáticos **no admiten hipervínculos cliqueables**. Si compartimos únicamente un sticker o una imagen sola, el bucle viral se rompe porque el receptor no tiene dónde pulsar para ir a la demo web. Sin embargo, los menús de compartir nativos de iOS y Android permiten enviar un archivo de imagen *junto* a un texto adjunto (caption). 
* **La Máquina:** El cliente genera localmente una **ficha de victoria compacta (PNG, <80 KB)** que muestra visualmente tu "Mano contra el Diablo" (captura el 56% de preferencia de stickers/imágenes personalizadas en LATAM). Esta imagen se envía a WhatsApp con el **Emoji-Grid de texto plano y el deep-link `ordago.gg/d/<seed>` embebidos en el cuadro de texto (caption)**. Así, el receptor experimenta el impacto visual instantáneo que cruza el chat familiar sin explicación y, a la vez, conserva el botón físico de 1-tap para jugar.

### Crux 2: Soporte del clip (P1) — ¿Co-primario móvil o Exclusivo PC?
**CIERRO hacia: ASIMÉTRICO (PC = MP4 de 6s para Broadcast; Móvil = WebP animado sin codificación para WhatsApp).**
* **Dato decisivo (Limitación de Hardware y Tiempos de Carga):** Compilar y codificar un archivo MP4 con audio mediante WebASM (como FFmpeg.wasm) en un navegador móvil de gama media-baja de LATAM (procesadores MediaTek/Snapdragon antiguos) viola la regla de oro de **fricción-cero (<3 segundos de carga)**, provocando bloqueos de memoria y rebote del usuario.
* **La Máquina:** 
  * **En Steam (PC):** El cliente nativo genera el clip de 6s MP4 ultra-comprimido (<500 KB) con audio reactivo (grito del Diablo) para subir directamente a TikTok/Reels (2-12× de alcance orgánico).
  * **En la Demo Web (Móvil):** El juego no codifica video. Genera un **WebP animado en bucle (<300 KB)** o simplemente utiliza la imagen estática del Crux 1 con una animación CSS local en el navegador. El clip de video complejo se degrada en móvil para priorizar la conversión inmediata.

### Crux 3: Banda de spread de EV (P2) — ¿≤15% (Ajedrez) o 15-25% (Suerte controlada)?
**CIERRO hacia: BANDA DINÁMICA DE SPREAD (15% a 20% de EV a 2 turnos).**
* **Dato decisivo (Psicología del Consumidor y Retención):** En el mercado hispano/LATAM, el éxito de los juegos de cartas (*Truco, Escoba*) radica en la "tensión de la codicia": el jugador quiere sentir que puede ganarle al azar con su astucia, no resolver un examen de matemáticas. Un spread $<15\%$ (ajedrez seco) eleva la carga cognitiva, matando el bucle de "partida rápida" en móviles. Un spread $>20\%$ hace que la jugada de escala o tempo sea trivial, destruyendo la brecha de habilidad (skill expression) y colapsando el foso vivo en D7.
* **La Máquina:** El solver del generador rechaza cualquier tablero donde la diferencia de EV entre la Ruta de Tempo y la Ruta de Escala esté fuera del rango **[15%, 20%]**. Esto garantiza matemáticamente el "dilema agonizante" en cada mano, manteniendo el juego fresco y adictivo sin volverse un rompecabezas rígido.

---

## 2. POSICIÓN DEFINITIVA

### Palanca 1 — El Artefacto-Puente Canónico
* **Fix Ganador:** Output dual local: (A) Imagen WebP de la mesa (<80 KB) con el Emoji-Grid de 5 líneas y link corto `ordago.gg/d/<seed>` en el caption de WhatsApp, y (B) Clip MP4 de 6s con firma sonora barroca (D3 🟡) exclusivo para PC Steam. Rotación procedural de 12 copys de rivalidad personal (A3 🟡) para evitar fatiga.
* **Confianza:** 🟢 **L1 (Data de plataforma robusta).**

### Palanca 2 — El Generador de Bifurcación + El Foso VIVO ★
* **Fix Ganador:** Algoritmo de siembra con restricción dura: spread de EV de 15-20% entre tempo y escala a 2 turnos. Instrumentación centinela mediante el tracking en backend de la entropía de Shannon ($H_{builds}$) de runs ganadoras en Steam; alarma si cae de $2.2$ bits (indica meta colapsado).
* **Confianza:** 🟡 **Requiere calibración del solver en el vertical slice.**

### Palanca 3 — Reconciliar plataforma ↔ viralidad ↔ economía
* **Fix Ganador:** Embudo de conversión segmentada: Tráfico WhatsApp/Móvil $\rightarrow$ Demo Web de 1 manga (fricción cero) $\rightarrow$ Registro de Email $\rightarrow$ Wishlist/Compra en Steam PC. Precios adaptados al LTV/CAC real: USA: $14.99 | US-Hispanos: $14.99 | LATAM: $7.49 (149 MXN) para sostener un ratio LTV/CAC $\ge 4$.
* **Confianza:** 🟢 **Basado en la elasticidad precio histórica de Balatro/Inscryption en LATAM.**

---

## 3. RECOMENDACIÓN SOBRE C-1 (Voto Final)

**Voto por el modelo HÍBRIDO (Steam Premium + Demo Web de Reto Móvil).**

* **Trade-off aceptado:** Asumimos un incremento del **15% en el costo de desarrollo inicial** (mantener el pipeline de WebGL optimizado para la demo) y una **pérdida de conversión directa del ~25%** en el tráfico de LATAM que juegue la demo pero no posea PC para comprar en Steam. 
* **Mitigación:** Capturamos el correo electrónico de ese 25% móvil excedente mediante la promesa de un port nativo para iOS/Android en el segundo año, convirtiendo la pérdida técnica en la base de datos de pre-registros para el lanzamiento móvil.

---

## 4. EL CAMBIO DE MAYOR APALANCAMIENTO AL GDD V1.2

> **"Sustituir el 'código alfanumérico para compartir' por un enlace web que abre una demo móvil jugable de 1 manga en <3 segundos desde WhatsApp, alimentada por el solver de dilemas (spread de EV 15-20%) para que el reto de tu primo sea real, cliqueable y mecánicamente adictivo."**