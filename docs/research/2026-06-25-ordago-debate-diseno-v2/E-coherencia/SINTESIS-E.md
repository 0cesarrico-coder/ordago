# SÍNTESIS — Clúster E · Coherencia interna y carga cognitiva · ÓRDAGO

> Fusión de Opus (sistemas/sustracción) + Gemini (valor/narrativa) + Meta AI (data L1 móvil), R1+R2+referee.
> Referee: `contested=6 flipped=6 consensus=6 total=12 verdict=CONVERGED`.
> **Cluster con muchas concesiones** (6 flips, todos hacia el realismo móvil de Meta). Por eso separo con cuidado lo **CONSENSO 3/3** de lo que sigue **CONTESTADO** (decisión de César).

---

## 1. VEREDICTO (2-3 líneas)

**CONVERGE.** El cuello de botella NO es el número de sistemas, sino **(a) cuántas reglas verbaliza el jugador antes del 1er win** y **(b) cuántos focos compiten en el mismo frame** — una sola restricción vista en tiempo y en espacio. R2 cerró 6 ítems en consenso firme (varios emergieron solo en el cross-review); los 3 conflictos duros restantes (cardinalidad N, run continuo vs capítulos, lift del tease) son **decisiones de producto de César**, no desacuerdos de análisis. La compresión-arquetipo de Gemini ("el tahúr que engaña al Diablo") es el mecanismo que reconcilia profundidad de sistemas con la carga de onboarding móvil que exige Meta.

---

## 2. RESOLUCIONES POR HUECO

### #5 — Jerarquía Z / saliencia · CONSENSO 3/3 · 🟢
**Cambio al GDD (§10.2 + extiende §11/§14):** la jerarquía Z se define como **regla de scheduler, no de render**: `Z1 silueta(palo/figura) > Z2 valor(número) > Z3 estado(Trampa/Sospecha) > Z4 cascada/feedback`. Dos eventos Z3+ **NUNCA comparten frame**: se serializan en el tiempo (`Δt(Z3_a, Z3_b) ≥ 300 ms`, log verificable). Mata "papilla" con cero UI nueva.
- **Falsable (gate Z):** peor caso combinado (Trampa activa + Sospecha subiendo + cascada T3) a **100×100 px, escala de grises, simulación deuteranopia** → silueta+valor identificables por **≥9/10 testers** Y `≤1 evento Z3+/frame` (log). Segundo filtro L1-móvil: **demo web en gama media (Moto G 2022) ≥55 fps y bounce <35% @60s**, **≤100 componentes de render activos** y **≤3 elementos animados simultáneos**. MUERE si <9/10, solape en log, fps<55 o bounce≥35%.
- **Data L1 (Meta):** DOM/WebGL degrada >100 objetos; peores performers pierden 46% de installs antes del min5. La legibilidad@px y el conteo-de-reglas son la MISMA restricción.
- **CONTESTADO residual (🟡):** Meta pide **1 solape Z3 controlado por run** para preservar el "wow" viral (cascada simultánea +18-22% CTR en Reels); Opus/Gemini quieren serialización 100%. → ver Decisiones de César.

### #6 / #3 — Presupuesto de complejidad ≤7±2 + denominadores · CONTESTADO (convergencia parcial) · 🟡
**Cambio al GDD (extiende §14):** se adoptan **DOS denominadores explícitos**, no uno:
- **(i) `reglas_core ≤ 9`** (techo duro de scope; lista nominal abajo).
- **(ii) `reglas_verbalizadas_por_tester ≤ 5`** (techo duro de onboarding; **gana en conflicto**). Método: el tester verbaliza en voz alta antes de la Manga 1; si nombra un sistema meta (Codex, Romancero, artefacto-puente, Diablo Fantasma), ese sistema **entró demasiado pronto** (bug de onboarding). Si nombra "Maña" como 2 conceptos, cuenta 2.
- **Regla de conservación:** +1 sistema de delivery ⇒ −1 unidad de carga core percibida (no se acumula).
- **Compresión-arquetipo (de Gemini, elevada a REQUISITO):** cada regla-core necesita un **gancho cultural de 1 frase** que la haga *sentir* sin tutorial; si no comprime a arquetipo, **cuenta doble** en el techo de verbalizadas.
- **Fórmula de carga (Gemini):** `C = Reglas_activas × Canales_feedback_activos ≤ 12` por mano.
- **Lista nominal CORE de la 1ª victoria (denominador, Opus):** 1) Sumar 15 = Escoba; 2) la Mesa tiene cartas capturables; 3) el Diablo impone 1 Trampa; 4) la rompes con 1 Fullería; 5) romper sube Sospecha; 6) ~3 ranuras de Maña; 7) Maña = Fullería **o** Pacto (trade-off). = **7 core**. Meta/delivery gateado NO cuenta.
- **Falsable:** D1 ≥35% en MX/BR con ≤5 reglas verbalizadas y onboarding ≤180s. MUERE si verbalizadas >5 o si el tester nombra un sistema meta antes de la Manga 1.
- **Data L1 (Meta, 🟢):** estándar que escala enseña 3 acciones core <180s (Mob Control D1 36.1%); industria 2024 D1 26.5-27.7%, "bueno" 40%+; **cada regla verbalizada extra ≈ +45s a time-to-win y −6pp D1**.
- **CONTESTADO duro:** Meta poda Pactos del tutorial → 5 reglas (gana ~10pp D1) PERO Opus/Gemini avisan que quitar el trade-off Pacto↔Fullería del inicio convierte el juego en "Escoba de 15 con skins" (pierde identidad). **Fix de reconciliación (Gemini, fuerte):** NO podar, **serializar la introducción en 3 micro-mangas** (Mano 1: reglas 1-2; Mano 2: reglas 3-4; Mano 3: reglas 5-7 → gana en la mano 3). Aprendizaje progresivo, cero pérdida de identidad. → Decisión de César.

### #48 — Presupuesto temporal de run · CONSENSO 3/3 (banda casi idéntica) · 🟢
**Cambio al GDD (§9, tabla validada por solver §14):** `Σ(12 dientes) ∈ [25,35] min en p50; p90 ≤ 40 min`; banda por diente declarada (Manga ~6-8 min, Cantina ≤90s). La duración se **deriva de Maña** (ranuras gastadas + Escobas), no es variable de pacing libre.
- **Falsable:** solver §14 sobre 1000 runs. MUERE si p90 >40 min o Cantina percibida >90s. (Meta propone p90 ≤38; diferencia de ~2 min, no de principio.)
- **CONTESTADO (run continuo vs capítulos):** ver #48-bis en Decisiones de César.

### #49 — Micro-frecuencias intra-sesión (hook) · CONSENSO 3/3 (Opus y Gemini hicieron FLIP a 90s) · 🟢
**Cambio al GDD (§14, KPI):** `time_to_first_fullería_jugada` **p50 ≤ 90s** y `first_meaningful_choice < 90s`. (Opus bajó 120→90s; Gemini bajó 180→90s; Meta ancló en 90s.)
- **Falsable:** por logs. MUERE si p50 >120s (banda-muerte de Opus); Gemini+Meta firmes en 90s como objetivo.
- **Data L1 (Meta):** sesión móvil LATAM fragmentada ("abrir en el bus, pocos minutos"); 46% se va antes del min5 → hook obligatorio <90s.

### #24 — Codex terminal anti-FOMO · CONSENSO 3/3 en el principio · 🟢 (número N ⚪ → César)
**Cambio al GDD (§ Codex/Romancero):** colección **terminable con cardinalidad CONOCIDA** (`X/N` visible) + **beat de catarsis al 100%** (recompensa **estrictamente estética**: cantar de ciego ilustrado / skin de baraja), **SIN timer** (premium B2P). Límite de huecos activos simultáneos (anti ansiedad de completado): **máx 2-3 siluetas con pistas activas**; el resto en "niebla de leyenda". **Terminal ≠ saciado**: cada cierre destapa la silueta del siguiente hueco (el wanting se renueva por profundidad, no por infinitud — SEEKING saludable de Panksepp).
- **Falsable:** **D30 ≥8% sin timers** solo con progreso visible; **abandono en el rango 80-99% de completitud <5%**; alarma si ratio abiertos:cerrados crece monótonamente (señal de gap diseñado-para-no-cerrarse).
- **Data L1 (Meta):** D30 promedio 3-10%, bueno 10%+; colecciones completables retienen por curiosidad, no urgencia; el costo de NO usar FOMO es ~2-4pp D30, **aceptado por coherencia premium**.
- **CONTESTADO duro (cardinalidad):** Gemini N=16/M=24 (ambición narrativa) vs Meta N=12/M=18 (colecciones >12 ítems en móvil caen <5% completado, L1 🟢) vs Opus ⚪. → Decisión de César.

### #26 — Biblia del Mundo 1 pág · CONTESTADO (Meta disiente del valor-retención) · 🟡
**Cambio al GDD (§ Narrativa):** **1 página** con **5 hechos canónicos invariables** + **3 ambigüedades estructurales**; cada Diablo/Trampa/Fullería **linkea a 1 hecho o 1 ambigüedad** (coherencia falsable barata, costo mínimo). El flavor de victoria reacciona al **arquetipo de victoria** (Limpia-con-Maña vs Sucia-con-Sospecha) = **2 variantes/Diablo (~32 strings)**, NO a la matriz 16×24 = 384 strings (Gemini auto-podó este scope-creep en R2).
- **Posición Opus:** defender el linkeo como **no-contradicción**, NO como motor de D7.
- **Data L1 (Meta, 🟢):** en hybrid-casual LATAM el lore no mueve installs ni D7; UGC es brag, no teorías (<0.5% discuten lore sin incentivo). Falsable propuesto: >10% de sesiones abren el Romancero en D7, o se poda a texto lineal.
- **Cómo se zanja:** mantener la Biblia como **coherencia barata** (no se le pide D7); medir apertura del Romancero como señal secundaria. 🟡

### #39 — Expression visible (firma de build / sticker) · CONSENSO 3/3 · 🟢
**Cambio al GDD (§ Social/Sticker):** sticker exportable que prioriza **IDENTIDAD** ("Soy Escobero" + emblema estético del Diablo derrotado + **título dinámico de 2 palabras** por entropía de build, ej. "Soberbio Tramposo" / "Pactador Silencioso") y **oculta la solución-de-seed** (separar identidad-de-build de secuencia-de-jugadas protege el foso y el anti-spoiler). Silueta **limpia**, no cargada de iconos de 3 Pactos.
- **Falsable:** share-rate del sticker limpio supera al cargado por **>15%** en WhatsApp; el generador garantiza **≥8 arquetipos visualmente distinguibles** en 1000 victorias (si 90% se ven idénticos, se mata por falta de expresividad).
- **Data L1 (Meta, 🟢):** stickers personalizados se reenvían ~4.6× más que predeterminados; silueta limpia +18-22% CTR vs cargada; firma compleja ilegible a 32px.

### #12 — Tease de mañana · CONTESTADO (lift en disputa) · 🟡
**Cambio al GDD (§ Retención):** pantalla de salida muestra **silueta del siguiente Diablo + 1 rumor narrativo útil** para el build-crafting de la 1ª run del día siguiente, **opt-in, SIN timer** (info-gap de Loewenstein sin live-ops; respeta B2P).
- **CONTESTADO:** Gemini ≥12% lift D7 (optimista) vs Meta <3pp realista (tease pasivo sin trigger no mueve aguja en data Reels). **Se zanja por experimento:** A/B con gate **D7 lift ≥3pp vs control** en cohorte LATAM; si <3pp, **se poda** la pantalla para limpiar el flujo de salida.
- **Decisión de César asociada:** ¿el rumor **altera el seed** de la 1ª partida del día siguiente para garantizar utilidad, o es cosmético?

---

## 3. DECISIONES DE CÉSAR (zanjan conflictos duros / parámetros)

1. **Denominador de reglas / cardinalidad de onboarding (N de reglas):** ¿**onboarding estricto de ≤5 reglas** podando Pactos del tutorial (Meta, +~10pp D1, riesgo "Escoba con skins") **o tutorial serializado de 7 reglas en 3 micro-mangas** (Opus/Gemini, conserva identidad mecánica, gana en la mano 3)? *(Recomendación del panel: serializar en 3 mangas — reconcilia ambos; ≤5 verbalizadas vía compresión-arquetipo, 7 core descubiertas al jugar.)*
2. **Cardinalidad del Codex N (y M):** **N=16/M=24** (Gemini, ambición narrativa) vs **N=12/M=18** (Meta, protege D30 móvil; >12 ítems caen <5% completado) vs **abierto** (Opus ⚪). Conflicto duro, sin resolver por el panel.
3. **Run continuo vs capítulos (#48-bis):** **run continuo premium [25-35] min con auto-save instantáneo de estado** (Gemini, preserva flow tipo Inscryption/Balatro; cierras la app en cualquier turno y retomas) vs **4 mangas × 6-8 min con save entre mangas** (Meta, sesión móvil fragmentada; Opus concede). *(Posible reconciliación: run continua + auto-save por turno da casi lo mismo que capítulos sin romper flow.)*
4. **Serialización de cascadas:** **serializar 100% Z3+** (Opus/Gemini, claridad máxima) vs **permitir 1 solape Z3 controlado por run** (Meta, preserva "wow" viral +18-22% CTR Reels). Trade-off legibilidad vs viralidad.
5. **Recompensa del 100% del Codex:** **estrictamente estética** (cantar de ciego/skins, protege anti-FOMO; voto de Opus+Gemini) vs **desbloquea "Diablo Fantasma" como boss mecánico final** (afecta balance).
6. **Hook 90s vs 120s:** casi resuelto en 90s; César fija si acepta 90s (máx D1) o 120s (margen de feel/setup de la Mesa viva). Cada 30s ≈ trade-off D1 vs profundidad.
7. **Biblia del Mundo:** ¿se valida alguna teoría de la comunidad en updates, o se mantiene hermética para siempre?
8. **Poda de Diablo Fantasma + artefacto-puente del onboarding:** Meta los marca "capa sin lift D1 medible"; ¿se podan del onboarding manteniéndolos como meta gateado?

---

## 4. PARA EL GDD v1.3 — lista accionable (§ → qué)

- **§10.2** → definir Jerarquía Z como **regla de scheduler** (Z1>Z2>Z3>Z4) con `≤1 evento Z3+/frame`, `Δt≥300 ms`. [#5, 🟢]
- **§11 / §14 (Gate Z)** → añadir test peor-caso @100×100px grises+deuteranopia (≥9/10) + filtro L1-móvil (≥55 fps, bounce <35% @60s, ≤100 render, ≤3 animados). [#5, 🟢]
- **§14 (Gate de complejidad)** → **dos denominadores**: `reglas_core ≤9` + `reglas_verbalizadas ≤5` (gana este); conteo por verbalización del tester; regla de conservación delivery↔core; fórmula `C = reglas × canales ≤12/mano`. [#6/#3, 🟡]
- **§ Onboarding** → compresión-arquetipo como REQUISITO (1 frase cultural por regla-core o cuenta doble); resolver vía César el formato (5 reglas podadas vs 3 micro-mangas). [#6/#3]
- **§9 (tabla de presupuesto temporal)** → `Σ12 dientes ∈ [25,35] p50, p90 ≤40 min`, duración derivada de Maña, validada por solver §14. [#48, 🟢]
- **§14 (KPI hook)** → `time_to_first_fullería_jugada p50 ≤90s`, `first_meaningful_choice <90s`; banda-muerte >120s. [#49, 🟢]
- **§ Codex/Romancero** → `X/N` visible + beat 100% estético + sin timer + máx 2-3 siluetas activas + cada cierre destapa siguiente silueta; gates D30≥8%, abandono 80-99% <5%. Cardinalidad N pendiente de César. [#24, 🟢/⚪]
- **§ Narrativa (Biblia)** → 1 pág (5 hechos + 3 ambigüedades), cada Diablo linkea 1 hecho/ambigüedad; flavor reactivo por arquetipo de victoria (~32 strings, NO 384); medir apertura Romancero D7 como señal secundaria, no gate de retención. [#26, 🟡]
- **§ Social/Sticker** → identidad ("Soy Escobero" + emblema + título 2 palabras), oculta solución-de-seed, silueta limpia; gates share-rate +15% y ≥8 arquetipos distinguibles/1000. [#39, 🟢]
- **§ Retención (Tease)** → silueta siguiente Diablo + rumor útil, opt-in sin timer; A/B con gate D7 lift ≥3pp o se poda; decidir si altera seed (César). [#12, 🟡]
- **§ Balance (complementariedad)** → solver §14: existe ≥1 estado de Mesa con EV(Pacto)>EV(Fullería); viabilidad Pacto ∈ [20%,50%] / Fullería no domina >85% sobre 1000 seeds. [#6, 🟢]
