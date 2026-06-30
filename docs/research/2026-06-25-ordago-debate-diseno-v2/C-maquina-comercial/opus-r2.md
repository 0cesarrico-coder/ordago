# ÓRDAGO · Clúster C · RONDA 2 — OPUS (Modelador de unit-economics + riesgo) · CROSS-REVIEW

## Lo que cambió con la data L1 de Meta AI
En R1 mis techos CAC ($3.1 USA / $3.1 hispanos / $1.55 LATAM) eran razonamiento ⚪ por falta de inputs vivos. **Meta AI me los dio y FALSAN mi gate tal como estaba escrito.** Eso es lo más importante de esta ronda: mi propio gate, con CAC reales, NO pasa por columna. Re-anclo.

---

## #47 — Gate LTV/CAC≥3 · STEELMAN + ATAQUE + REFINA

**STEELMAN (Meta AI).** Su corrección es la pieza que me faltaba y es demoledora: *"'CAC bajísimo orgánico LATAM' es falso… CR a compra PC 0.3–0.6% vs 1.2–1.8% hispanos-USA → CAC efectivo LATAM $4–8, hispanos-USA $6–11"* (L2, conf. Media). Mi tabla LTV se sostiene (neto-refund ~$9.3 / ~$4.7), pero el **CAC real choca contra el techo**:

| Nodo | LTV (neto-refund) | Techo CAC (LTV/3) | CAC real Meta AI | ¿Pasa ≥3? |
|---|---|---|---|---|
| USA general | ~$9.3 | ≤$3.1 | (no dado, ≈$5–9 proxy) | ⚪ probable NO con UA pago |
| Hispanos-USA | ~$9.3 | ≤$3.1 | **$6–11** | 🔴 **NO** (LTV/CAC ≈ 0.8–1.5) |
| LATAM | ~$4.7 | ≤$1.55 | **$4–8** | 🔴 **NO** (LTV/CAC ≈ 0.6–1.2) |

**ATAQUE a mí mismo + a Gemini.** Dos cosas se rompen:
1. **Mi gate "CAC≤LTV/3 medible ex-post" sigue siendo el marco correcto, pero su lectura ingenua mata el proyecto entero** si se interpreta como "UA de pago debe cerrar ≥3". Con CAC pago $6–11, NINGÚN nodo cierra ≥3 vía paid. Conclusión dura: **ÓRDAGO no es un negocio de UA pago a wishlist; es un negocio ORGÁNICO con paid como acelerante marginal de cola.** El gate ≥3 debe aplicarse al **CAC blended (orgánico+pago), no al CAC pago puro.**
2. **Gemini (#47) usa 0.04/0.09/0.16× conversión WL** y yo usé **0.05/0.12/0.17×**. Convergemos en banda (~2× de spread), pero su escenario "Bajo 0.04× = inviable" es el realista si la WL es fría — y Meta AI lo confirma: *"60–70% de WL LATAM nunca convierten"*. **CONTESTADO: la conversión WL no es una sola banda; es bimodal por CALIDAD de WL (orgánica-search vs fría-bundle).** Promediarlas es el error de Carless.

**REFINA — gate falsable v2 (re-anclado a L1):**
- **Gate primario (orgánico):** el proyecto vive si **≥60% de las ventas Sem-1 provienen de WL orgánica (search-velocity, no paid)**. Meta AI: search directo pesa 5× (vía Gemini) y convierte; WL fría no. Esto sustituye "predecir unidades" por "auditar la FUENTE de la WL".
- **Gate de UA pago (marginal):** paid solo se autoriza en el nodo donde **CAC_pago ≤ LTV** (payback simple <1, no ≥3). Hispanos-USA con LTV $9.3 y CAC $6–11 → **paid solo si el clip-puente baja CAC a ≤$6** (cae en virality/share, ver #66). LATAM paid: **prohibido a wishlist** (CAC $4–8 > LTV-share efectivo); LATAM se gana solo orgánico/viral. 🟡
- **Gate blended (el que importa para kill):** **LTV/CAC_blended ≥ 3 en escenario mediano**, donde CAC_blended se diluye porque el grueso del volumen es orgánico (CAC≈coste del clip-puente / WL incrementales, no $/comprador-paid). Falsable ex-post en demo/Next Fest.
- **Respondo a Gemini (su vacío directo):** *si review-bombing fuerza LATAM a $4.99* → LTV-LATAM cae a ~$3.0 neto-refund, techo CAC ≤$1.0 → **LATAM deja de aportar margen y pasa a ser 100% motor de volumen/viralidad (CAC-a-margen negativo, aceptado)**. NO mueve el breakeven de UA en USA porque **el presupuesto de UA en USA nunca debió cruzar-subsidiar LATAM**: cada nodo se autofinancia o es orgánico. El breakeven USA depende solo de su propio CAC_pago vs $9.3. 🟡

---

## #46/#59 — EA vs 1.0 · ★ DECISIÓN DE CÉSAR ★

**CONVERGENCIA TOTAL 🟢.** Los tres asientos recomendamos **1.0 DIRECTO**. Triangulación de tres evidencias independientes:
- **OPUS (yo):** revenue 1.0 mediano = 40% del EA en 2025; solo ~20% supera su EA [L2🟢 GameDiscoverCo].
- **Gemini:** ~20% supera revenue original; EA mata el "efecto streamer" de fin de semana [L2🟢].
- **Meta AI:** menciones "early access estafa" +34% en comentarios ES vs EN; hispano/LATAM castiga EA 1.4× [L2/L3].

Esta es la convergencia más fuerte del clúster: **el haircut financiero (yo), la dinámica de descubrimiento (Gemini) y el sentimiento del sweet-spot hispano (Meta AI) apuntan al mismo veredicto por caminos distintos.** Eso sube la confianza a 🟢 alta.

**STEELMAN de la única rama EA (mía + Gemini convergen):** EA solo si el balance del set **colapsa antes de hora 5 en >40% de jugadores** (umbral falsable de Gemini, lo adopto) Y requiere N>~5k jugadores reales imposible in-house. Añado mi condición dura: si se va EA, **EA = lanzamiento único, precio EA = $14.99 final, ventana ≤6–9m, updates ≤1 mes**. Meta AI añade la mitigación obligatoria: rótulo "Acceso Anticipado – Versión Jugable Completa" + roadmap ES día 1 + garantía de precio.

**DECISIÓN: 1.0 directo con descuento lanzamiento −20% (sale a $11.99).** Orden de falsación: (1) ¿balance necesita masa >5k? → (2) ¿WL≥7k? → (3) ¿runway aprieta? Solo (1)=SÍ ∧ (3)=SÍ → EA táctico con los 4 gates.

---

## CONVERGE / CONTESTADO

**CONVERGE 🟢:**
1. **1.0 directo** (los tres asientos, tres evidencias independientes).
2. **Gate LTV/CAC≥3 multiescenario por bandas**, validado en mediano (yo + Gemini).
3. **WL fría no cuenta** — gate de CALIDAD de WL, no de volumen (yo + Gemini + Meta AI).
4. **El cuello de botella es el salto móvil→PC**, no el clic (Meta AI L1) → mi payback debe penalizar el funnel WhatsApp→Steam 12–18%.
5. **Banda de review = activo financiero #1 de cola larga**; lift Mixed→Very Positive ~2× USA / +12–18% LATAM (yo + Gemini + Meta AI).

**CONTESTADO:**
- **CONTESTADO: magnitud del lift de review.** Gemini dice 2.1× store-wide; Meta AI acota +22–35% USA / +12–18% LATAM (más conservador y diferenciado por región). Resuelvo a favor de Meta AI (L1 de plataforma) y lo hago **diferencial por nodo**, no global.
- **CONTESTADO: conversión WL es banda única vs bimodal.** Gemini/yo la tratamos como banda continua; Meta AI revela que es bimodal por calidad (orgánica vs fría). Adopto bimodal.
- **CONTESTADO: viabilidad de UA pago a wishlist.** Implícito en R1 que paid alimenta el gate; con CAC L1 de Meta AI ($6–11 hispanos, $4–8 LATAM) **paid-a-wishlist NO cierra ≥3 en ningún nodo**. ÓRDAGO es orgánico-primario; paid solo si el clip-puente baja CAC bajo LTV. Esto es nuevo en R2 y nadie lo afirmó explícito en R1.
- **CONTESTADO: kill cultural / anti-decaimiento sigue en evidencia ⚪.** La señal "70% retención búsquedas 36m" es L4 sin URL (Meta AI lo confirma: no tiene L1). Sostiene TODO el LTV de cola larga → debe volverse KPI medido (búsquedas de marca/mes post-demo, decay <45% a 90d per Gemini) o el LTV largo es fe.

---

## Mi pieza única para R2
**El gate no se rompe por el LTV ni por la conversión WL — se rompe por el CAC pago real (Meta AI L1), que prueba que ÓRDAGO no es un negocio de UA pago sino orgánico-viral con paid marginal.** Reformulo el gate ≥3 sobre **CAC blended** (orgánico domina) y muevo el riesgo a un KPI auditable: **% de ventas Sem-1 con origen WL-orgánica-search ≥60%**. Decisión de César: **1.0 directo, $11.99 launch** (convergencia 🟢 de tres evidencias independientes), con la sola rama EA si el balance del set exige masa >5k imposible in-house Y el runway aprieta.

**Sources:** [GameDiscoverCo — wishlist conversions 2024-25] · [GameDiscoverCo — EA graduates 2025] · Meta AI auction data 2025-26 (L1/L2, eCPM/CTR/CPI por nodo).
