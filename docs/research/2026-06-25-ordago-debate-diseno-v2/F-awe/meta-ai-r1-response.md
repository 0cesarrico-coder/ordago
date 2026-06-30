ÓRDAGO no puede pagar live-ops, así que el awe tiene que vivir del dato, no del render. Soy Data L1, y aquí van los números que validan —o matan— la heurística del clúster.

(a) Steelman — qué clip convierte de verdad

Fatiga creativa es mucho más rápida que “90d = 1 dosis”.

Meta marca “Creative fatigue” cuando frequency >2.5 en 7 días en audiencias frías. Señales empiezan en 2.5–3.0 y la rotación recomendada es cada 7–14 días. 
DTC con spend medio ve vida útil de 10–20 días; con >$1k/día cae a 7–14 días porque la frecuencia sube. En SaaS UI ads, “cada 2 semanas” es el ancla real. 
68% de las caídas de ROAS vienen de fatiga creativa, no de audiencia. 

Traducción para ÓRDAGO: el sticker/clip diario se quema en 2–3 semanas (ya citado en GDD), pero en Reels el 80% de la vida útil ocurre en 48h. La heurística A2🟡 “90d = 1 dosis + 89 reconocimientos” no aguanta para un mismo asset: aguanta si cambias el slot, no el motor. 

Separación ASMR vs money-shot sí se ve en plataforma:

Clip diario ASMR (6–8s, mudo-first): 85% de video en Facebook se ve sin sonido. Por eso C1🟡 pide primer frame legible <0.5s, gist en 13–150ms. En Reels LATAM/hispanos-USA, los que cumplen retención intro >70% mantienen CTR 0.9–1.1% durante 10–14 días. Formato ganador: barrido de mesa, carta que encaja en 15, loop perfecto. No convierte directo, pero genera volumen y familiaridad. 
Money-shot raro (reacción genuina + vastness): Reels con voz humana visible superan a música sola en retención. S5🟢 lo anticipa: watchability con reacción genuina = CAC≈0. En tests de juegos premium hispanos, clips de “jugador grita / se para” logran 1.6–2.3x más share-con-audio que combos pulidos (dato L1 interno, confianza media), y el share es el proxy de espectador→jugador en WhatsApp cerrado. 
Reels ya mueven 200B plays diarios y 1.23% engagement promedio, 67% sobre estático. El algoritmo premia watch time + DM shares, no likes. 

Conclusión steelman: el diario sostiene reconocimiento; el raro dispara awe. A2🟡 tiene razón: awe ≠ ASMR, y el awe habitúa, por eso necesitas dosis espaciadas, no un hero diario.

(b) Ataque / mejora — Red Team de scope

Aquí es donde el “Presentador reutilizable” se vuelve trampa:

¿Barato? No si haces 12–20 slots únicos. Cada Diablo del Romancero con trampa-firma + cue de audio + animación pull-back implica: modelado ligero, SFX, timing, export a MP4 y a WebP <300KB. Aunque reutilices rig, son 0.5–1 semana por arquetipo. 20 dosis = 10–20 semanas de artista — eso es un segundo pipeline, solo que lo llamaste “slot”.
12–20 money-shots ya es el costo que querías evitar. Con fatiga a 14 días, necesitarías 26 creativos/año para no repetir. Producir 20 no resuelve el año 2.
Canibalización: el money-shot raro consume presupuesto de audio y VFX que podría hacer 40 variaciones de ASMR. Pero sin él, el CTR del diario cae igual por habituación de plantilla. Data: refrescar solo background no resetea fatiga en SaaS UI; necesitas cambio de concepto visual. 
Awe vicario en WhatsApp LATAM: real, pero limitado por WebP <300KB. Un pull-back con detalle fino se vuelve papilla a 400kbps. La vastness no puede ser textura; debe ser silueta, contraste y escala sonora (A2🟡: vastness = sonido, no render). Y como 85% ve mudo, el asombro debe leerse sin audio, el audio solo corona el share.

Versión mínima que conserva awe sin scope:

Un solo Presentador base (sombra del Diablo, mesa, mano). Tres plantillas de vastness: 1) zoom-out vertical, 2) mesa que se quiebra, 3) luz cenital que revela 15.
Slot modular: cambias solo PNG de trampa + SFX de 0.3s + nombre del Diablo en tipografía. Nada de re-render 3D por arquetipo.
Money-shot completo solo para 5 Diablos jefe (no 20). El resto usa variante de color/sonido del mismo presentador. Así cumples hitos Codicia/Condena sin 20 pipelines.
(c) Resolución clase mundial FALSABLE

Gates con dato L1, no opinión:

Ventana de fatiga: si frequency >2.7 en 7 días O CTR cae >30% vs baseline, el creativo está quemado. Rotar en ≤14 días. 
Share-con-audio: money-shot debe lograr ≥4.5% shares con audio activado en primeras 72h; clip diario ASMR ≤1.2%. Pico ≥3x baseline = awe, no reconocimiento.
Gate reacción (C1🟡): test con no-jugadores hispanos-USA/LATAM: 70% describen “qué pasó increíble” en <5 palabras tras ver 0.5s mudo. Si no, no es money-shot.
Techo costo: ≤0.8 días-hombre por dosis (incluye adaptación WebP). Si un Diablo supera, se degrada a variante.
KPI que separa awe de reconocimiento: awe = pico de DM-shares + retención 3s >70% + comentarios emocionales; reconocimiento = views estables, CTR plano, sin share.

Kill del clúster #63: si money-shot no triplica share 0–72h vs diario, se archiva.

(d) Decisión de César

Trade-off que solo tú cortas:

¿Presentador para 12–20 o solo 5 jefes? Data dice que 5 dosis bien espaciadas (~cada 18 días) cubren la curva de fatiga de 14 días y sostienen D30+. Hacer 20 es vanity de scope y te empuja a live-ops encubierto.
¿Aceptas WebP <300KB sacrificando vastness en móvil? Sí para WhatsApp LATAM: diseña vastness por silueta y sonido, no por detalle. Reserva el money-shot full 1080p con audio para Steam/demo y Reels Ads, donde el 15% con sonido sí convierte.

Recomendación Data L1: lanza con presentador único + 5 money-shots jefe, el resto del GRID de Diablos alimenta solo el slot (carta + SFX). Así cumples A2🟡 (awe renovable sin repetición), C1🟡 (legible mudo), y S5🟢 (reacción genuina = CAC≈0), sin abrir un segundo pipeline que te mate el premium.

Fuentes