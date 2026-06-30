# Bias Audit — iter-0 (Independent Checker)

> **Verdict**: **CONCERNS** — el reporte representa con justicia las 3 IAs y conserva todas las cifras L1 de Meta/Gemini y la banda de EV correctamente CONTESTADA; las únicas observaciones son 2 minimizaciones menores (un argumento de plataforma de Meta omitido y una cifra de Gemini comprimida), sin replacement, sin exclusión de hallazgo de consenso/mayoría, sin reclasificación.

---

## Metodología

Listé todos los hallazgos finales de `gemini-final.md` y `meta-ai-final-response.md`, y verifiqué uno por uno su presencia, profundidad y números en `report.iter-0.md`. Comparé el trato de los hallazgos de Opus contra los de Gemini/Meta al mismo nivel de consenso. Vigilé específicamente el riesgo pro-Opus (sintetizador Opus + debatiente Opus). La banda de EV se evaluó esperando que quede CONTESTADA (correcto por contrato, NO reclassification).

---

## Hallazgos (por instancia de sesgo)

### Instancia 1 — MINIMIZATION

- **Type**: Minimization
- **Finding affected**: Argumento "el peso no es excusa" de Meta AI (Crux 1, formato del objeto-puente).
- **Evidence**:
  - `meta-ai-final-response.md` (línea 12): *"Peso no es excusa: Profeco mide 1 MB por mensaje de texto y 1 MB por imagen en WhatsApp, así que la imagen no añade fricción."* — es un dato de plataforma (Profeco) que Meta usa para neutralizar la principal objeción de ingeniería contra la imagen (peso/fricción).
  - `report.iter-0.md` (§1): conserva el porqué-imagen (56%/52%, 12.4%, etnografía) pero NO incluye la equivalencia de peso Profeco 1MB texto = 1MB imagen que cierra el argumento. El reporte sí preserva la idea de fricción-cero por otra vía ("PNG <80KB renderizado en cliente"), por lo que la conclusión sobrevive, pero el dato L1 específico de Meta que la respalda quedó fuera.
- **Specific correction**: Debe quedar presente que el peso de la imagen NO añade fricción en WhatsApp respaldado por el dato de plataforma de Meta (Profeco: ~1 MB texto ≈ 1 MB imagen), atribuido a Meta AI como L1.

### Instancia 2 — MINIMIZATION

- **Type**: Minimization
- **Finding affected**: Cifra específica de Gemini para el asset móvil del clip (Crux 2): WebP animado **<300 KB**.
- **Evidence**:
  - `gemini-final.md` (líneas 13, 17) y corroborado por `meta-ai-final-response.md` (línea 15): Gemini fija el asset móvil en **WebP animado <300 KB** ("Genera un WebP animado en bucle (<300 KB)"); Meta también cita "<300KB".
  - `report.iter-0.md` (§1, línea 51): comprime ambos a *"un asset pre-renderizado ligero (MP4/WebP <500 KB)"*, usando el techo de Opus (<500KB del MP4) y absorbiendo el <300KB de Gemini/Meta dentro de él. La cifra propia de Gemini/Meta para el asset móvil pierde su valor concreto. NO hay contradicción ni negación (500 contiene a 300), por lo que es minimización, no replacement.
- **Specific correction**: Debe quedar visible la cifra de Gemini/Meta para el asset móvil pre-renderizado (WebP animado <300 KB), distinta del clip MP4 <500 KB de PC, atribuida a su fuente.

---

## No-instancias (verificadas y descartadas)

- **Banda de EV (Gemini banda única [15-20%] vs Opus/Meta banda dual)**: el reporte la presenta como el ÚNICO contestado vivo (§0, §2, §6) y expone AMBOS lados con la posición de Gemini (piso 15%, rango cerrado, "ajedrez seco") con espacio comparable al de Opus/Meta. Esto es CORRECTO por contrato — NO es reclassification.
- **Replacement (cifras)**: verificado número por número. WhatsApp 12.4% (>FB 11%, YT 10.7%), stickers 56%/52% vs 12%, Reels 2-12x, vida media 2-3 sem, 87% smartphone (Meta); entropía 2.0-2.2 bits y caída >15%, precio LATAM $7.49/149 MXN, LTV/CAC ~4-5, +15% scope, -25% conversión, penetración PC <28% LATAM vs 76% USA, test de humo $100 / CTR 2.5% / CPL (Gemini) — TODAS aparecen con su valor y su fuente. Las cifras especulativas de LTV/CAC de Gemini (2.84/4.87/10.80) y conversión de Meta (18/15/12%) se marcan explícitamente como NO-consenso e ilustrativas (§3) — exclusión JUSTIFICADA, no replacement. Cero replacements.
- **Exclusion de consenso/mayoría**: los 8 puntos de consenso 3/3, los re-siembra >20% (Meta)/>25% (Opus), backend propio de leaderboards, separación de loops, gate LTV/CAC≥3, precio LATAM, C-1 híbrido — todos presentes. Ningún hallazgo de consenso o mayoría de Gemini/Meta fue omitido.
- **Reclassification**: los umbrales de re-siembra de Meta (>20%) y la entropía de Meta (>15%) y de Gemini (2.2 bits) están atribuidos correctamente; el consenso de método para zanjar el EV se marca como consenso 3/3. Ningún acuerdo genuino fue diluido a "Contestado".

---

## Strengths (fairness)

- Atribución nominal rigurosa por cifra con nivel de evidencia (L1>L2>L3>L4) y confianza 🟢/🟡/⚪; la regla "no se asciende 🟡→🟢" protege a la data L1 de Meta de ser sobre-vendida o sustituida.
- La data L1 de plataforma de Meta (WhatsApp 12.4%, stickers 56%/52%, Reels 2-12x, vida media 2-3 sem, 87% smartphone) está íntegra y atribuida — sin minimización frente a Opus.
- El flip concedido por Opus (imagen primaria sobre su grid-de-texto de R1) se documenta honestamente como derrota de Opus ante data de Meta, lo opuesto al sesgo pro-Opus temido.
- La banda de EV mantiene la posición minoritaria de Gemini (1/3) con espacio y argumento equivalentes; no se aplastó la voz minoritaria.
- Las cifras especulativas se rebajan explícitamente para TODAS las IAs por igual (incluida Gemini y Meta), no solo para neutralizar a no-Opus.

---

SCORE-INPUT: exclusions=0 minimizations=2 replacements=0 reclassifications=0 verdict=CONCERNS
