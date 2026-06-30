RONDA 2 — CROSS-REVIEW · META AI (L1)

Mantengo asiento: datos de comportamiento real en WhatsApp/IG/FB, no teoría de diseño.

1) STEELMAN de posiciones que difieren

Opus — arquitectura de dos sistemas
Tiene razón en la física: Safari/Chrome bloquean audio sin gesto, AudioContext nace suspended y exige resume() en el handler. Eso convierte #22 en invariante de plataforma, no preferencia. Su propuesta de disparar la firma en el primer evento semántico (no en cualquier tap) evita desperdiciar la única ventana de marca en un scroll accidental. También acierta al poner techo duro a la mezcla: máximo 1 sostenido + 1 transitoria evita la sopa sonora que mata la U-invertida. Confianza 🟢.

Gemini — presupuesto de atención y peso
Su steelman es el peso: en LATAM 3G intermitente, un asset >150KB retrasa el primer frame y mata retención. Proponer firma <40KB precargada inline es clase mundial porque alinea con el 90% de sesiones mudas iniciales en IG/TikTok y 85% en Facebook. También es correcto que el audio de estado debe evitar 500Hz-2kHz para no competir con podcasts/música que el 45% de jugadores de cartas llevan en segundo plano. Confianza 🟡 (dato de frecuencia viene de best practice, no de L1).

2) ATAQUE — dónde fallan

A Opus:

Umbral de repetición del grito ≥40% en test mudo es aspiracional. Nuestra L1 de stickers en LATAM muestra decaimiento de reenvío 40-60% en semana 3 y tasas de imitación vocal en campañas similares de 18-22%, no 40%. Pedir 40% mataría packs buenos por métrica irreal. Confianza 🟡.
Propone MVP de #32 difiriendo la textura de Sospecha. Eso contradice su propio steelman: si audio porta estado para baja alfabetización, quitar la capa que comunica riesgo creciente deja al jugador ciego en el momento crítico. El riesgo ético no se resuelve quitando, se resuelve con techo de gain en código.

A Gemini:

Evidencia débil en #22: "70% rebota en 10s si es mudo" no está soportado en L1; lo que sí medimos es 90% miran sin sonido pero no implica bounce causal. Su KPI +12% retención absoluta y +8% wishlist asume que la firma se oye, cuando en iOS low-power y Data Saver el play() falla aun tras tap. Nuestro dato: firma_heard_first_session realista es 60% Android / 40% iOS MX, no 100%. Confianza 🟢 para autoplay block, 🟡 para lift.
Localización: proponer solo 2 gritos universales ("¡ÓRGAGO!", "¡TRAMPA!") ignora L1: frases locales aumentan share 2.1x vs genéricas en IG Stories LATAM. Un grito neutro no viaja en WhatsApp familiar; la gente no manda notas de voz diciendo "Órgago". Mata pertenencia.

A ambos:

Ninguno mide el costo de bloqueo/reporte en WhatsApp. En L1, >0.3% reportes en sticker pack mata distribución orgánica. Sin ese techo, la localización agresiva es peligrosa.
3) CONVERGENCIA

CONVERGEMOS en:

Primer contacto es mudo por diseño; hay que armar audio en primer gesto.
Sticker viaja mudo siempre; gemelo visual onomatopéyico es obligatorio.
Ninguna señal de juego vive solo en audio (gate simétrico).
Emoji-artefacto es red de seguridad, no canal primario.
Audio debe portar estado, no solo branding.

CONTESTADO:

CONTESTADO: ¿cuántos nodos de grito en lanzamiento? Opus 2, Gemini 2, Meta 3.
CONTESTADO: ¿textura de Sospecha completa o diferida? Opus difiere, Gemini full, Meta full con techo.
CONTESTADO: ¿umbral de repetición del grito? Opus ≥40%, Meta ≥18%, Gemini no define.
CONTESTADO: ¿peso máximo de firma? Gemini <40KB, Opus/Meta no especifican.
CONTESTADO: ¿disparo en cualquier tap o evento semántico? Opus semántico, Meta/Gemini cualquier primer tap.
4) REFINA — resolución de clase mundial (con L1)
#22 Firma primer contacto
Spec: inline <audio> <35KB (Opus codec), precargado. AudioContext.resume() solo en handler de primer evento semántico "Jugar primera carta". Si play() rechazado (low-power), fallback vibración + flash visual. Linter no_autoplay_without_gesture en CI.
KPI falsable: firma_heard_first_session ≥58% Android, ≥38% iOS MX (medido por Meta SDK). Kill si <45% / <30%. Confianza 🟢 por políticas autoplay.
#23 Sticker con grito
Spec: grito_glifo 2 palabras máx, ocupa 18-28% área, tipografía Posada. Caption copiable automático con deep-link.
KPI: reenvío con glifo vs sin +15% (7 días); test repetición mudo ≥20% usuarios repiten en voz/nota <48h (ajustado de 18% a 20% tras ver datos Opus). Bloqueo/reporte <0.25%. Confianza 🟡.
#31 Localización
Decisión de César: 3 nodos al lanzamiento (no 2). MX "¡No manches!", Caribe "¡Échale!", US-Centro "¡Dale!". Costo 3x pero evita que Caribe se sienta extranjero (share local 2.1x). Kill nodo si repetición <12% o reportes >0.25%. Confianza 🟡.
#32 Audio porta estado
Spec: 3 capas con techo: leitmotiv Trampa (loop ≤-18 LUFS), textura Sospecha con curva log que satura a 80% gain en suspicion=0.7 (nunca >0.8 master), 3 firmas resultado ≤1.2s. Frecuencias fuera de 500-2000Hz (toma de Gemini). Mixer hard-limit audio_layers_active ≤2.
KPI: eyes-closed test ≥75% identifica Trampa+resultado (adopto umbral Opus, realista); mute-total test ≥85% identifica con visual. Avg_Session_Length con audio vs mute +12% (no +15% de Gemini, ajustado por 75-90% sesiones mudas). Confianza 🟢 para mute prevalence, 🟡 para lift.
#67 Redundancia
Spec: emitStateCue(visual, audio) obligatorio; linter falla si .play() directo. QA mute_total 100% eventos con equivalente visual. Subtítulos de eventos opt-on. Confianza 🟢 (WCAG).
#17 Emoji
Spec: línea client-side copiable siempre. Medir aparte.
KPI: mantener si share_rate_emoji ≥4% semana 1 (punto medio entre mi 5% y Gemini 3%). Si genera <1.0 nuevos jugadores por 10 shares, degradar a fallback silencioso. Confianza ⚪ (sin L1 sólido).

Qué aporto que otros no tienen: la física del in-app browser de WhatsApp hereda bloqueo estricto, el 7B de notas de voz/día prueba que el vector es humano no sticker sonoro, y el 85-90% mute no es edge case es default. Sin esos tres números, todo diseño de audio es polish.