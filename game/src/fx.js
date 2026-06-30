// ÓRDAGO — capa de juice (ligera). Canvas overlay para partículas + helpers DOM.
// Cosmético: NO porta información (doctrina visual-primario §3.4) — el juego es legible sin esto.
let cv, ctx, parts = [], raf = null;

export function initCanvas() {
  cv = document.getElementById('fx');
  ctx = cv.getContext('2d');
  resize(); window.addEventListener('resize', resize);
}
function resize() {
  if (!cv) return;
  cv.width = innerWidth; cv.height = innerHeight;
}

function tick() {
  ctx.clearRect(0, 0, cv.width, cv.height);
  parts = parts.filter((p) => p.life > 0);
  for (const p of parts) {
    p.x += p.vx; p.y += p.vy; p.vy += p.g; p.life -= 1; p.vx *= 0.99;
    ctx.globalAlpha = Math.max(0, p.life / p.max);
    ctx.fillStyle = p.c;
    ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, 7); ctx.fill();
  }
  ctx.globalAlpha = 1;
  if (parts.length) raf = requestAnimationFrame(tick); else raf = null;
}
function ensure() { if (!raf) raf = requestAnimationFrame(tick); }

function emit(x, y, n, colors, opts = {}) {
  for (let i = 0; i < n; i++) {
    const a = Math.random() * Math.PI * 2;
    const sp = (opts.speed || 4) * (0.4 + Math.random());
    parts.push({ x, y, vx: Math.cos(a) * sp, vy: Math.sin(a) * sp - (opts.up || 2),
      g: opts.g ?? 0.15, r: 2 + Math.random() * 3, c: colors[(Math.random() * colors.length) | 0],
      life: 40 + Math.random() * 25, max: 65 });
  }
  ensure();
}

export function escobaBurst(score, limpia) {
  const mesa = document.querySelector('.felt');
  const r = mesa ? mesa.getBoundingClientRect() : { left: innerWidth / 2, top: innerHeight / 2, width: 0, height: 0 };
  const x = r.left + r.width / 2, y = r.top + r.height / 2;
  const cols = limpia ? ['#7fd18a', '#e8b13a', '#fff'] : ['#e8b13a', '#d4495e', '#f3e9d6'];
  emit(x, y, limpia ? 46 : 26, cols, { speed: limpia ? 6 : 4, up: 2 });
  const app = document.getElementById('app');
  if (app) { app.classList.remove('shake'); void app.offsetWidth; app.classList.add('shake'); }
}

export function confetti() {
  for (let k = 0; k < 5; k++) setTimeout(() =>
    emit(innerWidth * (0.2 + Math.random() * 0.6), innerHeight * 0.3, 30,
      ['#e8b13a', '#d4495e', '#6fb36f', '#6f9bd1', '#fff'], { speed: 7, up: 4, g: 0.18 }), k * 120);
}

export function floatScore(anchor, text, color = '#e8b13a') {
  const r = anchor ? anchor.getBoundingClientRect() : { left: innerWidth / 2, top: innerHeight / 2, width: 0 };
  const el = document.createElement('div');
  el.className = 'float-score';
  el.textContent = text; el.style.color = color;
  el.style.left = (r.left + r.width / 2 - 30) + 'px';
  el.style.top = (r.top - 10) + 'px';
  el.style.fontSize = '1.6rem';
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1000);
}

let toastEl = null;
export function toast(msg) {
  if (toastEl) toastEl.remove();
  toastEl = document.createElement('div');
  toastEl.textContent = msg;
  Object.assign(toastEl.style, { position: 'fixed', bottom: '90px', left: '50%', transform: 'translateX(-50%)',
    background: '#241420', color: '#f3e9d6', padding: '8px 14px', borderRadius: '10px',
    border: '1px solid #50384a', zIndex: 70, fontSize: '.85rem', boxShadow: '0 6px 18px #0007' });
  document.body.appendChild(toastEl);
  setTimeout(() => { if (toastEl) { toastEl.remove(); toastEl = null; } }, 1800);
}
