// ÓRDAGO — controlador + render del prototipo. La LÓGICA vive en game/engine/content;
// aquí solo orquestamos pantallas, input y juice. (Separación logic/render — best practice.)
import { Game } from './game.js';
import {
  PALO_GLYPH, NOMBRE_VALOR, PACTOS, FULLERIAS, BUILD_INICIAL, TRAMPAS, nombreCarta,
} from './content.js';
import * as fx from './fx.js';
import * as audio from './audio.js';

const app = document.getElementById('app');
let game = null;
let sel = { handIdx: null, mesa: new Set() };
let prevScore = 0;          // para el count-up de la barra
let cheatShown = false;     // beat de "trampa rota" mostrado una vez por Envite

// seed: de la URL (?d=seed para el deep-link §8.3) o aleatorio.
function pickSeed() {
  const u = new URLSearchParams(location.search).get('d');
  if (u && /^\d+$/.test(u)) return parseInt(u, 10) >>> 0;
  return (Math.floor(Math.random() * 1e9)) >>> 0;
}

// ---------------- Pantallas ----------------
function screenIntro() {
  app.innerHTML = `
    <div class="screen">
      <div class="diablo-cara">😈</div>
      <h1>ÓRDAGO</h1>
      <p><b>La partida contra el Diablo.</b><br>Suma <b>15</b> sobre la Mesa para hacer <b>Escoba</b>.
      El Diablo hace trampa; tú le haces <b>más trampa</b> con tus Fullerías.</p>
      <p class="small">Gana las 3 apuestas de la Manga para recuperar tu alma.</p>
      <button class="btn primary" id="play" style="max-width:240px">Repartir cartas</button>
      <p class="small">Semilla #${seedShown}</p>
    </div>`;
  document.getElementById('play').onclick = () => {
    audio.arm(); audio.resume(); audio.sfx.firma();   // arma audio en el 1.er gesto (§19.4)
    prevScore = 0; cheatShown = false;
    game.startApuesta(0); renderPlay();
  };
}

function renderPlay() {
  const s = game.getState();
  const t = s.tctx;
  const target = (s.enEnvite && t.activa) ? t.target : 15;
  const pct = Math.min(100, (s.scoreApuesta / s.umbral) * 100);
  app.innerHTML = `
    <div class="hud">
      <div class="hud-top">
        <span class="apuesta-nom">${s.apuesta.nombre}</span>
        <span><button id="mute" class="mutebtn">${audio.isEnabled() ? '🔊' : '🔇'}</button>
          <span class="reales">Reales: <b>${s.reales}</b> 🪙</span></span>
      </div>
      <div class="barra-wrap"><div class="barra" style="width:${pct}%"></div>
        <div class="barra-txt">${Math.round(s.scoreApuesta)} / ${s.umbral}</div></div>
      <div class="hud-bottom">
        <span class="manos">Manos: <b>${s.manosLeft}</b></span>
        <span>Apuesta ${s.apuestaIndex + 1}/3</span>
        <span>Objetivo: sumar <b>${target}</b></span>
      </div>
    </div>
    ${s.enEnvite ? trampaBanner(t) : ''}
    ${manaSlots(s.build)}
    ${(s.apuestaIndex === 0 && s.manosLeft === s.apuesta.manos)
      ? '<div class="comojugar">Toca una carta de tu <b>mano</b>, luego cartas de la <b>Mesa</b> que sumen <b>15</b> con ella → <b>ESCOBA</b>.</div>' : ''}
    <div class="felt">
      <span class="felt-label">LA MESA DEL DIABLO</span>
      <div class="mesa" id="mesa">${s.mesa.map((c, i) =>
        cardHTML(c, 'mesa', i, sel.mesa.has(i), false, oroBloqueado(c, t))).join('')}</div>
    </div>
    <div class="suma" id="suma"></div>
    <div class="mano-zona">
      <div class="mano-label">TU MANO</div>
      <div class="mano" id="mano">${s.hand.map((c, i) =>
        cardHTML(c, 'hand', i, sel.handIdx === i, false, false)).join('')}</div>
    </div>
    <div class="acciones">
      <button class="btn ghost" id="pasar">Pasar 🃏</button>
      <button class="btn primary" id="escoba" disabled>ESCOBA</button>
    </div>`;

  wirePlay();
  updateSuma();
  // count-up de la barra desde el score previo (juice §10)
  countUpBar(prevScore, s.scoreApuesta, s.umbral);
  prevScore = s.scoreApuesta;
  // beat "le hiciste trampa al Diablo" cuando entras al Envite con la Trampa ya rota (§7.6)
  if (s.enEnvite && t.roto && !cheatShown) {
    cheatShown = true;
    audio.sfx.cheat();
    fx.toast('😏 Rompiste la Trampa del Diablo');
  }
}

function countUpBar(from, to, umbral) {
  const txt = document.querySelector('.barra-txt');
  if (!txt || from === to) return;
  const t0 = performance.now(), dur = 420;
  (function step(t) {
    const k = Math.min(1, (t - t0) / dur);
    const v = Math.round(from + (to - from) * (1 - Math.pow(1 - k, 3))); // ease-out cubic
    txt.textContent = `${v} / ${umbral}`;
    if (k < 1) requestAnimationFrame(step);
  })(t0);
}

function trampaBanner(t) {
  return `<div class="trampa ${t.roto ? 'rota' : ''}">
    ${t.roto ? '✓ Trampa rota: ' : '👹 Trampa del Diablo: '}
    <span class="t-nom">${t.nombre}</span> — ${t.desc}${t.roto ? ' <b>(¡neutralizada!)</b>' : ''}</div>`;
}

function manaSlots(build) {
  return `<div class="mana">${build.map((id) => {
    const p = PACTOS[id], f = FULLERIAS[id];
    const tipo = p ? 'pacto' : 'fulleria';
    const d = p || f || { nombre: id, icon: '·' };
    return `<div class="slot ${tipo}"><span class="ico">${d.icon || (p ? '🜄' : '👁')}</span>
      <span class="nm">${d.nombre}</span></div>`;
  }).join('')}</div>`;
}

function cardHTML(c, zona, i, selected, hint, oroBloq) {
  const fig = NOMBRE_VALOR[c.v];               // 'Sota'|'Caballo'|'Rey' o undefined
  const cls = ['carta', `p-${c.palo}`, selected ? 'sel' : '', hint ? 'hint' : '',
    c.mata ? 'mata' : '', oroBloq ? 'oro-bloq' : ''].filter(Boolean).join(' ');
  return `<div class="${cls}" data-zona="${zona}" data-i="${i}">
    <span class="esq">${c.v}${PALO_GLYPH[c.palo]}</span>
    ${fig ? `<span class="fig">${fig}</span>` : ''}
    <span class="v">${c.v}</span>
    <span class="palo">${PALO_GLYPH[c.palo]}</span>
    ${c.mata ? '<span class="mata-pip">★</span>' : ''}</div>`;
}

// Resaltado de asistencia (§13.1): qué cartas de la Mesa completan un 15 con la carta de mano elegida.
function computeHints(handIdx) {
  const set = new Set();
  if (handIdx === null) return set;
  const s = game.getState();
  const plays = game.asistencia().plays.filter((p) => p.hand_idx === handIdx);
  for (const p of plays) for (const i of p.subset_idx) set.add(i);
  return set;
}

function oroBloqueado(c, t) { return t && t.activa && t.oros_bloqueados && c.palo === 'O'; }

// ---------------- Interacción ----------------
function wirePlay() {
  document.querySelectorAll('.carta').forEach((el) => {
    el.onclick = () => {
      const zona = el.dataset.zona, i = +el.dataset.i;
      if (zona === 'hand') { sel.handIdx = (sel.handIdx === i ? null : i); sel.mesa.clear(); audio.sfx.select(); }
      else {
        const s = game.getState();
        if (oroBloqueado(s.mesa[i], s.tctx)) return; // bloqueada por Trampa
        if (sel.mesa.has(i)) sel.mesa.delete(i); else { sel.mesa.add(i); audio.sfx.tap(); }
      }
      refreshSelection();
    };
  });
  document.getElementById('escoba').onclick = onEscoba;
  document.getElementById('pasar').onclick = onPasar;
  const mb = document.getElementById('mute');
  if (mb) mb.onclick = () => { audio.setEnabled(!audio.isEnabled()); mb.textContent = audio.isEnabled() ? '🔊' : '🔇'; };
}

function refreshSelection() {
  const hints = computeHints(sel.handIdx); // modo aprendiz: completa-15 con la carta elegida
  document.querySelectorAll('.carta').forEach((el) => {
    const zona = el.dataset.zona, i = +el.dataset.i;
    const seld = (zona === 'hand' && sel.handIdx === i) || (zona === 'mesa' && sel.mesa.has(i));
    el.classList.toggle('sel', seld);
    el.classList.toggle('hint', zona === 'mesa' && !seld && hints.has(i));
  });
  updateSuma();
}

function effTarget() {
  const s = game.getState();
  return (s.enEnvite && s.tctx.activa) ? s.tctx.target : 15;
}

function updateSuma() {
  const sumaEl = document.getElementById('suma');
  const escEl = document.getElementById('escoba');
  if (sel.handIdx === null) { sumaEl.innerHTML = '<span class="small">Elige una carta de tu mano…</span>'; escEl.disabled = true; return; }
  const s = game.getState();
  const target = effTarget();
  const hc = s.hand[sel.handIdx];
  const mesaSum = [...sel.mesa].reduce((a, i) => a + s.mesa[i].v, 0);
  const f1 = s.bi.fullerias.includes('F1_lectura_falsa') && hc.v >= 8;
  let handVal = hc.v, comodin = '';
  if (f1) { const need = target - mesaSum; if (need >= 1 && need <= 10) { handVal = need; comodin = ' <span class="small">(Lectura Falsa: tu figura se lee ' + need + ')</span>'; } }
  const total = handVal + mesaSum;
  const play = sel.mesa.size >= 0 ? game.validarSeleccion(sel.handIdx, [...sel.mesa]) : null;
  const ok = !!play;
  sumaEl.className = 'suma' + (ok ? ' ok' : '');
  sumaEl.innerHTML = ok
    ? `<span class="n">${target}</span> <span class="target">¡ESCOBA!</span>`
    : `<span class="n">${total}</span> / <span class="target">${target}</span>${comodin}`;
  escEl.disabled = !ok;
}

function onEscoba() {
  const escEl = document.getElementById('escoba');
  const res = game.jugarEscoba(sel.handIdx, [...sel.mesa]);
  if (!res.ok) return;
  audio.sfx.barrido(res.escobaLimpia);
  fx.escobaBurst(res.score, res.escobaLimpia);
  // Puntos×Suerte: el número grande es CONSECUENCIA, no mult en el vacío (§7.7)
  if (res.score > 0) {
    fx.floatScore(escEl, `${Math.round(res.puntos)}×${res.suerte.toFixed(1)} = +${Math.round(res.score)}`,
      res.escobaLimpia ? '#7fd18a' : '#e8b13a');
    if (res.escobaLimpia) fx.toast('🧹 ¡Escoba limpia! Mesa vacía');
  }
  if (res.nulaT3) fx.floatScore(escEl, 'NULA (Trampa del Diablo)', '#e0617a');
  sel = { handIdx: null, mesa: new Set() };
  setTimeout(() => afterAction(res), 300);   // hit-stop breve (game-feel)
}
function onPasar() {
  if (sel.handIdx === null) { fx.toast('Elige qué carta dejas en la Mesa'); return; }
  const res = game.pasar(sel.handIdx);
  sel = { handIdx: null, mesa: new Set() };
  afterAction(res);
}

function afterAction(res) {
  const st = game.status;
  if (st === 'won') { audio.sfx.firma(); return renderWin(); }
  if (st === 'lost') { audio.sfx.lose(); return renderLose(); }
  if (st === 'apuesta_won') { audio.sfx.coin(); cheatShown = false; prevScore = 0; return renderCantina(res); }
  renderPlay();
}

// ---------------- Cantina ----------------
function renderCantina() {
  const s = game.getState();
  const ofertas = game.ofertasCantina();
  const next = game.apuestaIndex + 1;
  const proximaTrampa = next === 2 ? s.trampaEnvite : null;
  app.innerHTML = `
    <div class="screen">
      <h2>🍷 La Cantina del Tahúr</h2>
      <p>Superaste <b>${s.apuesta.nombre}</b>. Reales: <b>${s.reales}</b> 🪙</p>
      ${proximaTrampa ? `<p class="small">⚠️ El Envite traerá la Trampa <b style="color:#e8b13a">${proximaTrampa.nombre}</b> — ${proximaTrampa.desc}. Equipa su Fullería para romperla.</p>` : ''}
      <p>Equipa una Maña (reemplaza una ranura). Tus ranuras:</p>
      <div class="mana">${s.build.map((id, i) => {
        const d = PACTOS[id] || FULLERIAS[id] || { nombre: id, icon: '·' };
        return `<div class="slot ${PACTOS[id] ? 'pacto' : 'fulleria'}" data-slot="${i}">
          <span class="ico">${d.icon}</span><span class="nm">${d.nombre}</span></div>`;
      }).join('')}</div>
      <div class="ofertas">${ofertas.map((o, k) => `
        <div class="oferta ${o.rompeEnvite ? 'counter' : ''}" data-k="${k}">
          <span class="ico">${o.data.icon}</span>
          <span class="nm">${o.data.nombre}</span>
          <span class="ds">${o.data.desc}</span>
          ${o.rompeEnvite ? '<span class="small" style="color:#e8b13a">rompe el Envite</span>' : ''}
          <span class="costo">${o.costo} 🪙</span>
          <button data-k="${k}" ${s.reales < o.costo ? 'disabled' : ''}>Equipar</button>
        </div>`).join('')}</div>
      <button class="btn primary" id="next" style="max-width:260px">Seguir a ${nextNombre(next)} →</button>
    </div>`;

  let pendiente = null;
  app.querySelectorAll('.oferta button').forEach((b) => b.onclick = () => {
    pendiente = ofertas[+b.dataset.k];
    app.querySelectorAll('.oferta').forEach((o) => o.classList.toggle('counter', false));
    b.closest('.oferta').classList.add('counter');
    fx.toast('Ahora toca la ranura a reemplazar');
    app.querySelectorAll('.slot[data-slot]').forEach((sl) => sl.onclick = () => {
      if (!pendiente) return;
      if (game.equipar(pendiente.id, +sl.dataset.slot, pendiente.costo)) { audio.sfx.coin(); fx.toast('Equipado ✓'); renderCantina(); }
      else fx.toast('Reales insuficientes');
    });
  });
  document.getElementById('next').onclick = () => { game.startApuesta(next); renderPlay(); };
}
function nextNombre(i) { return ['La Chica', 'La Grande', 'El Envite del Diablo'][i] || ''; }

// ---------------- Fin ----------------
function buildArquetipo(s) {
  const p = s.bi.pactos[0];
  const m = { P1_oro: 'del Oro', P2_filo: 'del Filo', P3_bosque: 'del Bosque' }[p] || 'Tahúr';
  return `Escobero ${m}`;
}
function renderWin() {
  const s = game.getState();
  const grito = '¡TE GANÉ, DIABLO!';
  fx.confetti();
  app.innerHTML = `
    <div class="screen">
      <h1>¡Recuperaste tu alma!</h1>
      <p>Le hiciste trampa al Diablo y ganaste la Manga.</p>
      <div class="sticker">
        <span class="stamp">Semilla #${s.seed}</span>
        <span class="diablo">😈💀</span>
        <span class="grito">${grito}</span>
        <span class="linea">Soy <b>${buildArquetipo(s)}</b></span>
        <span class="linea small">ordago.gg/d/${s.seed} — vencí al Diablo</span>
      </div>
      <p class="small">Comparte tu ficha y reta a alguien con esta misma semilla.</p>
      <button class="btn primary" id="again" style="max-width:240px">Otra partida</button>
    </div>`;
  document.getElementById('again').onclick = restart;
}
function renderLose() {
  const s = game.getState();
  app.innerHTML = `
    <div class="screen">
      <div class="diablo-cara">😈</div>
      <h2>El Diablo se queda tu alma… por ahora.</h2>
      <p>Llegaste a <b>${Math.round(s.scoreApuesta)}</b> de ${s.umbral} en ${s.apuesta.nombre}.</p>
      <p class="small">Derrotaste ${s.apuestaIndex} ${s.apuestaIndex === 1 ? 'apuesta' : 'apuestas'} · mejor jugada de tahúr.</p>
      <button class="btn primary" id="again" style="max-width:240px">Volver a intentar</button>
    </div>`;
  document.getElementById('again').onclick = restart;
}

// ---------------- Bootstrap ----------------
let seedShown = 0;
function restart() {
  const seed = pickSeed(); seedShown = seed;
  game = new Game(seed, BUILD_INICIAL.slice());
  sel = { handIdx: null, mesa: new Set() };
  screenIntro();
}
fx.initCanvas();
restart();

// exponer para smoke test / debug
import { scorePlay } from './engine.js';
window.__ordago = { get game() { return game; }, restart, scorePlay };
