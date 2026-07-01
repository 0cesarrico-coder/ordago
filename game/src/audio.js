// ÓRDAGO — audio PROCEDURAL (WebAudio, cero assets → no infla el bundle <10MB).
// Doctrina §3.4: el audio AMPLIFICA, nunca porta info (el juego es legible en mute).
// §19.4: se arma en el 1.er gesto semántico; mute toggle. Timbre folk-barroco (campana + jarana).
let ctx = null, master = null, reverb = null, enabled = true;

// impulso de reverb sintético (cola exponencial) → espacio de cantina, sin assets
function makeImpulse(seconds = 1.6, decay = 3.2) {
  const rate = ctx.sampleRate, len = Math.floor(rate * seconds);
  const buf = ctx.createBuffer(2, len, rate);
  for (let ch = 0; ch < 2; ch++) {
    const d = buf.getChannelData(ch);
    for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, decay);
  }
  return buf;
}

export function arm() {
  if (ctx) return;
  try {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0.5; master.connect(ctx.destination);
    // bus de reverb (send) — da cuerpo y "sala" a todo
    try {
      const conv = ctx.createConvolver(); conv.buffer = makeImpulse();
      const wet = ctx.createGain(); wet.gain.value = 0.22;
      conv.connect(wet); wet.connect(master); reverb = conv;
    } catch (e) { reverb = null; }
  } catch (e) { ctx = null; }
}
export function setEnabled(v) { enabled = v; if (master) master.gain.value = v ? 0.5 : 0; }
export function isEnabled() { return enabled; }
export function resume() { if (ctx && ctx.state === 'suspended') ctx.resume(); }

function tone(freq, t0, dur, type = 'sine', gain = 0.3, glideTo = null, send = 0.5) {
  if (!ctx || !enabled) return;
  const o = ctx.createOscillator(), g = ctx.createGain();
  o.type = type; o.frequency.setValueAtTime(freq, t0);
  if (glideTo) o.frequency.exponentialRampToValueAtTime(glideTo, t0 + dur);
  g.gain.setValueAtTime(0.0001, t0);
  g.gain.exponentialRampToValueAtTime(gain, t0 + 0.01);
  g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
  o.connect(g); g.connect(master);
  if (reverb && send) { const s = ctx.createGain(); s.gain.value = send; g.connect(s); s.connect(reverb); }
  o.start(t0); o.stop(t0 + dur + 0.02);
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
  select() { tone(560, now(), 0.06, 'triangle', 0.14); tone(840, now() + 0.01, 0.04, 'sine', 0.06); },
  // carta que cae sobre el fieltro (thock suave + aire)
  place()  { const t = now(); tone(150, t, 0.09, 'sine', 0.16, 90, 0.2); noise(t, 0.05, 0.06, 1200); },
  deal()   { const t = now(); noise(t, 0.04, 0.05, 1600); tone(520, t, 0.04, 'triangle', 0.06); },
  // barrido de la Escoba (ASMR §10.1): ruido filtrado en abanico + acorde ascendente + brillo
  barrido(big) {
    const t = now();
    noise(t, big ? 0.3 : 0.2, big ? 0.24 : 0.15, 500);
    noise(t + 0.05, 0.18, big ? 0.14 : 0.08, 2200);          // shimmer/aire
    tone(330, t, 0.2, 'sine', 0.18, 660, 0.7);
    tone(392, t + 0.03, 0.2, 'triangle', 0.12, 784, 0.7);
    if (big) { tone(660, t + 0.05, 0.26, 'triangle', 0.16, 990, 0.9);
      tone(988, t + 0.12, 0.3, 'sine', 0.1, 1320, 0.9); }    // destello agudo
  },
  coin()   { const t = now(); tone(880, t, 0.05, 'square', 0.1); tone(1320, t + 0.04, 0.06, 'square', 0.08);
    tone(1760, t + 0.08, 0.06, 'sine', 0.05); },
  // "¡le hiciste trampa al Diablo!" — gesto pícaro descendente-ascendente
  cheat()  { const t = now(); tone(300, t, 0.1, 'sawtooth', 0.16, 200); tone(500, t + 0.08, 0.12, 'triangle', 0.16, 750); },
  pillado(){ const t = now(); tone(200, t, 0.18, 'sawtooth', 0.2, 90); noise(t, 0.12, 0.15, 300); },
  // firma sonora de marca (arpegio folk campana + jarana, con cola de reverb) — splash/victoria (§10.1)
  firma() {
    const t = now();
    tone(196, t, 0.7, 'sine', 0.20, 196, 0.9);       // campana grave (Sol)
    tone(294, t + 0.14, 0.6, 'triangle', 0.16, null, 0.9);   // Re
    tone(392, t + 0.30, 0.6, 'triangle', 0.16, null, 0.9);   // Sol
    tone(494, t + 0.44, 0.8, 'sine', 0.16, null, 1);         // Si (acorde mayor)
    tone(784, t + 0.58, 0.9, 'triangle', 0.12, null, 1);     // Sol agudo brillante
    noise(t + 0.30, 0.35, 0.05, 1600);
  },
  lose()   { const t = now(); tone(220, t, 0.4, 'sawtooth', 0.18, 110); tone(165, t + 0.2, 0.5, 'sine', 0.16, 100); },
};
