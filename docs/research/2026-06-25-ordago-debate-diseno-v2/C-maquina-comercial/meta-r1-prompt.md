# ÓRDAGO · Clúster C — "La máquina comercial Steam-Premium" · RONDA 1 · META AI

Eres el **analista con data L1 de plataforma** (Meta Ads / Instagram / WhatsApp / Facebook) + **Red Team**. Aportas benchmarks reales por segmento y **atacas los supuestos optimistas**. Debate adversarial multi-IA (tú + Gemini = estratega de mercado/algoritmo de Steam, LIDERA el clúster + Opus = unit-economics/riesgo). NO tienes el GDD: aquí está todo lo necesario.

## Qué es ÓRDAGO
Roguelike deckbuilder **premium B2P** (compra única, **sin MTX**, updates gratis), Steam, baraja española, fantasía "**le haces trampa al Diablo**". Linaje Balatro/Inscryption. $14.99 (regional LATAM ~$7.49). Mercado: **USA general (Tier-1, eCPM ~$15-28) + hispanos-USA (sweet spot ~63M, Tier-1) + LATAM (eCPM ~$1-2 pero CPI bajísimo)**. Distribución: clip → demo web móvil (deep-link WhatsApp) → wishlist Steam → compra. Identidad latina como gancho de CTR.

## La tesis del clúster
El GDD declaró la máquina comercial "en una línea". Las otras IAs proponen calendario/gates/modelos financieros con números **auto-reportados u optimistas**. **Tu doble misión: (1) aportar los benchmarks REALES de plataforma que solo tú tienes (eCPM/CPI/CTR por segmento, creativos que convierten, fatiga creativa, review-bombing LATAM real), y (2) Red Team: atacar cada supuesto optimista con datos.**

## Los 9 huecos (resumen + dónde tu data L1 y tu ataque importan más)

1. **#36 — Demo vs Next Fest** (§17). Se asume demo móvil web (deep-link WhatsApp) como motor de wishlists. **Tu data:** ¿tasa real de apertura de deep-links de WhatsApp en MX/CO? ¿cuánta sesión LATAM es muda (autoplay bloqueado)? ¿el clip de 6-8s realmente convierte a wishlist Steam desde móvil, o el salto móvil→Steam-PC rompe el funnel? **Red Team:** el "2.5× wishlists demo-antes-del-fest" y "68-88% no-jugadores" son 🟡 auto-reportados — ¿qué ves tú?

2. **#45 — Banda de review como motor de ingreso** (§16/§18). **Tu data:** el lift de banda (Mixed→Very+) por mercado; ¿la curva mesetea tras ~49 reviews? **Tu ataque clave:** **review-bombing LATAM** — confirmaste antes que **~60% de negativas tempranas en LATAM vienen de pricing regional mal puesto / falta de localización al español**, no de bugs. Cuantifícalo.

3. **#46/#59 — EA vs 1.0** (§17/§19.3). **★ DECISIÓN DE CÉSAR ★.** Tu data sobre tasas EA→1.0 es limitada (fuera de tu plataforma); di honestamente qué NO puedes aportar y dónde te alineas. Red Team: ¿el público hispano/LATAM percibe "Early Access" distinto (desconfianza a juego incompleto)?

4. **#47 — Gate LTV/CAC≥3 sobre wishlist→venta ruidoso** (§16.1). **Tu data crítica para el modelo de Opus:** **CPI/eCPM/CTR REALES por segmento** (USA general, hispanos-USA, LATAM) en 2025-26 para alimentar el CAC del gate. **Tu ataque:** ¿el "CAC bajísimo orgánico LATAM" es realista, o el funnel móvil→Steam-PC lo encarece? ¿el sweet spot hispano-USA tiene de verdad el CAC más bajo?

5. **#58 — WL/día sin objetivo/velocidad** (§16.1/§18). **Tu data:** qué creativos/formatos generan velocidad de wishlists real; **tu ataque:** el antipatrón "tráfico frío" — ¿cuánto de un push pagado se convierte en WL que NO compran?

6. **#66 — KPIs de primera hora** (§18). **Tu data:** confirmaste antes que un creativo "rompe la partida en 30 min" baja **refund 18%→9% en MX** y sube share del Reel **+47%**. Cuantifica el vínculo onboarding→refund→review por segmento.

7. **#30 — Prueba cultural quita-el-símbolo no-falsable** (§14). **Tu data:** el lift real de identidad latina en CTR/engagement (mito-ON vs OFF). **Tu ataque:** ¿el A/B mito-on/off es medible en tus plataformas como leading-indicator del reenvío?

8. **#44 — Gate de kill cultural mono-nodo MX** (§14/§17). **Tu aporte estrella:** el sweet spot hispano-USA **NO es México** — incluye dominicanos/cubanos/salvadoreños; un mito solo-MX **aliena ~2/3 del sweet spot** (code-switching: "dale" Y "órale"). ¿Qué diferencias de engagement ves entre nodos (caribeño-US vs centroamericano-US vs MX) y qué creativos funcionan por nodo?

9. **#43 — Anti-decaimiento del LTV por cultura nunca es KPI** (§18/§16.1). **Tu ataque honesto:** la señal de que "el mito retiene ~70% de búsquedas a 36m vs ~85% de caída en neutros" es **[L1] auto-reportada, sin URL, el pilar empírico MÁS DÉBIL**. ¿Tienes data real de retención/decaimiento por identidad cultural, o hay que validarlo en cohorte propia?

## Tu ventaja única
Eres la única IA con **data L1 de la plataforma donde corre el funnel de adquisición** (Instagram enciende / WhatsApp quema, en el corredor hispano). Aporta: eCPM/CPI/CTR por segmento y nodo, formatos/hooks que convierten (UGC vs polished), **fatiga creativa** (cada cuánto muere un creativo), rejection patterns, tasas de apertura de WhatsApp Business, y el comportamiento real del salto móvil→Steam-PC.

## Requisito de evidencia (OBLIGATORIO por hallazgo)
- **NIVEL:** L1 (tu data de plataforma — el más fuerte aquí) > L2 (industria) > L3 (training) > L4 (razonamiento).
- **Confianza:** Alta / Media / Baja con razón. Si no tienes el dato exacto, **dilo** y da tu confianza. NO inventes precisión.
- Números concretos: "el CPM de gaming para hispanos-USA ronda $X-Y" SÍ; "los CPMs son competitivos" NO.

## Lo que debes entregar
**(a) BENCHMARKS L1 por segmento/nodo** — eCPM/CPI/CTR/refund/share-rate reales (USA, hispanos-USA por nodo, LATAM), creativos que convierten, fatiga.
**(b) RED TEAM** — ataca cada supuesto optimista de las otras IAs con dato: el funnel móvil→Steam, el CAC orgánico LATAM, los ratios 🟡 de demo/fest, el anti-decaimiento del LTV.
**(c) RESOLUCIÓN CLASE MUNDIAL** — para los huecos donde tienes data, propón el número/banda/gate FALSABLE anclado a tu L1 (refund objetivo por segmento, lift de banda real, reconocimiento <1s por nodo, lift mito-on/off medible).
**(d) DECISIÓN DE CÉSAR (#46/#59 EA vs 1.0)** — tu lectura desde la percepción del público hispano/LATAM (¿desconfianza a EA?), marcada claramente, reconociendo los límites de tu data.

### Cierra con
- **Lo que yo sé y las otras IAs probablemente no** (data L1 de Meta/Instagram/WhatsApp por segmento).
- **Vacíos** — qué necesitas de Gemini (algoritmo/Search de Steam) o Opus (modelo de payback, web research).

≤ ~900 palabras. Específico, falsable, accionable. Ataca con datos, no con opiniones.
