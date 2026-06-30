# ÓRDAGO v1.2 — Matriz de consenso (todos los fixes del debate multi-IA)

> Clasificación: **Consenso 3/3** · **Mayoría 2/3** · **Contestado** (ambos lados) · **Único** (1 IA, sin objeción). Atribución y confianza: 🟢 literatura verificada · 🟡 canónico/señal/L1 plataforma direccional · ⚪ razonamiento. Evidencia: L1 plataforma > L2 industria > L3 entrenamiento > L4 razonamiento. Referee R3: `contested=1 flipped=2 consensus=8 total=9` (CONVERGING). NO se asciende 🟡→🟢. NO se inventa consenso donde el referee marcó contestado.

---

## PALANCA 1 — Artefacto-puente (§8.3 nuevo)

| # | Fix | Clasificación | Quién lo sostiene | Conf / Evidencia |
|---|---|---|---|---|
| 1.1 | Artefacto DUAL desde UNA fuente serializada (`RunDigest`): objeto de grafo + clip de feed | **Consenso 3/3** | Opus + Gemini + Meta (estable desde R1) | 🟡 (estructura L4 / formato L1) |
| 1.2 | El deep-link aterriza en algo JUGABLE, no en tienda/paywall | **Consenso 3/3** | Opus + Gemini + Meta (Meta flipó en R2) | 🟢 (L4 + física de plataforma L1) |
| 1.3 | Formato del objeto que cruza = IMAGEN-sticker PNG/WebP <80KB en cliente (texto = fallback) | **Consenso 3/3** (era Contestado R1-R2; flip de Opus en R3) | Meta (lidera, L1) + Gemini + Opus (cedió) | 🟡 (L1 stickers 56% vs 12%, direccional) |
| 1.4 | Línea-verbo-nominal "Le robé el alma a @primo por +X%" como gancho social en 1ª posición | **Consenso 3/3** | Opus (R1) + Gemini + Meta | 🟡 (LD6 dominancia/reciprocidad) |
| 1.5 | Deep-link COMPONE K (receptor juega→genera su sticker→reenvía), no solo cruza | **Único** (defendido, no objetado; pendiente de A/B) | Opus 🟢 (Meta/Gemini priorizan "se entiende en 0.5s") | ⚪ (L4; crux a falsar) |
| 1.6 | Clip 6-8s CON AUDIO por defecto (firma sonora = foso barato D3) | **Consenso 3/3** | Gemini + Meta (L1 Reels 2-12×) + Opus | 🟡 (L1 alcance) |
| 1.7 | Clip NO se codifica en cliente móvil → render server-side/PC, móvil sirve asset pre-renderizado | **Consenso 3/3** (era Contestado R2 "móvil vs PC"; disuelto R3) | Opus (separar generar de codificar) + Gemini (PC genera) + Meta (pre-render) | 🟢 (L1 hardware LATAM dura) |
| 1.8 | Generador procedural de variantes (≈12 clips/20 grids) anti-fatiga, como invariante vivo | **Consenso 3/3** (Opus flipó en R2) | Meta (L1 fatiga 2-3 sem) + Gemini (plantillas) + Opus | 🟡 (L1 vida media) |
| 1.9 | Texto 100% editable, centrado en rivalidad personal, no en marca (anti-reactancia) | **Consenso 3/3** | Gemini (R1, A3) + Opus + Meta | 🟡 (A3) |
| 1.10 | Anti-spoiler: grid muestra resultado, link solo re-inicializa el seed determinista | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (C3) |
| 1.11 | Doble criterio de kill: comprensión <2s ≥70% Y disposición-a-reenviar ≥30% | **Consenso 3/3** (Opus flipó en R2; corregido por Meta) | Meta (L1) + Opus (cedió su test de R1) + Gemini | 🟡 (L1 reactancia) |
| 1.12 | Degradar "código de build" alfanumérico a opt-in ~5% en el Codex | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (A4) |
| 1.13 | KPI objetivo K_grafo WhatsApp >0.3 MX / >0.2 hispanos-USA | **Mayoría 2/3** | Meta + Opus (Gemini no fija el número) | ⚪ (L4 objetivo; validar) |

---

## PALANCA 2 — Generador de bifurcación + foso vivo (§7.3, §14, §18)

| # | Fix | Clasificación | Quién lo sostiene | Conf / Evidencia |
|---|---|---|---|---|
| 2.1 | Generador como INVARIANTE verificado por solver ANTES de un píxel (no kill-test a posteriori) | **Consenso 3/3** (estable desde R1) | Opus (lidera) + Gemini + Meta | 🟢 (A1) |
| 2.2 | Postcondición: ≥2 jugadas Pareto-no-dominadas tras cada siembra | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (A1) |
| 2.3 | Reformular la decisión: de "¿cuál suma 15?" a "¿qué futuro capturo?" (tempo/escala/defensa) | **Consenso 3/3** | Opus (lidera) + Gemini (tempo/escala) + Meta (3 rutas) | 🟢 (A1) / ⚪ (que ESTE eje lo produzca; validar con solver) |
| 2.4 | Siembra determinista por seed (misma semilla → misma siembra) | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (requisito de falsabilidad) |
| 2.5 | Re-siembra acotada (≤8 intentos) operando sobre EJES, no cartas concretas | **Mayoría 2/3** (Opus explícito; Gemini "regenera"; Meta "máx 8") | Opus + Meta (≤8) ; Gemini sin tope numérico | ⚪ (L4) |
| 2.6 | **Banda de spread de EV que define "decisión real"** | **CONTESTADO** | **Banda DUAL: Opus + Meta** (re-siembra >20-25%, foso ≤15%) **vs Banda ÚNICA: Gemini** ([15-20%], piso 15%) | ⚪ (número; método 🟢) |
| 2.7 | Carnada/Bloqueo (§7.3 existente) subordinados como herramientas del generador | **Único** (Opus; no objetado) | Opus | 🟡 (A1) |
| 2.8 | Foso vivo: entropía de Shannon de builds ganadores semanal (alarma si cae) | **Consenso 3/3** | Opus + Gemini + Meta (difieren solo el umbral) | 🟡 (A1; umbral exacto ⚪) |
| 2.9 | Respuesta a dominancia = matar con TRADE-OFF, no nerf de número | **Mayoría 2/3** (Opus explícito; Gemini "ajustar pesos de Sospecha") | Opus + Meta ; Gemini variante | 🟢 (A1) |
| 2.10 | Test del experto = techo de maestría (mismo seed novato vs experto) | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (A1) |
| 2.11 | Proxy gratis del test del experto vía Diablo Fantasma (curva de skill en producción) | **Único** (Opus; no objetado) | Opus | 🟢 (A1, LD6) |
| 2.12 | Solver de papel sobre 100 tableros como kill-test más barato del proyecto | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (método) |
| 2.13 | Crux-cimiento: si el verbo es puzzle aritmético (>20% tableros convergen) → pivotar de género | **Consenso 3/3** (el que se resuelve PRIMERO) | Opus (Riesgo C honesto) + Gemini + Meta | 🟢 (A1) |

---

## PALANCA 3 — Plataforma ↔ viralidad ↔ economía (§16.1)

| # | Fix | Clasificación | Quién lo sostiene | Conf / Evidencia |
|---|---|---|---|---|
| 3.1 | Separar loop ADQUISICIÓN (CAC>0) de loop SOCIAL/retención (CAC~0) | **Consenso 3/3** (estable desde R1) | Opus (lidera) + Gemini + Meta | 🟢 (L3, L7) |
| 3.2 | Borrar "CAC~0" del lenguaje de adquisición (corrección editorial) | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (L3) |
| 3.3 | El artefacto-puente (P1) ES parte del modelo económico, no un canal aparte | **Único** (Opus; no objetado, alineado con todos) | Opus | 🟢 (L3) |
| 3.4 | Modelo B2P de 3 columnas (USA / hispanos-USA / LATAM) | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (modelo) / ⚪ (cifras) |
| 3.5 | Gate duro LTV/CAC ≥ 3 por columna antes del vertical slice | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (modelo) / ⚪ (ratios exactos) |
| 3.6 | Precio LATAM ~$7.49 (149 MXN), NO $15 | **Consenso 3/3** (Meta flipó en R2 tras ataque de Gemini con data Balatro/Inscryption) | Gemini (lidera, L1) + Meta + Opus | 🟡 (L1 elasticidad) |
| 3.7 | Precio USA/hispanos-USA = $14.99 | **Mayoría 2/3 → 3/3 en R3** (Gemini R1 proponía $19.99/$17.99, convergió a $14.99) | Opus + Meta (R1) + Gemini (R3) | 🟡 (L2) |
| 3.8 | Cifras exactas de CAC/LTV/conversión de las tablas NO son consenso (ilustración, no hecho) | **Contestado en niveles** (modelo consensuado, números divergen) | Gemini (2.84/4.87/10.80) vs Meta (18/15/12%) vs Opus (rangos) | ⚪ (validar en cohorte propia) |
| 3.9 | Leaderboards en backend propio (no solo Steamworks) desde el prototipo | **Consenso 3/3** (Opus origina; los tres alinean) | Opus (L7) + Gemini + Meta | 🟢 (L7) |
| 3.10 | Clip degradado a feature exclusiva de PC (sin móvil) | **REFUTADO/superado** (Gemini R2) | propuesto por Gemini R2 → reemplazado por 1.7 (render server-side) en R3 | — |
| 3.11 | Embudo: WhatsApp móvil → demo web → captura email → wishlist/compra Steam PC | **Consenso 3/3** | Gemini (lidera) + Opus + Meta | 🟡 (L1 fricción móvil→PC) |

---

## DECISIÓN C-1 — Plataforma

| # | Fix | Clasificación | Quién lo sostiene | Conf / Evidencia |
|---|---|---|---|---|
| C1.1 | Modelo HÍBRIDO (Steam premium + demo web jugable de 1 mano) | **Consenso 3/3 + 2 referees** (total, nunca contestado) | Opus + Gemini + Meta + referee R2 + referee R3 | 🟢 |
| C1.2 | La demo web NO es marketing — es la primera mitad física del artefacto-puente | **Consenso 3/3** (Opus origina; los tres adoptan) | Opus + Gemini + Meta | 🟢 |
| C1.3 | Steam = producto premium $14.99, regional LATAM, protege linaje Balatro/sin-MTX | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (M1/LD7) |
| C1.4 | Demo deliberadamente delgada (1 mano/manga, sin meta): regala el verbo, cobra el foso | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 |
| C1.5 | Rechazar web-native-full-first (mata premium, invita piratería, desliza a F2P/MTX) | **Consenso 3/3** | Opus + Gemini + Meta | 🟢 (M1/LD7) |
| C1.6 | Trade-off aceptado: ~+15% scope (2 builds + render-worker + backend), costo servidor ≠0, piratería parcial demo, ~25% pérdida conversión LATAM | **Consenso 3/3** | Opus + Gemini + Meta | ⚪ (estimaciones de scope) |
| C1.7 | Mitigar pérdida LATAM con captura de email → pre-registro de port nativo móvil año 2 | **Mayoría 2/3** | Gemini + Meta ; Opus no lo menciona | ⚪ (L4) |

---

## Las apuestas falsables de cada asiento (lo que cada IA pondría como condición #1 del #1)

| Asiento | Apuesta falsable |
|---|---|
| **Opus** | ÓRDAGO no llega al #1 si el GENERADOR no se construye como INVARIANTE verificado por solver (≥2 Pareto-no-dominadas, spread dual ≤15%) ANTES de un píxel — todo lo demás descansa en que el verbo sea decisión, no puzzle. |
| **Gemini** | No supera 50,000 uds en 3 meses si el precio LATAM > $9.99 y la demo web no carga el reto de WhatsApp en < 2.0 s en red estándar. |
| **Meta AI** | No llega al #1 si el artefacto-puente no genera K-factor > 0.3 en grupos familiares MX sin pagar un centavo en ads. |

> **Convergencia de las tres apuestas:** las tres apuntan a la ENTREGA (no a la idea) y a un test barato y temprano — el solver (Opus), la latencia/precio de la demo (Gemini) y el K-factor del artefacto (Meta). Ninguna es una frase: las tres se corren con baraja+hoja de cálculo o un A/B de shares antes del vertical slice.
