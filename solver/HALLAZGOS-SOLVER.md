# HALLAZGOS DEL SOLVER DE PAPEL — ÓRDAGO Manga 1 (Fase 0, gate `balance-check`)

> Implementa §14.0 del Macro-GDD: **valida o mata el foso ANTES de un píxel.**
> Resultado completo y reproducible: `results/solver_report.json` (timestamped).
> Reproducir: `python3 solver/ordago_solver.py` (full ~45 s) o `--quick` (~3 s).

## Veredicto: 🟡 **YELLOW — FOSO VALIDADO. Proceder al prototipo.**

El gate más importante del proyecto (*"el verbo es puzzle, no decisión"*, riesgo nº1 §19.1) **pasa**:

| Gate | Resultado | Veredicto | Lectura |
|---|---|---|---|
| **Pareto ≥2 jugadas no-dominadas** | 96.7% | 🟢 | Cada tablero ofrece ≥2 jugadas con trade-off real (tempo/escala/defensa). |
| **Cimiento (≤1 jugada dominante)** | 3.3% | 🟢 | <4% de tableros colapsan a 1 jugada → **NO es un puzzle de solución única.** |
| **S5 escalado del umbral** | mediana 1.147× (p10 .94 / p90 1.43) | 🟢 | El umbral del Diablo está al borde justo (reto sin muralla ni trivialidad). |
| **S7 FTUE/Maestría** | 97% / 97% | 🟢 | Tanto el perfil novato como el experto encuentran decisión. |
| **Test del experto (lookahead)** | greedy 973 → k3 989 (+1.6%) | 🟡 | La previsión PAGA (motor de escala), aunque modesto — honesto para un card-game táctico. |
| **S4 dominancia de Maña** | top winrate 48.8%, 2/6 builds extremas viables | 🟡 | Ninguna build **degenerada** (>55%). Pero baja diversidad: los **mixes faustianos** (2P_1F, filo_x2F) ganan; las puras (3P, 3F) y 1-Pacto flojean. |
| **Banda EV (spread mejor↔2ª)** | 2.5% | 🔴 | Métrica ⚪ contestada del propio GDD (§7.3.3). Ver nota. |

## Qué quedó VALIDADO (proceder con confianza)
1. **El foso existe como decisión, no como aritmética.** La siembra intencional del Diablo
   (re-siembra acotada ≤8 para garantizar ≥2 jugadas Pareto, §7.3.2) **funciona**: produce 96.7%
   de tableros con bifurcación genuina. Sin ella caía a ~40% → el generador de bifurcación es
   **el componente de mayor apalancamiento**, confirmado.
2. **Los 3 ejes (tempo/escala/defensa) se decorrelacionan** cuando la Escala se ancla a
   cartas-semilla de bajo valor (que el greedy-tempo ignora) → la previsión es una estrategia real.
3. **El umbral del Diablo es calibrable** a la banda de reto (S5 🟢).

## Qué queda para PLAYTEST HUMANO (los amarillos — el GDD lo manda así, §14)
- **S4 / diversidad de builds (🟡):** en builds EXTREMAS fijas, los mixes dominan a las puras.
  *Pero las builds extremas son stress-tests:* el juego real usa la **Cantina adaptativa** (el
  jugador NO juega una build fija, la construye reaccionando a la Trampa del seed). La diversidad
  real se mide con la **entropía de builds ganadores por cohorte** (KPI §18) en telemetría, no en
  el solver. **Acción:** vigilar que ningún Pacto/Fullería domine >55% en cohortes reales; si pasa,
  responder con TRADE-OFF (no nerf de número), §18.
- **Test del experto (🟡, +1.6%):** la profundidad de previsión es real pero modesta. El GDD ya
  marca este eje 🟡/contestado (P1-5). El foso descansa más en el **trade-off Pareto por turno** +
  el **trade-off de slots de Maña** que en lookahead profundo. Aceptable para un verbo táctico.
- **Banda EV (🔴 2.5%, métrica ⚪):** el spread escalar entre las 2 mejores jugadas es bajo. Pero
  **el Pareto-front (96.7%) es la evidencia fuerte de profundidad**: las opciones son trade-offs
  genuinamente distintos (qué eje priorizar) que resultan cercanos en EV escalar — eso es **elección
  real, no arbitraria**. El GDD (§7.3.3, §14) dice explícitamente *"el número final lo fija el solver,
  no se hardcodea"* y lo marca ⚪. El número real lo zanjará el A/B de tells eco-gateados con humanos.

## Números cerrados del prototipo (fuente: `solver/content.py`, calibrados por el solver)
- Umbrales Manga 1: **chica 228 / grande 378 / Envite 358**; manos 5 / 6 / 7.
- Mesa 5–6 (siembra intencional ≥2 Pareto); mano 3; target 15.
- Escoba base = Σ puntos_base + **16 plano** (el base DOMINA; Pactos/Fullerías son modificadores).
- Baseline por slot: **Pacto +3 / Fullería +5** (la Fullería compensa con plano lo que el Pacto
  tiene de motor). Trampa en crudo = **×0.55** (progresivo +0.11/Fullería); romperla = ×1.0.
- Matas (base): As Espadas 13 (×1.1 Suerte) · As Bastos 11 (+4) · 7 Espadas 10 · 7 Oros 9.

> **Conclusión:** el cimiento aguanta. Construir el prototipo jugable (web) y llevar los 🟡 a
> playtest real es ahora el paso de mayor valor — el solver no puede resolverlos, los humanos sí.
