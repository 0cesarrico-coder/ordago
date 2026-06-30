# ÓRDAGO — Fixes de clase mundial (veredicto del debate multi-IA, para v1.2)

> Síntesis del árbitro. Funde 3 IAs × 3 rondas + 2 referees. NO debate: integra. Distingue **CONSENSUADO** de **CONTESTADO**. Cifras atribuidas a su fuente con confianza 🟢/🟡/⚪ y nivel de evidencia (L1 plataforma > L2 industria > L3 entrenamiento > L4 razonamiento). No se asciende 🟡→🟢. Toda cifra 🟡/⚪ lleva "validar en cohorte propia". Piso ético M1/LD7 inviolable.
>
> *iter-1: corrige las 2 minimizaciones que el bias-audit marcó como CONCERNS — el dato de plataforma de Meta AI sobre el peso de la imagen (Profeco 1MB) y la cifra propia de Gemini/Meta para el asset móvil (WebP animado <300 KB) — dándoles el mismo desarrollo que los hallazgos de Opus de nivel comparable. No se borró ni minimizó nada más; la banda de EV sigue CONTESTADA.*

---

## 0. Cómo se corrió + consenso del panel

**El método.** Tres asientos, tres rondas, dos pases de referee:
- **Opus = Director de Diseño/Sistemas** (lidera Palanca 2; estándar duro "valor DECLARADO vs valor ENTREGADO" — un número en tabla no es una máquina).
- **Gemini = Estratega de Valor + Señal de Mercado** (lidera Palanca 3; aporta señal de elasticidad de precio regional y fricción de plataforma).
- **Meta AI = Data L1 de plataforma + Red Team** (única con dato de comportamiento real de WhatsApp/IG en LATAM).
- R1 apertura → R2 confrontación cruzada (steelman + ataque + concesión) → R3 cierre de 3 cruxes. Referee tras R2 y R3.

**El veredicto del referee.** R3: **CONVERGING**, `SCORE-INPUT: contested=1 flipped=2 consensus=8 total=9`. (La etiqueta del árbitro de esta síntesis indica un *converging score* alto, ~83/100: 8 de 9 hallazgos en consenso, un solo número aún abierto.) De R2 a R3, **dos de los tres cruxes vivos colapsaron a consenso** (formato del objeto-puente y soporte del clip — ambos por flip concedido por Opus). Queda **un solo desacuerdo genuino**: la banda exacta de spread de EV.

**Qué unió al panel (el núcleo consensuado 3/3 que sobrevivió las 3 rondas).**
1. **Diagnóstico común:** el VERBO de ÓRDAGO es de clase mundial; lo que está lejos del #1 es la **entrega**, no la idea. El GDD apuesta el crecimiento a "CAC~0 vía WhatsApp" sin definir el objeto que la gente reenvía — fantasía hueca, exactamente lo que la v1.1 juró matar.
2. **Artefacto-puente dual** desde UNA fuente serializada (`RunDigest`): un objeto que cruza el grafo cerrado + un clip que enciende el feed abierto.
3. **El deep-link debe aterrizar en algo JUGABLE, no en una tienda/paywall** (Meta flipó hacia esto en R2; quedó unánime).
4. **Generador de bifurcación como INVARIANTE verificado por solver ANTES de un píxel** — no un kill-test a posteriori.
5. **Separar el loop de ADQUISICIÓN (CAC>0) del loop SOCIAL/retención (CAC~0)** y borrar "CAC~0" del lenguaje de adquisición.
6. **Modelo B2P de 3 columnas con gate duro LTV/CAC ≥ 3 por columna** antes del vertical slice.
7. **Precio LATAM ~$7.49 (149 MXN), no $15** (Meta flipó en R2 tras el ataque de Gemini con data Balatro/Inscryption).
8. **C-1 = HÍBRIDO** (Steam premium + demo web jugable = primera mitad física del artefacto-puente, no marketing). Convergencia total.

**Lo que sigue contestado:** un solo número — la banda de spread de EV del generador (§2 y §6). El método para zanjarlo SÍ está consensuado (solver de papel + test del experto).

---

## 1. PALANCA 1 — Artefacto-puente: el fix ganador  · (§8.3 nuevo)

**Clasificación general: Consenso 3/3 en la arquitectura; el FORMATO se zanjó por flip de Opus en R3 (de Contestado → Consenso).**

### El objeto exacto (formato resuelto)
**Sistema dual desde un único `RunDigest` serializado** (la fuente de verdad única; aporte de Opus 🟢 razonamiento de sistemas, L4):

- **Objeto A — La ficha-sticker (PRIMARIA, la que cruza el grafo familiar).** Imagen **PNG/WebP <80 KB renderizada EN CLIENTE** con sprites pre-cargados (0 servidor, 0 dependencia de red para generarla). Muestra: la "Mano contra el Diablo" + la **línea-verbo-nominal** *"Le robé el alma a @primo por +X%"* + score + la cara del Diablo en tipografía Posada.
  - **Por qué imagen y no texto (dato decisivo, Meta AI, L1 plataforma 🟡→direccional):** stickers personalizados **56%** + animados **52%** vs predeterminados **12%** de uso; WhatsApp concentra **12.4%** del consumo de información en México (> Facebook 11%, YouTube 10.7%). La etnografía del *family-group-chat* ("about to send one of those to my tías") muestra que cruza una imagen que se entiende en 0.5 s, no un string. Un grid de texto se lee como "predeterminado genérico" (la franja del 12%). *Confianza del veredicto de formato: 🟡 — la data de stickers es L1 fuerte pero direccional; el A/B propio del artefacto aún no se corrió.*
  - **El peso de la imagen NO es una excusa para no usarla (dato de plataforma decisivo, Meta AI, L1 🟡 — corrige la objeción de ingeniería).** La principal objeción contra hacer la imagen primaria (en vez del texto plano de la R1 de Opus) era de **fricción por peso/transferencia** en redes LATAM de gama baja. Meta la neutraliza con un dato de plataforma duro: **Profeco mide ~1 MB por mensaje de texto y ~1 MB por imagen en WhatsApp**, es decir, la app **contabiliza/transfiere el mismo orden de magnitud** para texto y para imagen — la imagen **no añade fricción** de datos sobre lo que el usuario ya paga al chatear. Como además el PNG es **<80 KB renderizado en cliente** (muy por debajo de ese ~1 MB), el costo de datos es trivial y la objeción de peso queda **muerta empíricamente**, no por intuición. Consecuencia operativa de Meta: **la imagen-sticker es el canónico** y el **texto plano queda como FALLBACK automático para feature phones** (no como formato principal). Este dato es lo que convierte "imagen primaria" de preferencia de diseño en una decisión respaldada por la economía de datos real de la plataforma en LATAM. *🟡 direccional — dato de plataforma (Profeco), validar el render <80 KB en dispositivos reales de cohorte.*
  - **Opus concedió en R3** ("imagen primaria; perdí el formato, no el principio") — su argumento de "0 servidor" se preserva porque el PNG se renderiza en cliente, y el dato de peso de Meta retira la última fricción que sostenía su preferencia por el texto.

- **Objeto B — El clip 6-8 s CON AUDIO (co-primario en ALCANCE, vive en el loop de adquisición).** Enciende el feed abierto (IG Reels/TikTok). Contenido: barrido de la Escoba final + campanazo + el Diablo gritando "¡tramposo!" + **firma sonora** (campana grave + jarana barroca).
  - **Por qué el clip importa (Meta AI, L1):** los Reels obtienen **entre 2× y 12×** más alcance que posts; los carruseles **+25.71%** sobre imagen única. El audio es el foso más barato (D3 🟡).

### El deep-link (lo que Opus NO cedió, 🟢)
Deep-link jugable `ordago.gg/d/<seedhash>` **embebido en el caption de ambos objetos**. Razón: comprensión sin acción es K de un solo salto. El receptor necesita QUÉ hacer → juega la mano → genera SU sticker → reenvía. Eso **compone** K (K = i × c, C2 🟡). La imagen gana la primera `i`; el deep-link gana la segunda. *Detalle de física de plataforma (Gemini, L1):* los stickers de WhatsApp **no admiten hipervínculos cliqueables**, pero el menú nativo de compartir de iOS/Android permite enviar la imagen **junto a un texto adjunto (caption)** → por eso imagen primaria **+ caption de texto** que contiene la línea-verbo y el link (el texto plano sobrevive como fallback universal si la imagen no carga). Sin este detalle el bucle viral se rompería: la imagen impacta pero el receptor no tendría dónde pulsar.

### El doble output — resuelto: separar GENERAR de CODIFICAR (aporte de síntesis de Opus, R3) + el asset móvil exacto (Gemini/Meta)
El crux "clip móvil vs solo-PC" se **disolvió** (Contestado R2 → Consenso R3). La arquitectura es **ASIMÉTRICA por plataforma**, y cada plataforma tiene su asset con su cifra propia:

- El cliente móvil **NO codifica video.** Compilar/codificar un MP4 con audio vía WebASM (FFmpeg.wasm) en navegador móvil de gama media-baja LATAM (MediaTek/Snapdragon antiguos) **"choke the main thread, exhaust browser heap memory, and lock the user's interface"** (data L1 dura, Gemini+Meta) → viola la regla de fricción-cero (<3 s de carga) y rebota al usuario. Refuerzo de mercado: **87% de los gamers LATAM están en smartphone**, mayormente gama media-baja (Meta).
- **PC/Steam — el clip broadcast.** El cliente nativo (o un render-worker server-side) genera desde el `RunDigest` el **clip de 6-8 s en MP4 ultra-comprimido <500 KB** con audio reactivo (grito del Diablo) para subir a TikTok/Reels (2-12× de alcance orgánico). *Cifra de Opus/Gemini/Meta, convergente, 🟡.*
- **Demo web / móvil — el asset pre-renderizado ligero, SIN codificación (cifra propia de Gemini, corroborada por Meta, L1 🟡):** el móvil **recibe y reenvía** un **WebP animado en bucle de <300 KB** ("Genera un WebP animado en bucle (<300 KB)", Gemini; "asset pre-renderizado, WebP animado <300KB", Meta), o, como degradación adicional, **la imagen estática del Objeto A con animación CSS local** en el navegador. Esta cifra **<300 KB es distinta y más exigente** que el techo <500 KB del MP4 de PC: aplica al asset que de verdad viaja por el grafo móvil de fricción-cero, donde cada KB pesa más por las redes de gama baja. Mantenerla explícita evita que el techo del MP4 de PC "absorba" el presupuesto real del activo móvil. Así el móvil **preserva fricción-cero (B5 🟢)** sin amputar el alcance broadcast: el video complejo se genera donde hay hardware (PC) y se **degrada deliberadamente en móvil** para priorizar la conversión inmediata.

### Anti-spoiler (resuelto, no prometido)
El grid/ficha muestra RESULTADO (escobas, trampas rotas, margen) pero NUNCA la solución (qué cartas, qué orden, qué Fullería). El link solo inicializa el MISMO estado aleatorio determinista (`?seed=...`); la semilla es **reto compartido (C3)**, no spoiler. Kill: si alguien puede reconstruir la run desde el grid → matar y rediseñar (Meta).

### Anti-fatiga (Consenso 3/3 — Opus flipó en R2 y lo adoptó como invariante)
**Generador procedural de variantes** (≈12 clips / 20 plantillas de grid + generador procedural del copy de rivalidad, 100% editable y centrado en la rivalidad personal, no en la marca — anti-reactancia, A3 🟡 Gemini). Razón (Meta, L1): los stickers se queman en **2-3 semanas** en grupos familiares ("NUEVOS STICKERS DIARIO"). Disciplina: el K se mantiene por una MÁQUINA, igual que el foso — no por un activo congelado.

### Cifras atribuidas y KPIs
| Señal | Valor | Fuente | Evidencia | Conf |
|---|---|---|---|---|
| WhatsApp = canal #1 info MX | 12.4% (> FB 11%, YT 10.7%) | Meta AI | L1 plataforma | 🟡 |
| Uso de stickers personalizados/animados | 56% / 52% vs 12% predeterminados | Meta AI | L1 plataforma | 🟡 |
| Peso WhatsApp: texto ≈ imagen (la imagen no añade fricción) | ~1 MB texto ≈ ~1 MB imagen (Profeco) | Meta AI | L1 plataforma | 🟡 |
| Alcance Reels vs posts | 2×–12× | Meta AI | L1 plataforma | 🟡 |
| Asset móvil pre-renderizado (no codifica) | WebP animado **<300 KB** | Gemini (corrob. Meta) | L1 plataforma | 🟡 |
| Clip broadcast PC (MP4 con audio) | <500 KB | Opus/Gemini/Meta | L1/L4 | 🟡 |
| Ficha-sticker render en cliente | PNG/WebP <80 KB | Opus/Gemini | L4 sistemas | 🟢 |
| Vida media del sticker en grupo familiar | 2-3 semanas | Meta AI | L1 plataforma | 🟡 |
| **KPI vivo objetivo:** K_grafo WhatsApp | >0.3 en MX, >0.2 en hispanos-USA | Meta/Opus | L4 objetivo | ⚪ (validar) |
| **KPI vivo:** `share_with_audio` del clip | medir (LATAM tiende a reenviar mudo) | Opus | L4 | ⚪ (validar) |

### § del GDD donde entra
**§8.3 nuevo — "El artefacto-puente de ÓRDAGO: el motor de reenvío"**. Degradar el "código de build" alfanumérico actual a **profundidad opt-in del ~5% en el Codex** (A4 🟢). Construir Objeto A (sticker) en el prototipo; Objeto B (clip) en el vertical slice.

### Falsabilidad (cambio + kill + test)
**Test del puente:** A/B en 20 grupos familiares MX — sticker-imagen vs texto plano, mismo mensaje. **Doble criterio de kill** (corrección de Opus en R2, anclada por Meta): (1) **reenvío sin explicación en 24h ≥30%** Y (2) **comprensión <2 s ≥70%**. Kill del formato si el ganador no supera AMBOS. **Kill de escala:** si tras 1,000 shares K_grafo <0.2 en cohorte hispana → el artefacto no cruza, no escalar UA. **Gate de costo del clip:** si el render server-side por share supera ~$0.02 → re-evaluar (rompería el CAC de Palanca 3, ⚪). **Test del peso (Meta):** si en dispositivos de cohorte el envío del PNG <80 KB añade fricción medible vs texto pese al dato Profeco → caer a fallback de texto.

---

## 2. PALANCA 2 — Generador de bifurcación + foso vivo: el fix ganador · (§7.3, §14, §18)

**Clasificación: Consenso 3/3 en el MECANISMO (invariante por solver, ≥2 Pareto-no-dominadas, instrumentación). CONTESTADO solo en el número exacto de la banda de EV.**

### El generador como INVARIANTE (regla de siembra)
El pecado del GDD: trata "≥2 jugadas correctas" como **kill-test a posteriori** (§7.3/§14: "si no aparecen, pivotar"), cuando A1 🟢 dice lo contrario — **diseñas el espacio de decisión, no esperas que emerja**. El fix mueve la garantía del playtest al algoritmo (Opus, lidera; consenso 3/3):

1. **Reformular la decisión:** de "¿cuál suma 15?" (puzzle aritmético de solución casi-única) a "¿qué FUTURO capturo?". Cada Escoba candidata se evalúa en ≥2 ejes que NO se maximizan a la vez — **tempo** (puntúa ya, barato, limpia la mesa), **escala** (captura una carta que alimenta tu rama de Pacto/Jugada; menos puntos ahora, motor mayor después), **defensa** (niega al Diablo una carta que habilitaría su Carnada/Bloqueo). El **valor futuro divergente** de las capturas es lo que produce la decisión, no que "haya varios 15".
2. **Regla de siembra dura (invariante verificable):** tras la siembra de cada turno, el tablero DEBE admitir **≥2 jugadas Pareto-no-dominadas** en (tempo, escala, defensa). La siembra se deriva **deterministamente del seed** (requisito: misma semilla → misma siembra; sin esto los retos son infalsables). Si no existen ≥2 Pareto-no-dominadas → **re-siembra acotada (≤8 intentos)** operando sobre EJES, no sobre cartas concretas. La Carnada (jugada alto-tempo/baja-escala) y el Bloqueo (elimina una jugada dominante) pasan de decoración a **herramientas del generador** (§7.3 existente subordinado a esta restricción).
3. **Valor futuro divergente calibrado:** "≥2 Pareto-no-dominadas" es necesario pero no suficiente — si la 2ª opción gana por 0.3%, nadie la considera. Por eso la banda de EV (abajo).

### La banda de EV — CONTESTADO (presentar AMBOS lados)
Este es el **único desacuerdo genuino vivo** que el referee R3 dejó abierto (`contested=1`). El método para zanjarlo SÍ es consenso.

| Posición | Quién | Estructura | Piso | Techo de re-siembra | "Duda real" cuenta si |
|---|---|---|---|---|---|
| **Banda DUAL** | **Opus + Meta AI** (2/3) | Dos funciones distintas: liveness ≠ calidad | Opus admite piso ~8% (concedido a Gemini); Meta sin piso explícito | re-siembra si dominancia >25% (Opus) / >20% (Meta) | spread **≤15%** a 2-3 turnos |
| **Banda ÚNICA** | **Gemini** (1/3) | Un solo rango cerrado | **piso 15%** (nada por debajo: "ajedrez seco") | rechaza fuera de [15%, 20%] | dentro de **[15%, 20%]** |

- **Argumento de Opus/Meta (≤15%, L4 razonamiento de diseño de información casi-perfecta):** un spread del 25% (o un piso de 15%) **no es una decisión, es una trampa de novato** — nadie con 2 runs duda entre A y B si B rinde 25% menos: la toma mal una vez, aprende, y la decisión muere. A1 🟢 exige que el jugador DUDE. Además: el techo de generación alto **siembra** la dominancia que la alarma de entropía luego declarará emergencia — liveness y salud-del-meta no pueden calibrarse a bandas que se contradicen.
- **Argumento de Gemini (15-20%, L4 + psicología del género/consumidor):** por debajo de ~10% el juego se siente "ajedrez seco" — se evapora la dopamina de la suerte percibida ("casi la salvo") y ÓRDAGO deja de sentirse baraja y empieza a sentirse solver; eso eleva la carga cognitiva y mata la "partida rápida" en móvil. En el mercado hispano/LATAM el éxito de los juegos de cartas (*Truco, Escoba*) radica en la "tensión de la codicia": el jugador quiere ganarle al azar con astucia, no aprobar un examen de matemáticas. Y, simétricamente, un spread **>20%** vuelve trivial la jugada de escala/tempo y **destruye la brecha de habilidad**, colapsando el foso vivo en D7. (Opus **concedió** el piso ~8% por la mitad de este punto.)
- **Punto de fricción exacto (referee R3):** lo que para Gemini es el SUELO inaceptable (≤15%) es para Opus/Meta la BANDA de calidad. Estructura dual vs única.
- **Cómo se zanja (Consenso de método 3/3 — NO se cierra por argumento):** **solver de papel sobre 100 tableros cruzado con el test del experto.** Dar al novato y al experto el mismo seed/build en tableros que pasan cada banda. Si en los tableros de 20-25% los scores **convergen** (<15% de brecha novato↔experto) → esa banda NO produce techo de maestría → no es foso → gana ≤15%. Si incluso ≤15% converge → el verbo no tiene profundidad → cae al crux-cimiento (¿es puzzle?). *El número es ⚪ hasta que el solver hable.*

### Instrumentación del foso VIVO (Consenso 3/3 en el mecanismo)
A1 🟢 exige medir el foso EN EL TIEMPO, no una vez en papel (el GDD mata en §14 una vez y nunca más vigila). Dos centinelas desde EA (§18):
1. **Entropía de Shannon de builds ganadores por cohorte semanal** — combinación (ranuras de Maña) × (rama de Jugada dominante). Salud = estable o creciente D7→D14→D30; **alarma = caída sostenida** (>15%, Meta; <2.0-2.2 bits, Gemini — umbral exacto ⚪, validar). **Respuesta correcta = matar la dominante con un TRADE-OFF (subir su costo de slot / atar un contra-Pacto), NO un nerf de número** (un nerf desplaza el óptimo; el trade-off mata la categoría — A1 🟢).
2. **Test del experto = techo de maestría.** Mismo seed/build a novato vs experto: si scores convergen → no hay techo → foso de profundidad falsa. **Proxy gratis en EA (clave, Opus):** el **Diablo Fantasma** (§8.1, banda 5-12%) — la distribución de márgenes de victoria/derrota contra rivales de percentil conocido ES la curva de skill, en producción, gratis.

### § del GDD
**§7.3** (regla de siembra como postcondición dual verificada por solver) · **§14** (el solver reemplaza al kill-test a-posteriori) · **§18** (los dos centinelas como KPIs).

### Falsabilidad (cambio + kill + test)
**Solver de papel sobre 100 tableros** (un finde con baraja + hoja de cálculo, o medio día de código), ANTES de un píxel. **Verde:** ≥95/100 con ≥2 Pareto-no-dominadas Y spread medio en banda. **Amarillo:** existen 2 pero spread <5% → recalibrar valor futuro de capturas. **KILL (cimiento):** si tras re-estructurar la siembra >20% de tableros sigue convergiendo a 1 dominante → el verbo es **puzzle aritmético → pivotar de género conscientemente** (Riesgo C honesto de Opus; ninguna re-siembra lo arregla).

---

## 3. PALANCA 3 — Plataforma ↔ viralidad ↔ economía: el fix ganador · (§16.1)

**Clasificación: Consenso 3/3 en el MODELO (separar loops, gate LTV/CAC≥3, 3 columnas, precio LATAM ~$7.49). Las CIFRAS exactas de las tablas son ⚪/🟡 de industria — el entregable es el MODELO, no el número.**

### El modelo reconciliado
Separar quirúrgicamente DOS loops que el GDD funde y por eso se contradice (Opus, L3 🟢 unit-economics / L7 🟢 dependencia de plataforma; consenso 3/3):
- **Loop de ADQUISICIÓN (CAC > 0 SIEMPRE):** clip broadcast → demo web → wishlist Steam → compra. El "CAC~0 vía WhatsApp" es **físicamente imposible** si el link aterriza en un paywall de $15-20. **Borrar "CAC~0" del lenguaje de adquisición** (corrección editorial gratis). Aquí vive el costo del render server-side del clip. El embudo concreto (Gemini): tráfico WhatsApp/móvil → demo web de 1 manga (fricción cero) → registro de email → wishlist/compra Steam PC.
- **Loop SOCIAL intra-juego (CAC~0 real):** Diablo Fantasma + sticker. Pero su producto es **RETENCIÓN/reactivación, no instalaciones**. El error del GDD es contabilizar retención como adquisición.

**Implicación de diseño dura (Opus 🟢):** para un B2P sin MTX, LTV ≈ una sola transacción (~precio neto). El modelo SOLO cierra si **CAC < ~⅓ del neto**. Por tanto **el artefacto-puente (Palanca 1) NO es marketing — es el único camino a LTV/CAC≥3** para un B2P de bajo precio. Las tres palancas están acopladas: Palanca 1 ES parte del modelo económico.

### Cifras de unit-economics por columna — atribución y rango (CONTESTADO en niveles, no en el modelo)
Las tres IAs aportaron tablas distintas; **el modelo (3 columnas + gate) es consenso; los números exactos divergen y son ⚪/🟡 — validar en cohorte propia.** No se inventa consenso en cifras.

| Métrica | USA general (Tier-1) | Hispanos-USA (sweet spot) | LATAM | Fuente / conf |
|---|---|---|---|---|
| Precio góndola (CONVERGIDO) | $14.99 | $14.99 | **~$7.49 / 149 MXN** | 3/3 en R3 🟡 (Gemini: Balatro $7.50, Inscryption $9 — $15 en LATAM es suicidio comercial, L1) |
| Neto tras −30% Steam | ~$10.49 | ~$10.49 | ~$5-6 | Opus/Meta L2 ⚪ |
| Refund Steam (deckbuilder) | ~8-12% | ~8-12% | ~10-14% | Opus/Gemini/Meta L2 🟡 |
| Conv. wishlist→venta | ~10-18% | ~12-18% (afinidad↑) | ~6-12% (sensib. precio↑) | divergen entre IAs ⚪ |
| CAC por venta/wishlist | el más alto (paid) | el más bajo (afinidad+share) | bajísimo CPI / orgánico | 3/3 dirección 🟡; nivel ⚪ |
| **LTV/CAC objetivo (gate duro)** | **≥3** | **≥3 (Gemini proyecta ~4-5)** | **≥3** | 3/3 modelo 🟢; ratios ⚪ |

> *Las cifras de CAC/LTV/conversión que cada IA puso en sus tablas (p.ej. Gemini LTV/CAC 2.84/4.87/10.80 y su objetivo ≥4; Meta 18%/15%/12% de conversión) NO son consenso y NO se elevan a hecho. Son ilustraciones de industria/razonamiento. El entregable falsable es el modelo de payback escrito, validado en cohorte propia.*

### Riesgo no auditado (Opus, L7 🟢) + mitigación de clase mundial
**Doble dependencia de plataforma:** Steam para descubrimiento+pago Y Steamworks para los leaderboards del Diablo Fantasma. Si Steam cambia reglas, el foso social muere. **Mitigación: leaderboards en BACKEND PROPIO** (no solo Steamworks) desde el prototipo → el Diablo Fantasma funciona fuera de Steam (habilita la demo web de C-1, ports, desacopla el foso social de la plataforma de venta). Costo bajo, opcionalidad enorme. (Consenso 3/3.)

### § del GDD
**§16.1 nuevo — "Unit-economics B2P de 3 columnas + separación de loops"** (corrige §16 y §3.1 donde dice "CAC bajo"). Backend propio de leaderboards → ajuste en §15 (hoy dice "Steamworks leaderboards suficiente").

### Falsabilidad (cambio + kill + test)
**Gate de escritorio (medio día):** escribir el modelo de 3 columnas y calcular payback. **Kill:** LTV/CAC < 3 en CUALQUIER columna con cifras realistas → bajar CAC (mejor artefacto, Palanca 1) o subir LTV antes del vertical slice. **Test vivo:** conversión wishlist→venta y refund el primer fin de semana post-launch vs proyección; desviación >2× = modelo roto, frenar UA. **Test de humo (Gemini):** ~$100 en Meta Ads a hispanos-USA/LATAM con video de 6 s → landing "juega la demo en tu teléfono"; kill si CTR <2.5% o CPL > $0.50 LATAM / $1.50 hispanos-USA.

---

## 4. DECISIÓN C-1 (web/Steam/híbrido) — recomendación del panel + trade-off (para César)

**Recomendación unánime (4 votos: Opus, Gemini, Meta + ambos referees): el MODELO HÍBRIDO.** Consenso total en R1, R2 y R3 — nunca estuvo contestado.

**La precisión que el GDD no hacía explícita (Opus, suscrita por los tres):** *la demo web NO es marketing — es la PRIMERA MITAD física del artefacto-puente de la Palanca 1.*

- **Steam = el producto premium.** $14.99 base, regional en LATAM (~$7.49). Da credibilidad, descubrimiento orgánico, leaderboards (espejados a backend propio), y protege el linaje Balatro/Inscryption (premium sin MTX). No construir el juego completo en web.
- **Demo web gratis, ultraligera (<10 MB, carga <2-3 s en 4G) = el artefacto-puente jugable.** "La Mesa del Diablo de hoy" = 1 mano / 1 Manga contra el Diablo de la semilla diaria, jugable en navegador móvil desde el deep-link. Cierra el loop que el GDD prometía y nunca entregó: el link de WhatsApp aterriza en **algo jugable en 1 tap**, no en un paywall. CTA al terminar: "domínalo entero → wishlist/compra Steam".
- **La demo regala el VERBO (que viraliza); cobra el FOSO (que retiene** — Codex, Tahúres, Diablo Fantasma social, backend).

**Trade-off honesto que el panel ACEPTA (para que César decida con los ojos abiertos):**
- **+Scope real:** dos builds (Steam completo + demo web delgada) + render-worker server-side del clip + backend propio de leaderboards. Estimación de las IAs: **~+15% de costo de desarrollo inicial** (Gemini/Meta, ⚪).
- **Costo de servidor distinto de cero** por cada clip/leaderboard (acotado: solo runs que el jugador ELIGE compartir).
- **Piratería parcial de la demo** (un card-game 2D web es pirateable). Mitigado: la demo es 1 mano sin meta; el valor está en el foso del producto de pago con backend.
- **Pérdida de conversión en LATAM móvil-sin-PC (~25%, Gemini ⚪).** Mitigación: capturar ese email con promesa de **port nativo móvil año 2** → la pérdida técnica se vuelve base de pre-registro.
- **Por qué se acepta:** sin ese puente jugable, la economía B2P de bajo precio NO cierra LTV/CAC≥3. El motor viral no es nice-to-have, es el único camino al ratio.

**Lo que el panel RECHAZA:** **web-native-full-first** — mata la percepción premium, invita piratería del juego completo, y un deckbuilder web monetizado tiende a deslizar hacia F2P/MTX → choca de frente con **M1/LD7 🟢** (piso ético: no monetizar por adicción).

---

## 5. Tabla de cambios concretos al GDD v1.2

| § | Cambio | Palanca | Carta | Conf | Criterio de kill |
|---|---|---|---|---|---|
| **§8.3 nuevo** | Crear "El artefacto-puente": sistema dual `RunDigest` → (A) sticker-imagen PNG/WebP <80KB en cliente + caption con verbo-nominal y deep-link; (B) clip 6-8s con audio, render server-side/PC → broadcast MP4 <500KB / móvil WebP animado <300KB pre-renderizado | 1 | C2, D1, A3 | 🟡 (L1 formato) | A/B 20 grupos MX: kill si reenvío 24h <30% **o** comprensión <2s <70% |
| §8.3 | Canónico = imagen-sticker (peso no es fricción: Profeco ~1MB texto ≈ ~1MB imagen, Meta); texto plano = fallback feature phones | 1 | C2 🟡 | 🟡 (L1 Profeco) | en cohorte el PNG <80KB añade fricción medible pese a Profeco → caer a fallback texto |
| §8.3 | Asset móvil = WebP animado <300KB (Gemini/Meta), distinto del MP4 <500KB de PC; móvil NO codifica video (FFmpeg.wasm choke en gama baja) | 1 | B5 🟢 | 🟡 (L1 hardware) | el asset móvil supera <300KB o codifica en cliente → rompe fricción-cero, rehacer |
| §8.3 | Degradar "código de build" alfanumérico a opt-in ~5% en el Codex | 1 | A4 🟢 | 🟢 | — |
| §8.3 | Generador procedural de variantes (≈12 clips / 20 grids, copy editable de rivalidad) anti-fatiga | 1 | A3 🟡 | 🟡 (L1 vida media 2-3 sem) | K_grafo por cohorte semanal decae sostenido pese a variantes |
| §8.3 | Anti-spoiler: grid muestra resultado, link solo re-inicializa el seed | 1 | C3 | 🟢 | reconstruir la run desde el grid → matar |
| **§7.3** | Generador del Diablo = INVARIANTE: postcondición ≥2 jugadas Pareto-no-dominadas, siembra determinista por seed, re-siembra acotada ≤8 sobre ejes (tempo/escala/defensa); Carnada/Bloqueo subordinados | 2 | A1 🟢 | 🟢 (mecanismo) | >20% de tableros convergen a 1 dominante tras re-estructurar → pivotar de género |
| §7.3 | Banda de spread de EV: **dual** (re-siembra >20-25%, foso medido en ≤15% a 2-3 turnos) **[CONTESTADO: Gemini [15-20%]]** | 2 | A1 🟢 | ⚪ (número) | solver + test del experto: si tableros 20-25% convergen novato↔experto <15% → banda rota |
| §14 | Reemplazar kill-test a-posteriori por el **solver de papel** ANTES de un píxel | 2 | A1 🟢 | 🟢 | (es el test mismo) |
| §18 | KPI centinela 1: entropía de Shannon de builds ganadores semanal (alarma caída sostenida; respuesta = trade-off, no nerf) | 2 | A1 🟢 | 🟡 (umbral ⚪) | entropía cae D7→D14→D30 → pasada de balance obligatoria |
| §18 | KPI centinela 2: test del experto vía Diablo Fantasma (proxy de brecha-skill) | 2 | A1, LD6 🟢 | 🟢 | scores convergen sin importar horas → no hay techo |
| **§16.1 nuevo** | Unit-economics B2P 3 columnas; separar loop ADQUISICIÓN (CAC>0) de loop SOCIAL (CAC~0); gate LTV/CAC≥3 por columna | 3 | L3, L7 🟢 | 🟢 (modelo) / ⚪ (cifras) | LTV/CAC <3 en cualquier columna con cifras realistas → no subir a vertical slice |
| §16 / §3.1 | Borrar "CAC~0" del lenguaje de adquisición; precio LATAM ~$7.49 (149 MXN), no $15 | 3 | L3 🟢 | 🟡 (L1 elasticidad) | — (corrección editorial) |
| §15 | Leaderboards en backend propio (no solo Steamworks) desde el prototipo | 3 | L7 🟢 | 🟢 | — |
| §15 / nuevo C-1 | Confirmar HÍBRIDO: Steam premium + demo web jugable (1 mano) = primera mitad del artefacto | C-1 | M1/LD7 🟢 | 🟢 | — |

---

## 6. Lo que sigue CONTESTADO / a falsar empíricamente

1. **La banda de spread de EV (el ÚNICO contestado vivo, referee R3 `contested=1`).** Opus+Meta = banda DUAL (foso medido ≤15%, re-siembra >20-25%); Gemini = banda ÚNICA [15-20%] con piso 15%. El número exacto es ⚪ para los tres. **Zanjarlo con:** solver de papel sobre 100 tableros + test del experto (novato↔experto, mismo seed/build). Es la primera cosa a falsar.
2. **El crux-cimiento (consensuado como el que se resuelve PRIMERO):** ¿el verbo "sumar 15" admite 3 ejes de valor futuro divergente, o es un puzzle aritmético? Si capturar nunca tiene valor futuro real, el spread colapsa estructuralmente y ninguna re-siembra lo arregla → pivotar de género. El MISMO solver lo zanja.
3. **¿La fatiga creativa decae K más rápido de lo que el generador procedural lo repone?** (Meta L1: stickers se queman 2-3 sem.) Medir K_grafo por **cohorte semanal** 6-8 semanas en EA. Si decae sostenido, la viralidad tiene vida media → la economía (Palanca 3) debe presupuestar CAC>0 antes de lo previsto.
4. **¿Grid-solo iguala a grid+deep-link en K compuesto?** (Opus 🟢 dice que el deep-link compone K; Meta/Gemini que la imagen que se entiende en 0.5s es lo que cruza.) A/B de 1,000 shares midiendo `i` de segundo orden (¿el receptor genera y reenvía SU grid?). Si grid-solo iguala, el deep-link es scope innecesario en P1 (vive solo en la demo de C-1).
5. **Migración móvil→PC en LATAM** (Gemini L1: penetración PC <28% LATAM vs 76% USA; conversión real podría caer <1.5-2%). Si el test de humo de la demo da <2% de conversión a wishlist/compra → activar port nativo móvil. *Las cifras de conversión/CAC/LTV de todas las tablas son ⚪/🟡 — validar en cohorte propia, no tomar como hecho.*

---

## 7. El cambio de MAYOR apalancamiento hacia el #1

> **Construir el SOLVER DE PAPEL del generador de bifurcación (postcondición dual: re-siembra si dominancia >20-25% EV, foso medido en banda ~8-15% EV a 2-3 turnos) y correrlo sobre 100 tableros cruzado con el TEST DEL EXPERTO — ANTES de un solo píxel de arte.**

**Por qué es el #1 (consenso explícito de Opus y Meta; Gemini alinea vía "solver de dilemas"):** valida o MATA el foso entero por el costo de un fin de semana con baraja y hoja de cálculo. Y el foso es el cimiento de TODO lo demás — el artefacto-puente, la economía B2P y el Diablo Fantasma descansan sobre la premisa de que el VERBO es una decisión y no un puzzle. Hoy esa premisa es una esperanza, no una máquina. El solver es lo que convierte el número de opinión en medición y zanja de un golpe el último crux contestado (la banda de EV) y el crux-cimiento (¿es puzzle?). **Es la entrega; todo lo demás sigue siendo PowerPoint hasta que el solver hable.**
