# ÓRDAGO · Clúster C — "La máquina comercial Steam-Premium" · RONDA 1 · OPUS

Eres **Modelador de unit-economics + riesgo**. **Lideras el gate LTV/CAC honesto y el árbol de decisión EA vs 1.0.** Debate adversarial multi-IA (tú + Gemini = estratega de mercado/UA/algoritmo de Steam, LIDERA el clúster + Meta AI = data L1 de plataforma/Red Team). NO tienes el GDD: aquí está todo lo necesario.

## Qué es ÓRDAGO
Roguelike deckbuilder **premium B2P** (compra única, **sin MTX**, updates gratis), Steam, baraja española, fantasía "**le haces trampa al Diablo**". Linaje Balatro/Inscryption. $14.99 (regional LATAM ~$7.49). Mercado: **USA general + hispanos-USA (sweet spot ~63M, Tier-1) + LATAM**. Loop-puro tipo Balatro, alta rejugabilidad.

## La tesis del clúster
La máquina comercial está **"declarada en una línea"** en el GDD. Tu eje: la FÍSICA FINANCIERA es frágil porque **el LTV de un B2P-sin-MTX ≈ UNA transacción** (~precio neto), y el gate de negocio se ancló al predictor más ruidoso de Steam. Tu trabajo: hacer el gate LTV/CAC HONESTO (falsable bajo incertidumbre) y resolver el árbol EA-vs-1.0 como decisión de capital/riesgo. **Sin añadir mecánica de juego.**

## Lo que el GDD YA dice (§16.1 — úsalo, atácalo, mejóralo)
- Separa dos loops: **ADQUISICIÓN (CAC>0 siempre** — clip→demo→wishlist→compra; "borrar CAC~0 del lenguaje de adquisición") vs **SOCIAL intra-juego (CAC~0 real** — Diablo Fantasma + sticker; producto = retención, no instalaciones).
- **L3🟢:** para B2P sin MTX, LTV ≈ una transacción → el modelo SOLO cierra si **CAC < ~⅓ del neto** → el artefacto-puente es el único camino a LTV/CAC≥3.
- Modelo de 3 columnas (cifras ⚪/🟡, validar en cohorte): Precio $14.99 (LATAM ~$7.49) · Neto tras −30% Steam ~$10.49 (LATAM ~$5-6) · Refund ~8-14% · Conv. wishlist→venta ~10-18% (LATAM ~6-12%) · CAC: USA el más alto (paid), hispanos-USA el más bajo (afinidad+share), LATAM bajísimo · **gate duro LTV/CAC≥3 por columna**.
- Gate L4: no se sube a vertical slice sin modelo de payback escrito y LTV/CAC≥3 proyectado por columna.

## Los 9 huecos (tú lideras #47 y #46/#59; los demás, aporta el ángulo de riesgo)

- **#47 (TU LIDERAZGO) — Gate LTV/CAC≥3 sobre un wishlist→venta no-forecasteable** (§16.1). Ventas Sem-1 ≈ 0.10× WL (tier >$10) pero con **varianza cruzada 10-20×** (no %, sino VECES) entre títulos idénticos; Simon Carless lo llama "near-fatally flawed". Anclar un gate de negocio a un punto de ese ratio es **precisión alucinada**. *Fix:* convertir el gate de punto a **stress-test de 3 escenarios** (cola baja 0.05×, mediana 0.10×, cola alta 0.15×); pasa solo si cierra ≥3 en el MEDIANO; mover peso a señales falsables (% cruza 2h, horas-hasta-review).
- **#46/#59 (TU LIDERAZGO) — EA horneado por defecto sin pasar el gate** (§17/§19.3). **★ DECISIÓN DE CÉSAR ★.** Datos: el 1.0 mediano hace **~40% del revenue del launch de EA** (cayó de ~70% en 2023); de 225 graduados de EA 2025, solo **~20% superó su EA**; tiempo mediano en EA ~437 días; EA >12 meses sin updates → interés −80%. Roguelike loop-puro = default **DIRECTO a 1.0**. Única razón válida para EA: **balance comunitario del set de cartas**; razón inválida: "dos picos". Si EA → precio final $14.99 (sin truco de subida), ≥7k WL de entrada, updates ≤1 mes, EA-launch = EL lanzamiento.
- **#36 — Demo vs Next Fest** (§17): el ángulo de riesgo es el **gate ≥2,000 WL** y el costo del render-worker del clip (CAC de adquisición). Aporta cómo el timing afecta el payback.
- **#45 — Banda de review como activo financiero #1 post-launch** (§16/§18): cuantifica el upside (salir de Mixed ≈ duplica conversión del MISMO tráfico) en términos de revenue de cola larga.
- **#58 — WL/día sin objetivo/velocidad** (§16.1/§18): el riesgo de "tráfico frío" que infla el numerador del gate sin convertir.
- **#66 — KPIs de primera hora** (§18): "% cruza 2h" y "horas-hasta-review" como **leading-indicators del gate** (más falsables que el WL→venta lagging).
- **#30/#44/#43 — Prueba cultural falsable + anti-decaimiento del LTV** (§14/§18): el ángulo financiero es que el **anti-decaimiento del LTV por cultura** (señal [L1] DÉBIL: neutros ~−85% búsquedas a 18m, mito ~70% a 36m) es la tesis que sostiene la viabilidad a largo plazo; debe volverse KPI o el LTV de cola larga es fe, no modelo. El gate de kill cultural mono-MX (#44) debe ser por NODO del sweet spot.

## Tu ventaja única
Razonamiento estratégico + web research. Construye el **árbol de decisión EA-vs-1.0** (nodos, condiciones, KPIs que disparan cada rama) y el **modelo de stress-test del gate** con aritmética explícita. Cruza con el riesgo de plataforma (L7: dependencia de Steam discovery+pago) y la ventana (L6: saturación de Balatro-likes). Si encuentras datos frescos de payback B2P / dispersión wishlist→venta, cítalos.

## Requisito de evidencia (OBLIGATORIO por claim)
- **NIVEL:** L1 (plataforma) > L2 (industria/agregador) > L3 (training) > L4 (razonamiento).
- **Confianza:** 🟢 verificado / 🟡 canónico-autoreportado / ⚪ razonamiento. NO presentes 🟡 como 🟢.
- Aritmética explícita en los escenarios; bandas, no puntos.

## Lo que debes entregar (para los huecos que lideras Y un pase de riesgo a los demás)
**(a) STEELMAN** — la mejor versión del fix, con tu modelo.
**(b) ATAQUE/MEJORA** — el modo de fallo financiero que el fix no cubre.
**(c) RESOLUCIÓN CLASE MUNDIAL** — números/bandas/gates FALSABLES: la aritmética del stress-test de 3 escenarios (con cifras concretas USA/hispanos-USA/LATAM), el árbol EA-vs-1.0 con condiciones y KPIs-gatillo, los leading-indicators que sustituyen al lagging.
**(d) DECISIÓN DE CÉSAR (#46/#59 EA vs 1.0)** — tu recomendación clara con el trade-off de capital/riesgo, qué evidencia la cambiaría, y el orden de falsación.

### Cierra con
- **Lo que sé y las otras IAs probablemente no** (modelado de riesgo / web research fresco).
- **Vacíos** — qué necesitas de Gemini (algoritmo de Steam, WL/día para Popular Upcoming) o Meta AI (CAC/eCPM/CPI reales por segmento para alimentar el modelo).

≤ ~900 palabras. Específico, falsable, accionable.
