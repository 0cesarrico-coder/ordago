# ÓRDAGO — HANDOFF para el próximo ciclo (leer ESTE archivo primero tras compactar)

> Propósito: este documento es la **fuente de verdad para retomar** tras una compactación de contexto.
> Contiene (1) el estado actual, (2) el método de 2 etapas replicable con comandos/paths exactos,
> (3) los aprendizajes de infraestructura que costó descubrir, (4) las rutas de todos los artefactos,
> y (5) el foco propuesto del PRÓXIMO ciclo. Si retomas el trabajo, **lee esto antes de actuar.**
> Fecha: 2026-06-25.

---

## 0. Resumen del ciclo completo ya hecho (v1.1 → v1.2)

**Dos etapas:**
- **Etapa 1 — búsqueda con múltiples agentes:** workflow de 135 agentes, 4 rondas loop-until-dry → **93 huecos confirmados** (22 temas: 8 P1 · 9 P2 · 5 P3 + 11 contratos de proceso + 6 decisiones de César).
- **Etapa 2 — debate con la skill multi-IA:** Opus + Gemini 3.5 Flash (API) + Meta AI (MCP), 3 rondas + referee (convergió, score 83) + síntesis auditada hasta **PASS 100/100**.

Antes hubo un **ciclo previo** (v0.1 → v1.1): debate multi-IA de diseño/valor (3 rondas, CONVERGED) que produjo las 5 decisiones (sistema dual, Diablo Fantasma social, asistencia UI en 3 capas, etc.).

**Resultado:** el GDD pasó de v0.1 → v1.1 → **v1.2** (actual).

---

## 1. ESTADO ACTUAL

- **GDD vigente:** `/Users/macbookprocesar/Roguelike-Deckbuilder-Baraja/ORDAGO_Macro_GDD.md` = **v1.3**
  (2.º ciclo de diseño, 2026-06-25: workflow 147 agentes → 65 huecos en 7 clústeres A–G; **regla de
  cobertura aplicada** → 1 debate multi-IA por clúster hasta CONVERGED + meta-síntesis auditada **PASS 88**
  → 14 P1·31 P2·6 P3, 8 conflictos cruzados, 32 decisiones de César). Plan maestro:
  `docs/research/2026-06-25-ordago-debate-diseno-v2/META-SINTESIS-v1.3.md`.
- **Backups:** v0.1 → `docs/research/2026-06-24-ordago-debate-valor/ORDAGO_Macro_GDD_v0.1_backup.md`;
  v1.1 → `docs/research/2026-06-25-ordago-debate-mejoras/ORDAGO_Macro_GDD_v1.1_backup.md`;
  v1.2 → `docs/research/2026-06-25-ordago-debate-diseno-v2/ORDAGO_Macro_GDD_v1.2_backup.md`.
- **El 2.º ciclo VALIDÓ la infra del debate paralelo:** receta de scrape de Meta AI corregida (tomar el
  **último** `[class*="group/assistant-message"]` con texto >800, no el más largo — el más largo agarra R1 o
  el prompt); orphan-lock resuelto matando ~34 nodos playwright-mcp viejos. K=3 en batches funcionó.
- **Lo que v1.2 ya resolvió (3 palancas + craft):** artefacto-puente §8.3 · generador de bifurcación como
  invariante §7.3 + solver §14.0 + foso vivo §18 · unit-economics B2P 3 columnas §16.1 · C-1 = **HÍBRIDO**
  (Steam premium + demo web jugable) · legibilidad dual + barra de Sospecha §7.6 · color redundante + juice
  4 tiers §10 · firma sonora §10.1 · lazo D1/D7 §8.4 · A/B arte con glance gate §11 · Codex grid de huecos.
- **★ Punto ABIERTO a propósito (NO se cierra por debate):** la **banda exacta de spread de EV** del generador
  (§7.3) — Opus+Meta ≤15% dual vs Gemini 15-20%. Se zanja con el **SOLVER DE PAPEL** (§14.0), que es el
  **primer experimento recomendado**: 100 tableros sembrados, ¿hay ≥2 jugadas Pareto-no-dominadas con spread
  en banda? Valida o mata el foso por un fin de semana, ANTES de un píxel.
- **Decisiones de César aún abiertas (§19.3):** banda EV (→solver) · arte (→A/B feed) · título · cosmología
  de palos · multi-nodo cultural C-3 · recuperabilidad de Pactos · ¿AZOTH o ÓRDAGO primero?
- **Repo:** NO es git. Hacer backup por copia antes de sobrescribir el GDD.

---

## 2. EL MÉTODO DE 2 ETAPAS (replicable — comandos/paths EXACTOS)

### Etapa 1 — Workflow de caza de huecos (multi-agente, loop-until-dry)
- **Tool:** `Workflow` (requiere opt-in del usuario; ya lo dio para estos ciclos).
- **Script reutilizable ya existe:**
  `/Users/macbookprocesar/.claude/projects/-Users-macbookprocesar-Roguelike-Deckbuilder-Baraja/323a5c34-8668-4993-8774-087ebf409324/workflows/scripts/ordago-huecos-clasemundial-wf_fc3ac14e-f8a.js`
  (editar con Write/Edit y relanzar con `Workflow({scriptPath})`). Estructura: ~15 auditores por dimensión
  anclados a cartas de `~/.claude/game-design-brain/`, verificación adversarial por hueco (sev≥3),
  crítico de completitud entre rondas, loop hasta 2 rondas secas o MAX_ROUNDS=4, síntesis priorizada.
- **Para el próximo ciclo:** cambiar las DIMENSIONES por el nuevo eje (ver §5) y apuntar el GDD a v1.2.
- **Modelos:** finders/verifiers = opus (inherit); síntesis = opus high (Fable 5 no disponible aún).

### Etapa 2 — Debate con la skill multi-ai-research (Opus + Gemini API + Meta AI MCP)
La skill se INVOCA con `Skill("multi-ai-research")` (el usuario lo exige explícitamente: "se tiene que
invocar la skill multi ia para el debate"). Soy el orquestador y ejecuto las fases manualmente, adaptando
los prompts al debate de diseño (no es research de negocio). Pipeline: FRAME → R1 (a ciegas) → R2
(cross-review) → loop de convergencia con referee → posiciones finales → síntesis (Loop B: MAKER ≠ CHECKER,
score en código) → PACKAGE.

**Asientos (priors) que funcionaron:**
- **Opus** = Diseño/Sistemas + rigor de elegancia (lidera lo de craft/foso).
- **Gemini 3.5 Flash** = Estratega de Valor + señal de mercado (lidera economía/precio).
- **Meta AI** = Data L1 de plataforma + Red Team (lidera viralidad/distribución; su data decidió formato y precio).

**Comandos clave (verificados, copiar tal cual):**
```bash
# Gemini API (venv con google.genai + GEMINI_API_KEY ya en entorno):
PY=~/Pipeline-TraducirVSL/.venv/bin/python
PYTHONIOENCODING=utf-8 "$PY" "$OUT/_gemini_run.py" "$OUT/<ai>-rN-prompt.md" "$OUT/<ai>-rN.md"
# (_gemini_run.py: model="gemini-3.5-flash", thinking_level="high"; copiar de un dir previo)

# Meta AI — pool de slots (login persistente por slot; usar SIEMPRE mcp__meta-ai-{SLOT}__*):
python3 ~/.claude/skills/multi-ai-research/tools/slot_pool.py claim   --owner "$OUT"   # devuelve SLOT y MCP
python3 ~/.claude/skills/multi-ai-research/tools/slot_pool.py heartbeat --owner "$OUT"  # cada ronda
python3 ~/.claude/skills/multi-ai-research/tools/slot_pool.py release  --owner "$OUT"   # al terminar
python3 ~/.claude/skills/multi-ai-research/tools/slot_pool.py status

# Scoring/ledger del debate (referee) y de la síntesis (auditor):
python3 ~/.claude/skills/multi-ai-research/tools/loop/debate_score.py "$OUT/referee-rN.md"
python3 ~/.claude/skills/multi-ai-research/tools/loop/synth_score.py  "$OUT/bias-audit.iter-N.md"
python3 ~/.claude/skills/multi-ai-research/tools/loop/loop_ledger.py  append <ledger> --iteration ...
```
**Prompts del skill (plantillas):** `~/.claude/skills/multi-ai-research/prompts/` (referee.md, bias-auditor.md,
cross-review.md, etc.). Las contrato-lines son OBLIGATORIAS:
- referee: `SCORE-INPUT: contested=N flipped=M consensus=K total=T verdict=CONVERGED|CONVERGING|STUCK`
- auditor: `SCORE-INPUT: exclusions=N minimizations=M replacements=R reclassifications=C verdict=PASS|CONCERNS|FAIL`
Stops: debate target 80 (o veredicto CONVERGED); síntesis target 85, max-iters 3. CONVERGED/CONVERGING≥80 = parar.

---

## 3. APRENDIZAJES DE INFRAESTRUCTURA (esto costó descubrirlo — NO re-derivar)

### Meta AI vía navegador (lo más frágil)
- **Servidores dedicados `mcp__meta-ai-1/2/3__*`** (perfil persistente, login de por vida). NUNCA usar el
  `playwright` general para Meta AI. Usar el namespace del slot que devolvió `claim`.
- **Orphan-lock:** si `browser_navigate` da *"Browser is already in use for .../slot-N"*, hay un Chrome/servidor
  MCP **huérfano** de una sesión vieja reteniendo el perfil. Diagnóstico y fix que funcionó:
  ```bash
  ps -eo pid,lstart,command | grep playwright-mcp | grep -v grep   # ver cuál es viejo
  ps -o ppid= -p <chrome_pid>                                       # padre = nodo MCP huérfano
  kill -9 <nodo_mcp_huérfano_pid>                                   # se lleva su Chrome
  rm -f ~/.cache/meta-ai/slot-N/Singleton*                         # limpiar locks
  ```
  Tras eso, re-`navigate` lanza Chrome fresco con el login intacto (vive en disco).
- **Enviar prompt grande SIN inflar mi contexto:** `pbcopy < prompt.md`, luego en el navegador:
  click en `[contenteditable="true"]` → `browser_press_key("Meta+v")` → verificar `innerText.length` →
  `browser_press_key("Enter")`. (El paste por clipboard evita meter 40-85KB en mi contexto por ronda.)
- **Esperar el streaming:** `browser_wait_for(textGone:"Parar", time:240)` funciona en slot 1, pero en
  **slot 2 topa a 30s** (timeout interno del backend). Workaround robusto: **polling manual** con
  `sleep` en bash + `browser_evaluate` chequeando que no exista botón "Parar" y que haya "Copiar respuesta".
- **Scrape de SOLO la respuesta del asistente (no el prompt pegado):** desde el último botón
  `aria-label*="Copiar respuesta"`, subir por `parentElement` y tomar el ancestro de **mayor longitud < ~25-40K**
  (por encima de eso el nodo ya engloba prompt+respuesta). Guardar con el param `filename` del evaluate para
  no inflar contexto, luego limpiar: el archivo viene **JSON-encoded** y con prefijo de UI **"Mostrar razonamiento\n"**
  → decodificar con `json.loads` + `re.sub(r'^\s*Mostrar razonamiento\s*\n','')` (ver `_clean_meta.py`).
- **Race de timing:** a veces el scrape corre antes de que renderice "Copiar respuesta" → devuelve vacío;
  **re-scrapear** tras unos segundos.

### Subagentes (Agent tool)
- **Glitch ocasional:** un subagente vuelve en ~8-10s con **0 tool_uses** y un texto corrupto/inyectado
  (no leyó ni escribió el archivo). **Fix:** simplemente **re-dispatch** con instrucciones explícitas
  "usa Read y luego Write". Pasó 2-3 veces; el retry siempre funcionó.
- **Modelos por rol (regla global del usuario):** investigación/auditoría = Opus; síntesis/orquestación/
  juicio estratégico = Fable 5 si estuviera disponible (hoy NO → Opus a max effort).

### Gemini
- venv con `google.genai`: `~/Pipeline-TraducirVSL/.venv/bin/python` (también existe en
  `~/spine-animation-ai/.venv`). `GEMINI_API_KEY` ya está en el entorno. Modelo `gemini-3.5-flash`,
  `thinking_level="high"`.

---

## 4. RUTAS DE TODOS LOS ARTEFACTOS

- **GDD vigente:** `ORDAGO_Macro_GDD.md` (v1.2).
- **Ciclo v0.1→v1.1 (debate de valor):** `docs/research/2026-06-24-ordago-debate-valor/`
  (report.md = veredicto §7-bis; DECISIONES-FINALES.md = las 5 decisiones; rondas R1-R3 de cada IA).
- **Etapa 1 (caza de huecos):** `docs/research/2026-06-25-ordago-huecos-clasemundial/HUECOS-CLASEMUNDIAL.md`
  (93 huecos, 22 temas, tabla P1/P2/P3 + 6 decisiones de César + 11 contratos de proceso).
- **Etapa 2 (debate de mejoras):** `docs/research/2026-06-25-ordago-debate-mejoras/`
  (report.md = fixes ganadores PASS 100; consensus-matrix.md; rondas R1-R3; referee-r2/r3; ledgers;
  utilidades reusables: `_gemini_run.py`, `_clean_meta.py`, `_frameworks.md`).
- **`_frameworks.md`** (cartas A1-A5, lentes QF→Lazzaro→MDA, M1·LD7 con confianza) — reusar como ancla.
- **game-design-brain:** `~/.claude/game-design-brain/` (router INDEX.md; clase-mundial/A1-A5,B1-B5,C1-C3,D1-D3,M1;
  monetizacion/L1-L13,E1-E8; lentes-diseno/LD0-LD7; raíz 00-12; horror; humor).

---

## 5. EL PRÓXIMO CICLO — foco propuesto: ÉXITO COMERCIAL (clase mundial ya tuvo 2 pasadas)

El usuario quiere "asegurar la clase mundial **Y éxito comercial**". El diseño/valor ya recibió dos ciclos
duros. El mayor valor marginal ahora es un ciclo con **lente COMERCIAL / go-to-market**, anclado a la
sub-biblioteca `monetizacion/` + las cartas de distribución `clase-mundial/D*,C*,B*`. Propuesta:

**ETAPA 1 (workflow) — dimensiones nuevas (eje comercial):**
- Unit-economics reales y break-even (monetizacion L3 LTV/CAC, L6 ventana, L4 el-modelo-manda).
- Estrategia de wishlists/Steam (algoritmo de descubrimiento, capsule, Next Fest, reviews velocity).
- UA por segmento y creativo (C2 ignición/combustión, matriz USA/LATAM/hispanos-USA; eCPM/CPI reales).
- El artefacto-puente como motor de crecimiento medible (D1, K=i×c) — ¿el número cierra?
- Ventana competitiva / saturación post-Balatro (L6) y timing de lanzamiento.
- Pricing regional y elasticidad; refund; conversión demo→wishlist→venta.
- Retención que sostiene el LTV de un B2P (Reloj A/B, §4.1); riesgo de cola larga.
- Plataforma y dependencia (L7); web demo como canal; ports.
- Localización/cultura como ventaja de CAC (B3, identidad latina).
- Riesgo legal/rating por región; Profeco/PEGI.

**ETAPA 2 (skill multi-ai-research) — debatir las palancas comerciales** que el workflow confirme, con los
mismos 3 asientos pero énfasis comercial (Gemini lidera mercado/UA; Meta AI data L1 de Ads/plataforma;
Opus modela unit-economics y riesgo). Salida: plan go-to-market falsable → cambios al GDD (§16-18) o un
doc nuevo `ORDAGO_GTM.md`.

> **★ REGLA DE COBERTURA DEL DEBATE (corrección del usuario, 2026-06-25, INVIOLABLE):** el debate NO se
> limita a las 3 palancas top. **Escala al número de huecos:** se debaten TODOS los huecos P1 y los P2
> significativos hasta encontrar la clase mundial — vía **tantas RONDAS como hagan falta por debate Y
> tantos DEBATES como hagan falta**. Cómo operarlo:
> 1. **Agrupar** los huecos confirmados en CLÚSTERES temáticos (p.ej. 5-8 clústeres de 2-4 huecos afines).
> 2. **Un debate multi-IA por clúster.** El pool de slots soporta **K=3 debates EN PARALELO**
>    (`mcp__meta-ai-1/2/3`), cada uno con su `claim`/`heartbeat`/`release` y su `output-dir` propio; correr
>    los clústeres de 3 en 3.
> 3. **Cada debate corre hasta CONVERGER** (referee CONVERGED, o score≥80, o STUCK declarado) — no un número
>    fijo de rondas. Loop A (counter-response) + Loop B (síntesis auditada PASS) por debate.
> 4. **Meta-síntesis final** (Fable 5 si disponible, hoy Opus max): funde los veredictos de TODOS los
>    debates de clúster en UN plan priorizado, resolviendo conflictos cruzados entre clústeres.
> 5. Solo entonces se aplica a una v1.3. Lo que quede irreducible/numérico → "a falsar", no "cerrado".
> Esta regla aplica a CUALQUIER ciclo futuro (comercial o de diseño): la cobertura del debate se dimensiona
> a los huecos encontrados, no al revés.

> Alternativa si el usuario prefiere: otro ciclo de DISEÑO sobre la v1.2 (puede haber huecos nuevos
> introducidos por los fixes). Pero el ROI mayor está en el eje comercial. CONFIRMAR con el usuario el
> eje del próximo ciclo antes de lanzar el workflow.

---

## 6. CHECKLIST DE ARRANQUE POST-COMPACTACIÓN

1. Leer este archivo + `ORDAGO_Macro_GDD.md` (v1.2) + `HUECOS-CLASEMUNDIAL.md` + el `report.md` de mejoras.
2. Confirmar con el usuario el **eje del próximo ciclo** (comercial vs diseño) — ver §5.
3. **Etapa 1:** editar el script de workflow (§2) con las nuevas dimensiones + GDD v1.2; lanzar `Workflow`.
4. **Etapa 2 (REGLA DE COBERTURA, §5):** agrupar los huecos en clústeres; **un debate multi-IA por clúster**,
   corriendo **K=3 en paralelo** (slots meta-ai-1/2/3, cada uno su `output-dir`); cada debate **hasta converger**;
   luego **meta-síntesis** que funde todos los veredictos. NO limitarse a los 3 huecos top.
   - `Skill("multi-ai-research")`; por clúster crear `docs/research/<fecha>-<slug-clúster>/`; copiar `_gemini_run.py`,
     `_clean_meta.py`, `_frameworks.md` de un dir previo; `claim` slot; verificar login; correr R1→...→síntesis.
   - Si el navegador Meta da orphan-lock → §3 (matar nodo huérfano + limpiar locks).
   - Usar clipboard para pegar prompts grandes; polling manual si `wait_for` topa a 30s; scrape con la receta de §3.
   - Si un subagente vuelve con 0 tool_uses → re-dispatch.
5. Aplicar los fixes consensuados a un GDD **v1.3** (backup primero; repo no es git). Marcar lo contestado
   como "a falsar", no como cerrado.
6. Mantener TodoWrite con el plan; liberar el slot Meta al terminar.

---

*Fin del handoff. Tras compactar: leer esto, confirmar eje del ciclo, y ejecutar las 2 etapas.*
