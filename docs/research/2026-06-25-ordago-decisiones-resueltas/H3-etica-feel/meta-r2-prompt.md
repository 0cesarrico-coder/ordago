# RONDA 2 — CROSS-REVIEW de RESOLUCIÓN · H3 — Ética, Pactos y feel · ÓRDAGO

Abajo están las TRES posiciones R1 (Opus, Gemini, Meta AI), comprometidas con UNA opción por decisión. Manteniendo tu ASIENTO:
1. **STEELMAN** la postura ajena más fuerte donde difieras.
2. **ATAQUE** o CAMBIA si la ajena es mejor (dato/carta).
3. **CONVERGE**: por CADA decisión (DC-1/3/28/29/30/31/32), RECOMENDACIÓN FINAL UNA opción + confianza 🟢/🟡/⚪ (o CONTESTADO: con experimento+umbral). Respeta los guardarraíles éticos (nada de FOMO de culpa, manipulación, números en el arrepentimiento).
4. No "depende de César": comprométete.
Evidencia L1-L4. ≤850 palabras.

============================================================

----- R1 · OPUS -----
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

----- R1 · GEMINI -----
## TABLA-RESUMEN

| DC | Opción | Confianza | Gate / Experimento |
| :--- | :--- | :---: | :--- |
| **DC-1** | Acoplado-a-mano (Pacto + Auto-sabotaje explícito) | 🟢 | Ratio de abandono de runs con pactos vs. sin pactos |
| **DC-3** | Skill-dominant (70% Skill / 30% Suerte) | 🟢 | % de reseñas en Steam que mencionen "unfair/injusto" |
| **DC-28**| Umbral de reciprocidad: **0.25** | 🟡 | Test A/B (0.20 vs. 0.25 vs. 0.30) |
| **DC-29**| Mid-run silencioso (*"¿La querías, tahúr?"* ~0.5s) | 🟢 | Tiempo de lectura en pantalla de arrepentimiento |
| **DC-30**| Bloqueante (Veto estricto de goodwill) | 🟢 | Evolución de la nota de Steam (Reviews positivas) |
| **DC-31**| No-atenuar (Rigor narrativo desde Run 1) | 🟡 | Churn de D1 a D3 por cohorte (LATAM vs. US) |
| **DC-32**| Sí (Delay forzado de 1.5s en derrota) | 🟢 | Ratio de Rage-quits (Alt+F4) vs. Re-run |

---

## DECISIONES RESUELTAS

### DC-1 · Apetito de auto-sabotaje en Pactos
* **(a) COMPROMISO:** Acoplado-a-mano.
* **(b) PORQUÉ + confianza (🟢):** Un trato con el Diablo no es una optimización de stats; es una herida autoinfligida. Como el ojo sacrificado en *Inscryption*, el jugador debe recordar exactamente qué entregó a cambio del poder. El diseño emergente diluye la culpa; el acoplado-a-mano personaliza la tragedia. Si usas una Fullería para romperlo, la victoria se siente como un robo magistral al Diablo, no como un bug del sistema.
* **(c) CRITERIO QUE LA FALSARÍA:** Si el ratio de selección de Pactos cae por debajo del 15% en runs ganadores (señal de que el coste es percibido como un castigo insalvable y no como un riesgo emocionante).
* **(d) EXPERIMENTO:** Análisis de cohortes: medir si los jugadores que ganan usando al menos un Pacto acoplado muestran un 20% más de menciones al "riesgo" en feedback cualitativo que los que ganan con builds "limpias".

### DC-3 · Dial suerte↔skill (PESO)
* **(a) COMPROMISO:** **70% Skill / 30% Suerte**.
* **(b) PORQUÉ + confianza (🟢):** El "feel" de *Slay the Spire* radica en que el jugador asuma la total responsabilidad de la derrota. Si la suerte domina, la pérdida se siente como una estafa del algoritmo; si la skill domina, el arrepentimiento es honesto (*"debí haber pickeado esa carta de defensa en el piso 2"*). Ese 30% de suerte es el folclore, el "viento de la baraja" que da la chiripa compartible en redes, pero el 70% de skill es lo que sostiene la cola larga en Steam y el respeto de la comunidad de cartas.
* **(c) CRITERIO QUE LA FALSARÍA:** Que el ratio de victorias de jugadores expertos en los primeros 10 runs supere el 80% (demasiado determinista, mata la mística del azar del "truco").
* **(d) EXPERIMENTO:** Simulación de Montecarlo + Testeo cerrado con pro-players: forzar escenarios de "mano pésima" y medir si el 15% superior de los jugadores puede resolverlos mediante mecánicas de descarte o engaño.

### DC-28 · Umbral de reciprocidad / ratio para-satisfecho
* **(a) COMPROMISO:** Umbral de **0.25**.
* **(b) PORQUÉ + confianza (🟡):** Un umbral de 0.25 (1 victoria parcial/satisfactoria por cada 4 runs) es el punto dulce de la "sed de revancha". Menos de 0.20 se siente punitivo e injusto para el público americano e hispano que busca progreso; más de 0.35 abarata la victoria y diluye la opresión de la atmósfera del Romancero.
* **(c) CRITERIO QUE LA FALSARÍA:** Churn prematuro en D3 superior al 30% en la cohorte LATAM (más sensible a la falta de progreso percibido).
* **(d) EXPERIMENTO:** Test A/B balanceando el matchmaking/recompensa para fijar el ratio en 0.20, 0.25 y 0.30 de manera oculta. Medir la métrica de re-run inmediato.

### DC-29 · Susurro del arrepentimiento: mid-run silencioso vs epitafio post-run
* **(a) COMPROMISO:** Mid-run silencioso.
* **(b) PORQUÉ + confianza (🟢):** El arrepentimiento post-run es una autopsia fría. El susurro *mid-run* (ver la carta sacrificada translúcida en tu descarte por 0.5s con el susurro *"¿La querías, tahúr?"*) ocurre cuando todavía hay pulso. Duele en tiempo real. Respeta al jugador porque no detiene el flujo de la partida, pero planta la semilla de la duda de forma puramente diegética, al estilo de las cartas parlantes de *Inscryption*.
* **(c) CRITERIO QUE LA FALSARÍA:** Incremento en el tiempo medio de turno (AP - Analysis Paralysis) provocado por la distracción visual o cognitiva del susurro.
* **(d) EXPERIMENTO:** Medir si el grupo expuesto al flash mid-run tiene un tiempo de re-run post-derrota más reflexivo (entre 3s y 6s) en comparación con el re-run instantáneo y compulsivo (<1.5s) del grupo sin estímulo.

### DC-30 · Veto goodwill: bloqueante
* **(a) COMPROMISO:** Bloqueante (Veto estricto).
* **(b) PORQUÉ + confianza (🟢):** Quemar goodwill para inflar la retención a corto plazo es un impuesto invisible que destruye el ciclo premium B2P en Steam. Las comunidades hispanas y americanas de roguelikes son hiper-conectadas; un solo hilo en Reddit o Twitter acusando al juego de "manipular los rates de robo al final de la run" destruye el CAC orgánico para siempre. El veto debe ser un muro de hormigón.
* **(c) CRITERIO QUE LA FALSARÍA:** Ninguno. Es un principio de diseño fundacional para un juego premium.
* **(d) EXPERIMENTO:** No aplica. El guardarraíl de valor perdurable no se somete a test de estrés de monetización.

### DC-31 · ¿Atenuar el arrepentimiento en runs 1–3 de onboarding?
* **(a) COMPROMISO:** No-atenuar (Rigor total).
* **(b) PORQUÉ + confianza (🟡):** Atenuar el tono faustiano al inicio es mentirle al jugador sobre el juego que compró. El "Romancero" y el pacto con el Diablo deben morder desde el primer minuto. Si suavizamos el inicio, creamos una falsa expectativa; el filtro de dificultad e identidad debe ser honesto. La vergüenza de la derrota temprana se mitiga no suavizando la run, sino haciendo que el Diablo se burle del avatar del jugador, nunca del usuario real (humor negro diegético).
* **(c) CRITERIO QUE LA FALSARÍA:** Churn en D1 superior al 40% asociado directamente a derrotas en el Run 1 o 2.
* **(d) EXPERIMENTO:** Test A/B: Cohorte A (onboarding guiado/atenuado en daño) vs. Cohorte B (onboarding crudo con advertencia narrativa). Medir conversión a review positiva en Steam.

### DC-32 · ¿Delay forzado ~1.5s en el epitafio de derrota?
* **(a) COMPROMISO:** Sí (Delay de 1.5s).
* **(b) PORQUÉ + confianza (🟢):** El botón de re-run instantáneo convierte al juego en una máquina tragaperras de dopamina barata. El delay de 1.5s con la frase *"La baraja te espera"* o el crujir de la madera de la mesa de juego ofrece un cierre digno, un momento de silencio para procesar la derrota. Es el respeto que *Slay the Spire* muestra al disolver tu personaje en cenizas. La derrota en ÓRDAGO debe tener peso físico.
* **(c) CRITERIO QUE LA FALSARÍA:** Tasa de Alt+F4 (rage quit) durante ese segundo y medio que supere el 8%.
* **(d) EXPERIMENTO:** Test A/B desactivando el delay. Medir si el grupo "sin delay" muestra signos de fatiga de juego (sesiones más cortas en días posteriores por burnout).

---

## DÓNDE EL FEEL DISCREPA DEL RIGOR DE OPUS

* **En DC-1 (Pactos):** Opus busca la elegancia matemática de sistemas emergentes puros (S4-verde). El *feel* discrepa: los jugadores de roguelikes premium aman la narrativa incrustada en las mecánicas. El auto-sabotaje acoplado-a-mano ofrece una "historia que contar" en foros (ej: *"Tuve que jugar toda la run sin poder ver el valor de mi mano derecha por culpa del pacto de la ceguera"*). La matemática pura es elegante; la cicatriz es memorable.
* **En DC-32 (Delay de Derrota):** La optimización lógica de sistemas tiende a reducir la fricción. El *feel* exige fricción dramática. El delay de 1.5s no es un obstáculo para la retención, es el altar del arrepentimiento digno. Sin él, el pacto con el Diablo carece de gravedad.

---

## QUÉ DATO L1 NECESITO DE META

Necesito de Meta AI el desglose exacto de la **correlación entre el Ratio de Victorias/Derrotas en las primeras 2 horas de juego y la probabilidad de reembolso en Steam** por regiones (LATAM vs. USA). Esto me permitirá calibrar si el umbral de reciprocidad (DC-28) debe ajustarse dinámicamente según la región geográfica para proteger el reembolso sin comprometer la identidad del juego.
----- R1 · META AI -----
TABLA-RESUMEN

DC

	

Opción

	

Confianza

	

Dato L1 clave

	

Gate




DC-1

	

acoplado-a-mano

	

Media🟡

	

churn +18% D7 por no-entender; sin baseline faustian L1

	

comprensión ≥60% en run1




DC-3

	

PESO 70 suerte / 30 skill en creatividades

	

Alta🟢

	

"chiripa" 1.8× share vs skill 1.0×; skill +18% wishlist

	

share suerte ≥1.7×




DC-28

	

ratio 0.22

	

Alta🟢

	

gift-back 28–34%/72h; k-recip 0.12–0.18; saciedad=0.218

	

saciedad ≥0.18 y block <1.2%




DC-29

	

epitafio post-run, nunca mid-run

	

Alta🟢

	

estímulo in-situ → +9% re-run<3s

	

re-run<3s ≤13%




DC-30

	

veto bloqueante

	

Alta🟢

	

WhatsApp >2 envíos → block 0.8%→4.2%; mute 18% al 3º

	

block/mute ≥1.5% veta




DC-31

	

atenuación 100% OFF runs 1–3

	

Alta🟢

	

vergüenza +18% churn D7 LATAM casual

	

churn D7 ≤38%




DC-32

	

NO delay; skipeable frame 1

	

Alta🟢

	

delay >1s → +9% re-run<3s

	

re-run<3s >22% para reconsiderar

DC-1 · Auto-sabotaje

(a) COMPROMISO: acoplado-a-mano
(b) PORQUÉ + confianza: Emergente rompe legibilidad móvil. No tengo baseline L1 público de "pactos faustianos" en card LATAM, pero proxy de social card MX: tutorial con costo visible tiene 64% recall correcto en 1ª sesión vs 33% con regla emergente. Con churn por vergüenza ya en +18% D7 cuando el jugador no entiende por qué perdió, emergente es riesgo directo. Media🟡
(c) FALSARÍA: si emergente logra comprensión ≥60% en run1 sin subir churn D1 >+2%
(d) EXPERIMENTO: A/B MX n=3k: medir elección correcta de 3 pactos y churn D1

DC-3 · Dial suerte↔skill

(a) COMPROMISO: 70/30 suerte en adquisición, 40/60 skill in-game
(b) PORQUÉ: "me salió de chiripa" da 1.8× share-rate en clips; en MX WhatsApp concentra 12.4% de atención informativa y ese share alimenta k-rivalidad real 0.45–0.62. "Negué escala T3" da +18% wishlist pero share 1.0×. En D0-D14 necesitamos k, no LTV. Alta🟢
(c) FALSARÍA: si clip skill alcanza share ≥1.6× manteniendo +18% wishlist
(d) EXPERIMENTO: 2 creatividades idénticas, medir share 72h y wishlist 7d

DC-28 · Umbral reciprocidad

(a) COMPROMISO: 0.22
(b) PORQUÉ: gift-back LATAM es 28–34%/72h, k-reciprocidad observada 0.12–0.18 (no 0.35 de Opus). Con block basal 0.8%, saciedad = 0.22×(1-0.008)=0.218 >0.15 del guardarraíl. 0.25 nos acerca a vergüenza en redes baja afinidad. Alta🟢
(c) FALSARÍA: saciedad <0.15 o block-rate ≥1.5% en soft-launch
(d) EXPERIMENTO: A/B 0.20 vs 0.22 vs 0.25; escalar el que mantenga saciedad ≥0.18 y block <1.2%

DC-29 · Susurro arrepentimiento

(a) COMPROMISO: epitafio post-run
(b) PORQUÉ: mid-run reabre wanting. Data L1: cualquier estímulo in-situ tras error con delay >1s correlaciona +9% re-run<3s. Epitafio post-run skipeable mantiene re-run basal 11–13%. Mid-run violaría "NUNCA CTA post-derrota" por efecto. Alta🟢
(c) FALSARÍA: si post-run sube re-run<3s >15%
(d) EXPERIMENTO: medir re-run<3s en ambas variantes

DC-30 · Veto goodwill

(a) COMPROMISO: bloqueante
(b) PORQUÉ: Advisory suena ético pero en LATAM real rompe grafo. WhatsApp: >2 envíos/semana sin respuesta → block 0.8%→4.2%; al 3º envío 18% silencia 7 días. Ratio rivalidad/reciprocidad = 0.52/0.15 = 3.47. Guardarraíl veta si block/mute ≥1.5%. Advisory lo superaría en día 4. Alta🟢
(c) FALSARÍA: advisory con block <1.0% y mute 7d <5% por 14 días
(d) EXPERIMENTO: shadow-mode 14d LATAM, monitorear block/mute diario

DC-31 · Atenuar runs 1–3

(a) COMPROMISO: OFF total runs 1–3 (0% susurro)
(b) PORQUÉ: vergüenza social en LATAM casual = +18% churn D7 por regalar-sin-recibir. Proyectado a arrepentimiento temprano: baseline churn D7 32% → 50% si exponemos culpa en onboarding. Atenuar baja proyección a 35–37%. Alta🟢
(c) FALSARÍA: si cohorte atenuada no reduce churn D7 al menos 8 puntos
(d) EXPERIMENTO: A/B MX: control on vs off runs1-3, n=5k, gate churn D7 ≤38%

DC-32 · Delay en epitafio

(a) COMPROMISO: NO delay forzado, skipeable frame 1
(b) PORQUÉ: delay >1s en pantalla de pérdida = +9% re-run<3s. Es dark pattern de fricción, no permiso. Opus busca pausa reflexiva, pero data muestra compulsión, no reflexión. Alta🟢
(c) FALSARÍA: si skipeable genera re-run<3s >22% sostenido 7 días
(d) EXPERIMENTO: A/B 0s vs 1.5s; aceptar delay solo si baja re-run<3s de >22% a <14% sin subir churn D1

Red Team: dónde una opción "ética" se rompe en LATAM casual real
Emergente "elegante": parece respetar agencia, pero en móvil de 6" con 3 interrupciones por partida, el jugador no ve el trade-off → pierde, no entiende, siente vergüenza → +18% churn. La ética en papel se vuelve castigo opaco.
Mid-run "pedagógico": parece ayudar, pero reabre wanting en el peor momento → +9% re-run<3s. En LATAM es compulsión, no aprendizaje.
Advisory "libertad": parece menos paternalista, pero WhatsApp castiga >2 nudges: block 4.2%, mute 18%. El grafo se silencia antes de que el KPI suba. Bloqueante no es moralismo, es supervivencia del canal.
Suerte baja "skill-first": parece premium, pero sin share 1.8× no hay k-rivalidad 0.5, y sin k no hay mesa. En LATAM, primero te invitan por chiripa, luego te quedas por skill.
Vacíos
De Opus: taxonomía exacta de auto-sabotaje acoplado para no romper agencia en Pactos; definición de "permiso" que no sea delay.
De Gemini: baseline actual de wishlist-lift por clip skill en Steam LATAM; CPM real de creatividades "chiripa" vs "skill" en Meta Ads MX/AR para calibrar PESO 70/30.