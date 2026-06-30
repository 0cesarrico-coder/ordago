# SÍNTESIS — Clúster B · Artefacto-puente (composición de K, primer contacto, watchability)

> Síntesis de 3 IAs (Opus = sistemas de crecimiento · Gemini = valor/mercado/discovery · Meta AI = data L1/red team) tras 2 rondas + referee. Fiel a lo dicho; sin inventar consenso. Veredicto referee: **CONVERGED** (consenso 9, contestados 5 — 4 los zanja un experimento, 1 real de arquitectura).

---

## 1. Veredicto del clúster

El debate convergió fuerte hacia **Meta AI como ancla de realidad L1**: el grafo LATAM vive en Dark Social (WhatsApp), donde **el click-through de link en chat familiar es <5%** y **el reenvío de sticker >60%**. Esto forzó el flip dominante del clúster: Opus cedió su K2≥0.35 (asumía click) y aceptó que **el sticker mudo autocontenido es el puente primario, el clip es solo encendedor de descubrimiento (Reels/IG), y el deep-link/demo es el destino del clip, no del sticker**. Hay 9 consensos firmes; los desacuerdos restantes son casi todos calibraciones de umbral que zanja un experimento barato, salvo uno genuino de principio (¿beacon stateless o cero-backend?) que queda para César.

---

## 2. Resoluciones de clase mundial — por hueco

### #27 · Composición de K / activación atribuible — **CONTESTADO (umbral) → resuelto a activación, no shares**
- **Cambio GDD:** la demo web genera el sticker+texto relacional **desde la 1ª mano, 100% cliente, 0 servidor** (invariante C2 de Chen: el nodo nuevo —que no pagó— produce output reinvertible). Esto convierte el árbol de profundidad-1 en profundidad-N. **CONSENSO 3/3.** 🟢 L2.
- **La métrica de ignición SÍ está contestada en el umbral:** todos aceptan medir **activación río abajo, no reenvíos ni clicks** (reenvíos = vanity). La brecha numérica se estrechó a: Opus-crossreview **≥3 partidas/100 stickers** (≈0.03, KILL <1/100) vs Meta AI **K2 local ≥0.18 / KILL <0.08**. Ambos declaran explícitamente que **falta L1 de "tasa real de partida-iniciada-desde-sticker en LATAM" para fijar el VERDE → lo zanja un experimento, no más debate.** 🟡 L4 (diseño).
- **Data L1 integrada (Meta AI):** click <5% en chat familiar + reenvío sticker >60% ⇒ el sticker debe ser **autocontenido** (entrega el golpe relacional completo SIN requerir click). Umbral 0.35 era "fantasía" (WhatsApp recortó viralidad de altamente-reenviados 70% y forwards totales 25% en 2 años). 🟢 L1.
- **Tensión interna sin cerrar:** los dos docs Opus difieren (0.35 en uno, 3/100 en el otro). Se toma el cross-review (3/100) como voto canónico.

### #19 · OG-preview <100ms — **CONSENSO 3/3 en estático; CONTESTADO si se añade capa dinámica**
- **Cambio GDD:** `og:image` **ESTÁTICO** 1200×630, <45–50KB JPEG, servido desde CDN/edge (MX/BR) con `Cache-Control: max-age=31536000`, **sin JS, sin SSR-por-seed**. TTFB p95 **<80–100ms** para sobrevivir el timeout sub-segundo del scraper (WhatsApp/FB/IG no ejecutan JS). KILL: preview en blanco en validador FB/WA, o p95 >120ms. **CONSENSO 3/3** en que lo que el scraper recibe debe ser estático. 🟢 L1 (docs API).
- **CONTESTADO (CT-2):** ¿añadir capa dinámica ("María te ganó por 2") horneada en cliente y subida a CDN para saltos posteriores? Opus/Gemini sí; **Meta AI NO** ("doble cache-miss en CDN LATAM; el chisme va en el TEXTO copiable, no en la imagen scrapeada"). **Falsable barato → lo zanja un experimento** (el validador FB/WA lo muestra en blanco o no).

### #40 · Glance del sticker — **CONSENSO 3/3**
- **Cambio GDD:** glance-gate de build — el sticker debe leer el **chisme relacional** ("por mucho/poco", "te robé +12%") a **100×100px gris/mudo**. VERDE ≥90% lectura correcta (n≥20); KILL <90% → rehacer silueta. Silueta Diablo centrada; texto relacional ocupa ≥40% del área. 🟢 L1/C1.

### #60 · Clip = arco del pillado, no barrido — **CONSENSO 3/3**
- **Cambio GDD:** el clip vende el **DUELO (Trampa↔Fullería)**, no combo/ASMR numérico (vs Balatro). Estructura temporal fija **0–8s: Gancho (0–1.5s, zoom a la Trampa) → Quiebre (1.5–4s, la Fullería rompe la regla) → Sospecha/Tensión (4–6s, barra de Sospecha tiembla) → Desenlace/Pillado (6–8s)**. First-frame-gate: el 1er frame = cara/ojos del Diablo pillándote (legible sin audio). **CONSENSO 3/3.** 🟢 L2 (Balatro/StS venden tensión de regla rota, no ASMR).

### #62 · Motion-gate — **CONSENSO 3/3 (reformulado como PISO, no techo)**
- **Cambio GDD:** WhatsApp recodifica WebP y **congela en el 1er frame** ⇒ "el primer frame lo dice todo". Gate = **piso de legibilidad del MOAT** (Opus R2 lo reformuló de techo a piso para no matar virales caóticos): ≥70% nombra "¿hubo trampa? ¿quién gana?" a 360p mudo 3s. Sticker mudo por diseño (sobrevive recodificación). 🟢 L1.

### #65 · Reacción transferible — **CONSENSO parcial 2-3/3 (residual)**
- **Cambio GDD:** el **chisme relacional cruza mejor que el score técnico** ("María te ganó por 2" > "10.000 de daño"). Data L1 (Meta AI): preferencia por stickers personalizados 56%, con texto 36% ⇒ legibilidad relacional > número abstracto. 🟡 L3 (no hay L1 de CTR-por-copy). Reaction-gate clasificado **residual de perdurabilidad**, no de ignición.

### #25 · Lore-UGC (Naipe del Romancero) — **CONSENSO 3/3: DIFERIR**
- **Cambio GDD:** diferir post-lanzamiento. Su KPI (lore_share D30–D60) no es falsable pre-launch y compite por arte con el sticker competitivo que mueve CAC en semana 1. Volumen de búsqueda se activa por **utilidad mecánica** ("cómo vencer al Diablo de Oros"), no por prosa críptica. **CONSENSO 3/3.** 🟢.

### #56 · Watchability de run (momento-clip como invariante) — **CONSENSO blando (Opus lo eleva)**
- **Cambio GDD:** invariante de run barato (solo telemetría) — "una run no termina sin ≥1 momento transmisible (pico de tensión-resuelta detectado)". KPI ≥1 clip/30min; KILL 30min sin pico → revisar densidad de Trampas/Fullerías. Reusa el detector de pico del exportador. Construible temprano por ser barato. 🟡 L4.

### #57 · SEO / Search Velocity — **CONTESTADO (Gemini aislado en el Engine; SV absorbido 3/3)**
- **Search Velocity como gate pre-launch** (de Gemini): es aceptado por los 3 como señal útil. **CONTESTADO el umbral:** Gemini ≥2,500/mes/región (Opus+Meta AI: "es número de Balatro post-launch, no pre-launch indie"); Meta AI baja a ~600/mes. KILL conceptual: SV bajo ⇒ Steam ve "tráfico frío" en Next Fest y hunde la conversión. **CONSENSO 3/3 en construir solo el MEDIDOR de SV ahora.** 🟡 L3.
- **SEO-Engine autogenerado por seed:** Gemini = motor principal; **Opus + Meta AI (2/3) = residual** ("thin content / soft-404s en Google 2026, traiciona 0-servidor"). Opus propone alternativa: **una sola landing-compendio estática** (top-100 seeds, cron diario, $0), no millones de páginas. **Gemini queda en minoría 1/3.**

### Transversal · #22 Autoplay (WKWebView) — **CONSENSO 3/3**
- **Cambio GDD:** in-app browser bloquea autoplay con sonido. Video **muted + playsinline**; el audio se **arma en el 1er tap** ("activar trampa sonora"). Demo inicia <1.5s (Lighthouse mobile). 🟢 L1.

---

## 3. Decisiones de César

| # | Decisión | Recomendación del clúster | Estado |
|---|---|---|---|
| **D1 (CT-4) — único contestado real** | **¿Beacon stateless o cero-backend para atribución?** | **Opus:** 1 endpoint stateless (nonce encadenado, sin identidad/cuentas) — medible. **Meta AI:** 0 servidor ni beacon — atribución 100% local en `localStorage` (contar arista si genera sticker en <24h), "instrumentación falsa > beneficio". Es decisión de **principio/arquitectura** ("0 servidor" como moat vs medibilidad), NO resoluble con un test. | **PARA CÉSAR** |
| **D2** | **Umbral de ignición / VERDE de K2** | Pre-comprometerse a medir **activación (partidas atribuibles), no reenvíos ni clicks**, con umbral BAJO calibrado a click<5%. Brecha 0.03 (Opus) vs 0.18 (Meta AI) → **fijar con un experimento real de tasa partida-desde-sticker en LATAM.** | Experimento |
| **D3** | **SEO: ¿Engine por-seed ahora?** | **Diferir el Engine** (residual, riesgo thin-content). Construir solo: medidor de Search Velocity + UNA landing-compendio estática. Engine completo post-ignición-verde. | Recomendación 2/3 |
| **D4** | **Pre-compromiso si K2 sale KILL** | Si <1/100 (Opus) o <0.08 (Meta AI): el problema NO es el copy — **el sticker no es autocontenido** (exige un click que LATAM no da). Fix = producto: el sticker entrega el golpe relacional SIN destino; el clip (no el sticker) carga el deep-link. Definirlo ANTES evita racionalizar el KILL como "mala plantilla". | Recomendación 3/3 |
| **D5** | **Reparto de esfuerzo sticker/clip** | Gemini implícito clip-pesado; **Meta AI 60/25/15** (60% sticker, 25% clip, 15% atribución local); Opus R1 70/30. Consenso: **sticker primario, clip encendedor.** | ~60-70% sticker |

---

## 4. Para el GDD v1.3 — ediciones accionables

- **§Artefacto-puente (objeto canónico):** sticker PNG/WebP estático **<80KB, 512×512**, render 100% cliente desde la 1ª mano, 0 servidor; texto relacional ≥40% del área + silueta Diablo centrada; texto/emoji copiable debajo (`ordago.gg/d/<seed> — te gané por 2`). El sticker es **autocontenido** (golpe relacional sin requerir click). [#27, #40, #65]
- **§Clip encendedor:** WebP animado **6–8s, <300KB, muted+playsinline, loop perfecto**; estructura fija Gancho→Quiebre→Sospecha→Pillado; 1er frame = Diablo pillándote (legible sin audio). Rol: **encendedor en Reels/IG/Stories**, no puente principal; es el portador del deep-link a la demo. [#60, #62]
- **§OG-preview:** `og:image` ESTÁTICO 1200×630 <45–50KB JPEG, CDN edge MX/BR, `max-age=1yr`, sin JS, sin SSR-por-seed; TTFB p95 <80–100ms. Chisme dinámico va en el TEXTO copiable (capa dinámica de imagen = experimento opcional, no bloquea). [#19]
- **§Gates de build (falsables, antes de arte):** glance-gate (≥90% lee chisme a 100×100px gris), first-frame/motion-gate (≥70% nombra trampa+ganador a 360p mudo 3s), hold-rate clip (≥45–48% @3s, ≥22–25% completion, sends/view ≥2.5–3%, KILL hold <35%). [#40, #62, #60]
- **§Métrica de ignición (K2):** medir **activación atribuible, no reenvíos**; umbral provisional bajo (3/100 ↔ 0.18) **pendiente de experimento L1**; reenvíos/partida (VERDE ≥1.8) solo como proxy de ALCANCE, nunca de éxito. Marcar D1 (beacon vs local) como decisión abierta de César. [#27]
- **§WKWebView/autoplay:** muted+playsinline; audio se arma al 1er tap; demo inicia <1.5s. [#22]
- **§Discovery pre-launch:** añadir **Search Velocity como gate centinela T-14d** (medidor solo; umbral ~600–2,500/mes/región a calibrar); **diferir SEO-Engine por-seed**; sustituir por landing-compendio estática top-100 seeds. [#57]
- **§Watchability de run:** invariante "≥1 momento transmisible por run" vía detector de pico (reusa exportador); KPI ≥1 clip/30min. [#56]
- **§Lore (Romancero):** marcar **DIFERIDO post-lanzamiento**. [#25]
