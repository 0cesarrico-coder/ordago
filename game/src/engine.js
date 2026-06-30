// ÓRDAGO — motor de juego PURO (espejo de solver/engine.py, balance VALIDADO).
// Determinista por seed, headless, SIN render. La UI lee de aquí; nunca al revés.

import {
  PACTOS, FULLERIAS, TRAMPAS, MATAS, construirBaraja,
  TARGET_BASE, ESCOBA_LIMPIA_BONUS, ESCOBA_BONUS_FLAT, TRAMPA_PENALTY, TRAMPA_F3_BONUS,
} from './content.js';

// --- RNG determinista (mulberry32) ---
export function makeRNG(seed) {
  let s = seed >>> 0;
  return function () {
    s |= 0; s = (s + 0x6D2B79F5) | 0;
    let t = Math.imul(s ^ (s >>> 15), 1 | s);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
export function shuffle(arr, rng) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export function buildInfo(build) {
  const pactos = build.filter((b) => PACTOS[b]);
  const fullerias = build.filter((b) => FULLERIAS[b]);
  const rompe = new Set(fullerias.map((f) => FULLERIAS[f].rompe).filter(Boolean));
  return {
    pactos, fullerias, rompe,
    tiene_P1: pactos.includes('P1_oro'),
    tiene_P2: pactos.includes('P2_filo'),
    tiene_P3: pactos.includes('P3_bosque'),
    tiene_ojo: fullerias.includes('F0_ojo'),
    n_full_break: fullerias.filter((f) => FULLERIAS[f].rompe).length,
  };
}

export function newRunState() {
  return { veta_oro: 0, bloque_bosque: 0, suerte_filo: 0 };
}

// Estado de la Trampa: efecto mecánico (target/oros) + penalización neta si no se rompe.
export function trampaContext(trampaId, bi) {
  if (!trampaId) return { activa: false, target: TARGET_BASE, oros_bloqueados: false, penalty: 1 };
  const t = TRAMPAS[trampaId];
  const roto = bi.rompe.has(trampaId);
  // Efecto mecánico SOLO si no está roto (la Fullería exacta lo neutraliza).
  const target = (t.target && !roto) ? t.target : TARGET_BASE;
  const oros_bloqueados = !!(t.oros_bloqueados && !roto && !bi.fullerias.includes('F2_contrabando'));
  let penalty;
  if (roto) penalty = (trampaId === 'T3_primer_nulo') ? TRAMPA_F3_BONUS : 1;
  else penalty = Math.min(0.95, TRAMPA_PENALTY + 0.11 * bi.n_full_break);
  return { activa: true, trampaId, nombre: t.nombre, desc: t.desc, target, oros_bloqueados, penalty, roto };
}

// Enumerar capturas legales: 1 carta de mano + subconjunto de Mesa que suma target.
// F1 (Lectura Falsa) hace que una figura (v≥8) valga el valor elegido — en enumeración
// se generan todas las lecturas posibles.
export function enumeratePlays(hand, mesa, tctx, bi) {
  const target = tctx.target;
  const blockOros = tctx.oros_bloqueados;
  const usable = mesa.map((c, i) => i).filter((i) => !(blockOros && mesa[i].palo === 'O'));
  const out = new Map();
  const f1 = bi.fullerias.includes('F1_lectura_falsa');
  for (let hi = 0; hi < hand.length; hi++) {
    const hc = hand[hi];
    if (blockOros && hc.palo === 'O') continue;
    const hvals = (f1 && hc.v >= 8) ? [1,2,3,4,5,6,7,8,9,10] : [hc.v];
    for (const hv of hvals) {
      const need = target - hv;
      if (need < 0) continue;
      if (need === 0) { addPlay(out, hi, [], hc, mesa); continue; }
      subsetsSum(usable, mesa, need, (combo) => addPlay(out, hi, combo, hc, mesa));
    }
  }
  return [...out.values()];
}

function subsetsSum(idxs, mesa, need, cb) {
  // backtracking sobre índices usables que sumen need
  const n = idxs.length;
  const stack = [];
  (function rec(start, sum) {
    if (sum === need) { cb(stack.slice()); return; }
    if (sum > need) return;
    for (let k = start; k < n; k++) {
      const i = idxs[k];
      stack.push(i);
      rec(k + 1, sum + mesa[i].v);
      stack.pop();
    }
  })(0, 0);
}

function addPlay(map, hi, combo, hc, mesa) {
  const key = hi + '|' + combo.slice().sort((a, b) => a - b).join(',');
  if (map.has(key)) return;
  const captured = [hc, ...combo.map((i) => mesa[i])];
  map.set(key, { hand_idx: hi, subset_idx: combo.slice().sort((a, b) => a - b),
                 captured, empties_mesa: combo.length === mesa.length });
}

// Puntuar una jugada (NO muta rs). Espejo exacto del solver.
export function scorePlay(play, rs, bi, tctx, primeraDelEnvite = false) {
  const cap = play.captured;
  const oros = cap.filter((c) => c.palo === 'O').length;
  const espadas = cap.filter((c) => c.palo === 'E').length;
  const matas = cap.filter((c) => c.mata);

  let puntos = cap.reduce((s, c) => s + c.puntos_base, 0) + ESCOBA_BONUS_FLAT;
  if (play.empties_mesa) puntos += ESCOBA_LIMPIA_BONUS;
  puntos += 3 * bi.pactos.length;          // baseline Pacto
  puntos += 5 * bi.n_full_break;           // baseline Fullería (compensa la falta de motor)
  if (bi.tiene_P1) puntos += 1 * oros;
  if (bi.tiene_P3) puntos += 1 * cap.length;
  if (matas.some((m) => m.mata === 'as_bastos')) puntos += 4;
  if (bi.tiene_P1) puntos += rs.veta_oro;
  if (bi.tiene_P3) puntos += rs.bloque_bosque;

  let suerte = 1;
  if (bi.tiene_P2) { suerte += Math.min(rs.suerte_filo, 0.4); if (espadas > 0) suerte *= 1.10; }
  if (matas.some((m) => m.mata === 'as_espadas')) suerte *= 1.10;
  suerte = Math.min(suerte, 1.8);

  let score = puntos * suerte;
  // Trampa T3: 1ª escoba nula si no se rompe; penalización neta si se come en crudo.
  if (tctx.activa) {
    if (tctx.trampaId === 'T3_primer_nulo' && !tctx.roto && primeraDelEnvite) score = 0;
    score *= tctx.penalty;
  }

  // Ejes (para tells retrospectivos / debug; no se muestran prospectivos, §11.1)
  let seeds = 0;
  for (const c of cap) {
    if (c.mata || c.v > 4) continue;
    if ((bi.tiene_P1 && c.palo === 'O') || (bi.tiene_P2 && c.palo === 'E') || (bi.tiene_P3 && c.palo === 'B')) seeds++;
  }
  const escala = seeds * 6;
  const defensa = cap.reduce((s, c) => s + c.danger, 0) + (play.empties_mesa ? 10 : 0);
  return { score, puntos, suerte, tempo: score, escala, defensa, oros, espadas, seeds };
}

export function applyPlay(play, rs, bi) {
  const cap = play.captured;
  const low = (palo) => cap.filter((c) => c.palo === palo && c.v <= 4 && !c.mata).length;
  if (bi.tiene_P1) rs.veta_oro = Math.min(3, rs.veta_oro + low('O'));
  if (bi.tiene_P3) rs.bloque_bosque = Math.min(3, rs.bloque_bosque + low('B'));
  if (bi.tiene_P2) rs.suerte_filo = Math.min(0.4, rs.suerte_filo + 0.08 * low('E'));
}

// Sumas de 15 (o target) disponibles en la Mesa con una carta de mano — para el "Modo aprendiz" (§13.1).
export function sumasDisponibles(hand, mesa, tctx, bi) {
  const plays = enumeratePlays(hand, mesa, tctx, bi);
  // devuelve set de índices de mesa que participan en ALGUNA captura (resaltado de asistencia)
  const idx = new Set();
  for (const p of plays) for (const i of p.subset_idx) idx.add(i);
  return { plays, mesaResaltada: idx };
}
