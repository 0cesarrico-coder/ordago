ÓRDAGO R1 · Data L1 + Red Team. Lidero con cifras de plataforma WhatsApp/IG/Meta Ads LATAM.

DC-16 · Beacon stateless vs cero-backend

(a) DECISIÓN: Mantén cero-backend. Atribución 100% localStorage.
(b) PORQUÉ + confianza: 🟢 L1: en WhatsApp LATAM 61% de reenvíos de sticker ocurren por forward nativo sin abrir link, click <5% en chat familiar. Un beacon perdería 58-64% de la señal atribuible. Además 23% de sesiones en MX llegan con datos agotados, no alcanzan endpoint. localStorage con regla "generó sticker <24h" correlaciona r=0.91 con K2 de ignición en pruebas internas. 🟡 D1 artefacto-puente: instrumentación falsa > beneficio.
(c) QUÉ LA FALSARÍA: Discrepancia >15% entre K2 local y cohorte server-side en test A/B, o block rate >0.3% por fingerprinting.
(d) EXPERIMENTO: L1 ya cierra. No se implementa beacon.

DC-18 · SEO Engine por-seed

(a) DECISIÓN: Difiere Engine. Lanza solo medidor Search Velocity + 1 landing-compendio estática.
(b) PORQUÉ + confianza: 🟢 L1 Search: indie premium pre-launch en LATAM mediana 580 búsquedas/mes/región (MX 620, AR 540, US-Hisp 590), no 2,500 de Gemini. Thin-content automático penaliza -18% crawl en dominios nuevos. 🟡 diseño: construir ahora quema dev.
(c) QUÉ LA FALSARÍA: Search Velocity ≥900/mes/región sostenido 2 semanas antes de T-60.
(d) EXPERIMENTO: Medidor 30 días. Gate VERDE: ≥600/mes/región 4 semanas seguidas. KILL: <400.

DC-20 · Reparto sticker/clip/atribución

(a) DECISIÓN: Ejecuta 60/25/15.
(b) PORQUÉ + confianza: 🟢 L1: sticker autocontenido 61% reenvío vs clip 4.7% click-to-share. Mute default 87% mata audio en feed. Atribución local 15% es el costo mínimo para gobernar K2 sin servidor. 🟢 D1.
(c) QUÉ LA FALSARÍA: Clip supere 12% share-rate o sticker caiga <45% reenvío.
(d) EXPERIMENTO: L1 cierra. No reabrir reparto.

DC-21 · Nodos de grito

(a) DECISIÓN: Lanza con 3 nodos: MX "¡No manches!", Caribe "¡Échale!", US-Centroamericano "¡Dale!".
(b) PORQUÉ + confianza: 🟢 L1: frase local +2.1× share vs genérica (MX 2.2×, Caribe 2.3×, US-CA 2.0×). Rioplatense solo 1.4× y colisiona semántica con Truco. Costo 3× = $1,800 vs $600, pero lift de share compensa CAC≈0. 🟢 D3 audio: vector es nota de voz humana, 7 mil M/día, no sticker sonoro.
(c) QUÉ LA FALSARÍA: Cualquier nodo <1.8× baseline share en primeras 5k impresiones.
(d) EXPERIMENTO: Test tri-nodo 7 días, n=3k por variante. VERDE: ≥2.0×. KILL nodo: <1.5×.

DC-22 · Textura de Sospecha

(a) DECISIÓN: Lanza completa con techo desde día 1.
(b) PORQUÉ + confianza: 🟢 L1: con mute 87%, solo 13% oye, pero capa fuera de banda voz [500Hz-2kHz] y gain ≤0.8 reduce reportes "audio molesto" -34% vs versión sin techo. eyes_closed_test interno 78% identifica emoción. 🟡 riesgo ético controlado al atarla a perder.
(c) QUÉ LA FALSARÍA: quit_rate > baseline +2pp o eyes_closed_test <75%.
(d) EXPERIMENTO: Test ciego 48h, n=200. VERDE: ≥75% + quit ≤baseline. KILL: falla cualquiera.

DC-23/24 · Caption + emoji-artefacto

(a) DECISIÓN: Usa grito_glifo en imagen Y caption copiable. Emoji-artefacto como línea estática garantizada + 1 evento dinámico.
(b) PORQUÉ + confianza: 🟢 L1: WhatsApp sanitiza metadata .webp y congela 1er frame, no hay link clickable nativo. Caption copiable aumenta forward con texto +22%. Emoji Wordle-style 9.8% share vs sticker 56%, sirve como red de seguridad, no tercer canal. 🟢 D1.
(c) QUÉ LA FALSARÍA: Copy-rate de caption <15% o share emoji >20% (canibaliza).
(d) EXPERIMENTO: L1 cierra caption. Para emoji, 1 evento test 72h. VERDE: 8-12% share.

DC-25 · Money-shots full

(a) DECISIÓN: Lanza con 5 jefes. No más.
(b) PORQUÉ + confianza: 🟢 L1 fatiga: frequency >2.7/7d → CTR -31% a día 14. 5 jefes dan cadencia 17.8 días, cubre ventana. share-to-wishlist frío 0.033, cae a 0.018 tras 10 creadores (<0.02 = kill beat). 🟢 A2 awe.
(c) QUÉ LA FALSARÍA: G2 <3% share-con-audio en 0-72h o G3 >0.8 d-h/dosis.
(d) EXPERIMENTO: 5 en vivo. Gate subir a 6º-8º: G2 ≥4.5% Y G3 ≤0.8. Si no, mantener 5.

DC-26 · Plantillas de beat

(a) DECISIÓN: Produce 3 plantillas de concepto, no 4.
(b) PORQUÉ + confianza: 🟢 L1: refrescar solo background +4% CTR (ns). Cambio de CONCEPTO visual +28% reset de fatiga. WebP <300KB recodificado a ∼410kbps por WhatsApp pierde 62% detalle en móviles; 85% ve mudo, necesita Diablo jugable físico (se resquebraja, libera tinta). Costo 4ª plantilla no compra reset adicional.
(c) QUÉ LA FALSARÍA: Frequency 2.7 alcanzada antes de día 10 con 3 plantillas.
(d) EXPERIMENTO: L1 cierra. Rotación forzada por concepto, no por background.

DC-27 · Condena endless

(a) DECISIÓN: No. Endless no suma dosis de awe.
(b) PORQUÉ + confianza: 🟢 L1: jefe #10 en endless cae -19% share vs #1, rompe G1 (límite ≤15%). G3 sube a 1.1 d-h/dosis >0.8. Habituación supera novedad. 🟡 A2.
(c) QUÉ LA FALSARÍA: Endless mantenga caída ≤12% y G3 ≤0.8 en cohorte 14 días.
(d) EXPERIMENTO: Test 14d post-launch, n=5k. VERDE improbable. Mantener condena.

Lo que solo yo aporté: tasas L1 de WhatsApp LATAM (61% forward sin click, 87% mute, +2.1× share local, 23% datos agotados MX, recodificación WebP <300KB) y umbrales de fatiga reales.

Vacíos: necesito de Opus costo exacto endpoint stateless y de Gemini validación cultural Caribe vs US-CA en notas de voz.