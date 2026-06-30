# META-SÍNTESIS v1.3 — Auditoría de SESGO FRESCO (iter1)

> Auditor adversarial sin contexto previo (no escribió ni auditó antes el plan). Misión: detectar
> FABRICACIÓN en 4 categorías — **exclusions** (contestados/decisiones omitidos), **minimizations**
> (contestado presentado como resuelto), **replacements** (números/§ alterados vs fuente),
> **reclassifications** (confianza subida o CONTESTADO→CONSENSO sin base). Cita fuente vs plan + veredicto.

---

## A. REPLACEMENTS (números / § alterados) — verificación dura

| Claim del plan | Fuente | ¿Fiel? |
|---|---|---|
| Estados referee A,B,C,D,E,G=CONVERGED; **F=CONVERGING** (consensus=9, contested=4, flipped=2) | A L3 CONVERGED; B L3 CONVERGED; C L3 CONVERGED; D L3 CONVERGED; E L4 CONVERGED; F L3 **CONVERGING (consensus=9, contested=4, flipped=2)**; G CONVERGED | ✅ EXACTO. El plan NO sobre-afirma F a CONVERGED (lo dice explícito). |
| P1-1 S4: ninguna build >55%, Sharpe <1.3×; 🟡 55–60%; KILL >60% o Sharpe >1.5× | A #1 L30: idéntico (🟢 >55%/Sharpe<1.3×; 🟡 55-60%; 🔴 KILL >60%/Sharpe>1.5×) | ✅ EXACTO |
| P1-2 S5: mediana ∈[0.95,1.15], p10>0.8, p90<1.6; KILL >25% ratio<0.7 o >25% ratio>2.0 | A #50 L33: idéntico | ✅ EXACTO |
| P1-3 S6: ≤6 reglas, ninguna Fullería >70%; KILL >7 o Fullería >85% | A #6/#3 L43: idéntico | ✅ EXACTO |
| P2-1: eliminar "≥70% nombran eje" (r=0.12 con D30); predicción contrafáctica ≥50% κ≥0.6 + Pareto ≥55% | A #4 L22-23: "r=0.12 con D30"; "≥50%, 2 jueces κ≥0.6"; "≥55% eligen la jugada Pareto" | ✅ EXACTO |
| P2-15: $14.99 / $11.99 launch (−20%) / $7.49 LATAM | C §3: "$14.99 / $11.99 launch / $7.49 LATAM" | ✅ EXACTO |
| P2-16: ≥35% >15min, ≥38% cruzan 2h/72h (no 55%) | C #36 L32: idéntico, "NO el 55%" | ✅ EXACTO |
| P2-17: Mixed→Mostly Positive ≥70%; +22–35% USA / +12–18% LATAM; primeras 10 reviews en 4h | C #45 L36: idéntico | ✅ EXACTO |
| P2-14 LTV neto-refund ~$9.3 / ~$4.7 | C #47 L16: "~$9.3 USA·hispanos / ~$4.7 LATAM" | ✅ EXACTO |
| P2-25c G-conversión 1:0.03–0.04 frío (NO 1:0.12 Gemini); <0.02 tras 10 creadores → kill | F §4 L54: idéntico | ✅ EXACTO |
| P2-25c G5 reacción muda ≥70% en <5 palabras tras 0.5s mudo | F §4 L53: idéntico | ✅ EXACTO |
| P1-14 cap G3 ≤0.8 días-hombre/dosis; Casta A ~5 full / Casta B ~15 ligeras | F #28/#29 L17-18: idéntico | ✅ EXACTO |
| P2-30 k-rivalidad 0.45–0.62 vs k-reciprocidad 0.12–0.18; target realista 0.20–0.25 | G #38 L32-33: idéntico | ✅ EXACTO |
| P1-13 máx 2 envíos/contacto/semana; block/mute <1.5%, report-spam <0.3% | G #37 L37-39: idéntico | ✅ EXACTO |
| P2-22 Σ12 dientes ∈[25,35] p50, p90 ≤40; Cantina ≤90s | E #48 L36: idéntico | ✅ EXACTO |
| P2-23 hook p50 ≤90s; banda-muerte >120s | E #49 L41-42: idéntico | ✅ EXACTO |
| INV-13 eyes_closed_test ≥75% (kill <60%) | D #32 L52: "eyes_closed_test ≥75% ... kill <60%" | ✅ EXACTO |
| P2-10 firma_heard_first_session ≥58% And/≥38% iOS-MX (kill <45%/<30%) | D #22 L23: idéntico | ✅ EXACTO |

**Replacements detectados: 0.** Muestreo amplio (~17 números/umbrales de los 7 clústeres) no halló un solo número, banda ni KILL alterado. Las §GDD citadas (§14.0, §10.2, §18, §7.6d, etc.) coinciden con las fuentes.

---

## B. RECLASSIFICATIONS (confianza subida / CONTESTADO→CONSENSO sin base)

Reviso cada caso donde el plan declara 🟢 o "3/3" o "resuelto", contra la marca de la fuente.

1. **P1-5 (techo maestría, A#53)** — Plan: "Contestado→resuelto (proxy bots, no humanos)", conf 🟡[L3].
   Fuente A #53 L35: "**CONTESTADO → se zanja con proxy de bots, NO con humanos** 🟡[L3]".
   → El plan NO lo lava a CONSENSO; mantiene la traza de que fue contestado y la resolución es por
   proxy (mecanismo que la propia fuente adopta). **FIEL.** ✅

2. **P1-6 / INV-4 (Pacto↔Fullería, E#6)** — Plan: Consenso 3/3, 🟢.
   Fuente E: #6/#3 está marcado **CONTESTADO (convergencia parcial) 🟡** en su encabezado (L23), PERO
   la sub-resolución de complementariedad Pacto↔Fullería aparece en la lista accionable L94 como
   "**[#6, 🟢]**" y el contenido (EV(Pacto)>EV(Fullería) en ≥1 estado; viabilidad [20%,50%]; no domina
   >85%) es CONSENSO. → El plan toma la pieza 🟢 correcta (balance), no el encabezado 🟡 (onboarding).
   Sutil pero **DEFENDIBLE**: son sub-ítems distintos del mismo hueco. ⚠️ menor (ver minimizations).

3. **P1-7 (tells predicado, A#2/#35)** — Plan: 3/3, 🟢[L4]. Fuente A #2 L15 "CONSENSO 3/3 🟢[L4]". ✅ FIEL.

4. **P2-4 (sticker autocontenido, B#27/#40/#65)** — Plan: 3/3, 🟢[L1/L2]. Fuente B #40 L25 "CONSENSO 3/3 🟢 L1/C1"; #27 L16 "CONSENSO 3/3 🟢 L2". ✅ FIEL.

5. **P2-8 (K2, B#27)** — Plan: "Consenso en activación; umbral = experimento", 🟡[L4].
   Fuente B #27 L17: activación 3/3 pero "umbral está CONTESTADO ... lo zanja un experimento 🟡 L4".
   → El plan separa correctamente "consenso en QUÉ medir" de "umbral contestado". **FIEL.** ✅

6. **P2-14 (gate #47, C#47)** — Plan: "Consenso en aritmética; umbral honesto contestado→dato", 🟡[L2].
   Fuente C #47 L15: "**CONTESTADO (lo zanja la data medida)** 🟡 L2". → El plan conserva el estatus
   contestado del umbral honesto y lo delega al dato, no lo declara resuelto. **FIEL.** ✅

7. **P2-19 (#43 anti-decay, C#43)** — Plan: "#43 evidencia ⚪→KPI", 🟡/⚪.
   Fuente C #43 L50: "**CONTESTADO (evidencia ⚪, debe volverse KPI)** ⚪ L4". → El plan degrada de hecho
   a hipótesis-con-KPI igual que la fuente; NO sube ⚪ a 🟢. **FIEL.** ✅

8. **P2-25 (watchability, B#56)** — Plan: "Consenso blando (Opus eleva)", 🟡[L4].
   Fuente B #56 L40: "**CONSENSO blando (Opus lo eleva)** 🟡 L4". ✅ FIEL — preserva el "blando".

9. **P2-26 (Codex Arrepentimientos, G#41)** — Plan: 3/3, 🟢 (umbral ⚪).
   Fuente G #41 L15: "CONSENSO 3/3 🟢"; el umbral ≥35% marcado "[umbral SUPUESTO ... ⚪ sin baseline]".
   → El plan marca el umbral como ⚪ explícitamente ("Gate: ≥35% ... [⚪ supuesto]"). **FIEL.** ✅

10. **P3-1 (SEO Engine, B#57)** — Plan: "2/3 (Gemini en minoría)", 🟡[L3].
    Fuente B #57 L45: "Gemini queda en minoría 1/3"; "CONSENSO 3/3 en construir solo el MEDIDOR". → El
    plan reporta 2/3 sobre DIFERIR el Engine (correcto: Gemini=motor, otros 2=diferir). **FIEL.** ✅

11. **P3-3 (Biblia del Mundo, E#26)** — Plan: "Contestado (Meta disiente del valor-retención)→coherencia barata", 🟡.
    Fuente E #26 L51: "**CONTESTADO (Meta disiente del valor-retención)** 🟡". ✅ FIEL — mantiene el contestado.

12. **P2-13 (text_glyph, D#17)** — Plan: "3/3 (patrón); umbral ⚪", 🟢/⚪.
    Fuente D #17 L66: "CONSENSO 3/3 🟢 patrón / ⚪ umbral". ✅ FIEL.

**Reclassifications fabricadas: 0.** Cada 🟢 verificado corresponde a un 3/3 real en la fuente; cada
⚪ supuesto se preserva como ⚪; cada CONTESTADO de umbral se reporta como contestado/experimento.
El plan respeta su propia regla declarada (L7, L257): "ningún ⚪ se subió a 🟢; ningún CONTESTADO se
reportó como consenso". 1 caso ⚠️ MENOR (P1-6) donde se elige la cara 🟢 de un hueco de encabezado
🟡, pero es defendible porque la sub-resolución de balance SÍ es 🟢 en la propia fuente (E L94).

---

## C. MINIMIZATIONS (contestado presentado como resuelto)

1. **P1-6 / encabezado E#6** — El encabezado del hueco #6/#3 en la fuente es CONTESTADO 🟡 (poda vs
   serializar onboarding). El plan disuelve #6 en DOS fixes: P1-6 (balance, 🟢, legítimamente consenso)
   y P2-21 (carga cognitiva, donde SÍ marca "poda vs serializar contestado" y lo manda a DC-4). →
   El aspecto contestado NO se pierde: vive en P2-21 + DECISIÓN DE CÉSAR #4. **NO es minimización.** ✅

2. **CX-4 serialización Z3** — Plan resuelve el money-shot dentro de la serialización y dice
   explícitamente "Queda como decisión de César (E-DC4) solo si se quisiera un solape DENTRO del loop".
   Fuente E #5 L21 + DC#4 L74: el solape-en-loop sigue contestado. → El plan NO declara cerrado lo que
   sigue abierto; acota la resolución al money-shot y preserva el contestado del loop. **FIEL.** ✅

3. **P2-3 / banda EV (A)** — Plan: "Contestado→delegado al solver". Fuente A §3 L51: "Delegado
   explícitamente al solver". → Coincide; no se presenta como número fijado. **FIEL.** ✅

4. **Caveats metodológicos** — El plan INCLUYE (L4-L5) los dos caveats que un sintetizador sesgado
   tendería a borrar: (a) E = "el de más concesiones, 6 flips hacia Meta"; (b) D = "nota de integridad,
   mismo operador en asientos Opus y Meta". Fuente E L5 y D L3 lo dicen; el plan los preserva
   literalmente en vez de minimizarlos. **Anti-minimización activa.** ✅✅

**Minimizations: 0.** El plan tiende a lo contrario (preserva caveats incómodos).

---

## D. EXCLUSIONS (contestados / decisiones de César omitidos)

Conté las Decisiones de César de cada fuente vs §5 del plan:

- **A**: 3 DC (auto-sabotaje Pactos, banda EV, dial suerte↔skill) → plan §5 #1,#2,#3. ✅ las 3 presentes.
- **E**: 8 DC (denominador onboarding, cardinalidad N, run vs capítulos, serialización cascadas,
  recompensa 100% Codex, hook 90/120, Biblia, poda Diablo Fantasma) → plan §5 #4–#12 (incluye tease
  #12). ✅ las 8 presentes.
- **C**: 2 DC (EA vs 1.0, precio) + umbral honesto → plan §5 #13,#14,#15. ✅ presentes.
- **B**: 5 DC (beacon vs cero-backend, umbral K2, SEO Engine, pre-compromiso KILL, reparto sticker/clip)
  → plan §5 #16–#20. ✅ las 5 presentes.
- **D**: 4 DC (nº nodos grito, textura Sospecha, grito_glifo en caption, emoji-artefacto) → plan §5
  #21–#24. ✅ las 4 presentes.
- **F**: 3 DC (nº money-shots, reparto arte, Condena endless) → plan §5 #25,#26,#27. ✅ las 3 presentes.
- **G**: 5 DC (umbral reciprocidad, susurro mid vs post, veto bloqueante vs advisory, atenuar
  arrepentimiento onboarding, delay epitafio) → plan §5 #28–#32. ✅ las 5 presentes.

**Total DC en fuentes: 3+8+2+5+4+3+5 = 30. En el plan §5: 32 entradas (incluye el umbral honesto C
como #15 separado y mantiene todas).** Ninguna decisión de César omitida.

**Guardarraíles éticos (G §4, 3 rechazados + corolarios)** → plan §6: los 3 rechazos (bot falso, burla
nominal, estrechar bucket) + corolarios (deuda HUD, CTA post-derrota, EV en arrepentimiento, liberar
slot Maña, Cheating_Success_Rate) ✅ todos presentes. Añade #9 (vetar variante que sube K si grafo se
silencia) y #10 (no asumir audio), ambos derivados fielmente de G#37/#42 y D#67. ✅

**Exclusions: 0.**

---

## E. SÍNTESIS DEL AUDITOR

- **Replacements:** 0 sobre ~17 números/umbrales/§ muestreados de los 7 clústeres. Cero alteración.
- **Reclassifications:** 0 fabricadas. Cada 🟢=3/3 real; ⚪ preservados; umbrales contestados marcados
  como experimento. 1 caso ⚠️ MENOR (P1-6 toma la cara 🟢 de un hueco de encabezado 🟡) pero DEFENDIBLE
  porque la sub-resolución de balance es 🟢 en la propia fuente y el aspecto contestado se conserva en
  P2-21/DC-4.
- **Minimizations:** 0. El plan hace lo opuesto: preserva activamente los caveats incómodos (E=6
  concesiones; D=mismo operador) y no sobre-afirma F (CONVERGING, no CONVERGED).
- **Exclusions:** 0. Las 30 Decisiones de César de las fuentes están todas presentes (32 entradas), y
  los 3 guardarraíles rechazados + corolarios también.

**Veredicto:** El plan v1.3 es notablemente fiel a las 7 fuentes. No se detectó fabricación grave ni
moderada. La única observación es un caso menor de selección-de-cara-de-confianza (P1-6) que es
defendible y no oculta el aspecto contestado. La regla de fidelidad declarada se cumple en la práctica.
Esto cae en **PASS** con una nota menor (no alcanza el umbral de CONCERNS, que requeriría fallas
moderadas — aquí solo hay 1 ⚠️ defendible y 0 en las otras 3 categorías).

SCORE-INPUT: exclusions=0 minimizations=0 replacements=0 reclassifications=1 verdict=PASS
