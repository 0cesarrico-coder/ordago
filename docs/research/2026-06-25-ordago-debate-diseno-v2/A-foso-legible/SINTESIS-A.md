# SÍNTESIS · Clúster A "El foso es invisible" (foso legible + invariantes)

**Síntesis de:** opus-r1/r2, gemini-r1/r2, meta-ai-r1/r2, referee-r2 · **Veredicto del referee:** CONVERGED (contested=2, flipped=5, consensus=7, total=9).

---

## 1. Veredicto del clúster

El debate convergió fuerte: de ~5 ejes en disputa en R1 a 2 en R2, con 5 flips hacia el centro y **cero atrincheramiento**. El principio rector quedó zanjado 3/3: **la legibilidad del foso (Tempo/Escala/Defensa) vive en el OUTPUT retrospectivo post-captura — nunca en el input prospectivo** — gateada y desvaneciente con la maestría. Los dos únicos contestados restantes (spread de EV exacto y forma fina del eco) no son desacuerdos de principio sino **calibración numérica que zanja el solver/experimento, no más debate**.

---

## 2. Resoluciones de clase mundial (por hueco)

### #2 — Tells de eje (Tempo/Escala/Defensa) — **CONSENSO 3/3** 🟢[L4]
**Cambio al GDD (§UI/§14.0):** Pintar el **PREDICADO** (estado del mundo), nunca el **SUJETO** (la carta a capturar).
- **NO** colorear ninguna carta candidata, **NO** iconos prospectivos en hover/long-press (Espada/Engranaje/Escudo de Gemini quedó **dominado** y absorbido — además "no hay hover en touch", Meta). La Mesa solo resalta sumas de 15.
- **SÍ** dos capas: **(Capa-1, estado)** banner minimal de Trampa activa / función-de-palo, 4-6 palabras, lectura <450ms; **(Capa-2, eco retrospectivo)** al capturar, destello 150-200ms + háptico distinto por eje, **solo tras ≥2 repeticiones de esa jugada**, desvanece a ~run 4. "Memoria muscular, no UI" (fusión telltale-Opus + eco-Meta).
- Criterio falsable: **Test del experto (A1)** — mismo seed+build, novato vs experto deben **divergir en jugada**; si convergen → el tell se volvió solver §317 → KILL.

### #4 — Onboarding del verbo correcto (kill de legibilidad) — **CONSENSO 3/3** sobre qué medir; método CONTESTADO→resuelto 🟢[L1]
**Cambio:** Eliminar "≥70% nombran el eje" (auto-confirmante; **r=0.12 con D30** en card games LATAM, dato L1 Meta — los 3 lo concedieron). Reemplazar por candado **vocabulario-ciego**:
- **Kill primario (comportamiento, no verbalización):** Opus = **L-b predicción contrafáctica** ("si capturabas la otra, el Diablo…"), ≥50% aciertan, 2 jueces κ≥0.6; Meta = **comprensión implícita**, ≥55% eligen la jugada Pareto en escenario espejo tras 3 runs **sin poder nombrar el eje**. **Convergen: ambos miden HACER, no DECIR.** Para el GDD se adoptan los dos como complementarios (predecir + elegir).
- **Diagnóstico no-bloqueante:** verbalización de eje se reporta como salud de comunicabilidad, **no como kill**.

### #35 — Glance gate del eje — **CONSENSO 3/3** 🟢[L4]
**Cambio:** El glance valida **score**, no decisión. Rechazado el "halo Pareto por eje always-on" (los 3: = solver §317). El estado (Trampa/función-de-palo) es leíble <0.5s pero es **contexto, no respuesta**. Cuidado anti-papilla: +3 iconos estáticos = +120ms de decisión, −9% completion en sesión muda móvil (Meta [L1]). Presupuesto perceptual finito (ÓRDAGO ya carga 4 cartas mesa + mano + Trampa).

### #1 — Dominancia de Maña (builds de Pactos) — **CONSENSO 3/3 en el test; cura = decisión de César** 🟡[L4]
**Cambio (§14.0, paso solver S4):** Sobre 100 tableros/seed × matriz de builds extremas (0F/3P, 3F/0P, 2/1, 1/2): **🟢** ninguna build >55% winrate y Sharpe (winrate/σ) <1.3× la 2ª; **🟡** 55-60%; **🔴 KILL** >60% winrate o Sharpe >1.5× la 2ª. Meta matiza: S4 sin la curva del Diablo (#50) es síntoma, no causa — medir **acoplado a S5**.

### #50 — Escalado del umbral del Diablo — **CONSENSO 3/3** 🟡[L4]
**Cambio (§14.0, paso solver S5):** Mediana de `score_logrado/umbral` por banda ∈ **[0.95, 1.15]**, p10>0.8, p90<1.6 = 🟢; [0.85,1.25] = 🟡; **🔴 KILL** si >25% seeds `ratio<0.7` (muralla) o >25% `ratio>2.0` (trivial).

### #53 — Techo de maestría (brecha p50-p95) — **CONTESTADO → se zanja con proxy de bots, NO con humanos** 🟡[L3]
- Meta: medir p50-p95 con humanos pre-launch = **vaporware** (varianza = ruido de aprendizaje, no señal). **Aceptado.**
- Opus: **proxy de bots de política fija** falsable HOY sin humanos — delta `bot_lookahead_k − bot_greedy_1ply` por banda de profundidad de Mesa. **Clase mundial = delta CRECE monótono con k; KILL = se aplana a k≥2** (no hay recompensa a la secuenciación). Meta no refutó el proxy de bots (solo la versión humana) pero advierte que sobre-estima techo humano (los bots no se frustran). **Resolución: usar el proxy de bots como gate pre-launch + confirmar p50/p95 reales post-launch** por banda 0-10/10-50/50h+.

### #8 — FTUE / 2 perfiles (novato vs maestría) — **CONSENSO 3/3** 🟡
**Cambio (§14.0, paso solver S7):** FTUE = ≥1 dominante-tempo legítima, spread <8%; Maestría = ≥2 Pareto, spread en banda. **KILL** si FTUE tiene 2 Pareto reales en turno-1 (rompe flow) o Maestría tiene 1 dominante (rompe foso). Gemini/Meta refuerzan: la asistencia de "sumar 15" es el **ancla cultural hispana** — no quitarla para forzar teoría de ejes.

### #6/#3 — Ratio reglas (composabilidad/elegancia) — **CONSENSO 3/3** 🟡
**Cambio (§14.0, paso solver S6):** Contar **working-set en la mano-pico de decisión** (no reglas totales; Miller 7±2 aplica al working set), verbalizado por **tester naïve** (no el diseñador = teatro). 🟢 ≤6 reglas y ninguna Fullería ("Ojo del Tahúr") en >70% de builds óptimas; **🔴 KILL** >7 reglas working-set o una Fullería en >85% de builds óptimas (colapsó el trade-off a "siempre lo llevo" → no es decisión). Meta matiza: S6 es teatro si no se mide también **carga visual** (banner permanente +120ms).

---

## 3. Decisiones de César (trade-offs reales, NO zanjables por diseño)

1. **Apetito de auto-sabotaje estructural en los Pactos (#1).** S4 *detecta* dominancia pero no *prescribe la cura*. Dos filosofías: **(A) emergente** — confiar en que S4-verde basta (más elegante, riesgo de que una build se cuele; A1 la prefiere); **(B) acoplado a mano** — cada Pacto fuerte lleva un auto-sabotaje diseñado que una Fullería específica resuelve (más control, presiona S6; el riesgo de producto la prefiere). **Apetito de riesgo de César, no data.**

2. **Banda de EV objetivo (el único contested numérico real).** Las 3 bandas R2 ya **se solapan en [12%, 13%]**: Opus [10-15%] centro ~13%, Gemini→12-16%, Meta 9-13%. **Delegado explícitamente al solver** (se fija donde S4-S7 co-pasan). César fija el número final viendo 100 tableros/seed. Nota de papel: <8% = "ajedrez seco" (bajo el ruido); >18-20% = el tell autorrevela la jugada (recrea §317).

3. **Dial revelar↔ocultar (suerte↔skill) = identidad del producto.** Meta lo plantea como dial irreconciliable ("taquería: 'me salió de chiripa', viral/+1.8x share" vs "Discord: 'negué su escala turno 3', cola larga/+18% wishlist"). **Opus lo reconcilia como SECUENCIA, no elección:** suerte en la **superficie de marketing/UA** (artefacto-puente viral, top del funnel), skill en el **cuerpo del loop** (foso legible, LTV/D30). El **peso** de cada capa sigue siendo apetito de César.

---

## 4. Para el GDD v1.3 — ediciones accionables

- **§UI / Tells:** Especificar regla dura "**predicado, no sujeto**": cero coloreado de cartas candidatas, cero iconos prospectivos de eje, cero hover/halo Pareto. Mesa limpia salvo resaltar sumas de 15.
- **§UI / Capa-1 (estado):** Banner minimal de Trampa activa + función-de-palo, 4-6 palabras, <450ms lectura. Permanente pero auditar coste de papilla (+120ms).
- **§UI / Capa-2 (eco retrospectivo):** Destello 150-200ms + háptico por eje (Tempo/Escala/Defensa), gateado tras ≥2 repeticiones de la jugada, desvanece ~run 4. "Memoria muscular, no UI".
- **§Onboarding / FTUE:** Mantener la asistencia "sumar 15" (ancla cultural hispana, no desactivar por defecto). FTUE = dominante-tempo legítima; profundidad de ejes llega en maestría.
- **§14.0 Solver — añadir pasos S4-S7** con umbrales V/A/KILL exactos de la sección 2 (Maña #1/S4, umbral Diablo #50/S5, composabilidad #6/S6, FTUE #8/S7). S4 **acoplado a S5**.
- **§14.0 / Techo:** Añadir proxy de bots (delta lookahead-k vs greedy-1ply, debe crecer monótono con k; KILL si se aplana a k≥2) como gate pre-launch para #53; p50/p95 reales post-launch.
- **§Test plan / Kill de legibilidad (#4):** Sustituir "≥70% nombran eje" por candado vocabulario-ciego: predicción contrafáctica (≥50%, κ≥0.6) **+** elección Pareto en escenario espejo (≥55%) tras 3 runs. Verbalización = diagnóstico, no kill.
- **§Test plan / Validación comercial:** A/B demo LATAM móvil n≥5k/rama (eco-gateado vs sin-tells): pasa si **D7 +≥5pp** (target >28%) **y** share-rate no cae >10% (target ≥1.4/100 sesiones) **y** refund <8%. Si sube D7 pero share −≥15% → mataste la suerte compartible → re-evaluar capa de UA.
- **§EV:** Dejar la banda como **parámetro a fijar por el solver en [10-15%]** (no hardcodear un número en el GDD hasta correr 100 tableros); documentar criterio (<8% ajedrez seco, >18% autorrevela).
- **§Identidad (marco común):** Adoptar el **diagnóstico Balatro** como invariante de diseño — transparencia en el cálculo táctico (output del turno), opacidad en la composición meta (Pactos/Maña).
