# Referee — Ronda 3 (Cierre · 3 cruxes + resto)

> **Verdict**: **CONVERGING** — Dos de los tres cruxes vivos colapsaron a consenso esta ronda (formato del objeto-puente y soporte del clip, ambos con flips concedidos por Opus), y todo el resto (3 palancas + C-1) está estable en consenso fuerte. Solo queda 1 desacuerdo genuino y vivo: la banda de EV, donde Opus/Meta convergieron en banda DUAL (≤15% calidad) pero Gemini se mantiene en banda ÚNICA [15-20%] con piso de 15% que contradice el techo de calidad de los otros dos. No está endurecido (hubo flips productivos hacia la estructura dual), por lo que otra ronda corta sobre ese único número aún puede mover a Gemini.

## Tabla de convergencia

| Finding | Estado esta ronda | ¿Cambió desde R2? | Quién concuerda / quién discrepa |
|---|---|---|---|
| **Crux 1 — Formato objeto-puente: imagen-sticker (<80KB) PRIMARIA + texto/caption fallback + deep-link embebido** | Consensus | Sí — FLIP de Opus (R2 defendía emoji-grid de texto como primario; R3 concede "imagen primaria, perdí el formato no el principio") | Opus + Gemini + Meta concuerdan. Nadie discrepa |
| **Crux 2 — Clip NO codificado en cliente móvil; render server-side/PC, distribuido a móvil como asset pre-renderizado ligero (<500KB)** | Consensus | Sí — FLIP de Opus (R2 = "diferir clip a vertical slice"; R3 = "construir ya, separar generar de codificar, render server-side") | Opus (server-side render) + Gemini (PC genera, móvil sirve WebP) + Meta (PC genera, móvil pre-render) concuerdan en la misma máquina |
| **Crux 3 — Banda de spread de EV** | **Contested** | Sí — FLIP de Opus y Meta hacia banda DUAL; Gemini se mantiene en banda única | Opus + Meta = banda dual (re-siembra >25%/>20%, calidad/foso solo ≤15%). Gemini = banda única [15%-20%], piso 15% (contradice el techo de calidad ≤15% de los otros dos) |
| Palanca 1 — Sistema dual desde un único `RunDigest` (sticker-imagen + clip), generador procedural de variantes anti-fatiga | Consensus | No (estable; ya convergía en R2) | Opus + Gemini + Meta |
| Palanca 2 — Generador como INVARIANTE verificado por solver ANTES de un píxel; instrumentación entropía de Shannon de builds ganadores + test del experto/Diablo Fantasma | Consensus | No (estable) | Opus + Gemini + Meta (solo el número exacto de la banda sigue en Crux 3) |
| Palanca 3 — Separar loop ADQUISICIÓN (CAC>0) de loop SOCIAL (CAC~0); modelo B2P 3 columnas con gate LTV/CAC≥3 por segmento; backend propio leaderboards | Consensus | No (estable) | Opus + Gemini + Meta |
| Precio regional LATAM ~$7.49 (149 MXN), no $15 | Consensus | No (ya concedido en R2 por Opus/Meta) | Opus + Gemini + Meta |
| C-1 — Voto HÍBRIDO (Steam premium + demo web jugable = primera mitad del artefacto-puente, no marketing) | Consensus | No (convergencia total ya en R2) | Opus + Gemini + Meta |
| Cambio de mayor apalancamiento = correr el solver de papel del generador ANTES de un píxel | Consensus | No (estable) | Opus + Meta explícito; Gemini alinea vía "solver de dilemas" en su cambio top |

## Lista de lo aún contestado

1. **Banda de spread de EV (Crux 3).** Punto exacto de conflicto:
   - **Estructura:** Opus y Meta cierran en banda **DUAL** (un techo de re-siembra por liveness — >25% Opus / >20% Meta — Y un criterio de calidad estricto: solo tableros con spread **≤15%** cuentan como "foso vivo / duda real"). Gemini cierra en banda **ÚNICA** [15%-20%]: rechaza todo lo que cae fuera de ese rango.
   - **Umbral de calidad:** Gemini pone un **piso de 15%** (nada por debajo de 15% se acepta, "ajedrez seco"), lo que **contradice** directamente a Opus/Meta, para quienes el foso de calidad se mide precisamente **en y por debajo de 15%** (Opus admite piso ~8%; Meta cuenta ≤15%). Es decir: lo que para Gemini es el SUELO inaceptable es para los otros dos la BANDA de calidad.
   - **No endurecido:** los tres coinciden en que el número exacto es ⚪/🟡 y lo zanja el mismo test (solver de papel sobre 100 tableros + test del experto). El desacuerdo es de calibración, no de método, y hubo flips esta ronda → otra ronda corta enfocada solo en este número puede cerrarlo.

SCORE-INPUT: contested=1 flipped=2 consensus=8 total=9 verdict=CONVERGING
