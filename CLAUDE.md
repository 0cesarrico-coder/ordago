# ÓRDAGO — guía del proyecto (CLAUDE.md)

Roguelike deckbuilder con baraja española. "El Balatro hispano: le haces TRAMPA al Diablo."
Metodología: **claude-code-game-studios** (Design → Architecture → Stories → Dev → **Quality gates** → Release)
+ el orden de falsación del propio GDD (§14): **solver de papel → prototipo → vertical slice**.

## Fuentes de verdad
- `ORDAGO_Macro_GDD.md` — GDD macro v1.3.2 (north-star, validado por 2 ciclos multi-IA + 2 auditorías).
- `design/MICRO-GDD-prototipo.md` — números concretos del prototipo.
- `solver/content.py` — **fuente de verdad de los números** (calibrados por el solver). `game/` los reusa.
- `solver/HALLAZGOS-SOLVER.md` — veredicto del gate `balance-check` (foso validado 🟡).

## Quality gates (path-scoped, estilo CCGS)
- **Gameplay (`game/`, `solver/`):** valores data-driven (NO hardcode); lógica desacoplada del render;
  determinista por seed (Monte Carlo gratis). El balance se valida con el solver ANTES del arte.
- **Foso:** ningún cambio de mecánica core sin re-correr `solver/ordago_solver.py` (Pareto ≥95%, cimiento <20%).
- **Doctrina visual-primario (§3.4):** el estado del juego debe ser 100% legible en silencio (mute=default LATAM).
- **Latencia (§10):** tocar <50 ms, suma/preview <80 ms, Escoba <100 ms; animaciones 100–300 ms.

## Control de versiones
Proyecto de juego → commit + push autorizados sin preguntar tras cada checkpoint VERIFICADO
(gates verdes primero). Conventional commits + Co-Authored-By.

## Stack del prototipo
Vanilla JS (ES modules) + DOM/CSS para cartas + Canvas overlay para juice + WebAudio. <10 MB, carga <3 s.
