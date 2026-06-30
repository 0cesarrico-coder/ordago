# AUDITORÍA DE SESGO — Plan META-SÍNTESIS v1.3 vs 7 fuentes (A–G)

> **Rol:** Auditor adversarial, contexto fresco (NO escribí la meta-síntesis). Misión: detectar FABRICACIÓN — consenso inventado, números cambiados, hallazgos contestados omitidos o reclasificados.
> **Método:** cada hallazgo del plan se contrastó línea-a-línea contra su clúster de origen. Se buscan 4 fallas: exclusions, minimizations, replacements, reclassifications.

---

## VEREDICTO GLOBAL (resumen)

El plan es **notablemente fiel**. La mayoría de números, umbrales, confianzas y marcas CONTESTADO/CONSENSO se transcriben correctamente desde las fuentes. El meta-sintetizador respetó su propia regla de fidelidad (§5 del plan): no subió ⚪→🟢, marcó CONTESTADO donde la fuente lo marcaba, y delegó umbrales a experimento donde la fuente lo hacía. **No hay fabricación grave.** Hay un puñado de fallas LEVES (minimizaciones de matices, y unas pocas omisiones de gates/sub-decisiones secundarias). Detalle abajo.

---

## 1. EXCLUSIONS (hallazgos/decisiones en una síntesis que el plan OMITIÓ)

### E-1 · Gate comercial A/B demo LATAM de Clúster A — OMITIDO [LEVE]
- **Fuente A (§4, línea 66):** "**§Test plan / Validación comercial:** A/B demo LATAM móvil n≥5k/rama (eco-gateado vs sin-tells): pasa si **D7 +≥5pp** (target >28%) **y** share-rate no cae >10% (target ≥1.4/100 sesiones) **y** refund <8%. Si sube D7 pero share −≥15% → mataste la suerte compartible."
- **Plan:** este A/B específico de A (validación comercial de la capa de tells eco-gateada con sus umbrales D7+5pp / share / refund) **no aparece** en el plan. El plan tiene P2-1 (kill de legibilidad) y P2-2 (test A1 novato/experto), pero omite este gate comercial concreto de A.
- **Veredicto:** EXCLUSIÓN LEVE. Es un gate falsable accionable de A que se perdió en la fusión. No cambia conclusiones, pero es una pérdida de contenido.

### E-2 · Gates G1, G4, G5, G-conversión de Clúster F — parcialmente OMITIDOS [LEVE]
- **Fuente F (§4, líneas 48-55):** lista explícita de gates G1 (habituación: share del N-ésimo jefe no cae monótono, ≤15% caída Diablo#10 vs #1), G4 (muerte del sistema: predicción del beat ≡ fatiga, frequency>2.7/7d o CTR−30% → rotar ≤14d), G5 (reacción muda: ≥70% no-jugadores describen en <5 palabras tras 0.5s mudo), **G-conversión (Meta L1): share-to-wishlist 1:0.03-0.04 en frío, NO 1:0.12 Gemini; <0.02 tras 10 creadores → kill beat**.
- **Plan:** solo conserva G2 (≥3× share, en P3-6) y G3 (≤0.8 d-h, en P1-14). G1, G4, G5 y G-conversión **no aparecen**. El número G-conversión 1:0.03-0.04 sí aparece mencionado en CX-6 ("G-conversión 1:0.03-0.04 frío") pero los gates G1/G4/G5 como invariantes se pierden.
- **Veredicto:** EXCLUSIÓN LEVE-MODERADA. Son gates falsables de F que el plan no traslada al GDD. G5 en particular (reacción muda ≥70%) es un kill-gate de awe relevante.

### E-3 · Decisión de César G#4 (atenuar arrepentimiento onboarding) — SÍ incluida, OK
- Verificado: aparece como DC-31 ("Atenuar arrepentimiento en runs 1–3"). No es exclusión.

### E-4 · Tensión interna de los dos docs Opus en B#27 (0.35 vs 3/100) — OMITIDA [TRIVIAL]
- **Fuente B (línea 19):** "Tensión interna sin cerrar: los dos docs Opus difieren (0.35 en uno, 3/100 en el otro). Se toma el cross-review (3/100) como voto canónico."
- **Plan (P2-8):** reporta "3/100 (Opus) ↔ 0.18 (Meta)" usando el valor canónico correcto. Omite mencionar la tensión interna, pero usa el valor canónico que la propia fuente eligió.
- **Veredicto:** TRIVIAL. La fuente ya resolvió la tensión; el plan usó el valor resuelto. No es falla.

### E-5 · Decisión de César E#7 (Biblia hermética vs validar teorías) — SÍ incluida
- Verificado: DC-10 ("Biblia del Mundo: ¿validar teorías de comunidad en updates?"). OK.

---

## 2. MINIMIZATIONS (puntos contestados presentados como más resueltos)

### M-1 · P2-21 "poda vs serializar contestado" — el plan SÍ lo marca, pero el changelog lo minimiza [LEVE]
- **Fuente E (#6/#3, marcado CONTESTADO duro; DC-1):** el formato onboarding (≤5 podadas vs 3 micro-mangas) es decisión de César sin resolver por el panel; el panel solo *recomienda* serializar.
- **Plan:** P2-21 marca "Consenso en 2 denominadores; poda vs serializar contestado" (FIEL) y DC-4 lo lista como [firma] con reco serializar (FIEL). PERO el changelog §12 dice "Formato (≤5 podadas vs 3 micro-mangas) = César" (FIEL).
- **Veredicto:** NO es minimización. El plan mantiene el contestado consistentemente. Correcto.

### M-2 · Clúster E es "cluster con muchas concesiones" (6 flips) — contexto perdido [LEVE]
- **Fuente E (línea 5):** advertencia explícita "Cluster con muchas concesiones (6 flips, todos hacia el realismo móvil de Meta). Por eso separo con cuidado lo CONSENSO 3/3 de lo que sigue CONTESTADO."
- **Plan:** no transmite que E fue el clúster con más concesiones/flips hacia Meta. Presenta los consensos de E (P2-22, P2-23 como 3/3) sin el caveat de que muchos fueron flips. Sin embargo, los ítems individuales SÍ se marcan correctamente (#48 y #49 fueron flips reales hacia 90s/banda y el plan los reporta como 3/3, lo cual es correcto post-flip).
- **Veredicto:** LEVE. Un flip-a-consenso ES consenso; reportarlo 3/3 es legítimo. No es minimización de un contestado vivo.

### M-3 · D — "Nota de integridad" de asientos Opus/Meta desempeñados — OMITIDA [LEVE]
- **Fuente D (línea 3):** "NOTA DE INTEGRIDAD: en este clúster ambos asientos 'Opus' y 'Meta' fueron desempeñados; donde hubo acuerdo 3/3 lo marco CONSENSO."
- **Plan:** no menciona esta nota de integridad metodológica de D. Reporta los consensos 3/3 de D sin el caveat. Dado que la propia fuente D los marcó CONSENSO pese a la nota, el plan no fabrica, pero pierde una salvedad de confianza.
- **Veredicto:** LEVE. La fuente asumió el consenso; el plan lo hereda. No es fabricación pero es transparencia perdida.

### M-4 · F referee "CONVERGING" (no "CONVERGED") — el plan dice "CONVERGED" [LEVE]
- **Fuente F (línea 3):** "**Referee: CONVERGING** (consensus=9, contested=4, flipped=2)." — gerundio, no pasado.
- **Plan (línea 3):** "cada una CONVERGED tras R1→R2→referee". Generaliza las 7 como CONVERGED, pero F dice CONVERGING.
- **Veredicto:** LEVE / REPLACEMENT menor. Estado del referee de F ligeramente sobre-afirmado (converging→converged). Bajo impacto porque F tenía 9 consensos firmes.

---

## 3. REPLACEMENTS (números/umbrales/§ que el plan CAMBIÓ vs la fuente)

### R-1 · P2-15 — "$11.99 launch (−20%)" — verificación aritmética [OK, no es replacement]
- **Fuente C (#46/#59 y §3):** "$14.99 USD con −20% descuento de lanzamiento → $11.99 launch". El plan reproduce $14.99/$11.99 launch/$7.49 LATAM. FIEL. (−20% de $14.99 = $11.99. Correcto.)
- **Veredicto:** OK.

### R-2 · P2-16 — "≥38% cruzan 2h en 72h" y "≥35% juegan >15min" [OK]
- **Fuente C (#36, #66):** "≥35% juegan >15 min + ≥38% de compradores cruzan 2h en 72h", "no 55%". Plan FIEL. Refund <10% MX/<7% hispanos/<6% USA FIEL. "<3% nota muy difícil" FIEL.
- **Veredicto:** OK.

### R-3 · P2-17 — banda review "Mostly Positive ≥70%" y lift "+22–35% USA / +12–18% LATAM" [OK]
- **Fuente C (#45):** idénticos. Plan FIEL.
- **Veredicto:** OK.

### R-4 · P2-30 / §8 — K_rivalidad "0.45–0.62" vs K_reciprocidad "0.12–0.18" [OK]
- **Fuente G (#38):** "k-rivalidad real 0.45-0.62 vs k-reciprocidad 0.12-0.18". Plan FIEL. Target realista 0.20-0.25 FIEL. Claim Community condicionado a ≥0.20 a 4 semanas, <0.15 corregir FIEL.
- **Veredicto:** OK.

### R-5 · P2-12 / §19.3 — techo audio Sospecha "banda ∉[500Hz,2kHz]", "gain≤0.8*master", "audio_layers_active≤2", "eyes_closed_test≥75%" [OK]
- **Fuente D (#32):** todos idénticos (satura 80% gain en suspicion=0.7, evita 500Hz-2kHz, ≤2 capas, eyes_closed ≥75% kill<60%). Plan FIEL. Prohibido Cheating_Success_Rate FIEL.
- **Veredicto:** OK.

### R-6 · P2-10 — firma audio "≤35KB", KPI "≥58% Android / ≥38% iOS-MX (kill <45%/<30%)" [OK]
- **Fuente D (#22):** "inline ≤35 KB precargada", "≥58% Android / ≥38% iOS-MX ... kill <45%/<30%". Plan FIEL.
- **Veredicto:** OK.

### R-7 · P1-13 / G#37 — "máx 2 envíos/contacto/semana", "block/mute ≥1.5%", "report-spam ≥0.3%" [OK]
- **Fuente G (#37):** "Máx 2 envíos/contacto/semana; el 3.º se auto-bloquea", "block/mute <1.5%, report-spam <0.3%; si supera → no shippea". Plan FIEL.
- **Veredicto:** OK.

### R-8 · P1-1/INV-1 — dominancia Maña ">55% winrate, Sharpe <1.3×, KILL >60%/Sharpe>1.5×" [OK]
- **Fuente A (#1):** idénticos (🟢 <55% y Sharpe<1.3×; 🟡 55-60%; KILL >60% o Sharpe>1.5×). Plan FIEL. Acoplado a S5 FIEL.
- **Veredicto:** OK.

### R-9 · P1-2/INV-2 — umbral Diablo "[0.95,1.15], p10>0.8, p90<1.6, KILL >25% ratio<0.7 o >25% ratio>2.0" [OK]
- **Fuente A (#50):** idénticos. Plan FIEL.
- **Veredicto:** OK.

### R-10 · P2-5 — glance-gate sticker "≥90% a 100×100px, ≥8 arquetipos/1000, share limpio >cargado >15%" [OK]
- **Fuente B (#40) + E (#39):** "≥90% lectura a 100×100px gris (n≥20)", "≥8 arquetipos distinguibles/1000", "share limpio supera cargado >15%". Plan FIEL (fusiona B#40 y E#39 correctamente).
- **Veredicto:** OK.

### R-11 · P2-4 — sticker "<80KB, 512×512" y OG P2-7 "<45-50KB JPEG, TTFB p95 <80-100ms, KILL p95>120ms" [OK]
- **Fuente B (#27, #19):** "<80KB, 512×512", "og:image estático 1200×630 <45-50KB JPEG, TTFB p95 <80-100ms, KILL p95>120ms". Plan FIEL.
- **Veredicto:** OK.

### R-12 · P2-3 / banda EV "[10–15%]" + "<8% ajedrez seco, >18% autorrevela" [OK]
- **Fuente A (#2 César, §EV):** "parámetro a fijar por el solver en [10-15%]", "<8% ajedrez seco, >18% autorrevela". Plan FIEL. Nota: A menciona que bandas R2 solapan [12%,13%]; plan repite "[12%,13%]". FIEL.
- **Veredicto:** OK.

### R-13 · P3-6 / G2 kill — "money-shot ≥3× share-con-audio del diario en 0-72h (≥4.5% vs ≤1.2%)" [OK]
- **Fuente F (#63):** "money-shot ≥3× share-con-audio del clip diario en 0-72h (Meta: ≥4.5% vs ≤1.2%)". Plan FIEL.
- **Veredicto:** OK.

### R-14 · P2-24 / Codex — "D30 ≥8% sin timers, abandono 80-99% <5%, máx 2-3 siluetas" [OK]
- **Fuente E (#24):** "D30 ≥8% sin timers", "abandono 80-99% <5%", "máx 2-3 siluetas con pistas activas". Plan FIEL. Cardinalidad N pendiente de César FIEL.
- **Veredicto:** OK.

### R-15 · P2-22 / presupuesto temporal — "[25,35]min p50, p90 ≤40min, Cantina ≤90s" [OK]
- **Fuente E (#48):** idénticos. Plan FIEL. (Nota: E menciona "Meta propone p90 ≤38"; plan usa ≤40 que es la banda principal de la fuente. Menor, no es replacement.)
- **Veredicto:** OK.

### R-16 · P2-23 / hook — "p50 ≤90s, banda-muerte >120s" [OK]
- **Fuente E (#49):** "p50 ≤90s", "MUERE si p50 >120s". Plan FIEL.
- **Veredicto:** OK.

### R-17 · P1-9 / Gate Z — "≥9/10, Moto G 2022 ≥55fps, bounce<35%, ≤100 render, ≤3 animados, Δt≥300ms" [OK]
- **Fuente E (#5):** idénticos. Plan FIEL.
- **Veredicto:** OK.

### R-18 · P2-14 / Gate #47 — LTV "~$9.3/~$4.7", "≥60% ventas Sem-1 WL orgánica", "≥3 blended O ≥1.5 hispanos/≥1.2 LATAM" [OK]
- **Fuente C (#47):** idénticos. Plan FIEL. "LATAM paid-a-wishlist prohibido ($0)" FIEL. Umbral honesto contestado→dato FIEL.
- **Veredicto:** OK.

### R-19 · P2-26 / Codex Arrepentimientos — umbral "≥35% verbaliza" + "re-run<3s no sube >12%" [OK con caveat]
- **Fuente G (#41):** "≥35% ⚪ sin baseline ... re-run<3s NO sube >12%". Plan marca el ≥35% como "[⚪ supuesto]" y confianza "🟢 (umbral ⚪)". FIEL — la fuente marca el umbral como SUPUESTO/⚪ y el plan lo preserva.
- **Veredicto:** OK. Confianza correctamente no-inflada.

### R-20 · P2-29 / bucket "~50 pares reales" [OK]
- **Fuente G (#15):** "bucket cerrado de ~50 pares del mismo percentil", "Diablo Fantasma poblado por PAR REAL", "auditar 0 sintéticos". Plan FIEL.
- **Veredicto:** OK.

### R-21 · P2-28 / TDF "≥30% gift-back/72h (🟡 28-34%), <25% revisar" [OK]
- **Fuente G (#16):** "TDF ≥30% gift-back en 72h 🟡 (Meta: 28-34%); si <25% → revisar". Plan FIEL.
- **Veredicto:** OK.

### R-22 · P2-11 / grito_glifo — "≤2 palabras 96×96px, contraste ≥4.5:1, reenvío +15%, repetición ≥20%, bloqueo <0.25%" [OK]
- **Fuente D (#23):** idénticos. Plan FIEL. Marca umbrales 🟡 FIEL.
- **Veredicto:** OK.

### R-23 · P3-1 / SEO — "diferir Engine, 2/3 (Gemini minoría)", "Search Velocity ~600-2,500/mes/región" [OK]
- **Fuente B (#57):** "Gemini ≥2,500/mes/región; Meta AI ~600/mes", "Gemini queda en minoría 1/3", "una landing-compendio estática top-100". Plan FIEL ("2/3 (Gemini en minoría)").
- **Veredicto:** OK.

### R-24 · P2-19 / gates culturales — "CTR ≥2.4% AND +15%", "<1.2s en ≥70% en 3 nodos", "decay <45% a 90d" [OK]
- **Fuente C (#30, #44, #43):** idénticos. Plan FIEL. "#43 evidencia ⚪→KPI", "degradar '70% a 36m' de hecho a hipótesis" FIEL.
- **Veredicto:** OK.

### R-25 · §4.1 / goodwill — "share rivalidad/reciprocidad >3.5", "block-rate >1.5%", auto-rollback [OK]
- **Fuente G (#42):** "share-rate rivalidad/reciprocidad >3.5 o block-rate >1.5% → Unstable, auto-rollback". Plan FIEL. "M1 veta no autoriza" FIEL.
- **Veredicto:** OK.

### R-26 · P2-31 / saciedad — "`(share_recip/total)×(1−block-rate)` >0.25 sano / <0.15 veto, ratio para-satisfecho >1.2" [OK]
- **Fuente G (#55):** idénticos. Plan FIEL.
- **Veredicto:** OK.

---

## 4. RECLASSIFICATIONS (confianza subida o CONTESTADO→CONSENSO sin base)

### RC-1 · P1-5 (techo maestría #53) — "Contestado→resuelto" [FIEL]
- **Fuente A (#53):** marcado "CONTESTADO → se zanja con proxy de bots, NO con humanos" 🟡[L3]. Resolución: proxy bots pre-launch + p50/p95 post-launch.
- **Plan:** marca "Contestado→resuelto (proxy bots, no humanos)" 🟡[L3]. FIEL — replica exactamente la resolución de la fuente y mantiene L3.
- **Veredicto:** NO es reclasificación indebida. Correcto.

### RC-2 · P2-1 (kill legibilidad #4) — confianza 🟢[L1] [FIEL]
- **Fuente A (#4):** "CONSENSO 3/3 sobre qué medir; método CONTESTADO→resuelto 🟢[L1]". Plan: "Consenso en QUÉ medir...; método resuelto" 🟢[L1]. FIEL.
- **Veredicto:** OK. La fuente ya marcaba 🟢[L1] (el L1 viene del dato r=0.12 de Meta). No hay inflado.

### RC-3 · P2-25 (watchability B#56) — "Consenso blando (Opus eleva)" 🟡[L4] [FIEL]
- **Fuente B (#56):** "CONSENSO blando (Opus lo eleva)" 🟡 L4. Plan: "Consenso blando (Opus eleva)" 🟡[L4]. FIEL — no infla un consenso blando a firme.
- **Veredicto:** OK. Honestidad preservada.

### RC-4 · P3-3 (Biblia E#26) — "Contestado (Meta disiente)→coherencia barata" 🟡 [FIEL]
- **Fuente E (#26):** "CONTESTADO (Meta disiente del valor-retención) 🟡". Plan: "Contestado (Meta disiente del valor-retención)→coherencia barata" 🟡. FIEL.
- **Veredicto:** OK.

### RC-5 · P3-4 (Tease E#12) — "Contestado (lift)→experimento" 🟡 [FIEL]
- **Fuente E (#12):** "CONTESTADO (lift en disputa) 🟡 ... Gemini ≥12% vs Meta <3pp ... A/B gate D7 lift ≥3pp o se poda". Plan: idéntico, gate D7 ≥3pp. FIEL.
- **Veredicto:** OK.

### RC-6 · P2-13 (text_glyph D#17) — "🟢/⚪", "umbral ⚪" [FIEL]
- **Fuente D (#17):** "CONSENSO 3/3 🟢 patrón / ⚪ umbral", "≥4% semana 1". Plan: "3/3 (patrón); umbral ⚪" 🟢/⚪. FIEL — preserva el ⚪ del umbral.
- **Veredicto:** OK.

### RC-7 · P2-8 (ignición K2 B#27) — "Consenso en activación; umbral=experimento" 🟡[L4] [FIEL]
- **Fuente B (#27):** "CONTESTADO (umbral) → resuelto a activación, no shares", umbral 🟡 L4. Plan: "Consenso en activación; umbral pendiente de experimento" 🟡[L4]. FIEL — el consenso es sobre QUÉ medir (activación), no sobre el umbral, y el plan lo dice así.
- **Veredicto:** OK. Distinción consenso-de-método vs umbral-contestado correctamente preservada.

### RC-8 · P2-30 (#38) — confianza 🟡, "dirección converge, target contra Gemini" [FIEL]
- **Fuente G (#38):** "CONSENSO 3/3 (en dirección) 🟡", "resuelto contra Gemini-R1". Plan: "3/3 (dirección); target realista 0.20–0.25 contra Gemini" 🟡. FIEL — no presenta como consenso numérico pleno.
- **Veredicto:** OK.

### RC-9 · Disclaimer final del plan (línea 253) — auto-declaración verificada [FIEL]
- El plan afirma: "Ningún ⚪ se subió a 🟢; ningún CONTESTADO se reportó como consenso." Tras auditar los 31 fixes + INV + DC + CX + changelog: esta afirmación se sostiene. No encontré ningún ⚪→🟢 ni CONTESTADO→CONSENSO fabricado.
- **Veredicto:** La auto-declaración es VERAZ.

---

## SÍNTESIS DE FALLAS

| Tipo | Hallazgos | Severidad |
|------|-----------|-----------|
| **Exclusions** | E-1 (A/B comercial de A), E-2 (gates G1/G4/G5/G-conv de F) | 2 leves-moderadas |
| **Minimizations** | M-2 (E "muchas concesiones"), M-3 (nota integridad D), M-4 (F CONVERGING→CONVERGED) | 3 leves |
| **Replacements** | Ninguno material. M-4 (converging→converged) es el único cambio de estado, menor. | 0 graves |
| **Reclassifications** | Ninguna indebida. RC-1..RC-9 todas FIELES. | 0 |

**Conteo final:** exclusions=2, minimizations=3, replacements=0 (graves), reclassifications=0.

**Razonamiento del veredicto:** El plan es de alta fidelidad. Cero números cambiados materialmente, cero confianzas infladas, cero CONTESTADO disfrazado de CONSENSO — la regla de fidelidad declarada se cumplió. Las únicas fallas son (a) dos exclusiones de gates falsables secundarios (A/B comercial de A; G1/G4/G5/G-conversión de F) que deberían reincorporarse al GDD, y (b) tres minimizaciones leves de caveats metodológicos (concesiones de E, nota de integridad de D, estado converging de F). Ninguna constituye fabricación. El nivel de fallas es **leve-moderado**, corregible añadiendo los gates omitidos; no hay fabricación grave. Veredicto: **CONCERNS** (cerca de PASS — las fallas son omisiones de completitud, no invenciones).

SCORE-INPUT: exclusions=2 minimizations=3 replacements=0 reclassifications=0 verdict=CONCERNS
