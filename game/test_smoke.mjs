// Smoke test del port JS: juega Mangas completas con un bot greedy-score y verifica
// que el loop corre sin excepciones y que el juego es ganable en una fracción razonable.
import { Game } from './src/game.js';
import { enumeratePlays, scorePlay } from './src/engine.js';
import { BUILD_INICIAL, APUESTAS_MANGA1 } from './src/content.js';

function botPlayApuesta(g) {
  let guard = 0;
  while (g.status === 'playing' && guard++ < 60) {
    const plays = enumeratePlays(g.hand, g.mesa, g.tctx, g.bi);
    if (plays.length === 0) {
      // pasar la carta más baja
      let lo = 0; for (let i = 1; i < g.hand.length; i++) if (g.hand[i].v < g.hand[lo].v) lo = i;
      g.pasar(lo);
      continue;
    }
    // elegir la jugada de mayor score
    let best = plays[0], bestScore = -1;
    for (const p of plays) {
      const sc = scorePlay(p, g.rs, g.bi, g.tctx, g.enEnvite && !g.primeraEscobaHecha);
      if (sc.score > bestScore) { bestScore = sc.score; best = p; }
    }
    g.jugarEscoba(best.hand_idx, best.subset_idx);
  }
}

function playGame(seed) {
  const g = new Game(seed, BUILD_INICIAL.slice());
  for (let i = 0; i < APUESTAS_MANGA1.length; i++) {
    g.startApuesta(i);
    botPlayApuesta(g);
    if (g.status === 'lost') return { win: false, reached: i };
    if (g.status === 'won') return { win: true, reached: 3 };
    // apuesta_won → equipar la counter-fullería si está y seguir
    if (g.status === 'apuesta_won' && i < 2) {
      const ofertas = g.ofertasCantina();
      const counter = ofertas.find((o) => o.rompeEnvite);
      if (counter && g.reales >= counter.costo) g.equipar(counter.id, 2, counter.costo);
    }
  }
  return { win: g.status === 'won', reached: g.apuestaIndex };
}

let wins = 0, errors = 0, reached = [0, 0, 0, 0];
const N = 300;
for (let s = 0; s < N; s++) {
  try {
    const r = playGame(s);
    if (r.win) wins++;
    reached[r.reached]++;
  } catch (e) { errors++; if (errors <= 3) console.error('ERR seed', s, e.message); }
}
console.log(`Smoke: ${N} partidas · wins=${wins} (${(wins/N*100).toFixed(1)}%) · errores=${errors}`);
console.log(`Llegaron hasta apuesta: 0=${reached[0]} 1=${reached[1]} 2=${reached[2]} ganó=${reached[3]}`);
console.log(errors === 0 ? '✓ Sin excepciones — loop OK' : '✗ Hubo excepciones');
