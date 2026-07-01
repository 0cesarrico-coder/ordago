// ÓRDAGO — telemetría (instrumentación para la prueba de mercado con miles de jugadores).
//
// Diseño zero-lock-in y sin backend propio:
//  1) window.dataLayer.push(...)  → si el usuario pega el snippet GA4/GTM, los eventos fluyen solos.
//  2) gtag('event', ...)          → si gtag existe, evento nativo GA4 (Measurement Protocol gratuito).
//  3) localStorage (ring buffer)  → QA local + fallback; inspeccionable con ordagoTelemetry.dump().
//  4) navigator.sendBeacon(URL)   → si CONFIG.endpoint está seteado, colector propio (Worker/CF/etc).
//
// Sin PII: id de cliente anónimo (uuid en localStorage), nada de nombres/emails. Apto LATAM/USA.

export const VERSION = '0.7.1';            // se incrementa por release; viaja en cada evento
// NOTA: al cambiar cualquier archivo del shell, sube TAMBIÉN VERSION en sw.js → el caché se refresca
// atómicamente (todo el shell junto) y evita mismatch entre módulos (p.ej. main.js nuevo + audio.js viejo).
const LS_CID = 'ordago.cid';
const LS_BUF = 'ordago.telemetry';         // ring buffer de eventos (QA)
const BUF_MAX = 200;

// CONFIG: el usuario rellena ga4Id con su "G-XXXXXXXXXX" y/o endpoint con su colector.
// Mientras estén vacíos, la telemetría NO hace red (solo dataLayer + localStorage) → cero coste,
// cero bloqueo de privacidad, y el día que pegue su ID empieza a medir sin tocar más código.
export const CONFIG = {
  ga4Id: '',          // p.ej. 'G-XXXXXXXXXX' — ver index.html (snippet listo, comentado)
  endpoint: '',       // p.ej. 'https://telemetria.tu-worker.dev/e' — recibe POST JSON
};

function uuid() {
  // RFC4122 v4 con crypto si está; si no, fallback determinista-suficiente (no es seguridad).
  if (globalThis.crypto?.randomUUID) return crypto.randomUUID();
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0, v = c === 'x' ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

function clientId() {
  try {
    let id = localStorage.getItem(LS_CID);
    if (!id) { id = uuid(); localStorage.setItem(LS_CID, id); }
    return id;
  } catch { return 'no-storage'; }
}

// id de sesión: una "visita". Se renueva por carga de página.
const SESSION_ID = uuid().slice(0, 8);
const START_TS = Date.now();

function deviceCtx() {
  const w = window.innerWidth, h = window.innerHeight;
  const mobile = Math.min(w, h) <= 600 || /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent || '');
  return {
    v: VERSION,
    plat: mobile ? 'mobile' : 'desktop',
    vw: w, vh: h, dpr: Math.round((window.devicePixelRatio || 1) * 100) / 100,
    lang: (navigator.language || 'es').slice(0, 8),   // 'es-419' (LatAm) / 'es-ES' / 'en-US' completos
    ref: document.referrer ? new URL(document.referrer).hostname : '(direct)',
  };
}

function pushBuf(evt) {
  try {
    const buf = JSON.parse(localStorage.getItem(LS_BUF) || '[]');
    buf.push(evt);
    while (buf.length > BUF_MAX) buf.shift();
    localStorage.setItem(LS_BUF, JSON.stringify(buf));
  } catch { /* storage lleno o bloqueado: no es fatal */ }
}

let seq = 0;
/** Emite un evento por todos los sinks disponibles. props: objeto plano sin PII. */
export function track(event, props = {}) {
  const evt = {
    event,
    cid: clientId(),
    sid: SESSION_ID,
    seq: seq++,
    t: Date.now(),
    dt: Date.now() - START_TS,   // ms desde carga (para construir funnels temporales)
    ...deviceCtx(),
    ...props,
  };
  // 1) dataLayer (GTM/GA4 sin gtag)
  (window.dataLayer = window.dataLayer || []).push({ ...evt, event: 'ordago_' + event });
  // 2) gtag nativo
  if (typeof window.gtag === 'function') {
    try { window.gtag('event', event, props); } catch { /* noop */ }
  }
  // 3) ring buffer QA
  pushBuf(evt);
  // 4) beacon a colector propio
  if (CONFIG.endpoint) {
    try {
      const body = JSON.stringify(evt);
      if (navigator.sendBeacon) navigator.sendBeacon(CONFIG.endpoint, body);
      else fetch(CONFIG.endpoint, { method: 'POST', body, keepalive: true, mode: 'no-cors' });
    } catch { /* red caída: el evento ya quedó en localStorage */ }
  }
  return evt;
}

// Captura de errores no atrapados → para saber si el juego se rompió en el campo (clave a escala).
let errCount = 0;
export function installErrorCapture() {
  window.addEventListener('error', (e) => {
    if (errCount++ > 10) return;   // anti-spam
    track('js_error', { msg: String(e.message || '').slice(0, 180), src: (e.filename || '').slice(-60), ln: e.lineno || 0 });
  });
  window.addEventListener('unhandledrejection', (e) => {
    if (errCount++ > 10) return;
    track('js_reject', { msg: String(e.reason?.message || e.reason || '').slice(0, 180) });
  });
}

// init GA4 gtag si el usuario configuró su ID (sin él, no carga nada externo).
export function initAnalytics() {
  if (!CONFIG.ga4Id) return;
  const s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + CONFIG.ga4Id;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { window.dataLayer.push(arguments); };
  window.gtag('js', new Date());
  window.gtag('config', CONFIG.ga4Id, { anonymize_ip: true });
}

// Utilidad de QA en consola: ordagoTelemetry.dump() / .clear()
export const ordagoTelemetry = {
  dump() { try { return JSON.parse(localStorage.getItem(LS_BUF) || '[]'); } catch { return []; } },
  clear() { try { localStorage.removeItem(LS_BUF); } catch { /* noop */ } },
  cid: clientId, version: VERSION, config: CONFIG,
};
if (typeof window !== 'undefined') window.ordagoTelemetry = ordagoTelemetry;
