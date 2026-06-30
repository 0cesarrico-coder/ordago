# Opus — Ronda 2 · Cross-review · Clúster E (coherencia / carga cognitiva)

**Asiento:** Diseñador de Sistemas + sustracción/elegancia. Mantengo: el riesgo no es nº de sistemas, es **reglas verbalizadas antes del 1er win** × **canales que compiten en el frame**.

---

## 1. STEELMAN de quien difiere

**Meta AI (la divergencia dura).** Su tesis no es "menos es mejor" abstracto: es que mi techo `≤7±2 reglas-core` y mi KPI `time_to_first_fullería ≤120s` están **medio loop de retención por encima** de lo que el móvil hispano gama-media tolera. Su cadena causal es concreta y caería en datos: 46% bounce antes del min5 → el onboarding útil cabe en 3-5 min → cada regla extra cuesta ~+45s a time-to-win y ~−6pp D1 → el estándar que *escala* (Mob Control 36.1% D1, Free Fire/Candy) enseña **3 acciones core <180s**. Si eso es cierto, mis 7 reglas no son "borde", son **2× el estándar que convierte**, y la elegancia que defiendo se paga en instalaciones perdidas que nunca ven la elegancia. Steelman fuerte: **legibilidad@100px y conteo-de-reglas son la MISMA restricción** vista en espacio y en tiempo; Meta la mide en la única plataforma donde corre el ad.

**Gemini.** Su aporte real no es contenido sino **compresión cognitiva por arquetipo**: "el tahúr que engaña al Diablo" hace que "hacer trampas sube la Sospecha" se entienda **sin tutorial**. Eso ataca mi denominador por el lado correcto — no podando reglas, sino **bajando el costo de verbalizar cada una a ~0**. Es la única vía que reconcilia "7 reglas-core" con "4-5 verbalizables" de Meta.

---

## 2. ATAQUE (con cita)

- **A Meta AI — confunde "reglas verbalizadas" con "reglas-core".** Mi denominador (R1, líneas 30-39) es explícito: meta/delivery gateado **no cuenta**, y el conteo es **por verbalización del tester**, no por nº de sistemas en el GDD. Meta dice "7 reglas antes de win es 2×" (L196) pero mis reglas 5-7 (romper sube Sospecha / ~3 ranuras / trade-off) **no se verbalizan, se descubren al jugar la 1ª Fullería**. Con la compresión-arquetipo de Gemini, el tester verbaliza ~3-4 ("sumo 15", "hay una trampa", "la rompo", "engañar tiene precio") y *siente* las otras 3. Así que su `≤4-5 verbalizadas` y mi `≤7 core` **no se contradicen**: miden cosas distintas. CONTESTADO solo si la verbalización empírica >5.
- **A Meta AI — su `máx 3 elementos animados` (L190) choca con MI propia regla de scheduler y la refuerza, pero su nº es arbitrario.** Mi serialización Z3 (R1 L26) ya garantiza que pillado-Sospecha y cascada-T3 **nunca comparten frame**. El límite no debe ser "3 objetos" (cuenta de render que un combo emergente romperá), sino "≤1 evento Z3+ por frame" (regla de scheduler). Atado a fps medido, no a inventario.
- **A Gemini — `N=16 Diablos, M=24` (L100) está decretado, no derivado.** El número sale de la nada narrativa; no hay función que lo ate al presupuesto de los 12 dientes ni al ritmo de revelación. Es número-a-falsar, no invariante. Y su "máx 3 siluetas activas" (L98) es **buena sustracción** — limita huecos abiertos — pero la mete en el Codex (meta) cuando el mismo principio debería gobernar el frame de juego.
- **A Gemini — su Lore-UGC ≥2% (L111) y mi linkeo Diablo→Biblia colisionan con Meta** (L217: "lore no mueve installs ni D7"). No defiendo el lore como retención; defiendo el linkeo como **coherencia falsable barata** (cada Diablo cita 1 hecho/ambigüedad). Si Meta gana, el lore se mantiene pero **no se le pide D7**, solo no-contradicción.

---

## 3. CONVERGENCIA

**CONVERGE (3 IAs):**
- El cuello no es nº de sistemas sino **carga al 1er win + focos simultáneos en el frame**. Mi serialización Z3 ≡ "máx animaciones" de Meta ≡ "saliencia legible" de Gemini: **una sola restricción**.
- **first meaningful choice / first-Fullería temprano** es el hook que decide D1. Las tres lo ponen como gate duro.
- **Anti-FOMO por colección terminable + brag**, sin timer (premium B2P). Meta cuantifica el costo: ~2-4pp D30 vs FOMO, aceptable por coherencia.
- Stickers se comparten por **identidad, no por build-data** (mi separación identidad-de-build vs solución-de-seed = "silueta limpia" de Meta).

**CONTESTADO:**
- **CONTESTADO: el número del hook (90s vs 120s).** Meta: `≤90s` (L197/203, atado a 46% bounce min5); yo: `≤120s`. Concedo parcialmente — bajo mi objetivo a **p50 ≤90s** porque su cadena causal es L1-móvil y mi 120s era teórico. Banda de muerte si p50 >120s.
- **CONTESTADO: techo de reglas (verbalizadas ≤4-5 Meta vs core ≤7 mío).** No es contradicción real (denominadores distintos) PERO el *kill* empírico es el de Meta: lo que se mide en el tester es verbalización, y ahí mando ≤5.
- **CONTESTADO: cardinalidad N del Codex.** Gemini=16 decretado; yo y Meta lo dejamos ⚪. Decisión de César.

---

## 4. REFINA — resolución de clase mundial (falsable)

- **Gate Z (scheduler, no render) — extiende §11/§14.** Peor caso combinado (Trampa activa + Sospecha subiendo + cascada T3) a **100×100px, grises, deuteranopia**: silueta+valor identificables por **≥9/10 testers**, y **≤1 evento Z3+ por frame** verificable por log (`Δt(Z3_a,Z3_b)>0`). Además, métrica de Meta como segundo filtro: **demo web móvil gama-media ≥55fps y bounce <35% @60s**. MUERE si <9/10, si el log muestra solape, o si fps<55 / bounce≥35%.
- **Gate de complejidad — DOS denominadores, no uno.** (i) `reglas_core ≤9` (techo duro de scope). (ii) `reglas_verbalizadas_por_tester ≤5` (techo duro de onboarding, gana este en conflicto). Regla de conservación: +1 delivery ⇒ −1 carga core percibida. MUERE si verbalizadas >5 **o** si el tester nombra un sistema meta antes de la Manga 1 (bug de onboarding).
- **Gate de hook.** `time_to_first_fullería_jugada` **p50 ≤90s** (bajado desde 120s por L1 de Meta); `first_meaningful_choice <90s`. MUERE si p50 >120s.
- **Gate de presupuesto temporal.** Σ(12 dientes) ∈ [25,35] p50; **p90 ≤40 min**; mangas **guardables cada 6-8 min** (concesión a sesión fragmentada de Meta — el run continuo muere en el bus). Duración derivada de Maña, no variable libre. MUERE si p90>40 o si no hay punto de guardado ≤8 min.
- **Gate de complementariedad (Pacto↔Fullería).** Existe ≥1 estado de Mesa donde EV(Pacto)>EV(Fullería) y "Fullería siempre óptima" ≤85% sobre 1000 seeds. MUERE si Fullería domina >85%.
- **Compresión-arquetipo (de Gemini) como requisito, no adorno.** Cada regla-core debe tener un **gancho cultural de 1 frase** que la haga *sentir* sin tutorial; si una regla no comprime a arquetipo, cuenta doble en el techo de verbalizadas.

**Decisión de César:** (1) ¿`≤90s` para el 1er Fullería (Meta, +D1) **o** `≤120s` (margen de feel/setup de la Mesa viva)? Cada 30s ≈ trade-off D1 vs profundidad. (2) ¿Run **continuo premium** o **mangas guardables cada 6-8 min** para sesión móvil fragmentada? (3) Cardinalidad **N del Codex** (16 de Gemini vs abierto). (4) ¿Acepta podar **Diablo Fantasma + artefacto-puente** del onboarding (Meta: "capa sin lift D1 medible") manteniéndolos como meta gateado?

---

**Lo que solo yo sostengo tras R2:** la falsa contradicción ≤7-core vs ≤4-5-verbalizadas se disuelve con **dos denominadores explícitos**; el límite de papilla es **regla de scheduler (≤1 Z3+/frame)**, no inventario de objetos; y la compresión-arquetipo de Gemini es el **mecanismo** que reconcilia profundidad de sistemas con carga de onboarding móvil de Meta.

*Confianza: serialización Z3 y dos-denominadores 🟢 (deriva de §11/§14 + CLT); p50≤90s 🟡 (concesión a L1 de Meta, falta validar en ÓRDAGO); N=16 ⚪ (decretado). Números = objetivos-a-falsar.*
