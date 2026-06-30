# CLÚSTER D — Audio como sistema de orden superior · RONDA 2

Mantengo mi asiento como **OPUS (Diseño de Sistemas y Accesibilidad)**.

---

## 1. STEELMAN DE LAS POSICIONES DIFERENTES

*   **Gemini (Optimización y Frecuencias):** Su enfoque en el presupuesto de assets ($<$40KB inline/Web Audio API, 🟢) para mitigar la latencia 3G/4G en LATAM es brillante. Asimismo, su propuesta de blindar el estado de Sospecha fuera del rango de la voz humana (500 Hz–2 kHz, 🟢) es brillante: permite al jugador escuchar música/podcasts en segundo plano (comportamiento en el 45% de jugadores de cartas) sin enmascaramiento de frecuencias.
*   **Meta AI (Data de Plataforma L1):** Su validación de que el 85-90% de las sesiones en feed son mudas (🟢) y que el modo de bajo consumo en iOS bloquea el `play()` aun tras un tap (🟢) aterriza el diseño a tierra. Su dato de que el 23% de las sesiones de WhatsApp en LATAM ocurren con datos agotados (🟢) justifica plenamente el emoji-artefacto (#17) como red de seguridad crítica.

---

## 2. ATAQUE

*   **A la "Metadata" de WhatsApp de Gemini (#23):** Gemini sugiere usar "*metadatos asociados o links cortos en la descripción del pack*". **Error técnico grave de plataforma:** WhatsApp sanitiza la metadata de los stickers `.webp` al ser reenviados; no existe el "sticker con enlace clickable nativo". El sticker viaja desnudo. Depender de la descripción del pack destruye la conversión.
*   **A la agrupación cultural de Gemini (#31):** Agrupar España y el Cono Sur en un solo "Nodo Sur" es un sinsentido cultural. El "¡Órdago!" (origen vasco/español) tiene un tempo, tono e intención diametralmente opuestos al "¡Truco!" rioplatense. Mezclarlos destruye el pilar de pertenencia (Ética 12).
*   **Al "Botón de Desbloqueo" de Meta AI (#22):** Meta AI propone una pantalla inicial con un botón gigante: *"Toca para escuchar al Diablo"*. **Fallo de UX/Inmersión:** Esto rompe la estética de misterio del juego de cartas (Curva U-invertida #09). Es sobre-ingeniería intrusiva. El audio se debe armar de manera *invisible* durante la primera acción natural del core-loop (vgr. al robar la primera carta o interactuar con el menú inicial).
*   **A la omisión geográfica de Meta AI (#31):** Meta AI propone tres nodos: MX, Caribe y "US-Centroamericano". **Punto ciego masivo:** Excluir al Cono Sur (Argentina/Uruguay) es un error de diseño fatal. Esa región es el hogar del *Truco*, el ancestro mecánico directo de *ÓRDAGO*. Su exclusión aliena al target de conversión orgánica más natural de LATAM.

---

## 3. CONVERGENCIA

*   **CONTESTADO:** **Mute por defecto.** El 85-90% de los usuarios de móvil juegan en silencio absoluto (Meta AI, 🟢). El juego debe ser 100% jugable en modo mudo sin perder información de estado.
*   **CONTESTADO:** **Stickers mudos y cortos.** No existen los stickers con sonido en WhatsApp. El grito es puramente visual, con tipografía expresiva y limitado a $\le$20 caracteres (Meta AI, 🟢) para evitar el recorte de preview en pantalla pequeña.
*   **CONTESTADO:** **Presupuesto de carga ultra-bajo.** La firma sonora inicial no superará los 40KB (Gemini, 🟢) para evitar latencia de feedback en conexiones móviles inestables.
*   **CONTESTADO:** **Ancho de banda cero.** El emoji-artefacto (#17) es obligatorio como fallback sin consumo de datos (Meta AI, 🟢).

---

## 4. RESOLUCIÓN DE CLASE MUNDIAL REFINADA

### #22 — Firma silenciosa armada por UX natural
La firma de identidad (3 s) se carga inline ($<$40KB, Web Audio API). Se prohíben pantallas de carga o modales intrusivos.
*   **Métrica falsable:** Invariante en código: linter `stealth_audio_arming` exige que el primer input interactivo del juego (`pointerdown` en el botón "Jugar" o "Desafiar") invoque `AudioContext.resume()`.
*   **KPI:** `Firma_Heard_First_Session` $\ge$ 70% de las cargas en WebView móvil. Si en el frame de interacción el `AudioContext.state` sigue `suspended` (bajo consumo de iOS), el motor visual activa una vibración háptica alternativa como fallback.

### #23 — El sticker visual auto-descriptivo
El sticker no lleva links ni metadata invisible. El grito se integra en el arte del sticker (glifo tipográfico) limitado a $\le$2 palabras y $\le$15 caracteres legibles en grids de $3x3$.
*   **Métrica falsable:** Linter de assets `sticker_text_constraints` valida que el glifo ocupe entre el 15% y el 30% del canvas del sticker y que el contraste tipográfico (WCAG 2.1 AA) sea $\ge$ 4.5:1.

### #31 — Localización cultural de dos nodos de alta afinidad
Se reduce el alcance de lanzamiento a exactamente **dos variantes culturales** que concentran el 80% de la conversión potencial:
1.  **grito.mx (Nodo Norte/MX):** "¡Órdago, cabrón!" / "¡Te doblo!"
2.  **grito.ar (Nodo Sur/Rioplatense):** "¡Quiero retruco!" / "¡Órdago, che!"
*   **KPI:** Tasa de reenvío de stickers específicos por región $\ge$ 15% en el primer mes de EA.

### #32 — Estado dual de Sospecha por bandas de frecuencia
El audio de estado (Sospecha) se diseña para convivir con la multitarea auditiva del usuario. Se implementa un filtro Notch permanente en la banda de 500 Hz a 2 kHz para el bucle de Sospecha.
```
  0 Hz ─── [Graves Tensos / Sub-graves] ─── 500 Hz ─── [ Notch Filter (Voz/Música) ] ─── 2 kHz ─── [ Textura Aguda / Roce metálico ]
```
*   **Métrica falsable (Gate de Release - Eyes Closed Test):** Con pantalla apagada y música externa sonando a 70 dB, $n \ge 15$ testers deben identificar el nivel de Sospecha (Bajo/Medio/Crítico) mediante el audio del juego con un $\ge$ 80% de precisión.

### #67 — Redundancia simétrica estructural (Mute-Play)
*   **Métrica de código:** El motor de audio se acopla mediante el wrapper `emitGameplayEvent(VisualPayload, AudioPayload)`. Si `VisualPayload` es `null`, el compilador lanza un error (`NoBareAudioEventError`).
*   **QA Automatizado:** Un test unitario corre el core-loop con `volume = 0` y simula inputs; si un cambio de estado de Sospecha no genera una mutación en el DOM/Canvas en el mismo frame, el build falla.

---

### DECISIÓN DE CÉSAR (Formulación Binaria)

1.  **Nodos de lanzamiento:** ¿Se lanza con un único grito genérico/teatral para optimizar costos de QA, o se asume el costo de desarrollo de los **dos nodos clave** (MX y AR)? 
    *   *Recomendación de Opus:* **Dos nodos (MX y AR).** El mercado de cartas en Argentina es el foso orgánico del juego; ignorarlo en el lanzamiento destruye el boca a boca más valioso.
2.  **Emoji-artefacto (#17):** ¿Se automatiza como una UI copiable dentro de la demo, o se mantiene solo como una cadena estática en el clipboard?
    *   *Recomendación de Opus:* **UI copiable dinámica.** Generar la representación visual exacta de la mano perdedora/ganadora en emojis genera un engagement de Wordle sin costo de ancho de banda.