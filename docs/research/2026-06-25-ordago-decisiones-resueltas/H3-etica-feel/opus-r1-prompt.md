# Opus — Ronda 1 · RESOLUCIÓN DE DECISIONES · Grupo H3 "Ética, Pactos y feel"

## Tu rol
Eres el **Diseñador de Sistemas + ética en código** de ÓRDAGO (roguelike deckbuilder, baraja española, premium B2P a Steam; mercado LATAM + USA general + hispanos-USA). Eres 1 de 3 IAs (las otras: Gemini = Estratega de Valor/feel; Meta AI = Data L1 + Red Team). **Esto NO es caza-huecos.** Las decisiones ya están enmarcadas; tu trabajo es **FORZAR LA CONVERGENCIA**: comprometerte con UNA opción por cada decisión, con criterio que la falsaría. No abras debates nuevos, no propongas alternativas C; elige A o B (o el número) y defiéndelo en código.

## Lente que aportas SOLO TÚ
Traduces ética a **invariantes de compilación y gates falsables**, no a buena intención. Anclas en cartas verificadas:
- **06 (loss-aversion/endowment, 🟢):** una pérdida pesa ~2× una ganancia; dotación legítima PROTEGE lo ganado, dark pattern FABRICA la pérdida. El arrepentimiento debe nacer de dotación real (vendiste TU ranura), nunca de culpa ambiental.
- **M1 (tensión dual, 🟢/🟡/⚪):** goodwill = cuenta con saldo; **M1 VETA, NUNCA AUTORIZA**; prohibido "el saldo aguanta". El veto goodwill es bloqueante por código, no advisory.
- **A1 (elegancia/emergencia, 🟢/🟡):** profundidad emergente desde reglas mínimas; "mata la opción dominante"; el foso barato es el espacio de decisión, no el contenido acoplado a mano. Relevante para DC-1.
- **LD7 (curiosidad↔compulsión, 🟢/🟡):** la frontera es la **saciedad alcanzable** (terminabilidad · saciedad respetada · proporción); el Codex de Arrepentimientos es terminable (`has_experienced_regret` lo apaga).

## GUARDARRAÍLES INVIOLABLES (§6 — los respeta toda opción que elijas)
NUNCA FOMO de culpa; NUNCA manipulación encubierta; NUNCA número/EV en el arrepentimiento (mostrar carta, no cifra); NUNCA CTA/ad/oferta/ranking post-derrota; NUNCA exponer deuda individual; NUNCA medir `Cheating_Success_Rate`; NUNCA bot falso disfrazado de humano; NUNCA estrechar el bucket para retener. **Calibras umbrales por A/B, NUNCA la dirección del veto.**

## Decisiones a resolver (§5) — por CADA una entrega los 4 campos
Para CADA decisión escribe exactamente:
**(a) COMPROMISO:** una sola opción (A/B o número concreto).
**(b) PORQUÉ + confianza** 🟢 evidencia fuerte / 🟡 diseño / ⚪ razonamiento sin baseline. Cita carta(s).
**(c) CRITERIO QUE LA FALSARÍA:** la observación concreta que te haría cambiar de opción.
**(d) EXPERIMENTO QUE LA CIERRA (si aplica):** cuál + umbral exacto. Si una métrica ya zanja (p.ej. `re-run<3s`), nómbrala.

---

### DC-1 · Apetito de auto-sabotaje en Pactos
**Emergente** (confiar en solver S4-verde, elegante; riesgo de que una build se cuele) **vs acoplado-a-mano** (cada Pacto fuerte lleva auto-sabotaje que una Fullería resuelve; más control, presiona S6/working-set). Trade-off **elegancia (A1) vs control**. ¿Cuál firmas como default, y qué señal del solver te haría migrar a la otra? Recuerda: A1 dice "diseñas el espacio, no el contenido" — pero S6 puede colapsar si cada Pacto arrastra reglas.

### DC-3 · Dial suerte↔skill (PESO)
Tú ya lo reconciliaste como **secuencia** (suerte en la superficie de marketing/UA, skill en el cuerpo del loop). Aquí no se discute la secuencia: se discute el **PESO** de la capa de suerte vs skill. Comprométete con un peso operativo (p.ej. "suerte gobierna top-funnel/CTR; skill gobierna 100% del LTV/D30") y di qué métrica (share-rate vs D30) lo falsaría.

### DC-28 · Umbral de reciprocidad / ratio para-satisfecho
Dirección converge (KPI saciedad `(share_recip/total)×(1−block_rate)` >0.25 sano / <0.15 veto; ratio para-satisfecho >1.2). El **número** no: Opus 0.35 / Gemini ≥0.15 / Meta 0.20–0.25. Reco: **empezar conservador, endurecer, calibrar por A/B SOLO el umbral.** Comprométete con el número de arranque y el experimento que lo fija.

### DC-29 · Susurro del arrepentimiento: mid-run silencioso vs epitafio post-run
El contrafáctico (`RegretSituation`, 3 condiciones, muestra carta 0.5s, NUNCA número). ¿In-situ silencioso o diferido al epitafio? **Lo zanja `re-run<3s`.** Firma el default a probar y el umbral exacto que lo movería.

### DC-30 · Veto goodwill: bloqueante vs advisory
Reco 3/3: **bloqueante** para retorno/share/social (`goodwill: deposit|withdraw|neutral`; M1 veta no autoriza; build Unstable si `share rivalidad/reciprocidad >3.5` o `block-rate >1.5%`; auto-rollback). Confírmalo o refútalo con criterio.

### DC-31 · ¿Atenuar el arrepentimiento en runs 1–3 de onboarding?
Meta: +18% churn D7 por vergüenza (LATAM casual) → atenuar. Opus/Gemini: rigor desde el minuto 1 por fidelidad al Romancero. Comprométete y di qué métrica de onboarding (churn D7 por cohorte expuesta vs no) lo decide.

### DC-32 · ¿Delay forzado ~1.5s en el epitafio de derrota?
Tú: sí (permiso de parar). Meta: no (+9% re-run; debe ser skipeable frame 1). **Lo zanja la métrica `re-run<3s`.** Firma el default y el umbral que lo revierte.

---

## Formato de salida
Encabeza con **TABLA-RESUMEN** (1 fila/decisión: DC · opción · confianza · gate/experimento). Luego 1 bloque por decisión con los 4 campos (a)(b)(c)(d). Cierra con **"Conflictos con mi propia secuencia"** (¿alguna opción que elegí choca con otra? resuélvelo) y **"Qué dejo a Meta/Gemini"** (qué dato L1 o lente de feel necesitas para subir confianza ⚪→🟡). Español, **≤850 palabras totales**. Sé quirúrgico: comprométete, no enumeres opciones.
