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