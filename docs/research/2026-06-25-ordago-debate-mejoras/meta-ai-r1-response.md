DEBATE ETAPA 2 — data L1 + red team

Voy a ser brutal: hoy el GDD apuesta todo el crecimiento a "CAC∼0 vía WhatsApp" pero no define el objeto que la gente realmente reenvía. Eso es fantasía hueca, exactamente lo que v1.1 juró matar. Mi ventaja es data de plataforma real en LATAM. Aquí está lo que cruza chats, lo que no, y cómo arreglar las 3 palancas.

PALANCA 1 — El artefacto-puente canónico (§8.3 nuevo)
Qué dice la data real, no la intuición
WhatsApp es el canal #1 en México: 12.4% del consumo de información, por encima de Facebook 11%, YouTube 10.7%, TikTok 9.4% e Instagram 9%. En Colombia, 75% de penetración empresarial y +84% crecimiento en mensajería. El chat familiar es el medio, no el feed. 
Lo que se comparte de verdad: stickers personalizados 56% y animados 52% son los más usados, con texto 36%; los predeterminados de WhatsApp solo 12%. WhatsApp 2025 empuja justo eso: emojis animados y creador de stickers animados nativo, más reacciones con stickers. 
Formato que gana alcance en Instagram: Reels obtienen entre el doble y doce veces más alcance que posts tradicionales. Carruseles logran 25.71% más alcance que imagen única. 
Cultura del reenvío hispano: el meme de Drake vs "¡Buenos días!" del family group chat (13k likes) muestra el patrón: imagen split-screen, texto en español, humor de irritación cariñosa. Los comentarios son literalmente "I'm about to send one of those to my tias" y "That's my family group chat from Jalisco". La gente no reenvía un link, reenvía una imagen que se entiende en 0.5s. 

Conclusión red team: el "código de run/build" del GDD es antipatrón D1. No cruza. Nadie abre WhatsApp para pegar un string alfanumérico que necesita explicación. La gente cruza: (1) imagen meme legible, (2) sticker animado, (3) video corto <15s con audio, (4) audio corto. Todo lo demás se ignora.

El fix de clase mundial — artefacto dual, no uno

Crear §8.3 "El artefacto-puente de ÓRDAGO" con DOS outputs generados en <2s, 1-tap, sin servidor:

A. Emoji-grid copiable (para WhatsApp grupos)

Formato: 5 líneas de texto plano con emojis nativos
Línea 1: ÓRDAGO 🪙🍷⚔🌳
Línea 2: Escobas: 🧹🧹🧹🧹🧹
Línea 3: Trampas rotas: 😈➡️🤡 x3
Línea 4: Le robé el alma a @primo por 12,450
Línea 5: Semilla de hoy: 🌵 (sin spoiler)
Por qué funciona: es como Wordle. Cabe en un mensaje, no necesita app, se lee sin abrir link, y usa el lenguaje de stickers personalizados que ya domina (56%). La mención "@primo" activa reciprocidad familiar (LD6).

B. Clip 6-8s con audio embebido (para IG Stories, Reels, WhatsApp Estados)

Contenido: barrido de Escoba + monedas saltando + el Diablo gritando "¡tramposo!" + firma sonora de 2 notas (campana grave + jarana)
Tamaño: <500KB, 720x1280, con audio SIEMPRE activado por defecto (WhatsApp Estados ahora permiten stickers y música centrada) 
Overlay texto: "le gané al Diablo de " en tipografía Posada[nombre]
Por qué funciona: Reels tienen 2-12x alcance, y el audio es el foso más barato (D3). En LATAM el clip se comparte mudo si no lo fuerzas; aquí el audio ES el chiste. 

Degradar el "código de build" a profundidad opt-in del 5% (en el Codex), nunca como output primario.

Riesgo principal: fatiga creativa. Los stickers animados se queman en 2-3 semanas en grupos familiares (data de Memetflix: "NUEVOS STICKERS DIARIO"). Mitigación: sistema de plantillas rotativas (12 variantes de clip, 20 grids) + generador procedural de texto (no manual). 

Test/kill más barato:

Prueba del puente: muestra el grid 0.5s a 20 no-jugadores hispanos. Si <70% pregunta "¿cómo se hace?" → falla. Si >30% lo reenvía sin explicación → pasa.
Prueba de spoiler: el grid no debe revelar la semilla jugable. Si alguien puede reconstruir la run desde el grid → matar y rediseñar.
K-factor por segmento: objetivo K_grafo WhatsApp >0.3 en MX, >0.2 en hispanos-USA. Si tras 1,000 shares K<0.2 → el artefacto no cruza, no gastar en marketing.
PALANCA 2 — Generador de bifurcación + foso VIVO

El GDD trata "≥2 jugadas correctas" como kill-test a posteriori. Eso es esperar magia. A1 dice: diseñas el espacio, no lo esperas.

Fix concreto en §7.3:

Regla de siembra dura: el algoritmo del Diablo DEBE dejar exactamente 2-3 conjuntos que sumen 15, cada uno con VALOR FUTURO divergente:
Opción A (tempo): captura 2 cartas bajas, deja mesa limpia para próxima Escoba
Opción B (escala): captura 4 cartas incluyendo una Mata, pero deja mesa bloqueada
Opción C (trampa): captura que activa una Trampa del Diablo
Verificable por solver en papel ANTES del playtest: en 100 tableros, ≥95% deben tener ≥2 jugadas Pareto-no-dominadas.

Instrumentación del foso VIVO (nuevo en §18):

KPI 1: Entropía de builds por cohorte semanal (Shannon entropy de combinaciones Maña + rama Jugada). Salud = estable o sube D7→D14. Si cae >15% → alarma de dominante oculta.
KPI 2: Test del experto. Mismo seed a novato vs experto. Si scores convergen <20% diferencia → no hay techo, añadir profundidad.

Riesgo: el generador hace el juego demasiado calculable. Mitigación: la Sospecha (ver P2-2) introduce ruido controlado.

Test barato: solver de papel en 1 tarde. No código.

PALANCA 3 — Reconciliar plataforma↔viralidad↔economía (§16.1)

Aquí el GDD se rompe. Promete "CAC∼0 vía WhatsApp" con un juego premium Steam $14.99-19.99. Eso es físicamente imposible: un link de WhatsApp a Steam es un paywall, no un juego.

Unit economics realistas (modelo 3 columnas):

Segmento

	

Precio bruto

	

Neto Steam (-30%)

	

Refund (10%)

	

Neto real

	

Conv wishlist→venta

	

CAC por wishlist




USA

	

$19.99

	

$13.99

	

-$1.40

	

$12.59

	

18%

	

$1.80 (Meta Ads)




Hispanos-USA

	

$17.99

	

$12.59

	

-$1.26

	

$11.33

	

15%

	

$0.90 (creators)




LATAM

	

$299 MXN (~$15)

	

$10.50

	

-$1.05

	

$9.45

	

12%

	

$0.40 (WhatsApp orgánico)

LTV/CAC objetivo ≥3. Payback <60 días. Sin estos números, no hay vertical slice.

Fix: separar loop social (retención) de loop adquisición (wishlists). El artefacto-puente NO vende el juego, vende la wishlist. El clip termina con "juega la demo gratis" no "compra ahora".

Riesgo: LATAM no convierte a $15. Mitigación: precio regional agresivo + demo web como filtro.

DECISIÓN C-1 — Mi recomendación

Híbrido, sin duda:

Steam como producto premium (credibilidad, descubrimiento, $14.99-19.99)
Demo web ligera de 1 mano (no el juego completo) como artefacto-puente jugable. Link de WhatsApp → juegas 45s contra el Diablo de tu primo → botón "añadir a wishlist"
Por qué: resuelve la contradicción sin romper el linaje Balatro. La demo web es pirateable pero es solo 1 mano, no la run. El motor viral real necesita fricción cero (B5). Steam-first mata el CAC∼0. Web-native-first mata el premium.

Trade-off: +15% scope para la demo web, -30% de comisión en ventas que vienen de demo (porque pasan por Steam igual). Vale la pena: el K-factor de WhatsApp en MX compensa.

Apuesta falsable

ÓRDAGO no llegará al #1 a menos que el artefacto-puente genere un K-factor >0.3 en grupos de WhatsApp familiares mexicanos sin pagar un centavo en ads.

No es el sistema dual, no es la Mesa viva, no es el arte. Es si tu primo reenvía el grid con "le robé el alma a Luis" y Luis responde "a ver, pásame el link". Si eso no pasa en el test de 1,000 shares, todo lo demás es optimización de un juego que nadie descubre.

¿Quieres que prototipe el emoji-grid y el clip de 6s con la firma sonora para correr la prueba del puente esta semana?

Fuentes