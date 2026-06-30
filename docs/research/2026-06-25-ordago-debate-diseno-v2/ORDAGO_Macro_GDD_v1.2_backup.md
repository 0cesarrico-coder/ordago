# ÓRDAGO — Macro Game Design Document

> *La partida contra el Diablo.* Un roguelike deckbuilder con baraja española.
> Working title: **ÓRDAGO** · Alternativas: *EL ENVITE*, *LA PARTIDA*, *NAIPE*
> Versión: **1.2** (macro / north-star · post multi-debate de mejoras) · Autor: César · Estado: validado por dos debates multi-IA; listo para micro-GDD + solver de papel

> **Nota — documento hermano de AZOTH.** ÓRDAGO comparte la *doctrina de diseño* de AZOTH (juice stack como producto, premium sin MTX, "rectángulos primero", cobertura asíncrona de arquetipos, decisión de engine). Aquí se detalla **solo lo propio de ÓRDAGO**.

> ### 🔄 Qué cambió en v1.2 (resumen ejecutivo)
> La v1.1 fue sometida a (a) un **workflow de 135 agentes** que cazó 93 huecos de clase mundial, y (b) un **debate multi-IA** (Opus + Gemini 3.5 Flash + Meta AI, 3 rondas + referee + síntesis auditada PASS 100). Diagnóstico: **el VERBO ya es de clase mundial; lo que estaba lejos del #1 era la CAPA DE ENTREGA** — el GDD prometía "CAC~0 / foso viral" cinco veces sin definir el objeto que la gente reenvía (la misma "fantasía hueca" que la v1.1 juró matar, ahora en la distribución). v1.2 construye las tres máquinas que faltaban:
> 1. **El artefacto-puente canónico (§8.3 nuevo)** — el objeto dual (ficha-sticker + clip con audio) que de verdad cruza WhatsApp/IG, con la decisión de formato resuelta por data de plataforma.
> 2. **El generador de bifurcación como INVARIANTE (§7.3 reescrito)** — la elegancia deja de ser promesa y se verifica por un **solver de papel antes de un píxel**; más instrumentación del foso vivo (§18).
> 3. **La reconciliación plataforma↔viralidad↔economía (§16.1 nuevo)** — separa el loop de adquisición (CAC>0) del social (CAC~0), modelo B2P de 3 columnas con gate LTV/CAC≥3, precio LATAM ~$7.49.
> Más: lazo de retorno D1/D7 (§8.4), legibilidad visual del sistema dual + barra de Sospecha (§7.6), color redundante + juice estratificado (§10), firma sonora (§10.1), A/B de arte con glance gate (§11). **Decisión C-1 resuelta: HÍBRIDO** (Steam premium + demo web jugable). Detalle: `docs/research/2026-06-25-ordago-debate-mejoras/report.md` y `…-huecos-clasemundial/HUECOS-CLASEMUNDIAL.md`.

---

## 1. Vision Statement

**ÓRDAGO es el Balatro del mundo hispano — donde de verdad le haces TRAMPA al Diablo.**

Donde Balatro tomó la baraja francesa (póker) y AZOTH tomó la alquimia, ÓRDAGO toma **la baraja española** —el mazo de la mesa de cocina de México, LatAm y España— y le aplica el motor del género: score-chase exponencial, estructura roguelite y feedback hiper-juicy.

Pero su verbo central **no son manos de póker ni la pura optimización de multiplicadores**: es el **Escoba contra un Diablo que hace trampa, y al que tú le haces más trampa todavía.** Sumas 15 sobre una **Mesa viva** que el Diablo puebla con intención; él te impone **Trampas** que rompen las reglas ("esta mano suma 13", "los Oros no cuentan"); y tú respondes con tus **Fullerías** —la maña del tahúr— rompiendo *su* regla por una mano, con el riesgo de que te pille.

**La propuesta de valor central:**
> *"ÓRDAGO te deja VENCER AL DIABLO HACIÉNDOLE TRAMPA —reescribiendo sus reglas en una Mesa viva con tus Fullerías, no acumulando multiplicadores— usando la baraja que ya conoces de la cocina."*

**La tesis comercial (lo que lo distingue de AZOTH):** AZOTH compite por white space *estético* global. ÓRDAGO compite por white space *cultural y de mercado*: el género está dominado por la baraja francesa, lo abstracto y lo anglo. El mundo hispano —cientos de millones— **no tiene su Balatro**, pese a que su shared mental model (baraja española, Escoba/Truco/Mus) es **más fuerte** que el del póker. Alinea con el perfil del autor: mexicano, español-first, mercado LATAM + hispanos-USA.

**Elevator pitch:** *"El roguelike de la baraja de tu abuela donde ganas haciéndole TRAMPA al Diablo —rompes sus reglas en una mesa viva con tus Fullerías, no sumando más— y tu mejor partida se vuelve, jugable de un toque, el Diablo que otro tiene que vencer."*

---

## 2. Design Pillars

Comparte los 6 pilares de AZOTH. Especificidades de ÓRDAGO:
- **Pilar 2 (mental model) — ventaja, no riesgo.** "Sumar 15" es tan inmediato como el blackjack; la baraja española es intuición de infancia para el mercado hispano.
- **Pilar 3 (romper tus propias reglas) — LITERAL.** El sistema dual (Trampa↔Fullería, §7.6) convierte el lema en mecánica: el "número que sube" es consecuencia de *ganarle la trampa al Diablo*, no de apilar mults. Ése es el foso vs Balatro (A1).
- **Pilar 5 (significado) — cálido, no frío.** Barroco, folk, teatral, vivo (cantina, velas, calacas). El tema cambia *cómo se juega* (Mesa viva, Trampa), no solo cómo se ve.
- **Pilar 7 (nuevo en v1.2) — la entrega es parte del diseño.** El crecimiento no se *declara*, se construye: el artefacto-puente (§8.3) y el foso medido (§7.3, §18) son sistemas falsables, no promesas de marketing.

---

## 3. Posicionamiento de mercado

### 3.1 La tesis de diferenciación (¿no es "Balatro con sombrero"?)
El riesgo nº1 del proyecto. **Por qué la v1.2 no cae ahí:**
1. **El verbo core no es póker ni pura optimización.** Es el Escoba sobre una **Mesa adversarial poblada por el Diablo** + el **duelo de trampas** (§7.6). El engaño es el verbo.
2. **La especificidad cultural es el moat de entrada, y el sistema dual la vuelve foso de diseño (A1).**
3. **Estética y tema 100% propios.**

> **Honestidad de diseño (del debate):** el moat de hoy es cultural; el foso de clase mundial lo entrega el sistema dual + el foso medido (§7.3). Si el **solver de papel** (§14) muestra que el verbo es un puzzle aritmético de solución casi-única, ÓRDAGO debe replegarse conscientemente a "pertenencia cultural competente" o pivotar — no fingir clase mundial.
>
> **Corrección de lenguaje (v1.2):** se elimina "CAC~0" del lenguaje de **adquisición** (ver §16.1). El motor social entrega **retención**, no instalaciones gratis; la adquisición siempre tiene CAC>0.

### 3.2 El mercado hispano como cuña
- Género roguelike en su pico (~$400M Steam 2025, +80% YoY); China pesa >1/3 — prueba de que un mercado culturalmente alineado y bien servido es oro.
- El mundo hispano carece de un score-chase deckbuilder propio. Asimetría explotable.
- **Doble alcance:** "el Balatro hispano" nativo + curiosidad exótica global.
- **Localización inversa:** el español es el idioma nativo; inglés/chino son expansión.

### 3.2.1 Estado de ventana del subgénero (nuevo)
El roguelike-deckbuilder está **abierto pero comoditizándose post-Balatro** (oleada de clones). La puerta sigue abierta **para ÓRDAGO** no por novedad mecánica abstracta sino por **cultura + verbo propio** (baraja española + duelo de trampas), que un clon no puede calcar sin el trabajo cultural. Riesgo "saturación de Balatro-likes" registrado en §19.1; se cruza con el break-even de §16.1.

### 3.3 Audiencia objetivo (Quantic Foundry primario; Bartle solo léxico)
- **Primaria:** mercado hispano (MX, LatAm, España, **hispanos-USA = sweet spot Tier-1**). Clusters QF: **Mastery-Achievement** (espinazo) + **Action-Social** (motor viral).
- **Secundaria:** fans globales del género (sabor fresco + estética).
- **Núcleo competitivo/social (Action-Social = 41% del engagement LATAM/MX, QF 🟡):** capturado asíncronamente vía Diablo Fantasma (§8.1).

---

## 4. Arquetipos y estéticas (Quantic Foundry × MDA)

Mismo método que AZOTH (cadena Jugador→Estética→Mecánica; arquetipos sociales asíncronos). Jerarquía de lentes **QF (🟢) → Lazzaro (🟡) → MDA (🟡)**.

| Estética / Cluster QF | Mecánica ÓRDAGO | Nota |
|---|---|---|
| **Sensación** | Juice stack de cartas (§10): barridas explosivas, monedas, campanazo, el "¡tramposo!" del pillado | Estratificado por frecuencia (§10) |
| **Mastery-Achievement** | Apuestas y Trampas crecientes, Mangas, Codicia, Envites del Diablo | El espinazo |
| **Submission / Relax** | Loop "una mano más", sesiones cortas | El zen del naipe |
| **Fantasía (Immersion)** | Ser el tahúr que **le hace trampa** al Diablo | Trickster que GANA |
| **Narrativa (Immersion)** | Cuento folk; viñetas de cantina (opt-in); Romancero | Cero lore dump (A4) |
| **Creativity — Discovery** | Pactos Oscuros y Fullerías secretas; Codex como GRID DE HUECOS (§8) | Discovery vive bajo Creativity |
| **Creativity — Expresión** | Tu set de Fullerías+Pactos en tus ranuras de Maña ES tu firma | Sistema que lo entrega |
| **Action-Social — Community** | Sticker compartible, "liberé el alma de [primo]", Pasar la Mano (§8) | Sin co-op en vivo |
| **Action-Social — Competition** | Diablo Fantasma (rival humano real, §8.1) | Hook competitivo diegético |

### 4.1 Contrato de asignación de motores (nuevo — frecuencia × superficie)
Regla de proceso (Ley de los 3 motores): cada sistema declara su frecuencia y no se le pide lo que no le toca. Ninguna feature pasa code-review si viola su fila.

| Sistema | Frecuencia | Superficie | Trabajo que hace |
|---|---|---|---|
| Escoba / barrido (ASMR) | cada mano | core | el placer momento-a-momento |
| Duelo de trampas (Trampa↔Fullería) | cada Envite | core | el foso de decisión (A1) |
| Economía de Maña (slots) | cada Cantina | meta-run | el trade-off faustiano |
| Pactos / cascada | media run | core | el escalado exponencial |
| Diablo Fantasma + daily | **D1–D7** | meta | Reloj A (retorno corto) |
| Codex / Codicia / Condena | **D30+** | meta | Reloj B (profundidad larga) |
| Artefacto-puente (§8.3) | al compartir | distribución | el crecimiento (K) |
| Última Mano / firma sonora | pico de run | identidad | el momento memorable/compartible |

> **Los dos relojes (§19):** NO pedirle al Diablo Fantasma el trabajo D30+, NI meter profundidad de 30 días en la cita diaria. Premium = sin temporadas live-ops.

---

## 5. La fantasía / experiencia del jugador

Eres un **tahúr** que apostó su alma. El Diablo reparte, **siembra la Mesa con intención, sube la apuesta y hace trampa** —y tú debes ser más astuto y **hacerle más trampa que él.** Arco de una run ganada:
1. **Primera Manga:** torpe; el Diablo sonríe y "te sopla" las cartas (modo aprendiz, §13).
2. **La primera Fullería que rima:** rompes una Trampa del Diablo y encadenas una Escoba que dispara otra. El Diablo deja de sonreír y deja de soplarte.
3. **La máquina:** equipas tus ranuras de Maña, decides qué le empeñas (Pactos) y qué te guardas (Fullerías), encadenas Escobas sobre su Mesa sembrada.
4. **La Última Mano:** rompes la banca del infierno con una trampa final. Recuperas tu alma.

El sentimiento no es "optimicé una build": es ***le hice trampa al Diablo y gané.*** (Criterio de kill §14: ≥60% de testers describe su victoria como "le hice trampa".)

---

## 6. Core Loop

### 6.1 El verbo central — el Escoba sobre una Mesa viva
**Formas jugadas que suman 15 (o múltiplos) para hacer una *Escoba* sobre una Mesa que el Diablo puebla con intención; el Diablo impone Trampas que alteran la regla y tú las rompes con Fullerías; los Pactos encadenan Escobas en cascadas; cada Escoba puntúa Puntos × Suerte.** Es un duelo asimétrico, no un solitario.

### 6.2 El loop de mano (segundos)
```
1. El Diablo REPARTE a tu mano Y SIEMBRA la Mesa con intención (carnada o bloqueo, §7.3).
2. (Si hay Envite) una TRAMPA del Diablo altera la regla esta mano.
3. Seleccionas cartas; la UI muestra la suma acumulada de tu selección y (modo aprendiz) resalta
   cartas de la mesa que completan el 15 (§13).
4. Opcional: gastas una FULLERÍA para romper la Trampa; sube la barra de SOSPECHA (riesgo legible,
   §7.6) — antes de jugar ves cuánto arriesgas.
5. Si suma 15, ESCOBA → Puntos base × Suerte. Los PACTOS encadenan (cascada).
6. Si usaste Fullería, se resuelve el arco de Sospecha: cuela / near-miss ("te la paso, tahúr") /
   te pilla (castigo anclado a dotación, §7.6).
7. Repites hasta agotar tus Manos o alcanzar la apuesta.
```
Ritmo: **30–45 s/mano**. Cantina entre mangas: **3–5 min**.

### 6.3 El loop de run (minutos)
```
La apuesta (= "blind"): supera el umbral del Diablo. 3 apuestas por Manga (chica / grande / Envite con TRAMPA).
La Cantina: compras/equipas Pactos y Fullerías (ranuras de Maña), naipes, mejoras, reroll, slots.
4 Mangas = La Partida. Ganar la 4ª = recuperar tu alma. Presupuesto de run objetivo: ~25–35 min (§9).
```

### 6.4 El loop de meta (horas/semanas)
```
Cada run → desbloqueos en Codex + Pactos/Fullerías nuevos + posición en leaderboards + tu mejor run
   se vuelve Diablo Fantasma jugable de otros + tu sticker compartible (§8.3).
Lazo de retorno D1/D7: el Diablo de hoy, el Romancero de hoy, la Cantina del Tahúr (§8.4).
Más Tahúres → estilos. Más Codicia → la Partida más dura. Semillas diarias → competición async.
```
> **Anti-overjustification (02-SDT):** los desbloqueos dan AUTONOMÍA (elegir entre 3), no recompensa contingente; "sin ratchet ni FOMO" se extiende explícitamente al Diablo Fantasma y al daily.

---

## 7. Sistemas centrales

### 7.1 Los cuatro palos
Baraja española con identidad mecánica por palo: **🪙 Oros** (economía/Reales + Puntos base) · **🍷 Copas** (redraws/repetición) · **⚔️ Espadas** (×Suerte/poder bruto) · **🌳 Bastos** (+Puntos en bloque/escala). El palo vive en **forma/icono**, NO en re-teñir los colores funcionales (§10).
> 🔶 Dec. abierta (§19): afinidades fuertes (definen build) vs ligeras. Rec.: fuertes; validar en vertical slice.

### 7.2 La baraja (los valores) — con legibilidad
40 cartas: 1–7 + Sota(10)/Caballo(11)/Rey(12) por palo (sin 8 ni 9). Para el Escoba, las figuras valen **8/9/10**. **Los naipes muestran el valor de juego 8/9/10 GRANDE** en las figuras (ilustración tradicional de fondo) — elimina la duda "¿la Sota valía 8 o 10?" (A5, onboarding global).

### 7.3 La Mesa viva — el generador de bifurcación (INVARIANTE, no promesa) — reescrito en v1.2
La Mesa es un **adversario vivo**: cada turno el Diablo **siembra cartas con intención** desde su mazo corrupto. La v1.2 eleva "que haya ≥2 jugadas correctas" de *kill-test a-posteriori* a **invariante diseñada y verificable** (A1 🟢: diseñas el espacio de decisión, no esperas que emerja):

1. **Reformular la decisión:** de "¿cuál suma 15?" (puzzle de solución casi-única) a **"¿qué FUTURO capturo?"**. Cada Escoba candidata se evalúa en ≥2 ejes que NO se maximizan a la vez:
   - **Tempo** — puntúa ya, barato, limpia la mesa.
   - **Escala** — captura una carta que alimenta tu rama de Pacto/Jugada (menos puntos ahora, motor mayor después).
   - **Defensa** — niega al Diablo una carta que habilitaría su Carnada/Bloqueo.
   El **valor futuro divergente** de las capturas es lo que produce la decisión, no que "haya varios 15".
2. **Regla de siembra dura (postcondición verificable):** tras la siembra de cada turno, el tablero DEBE admitir **≥2 jugadas Pareto-no-dominadas** en (tempo, escala, defensa). La siembra es **100% determinista por seed** (misma semilla → misma siembra; requisito para retos falsables, §8.4). Si no existen ≥2 → **re-siembra acotada (≤8 intentos)** operando sobre EJES, no sobre cartas concretas. La **Carnada** (alto-tempo/baja-escala) y el **Bloqueo** (elimina una jugada dominante) son herramientas del generador.
3. **Banda de spread de EV (🔶 contestado — a falsar por solver, no por argumento):** el spread entre la mejor y la 2ª jugada Pareto debe estar en una banda donde el jugador DUDE de verdad. **Postura del panel:** banda de calidad **~8–15%** a 2-3 turnos (Opus+Meta: >20-25% es trampa de novato que mata el foso; piso ~8%), vs **15–20%** (Gemini: por debajo se siente "ajedrez seco", se evapora la dopamina de suerte). Se zanja con el solver (§14), no aquí. El número final es ⚪ hasta que el solver hable.

> **Por qué es el cambio de mayor apalancamiento:** sin el generador, "sumar 15" es aritmética; con él, es decisión. El **solver de papel** (§14) valida o MATA el foso por el costo de un fin de semana, ANTES de un píxel.

### 7.4 Las Jugadas (combinaciones)
Sobre el "sumar 15", la profundidad viene de las combinaciones de la baraja española como capas de bonus/mult: **Escoba** (base) · **Pares/Medias/Duples** (Mus) · **Secuencia/Liga** (Chinchón/Tute) · **Envido** (Truco) · **Las Matas** (§7.5).
> **Cambio v1.2:** las Jugadas son **todas combinables** (sustrato multiplicativo, como los Jokers de Balatro). La firma/exclusividad vive en la **economía de ranuras de Maña** (§7.6), que ya es escasa — NO en podar tipos de Jugada (eso restaba combinatoria). Añadir Pactos que premian MEZCLAR Jugadas.

### 7.5 Las Matas (legendarias — rareza integrada)
La jerarquía del Truco: **1. As de Espadas · 2. As de Bastos · 3. Siete de Espadas · 4. Siete de Oros.** Cartas de Puntos base enormes y efectos únicos. El público hispano las reconoce sin explicación; el jugador global las **descubre por captura** (competencia informacional, no tooltip — §13).

### 7.6 El SISTEMA DUAL — Trampa ↔ Fullería + economía de Maña + el arco del pillado
**(a) Las Trampas del Diablo** (en cada Envite): una regla-trampa altera el verbo ("suma 13", "Oros no cuentan", "solo pares", "la 1ª Escoba no puntúa"). Es el reto (Mastery) y la diégesis del Diablo tramposo.

**(b) Las Fullerías** (tu maña): rompen la Trampa por una mano ("la Sota se lee como 5", "esconder una Mata", "robar de la Mesa", "forzar un 15 falso"). Se juegan como un **arco de 3 tiempos** (v1.2, anti-coin-flip):
- **ANTES:** una **barra de Sospecha** visible sube con señales que el jugador controla (cuántas Fullerías llevas, repetir el mismo truco, ir ganando mucho). El riesgo es DECIDIBLE, no un dado oculto.
- **DURANTE:** 1–2 s diegéticos (el Diablo entrecierra los ojos).
- **DESPUÉS:** cuela / **near-miss** ("te la paso, tahúr", mostrando cuán cerca estuvo) / te pilla. El % es **función de la Sospecha**, no fijo. *(Descartado: escalado punitivo tipo death-spiral.)*
- **El castigo se ancla a DOTACIÓN** (06-loss-aversion): confiscar la mejor carta capturada del Envite o corromper un Pacto equipado — no "la mano" abstracta. Opción **"cobro con dignidad"**: sacrificar algo voluntario para que cuele. **El alivio es un evento de juice** (guiño cómplice, exhalación de cantina), no la mera ausencia de castigo.

**(c) Los Pactos Oscuros** (poder pasivo brutal del Diablo): "+30 Puntos por Oro", "×1.5 Suerte si Escoba con Espadas", "cuando puntúa una Mata, repite el Pacto a su izquierda". Algunos **secretos** (Discovery).

**(d) La economía de Maña — el trade-off faustiano.** Fullerías y Pactos compiten por las **mismas ~3 ranuras de "Maña"**. Cada ranura equipa **o** una Fullería **o** un Pacto; tomar un Pacto **ocupa una ranura toda la run** (la maña que le vendiste al Diablo). Build "0 Fullerías / 3 Pactos" es legal (máx poder) pero **te comes cada Trampa en crudo**. Es UN solo trade-off elegante (A1🟢🟡); costo estructural y recurrente = fausto, no Joker renombrado; saciedad alcanzable (M1·LD7🟢, la run reinicia el saldo). Auto-balance: la Trampa del Envite escala para que jugar sin maña duela. *(Para que Fullerías y Pactos no sean comparables, diséñalos para que se NECESITEN: Pacto auto-saboteador ↔ Fullería que lo destraba; ver §19 riesgo de dominante.)*

**(e) Legibilidad visual del estado dual (v1.2, A5+C1 — el corazón debe LEERSE, no memorizarse):**
- La **Trampa activa se manifiesta SOBRE la Mesa** ("Oros no cuentan" → los Oros se agrietan/desaturan; "suma 13" → el HUD reescribe el número-objetivo).
- Las **ranuras de Maña** distinguen Fullería (silueta "tuya") vs Pacto (silueta "corrupta") por FORMA, y disponible/gastada por estado.
- El **tell de Sospecha** es un objeto legible que sube ANTES de jugar.

### 7.7 La matemática: Puntos × Suerte
**Puntos (azul) × Suerte (rojo).** Los +Suerte/×Suerte crean el escalado; el orden izquierda→derecha importa; las cascadas nacen de Pactos que disparan Pactos. **El número grande es consecuencia de ganarle la trampa al Diablo, no de apilar mults en el vacío.**

### 7.8 Naipes Marcados (mejoras — equivalente Foil/Glass)
**Marcada** (×Suerte fijo) · **Dorada** (genera Reales) · **Encerada** (vuelve a la mano) · **De Cristal** (×Suerte alto pero se rompe) · **Cargada** (un uso, efecto brutal).

### 7.9 Economía: La Cantina
Moneda: **Reales** + interés sobre lo guardado (tensión gastar/acumular). En la Cantina compras/equipas Pactos, Fullerías, naipes, mejoras, reroll, ranuras de Maña.

### 7.10 La estructura: La Partida contra el Diablo
**4 Mangas** (apuesta y Trampa suben), cada una con **3 apuestas**: chica, grande, **El Envite del Diablo** (boss con regla-trampa, §7.6a). Ganar la 4ª = recuperar tu alma. **Modo Condena** (endless) post-victoria: cada nivel = **modificación ESTRUCTURAL** del espacio (patrón de siembra/Trampa compuesta), NO +%.

---

## 8. Progresión, meta y capa social asíncrona

- **Tahúres (= decks/personajes):** palo de afinidad, condición inicial, estilo. Combustible para Discovery/Expresión.
- **Niveles de Codicia (= stakes):** **ladder cualitativa** — cada escalón = una regla nueva que cambia la DECISIÓN (I = 1 Bloqueo extra; III = 2 Trampas apiladas; V = Fullerías +Sospecha…), no +%. Cada escalón = desbloqueo de Codex. Soft-cap diegético al runaway ("el Diablo iguala la apuesta").
- **El Codex / Romancero como GRID DE HUECOS (v1.2, motor SEEKING):** no un trofeo retrospectivo sino silueta ennegrecida + 1 pista diegética + condición aproximada. Revelación en 3 escalones: hueco mostrado → pista near-miss al rozar la condición → revelación juicy. **Prohibido el secreto-wiki** (todo deducible in-game). Los **Diablos del Romancero** son un bestiario de ~12-20 arquetipos (memory palace tipo Lotería) con flavor ambiguo (A4) + Trampa-firma + entrada de Codex.

### 8.1 El Diablo Fantasma — rival humano real, social, cerrable
El high-score de otro jugador se encarna **como el Diablo** a vencer:
- **Siempre un jugador REAL**, por prioridad: **(1) tu grafo social** (WhatsApp/amigos que jugaron la semilla) → **(2) tu región** → **(3) global**.
- **Banda cerrable ~5–12% sobre tu mejor histórico** en esa semilla (Festinger/LD6🟢).
- Al vencerlo: *"liberaste el alma de [handle]"* + te quedas sus Reales; aparece el siguiente.
- **Cold-start:** un **"Diablo del Romancero"** (nombre+rostro Posada) con **score real de tu percentil** — etiquetado HONESTO: es flavor, **no** cuenta como "liberaste el alma de un humano" ni entra en la tabla comparable.
- **Integridad (M1🟢):** scores reales, nunca fudgeados; **nunca se baja la vara tras una derrota**; el rubber-band solo sube; siempre se muestra handle + margen.
- Sirve a las DOS mitades de Action-Social (41% engagement LATAM/MX, QF🟡) — Competición + Community. Es además el **proxy gratis de la brecha de habilidad** (test del experto, §18).

### 8.2 Capa social — más allá de la competición
- **People Fun / reciprocidad (v1.2):** **"Pasar la Mano"** — heredas la mesa/semilla donde un amigo perdió; si la ganas, AMBOS reciben recompensa (cooperación asíncrona). Objetivo de familia/gremio semanal (barra común). *(Podado: el amuleto regalable que altera la run del amigo — choca con scores reales / UNA escalera.)*
- **Semillas diarias** ("La mesa del Diablo de hoy"): ranking global.
- **Dos planos de tabla:** canónica (intacta) + **"Retos del Romancero"** (tablas ortogonales auto-verificadas por seed, C3).
- Stretch post-1.0: duelo asíncrono / carrera de semilla (NO co-op ni PvP en vivo).

### 8.3 El artefacto-puente de ÓRDAGO — el motor de reenvío (NUEVO, P1 del debate)
El GDD apostaba todo el crecimiento a la viralidad sin definir el objeto que cruza el chat. v1.2 lo define como **sistema dual desde una única fuente serializada (`RunDigest`)**:

- **Objeto A — La ficha-sticker (PRIMARIA, cruza el grafo familiar).** Imagen **PNG/WebP <80 KB renderizada EN CLIENTE** (0 servidor): la "Mano contra el Diablo" + la línea-verbo *"Le robé el alma a @primo por +X%"* + score + cara del Diablo en tipografía Posada.
  - *Por qué imagen, no texto (Meta AI, L1 plataforma 🟡):* stickers personalizados 56% / animados 52% vs predeterminados 12%; WhatsApp = 12.4% del consumo de info en MX. Una imagen se entiende en 0.5 s; un grid de texto se lee como genérico.
  - *El peso NO es excusa (Meta AI, L1 🟡):* Profeco mide **~1 MB texto ≈ ~1 MB imagen** en WhatsApp → la imagen no añade fricción de datos; y el PNG <80 KB está muy por debajo. **Canónico = imagen-sticker; texto plano = fallback para feature phones.**
  - *Detalle de plataforma (Gemini, L1):* los stickers no admiten hipervínculos, pero el share nativo permite imagen **+ caption** → la imagen va con un caption que lleva la línea-verbo y el deep-link.
- **Objeto B — El clip 6-8 s CON AUDIO (co-primario en alcance, loop de adquisición).** Barrido de la Escoba + campanazo + el Diablo "¡tramposo!" + firma sonora (§10.1). *Reels obtienen 2×–12× el alcance de posts (Meta, L1).* **Asimétrico por plataforma:** el móvil **NO codifica video** (FFmpeg.wasm ahoga la gama baja LATAM; 87% de gamers LATAM en smartphone) → PC genera **MP4 <500 KB**; móvil **recibe/reenvía un WebP animado <300 KB pre-renderizado** (cifra propia Gemini, corrob. Meta — más exigente que el techo de PC porque viaja por el grafo móvil de fricción-cero).
- **El deep-link jugable** `ordago.gg/d/<seedhash>` embebido en el caption de ambos objetos → aterriza en la **demo web jugable** (§15, C-1 híbrido), no en un paywall. Comprensión sin acción es K de un salto; el link compone K (K = i × c, C2🟡).
- **Anti-spoiler:** la ficha muestra RESULTADO (escobas, trampas rotas, margen), NUNCA la solución; el link solo re-inicializa el mismo seed determinista (reto, no spoiler).
- **Anti-fatiga:** **generador procedural de variantes** (≈12 clips / 20 plantillas de grid + copy de rivalidad editable) — los stickers se queman en **2-3 semanas** (Meta, L1). El K lo mantiene una MÁQUINA, como el foso.
- **Degradar** el "código de build" alfanumérico actual a profundidad opt-in del ~5% en el Codex (A4).
- **KPIs:** **k-factor por segmento** (objetivo K_grafo >0.3 MX, >0.2 hispanos-USA ⚪), **share_with_audio** del clip. NO MAU como north-star de viralidad.

### 8.4 El lazo de retorno D1/D7 (NUEVO — cierra el ciclo Hook)
La run reinicia saldo (sin ratchet, correcto), pero faltaba el trigger de retorno para el espinazo Mastery/Submission:
- **"La Cantina del Tahúr":** guarida persistente amueblada con **trofeos diegéticos** (expresión-no-poder; inmune a overjustification; crea endowment) — sin tocar la pureza de la run.
- **"El Diablo de hoy":** reto SOLITARIO diario con sabor (Trampa rara + Pacto), trofeo no-ranking.
- **"El Romancero de hoy":** un hueco de Codex sugerido en 1 tap.
- **Racha opt-in / con rollover** (nunca punitiva — anti-reactancia, M1·LD7).
- KPI: % de retorno D1/D7 atribuible a trofeo vs artefacto vs daily (segmentado por cluster).

---

## 9. Filosofía de dificultad y balance
Easy to learn / hard to master; curva que **fuerza** combos rotos; variance controlada (reroll + descarte). **Presupuesto de run ~25–35 min** (Partida ganada) con **curva serrada** (Cantina = valle real; Envite = pico; Manga 4 = pico máximo audible). **Telemetría de fatiga** (§18) + **cierre digno** (beat de catarsis post-victoria que da permiso de PARAR; en Condena, celebrar antes de ofrecer reintento). Balance por spreadsheet + telemetría + el solver (§14).

---

## 10. Game Feel / Juice
Juice stack de AZOTH (animación → partículas → screen effects → audio → háptica). Sabor de ÓRDAGO + disciplinas de v1.2:
- **Feel de naipe:** peso del barajeo, chasquido al repartir, el *barrido* de la Escoba.
- **El Diablo reacciona y actúa:** siembra la Mesa con un gesto, te sopla en onboarding y deja de hacerlo, te pilla una Fullería con un "¡tramposo!".
- **Color = canal REDUNDANTE, nunca único (v1.2, accesibilidad):** los 4 canales funcionales se doble-codifican: Puntos = azul + glifo moneda; Suerte = rojo + aspa "×"; Manos = verde + pips contables; Reales = oro + "R". ≥3 paletas con separación de **luminancia ≥40**. Rojo(Suerte)/Verde(Manos) es el peor par para deuteranopía (~8% de hombres) → la forma/glifo lo desambigua. El **palo** vive en forma/icono, no en re-teñir.
- **Juice estratificado por frecuencia (4 tiers):** T0 selección sutil → T3 cascada/Mata (<5% de eventos; ~80% en T0-T1). **Coalescencia + techo duro** de shake/flash en cascadas (crescendo, no N golpes; x100 y x10000 difieren en SONIDO, no en temblor — U-invertida de Kao: el Extremo marea).
- **Presupuestos de latencia (Vlambeer #1):** tocar <50 ms, suma/preview <80 ms, Escoba <100 ms. Ningún juice salva un control flojo.
- **Panel de accesibilidad de feel:** slider de shake, reduce-flashing (WCAG 2.3.1), reduce-motion — solo cosmético, **cero impacto en score**.

### 10.1 Firma sonora + grito imitable (NUEVO — el foso más barato y perdurable, D3)
En LATAM el juego es **sonoro antes que visual**.
- **Firma sonora:** 2–3 notas ≤3 s sobre timbre folk-barroco (campana grave + jarana), **congelada como activo de marca**; suena en splash + Última Mano + final del clip. El exportador de clip SIEMPRE incluye audio.
- **Grito imitable** ≤1.5 s ligado al verbo de trampa (que RIME con "hacerle trampa"; **NO "¡ÓRDAGO!"**, que significa all-in en Mus) + canto del Diablo al imponer la Trampa.
- KPI: **share_with_audio**; test de earworm (24-48 h ≥30% tararea la firma); test de chat de voz (≥50% repite el grito al 1er intento).

---

## 11. Dirección de arte y audio (🔶 ÚNICO crux irreducible — A/B con glance gate)
**Pilar estético: barroco folk latinoamericano.** El *qué* (cantina, Diablo-tahúr, calaca, baraja reinterpretada, grabado Posada) está fijo. La **paleta/grado de maximalismo** se zanja por **test A/B de feed de 3 s**, con un **gate de legibilidad como requisito de elegibilidad** (v1.2):
- **Glance/colorblind gate (gatekeeper):** cada paleta candidata DEBE pasar primero — HUD + frame a **100×100 px en gris** + simulación protan/deutan/tritan; un juez nuevo nombra Puntos/Suerte/Manos/Reales **<0.5 s**. Solo las que pasan compiten por CTR. (Un card-game con Mesa viva densa se vuelve papilla a 100×100 px; esto mata la ignición broadcast si no se gatea.)
- **Lado A — Claroscuro boutique premium** (negro/oro-vela; tipo *Darkest Dungeon/Cult of the Lamb/Inscryption*): alto CTR en trailers, gancho de exportación Steam. *Riesgo (Meta, L1):* lectura "hotel boutique en Tulum" / **blanqueamiento** ("MÉXICO ES MAXIMALISTA").
- **Lado B — Maximalismo identitario** (*el oro como moneda sucia*, cempasúchil, papel picado, color y textura): autenticidad, evita apropiación, es lo que se guarda en LATAM. *Restricción dura:* jerarquía de valor (saturado solo en lo accionable) para no romper el glance gate.
- Define además el **key-art / capsule canónico de Steam** (discovery frame, spec del día 0).

> ⚠️ **IP/estética:** estilo Posada (dominio público) + folk del Día de Muertos = seguro; **evitar** Catrinas de marcas, personajes de películas, barajas comerciales. Diseño de cartas 100% original. El lado B es además la mitigación cultural. Registrar **code-switching** como riesgo DISTINTO del blanqueamiento.
> **Pipeline AI-augmented:** grabado-Posada + filigrana es muy favorable a generación 2D asistida por IA. Ventaja de scope.
> **Multi-nodo cultural (C-3, abierta):** construir la interfaz `cultural_packs[]` como DATA desde día 1 + **1 pack MX profundo** al lanzamiento; packs no-MX (Caribe/Cono-Sur) post-EA con consultores del nodo.

---

## 12. Narrativa y worldbuilding
- **Premisa:** un tahúr apostó su alma y debe ganarle al Diablo **con maña, haciéndole trampa.**
- **Entrega:** 100% ambiental y opcional (viñetas, flavor de Pactos/Fullerías, el arco de las 4 Mangas, el Romancero). **Cero lore dump** (A4: regla de no-peaje, materializada como **linter anti-gate**, §13).
- **Subtexto:** el **trickster** — el pícaro que vence al poder con maña. El sistema dual (§7.6) ES ese subtexto hecho mecánica.

---

## 13. UX / Onboarding (asistencia escindida + instrumentación)
- **"Sumar 15" instantáneo** (blackjack); baraja española sin tutorial para el hispano.
- **Jugadas telegrafiadas** (suma + score previo antes de confirmar).
- **`time_to_first_escoba`** (v1.2): renombrar la métrica "comprensión <90 s" a ms hasta el primer juice, gate por percentil. **Linter anti-gate** que falle el build si hay cutscene/lore/tutorial no-skippable antes de la 1ª mano (materializa "cero lore dump").
- **Curva de incertidumbre por Manga (FTUE):** gatear el **Bloqueo** (solo desde Manga 2) y la 1ª inversión de regla (tras superar el 1er Envite); guion de casi-fracaso → golpe de suerte en la sesión 1.
- **Onboarding no-hispano (P3-5):** cold-open de 8 s con UNA trampa absurda visible + Matas como siluetas-fantasma desde el min 1 (skippable); las Matas se **descubren por captura**, no por tooltip. KPI con kill: si retención D7 no-hispano < X% del hispano → replegarse a "el Balatro hispano".

### 13.1 La asistencia de UI al verbo, en TRES capas
1. **Siempre ON (gratis):** valor 8/9/10 grande en figuras + suma acumulada de tu selección. Mata la aritmética estéril.
2. **"Modo aprendiz" (gratis, temporal):** resaltar cartas de la Mesa que completan el 15, ON las primeras ~3 runs / hasta la 1ª victoria, luego **se desvanece gradual** (*"el Diablo deja de soplarte"*) + toggle de accesibilidad permanente.
3. **En maestría = NO gratis:** el resaltado de Mesa se equipa como la Fullería **"Ojo del Tahúr"** (ocupa una ranura de Maña + riesgo de pillado) → cualquier ayuda de maestría cuesta un slot y entra al trade-off, **nunca fragmenta la tabla** del Diablo Fantasma.

> Bajo la Mesa adversarial poblada (§7.3), el resaltado de Mesa cruza a **solucionador parcial** en maestría → por eso se gatea. Onboarding rápido sin muleta resentida (M1🟢🟡); maestría en crudo conserva el foso (A1).

---

## 14. Scope y MVP — el prototipo falsa el foso ANTES del arte
Filosofía "rectángulos primero". Orden de falsación de v1.2 (lo más barato y mortal primero):

**0) EL SOLVER DE PAPEL (antes de un píxel — el cambio de mayor apalancamiento).** Sobre 100 tableros sembrados: ¿hay **≥2 jugadas Pareto-no-dominadas** (tempo/escala/defensa) en cada uno, con spread en banda? Cruzado con el **test del experto** (mismo seed/build a novato y experto; deben divergir en score).
- **Verde:** ≥95/100 con ≥2 Pareto + spread en banda.
- **Amarillo:** existen 2 pero spread <5% → recalibrar el valor futuro de las capturas.
- **KILL (cimiento):** si tras re-estructurar la siembra >20% de tableros converge a 1 dominante → el verbo es puzzle aritmético → **pivotar de género conscientemente**. Zanja además la banda de EV (§7.3) y el crux "¿es puzzle?".

**1) Prototipo de papel del sistema dual:** 1 Tahúr, motor de Escoba + Puntos×Suerte, **Mesa viva** (humano hace de Diablo sembrando), ~3 ranuras de Maña, 3 Pactos + 3 Fullerías + 3 Trampas en post-its, 1 Manga (3 apuestas + 1 Envite). Criterios de kill: ¿"una mano más" sin juice? ¿≥2 builds ganadores? **Recall de fantasía ≥60% "le hice trampa"**; señal viral (risas, "¡tramposo!", ganas de repetir/compartir).

**2) Prueba del puente (§8.3, antes de gastar en marketing):** A/B en 20 grupos familiares MX — sticker-imagen vs texto. **Kill si** reenvío 24h <30% **o** comprensión <2 s <70%. **Kill de escala:** tras 1,000 shares K_grafo <0.2 → no escalar UA.

**3) Vertical slice:** 4 Mangas, ~80–120 Pactos+Fullerías, 1 Tahúr pulido con juice + audio (firma sonora §10.1), UI/color final (tras el A/B + glance gate de §11), demo web jugable + Diablo Fantasma con backend propio. Demo de Next Fest.

**Criterios de kill ampliados (v1.2):** + legibilidad del sistema dual **sin texto** (¿el tester identifica la Trampa activa y su Fullería disponible?) · + **5º criterio cultural "quita-el-símbolo"** (A/B clip mito-ON cantina/Diablo/folk vs mito-OFF arte neutro del MISMO loop; si OFF reenvía igual → el foso vive en el VERBO, recargar identidad en audio/dichos) · + glance/colorblind gate.

**Cortes:** core single-player; capa social asíncrona sí (incl. Diablo Fantasma); multijugador en vivo NO. Múltiples Tahúres, Codicia alta, Modo Condena → post-EA/1.0.

---

## 15. Tecnología y plataforma — DECISIÓN C-1 RESUELTA: HÍBRIDO
- **Engine:** validar el loop con rectángulos en lo más rápido a la mano (Godot/Love2D, un finde); Unreal solo si el juice justifica la fricción de un 2D card-game en 3D. Datos data-driven (JSON/Data Tables).
- **🔶→✅ C-1 = MODELO HÍBRIDO (unánime, 4 votos del panel):**
  - **Steam = el producto premium.** $14.99 base, regional LATAM (~$7.49). Credibilidad, descubrimiento orgánico, linaje Balatro/Inscryption. NO construir el juego entero en web.
  - **Demo web gratis ultraligera (<10 MB, carga <2-3 s en 4G) = la PRIMERA MITAD física del artefacto-puente.** "La Mesa del Diablo de hoy" = 1 mano / 1 Manga contra el Diablo de la semilla, jugable en navegador móvil desde el deep-link (§8.3). CTA al terminar: "domínalo entero → wishlist/compra Steam". Regala el VERBO (que viraliza), cobra el FOSO (Codex, Tahúres, Diablo Fantasma, backend).
  - **Trade-off aceptado:** ~+15% de costo de desarrollo (dos builds + render-worker server-side del clip + backend propio); costo de servidor por clip/leaderboard (acotado a runs que el jugador elige compartir); piratería parcial de la demo (mitigada: 1 mano sin meta, el valor está en el foso de pago). Pérdida de conversión móvil-sin-PC LATAM (~25% ⚪) mitigada capturando email → pre-registro de port nativo móvil año 2.
  - **Rechazado:** web-native-full-first (mata el premium, invita piratería del juego completo, desliza a F2P/MTX → choca con M1/LD7).
- **Leaderboards en BACKEND PROPIO** (no solo Steamworks) desde el prototipo → el Diablo Fantasma funciona fuera de Steam (habilita la demo web, ports, desacopla el foso social de la plataforma de venta). **Mapa de dependencias de plataforma (L7)** en §19.1.

---

## 16. Modelo de negocio
**Premium buy-to-play, sin MTX, updates gratis, colaboraciones estilo "Friends of Jimbo", la confianza/comunidad como activo.** El español es el idioma nativo (mercado primario gigante). **Ventaja de rating:** el Escoba no evoca casino → 12+/T (el frame "Diablo/trampa" es folk, no apuestas reales).

### 16.1 Unit-economics B2P de 3 columnas + separación de loops (NUEVO, P1 del debate)
- **Separar dos loops** que el GDD fundía: **ADQUISICIÓN (CAC>0 siempre)** = clip → demo web → wishlist → compra (aquí vive el costo del render del clip; **borrar "CAC~0" del lenguaje de adquisición**), vs **SOCIAL intra-juego (CAC~0 real)** = Diablo Fantasma + sticker, cuyo producto es **retención/reactivación, no instalaciones**.
- **Implicación dura (L3🟢):** para un B2P sin MTX, LTV ≈ una transacción (~precio neto). El modelo SOLO cierra si **CAC < ~⅓ del neto** → el artefacto-puente (§8.3) NO es marketing, es el único camino a LTV/CAC≥3.
- **Modelo de 3 columnas (el ENTREGABLE es el modelo; las cifras son ⚪/🟡 — validar en cohorte propia, NO tomar como hecho):**

| Métrica | USA general | Hispanos-USA (sweet spot) | LATAM |
|---|---|---|---|
| Precio góndola | $14.99 | $14.99 | **~$7.49 / 149 MXN** |
| Neto tras −30% Steam | ~$10.49 | ~$10.49 | ~$5–6 |
| Refund (deckbuilder) | ~8–12% | ~8–12% | ~10–14% |
| Conv. wishlist→venta | ~10–18% | ~12–18% | ~6–12% |
| CAC | el más alto (paid) | el más bajo (afinidad+share) | bajísimo CPI/orgánico |
| **LTV/CAC (gate duro)** | **≥3** | **≥3** | **≥3** |

- **Gate L4:** no se sube a vertical slice sin modelo de payback escrito y **LTV/CAC ≥3 proyectado por columna**.

---

## 17. Roadmap de producción
5 fases (Prototipo → Vertical slice → Demo/Next Fest → Early Access → 1.0+post-launch), EA transparente. Hito propio: **campaña en español/LatAm** (creators hispanos, nostalgia de la baraja, el clip "le gané al Diablo de tu primo"). **Matriz de UA por segmento:** USA → broadcast/Shorts; LATAM → fricción-cero WhatsApp; hispanos-USA → "Instagram enciende / WhatsApp quema". No asumir piso eCPM LATAM para todo el corredor. **Físca del loop viral K=i×c instrumentada** (§18) con gate de retención D1-D7 de los traídos por share ANTES de escalar UA (anti-fuego-de-paja).

---

## 18. KPIs
Por cluster QF (compleción/Codicia = Mastery; descubrimiento de Pactos/Fullerías secretos = Creativity; Diablo Fantasma = Action-Social; runs compartidas = Community); session length, CCU, retención 20h+/50h+. **KPIs nuevos de v1.2:**
- **Recall de fantasía** ("le hice trampa" ≥60%) — valida el sistema dual.
- **Foso vivo:** **entropía de Shannon de builds ganadores por cohorte semanal** (alarma = caída sostenida; respuesta = matar la dominante con TRADE-OFF, no nerf de número) · **test del experto** vía Diablo Fantasma (proxy de brecha-skill).
- **Distribución:** **k-factor por segmento** (K_grafo) · **share_with_audio** · time-to-symbol · lift de reenvío mito-on vs mito-off **por nodo** (piso por nodo, no promedio).
- **Económicos B2P:** conversión wishlist→venta, refund, CAC/payback por columna.
- **Salud/saciedad:** telemetría de fatiga (abandono por apuesta#, degradación de decisión/seg intra-run) · KPI-centinela "para satisfecho vs encadena" · `time_to_first_escoba`.
- **Penetración por geografía hispana** y **conversión no-hispana**.

---

## 19. Riesgos y decisiones

### 19.1 Riesgos
| Riesgo | Severidad | Mitigación |
|---|---|---|
| **El verbo es puzzle, no decisión (el foso no existe)** | Alta (el riesgo clave) | **Solver de papel (§14)** antes de un píxel; kill = pivotar de género |
| **El artefacto-puente no cruza el chat (viralidad humo)** | Alta | §8.3 + prueba del puente (A/B 20 grupos MX) antes de marketing |
| **Steam premium vs motor viral / economía no cierra** | Media | §16.1 (separar loops, gate LTV/CAC≥3) + C-1 híbrido (demo web jugable) |
| **Build dominante colapsa el meta sin alarma** | Media | Entropía de builds + test del experto (§18); respuesta = trade-off, no nerf |
| **Percepción "Balatro con sombrero"** | Media | Sistema dual (§7.6) + recall ≥60% (§14) |
| **Dependencia de plataforma (Steam discovery+pago+leaderboards)** | Media | Backend propio de leaderboards (§15); mapa de dependencias L7 |
| **IP/estética (Posada, blanqueamiento, code-switching)** | Media | Estilo dominio público; diseños originales; A/B lado B maximalista; code-switching como riesgo propio |
| **Saturación de Balatro-likes (ventana)** | Media | §3.2.1: la puerta sigue abierta por cultura+verbo, no skin |
| **Accesibilidad (color único / daltonismo / motion)** | Media | Color redundante + glance gate + panel de accesibilidad (§10, §11) |
| **Onboarding fuera del mundo hispano** | Baja | §13: "sumar 15" universal, legibilidad 8/9/10, modo aprendiz |
| **Rating/gambling** | Baja (ventaja) | Escoba no evoca casino; tono folk sin gore |

### 19.2 Decisiones RESUELTAS
- ✅ Verbo core (Escoba sobre Mesa viva) · ✅ Sistema dual = corazón (economía de Maña ~3 slots) · ✅ Ambición clase mundial · ✅ Costo de Pactos (ocupan slot) · ✅ Diablo Fantasma social · ✅ Asistencia de UI en 3 capas · ✅ **C-1 = HÍBRIDO** (Steam + demo web jugable) · ✅ Precio LATAM ~$7.49 · ✅ Leaderboards en backend propio · ✅ Jugadas combinables (firma vive en slots).

### 19.3 Decisiones aún abiertas (para César)
1. 🔶 **Banda exacta de spread de EV (§7.3)** — la zanja el **solver de papel** (≤15% dual vs 15-20%), no el escritorio. *Primera cosa a falsar.*
2. 🔶 **Dirección de arte (§11)** — A/B de feed con glance gate; no cerrar por intuición.
3. 🔶 **Título** — ÓRDAGO vs EL ENVITE / LA PARTIDA (cruza con el nodo cultural C-3).
4. 🔶 **Cosmología de palos (§7.1)** — fuertes vs ligeras (rec.: fuertes).
5. 🔶 **Multi-nodo cultural (C-3)** — interfaz `cultural_packs[]` día 1 + 1 pack MX profundo; resto post-EA.
6. 🔶 **Recuperabilidad de Pactos** — variante rara, no regla base.
7. 🔶 **¿AZOTH o ÓRDAGO primero?** — ÓRDAGO tiene cuña comercial más clara y barata; AZOTH mayor techo de distinción global.

---

*Fin del macro GDD v1.2. Siguiente paso lógico: (1) el **solver de papel** del generador de bifurcación (§14.0) — valida o mata el foso por un finde; (2) el **micro-GDD del prototipo** — las ~3 Trampas + 3 Fullerías + 3 Pactos concretos con números, las reglas de siembra de la Mesa viva, las matas con sus valores, los umbrales de la primera Manga, y el spec del `RunDigest` → ficha-sticker.*
