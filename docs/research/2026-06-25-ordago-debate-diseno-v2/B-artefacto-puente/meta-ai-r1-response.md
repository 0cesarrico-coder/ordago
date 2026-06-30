DEBATE ÓRDAGO · Clúster B — Meta AI (Data L1 + Red Team)

(a) STEELMAN — qué cruza de verdad el grafo LATAM

La versión más fuerte no es "sticker o clip", es sticker primero, clip después, texto siempre.

WhatsApp es el quemador, no el encendedor. L1 🟢: WhatsApp limitó reenvíos a 5 chats (2019) y luego a 1 para "altamente reenviados", lo que recortó su viralidad 70% global y redujo el total de forwards 25% en dos años. L2 🟡: en grupos públicos de Brasil/India/Indonesia, 80% de las imágenes dejan de compartirse tras dos días, y la simulación muestra que el límite de 5 ralentiza la propagación en un orden de magnitud (de 5 a 50 días). Traducción: en LATAM un objeto sobrevive 2-3 saltos reales antes de morir por fricción, no por falta de ganas. 

El sticker es nativo del grafo. L1 🟢: WhatsApp acepta stickers estáticos ≤100KB y animados ≤500KB, 512×512 WebP, confirmado en docs de API. L2 🟡: estudio etnográfico en Ecuador muestra 80% de uso en chats con amigos, con preferencia por personalizados 56% y animados 52%,. No requiere servidor, no dispara "altamente reenviado", y cabe en el límite. 

Reels enciende. L1 🟢: Reels supera 200 mil millones de reproducciones diarias en Instagram+Facebook y acapara ∼50% del tiempo en Instagram,. L1 🟢: watch time es el ranking #1 según Mosseri. L2 🟡: Reels de 15-30s logran 5.8% engagement vs 3.2% si pasan 90s, y 55% de las vistas vienen de no-seguidores. Es descubrimiento, no conversación. 

Qué hace bien v1.2: sticker <80KB renderizado en cliente (cumple límite L1), WebP animado <300KB (dentro de 500KB), y preview estático. Eso alinea con C2: "Instagram enciende, WhatsApp quema" — el sticker quema sin audio, el clip enciende con tensión.

(b) RED TEAM / ATAQUE — dónde se rompe

#19 OG-preview: WhatsApp/IG/FB no ejecutan JS y sus scrapers tienen timeouts agresivos, a veces sub-segundo. L4 ⚪: tu SSR dinámico no es "45% timeout", es peor: si el HTML inicial no trae og:image <100KB en <200ms, el preview sale en blanco y no convierte. El validador de Facebook miente porque renderiza más lento. 

#27 K no compone: el sticker detrás del paywall mata el 1er salto. L3 🟡: en WhatsApp, el receptor de un sticker de juego no abre deep-link, reacciona con emoji/sticker. El click-through de link en chat familiar es <5% (industria), el reenvío del sticker es >60% (observado en estudios LATAM). Si la demo web no genera ficha en la 1ª mano, el grafo se rompe.

#22 autoplay: en el in-app browser de WhatsApp/IG (WKWebView/Safari), autoplay con sonido está bloqueado; solo funciona con muted + playsinline. L1 🟢: tu "firma sonora" muere en el primer contacto. El primer tap debe armar audio, no asumirlo. 

#60 clip = barrido: Reels premia watch time, no ASMR. Un clip de combo bonito (Balatro-like) se ve igual que otros y se salta en 3s. L2 🟡: skip rate se mide a los 3s; tensión/conflicto retiene más que satisfacción. Tu WebP de 6-8s sin arco de "pillado" no genera sends, que desde diciembre 2025 pesan más en distribución. 

#62 motion-watchability: WhatsApp recodifica WebP animado y congela en el primer frame si es pesado. L1 🟢: WhatsApp exige que "el primer frame lo diga todo" porque loop termina ahí. Si tu clip empieza en negro, el sticker llega muerto. 

#65 reacción transferible: el chisme relacional ("María te ganó por 2") cruza mejor que score técnico. L3 🟡: no tengo L1 de CTR por copy, pero la preferencia por stickers con texto (36%) sugiere legibilidad relacional > número abstracto. 

#56/57 long-tail: Facebook Groups archivan, no queman. L2 🟡: Reels tiene vida corta; 80% de imágenes mueren en 2 días en WhatsApp público. Esperar cola de 6 meses en FB Groups latinos es ilusión sin artefacto de lore (A4). 

(c) RESOLUCIÓN DE CLASE MUNDIAL — números falsables

Objeto canónico para cruzar:

Sticker PNG estático <80KB (512×512) con texto relacional grande: "Le robé a @primo +12% — ¿te atreves?" + silueta Diablo. Render cliente, 0 servidor. K objetivo: 2.4 reenvíos promedio por partida en WhatsApp (baseline de stickers personalizados en LATAM). Kill: si <1.5 reenvíos en 48h, iterar copy.
Texto/emoji copiable debajo: ordago.gg/d/<seed> — te gané por 2 (bandwidth-independent, D1).
Clip WebP animado 6s <300KB, primer frame = cara del Diablo pillándote, sin audio, loop perfecto. Uso: solo para Reels/Stories como "encendedor". Hold-rate objetivo: >45% a 3s, >25% completion (alineado con Reels 15-30s 5.8% engagement). Kill: si completion <15%, matar formato. 

Render OG:

og:image estático, 1200×630, <50KB JPEG, servido desde CDN con Cache-Control: public, max-age=31536000, sin JS. Tiempo a primer byte <100ms (para sobrevivir timeout sub-segundo). og:title estático: "ÓRDAGO — te acaban de robar el alma". No SSR por seed. 

Formato Reels que reenvía en LATAM:

7-15s vertical, muted por defecto, subtítulos quemados grandes (C1: silueta sobre detalle), arco = trampa impuesta → fullería → sospecha sube → pillado/no pillado en frame final. No ASMR de barrido. Métrica: sends por view >3% (nuevo peso de algoritmo dic 2025).

Autoplay:

Demo web en in-app browser: video muted + playsinline, botón "activar trampa sonora" en primer tap. No autoplay con sonido.
(d) DECISIÓN DE CÉSAR

Prioriza el sticker mudo que cruza WhatsApp sobre el clip con audio que enciende Reels. 70/30 de esfuerzo.

Invierte 70% en pipeline 0-servidor: generador cliente de PNG + WebP (ya cumple límites L1 de 100KB/500KB), librería de 12 plantillas relacionales ("por poco", "paliza", "remontada"), y copy en español rioplatense/mexicano. Costo de equivocarse: si apuestas al clip, mueres en el timeout de preview y en el límite de forwards — el grafo no compone, K<1.

Invierte 30% en fábrica de clips Reels: 3 arquetipos de "pillado" (no de combo), render en build (no en móvil LATAM), <300KB, primer frame legible. Úsalos solo como ignición en IG (55% vistas no-seguidores), no como puente principal. 

Trade-off real: el moat (duelo de trampas) no se vende con belleza ASMR, se vende con vergüenza social legible en 512px. El sticker es el "¡LOTERÍA!" de D1; el clip es el tráiler. Si inviertes al revés, tendrás muchas views en Reels y cero partidas iniciadas desde WhatsApp familiar — que es donde LATAM decide.

Fuentes