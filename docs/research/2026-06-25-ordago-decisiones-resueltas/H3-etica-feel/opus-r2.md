# Opus R2 · Cross-review de RESOLUCIÓN · H3 "Ética, Pactos y feel"

Asiento Diseñador de Sistemas + ética en código. Steelman, ataque/cambio y reco final comprometida por DC. Guardarraíles: nada de FOMO de culpa, manipulación, ni números en el arrepentimiento.

## TABLA-RESUMEN (post-cross-review)
| DC | Reco final R2 | Conf. | Movimiento vs mi R1 |
|----|---------------|-------|---------------------|
| DC-1 | **Emergente con *cicatriz acoplada* a 2–3 Pactos-ancla** (híbrido) | 🟡 | CEDO parcial a Gemini/Meta |
| DC-3 | **Suerte→top-funnel; skill→cuerpo del loop/LTV** | 🟢 | Mantengo; absorbo dato Meta |
| DC-28 | **Arranque 0.22** (calibrar al alza si saciedad baja) | 🟡 | CAMBIO de 0.30 → 0.22 (Meta L1) |
| DC-29 | **Epitafio post-run, nunca mid-run** | 🟢 | SUBO 🟡→🟢 (Meta L1 zanja) |
| DC-30 | **Bloqueante** (veto invariante de compilación) | 🟢 | Mantengo, consenso 3/3 |
| DC-31 | **OFF de *frecuencia* runs 1–3, texto intacto** | 🟡 | Mantengo, refuerzo con Meta |
| DC-32 | **NO delay forzado; permiso de parar = botón, no fricción** | 🟡 | CAMBIO de delay-skipeable → 0s |

---

### DC-1 · Auto-sabotaje en Pactos
**Steelman (Gemini/Meta):** Gemini tiene razón en que "la cicatriz es memorable" y la matemática pura no se cuenta en foros. Meta aporta el dato duro que mi R1 ignoró: regla emergente = 33% recall vs 64% con costo visible, y con churn-por-no-entender ya en +18% D7, lo emergente-opaco es **riesgo de comprensión real en móvil 6"**, no elegancia. Eso ataca mi premisa de "diseñas el espacio, no el contenido": un espacio ilegible no es agencia, es castigo opaco.

**Ataque/cambio:** Pero el acoplado-a-mano *puro* (Gemini) infla working-set y arrastra reglas que mi solver S4/S6 no garantiza. La síntesis correcta es **híbrida y verificable en código**: motor emergente como default + una *cicatriz acoplada explícita* en 2–3 Pactos-ancla (ej. "ceguera": no ves el valor de tu mano derecha). El acoplado se reserva para los Pactos donde la legibilidad y la historia importan; el resto vive emergente bajo gate. Esto satisface el `recall ≥60% run1` de Meta sin colapsar S6.

**RECOMENDACIÓN FINAL:** **Emergente + cicatriz acoplada a 2–3 Pactos-ancla** 🟡.
**Gate:** `recall_correcto_run1 ≥60%` (corpus etiquetado MX n=3k) Y `dominant_build_share <0.25` Y `working_set ≤ presupuesto S6`. Si recall <60% en los Pactos emergentes → acoplar más; si S6 se desborda → reducir acoplados.

### DC-3 · Dial suerte↔skill (PESO)
**Steelman:** Gemini (70/30 fijo) y Meta (70/30 adquisición, 40/60 in-game) convergen con mi tesis y la mejoran con un dato L1 fuerte: clip "chiripa" da 1.8× share, "negué escala T3" da +18% wishlist pero share 1.0×. Eso CONFIRMA mi separación de funnels, no la contradice.

**Ataque:** El número fijo "70/30" de Gemini como *peso del loop* es la trampa: si la suerte pesa 30% del **resultado in-game**, el arrepentimiento deja de ser honesto y D30 se contamina. Meta lo separa bien: 70/30 es **mezcla de creatividades de UA**, no peso del motor. Mi formulación gana en precisión: suerte gobierna *superficie de marketing*, skill gobierna *cuerpo del loop/LTV*.

**RECOMENDACIÓN FINAL:** **Suerte→top-funnel (CTR/share/UA, mezcla ~70/30 en creatividades); skill→cuerpo del loop y ~100% del LTV/D30** 🟢.
**Falsador:** si `D30 correlaciona con varianza de seed` > que con métricas de decisión → el motor está mal. Cohorte D30: win-rate ajustado vs seed-luck contra retención.

### DC-28 · Umbral de reciprocidad
**Steelman:** Meta trae L1 que mi 0.30 no tenía: k-reciprocidad observada LATAM = 0.12–0.18 (no 0.35), gift-back 28–34%/72h, saciedad = 0.22×(1−0.008) = 0.218 > piso 0.15. Mi 0.30 estaba calibrado a un k inflado. Gemini (0.25) y Meta (0.22) están ambos por debajo de mí con mejor evidencia.

**Cambio:** CEDO. El dato L1 de Meta manda sobre mi prior. Arranco en **0.22** (no 0.25 de Gemini, que "se acerca a vergüenza en redes de baja afinidad" según Meta) y endurezco solo si la saciedad real lo pide. Calibro el número, **nunca la dirección** del veto (guardarraíl).

**RECOMENDACIÓN FINAL:** **Arranque 0.22** 🟡.
**Gate:** A/B 0.20/0.22/0.25; escalar la celda con `saciedad ≥0.18` y `block <1.2%`. Si saciedad <0.15 → subir; si fabrica bloqueos legítimos → bajar.

### DC-29 · Susurro del arrepentimiento
**Steelman (contra Gemini):** Gemini defiende mid-run silencioso ("¿La querías, tahúr?" 0.5s) como duda diegética en tiempo real, estilo Inscryption. Es bello en feel.

**Ataque decisivo:** Meta lo rompe con L1: cualquier estímulo in-situ tras error con delay >1s = **+9% re-run<3s**; mid-run "reabre wanting" → es compulsión inyectada, no pedagogía. Eso viola directamente el guardarraíl (manipulación del impulso post-error). Mi R1 ya iba a post-run; Meta confirma y un tercero (yo) cierra el caso. El mid-run de Gemini es un dark pattern emocional disfrazado de feel.

**RECOMENDACIÓN FINAL:** **Epitafio post-run, nunca mid-run; muestra carta, no número** 🟢 (subo de 🟡: 3 asientos, 2 L1, convergencia).
**Falsador:** si post-run sube `re-run<3s >15%` → es compulsión también y se atenúa/quita. Gate: `re-run<3s ≤13%`.

### DC-30 · Veto goodwill: bloqueante vs advisory
**Steelman:** Consenso 3/3 (todos bloqueante). Meta da el L1 que lo sella: WhatsApp >2 envíos → block 0.8%→4.2%, mute 18% al 3º, ratio rivalidad/reciprocidad 3.47. Advisory se superaría el día 4.

**Sin ataque.** Advisory-que-se-ignora = dark pattern por omisión. El veto debe ser invariante de compilación, no una sugerencia.

**RECOMENDACIÓN FINAL:** **Bloqueante** 🟢. Implementación en código: `goodwill: deposit|withdraw|neutral`; build **Unstable** + auto-rollback si `share rivalidad/reciprocidad >3.5` O `block/mute ≥1.5%`. M1 veta, **nunca autoriza** ("el saldo aguanta" prohibido).
**Falsador (solo umbral, no dirección):** si vetar interacciones sanas a tasa alta → ajusto umbral, el veto sigue bloqueante. Gate CI: `block_rate ≤1.5%` sobre corpus etiquetado.

### DC-31 · ¿Atenuar arrepentimiento en runs 1–3?
**Steelman (Meta/Gemini):** Meta: vergüenza social LATAM casual = +18% churn D7; proyectado a arrepentimiento temprano, baseline 32%→50% si exponemos culpa en onboarding; atenuar baja a 35–37%. Meta pide OFF total (0% susurro) runs 1–3. Gemini pide no-atenuar (rigor pleno). Chocan de frente.

**Síntesis (mi posición gana matiz):** Ambos extremos fallan. Atenuar el **texto/fidelidad al Romancero** (Meta=0%) enseña una mentira que el run 4 contradice → rompe el contrato. No atenuar **nada** (Gemini) come el +18% churn que Meta documenta. El guardarraíl prohíbe FOMO de culpa, no rigor honesto. Resuelvo en código: en runs 1–3 se apaga la **frecuencia/ritmo** del susurro (puede ser 0 apariciones), pero cuando aparece (run 4+ o evento mayor) el **texto es íntegro**. Atenúo el *cuándo*, jamás el *qué*. Esto captura el ahorro de churn de Meta sin la mentira que Gemini teme.

**RECOMENDACIÓN FINAL:** **OFF de frecuencia en runs 1–3 (hasta 0 apariciones), texto/fidelidad intactos siempre** 🟡.
**Falsador:** A/B onboarding, si cohorte-expuesta-a-frecuencia-plena tiene `churn D7 > +12%` vs control → frecuencia aún más baja. Gate: `churn D7 ≤38%`.

### DC-32 · ¿Delay forzado ~1.5s en epitafio?
**Steelman (contra mí y Gemini):** Mi R1 (delay skipeable) y Gemini (delay forzado 1.5s) apostaban al "permiso de parar / cierre digno". Meta lo ataca con L1: delay >1s en pantalla de pérdida = **+9% re-run<3s**; "Opus busca pausa reflexiva, pero la data muestra compulsión, no reflexión". El delay forzado de Gemini es directamente un dark pattern de fricción.

**Cambio (cedo a Meta):** Mi "skipeable frame 1" era un parche; si nadie skipea, es delay forzado encubierto, y si todos skipean, no da permiso de nada. Meta tiene razón: el **permiso de parar se da con un BOTÓN claro de salir (no fricción temporal)**, no con un delay. Cero-delay + botón "Dejar la mesa" visible = permiso real sin compulsión inducida. Reconcilio mi LD7 ("permiso de parar") con el dato: el permiso es *affordance*, no *latencia*.

**RECOMENDACIÓN FINAL:** **NO delay forzado; epitafio skipeable frame 1 + botón de salida explícito como permiso de parar** 🟡.
**Falsador (de Meta):** si skipeable sostiene `re-run<3s >22%` 7 días → introducir delay SOLO si baja re-run de >22% a <14% sin subir churn D1. Gate: A/B 0s vs 1.5s.

---

## Convergencia del grupo H3 (3 asientos)
- **3/3:** DC-3 (suerte top-funnel / skill loop), DC-30 (bloqueante). Cerrados 🟢.
- **2/3 → cierro:** DC-29 (post-run, Meta L1 zanja mid-run de Gemini), DC-28 (bajo a 0.22 por L1 de Meta), DC-32 (NO delay, Meta L1 vence el feel de Gemini y mi parche).
- **Síntesis nueva mía:** DC-1 (híbrido emergente+cicatriz acoplada, ni Gemini puro ni mi emergente puro) y DC-31 (atenuar frecuencia, no texto: ni el 0% de Meta ni el rigor-pleno de Gemini).

## Guardarraíles verificados
Ningún FOMO de culpa, ninguna inyección de impulso post-error (mata mid-run y delay forzado), arrepentimiento siempre vía carta no número, veto bloqueante en código. Todos los números calibran *magnitud*, nunca la *dirección* ética.
