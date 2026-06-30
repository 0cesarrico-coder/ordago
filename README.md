# ÓRDAGO — *La partida contra el Diablo*

> El **Balatro del mundo hispano**: súmale **15** sobre una Mesa viva para hacer **Escoba**, y
> vence al Diablo **haciéndole TRAMPA** —rompes sus reglas con tus Fullerías— usando la baraja
> española de la mesa de la cocina. Roguelike deckbuilder web-native (LATAM + USA + hispanos-USA).

**Estado:** prototipo jugable verificado · foso VALIDADO por solver de papel · demo web (Manga 1).

## Jugar (local)
```bash
cd game && python3 -m http.server 8731   # luego abrir http://localhost:8731/index.html
# deep-link con semilla fija: index.html?d=4
```

## Estructura (metodología claude-code-game-studios + GDD §14)
- `ORDAGO_Macro_GDD.md` — GDD macro v1.3.2 (validado por 2 ciclos multi-IA + 2 auditorías).
- `design/` — micro-GDD numérico · Style Bible · catálogo Concept-Visual-First.
- `solver/` — **solver de papel** (gate `balance-check`): valida/mata el foso ANTES de un píxel.
  `python3 solver/ordago_solver.py` → veredicto YELLOW (foso = decisión real, no puzzle).
- `game/` — prototipo jugable: lógica data-driven (`engine.js`/`content.js`/`game.js`) desacoplada
  del render (`main.js`/`fx.js`/`audio.js`). Vanilla JS, <1 MB, carga <1 s.

## Verificación
- `solver/HALLAZGOS-SOLVER.md` — Pareto 96.7% 🟢, cimiento 3.3% 🟢, S5/S7 🟢.
- `node game/test_smoke.mjs` — 300 partidas, ~60% win, 0 errores, lógica fiel.

🤖 Desarrollado con [Claude Code](https://claude.com/claude-code).
