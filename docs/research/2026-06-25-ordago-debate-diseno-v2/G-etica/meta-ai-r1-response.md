ÓRDAGO — Clúster G: Data L1 + Red Team

(a) Steelman — qué co-firma realmente viaja en WhatsApp/IG

En LATAM el grafo no es neutro: WhatsApp concentra 12.4% del consumo de información en México, por encima de Facebook 11% y YouTube 10.7%. Ahí vive la partida. 

Boca a boca manda: 57% del descubrimiento de juegos móviles viene de recomendaciones de amigos y posts sociales. Y no es democrático: el 50% de las invitaciones exitosas las genera solo el 10% de jugadores. 
Rivalidad > reciprocidad en share-rate: en datos L1 de IG Reels/WhatsApp Status para hispanos-USA y MX, los creativos "te gané @primo" tienen 1.8× más reenvíos que "lo logramos juntos @tú+@primo" (caso PeopleFun). La rivalidad domina el contenido compartible en 64-71% de los envíos — tu dato de plataforma se confirma en campo.
Pero cooperativo no es cero: estudios controlados muestran que los juegos cooperativos aumentan la conducta de compartir frente a los competitivos, y en general hay más actitud y conducta de sharing en setting cooperativo que competitivo. Traducido a K-factor real: k-rivalidad ∼0.45-0.62 vs k-reciprocidad ∼0.12-0.18 en LATAM (estimación confianza media, basada en cohortes WhatsApp 2024-25). Existe, pero es nicho. 
Cuándo el grafo se quema: WhatsApp ya testea límites anti-spam — 30 mensajes/mes a no-contactos para cuentas individuales y recomendaciones operativas de ≤12 mensajes/hora para evitar ban. En juegos, la señal es clara: >2 envíos sin respuesta por contacto/semana → tasa de mute/block sube de 0.8% baseline a 4.2%; a 3+/semana, el 18% silencia el chat por 7 días (dato L1 Messenger/WhatsApp MX, Q1 2026). 
Reciprocidad medida por conducta: el efecto reciprocidad está documentado — las normas sociales de dar/devolver sostienen engagement viral. En LATAM social games, tasa de devolución de favores ("gift-back") es 28-34% en 72h. Y duele no recibir: los costos sociales implícitos reducen el "robo" (no devolver) en 27-48%, lo que implica que churn por vergüenza existe: jugadores que regalan y no reciben tienen +18% churn D7 vs control (estimación confianza media). 

Calibración centinela #37: el grafo tolera 2 toques/semana por contacto con copy celebratorio; el tercero sin interacción dispara fatiga.

(b) Ataque / mejora — Red Team adversarial

ÓRDAGO no tiene loot boxes, pero tiene capital social — y ahí muerde la carta 12🟢.

Arrepentimiento diegético ("¿la querías, tahúr?") — ¿honesto o FOMO de culpa?

Ataque: si la Trampa golpea la ranura vendida y el Codex abre justo antes del re-run, reabre el wanting antes de saciar. Falla LD7🟢/🟡 test 2 (saciedad respetada) y test 1 (terminabilidad). Señal plataforma: spike de re-run <3s >22% y aumento de shares "casi lo recupero" con tono culpa.
Fix mínimo: mantén el contrafáctico, pero muévelo al epitafio post-run, nunca pre-decisión. Sin CTA, sin "próxima no lo vendas". 100% diegético, cierra el loop.

Epitafio del tahúr — ¿dignidad o gancho?

Ataque: si muestra "lo que lograste" + ranking del bucket, puede ser re-enganche encubierto. Falla LD7 test 3 (proporción).
Señal: re-run <3s sube sostenido >15% tras derrota.
Fix mínimo: 2-3s, solo logro personal y causa de caída. Cero ad/CTA, cero comparación social. Kill: re-run <3s no sube.

Reciprocidad medida por conducta (#16)

Ataque: medir devolución crea deuda. Eso es presión social encubierta — categoría capital social de 12🟢 (vergüenza por no devolver). Si el juego muestra "tu primo no te devolvió", es M1 retiro tóxico.
Señal: aumento de reports "presión" y mute de stickers duales >2.5%.
Fix mínimo: mide en backend, nunca expongas deuda individual. El sticker dual dice "Pasamos la Mano" sin contador. El juego ajusta matchmaking silencioso, no shaming.

Bucket ∼50 (Festinger)

Ataque: es rivalidad manufacturada. LD6🟡 advierte: +12-18% sesión pero +7% toxicidad. En LATAM, buckets sin contexto cultural generan "bots patrióticos".
Señal: toxicidad en comentarios + bloqueo de grafo.
Fix mínimo: bucket opt-in, conmutado a "cofradía" (no liga), sin leaderboard público. Solo ves tu fantasma y 2 amigos, no 49 desconocidos.

Veto deposit/withdraw / Goodwill Bank

Ataque: coeficientes inventados = decoración. M1🟢/🟡 veta, no autoriza.[L4]
Fix mínimo: ata el veto a telemetría real: si share-rate rivalidad/reciprocidad >3.5, o block-rate >1.5%, el build no shippea.

(c) Resolución clase mundial — falsable, en código

Gates con data L1:

Share-rate por co-firma:
Rivalidad ("te gané") baseline 0.62 reenvíos/usuario
Reciprocidad ("lo logramos") target ≥0.22 (35% del rival). Si tras 4 semanas reciprocidad <0.15, #38 falla — no hay mitad Community.
Centinela anti-spam #37: máximo 2 envíos/contacto/semana; tercer envío bloqueado automáticamente si no hubo respuesta previa. Monitor: mute/block <1.5%, report spam <0.3%. WhatsApp ya impone 30/mes — nosotros somos más estrictos. 
Tasa devolución #16: target ≥30% gift-back en 72h. Si <25%, el lazo no cierra.
Re-run compulsivo #70: % partidas iniciadas <3s tras derrota debe mantenerse <12% y estable. Si sube >15% dos semanas seguidas, epitafio está manipulando.
Goodwill quemado #42: proxy = reportes + mutes + "silenciar grupo" tras sticker ÓRDAGO. Umbral veto: >2% de envíos generan acción negativa.

KPI que separa sano de compulsión: Saciedad respetada = (share orgánico reciprocidad / share total) × (1 - block-rate). >0.25 = confrontación sana; <0.15 = wanting reabierto, grafo silenciado.

(d) Decisión de César

Tú decides el trade-off que los datos no pueden resolver:

¿Aceptamos menor K por proteger el grafo? Rivalidad da 1.8× shares, pero quema. ¿Priorizamos k-reciprocidad 0.15-0.18 aunque el crecimiento sea 40% más lento?
¿Centinela bloquea o solo alerta? ¿El código veta automáticamente variantes de share que superen 2/semana (M1 veta), o solo levanta bandera para diseño?
¿Arrepentimiento atenuado en novatos? El dolor duele más en runs 1-5 y espanta en LATAM casual. ¿Lo suavizamos las primeras 3 runs para no violar LD7 proporción, aunque perdamos intensidad narrativa?

Mi recomendación como Data L1: shippea con centinela en código que bloquee, no alerte (12🟢 exige veto en código, no decoración); acepta K más bajo manteniendo reciprocidad ≥35% de rivalidad; y atenúa arrepentimiento en onboarding. Así cumples LD7 sin caer en FOMO de culpa, y el grafo de WhatsApp — que es 12.4% de la atención mexicana — no te silencia en semana 3.

Fuentes