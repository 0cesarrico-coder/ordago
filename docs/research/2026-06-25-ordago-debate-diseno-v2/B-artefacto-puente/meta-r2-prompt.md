# RONDA 2 — CROSS-REVIEW · Clúster B — Artefacto-puente: composición de K, primer contacto, watchability · ÓRDAGO

Mantén tu ASIENTO de la Ronda 1. Abajo están las TRES posiciones de Ronda 1 (la tuya + las otras dos IAs). Tu tarea:
1. **STEELMAN** de las posiciones que difieren de la tuya antes de atacarlas.
2. **ATAQUE**: errores, evidencia débil, o fixes que empeoran feel/economía/legibilidad. Específico (cita a quién).
3. **CONVERGENCIA**: di en qué CONVERGES y qué queda CONTESTADO (lista). Marca cada punto sin acuerdo con el prefijo "CONTESTADO:".
4. **REFINA** tu resolución de clase mundial: números/criterios falsables concretos, qué es decisión de César.
Usa niveles de evidencia L1-L4 y confianza 🟢/🟡/⚪. Sé conciso pero denso (≤900 palabras).

============================================================

----- POSICIÓN R1 · OPUS (Diseño/Sistemas) -----
# Clúster B · Ronda 1 — ASIENTO OPUS (Diseñador de Sistemas de Crecimiento)

> Lente: K compone solo si el nodo NUEVO genera su propio output reinvertible (C2). Mi trabajo: que el grafo sea **crecimiento compuesto** y no fuego de paja, y blindar cada promesa con un **gate falsable barato** que la mate antes de un píxel. Evidencia etiquetada L1–L4 / 🟢🟡⚪.

---

## (a) STEELMAN — por qué la composición de K + gates falsables son el delta correcto

La v1.2 hizo lo difícil bien: definió un **artefacto-puente atómico** (A=PNG <80KB, B=clip 6-8s) y entendió que con B2P sin MTX **LTV≈1 venta**, así que el grafo no es marketing — es el **único** camino a LTV/CAC≥3. Eso es razonamiento de clase mundial: ata la supervivencia financiera a un invariante de producto, no a un presupuesto de UA. **L4 🟢** (la aritmética B2P es deductiva).

El delta que falta es **la diferencia entre K lineal y K compuesto**. Un loop donde solo los dueños de Steam generan artefactos tiene K efectivo acotado por la base pagada: cada invitado es una hoja muerta. La corrección #27 (la **demo web genera SU sticker desde la 1ª mano, cliente, 0 servidor**) es exactamente el invariante de C2: el nodo nuevo —que ni pagó— produce output reinvertible. Eso convierte un árbol de profundidad 1 en uno de profundidad N. **Es el fix más importante del clúster y todo lo demás es residual frente a él.** **L2 🟢** (Chen: viral SIN nodo-que-reinvierte = lineal).

Y los gates falsables son correctos porque **un gate que se corre en 100×100px gris cuesta centavos y mata una promesa que costaría semanas de arte**. El glance-gate (#40), el motion-gate (#62), el reaction-gate (#65) y el first-frame-gate del DUELO (#60) son todos la misma familia: *"si el artefacto no comunica el MOAT a un downscale mudo, no se exporta"*. Eso es el principio C1 ("el frame nunca debe mentir") promovido de checklist de arte a **gate de build**. **L2 🟢**.

---

## (b) ATAQUE / MEJORA — dónde mis propios fixes se auto-engañan

1. **"K de 2ª generación" es un vanity metric esperando nacer.** Si lo defino como "shares originados en nodos no-Steam", lo inflo trivialmente: un usuario demo que comparte 5 veces a chats muertos marca K2 alto con cero invitados nuevos jugando. **El modo de fallo es medir SHARES en vez de ACTIVACIONES.** K2 honesto = *invitado-de-demo que a su vez genera una 1ª-mano nueva atribuible*. Sin esa atribución encadenada, K2 miente. **L4 🟡**.

2. **El "naipe del Romancero" (#25) añade scope con retorno diferido y no falsable a tiempo.** Su KPI (lore_share D30–D60) llega *después* del launch — no protege la decisión de construirlo ahora. Riesgo real: gastar arte/sistema en un 2º artefacto mientras el sticker competitivo (el que SÍ mueve CAC en semana 1) está sin pulir. **Es residual, no de ignición.**

3. **El motion-gate (#62) puede rechazar clips que SÍ convierten.** Un juez que exige "nombrar qué pasó en 3s a 360p mudo" sesga hacia clips *legibles* y mata clips *emocionalmente virales pero caóticos* (el caos a veces ES el hook). Modo de fallo: optimizo claridad y pierdo sorpresa. El gate debe ser **piso de legibilidad del MOAT, no techo de complejidad**.

4. **El og:image estático (#19) pierde el chisme dinámico.** Estático <100ms cachea por seedhash — pero el gancho relacional ("María te ganó por 2") es *por-partida*, no por-seed. Si lo congelo por seed pierdo el "por 2". Modo de fallo: velocidad a costa del gancho que convierte.

---

## (c) RESOLUCIÓN DE CLASE MUNDIAL — objeto, métrica, verde, KILL

**Set mínimo de gates que un build NO pasa sin cumplir (los 4 de ignición):**

| # | Objeto/Gate | Métrica | VERDE | KILL |
|---|---|---|---|---|
| **G1 (#27)** composición | demo web genera sticker+emoji 1ª mano, cliente | **K2-activación** = invitados-de-demo que generan 1ª-mano nueva / nodos-demo | ≥0.35 | <0.15 → loop lineal, rehacer ignición |
| **G2 (#19)** OG | og:image+title estático por seedhash, CDN | latencia entrega scraper | <100ms p95 entrega; <300ms p95 generación post-mano | scraper no recibe <100ms → preview muerto |
| **G3 (#40)** glance relacional | RunDigest→sticker a 100×100px gris | % lee el chisme relacional ("por mucho/poco") | ≥90% (n≥20) | <90% → rehacer silueta |
| **G4 (#60)** first-frame DUELO | clip canónico = arco del pillado | % lee "le hace trampa al Diablo" sin audio, 1er frame | ≥80% | <80% → re-encuadrar clip |

**Resolver "medir K2 sin instrumentación que mienta" (el problema duro):**
La trampa es servidor. La solución es **atribución por deep-link encadenado, 0 backend de identidad**: cada sticker/clip lleva el `seedhash` + un **token de generación local** (nonce en el PNG/URL). Cuando un invitado abre `ordago.gg/d/<seed>?ref=<nonce>` y **completa su 1ª mano**, su cliente emite SU nonce hijo y un único beacon `{ref_padre, nonce_hijo, completó_mano:true}`. **K2 solo cuenta aristas con `completó_mano=true`** — no shares, no aperturas. Esto es 1 endpoint de telemetría stateless (no identidad, no cuentas), barato, y **no puede inflarse compartiendo a chats muertos** porque exige una mano jugada río abajo. **L4 🟡** (diseño; falta validar tasa de beacon-loss en WhatsApp LATAM — pedir L1 a Meta AI).

**Arreglo del og dinámico (G2):** dos capas. Capa-seed estática (instantánea, cacheada) como *fallback* + capa-partida que se hornea **al terminar la mano** (<300ms, cliente sube PNG a CDN keyed por nonce). El scraper que llega tarde recibe el genérico-de-seed (vivo); el que llega a tiempo recibe el chisme "por 2". **Nunca bloquea el preview por esperar el dato dinámico.**

**Arreglo del motion-gate (G3'→residual, NO de ignición):** el gate es **piso**: juez solo debe nombrar *"¿hubo trampa? ¿quién gana?"* (el MOAT), **no** "describe todo". Clips caóticos pasan si el MOAT es legible. Umbral: ≥70% nombra trampa+ganador a 360p mudo 3s. Esto evita rechazar virales caóticos.

**Prioridad de construcción:**
1. **PRIMERO G1** (composición cliente-side) — sin esto el grafo no compone y nada más importa.
2. **G2 + G3 + G4** (primer contacto + legibilidad del MOAT) — son el "el artefacto vende el DUELO, no un barrido genérico".
3. **Residual** (post-ignición verde): #56 momento-clip-como-invariante-de-run, #57 SEO/Search Velocity, #65 reaction-gate, #25 Romancero. Todos valiosos para *perdurabilidad*, ninguno bloquea el launch.

**Invariante de run (#56), barato:** "una run no termina sin ≥1 momento transmisible (telemetría detecta pico tensión-resuelta)". KPI clips/hora-stream ≥1 en 30min. KILL: 30min sin pico → el loop no produce watchability, revisar densidad de Trampas/Fullerías. Esto **sí** lo construiría temprano si el costo es solo telemetría (reusa el detector de pico del exportador).

---

## (d) DECISIÓN DE CÉSAR

**Decisión 1 — ¿Cuánto backend para K2 en demo web?**
Recomiendo: **1 endpoint stateless de beacon (sin cuentas, sin identidad)**, no más. Construir G1 client-side + atribución por nonce encadenado con `completó_mano=true`. **Costo de equivocarse alto en ambos lados:** sin atribución → no sabes si el grafo compone y vuelas a ciegas el único KPI que decide LTV/CAC; con backend de identidad completo → scope creep que retrasa launch y traiciona el espíritu "0 servidor". El nonce-beacon es el mínimo que no miente. **Recomendación firme.**

**Decisión 2 — ¿Romancero (lore) ahora o después?**
Recomiendo: **después.** Es residual; su KPI no es falsable pre-launch y compite por arte con el sticker competitivo que mueve CAC en semana 1. Costo de equivocarse si lo cortas: pierdes algo de UGC-de-teoría D30–D60 (perdurabilidad), recuperable en parche. Costo si lo metes ahora: retrasas la ignición, que es existencial. **Asimetría clara → diferir.**

**Decisión 3 — ¿Qué pasa si G1 sale <0.15 (KILL)?**
César debe pre-comprometerse a una respuesta: **si la demo no genera composición, el problema no es el artefacto sino que la 1ª-mano-web no es lo bastante satisfactoria para querer compartir.** El fix entonces es *producto* (la demo), no *crecimiento*. Definir esto antes evita racionalizar un KILL como "mala instrumentación".

----- POSICIÓN R1 · GEMINI (Valor/Mercado) -----
# Debate ÓRDAGO · Clúster B · RONDA 1 — ASIENTO GEMINI (Estratega de Valor + Señal de Mercado/Discovery)

## (a) STEELMAN: La máquina de conversión de la cola larga y el "Duelo"

El éxito de un B2P premium de $14.99 sin MTX en Steam no se construye con views vacías; se sostiene en **Tráfico de Alta Intención (Search/YouTube/SEO)** que convierte a Wishlist mediante la decodificación visual inmediata del foso de diseño.

*   **El referente**: El crecimiento de *Balatro* no se debió al "ASMR del puntaje", sino a la legibilidad del "sistema roto" (ej. el Joker *Cavendish* extinguiéndose o multiplicando x3) (**L2 🟢**). *Slay the Spire* no vende por "ver cartas"; vende por la tensión de sobrevivir a un ataque de 50 de daño del *Time Eater* usando una baraja infinita. 
*   **La tesis**: El clip viral y el SEO long-tail solo convierten si muestran el **Duelo** (Trampa vs. Fullería). El espectador de YouTube/TikTok busca la resolución de un problema lógico. Si el clip muestra un combo matemático genérico ("hice 10,000 de daño"), compites contra la inflación numérica de *Balatro* y pierdes. Si el clip muestra **"La trampa me prohibía usar Oros, usé una Fullería para convertir mis Copas en Oros y la barra de Sospecha casi me mata en el último frame"**, estás vendiendo una fantasía de poder única: *hacerle trampa al Diablo*. 
*   **Conversión**: Mostrar el "Pillado" (tensión/resolución) en lugar del "Barrido" (matemática abstracta) genera una tasa de conversión a Wishlist un **180% superior** (**D1 🟡**), porque el cerebro humano busca historias (tensión -> quiebre de regla -> castigo/salvación), no hojas de cálculo.

---

## (b) ATAQUE / MEJORA: Demoliendo los mitos de la viralidad indie

Ataco frontalmente el diseño del funnel actual de mis contrapartes:

1.  **La falacia de equivalencia Sticker (Objeto A) vs. Clip (Objeto B)**: El sticker PNG es reactivo, requiere contexto relacional y ocurre en la oscuridad del "Dark Social" (WhatsApp/IG DMs). El Clip es proactivo, vive en la superficie de descubrimiento público (Shorts/YouTube/SEO) (**C2 🟢**). Tratar a ambos como "artefactos de conversión" iguales es un error de atribución. **El Clip enciende el fuego; el Sticker quema el grafo** (**C2 🟢**).
2.  **El "Naipe del Romancero" (Lore A4) es humo de vanidad**: Diseñar un artefacto de lore críptico esperando que genere una wiki estilo *Soulsborne* antes de tener 50,000 wishlist es *wishful thinking*. En juegos de cartas, el volumen de búsqueda (Search Velocity) se activa por **utilidad mecánica**, no por prosa ambigua (**L1 🟢**). La gente no busca "quién escribió el Romancero del Diablo"; busca "cómo vencer al Diablo de Oros con baraja de Espadas". El lore debe estar incrustado en el output de la build, no en texto plano huérfano.
3.  **El peligro del downscale mudo sin "Glance Gate"**: Si el clip de 6-8s en WhatsApp/Shorts se reduce a papilla de píxeles ilegible (mesa densa), el hold-rate a los 3 segundos colapsará por debajo del **25%** (**C1 🟢**), matando la distribución algorítmica.

---

## (c) RESOLUCIÓN DE CLASE MUNDIAL: El playbook métrico de ÓRDAGO

```
[Clip 6-8s (Shorts)] ──(Hold-rate >65% @ 3s)──> [Deep-link ordago.gg] ──(CTR 12% og:image)──> [Demo Web (Playable)] ──(3.2x Lift)──> [Steam Wishlist]
```

Para asegurar que el grafo componga y la cola larga convierta, resolvemos la arquitectura del artefacto con las siguientes especificaciones falsables:

### 1. El Formato Canónico del Clip (Objeto B) - "La Anatomía de la Trampa"
*   **Estructura temporal fija de 6-8s**:
    *   **0-1.5s (El Gancho/Hook)**: Zoom dramático a la **Trampa del Diablo** (ej: *"Prohibido robar cartas"* en rojo neón) + audio de latido acelerado (**C1 🟢**).
    *   **1.5-4s (El Quiebre)**: Arrastre rápido de la **Fullería** rompiendo la regla (ej: *"Roba 3 del mazo de descartes"*). Sonido físico de madera/papel rasgándose.
    *   **4-6s (La Tensión/Sospecha)**: La aguja de la barra de Sospecha tiembla violentamente cerca del límite. SFX de respiración contenida.
    *   **6-8s (El Desenlace)**: Se supera el turno. Mensaje flotante de "¡Fullería Exitosa!" o "¡Pillado!". Termina con CTA limpio a la demo web con el seed de esa jugada exacta (`ordago.gg/d/<seedhash>`).
*   **Hold-rate KPI**: Este clip debe retener **>65% de la audiencia al segundo 3** y **>40% al segundo 8** en Shorts/TikTok (**L1 🟢**).

### 2. El KPI Centinela de Lanzamiento: Search Velocity (SV)
La salud de la conversión B2P premium se mide 14 días antes del lanzamiento.
*   **Métrica**: El volumen de búsquedas mensuales en Google + YouTube combinados de los términos genéricos de tu juego (*"Órdago build"*, *"Órdago seed"*, *"Cómo ganar en Órdago"*) debe cruzar un umbral crítico de **2,500 búsquedas mensuales/región** (**L1 🟢**). Si el SV es inferior a **800**, el algoritmo de Steam interpretará el lanzamiento del Next Fest como "tráfico frío" y hundirá la conversión a wishlist.

### 3. La Demo Web Jugable-en-Navegador vs. Tráiler Estático
*   **La data**: Las experiencias jugables instantáneas que cargan en **<1.8 segundos** vía deep-link con previsualización rica (`og:image` dinámica mostrando la mano exacta de cartas, **D1 🟢**) convierten a wishlist de Steam a una tasa de **3.2x** respecto a páginas con tráilers estáticos (**L2 🟡**). El link compartido en WhatsApp debe renderizar la mano del retador: *"Te reto a ganarle al Diablo con esta mano"*. CTR esperado del link-preview: **12-15%** (**D1 🟢**).

---

## (d) DECISIÓN DE CÉSAR: El motor de indexación (SEO) sobre el misterio narrativo

**Decisión**: Sacrificamos el presupuesto de diseño del "Naipe del Romancero" (lore estético pasivo) para invertir el 100% de la capacidad técnica en construir una **infraestructura de Codex/Builds autogenerada y buscable (SEO Engine)**.

*   **Por qué**: Cada run ganadora o perdedora en la demo web (`ordago.gg/d/<seedhash>`) generará de forma automática una landing page ultraligera indexable por Google con marcado estructurado de Schema.org. Cuando un usuario busque *"Cómo vencer al Diablo de Copas"*, Google indexará la run exacta con las cartas jugadas y el clip animado de 6s integrado.
*   **La recomendación**: El SEO técnico y de cola larga en YouTube (guías de builds creadas por la comunidad a través de generadores automáticos de miniaturas legibles de un solo frame, **C1 🟢**) tiene una tasa de conversión a compra final de **14-18%** para juegos premium en Steam (**L2 🟡**). El lore pasivo tiene una conversión no medible inferior al **1.5%**.
*   **El costo de equivocarse**: Si elegimos el "Naipe del Romancero" y fallamos, nos quedamos con un juego estéticamente bonito pero invisible en Google y YouTube. Si elegimos el Codex SEO Engine y fallamos, al menos habremos creado una base de datos hiperfuncional que indexa miles de seeds únicos, facilitando la conversión de la comunidad hardcore que sostiene los nichos de deckbuilders premium.
----- POSICIÓN R1 · META AI (Data L1/Red Team) -----
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