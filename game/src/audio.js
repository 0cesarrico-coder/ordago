// ÓRDAGO — audio PROCEDURAL (WebAudio, cero assets → no infla el bundle <10MB).
// Doctrina §3.4: el audio AMPLIFICA, nunca porta info (el juego es legible en mute).
// §19.4: se arma en el 1.er gesto semántico; mute toggle. Timbre folk-barroco (campana + jarana).
let ctx = null, master = null, enabled = true;

export function arm() {
  if (ctx) return;
  try {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0.5; master.connect(ctx.destination);
  } catch (e) { ctx = null; }
}
export function setEnabled(v) { enabled = v; if (master) master.gain.value = v ? 0.5 : 0; }
export function isEnabled() { return enabled; }
export function resume() { if (ctx && ctx.state === 'suspended') ctx.resume(); }

function tone(freq, t0, dur, type = 'sine', gain = 0.3, glideTo = null) {
  if (!ctx || !enabled) return;
  const o = ctx.createOscillator(), g = ctx.createGain();
  o.type = type; o.frequency.setValueAtTime(freq, t0);
  if (glideTo) o.frequency.exponentialRampToValueAtTime(glideTo, t0 + dur);
  g.gain.setValueAtTime(0.0001, t0);
  g.gain.exponentialRampToValueAtTime(gain, t0 + 0.01);
  g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  o.connect(g); g.connect(master); o.start(t0); o.stop(t0 + dur + 0.02);
}
function noise(t0, dur, gain = 0.2, hp = 800) {
  if (!ctx || !enabled) return;
  const n = Math.floor(ctx.sampleRate * dur);
  const buf = ctx.createBuffer(1, n, ctx.sampleRate);
  const d = buf.getChannelData(0);
  for (let i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / n);
  const src = ctx.createBufferSource(); src.buffer = buf;
  const f = ctx.createBiquadFilter(); f.type = 'highpass'; f.frequency.value = hp;
  const g = ctx.createGain(); g.gain.value = gain;
  src.connect(f); f.connect(g); g.connect(master); src.start(t0);
}

const now = () => (ctx ? ctx.currentTime : 0);

export const sfx = {
  tap()    { tone(420, now(), 0.05, 'triangle', 0.12); },
  select() { tone(560, now(), 0.06, 'triangle', 0.14); },
  // barrido de la Escoba (ASMR §10.1): ruido filtrado + nota ascendente
  barrido(big) {
    const t = now();
    noise(t, 0.22, big ? 0.22 : 0.14, 600);
    tone(330, t, 0.18, 'sine', 0.18, 660);
    if (big) tone(660, t + 0.04, 0.22, 'triangle', 0.16, 990);
  },
  coin()   { const t = now(); tone(880, t, 0.05, 'square', 0.1); tone(1320, t + 0.04, 0.06, 'square', 0.08); },
  // "¡le hiciste trampa al Diablo!" — gesto pícaro descendente-ascendente
  cheat()  { const t = now(); tone(300, t, 0.1, 'sawtooth', 0.16, 200); tone(500, t + 0.08, 0.12, 'triangle', 0.16, 750); },
  pillado(){ const t = now(); tone(200, t, 0.18, 'sawtooth', 0.2, 90); noise(t, 0.12, 0.15, 300); },
  // firma sonora de marca (2-3 notas, campana grave + jarana) — splash/Última Mano (§10.1)
  firma() {
    const t = now();
    tone(196, t, 0.5, 'sine', 0.22, 196);          // campana grave (Sol)
    tone(294, t + 0.16, 0.5, 'triangle', 0.18);    // Re
    tone(392, t + 0.34, 0.7, 'triangle', 0.2);     // Sol agudo
    noise(t + 0.34, 0.3, 0.06, 1500);
  },
  lose()   { const t = now(); tone(220, t, 0.4, 'sawtooth', 0.18, 110); tone(165, t + 0.2, 0.5, 'sine', 0.16, 100); },
};
