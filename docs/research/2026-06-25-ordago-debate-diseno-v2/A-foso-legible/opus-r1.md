# Debate ÓRDAGO · Clúster A "El foso es invisible" · RONDA 1 · ASIENTO OPUS

**Rol:** Diseñador de Sistemas (carta A1, rigor de elegancia/emergencia). Lidero el espacio-de-decisión, no el mercado.

---

## TESIS CENTRAL

El fix del clúster es **correcto en su arquitectura pero peligroso en su default**. La legibilidad debe vivir en el *output* (mostrar **consecuencia**, no **solución**) y gatearse — eso es Church + Rosewater bien aplicado. Pero el "tell de eje" tal como está enunciado (color/forma sobre *la carta a capturar*) **recrea el solucionador-parcial §317**: si pinto la jugada Pareto, regalo el verbo. La salida elegante es **mover el tell del SUJETO al PREDICADO**: no marcar *qué captura* es escala/defensa, sino exponer la **función-de-palo y la Trampa** (el *estado del mundo*) y dejar que el jugador derive la jugada. Y casi todos los "kills" propuestos son **falsables solo si se fija el protocolo de medición ahora** — varios, tal como están, son auto-confirmantes o vaporware. Los reparo abajo con números.

---

## 1. STEELMAN del fix (la versión más fuerte)

**Por qué la legibilidad debe vivir en el output y gatearse — es correcto:**

- **Church 🟢[L2]:** una decisión sin *consecuencia perceptible <1s* degrada a azar. Si el jugador no puede *post-hoc* leer por qué su captura fue buena/mala, el foso tempo/escala/defensa es vocabulario designer-side y el juego se *siente* RNG aunque sea determinista. El output (feedback tras capturar) es donde la consecuencia se vuelve perceptible **sin** ser predictiva. Esto es lo que SALVA al fix: legibilidad *retrospectiva* ≠ solver *prospectivo*.
- **Rosewater/lenticular 🟢[L2]:** misma regla, dos lecturas. Gatear (ON ~3 runs, luego desvanece) implementa el lenticular en el *eje temporal del jugador*, no en el tablero: el novato ve andamiaje, el experto ve el tablero desnudo. Mismo sistema, dos profundidades.
- **A1🟢🟡:** subir el numerador (jugadas) sin subir el denominador (reglas). El tell de eje no añade una regla nueva al verbo; reexpone información ya presente en la Mesa con redundancia perceptual (forma+color, accesibilidad). Es *traducción*, no *mecánica*.
- **01🟢:** "escala el reto con el poder". El gateo es exactamente eso: el andamiaje se retira a la misma velocidad a la que sube la competencia, así mejorar no trivializa.

**Conclusión del steelman:** el principio es sólido. La legibilidad del *valor-futuro* pertenece al output y debe gatearse. El error no está en el QUÉ sino en el DÓNDE se pinta el tell y en QUÉ se mide.

---

## 2. ATAQUE / MEJORA

**(a) Dónde recrea el solver §317 — el tell sobre la carta-a-capturar.** 🟢[L4]
Si pinto de color-escala la carta que conviene capturar, **regalo la jugada Pareto**. El §317 ya advierte: el resaltado de *Mesa* cruza a solucionador-parcial bajo Mesa poblada. Un "tell de eje always-on sobre el sujeto de la captura" ES el solver, con otro nombre. **Rechazo el halo Pareto-por-eje always-on** (coincido con el fix de #35) y voy más lejos: lo rechazo **también gateado sobre el sujeto**, porque enseña al jugador a *leer el color en vez de leer el tablero* — entrena la muleta, no el verbo (anti-Rosewater: el andamiaje debe enseñar a ver, no a obedecer).

**(b) ¿"≥70% nombran el eje" es falsable o auto-confirmante?** 🟡[L4]
Tal como está, **auto-confirmante**: si el tester puede *nombrar* "escala" porque la palabra está pintada en pantalla, está leyendo la UI, no razonando el foso. Mide reconocimiento de etiqueta, no comprensión de decisión. **Falsable solo si:** (i) el think-aloud es **ciego al vocabulario** (no se le dan las palabras tempo/escala/defensa; se codifica *post-hoc* si su justificación mapea a un eje de futuro), y (ii) se exige **predicción contrafáctica**: "¿qué habría pasado si capturabas la otra?". Reconocer ≠ predecir.

**(c) ¿La curva p50-p95 (#53) es medible pre-lanzamiento o vaporware?** 🟡
Pre-lanzamiento con N humano grande = **vaporware**. PERO tiene un proxy duro: **bots de política fija** (greedy-tempo, greedy-escala, lookahead-k) corriendo sobre el solver. La "brecha de skill" pre-lanzamiento = **delta de score entre bot-greedy-1-ply y bot-lookahead-k-ply** por banda de dificultad. Si ese delta CRECE con la profundidad de la Mesa, hay techo de secuenciación. Si se aplana, no lo hay. Es falsable hoy, sin un solo humano.

**(d) ¿Contar "reglas verbalizadas ≤5-7" es gate o teatro?** 🟡
**Teatro si lo cuenta el diseñador** (sesgo de subestimar lo propio). **Gate real si:** (i) lo cuenta un tester naïve verbalizando "las reglas que crees que rigen" tras 1ª victoria, y (ii) se cuenta **carga simultánea en memoria de trabajo en la mano del pico de decisión**, no reglas totales del manual. Miller 7±2 aplica al *working set*, no al corpus. Reformulo el gate en §3.

---

## 3. RESOLUCIÓN DE CLASE MUNDIAL (números falsables)

### (a) Diseño del tell de eje — la distinción Church que NO regala el solver 🟢[L4]
**Principio: pinta el PREDICADO (estado del mundo), no el SUJETO (la jugada).**
- **NO** se colorea ninguna carta candidata a capturar.
- **SÍ** se exponen 2 *capas de estado* gateadas, leíbles <0.5s:
  1. **Función-de-palo / Trampa activa** (banner de regla): "Oros no cuentan" / "suma 13" — esto es el *contexto*, no la respuesta.
  2. **Telltale de consecuencia POST-captura** (output puro): al capturar, un flash de 0.4s codifica en qué eje pesó la jugada (tempo=destello limpieza, escala=la carta vuela a tu motor, defensa=la carta se "apaga" en la mano del Diablo). **Retrospectivo, nunca prospectivo.**
- **Gateo idéntico al modo aprendiz:** la capa-1 persiste (es info de reglas, accesibilidad permanente); la capa-2 (telltale) ON ~3 runs y se desvanece.
- **Test del experto (A1):** mismo seed+build a novato y experto deben **divergir en jugada**. Si convergen, el tell se volvió solver → falla.

### (b) Los 4 nuevos pasos del solver §14.0 (umbrales V/A/KILL)
Sobre **100 tableros/seed × matriz de builds**, todos deterministas:

| # | Paso | Métrica | 🟢 Verde | 🟡 Amarillo | 🔴 KILL |
|---|------|---------|----------|-------------|---------|
| **S4** | **Dominancia de Maña (#1)** | win-rate de cada build extrema (0F/3P, 3F/0P, 2/1, 1/2) sobre seeds, controlado por varianza | ninguna build >55% win-rate **ni** Sharpe (winrate/σ) >1.3× la 2ª mejor | una build 55-60% | cualquier build **>60%** win-rate **o** Sharpe >1.5× la 2ª → hay dominante → A1 ordena rediseño de trade-off, no nerf |
| **S5** | **Balance de umbral del Diablo (#50)** | mediana de `score_logrado/umbral` por banda | mediana ∈ **[0.95, 1.15]** y p10>0.8, p90<1.6 | mediana ∈ [0.85,1.25] | >25% de seeds `ratio<0.7` (muralla) **o** >25% `ratio>2.0` (trivial) |
| **S6** | **Composabilidad / elegancia (#6/#3)** | (i) reglas en working-set en mano-pico (tester naïve); (ii) ¿"Ojo del Tahúr" se lleva en >X% de builds óptimas? | ≤**6** reglas working-set **y** ninguna Fullería en >70% de builds óptimas | 7 reglas / Fullería en 70-85% | >7 reglas working-set **o** una Fullería en **>85%** de builds óptimas → colapsó el trade-off a "siempre lo llevo" → no es decisión |
| **S7** | **2-perfiles FTUE/maestría (#8)** | spread-EV objetivo por perfil | FTUE: ≥1 dominante-tempo legítima, spread <8%; Maestría: ≥2 Pareto, spread en banda | borde | FTUE con 2 Pareto reales en turno-1 (rompe flow) **o** Maestría con 1 dominante (rompe foso) |

### (c) Kill de legibilidad 🟡
Reemplazo "≥70% nombran el eje" (auto-confirmante) por **doble candado**, vocabulario-ciego:
- **L-a (comprensión):** ≥**60%** de testers, en think-aloud sin palabras-eje dadas, justifican una captura con un **eje de futuro** (escala/defensa), codificado post-hoc por 2 jueces (κ≥0.6). Tempo solo NO cuenta (es el verbo viejo).
- **L-b (predicción):** ≥**50%** predicen correctamente el contrafáctico ("si capturabas la otra, el Diablo…"). Este es el candado anti-muleta: separa leer-la-UI de entender-el-foso.

### (d) Métrica de techo (brecha p50-p95) 🟡
**Proxy pre-lanzamiento (sin humanos):** delta de score `bot_lookahead_k − bot_greedy_1ply` por banda de profundidad de Mesa.
- Clase mundial = **delta CRECE monótono** con k y con horas-equivalentes de dificultad.
- KILL = el delta se **aplana** a k≥2 (no hay recompensa a la secuenciación → no hay techo 50h+).
**Post-lanzamiento:** confirmar con p50 vs p95 reales de score por banda 0-10/10-50/50h+; la brecha debe seguir abriéndose.

### Banda de EV (~8-15% vs 15-20%) — argumento de elegancia, no de feel 🟡[L4]
Se zanja por **Meier**, no por gusto. Una decisión es interesante si **no hay dominante** (descarta spread bajo: <8% → diferencias bajo el ruido perceptual → "ajedrez seco" porque las opciones *son* casi idénticas, no porque falte caos) **y** si **no todo equivale** (descarta spread alto: >20% → una opción domina perceptualmente → puzzle de máximo). El óptimo elegante es la banda donde **el ranking de opciones cambia según el ENTORNO (build/Trampa) pero no según ruido**. Mi predicción de papel: **[10%, 18%]**, centro **~14%** — suficiente para que el orden Pareto *exista* y sea *sensible al contexto*, no tanto que se *autorrevele*. **Pero esto lo decide el solver S0**, no yo: se fija al spread donde S4-S7 pasan simultáneamente. Si solo pasan a 15-18%, Gemini tiene razón; si a 10-13%, Opus/Meta. **Es empírico, no retórico.**

---

## 4. QUÉ ES DECISIÓN DE CÉSAR (trade-off que NO zanjo)

1. **Cuánto auto-sabotaje estructural en los Pactos (#1).** El test S4 *detecta* dominancia pero no *prescribe la cura*. Hay dos curas y son filosofías distintas: **(A)** confiar en que S4-verde basta (trade-off emergente del sistema) — más elegante, más riesgo de que una build se cuele bajo el umbral; **(B)** acoplar pares a mano (cada Pacto fuerte lleva un auto-sabotaje diseñado que una Fullería específica resuelve) — más control, más reglas (presiona S6). **A1 prefiere (A); el riesgo de producto prefiere (B).** No lo zanjo: es apetito de riesgo de César.
2. **La banda de spread de EV** se fija tras ver el solver (sección 3 cierre). Yo entrego la *predicción de papel* [10-18%] y el *criterio* (donde S4-S7 co-pasan); **César fija el número final** viendo los 100 tableros.
3. **Coste de accesibilidad del tell** (forma+color redundante, telltales) vs minimalismo visual del Style Bible — trade-off estético que toca arte, no sistemas.

---

**Resumen de confianza:** arquitectura del fix 🟢; tell-en-predicado 🟢[L4]; umbrales numéricos S4-S7 🟡 (calibrar con solver real); banda EV 🟡 (empírica); proxy de techo por bots 🟡 (sólido pero no validado en este juego).
