# Bias Audit — Iteración 1 (CHECKER independiente)

> **Verdict**: **PASS** — La banda de EV queda correctamente CONTESTADA con ambos lados desarrollados; cada hallazgo y cada cifra de Gemini y Meta AI aparece en el reporte con atribución y profundidad equivalente a los de Opus. No detecto exclusión, minimización, reemplazo ni reclasificación.

---

## Método

Inventarié todos los hallazgos y cifras de `gemini-final.md` y `meta-ai-final-response.md`, y verifiqué uno por uno su presencia, atribución y trato en `report.iter-1.md`, comparándolos con el trato dado a los hallazgos de `opus-final.md` de importancia comparable. Riesgo vigilado: sintetizador Claude + debatiente Opus → sesgo pro-Opus.

---

## 1. EXCLUSION — búsqueda

Recorrí cada posición final de Gemini y Meta AI:

| Hallazgo (Gemini / Meta AI) | ¿En el reporte? | Dónde |
|---|---|---|
| Stickers NO admiten hipervínculos → imagen + caption (Gemini, L1) | Sí | §1 deep-link, líneas 49 (texto casi literal) + §5 |
| WhatsApp 12.4% info MX > FB 11% > YT 10.7% (Meta) | Sí | §1 línea 41 + tabla cifras línea 67 |
| Stickers 56% / animados 52% vs 12% predeterminados (Meta) | Sí | §1 línea 41 + tabla línea 68 |
| Profeco ~1MB texto ≈ ~1MB imagen (Meta) | Sí | §1 línea 42 (bloque dedicado) + tabla línea 69 + §5 |
| Reels 2-12× alcance; carruseles +25.71% (Meta) | Sí | §1 línea 46 + tabla línea 70 |
| FFmpeg.wasm "choke main thread…" móvil gama baja (Gemini/Meta, L1) | Sí | §1 línea 54 (cita literal) |
| 87% gamers LATAM smartphone (Meta) | Sí | §1 línea 54 |
| WebP animado <300KB asset móvil (Gemini/Meta) | Sí | §1 línea 56 (bloque dedicado) + tabla línea 71 + §5 |
| Banda ÚNICA [15%,20%], piso 15% (Gemini) | Sí | §2 tabla líneas 103-104 + argumento línea 106 |
| Truco/Escoba "tensión de la codicia" (Gemini) | Sí | §2 línea 106 |
| Entropía Shannon <2.0-2.2 bits umbral (Gemini) | Sí | §2 línea 112 (atribuido a Gemini) |
| Precio LATAM $7.49 / 149 MXN; Balatro $7.50, Inscryption $9 (Gemini) | Sí | §0 línea 26, §3 tabla línea 139, §4 |
| Penetración PC <28% LATAM vs 76% USA; conv <1.5-2% (Gemini) | Sí | §6 punto 5 línea 208 |
| +15% costo / -25% conversión LATAM móvil + mitigación pre-registro (Gemini) | Sí | §4 línea 170-173 |
| Embudo WhatsApp→demo→email→wishlist (Gemini) | Sí | §3 línea 129 |
| Backend propio leaderboards (Meta + Opus) | Sí | §3 línea 149 |
| Gate LTV/CAC ≥3 por columna (Meta/Opus) | Sí | §0, §3, §5 |
| Vida media sticker 2-3 sem (Meta) | Sí | §1 línea 62 + tabla línea 74 |
| C-1 HÍBRIDO (3/3) | Sí | §4 (unánime) |

**Exclusiones encontradas: 0.** Toda posición final de Gemini y Meta AI está presente. Donde una cifra concreta de tabla NO se eleva a consenso (LTV/CAC 2.84/4.87/10.80 de Gemini; 18/15/12% conversión de Meta), el reporte lo justifica EXPLÍCITAMENTE (§3 nota línea 146: "NO son consenso y NO se elevan a hecho… ilustraciones de industria"). Eso es justificación legítima, no exclusión silenciosa — y aplica el mismo trato a las cifras de Opus.

## 2. MINIMIZATION — búsqueda

Comparé profundidad por nivel de consenso:

- **Datos L1 de Meta AI** (Profeco, stickers 56%, WhatsApp 12.4%, Reels 2-12×, 87% smartphone): reciben bloques propios extensos en §1, no menciones de paso. El dato Profeco —que la iteración anterior marcó como minimizado— ahora tiene un párrafo dedicado completo (línea 42) con el mismo desarrollo que los hallazgos de sistemas de Opus. Corrección verificada.
- **Asset móvil WebP <300KB** (cifra propia Gemini/Meta): bloque dedicado (línea 56) que explica por qué <300KB es DISTINTO y más exigente que el <500KB de PC, evitando que el techo de PC "absorba" el presupuesto móvil. Desarrollo equivalente al de los hallazgos de Opus.
- **Banda ÚNICA de Gemini [15-20%]**: en §2 recibe su propia fila en la tabla comparativa (igual peso visual que la banda dual Opus/Meta) y un párrafo argumental completo (línea 106) tan largo como el de Opus/Meta (línea 105). Trato simétrico.
- **C-1 trade-offs de Gemini** (+15%/-25%): expuestos íntegros en §4 con su mitigación.

No detecto ningún hallazgo de Gemini/Meta con menos espacio/análisis que un hallazgo de Opus de importancia comparable. **Minimizaciones encontradas: 0.**

## 3. REPLACEMENT — búsqueda

Verifiqué que los números específicos de Gemini/Meta aparezcan SIN sustituir por estimaciones de Opus:

- Profeco ~1MB ≈ ~1MB → idéntico en reporte.
- Stickers 56%/52% vs 12% → idéntico.
- WhatsApp 12.4% / FB 11% / YT 10.7% → idéntico.
- Reels 2-12× → idéntico.
- WebP <300KB → idéntico (no fue colapsado al <500KB de Opus; el reporte explícitamente los mantiene separados).
- Precio LATAM $7.49 / 149 MXN, Balatro $7.50, Inscryption $9 → idénticos a Gemini.
- 87% smartphone → idéntico.
- Banda Gemini [15-20%], piso 15% → preservada literal; el techo 25% de Opus NO sustituye el techo 20% de Gemini, se presentan ambos.
- Entropía Shannon: el reporte conserva AMBOS umbrales (>15% caída de Meta; <2.0-2.2 bits de Gemini, línea 112) en vez de quedarse solo con uno.

Ninguna cifra de plataforma fue reemplazada por estimación de Opus. **Reemplazos encontrados: 0.**

## 4. RECLASSIFICATION — búsqueda

Busqué hallazgos donde 2+ IAs coinciden pero el reporte los degrada a "Contestado":

- **Banda de EV correctamente CONTESTADA (esperado):** Opus+Meta = banda dual (2/3); Gemini = banda única (1/3). Hay desacuerdo genuino de ESTRUCTURA (dual vs única) y de techo (25% vs 20%). El reporte lo marca como el ÚNICO contestado vivo (`contested=1`), lo cual es correcto: no es agreement diluido, es desacuerdo real. NO es reclasificación.
- En sentido inverso, verifiqué que el reporte no INFLE consenso: los 8 hallazgos marcados consenso 3/3 (artefacto-puente dual, deep-link jugable, generador invariante, separar loops, gate ≥3, precio $7.49, C-1 híbrido) sí tienen acuerdo de los tres en sus finales. Correcto.
- Nota de matiz (no es bias): en Crux 2 Gemini y Meta usan "exclusivo PC" mientras Opus aporta el framing "render server-side / separar generar de codificar"; el reporte lo marca consenso porque las tres convergen en "móvil NO codifica, PC/servidor genera". La sustancia coincide en las tres posiciones finales, así que la clasificación de consenso es honesta, no un secuestro de la posición de Gemini/Meta.

**Reclasificaciones encontradas: 0.**

---

## Strengths (fairness)

1. **Atribución cifra-por-cifra con fuente y nivel de evidencia** (tabla §1, §3): cada número lleva "Meta AI / Gemini / Opus" y L1/L4 — trazabilidad que hace difícil esconder sesgo.
2. **Las dos minimizaciones de la iteración previa están corregidas** (Profeco y WebP <300KB ahora con bloque propio), exactamente el alcance que el bias-audit anterior pidió, sin tocar nada más.
3. **El único desacuerdo se presenta con AMBOS lados desarrollados simétricamente** (tabla de dos filas + dos párrafos argumentales de longitud pareja), incluso registrando dónde Opus CONCEDIÓ a Gemini (piso ~8%) y a Meta (formato imagen, deep-link aterriza en jugable).
4. **Las cifras de Opus reciben el MISMO escepticismo** que las de los demás (⚪/🟡, "validar en cohorte propia"); no hay trato preferente al razonamiento Opus sobre la data L1 de Meta — al contrario, el reporte declara explícitamente "data L1 > razonamiento" y registra los flips de Opus.
5. **No se inventa consenso en cifras**: la nota §3 (línea 146) descarta por igual las cifras no-consensuadas de Gemini y de Meta.

---

SCORE-INPUT: exclusions=0 minimizations=0 replacements=0 reclassifications=0 verdict=PASS
