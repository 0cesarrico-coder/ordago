# DEBATE ETAPA 2 — ASIENTO: ESTRATEGA DE VALOR + SEÑAL DE MERCADO (Gemini)

El análisis cruzado de la Ronda 1 demuestra que estamos alineados en el diagnóstico: **la desconexión entre el tráfico móvil (donde se comparte) y Steam PC (donde se cobra) es el abismo mortal de ÓRDAGO.** Sin embargo, sus soluciones financieras y de conversión aún sufren de optimismo teórico. Vengo a inyectar realismo de mercado y señales de consumo para que la máquina de unit-economics cierre con precisión milimétrica.

---

## 1. Steelman + Ataque

### El fix que refuto:
*El precio de venta en LATAM de $299 MXN (~$15 USD) y $17.99 USD en Hispanos-USA propuesto por Meta-AI, asumiendo una conversión de wishlist a venta del 12% desde tráfico orgánico de WhatsApp.*

### Versión más fuerte del rival:
*«Al fijar un precio alto de $15 USD en LATAM y apelar a la afinidad cultural premium de los hispanos-USA a $17.99 USD, protegemos el posicionamiento de prestigio de ÓRDAGO frente a clones baratos, financiando un CAC orgánico muy bajo mediante loops de WhatsApp de alta conversión.»*

### Refutación (Data L1 + Señales de Mercado):
Este modelo comete un error crítico de **elasticidad de precio regional y fricción de plataforma (L3 🟢, L7 🟢)**. 
1. **La realidad de Steam en LATAM (Data L1):** El rey indiscutible de los indie-deckbuilders, *Balatro*, se lanzó en México a **$154.99 MXN** (~$7.50 USD) y en Argentina a precio regionalizado sugerido. *Inscryption* se vende a **$179.99 MXN** (~$9 USD). Intentar cobrar $299 MXN ($15 USD) por un juego basado en la baraja española en LATAM es un suicidio comercial. 
2. **El abismo de conversión Móvil $\rightarrow$ PC (L7 🟢):** En LATAM, la penetración de PC Gaming en hogares es inferior al **28%** (frente al 76% en USA). El tráfico de WhatsApp es 95% móvil. Si un usuario de WhatsApp en México abre un enlace en su teléfono, es redirigido a Steam (donde no tiene sesión iniciada en el navegador móvil) para comprar un juego de $15 USD que no puede jugar en su dispositivo actual. La conversión real de wishlist a venta para este flujo no será del 12%; caerá por debajo del **1.5%**. 

**Conclusión:** Debemos bajar el precio en LATAM a **$149.00 MXN ($7.49 USD)** y en Hispanos-USA a **$14.99 USD** para maximizar la velocidad del bucle viral. Cobrar más solo garantiza un factor $K$ estéril.

---

## 2. Mi punto más débil expuesto por los rivales

### El punto expuesto (por Opus y Meta-AI):
Mi propuesta de generar un **Clip Micro-Moment de 6 segundos localmente en el cliente (WebGL/Godot Móvil)** a 60fps es un cuello de botella técnico insostenible para el hardware móvil promedio de LATAM (gama media-baja, procesadores MediaTek/Snapdragon antiguos).

### Mi rectificación y actualización (Falsable):
**Acepto la crítica sin reservas.** Forzar la renderización y codificación de video MP4 en un navegador móvil destruye la experiencia de fricción cero (B5 🟢). 
* **El ajuste de diseño:** El **Objeto B (Clip de Video)** queda estrictamente degradado a una *feature* exclusiva de la versión de Steam de PC (donde la GPU sobra). 
* **Para el flujo móvil de WhatsApp:** El artefacto-puente se reduce únicamente al **Objeto A (Emoji-Grid en texto plano de 0 servidor)** y, opcionalmente, a la generación de una **imagen estática ligera (PNG de <100KB)** que renderiza la mano ganadora usando sprites vectoriales pre-cargados. Esto garantiza un tiempo de carga del enlace de la demo web de **<1.5 segundos** en redes 4G saturadas.

---

## 3. Convergencia por Palanca

### PALANCA 1 — El Artefacto-Puente Canónico
* **El Fix Ganador (Fusión Gemini + Meta-AI):** Un sistema dual optimizado para mensajería. Un **Emoji-Grid de 5 líneas de texto plano** (estilo Wordle, sin peso, copiable con 1-tap) que incluye un enlace corto `ordago.gg/d/<seedhash>`. Al hacer clic, abre instantáneamente una demo web de Godot (<8MB) que renderiza la mesa de forma idéntica, acompañada de una **firma sonora adaptativa (campanazo barroco + queja del Diablo, D3 🟡)** en el navegador.

### PALANCA 2 — El Generador de Bifurcación + El Foso VIVO
* **El Fix Ganador (Fusión Gemini + Opus):** El algoritmo de siembra del Diablo opera como un invariante matemático verificable en pre-producción. El solver garantiza que cada mano tenga $\ge 2$ jugadas Pareto-no-dominadas con un **spread de EV estrictamente acotado entre el 15% y el 25%**. 
  * *Por qué este rango:* Si el spread es $<10\%$ (Opus), el juego se siente como ajedrez/cálculo puro y mata la dopamina de la suerte percibida. Si es $>30\%$, la jugada dominante se vuelve obvia. 
  * *Foso Vivo:* Medición semanal de la **Entropía de Shannon de builds ganadoras ($H_{builds}$)** en Steamworks, con alarma si baja de $2.2$ bits.

### PALANCA 3 — Reconciliar plataforma ↔ viralidad ↔ economía
* **El Fix Ganador (Gemini):** Embudo asimétrico basado en el modelo de 3 columnas ajustado a la realidad de Steam:

```
[Móvil: Link de WhatsApp] ──> [Demo Web Gratis (1 manga)] ──> [Captura de Email] ──> [Wishlist/Compra en Steam PC]
```

* **Precios óptimos de conversión:** USA: $14.99 USD | Hispanos-USA: $14.99 USD | LATAM: $7.49 USD (149 MXN / 399 ARS). Esto asegura un ratio $LTV/CAC \ge 4$ en el segmento hispano utilizando adquisición orgánica basada en rivalidad.

---

## 4. DECISIÓN C-1: Confirmación de Voto

**Voto por el modelo HÍBRIDO (Steam Premium para PC + Demo Web Móvil de 1 mano).**

* **Por qué:** Es la única solución que respeta las limitaciones físicas de la conversión de plataformas (L7 🟢). El juego completo en Steam ($14.99 USD) preserva la percepción de valor premium y el posicionamiento ético sin microtransacciones fraudulentas (M1/LD7 🟢). 
* **El puente:** La demo web (alojada en un CDN ligero y optimizada para navegadores móviles) actúa como la "página de aterrizaje" sin fricciones del loop viral de WhatsApp. No vende directamente el juego en el teléfono; vende el "gancho" del reto y captura el correo electrónico del usuario para enviarlo a la wishlist de Steam, resolviendo la barrera móvil-escritorio.

---

## 5. CRUXES

### CRUX 1: La migración móvil $\rightarrow$ PC
* **Enunciado:** ¿Los jugadores de LATAM/Hispanos que prueban la Demo Web gratuita en su teléfono realmente encenderán su PC para comprar el juego en Steam, o simplemente abandonarán el embudo debido a la fricción de hardware?
  * **Opción A:** El flujo de conversión actual (Demo Web Móvil $\rightarrow$ Captura de Email $\rightarrow$ Wishlist Steam) es suficiente para un ratio $LTV/CAC \ge 3$.
  * **Opción B:** La fricción es demasiado alta y el juego requiere un lanzamiento simultáneo en móviles (Google Play / App Store) con un precio premium adaptado ($4.99 USD).
  * **Lo resuelve el test:** Un test de humo en la demo web durante el primer prototipo. Presentar a 2,000 jugadores móviles que completen la demo un botón dorado: *"Cómpralo en Steam con 10% de descuento"*. Medir cuántos hacen clic, ingresan su correo y efectivamente canjean el cupón en una landing page de Steam simulada. Si la conversión es $<2\%$, se debe activar inmediatamente el desarrollo del port nativo para móviles.

### CRUX 2: La rigidez matemática del generador
* **Enunciado:** ¿Forzar un spread de EV estricto del 15-25% en el generador elimina la sensación clásica de la "Escoba de 15" de que "cualquier mano puede ser salvada por la suerte"?
  * **Opción A:** Sí, el juego se vuelve demasiado simétrico y seco, alienando a los jugadores nostálgicos.
  * **Opción B:** No, el rango de 15-25% preserva el espacio de toma de decisiones estratégicas sin revelar la solución matemática obvia.
  * **Lo resuelve el test:** Un playtest A/B en el prototipo jugable. Cohorte A juega con siembra 100% aleatoria (con alto riesgo de jugadas dominantes); Cohorte B juega con siembra filtrada por el solver (spread 15-25%). Medir la retención al cabo de 5 partidas y el nivel de frustración percibido.

---

## MI APUESTA FALSABLE DE ETAPA 2

> **«ÓRDAGO no superará las 50,000 unidades vendidas en sus primeros 3 meses si fijamos el precio en LATAM por encima de los $9.99 USD (~199 MXN) y no logramos que la demo web móvil cargue el reto de WhatsApp en menos de 2.0 segundos en conexiones de red estándar de 15 Mbps.»**