## DEBATE ETAPA 2 — Afilar los FIXES de clase mundial (eje: DISEÑO + ENTREGA, no research de negocio)

Un workflow de 135 agentes ya cazó 93 huecos de clase mundial en el GDD v1.1 de ÓRDAGO (roguelike
deckbuilder con baraja española; verbo = hacerle trampa al Diablo en una Mesa viva). El diagnóstico:
el VERBO ya es clase mundial; lo que está lejos del #1 es la CAPA DE ENTREGA — "valor declarado sin
máquina detrás". Tu trabajo NO es re-encontrar huecos: es **debatir y converger en los MEJORES FIXES**
para las 3 palancas mayores, a vara de "el mejor juego del mundo". Aprovecha tu ventaja de datos/prior.

### LAS 3 PALANCAS A AFILAR (+ 1 decisión de César)
1. **PALANCA 1 — El artefacto-puente canónico (§8.3 nuevo).** El GDD apuesta TODO su CAC~0 a la
   viralidad pero el único output hoy es "código de build" (antipatrón D1: no cruza ningún chat). Hay
   que definir el OBJETO exacto que dispara el crecimiento. Pregunta dura: ¿qué se comparte y se GUARDA
   de verdad en WhatsApp/IG/TikTok entre hispanos (LATAM + hispanos-USA)? ¿Un emoji-grid copiable estilo
   Wordle (0 servidor)? ¿Un clip 6-8s con audio del barrido + "¡tramposo!"? ¿Ambos, y cuál primero?
   ¿Cómo se evita el spoiler de semilla? ¿Cómo se ata a "le robé el alma a [tu primo]"? (Cartas D1, C2 K=i×c, D3 audio.)
2. **PALANCA 2 — El generador de bifurcación + el foso VIVO.** La elegancia (A1) hoy es una promesa
   ("la siembra del Diablo produce ≥2 jugadas correctas") tratada como kill-test a-posteriori, no como
   invariante diseñada; y nadie vigila la entropía de builds en el tiempo (la dominante oculta colapsa
   el meta a D7-D14 sin alarma). ¿Cómo se DISEÑA el generador (tempo-vs-escala, valor futuro divergente
   de cada captura) para garantizar ≥2 jugadas Pareto-no-dominadas? ¿Qué instrumentación vigila el foso
   vivo en EA (entropía de builds por cohorte, test del experto)? (Carta A1.)
3. **PALANCA 3 — Reconciliar plataforma↔viralidad↔economía (§16.1).** "CAC~0 vía WhatsApp" + "premium
   Steam $15-20" se contradicen (el link aterriza en paywall) y no hay un solo número de unit-economics.
   ¿Cuál es el modelo que de verdad cierra para LATAM + USA + hispanos-USA? Aterriza cifras realistas:
   precio neto (-30% Steam), conversión wishlist→venta, refund, CAC por canal, payback, LTV/CAC por
   columna (USA / hispanos-USA / LATAM). (Cartas L3 unit-economics, L7 plataforma, D1, B5 fricción-cero.)
4. **DECISIÓN DE CÉSAR C-1 (informarla, no zanjarla):** web-native-first vs Steam-first vs híbrido
   (Steam premium + demo web ligera de 1 mano como artefacto-puente jugable). ¿Cuál maximiza llegar al
   #1 sin romper el linaje premium ni el motor viral? Da tu recomendación con su porqué y su trade-off.

### REGLAS
- Especificidad obligatoria: cifras, rangos, ejemplos concretos; si no tienes un dato, dilo.
- Jerarquía de evidencia: L1 data real de plataforma (Meta Ads/analytics) > L2 industria citable >
  L3 patrón de entrenamiento > L4 razonamiento. Etiqueta tus afirmaciones empíricas 🟢/🟡/⚪ y marca
  el nivel; "validar en cohorte propia" donde aplique. No fabriques certeza.
- Ancla los juicios de diseño a las cartas (A1, D1, C2, D3, L3, L7, B5, M1·LD7) con confianza.
- Mercado: LATAM + USA general + hispanos-USA (sweet spot). Modela por segmento, no asumas piso LATAM.
- Piso ético M1/LD7 inviolable (nada de FOMO fabricado / compulsión como motor de viralidad).
- Falsabilidad: cada fix con (a) el cambio concreto al GDD, (b) criterio de kill, (c) el test más barato.

### FORMATO DE SALIDA — RONDA 1
Para CADA palanca (1, 2, 3): tu **mejor fix de clase mundial** (concreto, anclado, con cifras donde
puedas), el **riesgo principal + mitigación**, y el **test/kill más barato**. Luego tu **recomendación
sobre C-1** (web/Steam/híbrido) con porqué y trade-off. Cierra con tu **apuesta falsable**: "ÓRDAGO no
llegará al #1 a menos que ___." Sé un red-team honesto, no un validador.
