# Bias Audit — ÓRDAGO Multi-Debate · iter-0

> **Verdict**: **FAIL** — el reporte descarta dos cifras de plataforma/mercado aportadas por Meta AI/Gemini (Escoba "4M descargas / 1M+ instalaciones" y "Action-Social 41% LATAM/MX"), y encima las "justifica" con una nota falsa ("no se citan números que ninguna IA aportó") cuando sí los aportaron — replacement + exclusion de datos no-Opus.

Auditoría independiente. No conozco el proceso de producción. Riesgo vigilado: sintetizador Claude (Opus) + un debatiente Opus → sesgo PRO-Opus que minimice las cifras de plataforma de Meta AI y Gemini. Confirmado en parte: las dos cifras concretas eliminadas provienen de los asientos NO-Opus, mientras que la lista de referentes estéticos de Opus (Darkest Dungeon / Cult of the Lamb / Inscryption) se conserva literal.

---

## Findings

### Instancia 1 — REPLACEMENT (cifra de mercado de Meta AI sustituida por una negación falsa)

- **Type**: Replacement
- **Finding affected**: CRUX 1 — evidencia de mercado que sostiene "la mesa compartida genera decisión / poblador activo".
- **Evidence**:
  - meta-ai-final-response.md L8: *"Dato de mercado: La Escoba en español supera **4 millones de descargas y 1M+ instalaciones** precisamente porque la mesa compartida genera decisión."*
  - report.iter-0.md NO contiene la cifra (grep de "millon/descarga/instalac/4m/1m" → 0 hits sobre datos). Peor: la nota de cierre (L90) afirma *"No se citan números de mercado que ninguna IA aportó; toda señal empírica queda 'validar en cohorte propia'."* — Meta AI **sí** aportó esa cifra de plataforma. El reporte la sustituye por una negación que la borra y la deslegitima.
- **Specific correction**: La cifra de Meta AI (Escoba ES ~4M descargas / 1M+ instalaciones) debe aparecer en el cuerpo (CRUX 1 / §3 Mesa, o §0) atribuida a Meta AI como dato de plataforma que respalda el poblador activo. Y la nota de cierre debe dejar de afirmar que "ninguna IA aportó números" (es falso): si se quiere matizar la confianza en la cifra, hágase explícitamente, no negando su existencia.

### Instancia 2 — EXCLUSION (cifra Quantic Foundry citada por 2 IAs, ausente sin justificación)

- **Type**: Exclusion
- **Finding affected**: Diablo Fantasma — magnitud del motor social-competitivo LATAM que justifica priorizarlo (§2 jerarquía, §3, §4 §8).
- **Evidence**:
  - gemini-final.md L27: *"…sirve al potente motor social-competitivo de LATAM (**Quantic Foundry: Action-Social 41% MX**)."*
  - meta-ai-final-response.md L20: *"**Action-Social es 41% del engagement LATAM**, pero LD6 exige gap cerrable."*
  - report.iter-0.md: ausente (grep "41/quantic/action-social/foundry" → 0 hits). El reporte habla del Diablo Fantasma pero elimina el dato cuantitativo que **dos** IAs (Gemini + Meta AI) usaron para dimensionar su importancia. No hay justificación de la omisión.
- **Specific correction**: Incluir el dato "Action-Social ~41% del engagement LATAM (Quantic Foundry)" donde se prioriza el Diablo Fantasma, atribuido a Gemini + Meta AI. Por ser acuerdo de 2 asientos no-Opus, su exclusión silenciosa es exactamente el sesgo a vigilar.

### Instancia 3 — MINIMIZATION (dirección de arte concreta de Meta AI colapsada a una etiqueta)

- **Type**: Minimization
- **Finding affected**: §11 — lado maximalista del crux estético / intervención de iconografía.
- **Evidence**:
  - meta-ai-final-response.md L52: *"§11, forzar **iconografía maximalista (oro no como lujo, como moneda sucia; cempasúchil, papel picado)** para evitar lectura boutique."* (Gemini converge en maximalismo identitario, L42.)
  - report.iter-0.md L47/L62-63: el maximalismo se reduce a la etiqueta *"maximalista-color"* / *"Maximalismo popular colorido"*, sin la prescripción concreta de Meta AI (moneda sucia, cempasúchil, papel picado). En contraste, el lado Opus/Gemini conserva su referencia concreta literal (*Darkest Dungeon / Cult of the Lamb / Inscryption*, L53). Trato desigual: la concreción del lado Opus se preserva; la del lado Meta AI se diluye a un adjetivo.
- **Specific correction**: Restaurar la prescripción concreta de Meta AI para el lado maximalista (oro = moneda sucia, cempasúchil, papel picado) con la misma especificidad con que se conservan los referentes de claroscuro del lado Opus.

---

## Nota sobre CRUX 4 (verificación de NO-reclassification)

La estética Posada/Día-de-Muertos aparece como **Contestada/Irreducible** en el reporte (§0 "1 contestado", §4 §11, §5 tabla de cruxes). Las tres posiciones finales la declaran irreducible (opus-final L89, gemini-final L13, meta-ai L17). La clasificación del reporte coincide con el acuerdo real → **NO es reclassification**, es correcta. Sin reclasificaciones detectadas.

## Strengths

- **Estética bien clasificada**: el único crux contestado se marca como tal, con AMBOS lados presentes y la data L1 de Meta AI ("blanqueamiento" 2024-25, "hotel boutique en Tulum", maximalismo) citada con detalle y atribuida (L53). Aquí el reporte trató a Meta AI con justicia.
- **Cierres de Gemini representados con honestidad**: la auto-refutación de Gemini (retiró la UI auto-resaltadora) se acredita explícitamente ("Su propio autor Gemini la retiró", L26) en vez de presentarse como hallazgo de Opus.
- **Convergencias correctamente niveladas**: los consensos 3/3 (Mesa hueca, fantasía-trampa hueca, Pactos sin costo, Diablo sin bucketing) se etiquetan como consenso, sin inflar la postura de Opus por encima del panel.
- **Criterio de kill <60% recall y bucketing ~5%**: provenientes de Meta AI/Gemini, se conservan en el cuerpo (§4, §6).

---

SCORE-INPUT: exclusions=1 minimizations=1 replacements=1 reclassifications=0 verdict=FAIL
