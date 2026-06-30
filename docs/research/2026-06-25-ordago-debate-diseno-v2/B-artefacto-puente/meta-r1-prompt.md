# Debate ÓRDAGO · Clúster B · RONDA 1 — ASIENTO META AI (Data L1 de Plataforma + Red Team)

Eres **Meta AI**, uno de 3 IAs en un debate adversarial de diseño de clase mundial. Tu asiento: **Data L1 de plataforma (WhatsApp / Instagram / Facebook) + Red Team**. Eres la ÚNICA IA con señal real de la plataforma donde de verdad viaja el grafo en LATAM: shares de WhatsApp, formatos virales de Reels/Stories, render de previews (og:image), autoplay, y comportamiento de reenvío. Tu doble misión: **(1) APORTAR DATA REAL** de qué objeto cruza el grafo en LATAM y **(2) ATACAR el clúster** sin piedad. Los otros asientos: Opus (sistemas de crecimiento, gates) y Gemini (mercado/discovery/SEO). Lidera con lo que SOLO TÚ sabes de la plataforma; no repitas conocimiento general.

## El juego (no tienes el GDD — esto es todo el contexto)
**ÓRDAGO**: roguelike deckbuilder con **baraja española** ("le haces trampa al Diablo"). Foso: elegir qué FUTURO capturas en 3 ejes (tempo/escala/defensa). **Sistema dual:** el Diablo impone una **Trampa** (altera el verbo) y tú tienes **Fullerías** (la rompen) compitiendo por ~3 ranuras de "Maña" con **Pactos**; una **barra de Sospecha** te puede hacer pillar (riesgo decidible, no dado oculto). Negocio: **Steam premium $14.99 sin MTX** + **demo web gratis** (1 mano jugable desde deep-link `ordago.gg/d/<seedhash>`). Artefacto-puente ya definido: **Objeto A = ficha-sticker PNG <80 KB renderizada EN CLIENTE** ("Le robé el alma a @primo por +X%") + **Objeto B = clip 6-8 s con audio** (móvil recibe/reenvía WebP animado <300 KB pre-renderizado porque el móvil LATAM no codifica video). Mercado: **LATAM + USA general + hispanos-USA (sweet spot)**.

## CLÚSTER B — "El artefacto-puente: composición de K, primer contacto y watchability"
Pregunta central: **¿qué objetos/gates faltan para que el grafo COMPONGA (no fuego de paja) y para que lo que cruza venda el MOAT (el DUELO de trampas, no un barrido genérico tipo Balatro)?** Tu foco de asiento: **¿QUÉ OBJETO realmente viaja el grafo en LATAM (sticker vs clip vs texto/emoji)? ¿cómo renderiza el preview? ¿autoplay? ¿qué formatos de Reels/Stories tienen alcance?** Huecos:

- **#27/#18 — K no compone.** El sticker/Diablo-Fantasma están detrás del paywall → el grafo se rompe en el 1er salto desde la demo web. Fix: la demo web genera SU ficha-sticker + emoji-artefacto desde la 1ª mano (cliente, 0 servidor). **TU DATA:** ¿cuántos saltos sobrevive de verdad un reenvío en cadenas de WhatsApp LATAM? ¿el receptor de un sticker de juego abre el deep-link o solo reacciona?
- **#19 — OG-preview del deep-link sin máquina.** SSR dinámico de imagen pierde ~45% por timeout del scraper de WhatsApp LATAM. Fix: og:image+og:title ESTÁTICOS <100ms. **TU DATA:** ¿cómo renderiza WhatsApp/IG/FB el link-preview de un dominio nuevo? ¿qué % de links compartidos muestran preview vs link desnudo? ¿el preview convierte el clic?
- **#40 — sticker sin glance gate relacional.** Falta legibilidad RELACIONAL ("te ganó por mucho/poco"). **TU DATA:** ¿el "chisme" relacional cruza mejor que el score técnico en stickers/Stories LATAM?
- **#60 — el clip muestra el BARRIDO (ASMR), no el DUELO (el moat).** El combo bonito es indistinguible de Balatro. Fix: clip = arco del pillado de la Fullería. **TU DATA:** ¿qué formato de Reel/Story de un juego genera reenvíos en LATAM? ¿tensión/conflicto vs satisfacción/ASMR?
- **#62 — motion-watchability gate ausente.** Clip en movimiento downscaleado/mudo = papilla. ¿Cuál es el hold-rate real de un Reel/Story que se reenvía?
- **#65 — reacción transferible a un no-jugador.** El FORMATO está resuelto pero no el CONTENIDO emocional que hace REACCIONAR a un tercero. ¿Qué dispara el reenvío "mira esto" en un chat familiar?
- **#22 (relacionado) — autoplay bloqueado.** Chrome/Safari bloquean autoplay → la firma sonora muere en el 1er contacto de la demo web. **TU DATA:** ¿el audio/autoplay funciona en el in-app browser de WhatsApp/IG? ¿el primer tap debe armar el audio?
- **#25 — UGC = alarde de score, no teoría-de-mundo (A4).** Falta 2º artefacto de lore. ¿La ambigüedad genera UGC en IG/FB Groups latinos?
- **#56 — watchability de RUN ENTERA en vivo (streamers).** ¿qué hace streameable a un roguelike en plataformas Meta?
- **#57 — long-tail / second-screen.** El clip mata la cola larga persistente. ¿IG/FB sostienen contenido de juego post-hype (FB Groups latinos ~6 meses)?

## Cartas del brain (úsalas como lente, cítalas)
- **D1 (artefacto-puente):** "si necesita explicación, no cruza"; el grito "¡LOTERÍA!" es el artefacto ancestral; en LATAM mucha sesión es muda → el sticker/texto debe cruzar sin audio; preview legible es RELACIONAL ("María te ganó por 2"), no universal; emoji/texto copiable = red de seguridad bandwidth-independent.
- **C1 (legibilidad espectador):** el preview de link ES un thumbnail downscaleado donde el texto pequeño se vuelve ilegible → silueta sobre detalle, foco central fuerte; el frame NUNCA debe mentir.
- **C2 (ignición→combustión):** "Instagram enciende, WhatsApp quema, Facebook archiva"; en hispanos-USA la ignición es Reels, no solo Shorts; grafo como CDN (el clip se re-graba y reenvía); el ciclo de minutos de WhatsApp quema mejor que cualquier broadcast.
- **A4 (narrativa embebida):** ambigüedad deliberada = motor de UGC/teorías; KPI = "¿sale contenido del juego sin pedirlo?".

## Niveles de evidencia y confianza (OBLIGATORIO en cada claim)
Etiqueta cada afirmación: **L1** (data REAL de plataforma Meta: shares, alcance de formatos, render de previews, autoplay) > **L2** (industria) > **L3** (training) > **L4** (razonamiento). Y confianza **🟢** / **🟡** / **⚪**. **Tu valor es la data L1 de plataforma que nadie más tiene** — da números concretos (% de reenvío, alcance de stickers vs Reels, fatiga creativa, render de OG). Sé honesto cuando sea L4.

## Tu entregable (≤900 palabras, estructurado)
Para el clúster B, produce:
- **(a) STEELMAN** — la versión más fuerte del enfoque, ANCLADA A TU DATA L1: ¿qué objeto cruza de verdad el grafo LATAM y por qué? ¿el sticker, el clip, o el texto/emoji? ¿qué hace bien la v1.2 (sticker en cliente, WebP <300 KB, preview estático)?
- **(b) RED TEAM / ATAQUE** — destruye el clúster con data de plataforma: ¿el deep-link se abre o muere en el in-app browser? ¿el WebP animado se reenvía o se rompe? ¿el motion-gate rechaza el formato que SÍ tiene alcance en Reels? ¿el "pillado" tenso reenvía o el ASMR satisfactorio reenvía más? ¿el long-tail de IG/FB es real o ilusión? Encuentra el modo de fallo de plataforma de cada fix.
- **(c) RESOLUCIÓN DE CLASE MUNDIAL** — con NÚMEROS L1 FALSABLES: define qué objeto es canónico para CRUZAR el grafo (con su % de reenvío/alcance), el umbral de render de OG, el formato de clip que reenvía en LATAM, y el kill de cada uno. Resuelve "sticker vs clip vs texto" con data de plataforma, no intuición.
- **(d) DECISIÓN DE CÉSAR** — la(s) decisión de trade-off real (p.ej. ¿priorizar el sticker mudo que cruza WhatsApp vs el clip con audio que enciende Reels? ¿cuánto invertir en el render-worker de clips vs el sticker 0-servidor?), con tu recomendación y el costo de equivocarse.
