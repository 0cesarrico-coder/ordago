# ÓRDAGO — *La partida contra el Diablo*

> El **Balatro del mundo hispano**: súmale **15** sobre una Mesa viva para hacer **Escoba**, y
> vence al Diablo **haciéndole TRAMPA** —rompes sus reglas con tus Fullerías— usando la baraja
> española de la mesa de la cocina. Roguelike deckbuilder web-native (LATAM + USA + hispanos-USA).

**Estado (v0.5.0):** **listo para prueba de mercado** · foso VALIDADO por solver · demo web (Manga 1)
con telemetría de funnel, onboarding, Reto del Día + racha, share nativo, OG preview y PWA instalable.

## Jugar (local)
```bash
cd game && python3 -m http.server 8731   # luego abrir http://localhost:8731/index.html
# deep-link con semilla fija: index.html?d=4
```

## Lanzar la prueba con miles de jugadores
El juego ya está instrumentado y es testeable a escala. **Único paso manual** para capturar datos:
1. Crea una propiedad **GA4** (gratis) y copia tu `G-XXXXXXXXXX`.
2. Pégalo en [game/src/telemetry.js](game/src/telemetry.js) → `CONFIG.ga4Id`. (Opcional: `CONFIG.endpoint`
   para un colector propio tipo Cloudflare Worker.) Sin esto, los eventos solo van a `localStorage`
   (QA: `ordagoTelemetry.dump()` en consola) — el juego funciona, pero no agregas datos de campo.
3. Despliega (GitHub Pages ya activo) y difunde el link. El share nativo + OG preview alimentan
   el motor viral (WhatsApp/Telegram). El Reto del Día (misma mesa para todos) + racha dan retención.

**Funnel instrumentado** (sin PII, id anónimo persistente): `session_start → intro_view → run_start
→ bet_start → escoba/pass → bet_won/bet_lost → cantina_view/cantina_buy → run_won/run_lost →
share_click/share_done · daily_won · js_error`. Cada evento lleva seed, modo (random/daily/shared),
build, device, locale (es-419/en-US…) → segmentable por LATAM / USA-hispano / España.

**Roadmap post-test** (expandir según lo que enseñe la prueba, no antes): Mangas 2-4, más Tahúres
y Trampas, arte de caras de carta (oleada 2-3), leaderboard con backend.

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
- Navegador (Playwright): 390×844 / 360×640 / desktop, 0 errores de consola; funnel disparando;
  SW registrado, manifest + íconos OK, Web Share disponible.

🤖 Desarrollado con [Claude Code](https://claude.com/claude-code).
