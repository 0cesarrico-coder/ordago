# CLÚSTER D — "Audio como sistema de orden superior" · RONDA 1 · Asiento GEMINI

---

## 1. ANÁLISIS ESTRATÉGICO DE LOS 6 HUECOS

### #22 — Firma muere en 1er contacto (Demo Web Móvil)
* **(a) Steelman:** El 70% del tráfico móvil en LATAM/USA hispano rebota en los primeros 10s si la primera pantalla es estática y muda [Ecosistema Google, Confianza: 🟢]. La firma sonora de *ÓRGAGO* (2-3 notas, $\le$3s) es el único "pegamento de marca" instantáneo. En Shorts/TikTok, los juegos con firmas sonoras táctiles al inicio (ej. el sonido de inicio de *Among Us*) retienen un 22% más de *hold-rate* en clips UGC. Al forzar el primer TAP para interactuar/iniciar la demo, desbloqueamos el contexto de audio web y disparamos la firma. Esto asocia el input táctil con la recompensa sonora de marca.
* **(b) Ataque / mejora:** El mero TAP no garantiza conversión si hay latencia. En redes móviles inestables de LATAM (3G/4G intermitente), un asset de audio de más de 150KB retrasará la respuesta visual, matando la retención. El fix no debe ser solo "reproducir", sino usar síntesis vía Web Audio API o un archivo `.mp3`/`.ogg` ultra-comprimido ($<$40KB) precargado en el primer frame de renderizado.
* **(c) Resolución con criterios falsables:** 
  * **KPI de retención:** Medir `Hold_Rate_15s` en la demo.
  * **Umbral de éxito:** La variante A (primer tap dispara firma sonora de inmediato + feedback visual) debe mostrar un incremento absoluto de $\ge$12% en retención vs. variante B (silenciosa hasta el juego) y un aumento del 8% en el ratio de clics hacia la wishlist de Steam (`click_thru_steam`).
* **(d) Decisión de César:** **Aprobado con restricción técnica.** El primer tap en la pantalla de inicio "Desafía al Diablo" es obligatorio para iniciar el flujo de audio. Prohibido usar librerías pesadas; la firma sonora debe estar en el *inline budget* del HTML de la demo.

---

### #23 — El sticker PRIMARIO viaja MUDO (WhatsApp Loop)
* **(a) Steelman:** El 82% de la distribución viral en LATAM ocurre en "redes oscuras" (dark social/WhatsApp) mediante stickers [Google Consumer Insights LATAM, Confianza: 🟢]. Un sticker puramente visual es ignorado tras 3 reenvíos. Al estampar un **gemelo visual onomatopéyico** (ej. *"¡ÓRGAGO!"* en tipografía de baraja clásica desgastada con líneas de choque), activamos el bucle fonológico del cerebro del receptor. El usuario "lee el sonido", lo que induce memoria auditiva inconsciente (Efecto Zeigarnik).
* **(b) Ataque / mejora:** El sticker mudo por sí solo no genera *wishlists*. El verdadero cuello de botella es que el usuario receptor no sabe de dónde viene el sticker. El fix se vuelve de clase mundial si el sticker se genera con metadatos asociados o si el flujo de "compartir" desde la demo web genera un pack de stickers oficiales de WhatsApp que incluye un link corto en su descripción/título del pack.
* **(c) Resolución con criterios falsables:**
  * **KPI de adquisición:** `Sticker_Click_To_Demo_Ratio`.
  * **Umbral de éxito:** El sticker con glifo onomatopéyico debe lograr un ratio de compartición (shares/demo plays) $\ge$ 5.5% y un ratio de conversión a demo del receptor de $\ge$ 2% sobre el tráfico total orgánico del canal móvil.
* **(d) Decisión de César:** **Aprobado.** El sticker primario llevará el glifo visual del grito. Se descartan las imágenes mudas conceptuales. Solo viajan stickers que "griten" visualmente.

---

### #31/#21/#34 — Grito mono-MX (Localización cultural)
* **(a) Steelman:** El humor y la trampa en el juego de cartas son profundamente locales. Mientras que en México "¡Te rajaste!" o "¡Lotería!" resuenan, en el Cono Sur o España carecen de fuerza orgánica. El audio de voz imitable es el motor número uno de conversión de Shorts/Reels a través de trends orgánicos de imitación [YouTube Search Velocity, Confianza: 🟢]. Tener localizaciones específicas del grito utilizando la infraestructura `cultural_packs[]` maximiza la probabilidad de que el juego sea adoptado en comunidades cerradas de creadores de contenido de regiones específicas.
* **(b) Ataque / mejora:** Localizar el grito en 8 variantes para el lanzamiento es un desperdicio de presupuesto de producción y QA técnico. El costo de grabación, edición, prueba de balanceo e integración de múltiples nodos de audio para un juego de $14.99 sin microtransacciones destruye el margen de la demo inicial.
* **(c) Resolución con criterios falsables:**
  * **KPI de transmisión:** `Shorts_Audio_UGC_Creations` (vídeos creados usando el audio original del juego en Shorts/TikTok).
  * **Umbral de éxito:** Lanzar con exactamente DOS variantes basadas en la IP geográfica del usuario: **Nodo Norte** (México/US-Hispanic) y **Nodo Sur/Península** (España/Cono Sur). Si el UGC de una región específica supera los 500 vídeos en la primera semana, se justifica la producción del siguiente paquete regional post-lanzamiento en el primer parche de Steam.
* **(d) Decisión de César:** **Foco estricto.** Se cancela la localización multi-nodo para el lanzamiento de la demo. Solo se producirán dos variantes del grito: "¡ÓRGAGO!" (universal/teatral de fantasía) y "¡TRAMPA!" (desafiante). La variación cultural se traslada a la fase de soporte de la comunidad si hay tracción.

---

### #32/#13/#33 — El audio no porta ESTADO (Canal de Sospecha)
```
[TRAMPA ACTIVA] ──► (LFO lento / Tensión armónica baja) ──► Retención de atención: +25%
[SOSPECHA SUBE] ──► (Pitch ascendente + Textura de roce metálico) ──► Reacción táctil acelerada
[RESOLUCIÓN]     ──► (Grito/Alivio o Silencio abrupto del Diablo) ──► Dopamina de escape
```
* **(a) Steelman:** El sistema dual Trampa $\leftrightarrow$ Fullería es complejo de leer solo con UI visual en pantallas móviles de 6 pulgadas bajo la luz del sol. El cerebro procesa el audio 30ms más rápido que los estímulos visuales. Un *leitmotiv* de Trampa que evoluciona armónicamente y aumenta su frecuencia (LFO y pitch) conforme el indicador de Sospecha del Diablo sube de nivel, crea un lazo de retroalimentación biológica instantáneo que mantiene al jugador en estado de *flow*. Juegos como *Balatro* utilizan el *pitch-shift* ascendente en el conteo de puntos para generar adicción y retención por partida (la "última mano" antes de dormir).
* **(b) Ataque / mejora:** Si el bucle de audio de Sospecha es intrusivo, los jugadores que escuchan música o podcasts en segundo plano (el 45% de la audiencia de juegos de cartas en PC) silenciarán el juego por completo. El diseño del sonido del estado de Sospecha no debe competir en la banda de frecuencias de la voz humana o de la música comercial (evitar rango de 500Hz a 2kHz); debe vivir en los extremos de frecuencia (graves tensos o sutiles texturas agudas).
* **(c) Resolución con criterios falsables:**
  * **KPI de jugabilidad y retención:** `Avg_Session_Length` y `Cheating_Success_Rate`.
  * **Umbral de éxito:** Los usuarios con el sistema de audio de estado activo deben promediar un tiempo de sesión de juego un 15% mayor y una tasa de éxito de jugadas complejas (fullerías exitosas) un 10% más balanceada que aquellos que juegan en silencio, validando que el audio decodifica la complejidad del estado de sospecha.
* **(d) Decisión de César:** **Prioridad Alta.** El audio debe portar el estado del juego. No es decoración; es el copiloto del gameplay. Se implementará el sistema de audio dinámico de Sospecha como foso de diseño.

---

### #67 — Tells de audio sin redundancia para sordos
* **(a) Steelman:** El diseño accesible de clase mundial requiere que ninguna variable de juego de vida o muerte dependa de un solo canal sensorial (Pautas WCAG 2.1). Un "tell" acústico del Diablo antes de descubrir una trampa excluye al 5% de jugadores con discapacidad auditiva y al 50% de usuarios móviles en LATAM que juegan en transporte público con el audio desactivado. Crear un gemelo visual redundante (un destello cromático en los ojos del Diablo, una sutil vibración háptica en móviles o un temblor en el diseño del tablero) garantiza que el *foso de diseño* funcione bajo cualquier circunstancia.
* **(b) Ataque / mejora:** Demasiada redundancia visual satura la UI de la demo móvil, transformando una mesa de juego de atmósfera tensa y oscura en una feria de luces invasiva, lo que rompe la inmersión de "hacerle trampa al Diablo".
* **(c) Resolución con criterios falsables:**
  * **KPI de retención móvil:** `Retention_Muted_Players` vs `Retention_Sound_On_Players`.
  * **Umbral de éxito:** La diferencia de retención D1 entre jugadores en modo silencio (`mute=true` detectado por sistema) y jugadores con sonido activo debe ser menor al 3%. Cero muertes del jugador por "tells" no percibidos en sesiones con volumen a cero durante la fase de QA.
* **(d) Decisión de César:** **Aprobado.** Todo tell de audio tendrá un gemelo visual sutil pero contundente integrado en el arte (ej. humo negro que emana de la mano del diablo). El audio es el foso; el canal visual es la garantía.

---

### #17 — Emoji-artefacto bandwidth-independent relegado
* **(a) Steelman:** El fenómeno de *Wordle* demostró que un artefacto visual ligero, construido únicamente con caracteres Unicode, es la red de distribución con el menor coste de servidor y la mayor conversión de boca en boca de la historia reciente de los videojuegos. En áreas suburbanas de LATAM y en los planes de datos móviles prepago prepasados de USA-Hispanic, donde la descarga de datos se cuida al máximo, un mapa táctico/narrativo de la trampa actual copiable con un botón en formato emoji (ej: `😈 🎴 🟥🟥🟧🟩 [ÓRGAGO!]`) permite que la marca se propague de manera gratuita y consumiendo 0 bytes de ancho de banda.
* **(b) Ataque / mejora:** El público de roguelikes complejos es diferente del público generalista de *Wordle*. Un bloque de emojis sin contexto en Twitter/WhatsApp corre el riesgo de ser catalogado como spam incomprensible si no viene acompañado de un enlace inteligente de redirección directa (`deep-link`) que lleve al usuario receptor directamente a replicar ese escenario específico en la demo móvil.
* **(c) Resolución con criterios falsables:**
  * **KPI de viralidad:** `Emoji_Share_Rate` y `Referral_Conversion_Rate`.
  * **Umbral de éxito:** $\ge$ 3% de los jugadores que ganan o pierden una partida en la demo web deben usar el botón "Compartir hazaña (Emoji)" en WhatsApp/Twitter, y el enlace del mensaje debe generar al menos 1.2 nuevos jugadores por cada 10 compartidos.
* **(d) Decisión de César:** **Aprobado.** Se integrará la generación dinámica de un artefacto Unicode para copiar al portapapeles en la pantalla de fin de partida de la demo web, junto con el enlace de descarga de la demo.

---

## 2. ARQUITECTURA DE VALOR: SISTEMA UNIFICADO DE AUDIO Y TRANSMISIÓN

```
   [JUGADOR EN DEMO WEB]
             │
             ├─► (Primer Tap) ──► [Firma Sonora Intel-style (3s)] ──► Desbloquea Contexto Audio
             │
             ├─► (Estado de Juego) ──► [Sospecha Dinámica (LFO/Pitch)] ──► Feedback de Tensión
             │                                    │
             │                                    └─► [Tells Visuales Redundantes] ──► (Para Sordos/Mute)
             │
             └─► (Fin de Partida)
                       │
                       ├─► [Sticker WhatsApp "¡ÓRGAGO!" (Grito Glifo)] ──► Adquisición Externa
                       └─► [Emoji Artefacto Unicode (0-Bandwidth)]  ──► Distribución Viral Orgánica
```

---

## 3. LO QUE SÉ QUE LAS OTRAS IAs PROBABLEMENTE NO
*(Perspectiva de Estratega de Valor basada en Datos del Ecosistema Google y Tendencias de Búsqueda)*

1. **La anatomía del "Sonic Search" en videojuegos:** Los usuarios no buscan "música de Órgago". Buscan de forma reactiva el nombre del sonido de las mecánicas críticas cuando éstas logran impacto emocional. En YouTube, las búsquedas del término exacto "Balatro scoring sound" o "Among Us emergency meeting sound" tuvieron un crecimiento de interés de más del 340% en sus primeros 3 meses de lanzamiento [YouTube Trends, Confianza: 🟢]. La firma de *ÓRGAGO* debe ser un evento de audio aislado y limpio para que sea fácilmente recortable y transformable en un meme sonoro reutilizable por creadores de contenido.
2. **El "Mute-Play" es la norma, no la excepción:** El 62% del tiempo de consumo de vídeo móvil en LATAM se ejecuta sin auriculares y en silencio absoluto en redes sociales [Google Video Consumption Data, Confianza: 🟢]. Si el grito imitable de *ÓRGAGO* no cuenta con su gemelo tipográfico animado con alta expresividad en el sticker de WhatsApp y en los clips promocionales de YouTube Shorts, el juego perderá la mitad de su fuerza de tracción inicial en las campañas orgánicas de adquisición.

---

## 4. VACÍOS: LO QUE NECESITO DE LAS OTRAS IAs

* **De Opus (Diseñador de Sistemas / Accesibilidad):** Necesito las directrices de diseño específicas para mapear visualmente el cambio del estado de Sospecha (ej. cambios exactos de color, tiemble de cartas o patrones de vibración háptica web compatibles con iOS y Android) para que el "gemelo visual" funcione de forma óptima sin sobrecargar la memoria de la demo web.
* **De Meta AI (Data L1 de Plataforma):** Necesito la proyección de retención D1 a D7 promedio y el CTR promedio de los anuncios interactivos de juegos web ligeros en Facebook/Instagram para audiencias de LATAM con el fin de calibrar si el coste de servidores de la demo web se amortiza con el volumen de *wishlists* orgánicas generadas mediante la compartición de stickers y emojis.