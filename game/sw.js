// ÓRDAGO — service worker. Estrategia: stale-while-revalidate del shell del juego.
// Objetivo: cargas repetidas instantáneas (retención) + jugable offline. Sin sorpresas: la versión
// del caché se ata a VERSION del juego, así un release nuevo invalida el caché viejo limpiamente.
const VERSION = '0.6.0';
const CACHE = 'ordago-' + VERSION;
const SHELL = [
  './', './index.html', './style.css',
  './src/main.js', './src/game.js', './src/engine.js', './src/content.js',
  './src/fx.js', './src/audio.js', './src/telemetry.js',
  './manifest.webmanifest',
  './assets/diablo.png', './assets/papel.png',
  './assets/icon-192.png', './assets/icon-512.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  // No interceptar la telemetría ni terceros (GA): déjalos ir directo a la red.
  if (url.origin !== self.location.origin) return;
  e.respondWith(
    caches.match(req).then((cached) => {
      const net = fetch(req).then((res) => {
        if (res && res.status === 200) {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy));
        }
        return res;
      }).catch(() => cached);     // offline: usa el caché
      return cached || net;        // instantáneo si está cacheado, revalida en segundo plano
    })
  );
});
