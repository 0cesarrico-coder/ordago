# Opus R1 · Grupo H3 "Ética, Pactos y feel" — RESOLUCIÓN

## TABLA-RESUMEN
| DC | Opción | Conf. | Gate / experimento que la cierra |
|----|--------|-------|----------------------------------|
| DC-1 | **Emergente** (solver S4-verde) | 🟡 | Migrar a acoplado si `dominant_build_share >25%` o S6 ok |
| DC-3 | **Suerte→top-funnel (CTR/share); skill→100% del LTV/D30** | 🟢/🟡 | D30 correlaciona con suerte, no con skill |
| DC-28 | **Arranque 0.30** (entre 0.25 y 0.35) | 🟡 | A/B saciedad: el 0.30 deja share-recip sano |
| DC-29 | **Epitafio post-run** (diferido) | 🟡 | `re-run<3s` cae bajo baseline |
| DC-30 | **Bloqueante** (M1 veta) | 🟢/🟡 | Falso positivo legítimo bloqueado por código |
| DC-31 | **Rigor desde run 1, sin atenuar texto; suavizar SOLO ritmo** | 🟡/⚪ | Churn D7 cohorte-expuesta > +12% vs no-expuesta |
| DC-32 | **Delay 1.5s skipeable frame 1** | 🟡 | `re-run<3s` cae ≥7% con delay no-skipeable |

---

### DC-1 · Auto-sabotaje en Pactos
**(a)** **Emergente** (confío en el solver S4-verde como default).
**(b)** A1 🟡: "diseñas el espacio, no el contenido". Acoplar auto-sabotaje a mano a cada Pacto fuerte mata la elegancia, infla el working-set y arrastra reglas que colapsan S6. El espacio de decisión (qué Fullería resuelve qué Pacto) es el foso barato; el contenido a mano es deuda. Loss-aversion (06 🟢) ya da el peso emocional sin necesidad de scripts.
**(c)** **Falsador:** si el solver S4 reporta una build dominante con `dominant_build_share >25%` (una línea que se cuela y trivializa Pactos), migro a acoplado-a-mano SOLO para esos Pactos-outlier.
**(d)** Solver S4 en barrido de seeds: si <5% de builds son dominantes y S6 no se desborda, queda emergente. Umbral exacto: `dominant_build_share <0.25` Y `working_set ≤ presupuesto S6`.

### DC-3 · Dial suerte↔skill (PESO)
**(a)** **Suerte gobierna top-funnel (CTR/share/UA); skill gobierna ~100% del LTV/D30.**
**(b)** 🟢/🟡: la secuencia ya está reconciliada; el peso operativo es que la suerte es *superficie de marketing* (legible, viral, baja barrera) y la skill es *cuerpo del loop* (lo que retiene). LD7: la saciedad y la retención nacen de decisión, no de varianza. Si la suerte gobernara el LTV, sería casino, no deckbuilder.
**(c)** **Falsador:** si `D30 correlaciona con varianza de seed` (suerte) más que con métricas de decisión del jugador → el peso está mal y la skill no manda en el loop.
**(d)** Cohorte D30: correlación skill-proxy (win-rate ajustado) vs seed-luck contra retención. Skill debe explicar la mayor parte.

### DC-28 · Umbral de reciprocidad
**(a)** **Arranque 0.30** (bajo de mi 0.35 hacia el consenso; sobre el piso 0.15).
**(b)** 🟡: reco compartida = empezar conservador y endurecer. 0.35 es defendible pero arriesga vetar reciprocidad legítima al inicio; 0.30 deja margen sin caer al piso-veto. Calibro **solo el umbral** por A/B, **nunca la dirección** del veto (guardarraíl).
**(c)** **Falsador:** si a 0.30 el `share_recip/total` se hunde <0.20 (KPI saciedad) → endurezco a 0.35; si fabrica bloqueos legítimos, suelto a 0.25.
**(d)** A/B saciedad: `(share_recip/total)×(1−block_rate)` — sano >0.25, veto <0.15. Fijo el número con la celda que maximiza saciedad sin pasar block-rate >1.5%.

### DC-29 · Susurro del arrepentimiento
**(a)** **Epitafio post-run (diferido)**, no mid-run.
**(b)** 🟡: mid-run silencioso compite con la atención del loop y roza el FOMO ambiental (06: el arrepentimiento debe nacer de dotación real, no inyectarse en caliente). El epitafio respeta el "permiso de parar" y muestra carta (no número, guardarraíl). LD7: terminable vía `has_experienced_regret`.
**(c)** **Falsador:** si el epitafio diferido baja `re-run<3s` bajo baseline (el jugador rumia y abandona) → muevo a mid-run silencioso.
**(d)** Métrica **`re-run<3s`** lo zanja: si cae ≥7% vs baseline sin susurro, cambio.

### DC-30 · Veto goodwill: bloqueante vs advisory
**(a)** **Bloqueante.**
**(b)** 🟢/🟡: M1 (🟢) **veta, nunca autoriza**; "el saldo aguanta" está prohibido. Advisory = advisory-que-se-ignora = dark pattern por omisión. El veto debe ser invariante de compilación: `goodwill: deposit|withdraw|neutral`, build **Unstable** si `share rivalidad/reciprocidad >3.5` o `block-rate >1.5%`, **auto-rollback**.
**(c)** **Falsador:** si el bloqueante produce falsos positivos que vetan interacciones claramente sanas a tasa alta → reviso el *umbral* (no la dirección): el veto sigue bloqueante.
**(d)** Gate CI: `block_rate ≤1.5%` sobre corpus de interacciones etiquetadas; si excede, rollback automático.

### DC-31 · ¿Atenuar arrepentimiento en runs 1–3?
**(a)** **No atenuar el texto/fidelidad al Romancero; suavizar SOLO el ritmo de aparición** (frecuencia, no contenido).
**(b)** 🟡/⚪: Meta reporta +18% churn D7 por vergüenza (LATAM casual) — dato L1 que respeto, PERO atenuar el contenido rompe fidelidad y enseña al jugador una mentira que luego se contradice. El guardarraíl prohíbe FOMO de culpa, no rigor honesto. Compromiso: mismo arrepentimiento, menos frecuente en runs 1–3.
**(c)** **Falsador:** si la cohorte-expuesta a rigor-pleno run-1 tiene churn D7 **> +12%** vs no-expuesta → atenúo más agresivo (ritmo aún más bajo), nunca falseo el texto.
**(d)** A/B onboarding: churn D7 cohorte-expuesta vs control. Umbral de acción: Δ >+12%.

### DC-32 · ¿Delay forzado ~1.5s en epitafio?
**(a)** **Delay 1.5s PERO skipeable desde frame 1.** (Reconcilio mi "permiso de parar" con el "+9% re-run" de Meta.)
**(b)** 🟡: el delay da permiso de parar (anti-compulsión, LD7) sin forzar; skipeable frame 1 preserva el re-run de quien quiere seguir. No es delay-forzado-bloqueante (eso cuesta +9% re-run según Meta) ni cero-delay (pierde el permiso de parar).
**(c)** **Falsador:** si la variante con delay-skipeable iguala el re-run del delay-forzado (jugadores no skipean) → el skip no protege; si `re-run<3s` cae ≥7% → quito el delay.
**(d)** Métrica **`re-run<3s`** lo zanja: 3 celdas (sin delay / skipeable / forzado). Elijo la que conserva re-run y da permiso de parar.

---

## Conflictos con mi propia secuencia
- **DC-29 (epitafio diferido) + DC-32 (delay 1.5s en epitafio):** se refuerzan — ambos viven en el epitafio post-run y comparten la métrica `re-run<3s`. Coherente: un solo gate los gobierna; si el epitafio daña re-run, reviso los dos juntos.
- **DC-31 (no atenuar texto) vs DC-29/32 (proteger re-run):** posible roce — rigor pleno podría deprimir re-run en runs 1–3. Resuelvo: en runs 1–3 manda el **ritmo** (DC-31: menos frecuente), no el texto; el delay sigue skipeable. La fidelidad no se sacrifica; la frecuencia sí se calibra.
- **DC-3 (skill manda el LTV) + DC-1 (emergente):** alineados — la profundidad emergente (A1) ES la skill que retiene; acoplar contenido a mano sería contenido-suerte disfrazado.

## Qué dejo a Meta/Gemini
- **Meta (Data L1):** el número exacto de DC-28 (¿0.25, 0.30 o 0.35 maximiza saciedad real?) y el Δchurn D7 de DC-31 por cohorte LATAM — solo su data L1 sube mi ⚪→🟡. También el `re-run<3s` real de las 3 celdas de DC-32.
- **Gemini (feel/valor):** si el epitafio diferido (DC-29) *se siente* como cierre digno o como rumiación; y si el delay-skipeable (DC-32) se lee como respeto o como fricción. La lente de feel decide entre mid-run y post-run si la métrica empata.
