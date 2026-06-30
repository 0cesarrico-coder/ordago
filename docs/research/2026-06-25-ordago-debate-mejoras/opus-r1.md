# RONDA 1 — ASIENTO: DIRECTOR DE DISEÑO/SISTEMAS (Opus)

> Lidero la **Palanca 2** (el generador de bifurcación como invariante + la instrumentación del foso vivo). Me pronuncio en las 3 y en C-1.
> Postura de partida (red-team, no validador): el reporte de huecos tiene razón en su tesis central — **el verbo ya es de clase mundial; lo lejos del #1 es la entrega**. Mi trabajo aquí es asegurar que los fixes no vuelvan a ser "valor declarado sin máquina detrás". Por eso para cada palanca exijo el mismo estándar que la v1.1 se autoimpuso: **distinguir valor DECLARADO de valor ENTREGADO**, y que la diferencia sea un artefacto/algoritmo/cifra falsable, no una frase.

---

## PALANCA 1 — El artefacto-puente canónico (§8.3)

### Mi mejor fix de clase mundial
**El artefacto NO es "un emoji-grid O un clip". Es un sistema de DOS objetos con UNA fuente de verdad serializada, y cada objeto tiene un trabajo distinto en un embudo distinto.** El error latente del GDD es tratar "compartir" como una feature; en realidad son DOS loops virales con física distinta (C2: K = i × c) que comparten un solo `RunDigest`.

**Objeto A — El parte de la trampa (emoji-grid, 0 servidor, el que CRUZA el grafo).** Texto plano copiable a 1 tap, legible mudo en WhatsApp/iMessage. Estructura propuesta (falsable, no decorativa):

```
ÓRDAGO · Mesa del Diablo #lun-24-jun
🪙🍷⚔️🌳  Almas: 🔓🔓🔓🔓  (4/4 Mangas)
Trampas rotas: 🃏🃏🃏  Fullerías pilladas: 👁️
Le robé el alma a @primo por +18%
Tu turno, tahúr → ordago.gg/d/7F3K
```

Reglas de diseño duras (esto es lo que lo separa del antipatrón D1):
- **Cruza sin explicación (D1 🟢):** un no-jugador entiende "le ganó a alguien a las cartas contra el Diablo" en <2s. El "código de build" actual NO cumple esto y debe degradarse a profundidad opt-in del ~5% (A4 🟢).
- **El gancho social va en la PRIMERA línea legible, no en metadata:** "Le robé el alma a @primo" es el verbo + el nombre del grafo. Eso es lo que dispara la respuesta ("¿cómo?/¡revancha!") — el motor de K_grafo.
- **Anti-spoiler de semilla (resuelto, no prometido):** el grid muestra RESULTADO (4/4, trampas rotas, margen) pero NUNCA la solución (qué cartas, qué orden, qué Fullería). El link `ordago.gg/d/<seedhash>` deja jugar la MISMA mesa sin revelar cómo se ganó. La semilla es reto compartido (C3), no spoiler.
- **El "+18%" es el margen sobre el Diablo Fantasma** (§8.1, banda 5-12%→aquí mostrado tras vencer): ata el artefacto al rival humano real. Sin nombre+margen, es un share de dominancia anónimo (no cruza el grafo LATAM).

**Objeto B — El clip de 6-8s CON AUDIO (el que enciende BROADCAST, IG/TikTok).** El barrido de la Escoba final + el campanazo del ×Suerte + el "¡tramposo!" del Diablo + la firma sonora (Palanca audio, P2-5). Trabajo distinto: no cruza el grafo cerrado, enciende el feed abierto → wishlists, no instalaciones.

**Cuál primero:** **A primero, B segundo.** Razón anclada al mercado (regla de César): en LATAM el canal de mayor fricción-cero y mayor reciprocidad es **WhatsApp** (B5 🟢 fricción-cero; D1 🟢 cruza chats), donde el clip pesa, se comprime y se reenvía mudo el 70-80% de las veces (D3 🟡 — validar share_with_audio en cohorte). El emoji-grid es **0 servidor, 0 peso, 1 tap, audio-independiente** → cruza primero y barato. El clip es el multiplicador de alcance broadcast pero con CAC>0 (vive en el embudo de wishlists, no en CAC~0). **Construir A en el prototipo; B en el vertical slice.**

### Riesgo principal + mitigación
**Riesgo:** el emoji-grid se lee como "otro Wordle clone" y el verbo único (trampa) se pierde en el ruido de grids genéricos → i (invitación) alta pero c (conversión del que la recibe) baja → K colapsa. **Mitigación:** el diferenciador NO es el grid (commodity) sino **la línea de verbo nominal** ("le robé el alma a @primo") + el **deep-link que deja jugar la misma mesa**. El grid es el envoltorio; el reto-jugable-en-1-tap es el producto. Segundo riesgo (M1 🟢): que el "te robé el alma a @primo" se sienta agresivo/deuda en el grafo → tensión con P2-6 (reciprocidad). Mitigación: ofrecer variante cooperativa del mismo artefacto ("te dejé la mesa servida, ¿la cierras?") — el artefacto debe tener modo dominancia Y modo reciprocidad.

### Test/kill más barato
**Prueba del puente (pre-construcción, papel/Figma):** mostrar el emoji-grid mockup 0.5s a 10 no-jugadores hispanos. Pregunta: "¿qué pasó aquí?". **Kill:** si <60% dice algo como "le ganó/le hizo trampa a alguien contra el Diablo" → el output no cruza, rediseñar ANTES de gastar en marketing. **KPI vivo:** `K_grafo` por segmento; si K_grafo < 0.2 en cohorte hispana → el artefacto no cruza, no escalar UA (anti-fuego-de-paja, C2).

---

## PALANCA 2 — El generador de bifurcación + el foso VIVO ★ (lidero)

Esta es la palanca donde el GDD comete su pecado más caro disfrazado de virtud: **trata la elegancia (A1 🟢) como una HIPÓTESIS a falsar en playtest ("si no aparecen ≥2 jugadas, pivotar"), cuando A1 dice lo contrario — diseñas el espacio de decisión, no esperas que emerja.** Un kill-test a-posteriori es una red de seguridad, no un diseño. Si el generador no está construido como invariante, lo más probable (prior 🟡) es que la Mesa converja a una jugada casi-dominante y el kill-test lo descubra TARDE y caro. Hay que mover la garantía del playtest al algoritmo.

### Mi mejor fix de clase mundial — el generador como INVARIANTE, en 3 capas

**Capa 1 — Reformular la decisión: de "¿cuál suma 15?" a "¿qué FUTURO capturo?" (tempo-vs-escala).**
El verbo "sumar 15" en mano+mesa abiertas tiene, casi siempre, solución aritmética casi-única → es un puzzle, no una decisión (A1: sin trade-off real no hay foso). La emergencia NO puede venir de "hay varios 15"; debe venir de que **cada 15 captura un conjunto de cartas con VALOR FUTURO divergente**. Concretamente, cada Escoba candidata se evalúa en ≥2 ejes que NO se pueden maximizar a la vez:
- **Tempo:** puntúa YA (cierra la apuesta este turno, barato, seguro).
- **Escala:** captura una carta que **alimenta tu rama de Pacto/Jugada** (p.ej. una Mata para el Pacto "cuando puntúa una Mata, repite"; un Oro para el build de Oros) → menos puntos AHORA, motor más grande DESPUÉS.
- **Defensa:** niega a la siembra del Diablo una carta que, si la dejas, le habilita su Carnada/Bloqueo el próximo turno.

La decisión deja de ser aritmética y pasa a ser **economía de oportunidad sobre el tiempo** — exactamente el foso A1 (trade-off real, consecuencia <1s perceptible, se renueva cada tablero). Ancla: A1 🟢 (el trade-off) / ⚪ (que ESTE eje específico lo produzca — validar con solver).

**Capa 2 — La regla de siembra dura (el invariante verificable).** El algoritmo del Diablo NO siembra al azar ni "para tentar"; siembra bajo una **restricción de garantía**: *tras la siembra de cada turno, el tablero DEBE admitir ≥2 jugadas Pareto-no-dominadas en el espacio (tempo, escala, defensa).* Implementación (data-driven, falsable):
1. El generador propone un tablero candidato (mano + siembra) desde el mazo corrupto del Diablo, **derivado deterministamente del seed** (requisito P2-4: misma semilla → misma siembra; sin esto los retos son infalsables).
2. Un **solver de papel/código** enumera todas las Escobas legales y las puntúa en los 3 ejes.
3. Si NO existen ≥2 jugadas Pareto-no-dominadas (una domina a todas en los 3 ejes) → **el generador RECHAZA y re-siembra** (re-roll acotado, p.ej. máx 8 intentos; si falla, ajusta 1 carta de la siembra hacia divergencia). Esto convierte "≥2 jugadas correctas" de ESPERANZA en POSTCONDICIÓN del generador.
4. La Carnada/Bloqueo del GDD (§7.3) se subordinan a esta restricción: la Carnada es una jugada de alto-tempo/baja-escala (Pareto-no-dominada por tempo), el Bloqueo elimina una jugada dominante para forzar divergencia. Es decir, **los dos modos de siembra que ya existen pasan a ser HERRAMIENTAS del generador, no decoración.**

**Capa 3 — Calibración de la divergencia (que las 2 jugadas valgan la pena de verdad).** "≥2 Pareto-no-dominadas" es necesario pero no suficiente: si la 2ª opción es Pareto-no-dominada por 0.3%, nadie la considera. Métrica de salud: **spread de decisión** = diferencia de EV entre la mejor jugada-tempo y la mejor jugada-escala, evaluada a horizonte de 2-3 turnos. Objetivo: que ninguna de las dos domine en EV por más de ~10-15% para el jugador medio (banda donde la skill, no la aritmética, decide). Esto es lo que separa "técnicamente hay 2 jugadas" de "de verdad dudo".

### El foso VIVO — instrumentación (lo que el GDD NO tiene)
A1 🟢 exige medir el foso **en el tiempo**, no una vez en papel. El GDD mata en §14 una vez y nunca más vigila. Dos KPIs centinela desde EA:

1. **Entropía de builds por cohorte semanal.** Variable = combinación (ranuras de Maña: qué Fullerías/Pactos) × (rama de Jugada dominante). Métrica = entropía de Shannon de la distribución de builds GANADORES por cohorte. **Salud = estable o creciente D7→D14→D30.** **Alarma = caída sostenida** (la dominante oculta está colapsando el meta). Respuesta correcta cuando suena: **matar la dominante con un trade-off** (subir su costo de slot / atar un contra-Pacto), NO un nerf de número (un nerf desplaza el óptimo a otra dominante; el trade-off mata la categoría de dominancia — A1). Umbral falsable: definir piso de entropía en vertical slice (p.ej. ≥80% de la entropía teórica máxima del set actual); por debajo = pasada de balance obligatoria.

2. **El test del experto (brecha de skill = techo de maestría).** En vertical slice: dar el **mismo seed y el mismo build inicial** a un novato y a un experto. Si sus scores **convergen** → no hay techo de maestría → el foso es de profundidad falsa (el juego "se juega solo"). Si **divergen** de forma estable → hay skill expression → hay foso vivo. **Proxy escalable en EA (clave, descarta el solver completo que es intratable):** usar el **Diablo Fantasma** (§8.1, banda 5-12%) como medidor natural de brecha-skill — la distribución de márgenes de victoria/derrota contra rivales reales de percentil conocido ES la curva de skill, gratis, en producción. Si todos ganan por el mismo margen sin importar horas jugadas → no hay techo.

### Riesgo principal + mitigación
**Riesgo A (el grande):** que la restricción "≥2 Pareto-no-dominadas" se cumpla técnicamente pero la 2ª jugada sea **transparentemente peor** para cualquiera con 2 runs de experiencia → la decisión muere igual, solo que el kill-test la deja pasar porque el criterio era binario. **Mitigación:** la Capa 3 (spread de EV ≤10-15%) — el criterio falsable no es "existen 2 jugadas" sino "existen 2 jugadas cuyo EV difiere <15% a 2-3 turnos". Esto es lo que estoy afilando frente al reporte de huecos, que solo pedía "Pareto-no-dominadas".
**Riesgo B:** que el generador con re-siembra produzca tableros que se sienten ARTIFICIALES/repetitivos (siempre la misma forma de dilema) → el jugador detecta la mano del diseñador y se rompe la diégesis del "Diablo siembra con intención". **Mitigación:** el re-roll está acotado (máx ~8 intentos) y la restricción opera sobre EJES, no sobre cartas concretas → hay miles de tableros que satisfacen el invariante; medir variedad de FORMA de dilema, no solo existencia.
**Riesgo C (honestidad de diseño):** este sistema es **más caro de construir** que "sembrar y rezar". Si el solver muestra que el verbo NO admite 3 ejes de valor divergente (p.ej. porque capturar nunca tiene valor futuro real), entonces el verbo ES un puzzle y el kill original del GDD (§7.3) se dispara — **pivotar de género, conscientemente.** No fingir que el generador lo arregla.

### Test/kill más barato
**Solver de papel sobre 100 tableros sembrados** (antes de cualquier playtest, antes de arte). Para cada tablero: enumerar Escobas, puntuar en (tempo, escala, defensa), contar Pareto-no-dominadas y medir spread de EV.
- **Verde:** ≥95/100 tableros con ≥2 jugadas Pareto-no-dominadas Y spread medio ≤15%.
- **Amarillo:** ≥2 jugadas pero spread <5% (existen pero no importan) → recalibrar valor futuro de capturas.
- **KILL (rojo):** si tras re-estructurar la siembra el espacio sigue convergiendo a 1 dominante en >20% de tableros → el verbo es puzzle aritmético → pivotar de género (no es deshonra; es la disciplina que la v1.1 prometió).
Costo: un fin de semana de un humano con baraja + hoja de cálculo, o medio día de código. **Es el test más barato y de mayor apalancamiento de todo el proyecto** — valida o mata el foso entero antes de un solo píxel.

---

## PALANCA 3 — Reconciliar plataforma ↔ viralidad ↔ economía (§16.1)

> No es mi asiento de liderazgo (es de negocio), pero como Director de Sistemas exijo que la "entrega" económica sea una MÁQUINA con cifras, no una promesa — el mismo estándar de las otras dos. Marco mis cifras como ⚪/🟡: son rangos de industria/razonamiento, no data de cohorte propia. **Validar todo en cohorte propia.**

### Mi mejor fix de clase mundial
**Separar quirúrgicamente DOS loops que el GDD funde y por eso se contradice (L3 🟢 unit-economics, L7 🟢 dependencia de plataforma):**
- **Loop de ADQUISICIÓN** (CAC > 0 siempre): clip broadcast → wishlist Steam → compra. Aquí el "CAC~0 vía WhatsApp" es **físicamente imposible** si el link aterriza en un paywall de $15-20 (C-2). Borrar "CAC~0" del lenguaje de adquisición y reformular como "CAC bajo / motor de wishlists" (la corrección editorial es gratis).
- **Loop SOCIAL intra-juego** (retención, no adquisición): el Diablo Fantasma + el emoji-grid retienen y reactivan a quien YA compró. Aquí el "comparte solo en el grupo" sí es CAC~0 — pero su producto es RETENCIÓN/reactivación, no instalaciones nuevas. El error del GDD es contabilizar retención como adquisición.

**El §16.1 "Unit economics B2P de 3 columnas" (cifras ⚪/🟡 de industria — validar):**

| Métrica | USA general (Tier-1) | Hispanos-USA (sweet spot) | LATAM |
|---|---|---|---|
| Precio góndola | $14.99 | $14.99 | regional ~$7-9 (paridad) |
| Neto tras -30% Steam | ~$10.49 | ~$10.49 | ~$5-6 |
| Refund Steam (típico deckbuilder) | ~8-12% 🟡 | ~8-12% | ~8-12% |
| Conversión wishlist→venta (launch month) | ~10-20% 🟡 | ~12-20% (afinidad↑) | ~6-12% (sensib. precio↑) |
| CAC por wishlist (clip orgánico) | bajo, no-cero ⚪ | el más bajo (afinidad + share) ⚪ | bajísimo CPI pero eCPM bajo |
| Motor dominante | broadcast/Shorts | "IG enciende / WhatsApp quema" | WhatsApp fricción-cero |

**La regla de oro de viabilidad (gate L4 del reporte, la suscribo):** no se sube a vertical slice sin un modelo de payback escrito y **LTV/CAC ≥ 3 proyectado por columna**. Para un B2P sin MTX, LTV ≈ precio neto × (1 + tasa de re-compra de DLC/secuela, ~0 en v1) — es decir LTV es casi una sola transacción. Eso significa que el modelo SOLO cierra si **CAC < ~$3.50 por venta en USA** (un tercio de $10.49 neto). **Implicación de diseño dura:** el motor viral orgánico (emoji-grid + clip) no es un "nice-to-have de marketing" — es **el único camino a LTV/CAC ≥3 para un B2P de bajo precio.** Si el artefacto-puente (Palanca 1) no funciona, la economía no cierra. Las tres palancas están acopladas: Palanca 1 ES parte del modelo económico, no un canal aparte.

### Riesgo principal + mitigación
**Riesgo:** doble dependencia de plataforma no auditada (L7 🟢) — Steam para descubrimiento+pago Y Steamworks para los leaderboards del Diablo Fantasma. Si Steam cambia reglas (cut, visibilidad, leaderboard API) el foso social muere. **Mitigación:** leaderboards en **backend propio** (no solo Steamworks) desde el prototipo → el Diablo Fantasma funciona fuera de Steam (habilita la demo web de C-1, ports, y desacopla el foso social de la plataforma de venta). Costo bajo, opcionalidad enorme.

### Test/kill más barato
**Gate de escritorio (medio día):** escribir el modelo de 3 columnas con las cifras anteriores y calcular payback. **Kill:** si LTV/CAC < 3 en CUALQUIER columna con cifras realistas → o baja el CAC (mejor artefacto, Palanca 1) o sube el LTV (¿precio? ¿DLC futuro?) antes del vertical slice. **Test vivo barato:** medir conversión wishlist→venta y refund en el primer fin de semana post-launch contra estas proyecciones; desviación >2× = el modelo estaba roto, frenar gasto de UA.

---

## RECOMENDACIÓN SOBRE C-1 (plataforma) — informar, no zanjar

**Recomiendo el HÍBRIDO, con una precisión que el reporte no hace explícita: la demo web no es "marketing", es la PRIMERA MITAD del artefacto-puente de la Palanca 1.**

- **Steam = el producto premium** ($14.99 base, regional en LATAM). Da credibilidad, descubrimiento orgánico, leaderboards (espejados a backend propio), y protege el linaje Balatro/premium-sin-MTX. No construir el juego completo en web (rompe scope y la percepción premium).
- **Demo web gratis, ultraligera = el artefacto-puente jugable.** Específicamente: **"La Mesa del Diablo de hoy" = 1 mano / 1 Manga contra el Diablo de la semilla diaria, jugable en el navegador desde el deep-link del emoji-grid** (`ordago.gg/d/<seed>`). Esto cierra el loop que el GDD prometía y nunca entregó: el link de WhatsApp aterriza en **algo jugable en 1 tap**, no en un paywall. El que pierde/gana la mano recibe el CTA: "domínalo entero → wishlist/compra Steam".

**Por qué maximiza el #1:** convierte el emoji-grid (Palanca 1, Objeto A) en un embudo cerrado y medible — el reto que viaja por WhatsApp ES jugable, y el que lo juega es un wishlist potencial con CAC casi-cero (B5 🟢 fricción-cero; D1 🟢 cruza). Resuelve la contradicción de C-2 sin borrar la ambición viral: el CAC~0 vive en la **demo jugable**, no en el producto de pago.

**Trade-off honesto (L7 🟢):** un card-game 2D web es pirateable y la demo web es scope/mantenimiento extra (un build separado, ligero pero real). Mitigaciones: la demo es deliberadamente **delgada** (1 Manga, 1 Tahúr, sin meta — da el sabor del verbo, no el juego completo); el riesgo de piratería se acota porque el VALOR está en el meta (Codex, Tahúres, Codicia, Diablo Fantasma social) que vive en el producto de pago con backend. La demo regala el verbo (que viraliza); cobra el foso (que retiene).

**Lo que NO recomiendo:** web-native-FULL-first. Mata la percepción premium, invita piratería del juego completo, y un deckbuilder web monetizado tiende a deslizar hacia F2P/MTX → choca de frente con M1/LD7 🟢 (el piso ético: no monetizar por adicción). El híbrido es el único que sirve a las tres palancas a la vez.

---

## MI APUESTA FALSABLE

> **ÓRDAGO no llegará al #1 a menos que el GENERADOR DE BIFURCACIÓN se construya como INVARIANTE verificado por solver (≥2 jugadas Pareto-no-dominadas con spread de EV ≤15%, garantizado por re-siembra) ANTES de gastar un solo píxel de arte — porque todo lo demás (el artefacto-puente, la economía B2P, el Diablo Fantasma) descansa sobre la premisa de que el VERBO es una decisión y no un puzzle, y esa premisa hoy es una esperanza, no una máquina.**

Corolario red-team, sin anestesia: el reporte de huecos diagnostica bien que el problema es "valor declarado sin máquina detrás" — pero su propio fix de la Palanca 2 ("≥2 jugadas Pareto-no-dominadas, verificable por solver") **arriesga repetir el pecado** si se queda en el criterio binario. La diferencia entre clase mundial y "competente" aquí es de UN número: el **spread de EV ≤15%**. Sin él, tendrás un juego donde técnicamente hay 2 jugadas y prácticamente solo una importa — y eso es, otra vez, una promesa de profundidad que el meta colapsará en D7-D14. La entrega de la Palanca 2 se mide en ese solver, no en este documento.
