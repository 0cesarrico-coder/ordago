# Consensus Matrix — Fixes de ÓRDAGO v1.2 (clasificación + quién sostiene)

> Clasificación por fix: **Consenso 3/3** · **Mayoría 2/3** · **Contestado** (ambos lados) · **Único**. Atribución nominal + confianza 🟢/🟡/⚪ y nivel de evidencia (L1 plataforma > L2 industria > L3 entrenamiento > L4 razonamiento). No se asciende 🟡→🟢. La banda de EV permanece **Contestado** (correcto por contrato). iter-1: añade explícitas las 2 instancias que el bias-audit marcó (peso Profeco de Meta; WebP <300 KB de Gemini/Meta) con su atribución y evidencia.

---

## A. PALANCA 1 — Artefacto-puente

| # | Fix | Clasificación | Quién lo sostiene | Conf / evidencia |
|---|---|---|---|---|
| 1.1 | Sistema dual desde UNA fuente serializada (`RunDigest`): un objeto que cruza el grafo + un clip que enciende el feed | **Consenso 3/3** | Opus (arquitectura, lidera) + Gemini + Meta | 🟢 / L4 sistemas |
| 1.2 | Formato del objeto-puente = imagen-sticker PRIMARIA (PNG/WebP <80KB en cliente), texto = fallback | **Consenso (flip de Opus R3)** — era Contestado R2 | Meta (data stickers, lidera) + Gemini, Opus concedió ("perdí el formato, no el principio") | 🟡 / L1 plataforma (stickers 56%/52% vs 12%; WhatsApp 12.4%) |
| 1.3 | **El peso de la imagen NO añade fricción: Profeco mide ~1 MB texto ≈ ~1 MB imagen en WhatsApp** → la imagen-sticker es canónica, texto = fallback feature phones | **Único (Meta AI)** — dato que neutraliza la objeción de ingeniería; no contradicho por nadie | **Meta AI** (dato de plataforma Profeco) | 🟡 / **L1 plataforma** (validar render <80KB en dispositivos de cohorte) |
| 1.4 | Clip 6-8s CON AUDIO (firma sonora) como co-primario en alcance; Reels 2-12× vs posts, carruseles +25.71% | **Consenso 3/3** (importancia del clip) | Meta (data alcance, lidera) + Opus + Gemini | 🟡 / L1 plataforma |
| 1.5 | Deep-link jugable `ordago.gg/d/<seed>` embebido en caption de ambos objetos (compone K = i × c) | **Mayoría → Consenso** (Opus 🟢 no cedió; Gemini/Meta lo integran vía caption) | Opus (lidera) + física de plataforma de Gemini (stickers no admiten hipervínculos → imagen + caption con link) | 🟢 (principio) / 🟡 (física plataforma, Gemini L1) |
| 1.6 | Arquitectura ASIMÉTRICA por plataforma: móvil NO codifica video (FFmpeg.wasm "choke main thread / exhaust heap"); 87% gamers LATAM en smartphone gama media-baja | **Consenso 3/3** (disuelve el crux clip-móvil) | Gemini + Meta (data hardware L1) + Opus (separar GENERAR de CODIFICAR) | 🟢 (mecanismo) / 🟡 (data hardware L1) |
| 1.7 | **Clip broadcast PC = MP4 ultra-comprimido <500 KB con audio reactivo** (para TikTok/Reels) | **Consenso 3/3** (cifra convergente) | Opus + Gemini + Meta | 🟡 / L1+L4 |
| 1.8 | **Asset móvil pre-renderizado = WebP animado en bucle <300 KB** (distinto y más exigente que el MP4 <500KB de PC); o imagen estática del Objeto A + animación CSS. El móvil recibe y reenvía, no codifica | **Mayoría 2/3 (Gemini cifra, Meta corrobora)** — Opus no fija cifra móvil propia, concede vía "separar generar de codificar" | **Gemini** ("Genera un WebP animado en bucle (<300 KB)") **+ Meta** ("asset pre-renderizado, WebP animado <300KB") | 🟡 / **L1 plataforma** (validar en cohorte; cada KB pesa más en redes gama baja) |
| 1.9 | Anti-spoiler: grid muestra RESULTADO, link solo re-inicializa el seed determinista (reto compartido, no spoiler) | **Consenso 3/3** | Opus + Gemini + Meta (kill de Meta: si se reconstruye la run desde el grid → matar) | 🟢 / L4 |
| 1.10 | Anti-fatiga: generador procedural de variantes (~12 clips / 20 grids + copy de rivalidad editable); stickers se queman en 2-3 sem | **Consenso 3/3** (Opus flipó en R2 y lo adoptó como invariante) | Meta (vida media 2-3 sem, L1) + Gemini (copy de rivalidad anti-reactancia A3) + Opus | 🟡 / L1 plataforma |
| 1.11 | Degradar "código de build" alfanumérico a opt-in ~5% en el Codex (A4) | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 / L4 |

---

## B. PALANCA 2 — Generador de bifurcación + foso vivo

| # | Fix | Clasificación | Quién lo sostiene | Conf / evidencia |
|---|---|---|---|---|
| 2.1 | Generador = INVARIANTE verificado por solver ANTES de un píxel (no kill-test a posteriori); reformular "¿cuál suma 15?" → "¿qué futuro capturo?" en ejes tempo/escala/defensa | **Consenso 3/3** | Opus (lidera) + Gemini + Meta | 🟢 / L4 (carta A1 🟢) |
| 2.2 | Regla de siembra dura: ≥2 jugadas Pareto-no-dominadas, siembra determinista por seed, re-siembra acotada ≤8 sobre ejes; Carnada/Bloqueo subordinados al generador | **Consenso 3/3** (mecanismo) | Opus + Gemini + Meta | 🟢 / L4 |
| 2.3 | **Banda de spread de EV** | **CONTESTADO** (único vivo, referee R3 `contested=1`) | **Banda DUAL: Opus + Meta (2/3)** (foso medido ≤15%, re-siembra >25% Opus / >20% Meta) **vs Banda ÚNICA: Gemini (1/3)** [15%, 20%] con piso 15% ("ajedrez seco" <10%, "trampa de novato" >20%) | ⚪ (número) — Opus/Meta L4 diseño de info; Gemini L4 + psicología consumidor LATAM (Truco/Escoba, "tensión de la codicia") |
| 2.4 | Cómo se zanja la banda: solver de papel sobre 100 tableros + test del experto (novato↔experto, mismo seed/build) | **Consenso de método 3/3** | Opus + Gemini + Meta | 🟢 / L4 |
| 2.5 | Centinela 1: entropía de Shannon de builds ganadores por cohorte semanal; alarma = caída sostenida (>15% Meta / <2.0-2.2 bits Gemini); respuesta = trade-off, NO nerf de número | **Consenso 3/3** (mecanismo); umbral exacto ⚪ | Opus (respuesta = trade-off) + Meta (>15%) + Gemini (<2.2 bits) | 🟡 (umbral ⚪) / L1-L4 |
| 2.6 | Centinela 2: test del experto = techo de maestría, proxy gratis vía Diablo Fantasma (margen vs percentil = curva de skill) | **Consenso 3/3** | Opus (proxy Diablo Fantasma, clave) + Gemini + Meta | 🟢 / L4 |

---

## C. PALANCA 3 — Plataforma ↔ viralidad ↔ economía

| # | Fix | Clasificación | Quién lo sostiene | Conf / evidencia |
|---|---|---|---|---|
| 3.1 | Separar loop ADQUISICIÓN (CAC>0 siempre) de loop SOCIAL/retención (CAC~0 real); borrar "CAC~0" del lenguaje de adquisición | **Consenso 3/3** | Opus (lidera, L3/L7) + Gemini + Meta | 🟢 (modelo) / L3 unit-economics |
| 3.2 | Embudo segmentado: WhatsApp/móvil → demo web 1 manga (fricción cero) → email → wishlist/compra Steam | **Consenso 3/3** | Gemini (embudo concreto) + Opus + Meta | 🟢 / L4 |
| 3.3 | Modelo B2P de 3 columnas (USA / hispanos-USA / LATAM) con gate duro LTV/CAC ≥ 3 por columna antes del vertical slice | **Consenso 3/3** (modelo) — cifras ⚪/🟡 | Opus + Gemini (proyecta ~4-5) + Meta | 🟢 (modelo) / ⚪ (ratios) |
| 3.4 | Precio LATAM ~$7.49 (149 MXN), no $15 (Balatro $7.50 / Inscryption $9; $15 en LATAM = suicidio comercial) | **Consenso 3/3** (Meta flipó R2 ante data de Gemini) | Gemini (lidera, elasticidad L1) + Opus + Meta | 🟡 / L1 elasticidad regional |
| 3.5 | Cifras de CAC/LTV/conversión por columna NO son consenso (Gemini 2.84/4.87/10.80 y objetivo ≥4; Meta 18/15/12%) — ilustrativas, validar en cohorte | **Único por IA, NO-consenso explícito** | cada IA con su tabla; el árbitro las marca como ilustrativas | ⚪ / L2-L4 |
| 3.6 | Leaderboards en BACKEND PROPIO (no solo Steamworks) desde el prototipo — desacopla el foso social de la plataforma de venta | **Consenso 3/3** | Opus (riesgo doble dependencia, L7) + Gemini + Meta | 🟢 / L7 |

---

## D. DECISIÓN C-1 (plataforma)

| # | Fix | Clasificación | Quién lo sostiene | Conf / evidencia |
|---|---|---|---|---|
| 4.1 | Modelo HÍBRIDO: Steam premium + demo web jugable ultraligera (<10MB, <2-3s en 4G) = primera mitad física del artefacto-puente | **Consenso unánime 4 votos** (3 IAs + 2 referees); nunca contestado | Opus + Gemini + Meta + referees | 🟢 / M1/LD7 |
| 4.2 | Trade-off aceptado: ~+15% scope, costo de servidor >0, piratería parcial de demo, ~25% pérdida de conversión móvil-sin-PC LATAM (mitigada con email→port móvil año 2) | **Consenso 3/3** (estimaciones ⚪) | Gemini + Meta (cifras) + Opus | ⚪ / L4 |
| 4.3 | RECHAZADO: web-native-full-first (mata premium, invita piratería, desliza a F2P/MTX → choca con piso ético M1/LD7) | **Consenso 3/3 (rechazo)** | Opus + Gemini + Meta | 🟢 / M1/LD7 |

---

## E. Resumen de clasificación

| Clasificación | Conteo | Ejemplos |
|---|---|---|
| **Consenso 3/3 (o 4 votos)** | mayoría de los fixes | arquitectura dual, invariante por solver, separar loops, gate LTV/CAC≥3, precio LATAM, backend propio, híbrido |
| **Mayoría 2/3** | 1.5 (deep-link), 1.8 (WebP <300KB Gemini/Meta) | imagen + caption con link; asset móvil <300KB |
| **Contestado** | **1** (banda de EV) | DUAL (Opus+Meta) vs ÚNICA (Gemini) — se zanja con solver + test del experto |
| **Único (atribuido, no contradicho)** | 1.3 (peso Profeco, Meta), 3.5 (tablas por IA marcadas ilustrativas) | dato de plataforma Profeco de Meta; cifras especulativas de cada IA |

**Banda de EV = el ÚNICO contestado vivo. Cero consenso fabricado. Las dos minimizaciones del bias-audit (1.3 peso Profeco de Meta; 1.8 WebP <300KB de Gemini/Meta) quedan con atribución, evidencia L1 y desarrollo equivalente a los hallazgos de Opus de nivel comparable.**
