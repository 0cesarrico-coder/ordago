# META-SÍNTESIS v1.3 — ÓRDAGO · Fusión de 7 debates multi-IA

> **Rol:** Meta-sintetizador estratégico. Funde las 7 síntesis de clúster (A–G) tras R1→R2→referee (Opus + Gemini 3.5 Flash + Meta AI L1) en UN plan priorizado para el GDD v1.3, resolviendo conflictos cruzados.
> **Estado de referee por clúster (fiel a cada fuente):** A, B, C, D, E, G = **CONVERGED**; **F = CONVERGING** (gerundio; consensus=9, contested=4, flipped=2 — no se sobre-afirma a CONVERGED). No todas son CONVERGED.
> **Caveats metodológicos heredados de las fuentes (no minimizar):** (1) **Clúster E fue el de más concesiones** — 6 flips, todos hacia el realismo móvil de Meta AI; sus consensos son flips-a-consenso, legítimos pero nacidos de cesión, no de acuerdo inicial. (2) **Clúster D lleva una "nota de integridad"**: en ese debate ambos asientos "Opus" y "Meta" fueron desempeñados por el mismo operador; sus marcas CONSENSO 3/3 se heredan tal cual la fuente las asumió, con esa salvedad de confianza.
> **Fuentes:** `A-foso-legible/SINTESIS-A.md`, `B-artefacto-puente/SINTESIS-B.md`, `C-maquina-comercial/SINTESIS-C.md`, `D-audio/SINTESIS-D.md`, `E-coherencia/SINTESIS-E.md`, `F-awe/SINTESIS-F.md`, `G-etica/SINTESIS-G.md`.
> **Regla de fidelidad:** No se inventa consenso donde una síntesis marca CONTESTADO; no se cambian números reportados; cada fix cita su clúster; ⚪ razonamiento NO se sube a 🟢.

---

## 1. Resumen ejecutivo

Este ciclo entregó **7 síntesis convergidas** que, leídas juntas, exponen **un único patrón dominante**: la v1.2 **prometía máquinas que no cableaba** — un "foso legible", un "artefacto-puente viral", un "audio de orden superior", un "money-shot renovable", una "ética en código" — pero las dejaba como aspiraciones sin gate falsable. **v1.3 las cablea**: cada máquina se convierte en (a) un invariante con umbral V/🟡/KILL numérico, (b) un linter/test que falla el build, o (c) un experimento pre-comprometido cuyo VERDE lo fija el dato medido, no el debate. El segundo patrón transversal: **mute=default 85–90% del feed LATAM** (data L1 Meta repetida en B, D, F) obliga a una doctrina rectora única — **visual-primario, audio/awe-amplificador** — y a que **el output retrospectivo y autocontenido** (no el input prospectivo, no el click) sea el portador de todo: legibilidad del foso, golpe relacional del sticker, estado de juego.

**Las 3–4 palancas mayores:**
1. **El foso vive en el OUTPUT retrospectivo, no en el input** (A): cero tells prospectivos; legibilidad como eco post-captura gateado por maestría; solver §14.0 con pasos S4–S7 que matan la dominancia de Maña y validan el escalado del umbral del Diablo ANTES de un píxel.
2. **El sticker autocontenido es el puente primario; el clip es encendedor** (B+D+F): porque el click <5% en chat familiar mata todo deep-link en el sticker. El artefacto-puente entrega el chisme relacional SIN requerir click; el clip carga el deep-link en Reels/IG.
3. **1.0 directo a Steam, orgánico-primario** (C): NO es un negocio de UA pago a wishlist; LTV B2P es casi constante (~$9.3 USA·hispanos / ~$4.7 LATAM), la única variable viva es el CAC. 1.0 directo es consenso 3/3 triangulado por 3 caminos.
4. **Ética y carga cognitiva en código, no en buena intención** (G+E): veto goodwill bloqueante en CI, gobernador anti-spam que bloquea (no alerta), techo `audio_layers_active ≤ 2`, `reglas_verbalizadas ≤ 5`, serialización Z3 — todo como invariante de compilación/release.

---

## 2. Plan priorizado de fixes para v1.3

> Leyenda: Consenso = **3/3** (las 3 IAs convergieron) · **Contestado** (sigue abierto → decisión de César o experimento). Confianza: 🟢 evidencia fuerte/L1-L2 · 🟡 diseño/L3 · ⚪ razonamiento/supuesto sin baseline. §GDD = sección a editar. Fixes agrupados por § para edición limpia.

### 🔴 P1 — Invariantes y máquinas que se cablean ANTES de cualquier arte/píxel

| # | Fix | Clúster | §GDD | Cambio concreto (criterio falsable) | Consenso | Conf. |
|---|-----|---------|------|--------------------------------------|----------|-------|
| P1-1 | Solver S4 — dominancia de Maña | A (#1) | §14.0 | 100 tableros/seed × builds extremas (0F/3P,3F/0P,2/1,1/2): 🟢 ninguna build >55% winrate y Sharpe <1.3× la 2ª; 🟡 55–60%; **🔴 KILL >60% o Sharpe >1.5×**. Medir **acoplado a S5**. | 3/3 | 🟡 |
| P1-2 | Solver S5 — escalado umbral del Diablo | A (#50) | §14.0 | Mediana `score_logrado/umbral` por banda ∈ **[0.95,1.15]**, p10>0.8, p90<1.6 = 🟢; [0.85,1.25]=🟡; **🔴 KILL si >25% seeds ratio<0.7 (muralla) o >25% ratio>2.0 (trivial)**. | 3/3 | 🟡 |
| P1-3 | Solver S6 — composabilidad/working-set | A (#6/#3), E (#6/#3) | §14.0 | Working-set en mano-pico verbalizado por tester naïve: 🟢 ≤6 reglas y ninguna Fullería en >70% builds óptimas; **🔴 KILL >7 reglas working-set o una Fullería en >85% builds** (trade-off colapsado). | 3/3 | 🟡 |
| P1-4 | Solver S7 — 2 perfiles FTUE/Maestría | A (#8) | §14.0 | FTUE = ≥1 dominante-tempo legítima, spread <8%; Maestría = ≥2 Pareto en banda. **KILL si FTUE tiene 2 Pareto turno-1 o Maestría tiene 1 dominante.** | 3/3 | 🟡 |
| P1-5 | Techo de maestría vía proxy de bots | A (#53) | §14.0 | Delta `bot_lookahead_k − bot_greedy_1ply` por banda: 🟢 crece monótono con k; **🔴 KILL si se aplana a k≥2**. Gate pre-launch; p50/p95 humanos solo post-launch. | Contestado→resuelto (proxy bots, no humanos) | 🟡 [L3] |
| P1-6 | Complementariedad Pacto↔Fullería | E (#6) | §14.0 | Solver: existe ≥1 estado de Mesa con EV(Pacto)>EV(Fullería); viabilidad Pacto ∈ [20%,50%]; Fullería no domina >85% sobre 1000 seeds. | 3/3 | 🟢 |
| P1-7 | Tells = predicado, no sujeto | A (#2,#35) | §11/§UI | Regla dura: **cero coloreado de cartas candidatas, cero iconos prospectivos de eje, cero hover/halo Pareto**. Mesa limpia salvo resaltar sumas de 15. Glance valida **score, no decisión**. | 3/3 | 🟢 [L4] |
| P1-8 | Jerarquía Z como scheduler | E (#5) | §10.2 | `Z1 silueta > Z2 valor > Z3 estado > Z4 cascada`; dos eventos Z3+ NUNCA comparten frame: `Δt(Z3a,Z3b) ≥ 300ms` (log verificable). | 3/3 | 🟢 |
| P1-9 | Gate Z peor-caso | E (#5) | §11/§14 | Trampa+Sospecha+cascada T3 @100×100px grises+deuteranopia: silueta+valor por **≥9/10** Y `≤1 Z3+/frame`. Filtro L1: Moto G 2022 **≥55 fps, bounce <35% @60s, ≤100 render, ≤3 animados**. MUERE si falla. | 3/3 | 🟢 |
| P1-10 | Emisor audio simétrico no-nullable | D (#67) | §Accesibilidad/§Arq-audio | `emitStateCue(visual, audio)` con `visual` **no-nullable**; lint `no_bare_audio_emit`; test `mute_total` corre suite con master=0, **100% eventos producen cambio visual** o falla build (binario). | 3/3 | 🟢 (WCAG 1.3.3 + Xbox XAG 103) |
| P1-11 | Doctrina `state_is_visual_complete` | D (#32) | §Audio-de-estado | El oracle `mute_total` pasa al 100% ANTES de que cualquier capa de audio de estado entre a producción. Juego 100% legible en silencio primero. | 3/3 | 🟢 |
| P1-12 | Veto goodwill bloqueante en CI | G (#42) | §4.1 / §proceso-CI | Toda feature retorno/share/social lleva `goodwill: deposit\|withdraw\|neutral`. **M1 VETA, nunca AUTORIZA**; prohibido "el saldo aguanta". `withdraw` no mergea sin `deposit` compensatorio o veto de César. Build **Unstable** si `share rivalidad/reciprocidad >3.5` o `block-rate >1.5%`; auto-rollback. | 3/3 | 🟢 |
| P1-13 | Gobernador anti-spam en código | G (#37) | §18 | Centinela **bloquea, no alerta**: máx **2 envíos/contacto/semana**; el 3.º auto-bloqueado sin respuesta previa. **Build no shippea si block/mute ≥1.5% o report-spam ≥0.3%**. Si K sube pero el grafo se silencia → vetar la variante. | 3/3 | 🟢 [L1] |
| P1-14 | Money-shot = motor único + slot | F (#28/#29) | §10.2 | "Presentador de Asombro" = 1 motor scriptado (mano+mesa+sombra-Diablo+cámara pull-back), slot intercambiable. **Casta A = ~5 money-shots FULL (jefes); Casta B = ~15 dosis ligeras** (PNG+SFX 0.3–0.4s+tipografía, sin re-render). **Cap duro G3: ≤0.8 días-hombre/dosis** o degradar A→B. | 3/3 | 🟢 |

### 🟡 P2 — Especificaciones de producto con gate falsable (construir el medidor / experimento pre-comprometido)

| # | Fix | Clúster | §GDD | Cambio concreto (criterio falsable) | Consenso | Conf. |
|---|-----|---------|------|--------------------------------------|----------|-------|
| P2-1 | Kill de legibilidad = vocabulario-ciego | A (#4) | §Test-plan | Eliminar "≥70% nombran eje" (r=0.12 con D30, L1 Meta). Reemplazar por: predicción contrafáctica ≥50% (κ≥0.6) **+** elección Pareto en escenario espejo ≥55% tras 3 runs SIN nombrar el eje. Verbalización = diagnóstico, no kill. | Consenso en QUÉ medir (HACER no DECIR); método resuelto | 🟢 [L1] |
| P2-2 | Capa-1 estado + Capa-2 eco retrospectivo | A (#2) | §UI/§Tells | Capa-1: banner Trampa/función-palo, 4–6 palabras, <450ms. Capa-2: destello 150–200ms + háptico por eje, **gateado tras ≥2 repeticiones de la jugada, desvanece ~run 4** ("memoria muscular, no UI"). Test A1: novato vs experto deben divergir en jugada o KILL. | 3/3 | 🟢 [L4] |
| P2-3 | Banda EV objetivo | A (#EV) | §EV | Dejar como **parámetro a fijar por el solver en [10–15%]** (no hardcodear); bandas R2 solapan [12%,13%]. Documentar: <8% = ajedrez seco; >18% = autorrevela (recrea solver §317). | Contestado→delegado al solver | 🟡 |
| P2-4 | Sticker autocontenido (objeto canónico) | B (#27,#40,#65), E (#39) | §Artefacto-puente | PNG/WebP estático **<80KB, 512×512**, render 100% cliente desde 1ª mano, **0 servidor**; texto relacional ≥40% del área + silueta Diablo centrada; emoji/texto copiable debajo (`ordago.gg/d/<seed> — te gané por 2`). **Autocontenido: entrega el golpe relacional SIN requerir click.** Prioriza IDENTIDAD ("Soy Escobero" + título 2 palabras por entropía de build), oculta solución-de-seed. | 3/3 | 🟢 [L1/L2] |
| P2-5 | Glance-gate del sticker | B (#40), E (#39) | §Gates-de-build | Sticker lee el chisme a **100×100px gris/mudo**: VERDE ≥90% lectura (n≥20), KILL <90%. Generador garantiza **≥8 arquetipos distinguibles/1000 victorias**; share-rate sticker limpio > cargado por **>15%**. | 3/3 | 🟢 [L1] |
| P2-6 | Clip encendedor (estructura fija) | B (#60,#62) | §Clip | WebP animado **6–8s, <300KB, muted+playsinline, loop perfecto**; estructura **Gancho(0–1.5s)→Quiebre(1.5–4s)→Sospecha(4–6s)→Pillado(6–8s)**; 1er frame = Diablo pillándote (legible sin audio, WhatsApp congela 1er frame). Vende el DUELO Trampa↔Fullería, NO combo/ASMR numérico. Motion-gate como **PISO**: ≥70% nombra "¿trampa? ¿quién gana?" @360p mudo 3s. | 3/3 | 🟢 [L1/L2] |
| P2-7 | OG-preview estático | B (#19) | §OG-preview | `og:image` ESTÁTICO 1200×630, **<45–50KB JPEG**, CDN edge MX/BR, `max-age=1yr`, sin JS/SSR-por-seed; TTFB p95 **<80–100ms**. KILL: preview en blanco en validador FB/WA o p95 >120ms. Chisme dinámico va en el TEXTO copiable. | 3/3 en estático | 🟢 [L1] |
| P2-8 | Métrica de ignición K2 | B (#27) | §Métrica-ignición | Medir **activación atribuible (partidas), no reenvíos ni clicks**; umbral provisional bajo **3/100 (Opus) ↔ 0.18 (Meta)** pendiente de experimento L1; reenvíos/partida (VERDE ≥1.8) solo como proxy de ALCANCE. | Consenso en activación; umbral = experimento | 🟡 [L4] |
| P2-9 | WKWebView/autoplay | B (#22), D (#22) | §Demo/§Audio-onboarding | Video **muted+playsinline**; audio se arma en el **1er evento semántico** (jugar 1ª carta / "Desafía al Diablo"), no tap accidental. Demo inicia <1.5s. Linter `no_autoplay_without_gesture` / `first_tap_arms_audio`. Fallback flash+vibración si `play()` falla. | 3/3 | 🟢 [L1] |
| P2-10 | Firma de identidad (audio) | D (#22) | §Audio/Onboarding-demo | Firma 2–3s **inline ≤35KB, precargada en 1er frame**; `AudioContext.resume()` en handler del 1er evento semántico. KPI `firma_heard_first_session` **≥58% Android / ≥38% iOS-MX** (kill <45%/<30%). North-star negocio medido pero no bloqueante. | 3/3 | 🟢 [L1] |
| P2-11 | grito_glifo en sticker | D (#23) | §Viralidad/Stickers | Campo `grito_glifo` **no-null** en `RunDigest` (linter `digest_has_grito_glifo`); gemelo visual onomatopéyico Posada **estampado en el arte** (no sello pegado); **≤2 palabras legibles a 96×96px** (OCR-gate `glifo_ocr_legible`), contraste ≥4.5:1. KPI: reenvío +15%, repetición ≥20% <48h, bloqueo <0.25%. | 3/3 (principio); umbrales 🟡 | 🟢/🟡 |
| P2-12 | Audio de estado (3 capas con techo) | D (#32) | §Audio-de-estado | (1) leitmotiv Trampa loop ≤-18 LUFS; (2) textura Sospecha curva log satura al 80% gain en `suspicion=0.7`, invariante `suspicion_audio_gain ≤ 0.8*master`; (3) 3 firmas resultado ≤1.2–1.5s. **Techo de banda: Sospecha ∉ [500Hz,2kHz]** (no enmascara voz/música). **`audio_layers_active ≤ 2`**. Gate `eyes_closed_test ≥75%` (kill <60%). KPI ético `quit_rate ≤ baseline`; **prohibido medir `Cheating_Success_Rate`**. | 3/3 | 🟢/🟡 |
| P2-13 | text_glyph emoji-artefacto | D (#17) | §Viralidad | `RunDigest.text_glyph` siempre presente copiable (`🃏👹🔥 … ¡ÓRDAGO!`); KPI **separado** `text_glyph_share_rate` ≥4% sem-1; degradar a fallback silencioso si <1.0 jug/10 shares. Nunca se mata (costo ~0). Es red de seguridad (23% sesiones MX sin datos), NO 3er canal. | 3/3 (patrón); umbral ⚪ | 🟢/⚪ |
| P2-14 | Gate #47 — unit-economics en 3 capas | C (#47) | §Modelo-negocio | (1) gate orgánico = ≥60% ventas Sem-1 de WL orgánica-search; (2) paid marginal solo donde CAC_pago ≤ LTV, **LATAM paid-a-wishlist prohibido ($0)**; (3) kill blended LTV/CAC≥3 **O** honesto ≥1.5 hispanos/≥1.2 LATAM. **Lo zanja el CAC/CPWL medido en demo/Next Fest.** Tabla LTV neto-refund (~$9.3/~$4.7), bandas WL→venta bimodales. | Consenso en aritmética; umbral honesto contestado→dato | 🟡 [L2] |
| P2-15 | 1.0 directo + precio | C (#46/#59) | §Estrategia-lanzamiento | **1.0 directo, $14.99 USD / $11.99 launch (−20%)**, regional **$7.49 LATAM** + español 100% día 1 + disclaimer impuestos AR (anti-review-bombing, 58–63% negativas LATAM = precio/idioma). Única rama EA falsable: balance exige >5k jugadores simultáneos ∧ runway <4m → EA táctico ≤6–9m con precio final desde día 1. | 3/3 (triangulado, 🟢 alta) | 🟢 |
| P2-16 | Next Fest timing + retención demo | C (#36,#66) | §Estrategia-lanzamiento/§KPIs | Demo viva **T-12 semanas**; gate de entrada = **velocity +150 WL/día 7d** (no número fijo). Retención: **≥35% juegan >15min**, **≥38% cruzan 2h en 72h** (no 55%). Jugador vive "el momento de la trampa" antes del min 45. Refund <10% MX/<7% hispanos/<6% USA; <3% nota "muy difícil". | 3/3 (umbral a la baja) | 🟡 [L2] |
| P2-17 | Banda de review como activo | C (#45) | §KPIs | Escalón crítico = **Mixed→Mostly Positive (≥70%)**, no Very Positive ≥82%. Lift diferencial: **+22–35% conversión USA / +12–18% LATAM**. Primeras 10 reviews se deciden en **primeras 4h** → soporte 24/7 Discord sem-1. | 3/3 (magnitud a favor Meta L1) | 🟢 [L2] |
| P2-18 | WL velocity > acumulado | C (#58) | §KPIs/§Steam | Reportar **WL/día con fuente y cohorte**, no stock (WL fría infla numerador). Umbral exacto contestado → lo zanja el dato del algoritmo. | 3/3 | 🟡 [L2] |
| P2-19 | Gates culturales medidos | C (#30,#44,#43) | §Identidad-cultural | A/B Mito-ON/OFF: gate **CTR ≥2.4% AND +15%** en hispanos-USA (48h), afecta CTR/velocity no retención D3. Reconocimiento "trampa al diablo con cartas" **<1.2s en ≥70%** en 3 nodos (MX/Miami/Houston) + 3 variantes (MX/Caribe/Centro). Decay búsquedas de marca **<45% a 90d** (degradar "70% a 36m" de hecho a hipótesis-con-KPI). | 3/3 (#30/#44); #43 evidencia ⚪→KPI | 🟡 / ⚪ |
| P2-20 | Tags + funnel Steam | C | §Steam/§Funnel | Tags = **Roguelike Deckbuilder + Rogue-lite + Dark Fantasy + Solitaire** (NO "Card Game"). UA empuja a **buscar el nombre** (search directo pesa 5×). Penalizar cuello móvil→PC (WhatsApp→Steam completion 12–18%); gate >15% completan deep-link o priorizar demo web jugable. | 3/3 | 🟡 [L2] |
| P2-21 | Presupuesto de complejidad (2 denominadores) | E (#6/#3) | §14 | `reglas_core ≤9` (techo scope) **+** `reglas_verbalizadas_por_tester ≤5` (techo onboarding, **gana en conflicto**). Tester verbaliza antes de Manga 1; si nombra sistema meta (Codex/Romancero/puente/Diablo Fantasma) → entró demasiado pronto. Conservación: +1 delivery ⇒ −1 carga core. Compresión-arquetipo = REQUISITO (1 frase cultural/regla o cuenta doble). `C = reglas × canales ≤12/mano`. D1 ≥35% MX/BR con ≤5 verbalizadas, onboarding ≤180s. | Consenso en 2 denominadores; poda vs serializar contestado | 🟡 |
| P2-22 | Presupuesto temporal de run | E (#48) | §9 | `Σ(12 dientes) ∈ [25,35]min p50; p90 ≤40min`; banda por diente (Manga ~6–8min, Cantina ≤90s). Duración **derivada de Maña**, no pacing libre. Solver §14 sobre 1000 runs. MUERE si p90>40min o Cantina >90s. | 3/3 | 🟢 |
| P2-23 | Hook intra-sesión | E (#49) | §14 | `time_to_first_fullería_jugada` **p50 ≤90s** y `first_meaningful_choice <90s` (Opus 120→90, Gemini 180→90, Meta ancla 90). Banda-muerte >120s. | 3/3 | 🟢 |
| P2-24 | Codex terminal anti-FOMO | E (#24) | §Codex/Romancero | Colección terminable, cardinalidad conocida (`X/N` visible) + beat catarsis 100% **estrictamente estético** (skin/cante), **SIN timer**; máx **2–3 siluetas con pistas activas** (resto en niebla); cada cierre destapa la silueta siguiente (SEEKING, no infinitud). Gates: **D30 ≥8% sin timers**, abandono 80–99% **<5%**. Cardinalidad N pendiente de César. | 3/3 en principio; N ⚪ | 🟢/⚪ |
| P2-25 | Watchability de run | B (#56) | §Watchability | Invariante "≥1 momento transmisible por run" vía detector de pico (reusa exportador). KPI ≥1 clip/30min; KILL 30min sin pico → revisar densidad Trampas/Fullerías. | Consenso blando (Opus eleva) | 🟡 [L4] |
| P2-25b | A/B comercial demo LATAM (validación de tells eco-gateados) | A (§4) | §16/§Test-plan | A/B demo LATAM móvil **n≥5k/rama** (eco-gateado vs sin-tells): pasa si **D7 +≥5pp** (target >28%) **y** share-rate no cae >10% (target ≥1.4/100 sesiones) **y** **refund <8%**. Si sube D7 pero share −≥15% → mataste la suerte compartible → re-evaluar capa de UA. | 3/3 | 🟡 |
| P2-25c | Gates de awe falsables G1/G4/G5/G-conversión | F (§4) | §Gates-QA/§16 | **G1** habituación: share del N-ésimo jefe NO cae monótono vs el 1º (≤15% caída Diablo#10 vs #1). **G4** muerte del sistema: predicción del beat por espectadores ≡ fatiga (frequency >2.7/7d **o** CTR −30% vs baseline → rotar ≤14d). **G5** reacción muda: **≥70% no-jugadores describen "qué pasó increíble" en <5 palabras tras 0.5s mudo** (kill-gate de awe). **G-conversión** (Meta L1): share-to-wishlist **1:0.03–0.04 en frío** (NO 1:0.12 Gemini, inviable premium $14.99); **<0.02 tras 10 creadores → kill beat**. | 3/3 (G1/G4/G5 🟡, G-conv L1) | 🟡 |
| P2-26 | Codex de Arrepentimientos (3 condiciones) | G (#41/#73) | §7.6d + nuevo §9.x | `RegretSituation` SOLO si: (1) Trampa golpea ranura con Pacto; (2) existía en la run una Fullería que rompía esa Trampa; (3) el jugador no la tiene por vender la ranura al Pacto. Muestra la **carta** ~0.5s (*"¿La querías, tahúr?"*), **NUNCA número/EV**. `has_experienced_regret[pact_id]` apaga el susurro **permanente** (terminable). Gate: ≥35% verbaliza "la próxima no lo vendo" [⚪ supuesto] Y `re-run<3s` NO sube >12% Y Codex silencia al completar. Roto cualquiera → kill. | 3/3 | 🟢 (umbral ⚪) |
| P2-27 | Epitafio de derrota | G (#70), E + F | §9 (Catarsis→Derrota) | Beat 2–3s con (a) logro agregado ("Derrotaste 4 Diablos · mejor Escoba 38", **nunca "te faltó 1 punto"**); (b) permiso de parar. **CERO CTA/ad/oferta/ranking por código.** Gate `re-run<3s` **<12% estable**; si sube >15% dos builds → revertir beat. Delay 1.5s = decisión de César. | 3/3 (delay contestado→métrica) | 🟢 |
| P2-28 | Reciprocidad backend (TDF) | G (#16) | §social/§18 | TDF/gift-back **solo backend** para matchmaking silencioso; **prohibido por código** exponer deuda/contador/shaming. Sticker dice "Pasamos la Mano" sin contador. Gate: TDF ≥30% gift-back/72h (🟡 28–34%); <25% revisar; ~0 → bonding no existe. | 3/3 | 🟢 |
| P2-29 | Bucket social ~50 pares reales | G (#15) | §18 | Bucket cerrado **~50 pares del mismo percentil**; Diablo Fantasma poblado por **PAR REAL** (nunca #global ni bot). Sin leaderboard global público; opt-in/cofradía. Si no hay 50 reales → "tu mejor marca", no inventa rivales. Auditar **0 Diablos Fantasma sintéticos**. | 3/3 | 🟢 |
| P2-30 | K_rivalidad ≠ K_reciprocidad | G (#38) | §8.1 / §18 | Separar por segmento: **k-rivalidad 0.45–0.62 vs k-reciprocidad 0.12–0.18** (L1 Meta). Claim "Community" condicionado a **k-reciprocidad ≥0.20 a 4 semanas**; si <0.15 → corregir el claim, no fingirlo. Stickers de "Alma Co-firmada" (humor negro contra el Diablo, no humano nombrado). | 3/3 (dirección); target realista 0.20–0.25 contra Gemini | 🟡 |
| P2-31 | Telemetría de fatiga/saciedad | G (#55) | §18 + gate-release | KPI maestro saciedad `(share_reciprocidad/share_total)×(1−block_rate)`: **>0.25 sano / <0.15 veto**. Ratio para-satisfecho-vs-encadena >1.2 (umbral exacto = César). | 3/3 (dirección) | 🟡 |

### ⚪ P3 — Diferidos, narrativa barata y señales secundarias

| # | Fix | Clúster | §GDD | Cambio concreto | Consenso | Conf. |
|---|-----|---------|------|------------------|----------|-------|
| P3-1 | Diferir SEO-Engine por-seed | B (#57) | §Discovery | Diferir Engine (riesgo thin-content/soft-404 Google 2026). Construir solo: **medidor de Search Velocity** (gate centinela T-14d, ~600–2,500/mes/región a calibrar) + **UNA landing-compendio estática** top-100 seeds (cron diario, $0). | 2/3 (Gemini en minoría) | 🟡 [L3] |
| P3-2 | Diferir Lore-UGC (Romancero) | B (#25) | §Lore | DIFERIDO post-lanzamiento. KPI (lore_share D30–60) no falsable pre-launch; búsqueda se activa por utilidad mecánica, no prosa críptica. | 3/3 | 🟢 |
| P3-3 | Biblia del Mundo (coherencia barata) | E (#26) | §Narrativa | 1 página: **5 hechos canónicos + 3 ambigüedades**; cada Diablo/Trampa/Fullería linkea a 1 hecho/ambigüedad. Flavor reactivo por **arquetipo de victoria** (Limpia-con-Maña vs Sucia-con-Sospecha) = ~32 strings, **NO la matriz 16×24 = 384**. Linkeo = no-contradicción, NO motor de D7. Medir apertura Romancero D7 como señal secundaria (>10% o se poda a texto lineal). | Contestado (Meta disiente del valor-retención)→coherencia barata | 🟡 |
| P3-4 | Tease de mañana | E (#12) | §Retención | Pantalla salida: silueta siguiente Diablo + 1 rumor útil, **opt-in SIN timer**. A/B con gate **D7 lift ≥3pp** vs control o **se poda**. (Gemini ≥12% optimista vs Meta <3pp realista → experimento.) | Contestado (lift)→experimento | 🟡 |
| P3-5 | Awe asíncrono D30+ | F (#68/#69) | §10.2 | KPI = "el clip del veterano convierte espectador", no "veterano asombrado". Lo que convierte = **reacción física del Diablo** (se resquebraja, libera tinta) + limpiado físico de mesa, NO números flotantes. | 3/3 (reencuadre Opus) | 🟡 |
| P3-6 | Separación ASMR vs money-shot | F (#63) | §10.1 vs §10.2 | §10.1 Clip diario ASMR (barrido Escoba, repetible, D1-D7); §10.2 Money-shot raro (awe, espaciado). **Kill #63: money-shot debe ≥3× share-con-audio del diario en 0–72h** (≥4.5% vs ≤1.2%) o se archiva. | 3/3 | 🟢 |

---

## 3. Resolución de CONFLICTOS CRUZADOS entre clústeres

Estas son las tensiones reales que surgen al fusionar clústeres. Cada una se nombra y se resuelve sin contradicción.

### CX-1 · Legibilidad del foso (A) vs carga cognitiva ≤7±2 (E)
**Tensión:** A quiere tells de eje (Tempo/Escala/Defensa) legibles; E impone working-set ≤7 reglas y `reglas_verbalizadas ≤5`, y advierte que +3 iconos estáticos = +120ms/−9% completion.
**Resolución (ya implícita en ambas síntesis, ahora explícita):** **No hay contradicción porque A movió la legibilidad al OUTPUT retrospectivo, no al input.** El tell de eje NO es un icono prospectivo que el jugador deba leer antes de decidir (eso cargaría el working-set y recrearía el solver §317); es un **eco post-captura** (Capa-2: destello+háptico) que aparece **tras ≥2 repeticiones** y **desvanece ~run 4**. Por construcción no suma reglas verbalizadas (es memoria muscular, no UI) ni focos en el frame de decisión. La única capa permanente (Capa-1, banner de estado 4–6 palabras) se audita explícitamente contra el coste de papilla de E (+120ms). **Regla unificada: el foso se paga en el frame de RESULTADO, nunca en el de DECISIÓN; E gobierna el frame de decisión, A gobierna el de resultado.**

### CX-2 · Audio mute-default (D) vs firma sonora/awe sonoro (D+F)
**Tensión:** D establece mute=default 85–90% y doctrina `state_is_visual_complete`; pero D (#22/#23) y F (#28) quieren una firma sonora de identidad y "escala SONORA" como vector de awe.
**Resolución:** **Dos presupuestos de atención opuestos, ya separados en D:** IDENTIDAD (firma+grito, optimizada por *recuerdo* en touchpoints virales) vive en el momento de **gesto/post-victoria** donde el audio SÍ puede armarse (`AudioContext.resume()` en evento semántico); ESTADO (leitmotiv/textura in-game) vive bajo mute y por eso **nunca porta información que no esté también en visual** (gate `mute_total` 100%). El awe sonoro de F es **amplificador post-victoria** (freeze 0.5s, no durante decisión), no portador. **No se contradicen: la firma/awe sonoro es opt-in amplificador en momentos de gesto; el estado es visual-completo siempre.** Invariante que los une: `state_is_visual_complete` (P1-11) gobierna; la firma sonora se mide (`firma_heard_first_session`) pero **no bloquea** comprensión.

### CX-3 · Gobernador anti-spam de G (#37) vs motor de K viral de B (#27)
**Tensión:** B quiere maximizar ignición K2 (partidas atribuibles desde sticker); G impone máx 2 envíos/contacto/semana y veta variantes que suben K si el grafo se silencia.
**Resolución:** **G define el techo dentro del cual B optimiza.** B ya migró de "shares" a **activación atribuible** (no premia el spam de reenvíos), y su propio KILL (#27) es que el sticker no sea autocontenido — exactamente alineado con G, que castiga el envío sin valor. **Regla unificada: K se mide por partidas-iniciadas, NUNCA por volumen de envíos; cualquier ganancia de K que coincida con block/mute ≥1.5% se VETA (G P1-13/P1-12 manda sobre B).** El gobernador no limita el alcance del sticker bueno (autocontenido, reenviado orgánicamente >60%), solo el spam degradante. Coexisten: **k-rivalidad (motor viral de B) ≤ techo del centinela de G**.

### CX-4 · Serialización Z3 100% (E/A) vs solape para "wow" viral (E-Meta) vs money-shot de F
**Tensión:** E (#5) quiere serializar 100% los eventos Z3+ para claridad; Meta pide 1 solape controlado por run (+18–22% CTR Reels); F dispara el money-shot (un evento de máxima saliencia).
**Resolución:** **El money-shot de F NO viola la serialización de E porque se dispara post-victoria (freeze 0.5s), fuera del frame de decisión** — es exactamente el "1 solape Z3 controlado por run" que Meta pide, pero **acotado al momento de catarsis, no durante la jugada**. Así el conflicto se disuelve: la regla `≤1 Z3+/frame` de E aplica al **loop de decisión**; el money-shot vive en el **beat de resultado** donde la saliencia máxima es deseable y no compite con legibilidad. **Queda como decisión de César (E-DC4) solo si se quisiera un solape DENTRO del loop** — el money-shot post-victoria no lo requiere.

### CX-5 · Eco retrospectivo de A (#2) vs Codex de Arrepentimientos de G (#41) — ¿colisión de "feedback post-jugada"?
**Tensión:** ambos ponen información en el momento post-jugada/post-run (A: eco de eje; G: carta sacrificada del arrepentimiento). Riesgo de saturar el frame de resultado.
**Resolución:** **Son neuroquímicas y momentos distintos:** el eco de A es **háptico/destello 150–200ms inmediato a la captura** (maestría, desvanece run 4); el arrepentimiento de G es un **beat diegético de 0.5s con 3 condiciones estrictas** que solo se arma cuando hubo Pacto + Fullería disponible + no comprada (raro por diseño). Comparten el gobierno de la **jerarquía Z** (P1-8): se serializan con `Δt ≥ 300ms` si coincidieran. **Regla unificada: todo feedback post-jugada pasa por el scheduler Z3 (E P1-8); A y G no compiten porque su disparo es condicional y mutuamente excluyente en la mayoría de manos.**

### CX-6 · Money-shot "renovable" de F vs cap de scope / live-ops encubierto (F+C)
**Tensión:** F quiere ~5–20 dosis de awe; C insiste en que ÓRDAGO no paga live-ops y el LTV es casi constante.
**Resolución:** **Ya resuelto dentro de F con el cap G3 (≤0.8 días-hombre/dosis) y la casta-doble.** El awe NO es retención (D30+) sino **munición de evangelización asíncrona** (alineado con C: orgánico-primario, CAC≈0). "1 sprint × 20 = live-ops encubierto → prohibido". **Regla unificada: el money-shot se justifica por share/adquisición (G-conversión 1:0.03–0.04 frío), no por retención; su conteo se ata a evidencia de share (G2 ≥3× diario), no a ambición de contenido.** Esto mantiene a F dentro del modelo orgánico-primario de C.

### CX-7 · Anti-FOMO del Codex (E #24) y de Arrepentimientos (G #41) vs SEEKING renovable (E+F)
**Tensión:** E/G quieren saciedad (colección terminable, susurro que se apaga); E/F quieren wanting renovable.
**Resolución:** **Convergen en "terminal ≠ saciado":** el wanting se renueva por **profundidad** (cada cierre destapa la silueta del siguiente hueco — SEEKING saludable de Panksepp), no por **infinitud con timer**. El Codex de Arrepentimientos es terminable por Pacto (`has_experienced_regret` apaga el susurro), pero el awe de F renueva por **beat conceptual nuevo**, no por más de lo mismo. **Regla unificada: nada se renueva por escasez artificial/timer (premium B2P); todo se renueva por profundidad conceptual revelada.**

### CX-8 · Identidad cultural como CTR/atracción (C #30/#44) vs como retención/LTV (C #43)
**Tensión:** dentro de C, ¿la IP latina mueve adquisición o retención?
**Resolución (ya zanjada en C, 2-vs-1 a favor de CTR):** la IP afecta **CTR/velocity de WL (atracción)**, NO retención D3 (eso lo da la mecánica). La afirmación "70% retención búsquedas a 36m" (#43) es **L4 sin URL → degradada a hipótesis-con-KPI** (decay <45% a 90d). **Regla unificada con A: suerte/identidad en la superficie de marketing (top de funnel, CTR), skill/mecánica en el cuerpo del loop (LTV/D30)** — idéntica a la reconciliación suerte↔skill de A-DC3.

---

## 4. Invariantes nuevos a falsar con el solver/playtest ANTES de un píxel

> Extensiones de §14.0. Todos falsables con solver (1000 runs / 100 tableros/seed) o playtest n≥15–20 humanos, **sin código de producción**. Orden = lo más barato y bloqueante primero.

1. **INV-1 · Dominancia de Maña (S4, A#1):** ninguna build >55% winrate, Sharpe <1.3× la 2ª. KILL >60%/Sharpe>1.5×. Medir acoplado a INV-2.
2. **INV-2 · Escalado del umbral del Diablo (S5, A#50):** mediana `score/umbral` por banda ∈ [0.95,1.15]; KILL >25% seeds ratio<0.7 o >25% ratio>2.0.
3. **INV-3 · Composabilidad de Condena/working-set (S6, A#6+E#6):** ≤6 reglas working-set, ninguna Fullería ("Ojo del Tahúr") en >70% builds óptimas; KILL >7 reglas o Fullería en >85%.
4. **INV-4 · Complementariedad Pacto↔Fullería (E#6):** ≥1 estado de Mesa con EV(Pacto)>EV(Fullería); viabilidad Pacto ∈[20%,50%]; Fullería no domina >85%.
5. **INV-5 · Techo de maestría por proxy de bots (A#53):** delta `lookahead_k − greedy_1ply` crece monótono con k; KILL si se aplana a k≥2.
6. **INV-6 · Banda EV objetivo (A):** EV se fija donde S4–S7 co-pasan, en [10–15%]; <8% ajedrez seco, >18% autorrevela.
7. **INV-7 · Presupuesto temporal (E#48):** `Σ12 dientes ∈ [25,35]min p50, p90 ≤40min`, derivado de Maña.
8. **INV-8 · Hook (E#49):** `time_to_first_fullería p50 ≤90s`.
9. **INV-9 · Carga cognitiva (E#6/#3):** `reglas_verbalizadas ≤5`, `reglas_core ≤9`, `C = reglas×canales ≤12/mano`; D1 ≥35% con ≤5 verbalizadas.
10. **INV-10 · Jerarquía Z / Gate Z (E#5):** `≤1 Z3+/frame`, `Δt≥300ms`; ≥9/10 legibilidad peor-caso @100×100 grises; ≥55fps Moto G, bounce<35%.
11. **INV-11 · Momento-clip por run / watchability (B#56):** ≥1 pico transmisible detectado/run; KILL 30min sin pico.
12. **INV-12 · mute_total binario (D#67):** 100% eventos de estado producen cambio visual con master=0.
13. **INV-13 · eyes_closed_test (D#32):** ≥75% identifica Trampa+resultado sobre base visual (kill <60%).
14. **INV-14 · Codex de Arrepentimientos falsable (G#41):** susurro solo con las 3 condiciones; `re-run<3s` no sube >12%; Codex silencia al completar.
15. **INV-15 · Saciedad / re-run (G#55/#70):** `re-run<3s` <12% estable; ratio para-satisfecho >1.2; KPI saciedad >0.25.
16. **INV-16 · Test del experto / kill de legibilidad (A#4):** novato vs experto divergen en jugada (mismo seed); vocabulario-ciego: predicción contrafáctica ≥50% + elección Pareto ≥55%.

**Primero a falsar por centavos (D-nota + G + A):** test de repetición del grito mudo (D#23/#31) + `eyes_closed_test` (INV-13) + test del experto (INV-16) + solver S4–S7 (INV-1..5). Estos deciden si "foso legible", "audio de orden superior" y "ética terminable" son reales o aspiracionales ANTES de gastar en producción.

---

## 5. DECISIONES DE CÉSAR (consolidadas, deduplicadas)

> Lista única de todos los clústeres. Cada una: recomendación de las IAs + trade-off. Las que el dato/experimento zanja se marcan **[experimento]**; las de apetito/principio **[firma]**.

**Economía y producto (foso/balance):**
1. **Apetito de auto-sabotaje en Pactos (A#1).** (A) emergente: confiar en S4-verde (elegante, riesgo de que una build se cuele) vs (B) acoplado a mano: cada Pacto fuerte lleva auto-sabotaje que una Fullería resuelve (control, presiona S6). **[firma — apetito de riesgo, no data].**
2. **Banda de EV objetivo (A).** Las 3 bandas solapan [12%,13%]; delegado al solver. César fija el número viendo 100 tableros/seed. **[experimento].**
3. **Dial revelar↔ocultar / suerte↔skill (A#DC3).** Opus lo reconcilia como SECUENCIA (suerte en marketing, skill en loop); el **peso** de cada capa es apetito de César. **[firma].**

**Onboarding y carga (coherencia):**
4. **Denominador de onboarding (E#1):** ≤5 reglas podando Pactos del tutorial (Meta, +10pp D1, riesgo "Escoba con skins") vs **tutorial serializado de 7 reglas en 3 micro-mangas** (Opus/Gemini, conserva identidad, gana en mano 3). **Recomendación del panel: serializar.** **[firma].**
5. **Run continuo vs capítulos (E#48-bis):** run continuo premium [25–35]min con auto-save por turno (Gemini, flow Balatro/Inscryption) vs 4 mangas×6–8min con save entre mangas (Meta, sesión fragmentada). **Reconciliación: run continua + auto-save por turno ≈ capítulos sin romper flow.** **[firma].**
6. **Cardinalidad del Codex N/M (E#2):** N=16/M=24 (Gemini, ambición) vs N=12/M=18 (Meta, >12 ítems caen <5% completado móvil, L1🟢) vs abierto (Opus ⚪). Conflicto duro sin resolver por el panel. **[firma, sesgo a Meta por L1].**
7. **Serialización de cascadas (E#4):** serializar 100% Z3+ (Opus/Gemini) vs 1 solape Z3 controlado por run (Meta, +18–22% CTR). **Resuelto en CX-4 para el money-shot; queda abierto solo para solape DENTRO del loop.** **[firma].**
8. **Recompensa del 100% del Codex (E#5):** estrictamente estética (Opus/Gemini, anti-FOMO) vs desbloquea "Diablo Fantasma" como boss mecánico (afecta balance). **[firma].**
9. **Hook 90s vs 120s (E#6):** casi resuelto en 90s; cada 30s = trade-off D1 vs feel/setup. **[firma].**
10. **Biblia del Mundo (E#7):** ¿validar teorías de comunidad en updates o mantener hermética? **[firma].**
11. **Poda de Diablo Fantasma + artefacto-puente del onboarding (E#8):** ¿podarlos del onboarding manteniéndolos como meta gateado? **[firma].**
12. **¿Tease altera el seed de mañana o es cosmético? (E#12).** **[firma + experimento del lift].**

**Comercial (Steam):**
13. **★ EA vs 1.0 → 1.0 DIRECTO ★ (C).** Unánime 3/3, triangulado. Única excepción: balance exige >5k jugadores simultáneos ∧ runway <4m → EA táctico ≤6–9m con precio final desde día 1. **[firma, reco fuerte 1.0].**
14. **★ Precio ★ (C).** $14.99 / $11.99 launch / $7.49 LATAM + español día 1 + disclaimer AR. Si LATAM cae a $4.99 por review-bombing → LTV-LATAM ~$3.0, pasa a 100% motor de volumen (no cruza-subsidia USA). **[firma].**
15. **Umbral honesto del gate LTV/CAC (C#47):** ≥3 blended (Opus) vs ≥1.5 hispanos/≥1.2 LATAM (Meta, ≥3 paid imposible). **Lo zanja el CAC/CPWL medido en demo/Next Fest.** **[experimento].**

**Artefacto-puente (B):**
16. **Beacon stateless vs cero-backend (B#D1, único contestado real de B):** Opus = 1 endpoint stateless (medible) vs Meta = 0 servidor, atribución 100% local en localStorage ("0 servidor" como moat vs medibilidad). **[firma — principio de arquitectura].**
17. **Umbral VERDE de K2 (B#D2):** 3/100 (Opus) vs 0.18 (Meta); medir activación, no reenvíos. **[experimento real de tasa partida-desde-sticker en LATAM].**
18. **SEO Engine por-seed ahora (B#D3):** diferir (reco 2/3); construir solo medidor de Search Velocity + landing-compendio. **[firma, reco diferir].**
19. **Pre-compromiso si K2 sale KILL (B#D4):** si <umbral, el fix es de PRODUCTO (sticker no autocontenido), no de copy. Definirlo ANTES evita racionalizar. **[firma].**
20. **Reparto sticker/clip (B#D5):** Meta 60/25/15 (sticker/clip/atribución) vs Opus 70/30. Consenso: sticker primario. **[firma, ~60–70% sticker].**

**Audio (D):**
21. **★ Nº de nodos de grito 2 vs 3 y CUÁLES (D#1, única sin evidencia que la zanje):** 2 nodos (Opus: MX+Caribe / Gemini: MX+Rioplatense-AR por ancestro Truco) vs 3 nodos (Meta L1: MX+Caribe+US-Centroamericano, +2.1× share justifica costo 3×). Tensión sobre CUÁLES: Caribe (Meta) vs Rioplatense (Gemini, ancestro mecánico). **Reco síntesis: si 2 → MX+AR; si 3 → MX+AR+Caribe.** **[firma].**
22. **Textura de Sospecha completa al lanzamiento (con techo) vs MVP diferido (D#2).** Reco clúster: completa con techo gain+banda. **[firma].**
23. **grito_glifo en caption copiable además de la imagen (D#3).** Reco: ambos. **[firma].**
24. **Emoji-artefacto: UI copiable dinámica vs línea estática garantizada (D#4).** Reco: línea garantizada + 1 evento analítico. **[firma].**

**Awe (F):**
25. **Nº de money-shots full: 5 (Meta) o más (Opus) (F#1).** Reco fusionada: lanzar con 5 jefe + medir G2; subir a 6º–8º solo si superan G2 (≥4.5× share) y G3 (≤0.8 d-h) aguanta. **No 20.** **[firma + experimento de share].**
26. **Reparto de arte: plantilla anti-habituación vs fidelidad/Diablo jugable (F#2).** Reco: gasto al BEAT+SONIDO y al Diablo jugable; mínimo a fidelidad de render. ¿3 plantillas (Meta) o 4 (Opus/Gemini)? **[firma].**
27. **¿Condena endless suma dosis? (F#3).** Solo si G3 aguanta; nadie lo refutó. **[firma].**

**Ética (G):**
28. **Umbral de reciprocidad / ratio para-satisfecho (G#1):** dirección converge, número no (Opus 0.35 / Gemini ≥0.15 / Meta 0.20–0.25). Reco 3/3: empezar conservador y endurecer; **calibrar por A/B solo el umbral, NUNCA la dirección del veto.** **[experimento del umbral, firma de la dirección].**
29. **Susurro mid-run silencioso vs epitafio post-run del contrafáctico (G#2).** Lo zanja `re-run<3s`. César firma el default a probar. **[firma + métrica].**
30. **Veto goodwill bloqueante vs advisory (G#3).** Reco 3/3: bloqueante para retorno/share/social. **[firma, reco bloqueante].**
31. **Atenuar arrepentimiento en runs 1–3 de onboarding (G#4):** Meta +18% churn D7 por vergüenza LATAM casual vs Opus/Gemini rigor desde minuto 1. **[firma].**
32. **¿Delay forzado ~1.5s en el epitafio? (G#5):** Opus sí (permiso de parar) vs Meta no (+9% re-run). Lo zanja la métrica. **[firma + métrica].**

---

## 6. Guardarraíles éticos (lo que NO se hace)

> De G (3 fixes rechazados + corolarios), reforzado por D. Inviolables por código.

1. **NUNCA un bot falso** ("Pacto/Diablo Compasivo") disfrazado de ayuda humana. Falsa prueba social. Si César quiere asistencia, debe ser un NPC del Romancero **claramente identificado como bot** — transparencia, no engaño.
2. **NUNCA sticker de burla NOMINAL a un humano.** Burla AL DIABLO (enemigo común) = depósito; burla a tu primo nombrado = withdraw tóxico.
3. **NUNCA estrechar el bucket dinámicamente (50→30) para retener.** Ansiedad manufacturada.
4. **NUNCA exponer deuda individual** como HUD/contador/shaming (#16).
5. **NUNCA CTA/ad/oferta/ranking post-derrota** (#70): no monetizar la frustración.
6. **NUNCA números/EV en el arrepentimiento** — mostrar carta, no cifra (#41).
7. **NUNCA "liberar slot de Maña por cooperación"** — rompe el trade-off faustiano §7.6d.
8. **NUNCA medir `Cheating_Success_Rate`** ni atar audio a la tasa de éxito de fullerías (sería pay-to-hear, rompe fairness) (D#32).
9. **NUNCA escalar una variante que sube K si el grafo se silencia** (block/mute ≥1.5%) — vetar, no escalar (#37/#42).
10. **NUNCA asumir audio** — todo evento de estado debe ser legible en mute (D#67).

---

## 7. Changelog v1.2→v1.3 (ordenado por sección del GDD)

> Aplicación mecánica. Cada entrada cita el/los fix(es) y clúster(es).

- **§3 (Visión/Identidad):** Adoptar el **diagnóstico Balatro** como invariante: transparencia en el cálculo táctico (output del turno), opacidad en la composición meta (Pactos/Maña) [A]. Doctrina rectora global: **visual-primario, audio/awe-amplificador** (mute=default 85–90% LATAM) [D, F].
- **§4.1 (Ley de 3 motores):** Etiqueta `goodwill: deposit|withdraw|neutral` obligatoria en PRs de retorno/share/social; **M1 veta, no autoriza**; veto bloqueante de compilación; auto-rollback si `share rivalidad/reciprocidad >3.5` o `block-rate >1.5%` [G#42, P1-12].
- **§7.3 (Maña/ranuras):** Documentar el trade-off Maña = Fullería **o** Pacto como regla-core nº7 del onboarding; viabilidad Pacto ∈[20%,50%], complementariedad EV(Pacto)>EV(Fullería) en ≥1 estado [E#6, P1-6, P2-21].
- **§7.6 (Pactos):** Apetito de auto-sabotaje estructural en Pactos = decisión de César (emergente vs acoplado-a-mano) [A#1, DC-1].
- **§7.6d (trade-off faustiano):** Disparador `RegretSituation` de 3 condiciones; muestra carta 0.5s sin número; `has_experienced_regret[pact_id]` apaga el susurro permanente (terminable). Prohibido liberar slot de Maña por cooperación [G#41, P2-26].
- **§8 (Social/Viralidad — marco):** Separar K_rivalidad (0.45–0.62) ≠ K_reciprocidad (0.12–0.18) por segmento [G#38, P2-30].
- **§8.1 (claim "Community"):** Condicionar a **k-reciprocidad ≥0.20 a 4 semanas**; si <0.15, corregir el claim, no fingirlo. Stickers de "Alma Co-firmada" (humor negro contra el Diablo) [G#38, P2-30].
- **§8.3 (Exportación/disparo de clips):** Money-shot dispara **post-victoria** (freeze 0.5s); CTA = compartir, nunca comprar; export dual (1080p Steam/Reels + WebP <300KB WhatsApp); vastness por silueta/contraste/sonido, no textura [F#28, P1-14, CX-4].
- **§9 (Presupuesto temporal):** Tabla `Σ12 dientes ∈ [25,35]min p50, p90 ≤40min`, derivada de Maña, validada por solver §14 [E#48, P2-22]. Run continuo vs capítulos = César [E#48-bis, DC-5].
- **§9 (Catarsis → extender a Derrota):** Epitafio 2–3s con logro/esfuerzo + permiso de parar; CERO CTA/ad/ranking por código; gate `re-run<3s` <12% estable [G#70, P2-27]. **Nuevo §9.x "Codex de Arrepentimientos"** [G#41, P2-26].
- **§10 (Awe/clips — marco):** Separación taxativa **§10.1 ASMR (repetición/D1-D7) vs §10.2 money-shot (awe/espaciado)** como dos sistemas con dos KPIs [F#63, P3-6].
- **§10.1 (Clip diario ASMR):** barrido de Escoba 6–8s, mudo-first, loop perfecto; motor de volumen/familiaridad [F#63, B#60].
- **§10.2 (Money-shot/Presentador de Asombro):** Reescribir como **motor único scriptado + slot intercambiable**; casta-doble (A: ~5 full jefe con beat+reacción física; B: ~15 dosis ligeras PNG+SFX); cap duro **G3 ≤0.8 días-hombre/dosis**; awe asíncrono D30+ (KPI = clip convierte espectador); registrar gates falsables **G1** (habituación ≤15% caída #10 vs #1), **G4** (fatiga frequency>2.7/7d o CTR−30% → rotar ≤14d), **G5** (reacción muda ≥70% en <5 palabras tras 0.5s mudo), **G-conversión** (share-to-wishlist 1:0.03–0.04 frío, <0.02 tras 10 creadores → kill beat); Jerarquía Z como scheduler `Z1>Z2>Z3>Z4`, `≤1 Z3+/frame`, `Δt≥300ms` [F#28/#29/#68/#69 + F§4 gates, E#5; P1-8, P1-14, P2-25c, P3-5].
- **§11 (UI/Tells):** Regla dura **predicado, no sujeto**: cero coloreado de candidatas, cero iconos prospectivos de eje, cero hover/halo Pareto; Mesa limpia salvo sumas de 15. Capa-1 banner estado (4–6 palabras, <450ms) + Capa-2 eco retrospectivo (destello 150–200ms + háptico, gateado ≥2 reps, desvanece run 4). Gate Z peor-caso ≥9/10 [A#2/#35, E#5; P1-7, P1-9, P2-2, CX-1].
- **§12 (Onboarding/FTUE):** Mantener asistencia "sumar 15" (ancla cultural hispana, no desactivar). Compresión-arquetipo = REQUISITO (1 frase cultural/regla o cuenta doble). Formato (≤5 podadas vs 3 micro-mangas) = César [A#8, E#6; P2-21, DC-4].
- **§13 (Codex/Romancero):** Colección terminable `X/N` visible + beat 100% estético + sin timer + máx 2–3 siluetas activas + cada cierre destapa la siguiente; gates D30≥8%, abandono 80–99% <5%. Cardinalidad N = César [E#24, P2-24, DC-6]. Biblia del Mundo: 1 pág (5 hechos + 3 ambigüedades), flavor reactivo por arquetipo de victoria (~32 strings, NO 384); apertura Romancero D7 = señal secundaria [E#26, P3-3]. Lore-UGC DIFERIDO post-launch [B#25, P3-2].
- **§14 (Gates/Solver §14.0):** Añadir pasos **S4 (dominancia Maña), S5 (umbral Diablo, acoplado a S4), S6 (composabilidad working-set), S7 (FTUE/Maestría)** con umbrales V/🟡/KILL exactos; proxy de bots para techo de maestría (#53); banda EV [10–15%] a fijar por solver; complementariedad Pacto↔Fullería; `reglas_verbalizadas ≤5` + `reglas_core ≤9` + `C=reglas×canales ≤12/mano`; hook `p50 ≤90s`; Gate Z (≥9/10, ≥55fps Moto G, bounce<35%) [A#1/#50/#6/#8/#53, E#5/#6/#48/#49; P1-1..6, P1-9, P2-21..23, INV-1..10].
- **§16 (Test plan):** Kill de legibilidad = vocabulario-ciego (predicción contrafáctica ≥50% κ≥0.6 + elección Pareto ≥55%), NO "≥70% nombran eje"; test del experto A1 [A#4, P2-1, INV-16]. Watchability "≥1 momento transmisible/run" [B#56, P2-25]. **A/B comercial demo LATAM n≥5k/rama** (eco-gateado vs sin-tells): D7 +≥5pp (target >28%) ∧ share no cae >10% (≥1.4/100) ∧ refund <8%; share −≥15% → re-evaluar UA [A§4, P2-25b]. **Gates de awe G1/G4/G5/G-conversión** (G1 share N-ésimo jefe ≤15% caída #10 vs #1; G4 fatiga frequency>2.7/7d o CTR−30% → rotar ≤14d; **G5 reacción muda ≥70% en <5 palabras tras 0.5s**; **G-conv share-to-wishlist 1:0.03–0.04 frío, <0.02 tras 10 creadores → kill beat**) [F§4, P2-25c]. Primero a falsar por centavos: grito mudo + eyes_closed + experto + solver S4–S7 [D-nota].
- **§17 (Modelo de negocio/comercial):** Gate #47 en 3 capas (orgánico ≥60% ventas Sem-1 / paid marginal CAC≤LTV, LATAM $0 / kill LTV/CAC≥3 blended O ≥1.5 hispanos/≥1.2 LATAM — lo zanja el CAC medido); tabla LTV neto-refund (~$9.3/~$4.7); bandas WL→venta bimodales. **1.0 directo, $14.99/$11.99/$7.49 LATAM** + español día 1 + disclaimer AR. Next Fest demo T-12sem, gate velocity +150 WL/día 7d. Retención demo ≥35%>15min, ≥38% cruzan 2h/72h. Banda review Mostly Positive ≥70% (lift +22–35% USA/+12–18% LATAM). WL velocity>acumulado. Tags = Roguelike Deckbuilder + Rogue-lite + Dark Fantasy + Solitaire. Gates culturales medidos (CTR ≥2.4% AND +15%; reconocimiento <1.2s/≥70% en 3 nodos; decay marca <45%/90d) [C todo; P2-14..20]. Diferir SEO-Engine, construir medidor Search Velocity + landing-compendio [B#57, P3-1].
- **§18 (Telemetría/social/ética en código):** TDF/gift-back solo backend (≥30%/72h); centinela del grafo en código (máx 2 envíos/contacto/semana, 3.º auto-bloqueado; block/mute <1.5%, report-spam <0.3%, o no shippea); KPI maestro saciedad `(share_recip/total)×(1−block-rate)` >0.25 sano/<0.15 veto; bucket cerrado ~50 pares reales, Diablo Fantasma real (auditar 0 sintéticos), sin re-barajar para retener; ratio para-satisfecho >1.2 atado al release [G#16/#37/#55/#15, P1-13, P2-28..31].
- **§19.3 (Audio/Accesibilidad/Arquitectura-audio):** Doctrina `state_is_visual_complete`; emisor `emitStateCue(visual,audio)` con visual no-nullable, lint `no_bare_audio_emit`, test `mute_total` 100% binario; 3 capas con techo (leitmotiv Trampa loop + textura Sospecha `gain≤0.8*master` y banda ∉[500Hz,2kHz] + 3 firmas resultado), `audio_layers_active ≤2`, gate `eyes_closed_test ≥75%`, KPI ético `quit_rate ≤baseline`, prohibido `Cheating_Success_Rate`; firma identidad 2–3s inline ≤35KB precargada, `AudioContext.resume()` en evento semántico, linter `no_autoplay_without_gesture`, KPI `firma_heard_first_session` ≥58% And/≥38% iOS-MX, fallback flash+vibración; `grito_glifo` no-null Posada ≤2 palabras OCR-legible 96×96px contraste≥4.5:1; `cultural_packs[node].grito={audio,glifo,locale}` + fallback default, nº de nodos = César; `RunDigest.text_glyph` copiable, KPI separado ≥4% sem-1; muted+playsinline, audio arma al 1er tap, demo <1.5s [D todo, B#22; P1-10, P1-11, P2-9..13, DC-21..24].

---

**Confianza global de la fusión:** alta donde 3/3 + L1/L2 (P1 casi todo, gates comerciales C, ética G); media donde el umbral espera experimento (K2, EV, LTV/CAC, lift del tease, reciprocidad); explícitamente ⚪ donde el GDD lo marcó supuesto (cardinalidad N, "70% a 36m" #43, umbral del arrepentimiento, text_glyph). Ningún ⚪ se subió a 🟢; ningún CONTESTADO se reportó como consenso.
