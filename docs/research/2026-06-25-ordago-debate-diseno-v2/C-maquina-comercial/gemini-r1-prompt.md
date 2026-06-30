# ÓRDAGO · Clúster C — "La máquina comercial Steam-Premium" · RONDA 1 · GEMINI

Eres **Estratega de mercado/UA + experto en el algoritmo de descubrimiento de Steam** (wishlists, Next Fest, velocity, tags, banda de review). **LIDERAS este clúster.** Debate adversarial multi-IA (tú + Opus = unit-economics/riesgo + Meta AI = data L1 de plataforma/Red Team). NO tienes el GDD: aquí está todo lo necesario.

## Qué es ÓRDAGO
Roguelike deckbuilder **premium B2P** (compra única, **sin MTX**, updates gratis) para Steam, con baraja española y la fantasía "**le haces trampa al Diablo**". Linaje Balatro/Inscryption. Precio $14.99 (regional LATAM ~$7.49). Mercado: **USA general + hispanos-USA (sweet spot ~63M, Tier-1) + LATAM**. Distribución por artefacto-puente (clip → demo web → wishlist) + identidad latina como gancho. Es un loop-puro tipo Balatro.

## La tesis del clúster
El GDD tiene la máquina comercial **"declarada en una línea"**: el roadmap (§17) nombra 5 fases sin disciplina, los unit-economics (§16.1) dan un gate LTV/CAC≥3 pero sin proceso, los KPIs (§18) no cubren la primera hora ni la velocidad de wishlists. **Tu misión: convertir el playbook de Steam premium en DISCIPLINA falsable de calendario/proceso/KPI, SIN añadir mecánica de juego.**

## Los 9 huecos (resumen, § del GDD, por qué NO es clase mundial, fix propuesto)

1. **#36 — Demo y Next Fest fundidos en la misma fase** (§17/§14). El GDD dice "Demo de Next Fest" como un solo hito. Antipatrón #1: lanzar la demo el día del fest pierde **~2.5× wishlists** (vs lanzarla 2-3 meses antes) y el tiempo para cruzar el **gate de entrada ≥2,000 WL**. Además 68-88% de las WL del fest vienen de **no-jugadores** de la demo → la store page debe convertir sin demo. Y **NO retirar la demo post-fest** (captura ~40% de creators tardíos, sostiene search velocity). *Fix:* demo viva 2-3 meses ANTES → fest → demo PERMANENTE.

2. **#45 — Banda de review como motor de ingreso post-launch: ausente** (§16/§18). En B2P-sin-MTX la banda (Mixed→Very+) es la **palanca #1 de ingreso post-launch**; "salir de Mixed (<70%)" no aparece como objetivo ni KPI. *Fix:* §16.2 nueva, banda como KPI financiero #1; cablear "horas-hasta-1ª-review" + "% cruza 2h" como leading-indicators.

3. **#46/#59 — Early Access horneado por defecto sin pasar el gate** (§17/§19.3). Roguelike loop-puro tipo Balatro: el default debería ser **DIRECTO a 1.0**; EA "para tener dos picos" es antipatrón (el 1.0 mediano hace solo ~40% del revenue del launch de EA; solo ~20% de graduados superan su EA). Única condición válida para EA: balance comunitario del set. **★ ESTA ES LA DECISIÓN DE CÉSAR (EA vs 1.0) ★.** *Fix:* default = directo a 1.0 ($14.99, −20% launch week); rama EA opcional con gatillo único.

4. **#47 — Gate LTV/CAC≥3 anclado a un wishlist→venta no-forecasteable** (§16.1). El gate de negocio se construyó sobre el predictor MÁS débil de Steam: ventas Sem-1 ≈ 0.10× WL pero con **varianza cruzada 10-20×** ("near-fatally flawed"). *Fix:* convertir el gate de punto a **stress-test de 3 escenarios** (cola baja 0.05×, mediana 0.10×, cola alta 0.15×); pasa solo si cierra ≥3 en el MEDIANO. (Lo lidera Opus; tú aportas los ratios de plataforma.)

5. **#58 — Wishlists como % de conversión, sin objetivo/velocidad/run-up** (§16.1/§18). Falta **WL/día** (la pendiente alimenta el Personal Calendar y el run-up de 30 días → Popular Upcoming), falta objetivo con banda, falta el antipatrón explícito "comprar tráfico frío". *Fix:* WL/día como KPI vivo; proteger run-up de 30d (demo viva + tags exactos del vecindario).

6. **#66 — Faltan los 2 KPIs núcleo de la primera hora** (§18). "% que cruza 2h" (ligado a la ventana de reembolso) y "horas-hasta-1ª-review" como leading-indicators. *Fix:* bloque §18 "Gate de la primera hora".

7. **#30 — La prueba cultural quita-el-símbolo se degradó a no-falsable** (§14). El 5º criterio del GDD dice "si OFF reenvía igual → el foso vive en el VERBO, recargar identidad en audio" = racionalización auto-confirmante; el foso cultural debe poder MORIR. *Fix:* gate binario **simétrico** (reenvío ON>OFF por nodo Y retención-de-búsqueda ON>OFF a 90d).

8. **#44 — El gate de kill cultural es mono-nodo MX** (§14/§17). El gate que autoriza gasto se instrumenta solo en "20 grupos familiares MX", pero el sweet spot hispano-USA NO es México (incluye dominicanos/cubanos/salvadoreños; un mito solo-MX aliena ~2/3). *Fix:* **gate de reconocimiento <1s ≥70% por NODO** del sweet spot (MX, caribeño-US, centroamericano-US) ANTES de escalar UA hispano-USA.

9. **#43 — El anti-decaimiento del LTV por cultura nunca se vuelve KPI** (§18/§16.1). La tesis comercial (cultura=foso) descansa en que el mito evita el decaimiento del LTV (señal [L1] auto-reportada: neutros pierden ~85% de búsquedas a 18m, mito retiene ~70% a 36m — DÉBIL). *Fix:* extender el A/B mito-ON/OFF a un readout de retención-de-búsqueda en el tiempo.

## Datos de plataforma que el GDD ya asume (úsalos, refínalos o refútalos)
- Ventas Sem-1 ≈ 0.10× WL (tier >$10), varianza 10-20×; Personal Calendar (oct-2025) → run-up de 30d.
- Demo ANTES del fest ≈ 2.5×; ≥2,000 WL de entrada; 68-88% de WL del fest son no-jugadores; mantener demo post-fest = +35% search velocity 🟡.
- Banda de review: salir de Mixed duplica conversión; **NO hay gate algorítmico** a 10 ni a 50 reviews (correlación vía RPI, no causalidad). Review-bombing LATAM ~60% por pricing/localización.
- EA→1.0: 1.0 ≈ 40% del revenue de EA; ~20% superan su EA; ≥7k WL para EA, updates ≤1 mes.

## Tu ventaja única
Lidera con datos de **Search Trends / YouTube SEO long-tail / segunda pantalla** y el **algoritmo de descubrimiento de Steam** (Personal Calendar, Popular Upcoming, search velocity, tag neighborhoods, Discovery Queue). ¿Qué WL/día se necesita para entrar a Popular Upcoming? ¿Cómo se mide Search Velocity como centinela pre-launch? ¿Qué tags del vecindario deckbuilder maximizan el match del Personal Calendar?

## Requisito de evidencia (OBLIGATORIO por claim)
- **NIVEL:** L1 (dato de plataforma) > L2 (industria/agregador) > L3 (training) > L4 (razonamiento).
- **Confianza:** 🟢 verificado / 🟡 canónico-autoreportado / ⚪ razonamiento. NO presentes 🟡 como 🟢.
- Cada hallazgo con números/rangos/bandas concretas. "Convierte bien" NO es aceptable.

## Lo que debes entregar (para CADA uno de los 9 huecos)
**(a) STEELMAN** — la mejor versión del fix propuesto, con tu dato de plataforma.
**(b) ATAQUE/MEJORA** — dónde el fix está flojo, mal calibrado o tiene un mejor diseño.
**(c) RESOLUCIÓN CLASE MUNDIAL** — números/bandas/gates FALSABLES: calendario exacto (semanas antes del fest, días de run-up), umbrales (WL totales, WL/día, % que cruza 2h, horas-hasta-review, banda de review objetivo), criterios de kill por nodo. Que César pueda ejecutarlos como checklist.
**(d) DECISIÓN DE CÉSAR (#46/#59 EA vs 1.0)** — marca claramente tu recomendación con el trade-off real, las condiciones que dispararían cada rama y los KPIs que la deciden.

### Cierra con
- **Lo que sé y las otras IAs probablemente no** (algoritmo de Steam / Search / long-tail).
- **Vacíos** — qué necesitas de Opus (unit-economics/escenarios) o Meta AI (eCPM/CPI por segmento, creativos, review-bombing real).

≤ ~900 palabras. Específico, falsable, accionable.
