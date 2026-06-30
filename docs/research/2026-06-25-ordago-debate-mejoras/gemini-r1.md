# DEBATE ETAPA 2 — ASIENTO: ESTRATEGA DE VALOR + SEÑAL DE MERCADO (Gemini)

Un workflow de 135 agentes ha hecho un diagnóstico implacable. El verbo de **ÓRDAGO** es de clase mundial, pero la capa de entrega y la ingeniería financiera son humo de PowerPoint. Vengo a destruir el sesgo de confirmación: **el "CAC~0 vía WhatsApp" para un juego premium de $15 USD en Steam es una fantasía técnicamente imposible** sin la arquitectura de puente correcta. 

Como **Estratega de Valor y Señal de Mercado**, vengo a reconciliar el diseño profundo con los números fríos del mercado de consumo (USA, hispanos-USA y LATAM), utilizando señales de volumen de búsqueda de YouTube, fricción de plataforma y conversión real.

---

## PALANCA 1 — El Artefacto-Puente Canónico (§8.3 nuevo)

### El Fix de Clase Mundial (Cambio Concreto al GDD v1.2)
Añadir la sección **§8.3 "El Artefacto-Puente de ÓRDAGO: El Motor de Reenvío"**. Prohibido el código de texto plano como core viral (D1 🟢, C2 🟡). El loop de reenvío se divide en dos outputs automáticos de 1-tap generados localmente por el cliente (0 costo de servidor por renderizado):

```
                       [ JUGADOR EN STEAM / WEB DEMO ]
                                      |
                 +--------------------+--------------------+
                 | (1-Tap Share)                           | (Auto-Generación)
                 v                                         v
       [ EL EMOJI-GRID (WhatsApp) ]              [ EL CLIP MICRO-MOMENT (6s) ]
  • Fila de palos: 🪙 🍷 ⚔️ 🌳                 • MP4 ligero (<800KB)
  • "Le robé el alma a [Primos Group]"      • Barrido de Escoba + ¡Zas! + Firma
  • Score: 14,250 (Semilla #402)            • Audio-reactivo (Devil: "¡Tramposo!")
  • Link corto → Abre Demo Web              • QR / Link en marca de agua
```

1. **El Emoji-Grid de WhatsApp (Grafo Estrecho):** Copiado al portapapeles con formato específico para chats familiares.
   > *«Le robé el alma al Diablo de mi primo @Carlos en la Mesa de hoy (Semilla #402).*
   > *🪙 🍷 🍷 [Escoba Mayor]*
   > *⚔️ 🌳 🪙 [Pacto Roto]*
   > *Score: 14,250 | ¿Te da la maña para ganarme? Juega mi mano gratis aquí: [Link de la Demo Web de 1 mano]»*
   
   *Sin spoilers:* El link contiene el hash de la semilla (`?seed=402&rival_score=14250&rival_name=Carlos`). No revela las cartas de la mesa, solo inicializa el mismo estado aleatorio determinista para el receptor.

2. **El Clip Micro-Moment (TikTok/Shorts - Grafo Amplio):** Un shader local renderiza en segundo plano un loop de video de 6 segundos ($60\text{ fps}$, ultra-comprimido, <800KB, formato 9:16) con la última jugada exponencial de la run. 
   * **El Hook Visual:** Las cartas vuelan por la pantalla con física de gravedad barroca (estilo Posada).
   * **La Firma Sonora (D3 🟢/🟡):** El tintineo metálico de los Reales, el latigazo del naipe, el grito imitable del Diablo de fondo (*"¡Tramposo!"*) y el acorde final de jarana barroca.
   * **La Llamada:** Código QR dinámico en la esquina superior derecha y un link de redirección.

### Riesgo Principal + Mitigación
* **Riesgo:** Reactancia y fatiga de spam en grupos de WhatsApp. Si el mensaje se lee como publicidad institucional, el usuario borra el link y el factor viral $K$ colapsa a 0.
* **Mitigación:** *Diseño con ADN de Meme (A3 🟡).* El texto del reenvío debe ser 100% editable, informal y centrado en la **rivalidad personal**, no en la marca del juego. El juego no se autopromociona; es el jugador el que humilla a su primo.

### El Test/Kill Más Barato
**Test de Fricción de Reenvío en WhatsApp (Papel/WhatsApp Web):** Crear un grupo de WhatsApp con 20 usuarios del cohorte "hispanos-USA/LATAM" (18-34 años). Darles un borrador del emoji-grid y un link simulado. 
* **Criterio de Kill:** Si $<40\%$ de los participantes se siente cómodo reenviándolo a su grupo familiar/amigos real por vergüenza o porque "parece spam", el formato del artefacto está muerto. Rediseñar hasta que el reenvío sea un acto de ego natural.

---

## PALANCA 2 — El Generador de Bifurcación + El Foso VIVO

### El Fix de Clase Mundial (Cambio Concreto al GDD v1.2)
Modificar **§7.3 "La Mesa Viva"**. El algoritmo del Diablo no siembra cartas al azar. Para asegurar que "sumar 15" no sea un cálculo aritmético con solución única dominante (A1 🟢/🟡), el motor de siembra opera bajo el **Invariante de Pareto de Dos Vías**:

```
                       [ ESTADO DE LA MESA (Turno N) ]
                                      |
                     (Algoritmo de Siembra del Diablo)
                                      |
             +------------------------+------------------------+
             v                                                 v
     [ RUTA DE TEMPO (Escoba Rápida) ]                 [ RUTA DE ESCALA (Mata/Oros) ]
     • Retorno inmediato de Puntos base.               • Sacrifica mesa para preparar combo.
     • Limpia la mesa de inmediato.                    • Mayor riesgo de Trampa / Bloqueo.
             +------------------------+------------------------+
                                      v
                    ¿Ambas rutas son viables en el Turno?
                                      |
                        +-------------+-------------+
                        | Sí                        | No
                        v                           v
                 [ Aprobar Tablero ]        [ Regenerar Siembra ]
```

1. **La Ecuación de Decisión:** Cada carta sembrada en la mesa debe tener un peso de **Valor Futuro ($V_f$)** frente a su **Valor de Captura Inmediato ($V_i$)**.
2. **La Bifurcación Diseñada:** El algoritmo calcula las dos mejores jugadas posibles del jugador en cada mano:
   * **Ruta de Tempo:** Una jugada que limpia la mesa rápido (Escoba), asegurando puntos base inmediatos pero consumiendo cartas valiosas de la mano.
   * **Ruta de Escala:** Una jugada que no limpia la mesa (no hace Escoba), pero conserva un Oro o una Mata en mano para preparar una cascada multiplicadora en el siguiente turno, asumiendo el riesgo de que el Diablo aplique un "Bloqueo" (§7.3) en su turno.
3. **El Filtro Invariante:** Si en el análisis del árbol de juego de la mano una sola de las opciones supera a la otra por más del $35\%$ de Valor Esperado (EV), la siembra se descarta y el algoritmo regenera la mesa añadiendo una carta de bloqueo o una carnada. El juego solo te entrega tableros donde elegir la opción segura vs. la codiciosa duela en el cerebro.

#### Instrumentación del Foso Vivo en Early Access (§18):
Vigilar la **Entropía de Shannnon de builds de Maña ($H_{builds}$)** de forma semanal en base de datos.
$$H_{builds} = -\sum (p_i \log_2 p_i)$$
Donde $p_i$ es la frecuencia de uso del combo de Maña $i$ en runs ganadas.
* **Alarma de Colapso Metagame:** Si $H_{builds} < 2.0$ bits en una cohorte de más de 7 días, significa que el $80\%$ de los jugadores ha descubierto una build dominante única (el "meta de un solo truco"). El juego se ha vuelto estático.
* **Mitigación:** El sistema responde ajustando los pesos de riesgo de la Sospecha (§7.6b) de las piezas sobreutilizadas, no nerfeando los multiplicadores de daño.

### Riesgo Principal + Mitigación
* **Riesgo:** Que el jugador perciba que la inteligencia artificial del Diablo hace "trampa oculta" manipulando la baraja para forzar la bifurcación, rompiendo la confianza en la física justa del naipe.
* **Mitigación:** La baraja del jugador es física y finita. El Diablo solo siembra desde *su* mazo corrupto visible, cuyas cartas restantes se pueden contar y predecir en la interfaz. La trampa del Diablo es transparente y sus reglas son públicas.

### El Test/Kill Más Barato
**Solver de Papel de 100 Manos:** Diseñar un script básico en Python sin gráficos. Correr 1,000 simulaciones de tableros sembrados automáticamente. Si en más del $15\%$ de los casos el script encuentra que una sola jugada es óptima en todos los escenarios de riesgo (tempo y escala), el generador de bifurcación ha fallado. Reajustar la heurística del algoritmo de siembra antes de escribir una sola línea de código en el engine.

---

## PALANCA 3 — Reconciliar plataforma ↔ viralidad ↔ economía (§16.1)

El modelo de "un juego premium de $15 USD que se hace viral por WhatsApp" es una contradicción estructural. El tráfico móvil de WhatsApp tiene una fricción de conversión del $99\%$ hacia una compra de escritorio en Steam (B5 🟢, L7 🟡). Para solucionar esto, modelamos la economía con un embudo híbrido (Steam Premium + Demo Web Ligera de 1 mano sin registro) estructurado por segmentos de mercado realistas.

### El Fix de Clase Mundial: Unit-Economics B2P de 3 Columnas (§16.1 nuevo)

Aterrizamos los números financieros netos para el ciclo de vida del juego (proyecciones de lanzamiento de 12 meses):

| Métrica / Variable de Negocio | USA (Steam Direct) | Hispanos-USA (Sweet Spot Target) | LATAM (Regionalizado) |
| :--- | :--- | :--- | :--- |
| **Precio de Venta Sugerido** | $19.99 USD | $14.99 USD | $7.99 USD (Promedio) |
| **Comisión de Plataforma (Steam 30%)** | -$6.00 USD | -$4.50 USD | -$2.40 USD |
| **Impuestos + Retenciones Estructuradas** | -$1.00 USD ($5\%$) | -$0.75 USD ($5\%$) | -$1.20 USD ($15\%$) |
| **Tasa de Reembolso (Refund Rate)** | $8\%$ (-$1.04 USD) | $10\%$ (-$0.97 USD) | $14\%$ (-$0.61 USD) |
| **Ingreso Neto por Unidad Vendida ($LTV$)** | **$11.95 USD** | **$8.77 USD** | **$3.78 USD** |
| **Costo de Adquisición de Tránsito ($CAC$)** | $4.20 USD (Paid Ads/PR) | $1.80 USD (Social Ads/Micro-inf) | $0.35 USD (Viral Orgánico/Grafo) |
| **Conversión Demo Web (Móvil) → Wishlist Steam**| N/A (Tráfico Directo PC) | $4.5\%$ | $7.0\%$ |
| **Relación de Rentabilidad ($LTV / CAC$)** | **$2.84$** (Límite saludable) | **$4.87$** (Eficiencia óptima) | **$10.80$** (Foso de tracción) |
| **Payback Period (Meses de retorno)** | 3.5 meses | 1.8 meses | 0.5 meses |

*Señales de Intención de Consumo (L1 data de plataforma 🟢/🟡):* Las búsquedas de "La Escoba de 15" y "Truco Argentino/Mexicano" tienen su pico en dispositivos móviles (82% del tráfico en LATAM). Forzar a un usuario móvil de WhatsApp a abrir Steam en su teléfono para comprar un juego de $15 dólares mata el impulso de compra. El flujo debe ser: **Link de WhatsApp móvil $\rightarrow$ Demo Web instantánea en navegador móvil $\rightarrow$ Cuenta de correo (Wishlist) $\rightarrow$ Compra final en PC (Steam).**

### Riesgo Principal + Mitigación
* **Riesgo:** Que el tráfico de LATAM consuma todo el ancho de banda del servidor de la demo web pero no convierta a ventas de Steam debido a la falta de computadoras de juego (PC Gaming) en ciertos sectores demográficos.
* **Mitigación:** La demo web móvil está optimizada para consumir $<10\text{MB}$ de transferencia y corre en el cliente del navegador. El botón de conversión en LATAM debe ofrecer, además de Steam, la opción "Registrar para lanzamiento en Móviles (Google Play / App Store)" para capturar la preventa de un port premium móvil post-lanzamiento.

### El Test/Kill Más Barato
**Test de Humo de Conversión en Landing Page:** Gastar $100 USD en Meta Ads segmentando a hispanos-USA e hispanos-LATAM con un anuncio de video falso de 6 segundos que muestre el juego. El botón de llamada a la acción lleva a una página con la promesa: *"Juega la demo en tu teléfono ahora"*. 
* **Criterio de Kill:** Si la tasa de click-through (CTR) es $<2.5\%$ o el costo por lead para registrarse a la beta cerrada supera los $0.50 USD en LATAM / $1.50 USD en hispanos-USA, el interés por la baraja tradicional como gancho de juego digital moderno no es suficiente para sostener un desarrollo premium. Matar el proyecto de inmediato.

---

## DECISIÓN DE CÉSAR — C-1 (Recomendación e Informe de Trade-Off)

### Recomendación Estratégica: El Modelo Híbrido (Steam Premium + Demo Web Móvil de Reto)

Como Estratega de Valor, recomiendo rechazar el lanzamiento exclusivo en Steam Direct y rechazar el modelo puramente web. **La única ruta hacia el #1 del mundo sin perder la credibilidad premium ni el motor viral es el Modelo Híbrido.**

```
   [ WHATSAPP / TIKTOK MÓVIL ]
                |
                v  (Fricción Cero - 3s Load)
    [ DEMO WEB DE RETO MÓVIL ]  <-- (Juegas exactamente la mano que te enviaron)
                |
                +------------------------+------------------------+
                | Si Pierde / Quiere más | Si Gana (Ego inflado)  |
                v                        v                        v
        [ "Pactar con el Diablo" ]  [ "Humillar en Steam" ]  [ Compra Steam ]
                |                        |                   (PC - $14.99-$19.99)
                +------------------------+-------------------+
                                         v
                         [ Captura de Email / Wishlist ]
```

### El Flujo del Trade-Off de Plataforma

* **Web-Native-First:** 
  * *Pros:* Máxima conversión viral, fricción cero, alcance masivo instantáneo.
  * *Contras:* Monetización devaluada (la web no paga premium de $15 USD), piratería incontrolable, pérdida del posicionamiento de prestigio de Steam junto a *Balatro* e *Inscryption*.
* **Steam-First Puro:** 
  * *Pros:* Reputación premium, protección de archivos, visibilidad orgánica del algoritmo de Steam (muy fuerte para el género roguelike).
  * *Contras:* Mutilación total del motor viral móvil. Un link de WhatsApp compartido en un smartphone tiene un $99\%$ de fricción de salida si requiere que el usuario vaya a su PC a comprar el juego.
* **El Modelo Híbrido (Nuestra Propuesta):**
  * *Cómo funciona:* El juego completo de $15-$20 USD se vende **únicamente en Steam** para PC como experiencia de prestigio. Sin embargo, el estudio mantiene una **Demo Web ligera basada en WebGL/Godot** alojada en un dominio propio de bajo costo. 
  * *La magia:* Cuando un jugador comparte un reto desde Steam, el link abre la Demo Web en el teléfono del receptor en menos de 3 segundos sin descargar nada. El receptor juega **solo esa mano específica** contra el "Diablo Fantasma" de su amigo. Si quiere jugar más mangas, configurar su baraja o comprar maña, el juego le muestra el botón dorado: *"Cómpralo en Steam para guardar tu alma"*.

---

## Mi Apuesta Falsable de Red-Team

> **«ÓRDAGO no llegará al #1 del mundo a menos que el juego logre convertir la victoria en una humillación personal compartible y el juego tenga una demo web de 1 mano jugable en móviles en menos de 3 segundos desde un link de WhatsApp.»**

Si mantenemos el juego cerrado en un instalador de Steam tradicional y seguimos confiando en "códigos de texto para compartir builds", seremos un juego de nicho respetable con buenas reseñas pero sin volumen de negocio masivo. Si abrimos la mesa de juego al ecosistema móvil sin fricciones a través de la demo de reto, capturaremos el mercado de consumo desatendido de más de 500 millones de hispanohablantes antes de que los competidores angloparlantes se den cuenta de que la baraja española era el mayor foso cultural sin explotar de la década.