# Referee R2 — Clúster B (artefacto-puente: composición de K, primer contacto, watchability)

> Contexto fresco. NO debatiente. Mido convergencia R2 vs R1, no opino de diseño.
> Asientos: Opus (sistemas de crecimiento), Gemini (valor/mercado/discovery), Meta AI (data L1/red team).
> Nota: en R2 hay DOS documentos firmados "OPUS" (`opus-r2.md` y `opus-r2-crossreview.md`). Trato `opus-r2-crossreview.md` como el voto canónico de Opus por ser el cross-review explícito; uso `opus-r2.md` solo para detectar tensiones internas. Donde difieren, lo anoto.

---

## (1) CONSENSO 3/3 (los tres asientos lo afirman explícitamente en R2)

| # | Punto convergido | Opus R2 | Gemini R2 | Meta AI R2 | Evidencia |
|---|---|---|---|---|---|
| C1 | **El artefacto debe vender el DUELO (Trampa↔Fullería), NO barrido/combo numérico** | sí | sí (tesis central R1, sostenida) | sí ("los tres lo piden") | L2 🟢 |
| C2 | **Sticker mudo, render 100% cliente, 0 servidor, texto relacional grande = objeto-puente primario que cruza WhatsApp** | sí | sí | sí | L1/L2 🟢 |
| C3 | **La demo web genera output (sticker) desde la 1ª mano, en cliente** (composición / C2 de Chen) | sí (G1) | sí | sí ("Opus G1 = mi sticker") | L2 🟢 |
| C4 | **Clip = encendedor de descubrimiento (Reels/IG/Stories), no puente principal; arco "pillado", no ASMR** | sí (G4) | sí (anatomía del clip) | sí (G3 encendedor) | L1/L2 🟢 |
| C5 | **og:image ESTÁTICO desde CDN, sin JS, sin SSR-bloqueante-por-seed, baja latencia (<~100ms)** | sí (sirve fallback estático instantáneo) | — (ver contestado #2) | sí (<80-100ms, núcleo de su red team) | L1 🟢 |
| C6 | **Romancero/lore = diferir post-lanzamiento** | sí | sí | sí | 🟢 |
| C7 | **WKWebView: audio muted+playsinline, audio se arma en el 1er tap; nunca autoplay con sonido** | sí (G4) | sí (lo concede) | sí (L1) | L1 🟢 |
| C8 | **El MOAT debe ser legible a downscale mudo / "primer frame lo dice todo"** (glance-gate / first-frame-gate) | sí | sí (glance gate) | sí (C1, 100px gris) | L1/C1 🟢 |
| C9 | **Estructura temporal fija del clip 0-8s: Gancho → Quiebre → Sospecha → Desenlace/Pillado** | sí | sí (la propuso) | sí (alinea con watch-time) | L2 🟡 |

Nueve puntos en consenso firme. C5 es 3/3 en *que el og debe ser estático para sobrevivir el scraper*; el desacuerdo residual es solo si se le AÑADE una capa dinámica (ver contestado).

---

## (2) CONTESTADOS — postura de cada IA en R2

### CT-1 · Métrica de ignición / umbral de K2 *(el contestado central)*
- **Opus (cross-review):** abandona su K2-puro de R1. Adopta **DOS métricas separadas**: (a) *alcance* = reenvíos/partida (de Meta AI, "no confundir con éxito"); (b) *ignición* = **partidas-atribuibles/100-stickers** vía nonce, con umbral **bajado a ≥3/100** (KILL <1/100) *precisamente porque click<5% es estructural en LATAM*. Reconoce que su 0.35 de R1 "asumía click como default" y era un error.
- **Opus (doc paralelo `opus-r2.md`):** todavía sostiene **K2 ≥0.35 / KILL <0.15** sobre clicks-en-demo. → tensión interna no resuelta entre los dos docs Opus.
- **Meta AI:** **K2 ≥0.35 es fantasía** (L1 🟢: WhatsApp cortó viralidad 70%, forwards 25%). Propone **K2 local ≥0.18 / KILL <0.08** (sin beacon) + reenvíos/partida ≥1.8 como proxy de alcance.
- **Gemini:** su métrica de ignición es **Search Velocity** (≥2,500/región), no K2. No fija un umbral de K2.

**Estado:** convergencia FUERTE en R2. Los tres aceptan (i) medir activación, no shares; (ii) que el umbral debe reflejar click<5% → bajarlo. La brecha numérica se estrechó de [0.35 vs reenvíos] a **[Opus-cross 3/100 ≈ 0.03 vs Meta AI 0.18]** — el desacuerdo restante es **calibración del VERDE, que ambos dicen explícitamente que falta L1 para fijar** (Opus: "pedir a Meta AI L1 de tasa real partida-iniciada-desde-sticker"). → **lo zanja un experimento, no más debate.**

### CT-2 · Personalización del preview: og dinámico por partida, sí o no
- **Opus:** **híbrido** — fallback estático instantáneo (<50-80ms) para el scraper + capa dinámica horneada en cliente y subida a CDN keyed por nonce para el *siguiente* salto. Nunca bloquea el preview.
- **Gemini:** quiere el chisme dinámico ("María te ganó por 2") en el preview (multiplicador de CTR).
- **Meta AI:** **NO al og dinámico.** El scraper sub-segundo verá siempre el fallback genérico; "el chisme va en el texto copiable, no en la imagen scrapeada". Dos capas = doble cache-miss en CDN LATAM.

**Estado:** PARCIALMENTE convergido. Los tres coinciden en que **lo que el scraper recibe debe ser estático** (C5). El desacuerdo es si vale la pena la capa dinámica adicional para saltos posteriores. Meta AI lo declara medible ("el validador FB/WA lo muestra en blanco o no"). → **falsable barato → lo zanja un experimento.**

### CT-3 · Cuánta infraestructura SEO / "Codex de seeds" ahora
- **Gemini:** **motor principal** — landing autogenerada por seed, Schema.org, indexable; sacrificar lore por esto.
- **Opus:** **rechazar el indexador por-seed** (thin content, soft-404s, traiciona 0-servidor). Conservar solo: **medidor de Search Velocity** ahora + UNA landing-compendio estática (top-100 seeds, cron diario). El Engine completo = post-ignición.
- **Meta AI:** miles de landing /d/<seed> = **thin content 2026**; Search Velocity 2,500 es número de Balatro *post*-launch, no pre-launch indie. Baja el umbral sano a ~600/mes.

**Estado:** Opus + Meta AI convergen (2/3) en "SEO-Engine = residual, no de ignición". Gemini sigue solo. PERO los tres aceptan **Search Velocity como señal pre-launch útil** — el desacuerdo es el umbral (2,500 vs 600) y si el Engine se construye ya. → 2/3, Gemini aislado pero su pieza accionable (SV) fue absorbida.

### CT-4 · Backend para atribución: beacon stateless sí o no
- **Opus (cross):** 1 endpoint de telemetría **stateless** (beacon, sin identidad/cuentas).
- **Meta AI:** **0 servidor, ni siquiera beacon** — "el costo de instrumentación falsa > beneficio"; atribución 100% local en `localStorage`, contar arista si genera sticker en <24h.
- **Gemini:** no toma postura explícita sobre beacon (su foco es SEO/SSR).

**Estado:** CONTESTADO real 1-vs-1 (Opus beacon mínimo vs Meta AI cero-backend). Es genuino y no se zanja con un solo experimento de artefacto — es una decisión de arquitectura/principio ("0 servidor" como moat vs medibilidad). Queda para César.

### CT-5 · Hold-rate objetivo del clip (realismo del benchmark)
- **Gemini:** >65% @3s, >40% @8s.
- **Meta AI:** **>65% no existe para IP nueva** (L1: Reels gaming 45-52% @3s). Propone ≥48% @3s, ≥22% completion.
- **Opus:** adopta los números de Meta AI (≥45% @3s, sends/view ≥3%) en su tabla de gates.

**Estado:** CONVERGIDO de facto. Opus se movió al rango de Meta AI; solo Gemini mantiene 65%. 2/3 fuerte, y es puramente empírico (un test de 3 clips lo zanja). → **lo zanja un experimento.**

---

## (3) CAMBIOS R1 → R2

| Asiento | R1 | R2 | Tipo de cambio |
|---|---|---|---|
| **Opus** | K2-activación ≥0.35 vía deep-link+nonce, asumía que el invitado hace click | **Concede el ataque de Meta AI**: click<5% en chat familiar destruye su G1. Separa en **alcance (reenvíos) + ignición (partidas/100 stickers)** y **baja el umbral a 3/100**. Sticker debe ser **autocontenido** (golpe relacional sin requerir click); el click es el camino del CLIP, no del sticker. | **FLIP grande** (cede la premisa central de R1) |
| **Opus** | og:image dinámico por seed | **Fallback estático gana sobre la capa dinámica** para el scraper; capa dinámica solo para saltos posteriores | Ablandamiento parcial (movimiento hacia Meta AI) |
| **Opus** | motion-gate como techo | reformula a **piso de legibilidad del MOAT** (≥70% nombra trampa+ganador) | Refinamiento propio |
| **Gemini** | Clip 6-8s + SEO-Engine como motores; SV ≥2,500; hold 65%; lift 180%/3.2x como premisas | Sostiene SEO-Engine y SV ≥2,500 y hold 65%. **No concede** los ataques (thin-content, click<5%, benchmark 65% irreal). Sus multiplicadores 180%/3.2x quedan marcados por Opus como D1 🟡 = hipótesis, no premisa. | **Se mantiene firme** (poco movimiento; el más estático) |
| **Meta AI** | sticker primero/clip después/texto siempre; K=2.4 reenvíos; 70/30; OG <100ms; hold 45% | **Refina con más L1**: pipeline **60/25/15**, K2 local **≥0.18** (sin beacon), reenvíos VERDE ≥1.8, og <45KB TTFB <80ms, hold ≥48%, SV sano ~600. Mantiene "0 servidor, sin beacon" frente a Opus. | **Consolidación + endurece** la línea anti-beacon |

**Dirección neta del clúster:** convergencia hacia **Meta AI** como ancla de realidad L1. El movimiento dominante de R2 es el **FLIP de Opus** (cede su K2≥0.35 y su og-dinámico-prioritario). Gemini es el outlier que menos se movió; sus piezas falsables (Search Velocity) fueron absorbidas por consenso aunque su tesis de SEO-Engine-como-motor quedó en minoría 1/3.

---

## Veredicto del referee

- **Consenso 3/3:** 9 puntos (C1–C9).
- **Contestados vivos:** 5 nominales (CT-1…CT-5), pero el estado real:
  - CT-1 (umbral K2), CT-2 (og dinámico), CT-3 (SEO ahora), CT-5 (hold-rate) → **los cuatro son falsables baratos y ambos lados lo reconocen**: *los zanja un experimento, no más debate.*
  - CT-4 (beacon vs 0-backend) → **único contestado genuino de principio/arquitectura** (1-vs-1 Opus↔Meta AI), no resoluble con un test de artefacto; queda para César.
- **Endurecimiento:** ninguno salvo Gemini, que se mantuvo firme pero quedó en minoría sin endurecer el tono; y una **tensión interna no resuelta dentro de los dos docs Opus** (0.35 en uno, 3/100 en el otro) — señal de que la calibración del umbral aún no está cerrada, pero ambos coinciden en que es empírica.
- Aplicando la regla: descontando los 4 contestados que "los zanja un experimento", queda **1 contestado real (CT-4)**. → **CONVERGED.**

Total temas evaluados (T) = consenso 9 + contestados 5 = 14.
Contested vivos (N) = 5. De ellos, contestado-real-no-experimentable = 1 (CT-4).
Flipped (M) = 1 (Opus cede K2≥0.35 → activación calibrada a click<5%, el flip dominante del clúster).
Consensus (K) = 9.

SCORE-INPUT: contested=5 flipped=1 consensus=9 total=14 verdict=CONVERGED
