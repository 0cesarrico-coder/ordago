# Clúster B · Ronda 2 — CROSS-REVIEW · ASIENTO OPUS (Diseñador de Sistemas de Crecimiento)

> Mantengo mi lente: el grafo solo importa si **compone** (nodo nuevo genera output reinvertible) y cada promesa muere en un **gate falsable barato** antes de un píxel. La R2 me obliga a un giro grande: Meta AI aportó **L1 que rompe mi G1**.

---

## (a) STEELMAN de las posiciones ajenas

**Meta AI (Data L1/Red Team) — la posición más fuerte del clúster.** Su tesis "sticker primero, clip después, texto siempre" no es preferencia, es **topología medida del grafo LATAM**. Tres L1 que yo no tenía y que reescriben mi diseño:
1. **Click-through de link en chat familiar <5%, reenvío de sticker >60%** (L3 🟡, estudios LATAM). Esto **destruye mi G1 tal como lo escribí**: yo definí K2 como "invitado abre deep-link y completa 1ª mano". Si el 95% del grafo nunca hace click, mi nonce-encadenado mide el 5% que sí — un grafo fantasma. **Concede el ataque.**
2. **OG sin JS, scraper con timeout sub-segundo, og:image <100KB en <200ms o preview en blanco** (L4 ⚪→L1 🟢 en docs). Mi G2 "capa-partida horneada al terminar la mano" llega tarde para el scraper. Tenía razón a medias: mi *fallback* estático salva, pero la capa dinámica que yo quería era humo para el scraper.
3. **WhatsApp recodifica WebP y congela en primer frame; autoplay con sonido bloqueado en WKWebView** (L1 🟢). Mata mi supuesto implícito de que el clip "se reproduce".

**Gemini (Valor/Mercado).** Steelman fuerte: el **Search Velocity como KPI centinela 14 días pre-launch** (umbral ≥2,500/región, <800 = "tráfico frío" que Steam hunde) es exactamente lo que me faltaba — un gate falsable **antes** del launch para la conversión B2P, no después. Es el complemento de discovery a mi familia de gates de artefacto. Y su distinción "Clip enciende / Sticker quema" coincide con Meta AI por dos caminos independientes (mercado + data) → señal robusta.

---

## (b) ATAQUE específico

1. **A Gemini — el "180% superior" y "3.2x lift" son D1 🟡 sin cadena causal y los trata como L1 operativos.** Cita: *"genera una tasa de conversión a Wishlist un 180% superior (D1 🟡)"* y *"convierten a wishlist 3.2x (L2 🟡)"*. Construir el funnel sobre dos multiplicadores no atribuidos es mi propio pecado de R1 (vanity metric) en versión mercado. **CONTESTADO: los multiplicadores son hipótesis a medir, no premisas de diseño.** El número que SÍ es accionable es su Search Velocity (falsable, barato, pre-launch).

2. **A Gemini — su "SEO Engine autogenerado por seed" colisiona con la L1 de Meta AI.** Miles de landing pages por seedhash asumen tráfico que hace click y que Google indexa rápido. Pero si el grafo vive en Dark Social (WhatsApp, click <5%), el SEO Engine indexa páginas que casi nadie visita vía grafo — su valor es de **cola larga/hardcore**, no de ignición. Gemini lo vende como motor principal; es residual de perdurabilidad. Coincide con mi crítica R1 al Romancero: scope con retorno diferido.

3. **A Meta AI — su 70/30 sticker/clip es correcto pero su K=2.4 reenvíos/partida mide el síntoma equivocado, igual que yo en R1.** Cita: *"K objetivo: 2.4 reenvíos promedio por partida... Kill si <1.5 reenvíos en 48h"*. **Reenvíos ≠ activaciones.** Es exactamente la trampa que yo señalé contra mí mismo (K2 = shares vs activaciones). Si el sticker se reenvía 2.4× pero nadie juega, K_real<1. Meta AI cae en el mismo pozo que critiqué. **CONTESTADO: la métrica de ignición debe ser activación río abajo, no reenvíos.**

---

## (c) CONVERGENCIA

**CONVERGES (3/3 o 2/3 fuerte):**
- **Sticker mudo, render cliente, 0 servidor, texto relacional grande = objeto-puente primario.** Los tres asientos. 🟢 L1/L2.
- **Clip = encendedor de descubrimiento (Reels/IG), no puente principal; arco de "pillado/trampa", no barrido/combo.** 3/3. 🟢
- **og:image ESTÁTICO desde CDN, <100ms, sin JS, sin SSR-por-seed bloqueante.** Meta AI + yo (mi fallback estático gana sobre mi capa dinámica). 🟢 L1.
- **Romancero/lore = diferir.** 3/3. 🟢
- **El MOAT (duelo Trampa↔Fullería) debe ser legible a downscale mudo.** 3/3 (glance-gate). 🟢

**CONTESTADO:**
- **CONTESTADO: la métrica de ignición del grafo.** Reenvíos (Meta AI) vs deep-link+1ª-mano (yo R1) vs lift-a-wishlist (Gemini). Resolución abajo: medir **activación, no reenvío ni click**.
- **CONTESTADO: cuánta infraestructura SEO/seed ahora.** Gemini = motor principal; yo + Meta AI = residual de perdurabilidad. No bloquea launch.
- **CONTESTADO: si la demo web jugable es el destino del puente.** Si click<5%, el deep-link a demo NO es el puente primario — el sticker autocontenido lo es, y la demo es el destino del clip (superficie pública), no del sticker (Dark Social).

---

## (d) REFINA — resolución de clase mundial (números falsables)

**Giro central forzado por L1 de Meta AI:** el sticker primario debe **convertir SIN requerir click** (autocontenido), porque el 95% no hace click. El click es el camino del **clip** (superficie pública IG/Reels), no del sticker (Dark Social WhatsApp). Dos puentes, dos métricas.

| # | Gate | Métrica falsable | VERDE | KILL |
|---|---|---|---|---|
| **G1' sticker** | sticker render-cliente, texto relacional, 0 srv | **reenvíos/partida** (proxy de alcance, NO de ignición) | ≥2.0 en 48h | <1.5 → iterar copy/plantilla |
| **G1'' ignición** | nonce encadenado, pero medido como **nuevas-partidas-atribuibles / 100 stickers-enviados** | activación río abajo | ≥3 partidas/100 (realista dado click<5%) | <1/100 → el sticker no enciende; revisar si el destino debe ser demo o si el sticker debe ser autocontenido |
| **G2 OG** | og:image estático 1200×630 <50KB, Cache 1yr, sin JS, TTFB | latencia scraper | <100ms p95, render ≤200ms | preview en blanco en validador FB/WA → muerto |
| **G3 glance** | sticker→100×100px gris | % lee chisme relacional ("por mucho/poco") | ≥90% (n≥20) | <90% → rehacer silueta |
| **G4 clip** | WebP 6-8s, 1er frame=cara Diablo pillándote, muted+playsinline, loop | hold-rate @3s; sends/view | ≥45% @3s **y** sends/view ≥3% | <15% completion **o** <1% sends → matar formato |
| **G5 SV** (de Gemini) | Search Velocity pre-launch | búsquedas/mes/región T-14d | ≥2,500 | <800 → Next Fest verá tráfico frío, retrasar/inyectar UA |

**Reconciliación de la métrica contestada (el delta de R2):** abandono mi K2 puro de R1 (asumía click). Adopto **dos métricas separadas**: (1) **alcance** = reenvíos/partida de Meta AI (barato, observable, pero NO confundir con éxito); (2) **ignición** = nuevas-partidas-atribuibles/100-stickers vía nonce, calibrada a la realidad click<5% (de ahí el umbral 3/100, no 35%). Mi error R1 fue poner el umbral como si el click fuera default. **L4 🟡** — pedir a Meta AI L1 de tasa real de partida-iniciada-desde-sticker en juegos LATAM para fijar el VERDE.

**Audio (de Meta AI, lo incorporo):** primer tap arma audio; nunca autoplay con sonido. El sticker es mudo por diseño (sobrevive recodificación WhatsApp y congelado en 1er frame). **L1 🟢.**

---

## (e) DECISIÓN DE CÉSAR (refinada)

**D1 — Métrica de ignición.** Pre-comprometerse a medir **activación (partidas atribuibles), no reenvíos ni clicks**, con nonce stateless. Aceptar umbral bajo (3/100) porque click<5% es estructural en LATAM (L1 Meta AI). Costo de equivocarse: optimizar reenvíos (vanity) y celebrar un grafo que no compone.

**D2 — SEO/seed Engine: diferir como motor, construir el esqueleto barato.** Contra Gemini-como-motor-principal: es residual de perdurabilidad/hardcore, no de ignición (click<5% lo confirma). PERO el **Search Velocity (G5) sí es gate pre-launch barato** → construir solo el medidor de SV ahora; el Engine de landing pages, post-ignición-verde.

**D3 — Si G1'' sale KILL (<1/100):** pre-comprometerse: el problema no es el copy del sticker sino que **el sticker no es autocontenido** (exige un click que LATAM no da). Fix = producto: el sticker debe entregar el golpe relacional completo SIN destino, y el clip (no el sticker) carga el deep-link a la demo. Definirlo antes evita racionalizar el KILL como "mala plantilla".

**Convergencia neta:** 3/3 en sticker-mudo-primario, clip-encendedor, og-estático, diferir-lore, MOAT-legible. **Contestado:** la métrica de ignición (resuelto a activación, no reenvíos/clicks) y cuánto SEO ahora (solo el medidor de Search Velocity).
