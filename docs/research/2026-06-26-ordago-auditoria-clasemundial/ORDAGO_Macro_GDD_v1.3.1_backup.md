# ÓRDAGO — Macro Game Design Document

> *La partida contra el Diablo.* Un roguelike deckbuilder con baraja española.
> Working title: **ÓRDAGO** · Alternativas: *EL ENVITE*, *LA PARTIDA*, *NAIPE*
> Versión: **1.3.1** (macro / north-star · post 2.º ciclo de diseño · 7 debates multi-IA + debate de resolución de decisiones) · Autor: César · Estado: validado por dos ciclos de debate multi-IA (7 clústeres A–G, síntesis auditada PASS anti-fabricación) + 22 decisiones de César resueltas (12 consenso 3/3, 5 mayoría 2/3, 2 experimento); listo para micro-GDD + solver de papel

> **Nota — documento hermano de AZOTH.** ÓRDAGO comparte la *doctrina de diseño* de AZOTH (juice stack como producto, premium sin MTX, "rectángulos primero", cobertura asíncrona de arquetipos, decisión de engine). Aquí se detalla **solo lo propio de ÓRDAGO**.

> ### 🔄 Qué cambió en v1.2 (resumen ejecutivo)
> La v1.1 fue sometida a (a) un **workflow de 135 agentes** que cazó 93 huecos de clase mundial, y (b) un **debate multi-IA** (Opus + Gemini 3.5 Flash + Meta AI, 3 rondas + referee + síntesis auditada PASS 100). Diagnóstico: **el VERBO ya es de clase mundial; lo que estaba lejos del #1 era la CAPA DE ENTREGA** — el GDD prometía "CAC~0 / foso viral" cinco veces sin definir el objeto que la gente reenvía (la misma "fantasía hueca" que la v1.1 juró matar, ahora en la distribución). v1.2 construye las tres máquinas que faltaban:
> 1. **El artefacto-puente canónico (§8.3 nuevo)** — el objeto dual (ficha-sticker + clip con audio) que de verdad cruza WhatsApp/IG, con la decisión de formato resuelta por data de plataforma.
> 2. **El generador de bifurcación como INVARIANTE (§7.3 reescrito)** — la elegancia deja de ser promesa y se verifica por un **solver de papel antes de un píxel**; más instrumentación del foso vivo (§18).
> 3. **La reconciliación plataforma↔viralidad↔economía (§16.1 nuevo)** — separa el loop de adquisición (CAC>0) del social (CAC~0), modelo B2P de 3 columnas con gate LTV/CAC≥3, precio LATAM ~$7.49.
> Más: lazo de retorno D1/D7 (§8.4), legibilidad visual del sistema dual + barra de Sospecha (§7.6), color redundante + juice estratificado (§10), firma sonora (§10.1), A/B de arte con glance gate (§11). **Decisión C-1 resuelta: HÍBRIDO** (Steam premium + demo web jugable). Detalle: `docs/research/2026-06-25-ordago-debate-mejoras/report.md` y `…-huecos-clasemundial/HUECOS-CLASEMUNDIAL.md`.

> ### 🔄 Qué cambió en v1.3 (resumen ejecutivo)
> La v1.2 fue sometida a un **2.º ciclo de 7 debates multi-IA** (clústeres A–G: foso legible, artefacto-puente, máquina comercial, audio, coherencia, awe, ética; Opus + Gemini 3.5 Flash + Meta AI L1 → R1→R2→referee → meta-síntesis auditada PASS anti-fabricación). Diagnóstico de **un único patrón dominante**: la v1.2 **prometía máquinas que no cableaba** —un "foso legible", un "artefacto-puente viral", un "audio de orden superior", un "money-shot renovable", una "ética en código"— pero las dejaba como aspiraciones sin gate falsable (la misma "fantasía hueca" que el proyecto juró matar, ahora en las máquinas de entrega y ética). **v1.3 las cablea:** cada máquina pasa a ser (a) un **invariante con umbral V/🟡/KILL numérico**, (b) un **linter/test que falla el build**, o (c) un **experimento pre-comprometido** cuyo VERDE lo fija el dato medido, no el debate.
> Las **4 palancas mayores:**
> 1. **El foso vive en el OUTPUT retrospectivo, no en el input** (A): cero tells prospectivos; legibilidad como eco post-captura gateado por maestría; solver §14.0 con pasos S4–S7 que validan dominancia de Maña y escalado del umbral del Diablo ANTES de un píxel.
> 2. **El sticker autocontenido es el puente PRIMARIO; el clip es el ENCENDEDOR** (B+D+F): el click <5% en chat familiar mata todo deep-link en el sticker → el sticker entrega el chisme relacional SIN requerir click; el clip carga el deep-link en Reels/IG.
> 3. **1.0 directo a Steam, orgánico-primario** (C): NO es un negocio de UA pago a wishlist; el LTV B2P es casi constante (~$9.3 USA·hispanos / ~$4.7 LATAM), la única variable viva es el CAC.
> 4. **Ética y carga cognitiva en CÓDIGO, no en buena intención** (G+E): veto goodwill bloqueante en CI, gobernador anti-spam que bloquea (no alerta), techo `audio_layers_active ≤ 2`, `reglas_verbalizadas ≤ 5`, serialización Z3 — todo invariante de compilación/release.
> Doctrina rectora global nueva: **visual-primario, audio/awe-amplificador** (mute=default 85–90% del feed LATAM, data L1 Meta). Plan maestro y fidelidad anti-fabricación: `docs/research/2026-06-25-ordago-debate-diseno-v2/META-SINTESIS-v1.3.md`.

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

### 3.4 El diagnóstico Balatro como invariante de identidad (v1.3, A)
ÓRDAGO adopta el reparto de transparencia de Balatro como **invariante**, no como gusto:
- **Transparencia en el cálculo TÁCTICO** (el output del turno): la suma, el score y la consecuencia de la jugada son legibles al 100%; nunca se esconde lo que pasó *en esta mano*.
- **Opacidad en la composición META** (Pactos / economía de Maña): el descubrimiento y la combinatoria de la build se revelan jugando (Discovery), no por tooltip.
- **Doctrina rectora global (v1.3, D+F): visual-primario, audio/awe-amplificador.** El **mute es el default del 85–90% del feed LATAM** (data L1 Meta, repetida en los clústeres B, D, F). Consecuencia inviolable: **el estado del juego debe ser 100% legible en silencio**; el audio y el awe son *amplificadores* (identidad, catarsis), nunca *portadores* de información. Esta doctrina gobierna §10, §11 y §19.3.

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

**Veto goodwill bloqueante en CI (v1.3, G#42 — P1-12 🟢, consenso 3/3).** Toda feature de retorno/share/social lleva una etiqueta obligatoria `goodwill: deposit | withdraw | neutral` en su PR. **El motor M1 (confianza/comunidad) VETA, nunca AUTORIZA** — está prohibido el argumento "el saldo aguanta". Un `withdraw` no mergea sin un `deposit` compensatorio o un veto explícito de César. El build queda **Unstable con auto-rollback** si en telemetría `share de rivalidad/reciprocidad > 3.5` o `block-rate > 1.5%`. Es un gate de compilación, no una guía de estilo.

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

> **El trade-off de Maña como regla-core nº7 (v1.3, E#6 / P1-6 / P2-21):** el trade-off "una ranura de Maña = una Fullería **o** un Pacto" (§7.6d) se documenta como la **regla-core nº7 del onboarding** (cuenta dentro del techo `reglas_core ≤9`, §14). El solver debe verificar **complementariedad Pacto↔Fullería** (P1-6, 🟢, 3/3): existe **≥1 estado de Mesa con EV(Pacto) > EV(Fullería)**, la **viabilidad de tomar Pacto ∈ [20%, 50%]**, y ninguna Fullería domina en **>85%** de 1000 seeds. Si no se cumple, el trade-off está colapsado y no es elegante.

### 7.4 Las Jugadas (combinaciones)
Sobre el "sumar 15", la profundidad viene de las combinaciones de la baraja española como capas de bonus/mult: **Escoba** (base) · **Pares/Medias/Duples** (Mus) · **Secuencia/Liga** (Chinchón/Tute) · **Envido** (Truco) · **Las Matas** (§7.5).
> **Cambio v1.2:** las Jugadas son **todas combinables** (sustrato multiplicativo, como los Jokers de Balatro). La firma/exclusividad vive en la **economía de ranuras de Maña** (§7.6), que ya es escasa — NO en podar tipos de Jugada (eso restaba combinatoria). Añadir Pactos que premian MEZCLAR Jugadas.

### 7.5 Las Matas (legendarias — rareza integrada)
La jerarquía del Truco: **1. As de Espadas · 2. As de Bastos · 3. Siete de Espadas · 4. Siete de Oros.** Cartas de Puntos base enormes y efectos únicos. El público hispano las reconoce sin explicación; el jugador global las **descubre por captura** (competencia informacional, no tooltip — §13).

### 7.6 El SISTEMA DUAL — Trampa ↔ Fullería + economía de Maña + el arco del pillado
**(a) Las Trampas del Diablo** (en cada Envite): una regla-trampa altera el verbo ("suma 13", "Oros no cuentan", "solo pares", "la 1ª Escoba no puntúa"). Es el reto (Mastery) y la diégesis del Diablo tramposo.

**(b) Las Fullerías** (tu maña): rompen la Trampa por una mano ("la Sota se lee como 5", "esconder una Mata", "robar de la Mesa", "forzar un 15 falso"). Se juegan como un **arco de 3 tiempos** (v1.2, anti-coin-flip):
- **ANTES:** una **barra de Sospecha** visible sube con señales que el jugador controla (cuántas Fullerías llevas, repetir el mismo truco, ir ganando mucho). El riesgo es DECIDIBLE, no un dado oculto.
- **DURANTE:** 1–2 s diegéticos (el Diablo entrecierra los ojos). *(Spec v1.3, #10/#74: es un **beat de revelación NO bloqueante** —el control nunca se congela—; el resultado resuelve **<100 ms** tras el suspense, sin 2.º freeze. La Fullería ocurre por Envite (~4×/run), no por mano; el beat se **comprime en repeticiones** para no fatigar a la 3.ª–4.ª vez. No hay hit-stop que bloquee input.)*
- **DESPUÉS:** cuela / **near-miss** ("te la paso, tahúr", mostrando cuán cerca estuvo) / te pilla. El % es **función de la Sospecha**, no fijo. *(Descartado: escalado punitivo tipo death-spiral.)*
- **El castigo se ancla a DOTACIÓN** (06-loss-aversion): confiscar la mejor carta capturada del Envite o corromper un Pacto equipado — no "la mano" abstracta. *(Spec v1.3, #72: **"corromper" un Pacto = embrujo temporal recuperable en la Cantina, NUNCA destrucción permanente del techo de motor de la run.** El castigo del pillado jamás reduce de forma irreversible la potencia de la build — descartado el death-spiral.)* Opción **"cobro con dignidad"**: sacrificar algo voluntario para que cuele. **El alivio es un evento de juice** (guiño cómplice, exhalación de cantina), no la mera ausencia de castigo.

**(c) Los Pactos Oscuros** (poder pasivo brutal del Diablo): "+30 Puntos por Oro", "×1.5 Suerte si Escoba con Espadas", "cuando puntúa una Mata, repite el Pacto a su izquierda". Algunos **secretos** (Discovery).
> 🔶 **Decisión de César (DC-1, v1.3 — A#1, [firma de apetito de riesgo, no data]):** ¿**auto-sabotaje estructural** en los Pactos? (A) **emergente** — confiar en el solver S4-verde (más elegante, riesgo de que una build se cuele) vs (B) **acoplado a mano** — cada Pacto fuerte lleva un auto-sabotaje que una Fullería resuelve (más control, presiona el composabilidad-test S6). No es un consenso del panel: es apetito de riesgo del autor.

**(d) La economía de Maña — el trade-off faustiano.** Fullerías y Pactos compiten por las **mismas ~3 ranuras de "Maña"**. Cada ranura equipa **o** una Fullería **o** un Pacto; tomar un Pacto **ocupa una ranura toda la run** (la maña que le vendiste al Diablo). Build "0 Fullerías / 3 Pactos" es legal (máx poder) pero **te comes cada Trampa en crudo**. Es UN solo trade-off elegante (A1🟢🟡); costo estructural y recurrente = fausto, no Joker renombrado; saciedad alcanzable (M1·LD7🟢, la run reinicia el saldo). Auto-balance: la Trampa del Envite escala para que jugar sin maña duela. *(Para que Fullerías y Pactos no sean comparables, diséñalos para que se NECESITEN: Pacto auto-saboteador ↔ Fullería que lo destraba; ver §19 riesgo de dominante.)*

> **El disparador del arrepentimiento (v1.3, G#41 / P2-26 — §9.x Codex de Arrepentimientos).** Sobre este trade-off faustiano se construye el `RegretSituation`: **solo se arma cuando coinciden las 3 condiciones** —(1) una Trampa golpea una ranura ocupada por un Pacto; (2) existía en la run una Fullería que rompía esa Trampa; (3) el jugador no la tiene **por haber vendido esa ranura al Pacto**. Muestra la **carta** ~0.5 s (*"¿La querías, tahúr?"*), **NUNCA un número ni un EV**. `has_experienced_regret[pact_id]` apaga el susurro de forma **permanente** (terminable). Detalle, gates y kills en §9.x. **Guardarraíl ético (G):** prohibido por código "liberar slot de Maña por cooperación" — rompería este mismo trade-off.

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

> **Marco de viralidad v1.3 (G#38 / P2-30 — separar dos K):** los dos vectores virales NO se promedian. **k-rivalidad ≈ 0.45–0.62** (burla AL DIABLO, motor de alcance) **≠ k-reciprocidad ≈ 0.12–0.18** (cooperación, motor de bonding) — bandas L1 Meta, por segmento. El claim de "Community" se condiciona en §8.1; la rivalidad opera bajo el techo del gobernador anti-spam (§18).

- **Tahúres (= decks/personajes):** palo de afinidad, condición inicial, estilo. Combustible para Discovery/Expresión.
- **Niveles de Codicia (= stakes):** **ladder cualitativa** — cada escalón = una regla nueva que cambia la DECISIÓN (I = 1 Bloqueo extra; III = 2 Trampas apiladas; V = Fullerías +Sospecha…), no +%. Cada escalón = desbloqueo de Codex. Soft-cap diegético al runaway ("el Diablo iguala la apuesta").
- **El Codex / Romancero como GRID DE HUECOS (v1.2, motor SEEKING):** no un trofeo retrospectivo sino silueta ennegrecida + 1 pista diegética + condición aproximada. Revelación en 3 escalones: hueco mostrado → pista near-miss al rozar la condición → revelación juicy. **Prohibido el secreto-wiki** (todo deducible in-game). Los **Diablos del Romancero** son un bestiario de ~12-20 arquetipos (memory palace tipo Lotería) con flavor ambiguo (A4) + Trampa-firma + entrada de Codex.
  - **Codex TERMINABLE anti-FOMO (v1.3, E#24 / P2-24 🟢, 3/3):** colección **terminable** con **cardinalidad conocida (`X/N` visible)** + beat de catarsis al 100% **estrictamente estético** (skin/cante, **SIN timer**); **máx 2–3 siluetas con pistas activas** a la vez (el resto en niebla); **cada cierre destapa la silueta siguiente** (SEEKING por profundidad, no infinitud — CX-7). Gates: **D30 ≥8% sin timers**, abandono 80–99% **<5%**. 🔶 **Decisión de César (DC-6):** cardinalidad **N** (Gemini N=16/M=24 vs Meta N=12/M=18 — >12 ítems caen <5% completado móvil L1🟢 vs Opus abierto ⚪; [firma, sesgo a Meta por L1]).
  - **Biblia del Mundo — coherencia barata (v1.3, E#26 / P3-3 🟡):** **1 página = 5 hechos canónicos + 3 ambigüedades**; cada Diablo/Trampa/Fullería linkea a 1 hecho/ambigüedad. Flavor **reactivo por arquetipo de victoria** (Limpia-con-Maña vs Sucia-con-Sospecha) = **~32 strings, NO la matriz 16×24 = 384**. El linkeo es **no-contradicción, NO un motor de D7**. Apertura del Romancero D7 = **señal secundaria** (>10% o se poda a texto lineal). **Lore-UGC del Romancero DIFERIDO post-lanzamiento** (B#25 / P3-2).

### 8.1 El Diablo Fantasma — rival humano real, social, cerrable
El high-score de otro jugador se encarna **como el Diablo** a vencer:
- **Siempre un jugador REAL**, por prioridad: **(1) tu grafo social** (WhatsApp/amigos que jugaron la semilla) → **(2) tu región** → **(3) global**.
- **Banda cerrable ~5–12% sobre tu mejor histórico** en esa semilla (Festinger/LD6🟢).
- Al vencerlo: *"liberaste el alma de [handle]"* + te quedas sus Reales; aparece el siguiente.
- **Cold-start:** un **"Diablo del Romancero"** (nombre+rostro Posada) con **score real de tu percentil** — etiquetado HONESTO: es flavor, **no** cuenta como "liberaste el alma de un humano" ni entra en la tabla comparable.
- **Integridad (M1🟢):** scores reales, nunca fudgeados; **nunca se baja la vara tras una derrota**; el rubber-band solo sube; siempre se muestra handle + margen.
- Sirve a las DOS mitades de Action-Social (41% engagement LATAM/MX, QF🟡) — Competición + Community. Es además el **proxy gratis de la brecha de habilidad** (test del experto, §18).
- **Claim "Community" condicionado (v1.3, G#38 / P2-30 🟡):** la afirmación de que ÓRDAGO entrega *Community* (no solo *Competition*) se condiciona a **k-reciprocidad ≥ 0.20 a 4 semanas** (target realista 0.20–0.25, contra el 0.45–0.62 de rivalidad). Si k-reciprocidad **< 0.15**, se **corrige el claim, no se finge**. Vehículo de reciprocidad: stickers de **"Alma Co-firmada"** (humor negro de DOS tahúres contra el Diablo enemigo común, **nunca burla a un humano nombrado** — guardarraíl G).
- **Bucket social cerrado (v1.3, G#15 / P2-29 🟢):** el Diablo Fantasma se puebla desde un **bucket cerrado de ~50 pares reales del mismo percentil**, siempre un **PAR REAL** (nunca #global público, nunca un bot). Si no hay 50 reales en el bucket → se muestra "tu mejor marca", **no se inventan rivales**. Auditoría de release: **0 Diablos Fantasma sintéticos**. Prohibido estrechar el bucket dinámicamente (50→30) para retener (guardarraíl G).

### 8.2 Capa social — más allá de la competición
- **People Fun / reciprocidad (v1.2):** **"Pasar la Mano"** — heredas la mesa/semilla donde un amigo perdió; si la ganas, AMBOS reciben recompensa (cooperación asíncrona). Objetivo de familia/gremio semanal (barra común). *(Podado: el amuleto regalable que altera la run del amigo — choca con scores reales / UNA escalera.)*
- **Semillas diarias** ("La mesa del Diablo de hoy"): ranking global.
- **Dos planos de tabla:** canónica (intacta) + **"Retos del Romancero"** (tablas ortogonales auto-verificadas por seed, C3).
- Stretch post-1.0: duelo asíncrono / carrera de semilla (NO co-op ni PvP en vivo).

### 8.3 El artefacto-puente de ÓRDAGO — el motor de reenvío (P1 del debate · reordenado en v1.3)
El GDD apostaba todo el crecimiento a la viralidad sin definir el objeto que cruza el chat. v1.2 lo definió como sistema dual; **v1.3 fija la jerarquía con data L1: el sticker autocontenido es PRIMARIO, el clip es el ENCENDEDOR** — porque el **click <5% en chat familiar** mata cualquier deep-link metido *dentro* del sticker. El sistema nace de una **única fuente serializada (`RunDigest`)**:

- **Objeto A — La ficha-sticker (PRIMARIA · puente del grafo familiar · v1.3, B#27/#40/#65, E#39 / P2-4 🟢).** PNG/WebP **estático <80 KB, 512×512, renderizado 100% en CLIENTE desde la 1ª mano, 0 servidor**. **Autocontenido: entrega el golpe relacional SIN requerir click.** Composición: **texto relacional ≥40% del área** + **silueta del Diablo centrada** + emoji/texto **copiable debajo** (`ordago.gg/d/<seed> — te gané por 2`). Prioriza **IDENTIDAD** ("Soy Escobero" + título de 2 palabras derivado de la entropía de la build) y **oculta la solución del seed**.
  - *Glance-gate del sticker (v1.3, B#40 / E#39 / P2-5 🟢):* el chisme debe leerse a **100×100 px en gris y mudo** — **VERDE ≥90% de lectura** (n≥20), **KILL <90%**. El generador garantiza **≥8 arquetipos distinguibles por 1000 victorias**; el sticker limpio debe superar al cargado en **share-rate >15%**.
  - *Por qué imagen, no texto (Meta AI, L1 🟡):* stickers personalizados 56% / animados 52% vs predeterminados 12%; WhatsApp = 12.4% del consumo de info en MX; una imagen se entiende en 0.5 s. El peso NO es excusa: Profeco mide ~1 MB texto ≈ ~1 MB imagen en WhatsApp, y el PNG <80 KB está muy por debajo. **Canónico = imagen-sticker; texto plano = fallback feature phones.**
- **Objeto B — El clip ENCENDEDOR 6–8 s (carga el deep-link en Reels/IG · v1.3, B#60/#62 / P2-6 🟢).** Estructura **FIJA: Gancho (0–1.5 s) → Quiebre (1.5–4 s) → Sospecha (4–6 s) → Pillado (6–8 s)**; el **1.er frame = el Diablo pillándote** (legible sin audio, porque WhatsApp congela el 1.er frame). **Vende el DUELO Trampa↔Fullería, NO el combo/ASMR numérico.** Formato: **WebP animado 6–8 s, <300 KB, muted+playsinline, loop perfecto**. **Motion-gate como PISO: ≥70% nombra "¿trampa? ¿quién gana?" @360p mudo en 3 s.** *Reels obtienen 2×–12× el alcance de posts (Meta, L1).* Asimétrico por plataforma: el móvil **NO codifica video** (FFmpeg.wasm ahoga la gama baja LATAM) → PC genera el MP4 1080p (Steam/Reels); móvil **recibe/reenvía el WebP <300 KB pre-renderizado**.
  - *Disparo (v1.3, F#28 / CX-4):* el money-shot del clip se dispara **post-victoria** (freeze 0.5 s, fuera del frame de decisión); el **CTA es COMPARTIR, nunca comprar**.
- **OG-preview estático (v1.3, B#19 / P2-7 🟢):** el `og:image` del deep-link es **ESTÁTICO 1200×630, <45–50 KB JPEG**, servido por **CDN edge MX/BR, `max-age=1yr`, sin JS ni SSR-por-seed**; TTFB **p95 <80–100 ms**. **KILL:** preview en blanco en el validador de FB/WhatsApp **o** p95 >120 ms. El chisme dinámico va en el TEXTO copiable, no en el preview.
- **El deep-link jugable** `ordago.gg/d/<seedhash>` viaja en el **caption** (no dentro del sticker) → aterriza en la **demo web jugable** (§15, C-1 híbrido), no en un paywall.
- **WKWebView/autoplay (v1.3, B#22 / D#22 / P2-9 🟢):** video **muted+playsinline**; el audio se arma en el **1.er evento semántico** (jugar la 1ª carta / "Desafía al Diablo"), no en un tap accidental; demo inicia **<1.5 s**; linters `no_autoplay_without_gesture` / `first_tap_arms_audio`; fallback flash+vibración si `play()` falla.
- **Anti-spoiler:** la ficha muestra RESULTADO (escobas, trampas rotas, margen), NUNCA la solución; el link solo re-inicializa el mismo seed determinista (reto, no spoiler).
- **Anti-fatiga:** **generador procedural de variantes** (≈12 clips / 20 plantillas de grid + copy de rivalidad editable) — los stickers se queman en **2–3 semanas** (Meta, L1). El K lo mantiene una MÁQUINA, como el foso.
- **Degradar** el "código de build" alfanumérico actual a profundidad opt-in del ~5% en el Codex (A4).
- **KPIs (v1.3):** **métrica de ignición K2 = activación atribuible (partidas iniciadas), NO reenvíos ni clicks** (B#27 / P2-8); umbral provisional **3/100 (Opus) ↔ 0.18 (Meta)** pendiente de experimento L1; reenvíos/partida (VERDE ≥1.8) solo como proxy de ALCANCE. **share_with_audio** del clip. NO MAU como north-star de viralidad.
- **Reparto sticker/clip (v1.3, DC-20, [firma]):** consenso de "sticker primario"; reparto ~60–70% sticker / 25–30% clip / 0–15% atribución (Meta 60/25/15 vs Opus 70/30) — decisión de César.

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

### 9.1 Presupuesto temporal de run como invariante (v1.3, E#48 / P2-22 🟢, 3/3)
El presupuesto deja de ser aspiración y pasa a invariante verificable por solver (§14, 1000 runs): **`Σ(12 dientes) ∈ [25,35] min p50; p90 ≤ 40 min`**, con banda por diente (**Manga ~6–8 min, Cantina ≤90 s**). La duración se **deriva de la economía de Maña**, no de pacing libre. **MUERE si p90 > 40 min o Cantina > 90 s.**
> 🔶 **Decisión de César (DC-5, [firma]):** run continuo premium [25–35] min con **auto-save por turno** (Gemini, flow Balatro/Inscryption) vs **4 mangas × 6–8 min con save entre mangas** (Meta, sesión fragmentada). Reconciliación del panel: run continua + auto-save por turno ≈ capítulos sin romper el flow.

### 9.2 El epitafio de derrota — extender el cierre digno a la derrota (v1.3, G#70 / P2-27 🟢, 3/3)
El cierre digno se extiende a la **derrota**, no solo a la victoria: un **beat de 2–3 s** con (a) un **logro agregado** (*"Derrotaste 4 Diablos · mejor Escoba 38"*, **nunca "te faltó 1 punto"**) y (b) **permiso de parar**. **CERO CTA / ad / oferta / ranking post-derrota, por código** (guardarraíl ético G: no se monetiza la frustración). Gate: **`re-run<3s` < 12% estable**; si sube **>15% en dos builds → revertir el beat**.
> 🔶 **Decisión de César (DC-32, [firma + métrica]):** ¿**delay forzado ~1.5 s** en el epitafio? Opus sí (refuerza el permiso de parar) vs Meta no (+9% re-run). Lo zanja la métrica `re-run<3s`.

### 9.x El Codex de Arrepentimientos (NUEVO — v1.3, G#41 / P2-26, 3/3, 🟢 con umbral ⚪)
Un sistema de **enseñanza diegética del trade-off faustiano** (§7.6d), construido como invariante ético-falsable. **El susurro de arrepentimiento solo se arma cuando coinciden las 3 condiciones** (de lo contrario es ruido y se silencia):
1. Una **Trampa** del Diablo golpea una ranura de Maña **ocupada por un Pacto**.
2. **Existía en la run** una Fullería que rompía esa Trampa.
3. El jugador **no la tiene por haber vendido esa ranura al Pacto** (el coste faustiano se materializó).

**Forma:** muestra la **carta** que sacrificaste durante ~**0.5 s** con el texto *"¿La querías, tahúr?"* — **NUNCA un número ni un EV** (guardarraíl ético G#41). **Terminable:** `has_experienced_regret[pact_id]` apaga ese susurro de forma **permanente** una vez aprendido; el Codex **silencia al completar** (saciedad, anti-FOMO).
**Gates de kill (3/3, umbral ⚪ donde se marca):**
- **≥35% verbaliza "la próxima no lo vendo"** [⚪ supuesto, a falsar en playtest].
- **`re-run<3s` NO sube >12%** (no debe inducir tilt/compulsión).
- El **Codex silencia al completar** (terminabilidad real).
Si se rompe **cualquiera** de los tres → **KILL** del sistema. Pasa por el scheduler de jerarquía Z (§10.2): si coincidiera con el eco retrospectivo del foso (§11), se serializan con `Δt ≥ 300 ms` (CX-5: disparos mutuamente excluyentes en la mayoría de manos).

---

## 10. Game Feel / Juice
> **Separación taxativa v1.3 (F#63 / P3-6 🟢, 3/3): dos sistemas de clip, dos KPIs.** **§10.1 = el clip diario ASMR** (barrido de Escoba, repetible, motor de volumen/familiaridad D1–D7). **§10.2 = el money-shot / Presentador de Asombro** (awe, raro, espaciado, munición de evangelización asíncrona). **Kill #63:** el money-shot debe lograr **≥3× el share-con-audio del clip diario en 0–72 h** (≥4.5% vs ≤1.2%) o **se archiva**. No son el mismo sistema y no comparten KPI.

Juice stack de AZOTH (animación → partículas → screen effects → audio → háptica). Sabor de ÓRDAGO + disciplinas de v1.2:
- **Feel de naipe:** peso del barajeo, chasquido al repartir, el *barrido* de la Escoba.
- **El Diablo reacciona y actúa:** siembra la Mesa con un gesto, te sopla en onboarding y deja de hacerlo, te pilla una Fullería con un "¡tramposo!".
- **Color = canal REDUNDANTE, nunca único (v1.2, accesibilidad):** los 4 canales funcionales se doble-codifican: Puntos = azul + glifo moneda; Suerte = rojo + aspa "×"; Manos = verde + pips contables; Reales = oro + "R". ≥3 paletas con separación de **luminancia ≥40**. Rojo(Suerte)/Verde(Manos) es el peor par para deuteranopía (~8% de hombres) → la forma/glifo lo desambigua. El **palo** vive en forma/icono, no en re-teñir.
- **Juice estratificado por frecuencia (4 tiers):** T0 selección sutil → T3 cascada/Mata (<5% de eventos; ~80% en T0-T1). **Coalescencia + techo duro** de shake/flash en cascadas (crescendo, no N golpes; x100 y x10000 difieren en SONIDO, no en temblor — U-invertida de Kao: el Extremo marea).
- **Presupuestos de latencia (Vlambeer #1):** tocar <50 ms, suma/preview <80 ms, Escoba <100 ms. Ningún juice salva un control flojo.
- **Panel de accesibilidad de feel:** slider de shake, reduce-flashing (WCAG 2.3.1), reduce-motion — solo cosmético, **cero impacto en score**.

### 10.1 Firma sonora + grito imitable + el clip diario ASMR (el foso más barato y perdurable, D3)
> **Doble rol de §10.1 (v1.3, F#63 / B#60):** además de la firma sonora, §10.1 alberga el **clip diario ASMR** — barrido de la Escoba 6–8 s, mudo-first, **loop perfecto**, repetible — que es el **motor de volumen/familiaridad D1–D7**. Es el clip *frecuente*, distinto del money-shot *raro* de §10.2.

En LATAM el juego es **sonoro antes que visual**.
- **Firma sonora:** 2–3 notas ≤3 s sobre timbre folk-barroco (campana grave + jarana), **congelada como activo de marca**; suena en splash + Última Mano + final del clip. El exportador de clip SIEMPRE incluye audio.
- **Grito imitable** ≤1.5 s ligado al verbo de trampa (que RIME con "hacerle trampa"; **NO "¡ÓRDAGO!"**, que significa all-in en Mus) + canto del Diablo al imponer la Trampa.
- KPI: **share_with_audio**; test de earworm (24-48 h ≥30% tararea la firma); test de chat de voz (≥50% repite el grito al 1er intento).

### 10.2 El Presentador de Asombro — money-shot raro (REESCRITO en v1.3 — F#28/#29/#68/#69, 3/3)
v1.2 prometía un "money-shot renovable" sin cablearlo (ni motor, ni cap de scope, ni gates de habituación). v1.3 lo convierte en **un único motor scriptado + slot intercambiable**, con presupuesto duro y gates falsables:

- **El motor único:** **un** beat scriptado (mano + mesa + **sombra del Diablo** + cámara **pull-back**) con un **slot intercambiable**. NO se autoriza un sistema de awe por jefe; se reusa el mismo motor.
- **Casta doble:**
  - **Casta A — ~5 money-shots FULL** (jefes), con beat + **reacción física del Diablo** (se resquebraja, libera tinta) + limpiado físico de la mesa.
  - **Casta B — ~15 dosis ligeras** (PNG + SFX **0.3–0.4 s** + tipografía, **sin re-render**).
- **Cap duro de scope (G3): ≤ 0.8 días-hombre por dosis**, o se **degrada A → B**. (*"1 sprint × 20 = live-ops encubierto → prohibido"*, CX-6: el money-shot se justifica por share/adquisición, NO por retención.)
- **Awe asíncrono D30+ (P3-5):** el KPI es *"el clip del veterano convierte a un espectador"*, **no** *"el veterano está asombrado"*. Lo que convierte = la **reacción física del Diablo** + el limpiado físico de mesa, **NO números flotantes**.
- **Jerarquía Z como scheduler (v1.3, E#5 / P1-8 🟢, 3/3):** `Z1 silueta > Z2 valor > Z3 estado > Z4 cascada`; **dos eventos Z3+ NUNCA comparten frame** (`Δt(Z3a, Z3b) ≥ 300 ms`, log verificable). En el loop de decisión aplica `≤1 Z3+/frame`; el money-shot es el "1 solape Z3 controlado por run" que vive en el **beat de resultado** (CX-4), no durante la jugada.
- **Gates falsables (v1.3, F§4 / P2-25c 🟡, G-conv L1):**
  - **G1 (habituación):** el share del N-ésimo jefe **no cae monótono** vs el 1.º (**≤15% de caída del Diablo #10 vs #1**).
  - **G4 (muerte del sistema):** si `frequency > 2.7/7d` **o** `CTR −30% vs baseline` → **rotar el beat en ≤14 días**.
  - **G5 (reacción muda — kill-gate de awe):** **≥70% de no-jugadores describen "qué pasó increíble" en <5 palabras tras 0.5 s mudo.**
  - **G-conversión (Meta L1):** **share-to-wishlist 1 : 0.03–0.04 en frío** (NO 1:0.12 de Gemini, inviable a premium $14.99); **<0.02 tras 10 creadores → kill del beat.**
> 🔶 **Decisiones de César (DC-25/26/27, [firma + experimento]):** nº de money-shots full (lanzar con **5** + medir G2; subir a 6.º–8.º solo si superan G2 ≥4.5× share y G3 aguanta — **no 20**); reparto de arte (gasto al BEAT+SONIDO y al Diablo jugable, mínimo a fidelidad de render; ¿3 plantillas Meta vs 4 Opus/Gemini?); ¿Condena endless suma dosis? (solo si G3 aguanta).

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

### 11.1 Tells y legibilidad del foso: PREDICADO, no sujeto (v1.3, A#2/#35, E#5 — P1-7/P1-9/P2-2, CX-1)
La legibilidad del foso vive en el **OUTPUT retrospectivo, jamás en el input prospectivo** (CX-1: E gobierna el frame de DECISIÓN, A gobierna el de RESULTADO). Regla dura (P1-7 🟢, 3/3):
- **Cero coloreado de cartas candidatas · cero iconos prospectivos de eje (Tempo/Escala/Defensa) · cero hover/halo Pareto.** La Mesa está **limpia salvo el resaltado de las sumas de 15**. El glance-gate valida **score, no decisión** (un tell prospectivo recrearía el solver §317 y cargaría el working-set de §14).
- **Capa-1 (estado, permanente):** un **banner de Trampa / función-de-palo de 4–6 palabras, <450 ms**, auditado contra el coste de papilla de E (+120 ms / −9% completion).
- **Capa-2 (eco retrospectivo, maestría):** **destello 150–200 ms + háptico por eje**, **gateado tras ≥2 repeticiones** de la jugada y que **desvanece ~run 4** (*"memoria muscular, no UI"*). Por construcción no suma reglas verbalizadas.
- **Gate Z de peor caso (P1-9 🟢, 3/3):** con Trampa + Sospecha + cascada T3 **@100×100 px en grises + deuteranopía**, silueta+valor legibles por **≥9/10** Y `≤1 Z3+/frame`. Filtro L1: **Moto G 2022 ≥55 fps, bounce <35% @60 s, ≤100 render, ≤3 animados**. **MUERE si falla.**

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
- **"Sumar 15" no se desactiva (v1.3, A#8 / E#6):** la asistencia "sumar 15" es **ancla cultural hispana** y se mantiene siempre. **Compresión-arquetipo = REQUISITO** (P2-21): cada regla debe expresarse en **1 frase cultural** (Escoba, Truco, Mus…) o **cuenta doble** en el presupuesto de complejidad (§14). El tester debe **verbalizar antes de la Manga 1**; si nombra un sistema meta (Codex/Romancero/puente/Diablo Fantasma), entró **demasiado pronto**. Conservación: **+1 delivery ⇒ −1 carga core**. Gate: **D1 ≥35% MX/BR con ≤5 reglas verbalizadas, onboarding ≤180 s.**
> 🔶 **Decisión de César (DC-4, [firma — recomendación del panel: SERIALIZAR]):** denominador de onboarding — **≤5 reglas podando Pactos** del tutorial (Meta, +10 pp D1, riesgo "Escoba con skins") vs **tutorial serializado de 7 reglas en 3 micro-mangas** (Opus/Gemini, conserva identidad, gana en la mano 3).

### 13.1 La asistencia de UI al verbo, en TRES capas
1. **Siempre ON (gratis):** valor 8/9/10 grande en figuras + suma acumulada de tu selección. Mata la aritmética estéril.
2. **"Modo aprendiz" (gratis, temporal):** resaltar cartas de la Mesa que completan el 15, ON las primeras ~3 runs / hasta la 1ª victoria, luego **se desvanece gradual** (*"el Diablo deja de soplarte"*) + toggle de accesibilidad permanente.
3. **En maestría = NO gratis:** el resaltado de Mesa se equipa como la Fullería **"Ojo del Tahúr"** (ocupa una ranura de Maña + riesgo de pillado) → cualquier ayuda de maestría cuesta un slot y entra al trade-off, **nunca fragmenta la tabla** del Diablo Fantasma.

> Bajo la Mesa adversarial poblada (§7.3), el resaltado de Mesa cruza a **solucionador parcial** en maestría → por eso se gatea. Onboarding rápido sin muleta resentida (M1🟢🟡); maestría en crudo conserva el foso (A1).

---

## 14. Scope y MVP — el prototipo falsa el foso ANTES del arte
Filosofía "rectángulos primero". Orden de falsación de v1.2 (lo más barato y mortal primero):

**0) EL SOLVER DE PAPEL (§14.0 — antes de un píxel — el cambio de mayor apalancamiento).** Sobre 100 tableros sembrados: ¿hay **≥2 jugadas Pareto-no-dominadas** (tempo/escala/defensa) en cada uno, con spread en banda? Cruzado con el **test del experto** (mismo seed/build a novato y experto; deben divergir en score).
- **Verde:** ≥95/100 con ≥2 Pareto + spread en banda.
- **Amarillo:** existen 2 pero spread <5% → recalibrar el valor futuro de las capturas.
- **KILL (cimiento):** si tras re-estructurar la siembra >20% de tableros converge a 1 dominante → el verbo es puzzle aritmético → **pivotar de género conscientemente**. Zanja además la banda de EV (§7.3) y el crux "¿es puzzle?".

**0-bis) PASOS NUEVOS DEL SOLVER S4–S7 (v1.3, A#1/#50/#6/#8/#53, E#6 — INV-1..6, todos falsables ANTES de un píxel, sin código de producción):**
- **S4 · Dominancia de Maña (P1-1, 🟡, 3/3):** 100 tableros/seed × builds extremas (0F/3P, 3F/0P, 2/1, 1/2). **🟢 ninguna build >55% winrate y Sharpe <1.3× la 2ª · 🟡 55–60% · 🔴 KILL >60% winrate o Sharpe >1.5×.** Medir **acoplado a S5**.
- **S5 · Escalado del umbral del Diablo (P1-2, 🟡, 3/3):** mediana `score_logrado/umbral` por banda **∈ [0.95, 1.15]**, **p10 >0.8, p90 <1.6** = 🟢; [0.85, 1.25] = 🟡; **🔴 KILL si >25% de seeds con ratio <0.7 (muralla) o >25% con ratio >2.0 (trivial).**
- **S6 · Composabilidad / working-set (P1-3, 🟡, 3/3):** working-set en mano-pico verbalizado por tester naïve: **🟢 ≤6 reglas y ninguna Fullería ("Ojo del Tahúr") en >70% de builds óptimas; 🔴 KILL >7 reglas working-set o una Fullería en >85% de builds** (trade-off colapsado).
- **S7 · Dos perfiles FTUE/Maestría (P1-4, 🟡, 3/3):** FTUE = **≥1 dominante-tempo legítima, spread <8%**; Maestría = **≥2 Pareto en banda**. **KILL si FTUE tiene 2 Pareto en turno-1 o Maestría tiene 1 dominante.**
- **Techo de maestría por PROXY DE BOTS (P1-5, 🟡 [L3], Contestado→resuelto con proxy bots, NO humanos):** delta `bot_lookahead_k − bot_greedy_1ply` por banda crece **monótono con k**; **🔴 KILL si se aplana a k≥2.** Gate pre-launch; p50/p95 humanos solo post-launch.
- **Complementariedad Pacto↔Fullería (P1-6, 🟢, 3/3):** existe **≥1 estado de Mesa con EV(Pacto) > EV(Fullería)**; viabilidad de Pacto **∈ [20%, 50%]**; Fullería no domina >85% sobre 1000 seeds.
- **Banda EV objetivo (P2-3, 🟡, Contestado→delegado al solver):** **parámetro a fijar por el solver en [10–15%]** (las bandas R2 solapan en [12%, 13%]) — **no hardcodear**. Documentado: **<8% = ajedrez seco; >18% = autorrevela** (recrea el solver §317).

**0-ter) PRESUPUESTOS QUE EL SOLVER VERIFICA (v1.3, E#48/#49/#6 — INV-7..10):**
- **Presupuesto temporal (P2-22):** `Σ(12 dientes) ∈ [25,35] min p50; p90 ≤40 min`, derivado de Maña, sobre 1000 runs (§9.1). **MUERE si p90 >40 min o Cantina >90 s.**
- **Hook intra-sesión (P2-23):** `time_to_first_fullería_jugada` **p50 ≤90 s** y `first_meaningful_choice <90 s`. **Banda-muerte >120 s.**
- **Carga cognitiva / 2 denominadores (P2-21):** `reglas_core ≤9` (techo de scope) **+** `reglas_verbalizadas_por_tester ≤5` (techo de onboarding, **gana en conflicto**); `C = reglas × canales ≤12/mano`. **D1 ≥35% con ≤5 verbalizadas, onboarding ≤180 s.**
- **Gate Z / Jerarquía Z (P1-8/P1-9):** `≤1 Z3+/frame`, `Δt ≥300 ms`; **≥9/10 legibilidad peor-caso @100×100 px grises + deuteranopía**; **≥55 fps Moto G 2022, bounce <35%** (ver §11.1).

**1) Prototipo de papel del sistema dual:** 1 Tahúr, motor de Escoba + Puntos×Suerte, **Mesa viva** (humano hace de Diablo sembrando), ~3 ranuras de Maña, 3 Pactos + 3 Fullerías + 3 Trampas en post-its, 1 Manga (3 apuestas + 1 Envite). Criterios de kill: ¿"una mano más" sin juice? ¿≥2 builds ganadores? **Recall de fantasía ≥60% "le hice trampa"**; señal viral (risas, "¡tramposo!", ganas de repetir/compartir).

**2) Prueba del puente (§8.3, antes de gastar en marketing):** A/B en 20 grupos familiares MX — sticker-imagen vs texto. **Kill si** reenvío 24h <30% **o** comprensión <2 s <70%. **Kill de escala:** tras 1,000 shares K_grafo <0.2 → no escalar UA.

**3) Vertical slice:** 4 Mangas, ~80–120 Pactos+Fullerías, 1 Tahúr pulido con juice + audio (firma sonora §10.1), UI/color final (tras el A/B + glance gate de §11), demo web jugable + Diablo Fantasma con backend propio. Demo de Next Fest.

**Criterios de kill ampliados (v1.2):** + legibilidad del sistema dual **sin texto** (¿el tester identifica la Trampa activa y su Fullería disponible?) · + **5º criterio cultural "quita-el-símbolo"** (A/B clip mito-ON cantina/Diablo/folk vs mito-OFF arte neutro del MISMO loop; si OFF reenvía igual → el foso vive en el VERBO, recargar identidad en audio/dichos) · + glance/colorblind gate.

**Plan de test ampliado (v1.3):**
- **Kill de legibilidad = vocabulario-CIEGO (A#4 / P2-1 🟢, INV-16).** Se **elimina** "≥70% nombran el eje" (r=0.12 con D30, L1 Meta). Se reemplaza por: **predicción contrafáctica ≥50% (κ≥0.6) + elección Pareto en escenario espejo ≥55% tras 3 runs SIN nombrar el eje**. La verbalización es **diagnóstico, no kill** (HACER, no DECIR). Cruzado con el **test del experto** (A1: novato vs experto deben divergir en jugada con el mismo seed, o KILL).
- **Watchability de run (B#56 / P2-25 🟡):** invariante **"≥1 momento transmisible por run"** vía detector de pico (reusa el exportador). KPI ≥1 clip/30 min; **KILL: 30 min sin pico → revisar densidad de Trampas/Fullerías.**
- **A/B comercial demo LATAM (A§4 / P2-25b 🟡, validación de tells eco-gateados):** **n≥5k/rama** (eco-gateado vs sin-tells). **Pasa si: D7 +≥5 pp (target >28%) Y share-rate no cae >10% (target ≥1.4/100 sesiones) Y refund <8%.** Si sube D7 pero **share −≥15% → mataste la suerte compartible → re-evaluar la capa de UA.**
- **Gates de awe falsables (F§4 / P2-25c 🟡, G-conv L1):** **G1** share del N-ésimo jefe ≤15% de caída #10 vs #1 · **G4** fatiga `frequency>2.7/7d` o `CTR−30%` → rotar ≤14 d · **G5** reacción muda **≥70% en <5 palabras tras 0.5 s** · **G-conversión** share-to-wishlist **1:0.03–0.04 en frío**, **<0.02 tras 10 creadores → kill del beat**.
- **Primero a falsar por centavos (D-nota + G + A):** test de repetición del **grito mudo** + **`eyes_closed_test`** (INV-13, ≥75%) + **test del experto** (INV-16) + **solver S4–S7** (INV-1..5). Estos deciden si "foso legible", "audio de orden superior" y "ética terminable" son reales o aspiracionales ANTES de gastar en producción.

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

### 16.2 Estrategia comercial v1.3 — 1.0 directo, orgánico-primario (C, P2-14..20)
El 2.º ciclo (clúster C, consenso 3/3 triangulado) reencuadra el negocio: **ÓRDAGO NO es un negocio de UA pago a wishlist.** El **LTV B2P es casi constante** (~**$9.3** USA·hispanos / ~**$4.7** LATAM, neto-refund); **la única variable viva es el CAC**.

- **Gate #47 en 3 capas (C#47 / P2-14 🟡):** (1) **gate orgánico = ≥60% de las ventas de la Sem-1 desde wishlist orgánica-search**; (2) **paid marginal solo donde `CAC_pago ≤ LTV`**, con **LATAM paid-a-wishlist PROHIBIDO ($0)**; (3) **kill: blended LTV/CAC ≥3 O honesto ≥1.5 hispanos / ≥1.2 LATAM** — **lo zanja el CAC/CPWL medido en demo/Next Fest** (DC-15, [experimento]). Bandas WL→venta bimodales.
- **★ 1.0 DIRECTO + precio (C#46/#59 / P2-15 🟢, 3/3 triangulado · DC-13/DC-14 ★, [firma]):** **1.0 directo, $14.99 USD / $11.99 launch (−20%)**, regional **$7.49 LATAM** + **español 100% día 1** + disclaimer de impuestos AR (anti-review-bombing: 58–63% de las negativas LATAM = precio/idioma). **Única rama EA falsable:** si el balance exige **>5k jugadores simultáneos ∧ runway <4 meses** → EA táctico ≤6–9 m **con precio final desde día 1**. (Si LATAM cae a $4.99 por review-bombing → LTV-LATAM ~$3.0, pasa a 100% motor de volumen, no cruza-subsidia USA.)
- **Next Fest timing + retención de demo (C#36/#66 / P2-16 🟡):** demo viva **T-12 semanas**; **gate de entrada = velocity +150 WL/día sostenido 7 d** (no número fijo). Retención: **≥35% juegan >15 min**, **≥38% cruzan 2 h en 72 h** (no 55%); el jugador vive "el momento de la trampa" **antes del min 45**. Refund **<10% MX / <7% hispanos / <6% USA**; **<3% nota "muy difícil"**.
- **Banda de review como activo (C#45 / P2-17 🟢):** el escalón crítico es **Mixed→Mostly Positive (≥70%)**, no Very Positive ≥82%. Lift diferencial: **+22–35% conversión USA / +12–18% LATAM**. Las primeras 10 reviews se deciden en las **primeras 4 h** → soporte **24/7 en Discord la Sem-1**.
- **WL velocity > acumulado (C#58 / P2-18 🟡):** reportar **WL/día con fuente y cohorte**, no stock (la WL fría infla el numerador); umbral exacto → lo zanja el dato del algoritmo de Steam.
- **Tags + funnel Steam (P2-20 🟡):** tags = **Roguelike Deckbuilder + Rogue-lite + Dark Fantasy + Solitaire** (**NO "Card Game"**). La UA empuja a **buscar el nombre** (search directo pesa 5×). Penalizar el cuello móvil→PC (WhatsApp→Steam completion 12–18%); **gate >15% completan el deep-link o priorizar demo web jugable.**
- **Gates culturales medidos (C#30/#44/#43 / P2-19 🟡/⚪):** A/B Mito-ON/OFF gate **CTR ≥2.4% AND +15%** en hispanos-USA (48 h, afecta CTR/velocity, **NO retención D3**); reconocimiento "trampa al diablo con cartas" **<1.2 s en ≥70%** en 3 nodos (MX/Miami/Houston) × 3 variantes (MX/Caribe/Centro); decay de búsquedas de marca **<45% a 90 d** (el "70% a 36 m" del #43 se **degrada de hecho a hipótesis-con-KPI**, ⚪).
- **Discovery — diferir SEO-Engine (B#57 / P3-1 🟡):** diferir el Engine por-seed (riesgo thin-content/soft-404 Google 2026); construir **solo** el **medidor de Search Velocity** (gate centinela T-14 d, ~600–2,500/mes/región a calibrar) + **UNA landing-compendio estática** top-100 seeds (cron diario, $0).

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

### 18.1 Ética, anti-spam y reciprocidad EN CÓDIGO (v1.3, G#16/#37/#55/#15 — P1-13, P2-28..31)
La salud social deja de ser "buena intención" y pasa a invariantes de release:
- **Gobernador anti-spam que BLOQUEA, no alerta (G#37 / P1-13 🟢 [L1]):** **máx 2 envíos/contacto/semana**; el **3.º se auto-bloquea** sin respuesta previa. **El build no shippea si `block/mute ≥1.5%` o `report-spam ≥0.3%`.** Si K sube pero el grafo se silencia → **vetar la variante** (CX-3: G manda sobre el motor de K de B).
- **KPI maestro de saciedad (G#55 / P2-31 🟡):** `(share_reciprocidad / share_total) × (1 − block_rate)` → **>0.25 sano / <0.15 veto**. Ratio para-satisfecho-vs-encadena **>1.2** (umbral exacto = César).
- **Reciprocidad backend / TDF (G#16 / P2-28 🟢):** TDF/gift-back **solo backend** para matchmaking silencioso; **prohibido por código** exponer deuda/contador/shaming; el sticker dice "Pasamos la Mano" **sin contador**. Gate: **TDF ≥30% gift-back/72 h** (🟡 28–34%); <25% revisar; ~0 → el bonding no existe.
- **Bucket social cerrado (G#15 / P2-29 🟢):** ~50 pares reales del mismo percentil; Diablo Fantasma poblado por **PAR REAL** (nunca #global ni bot); sin leaderboard global público; **auditar 0 Diablos Fantasma sintéticos**; prohibido re-barajar (50→30) para retener.
- **K_rivalidad ≠ K_reciprocidad (G#38 / P2-30 🟡):** medir por segmento (**0.45–0.62** vs **0.12–0.18**, L1 Meta); claim "Community" condicionado a **k-reciprocidad ≥0.20 a 4 sem** (§8.1).
> 🔶 **Decisiones de César abiertas (G):** umbral de reciprocidad / ratio para-satisfecho (DC-28, dirección converge, número no — empezar conservador y endurecer, **calibrar por A/B solo el umbral, NUNCA la dirección del veto**); atenuar el arrepentimiento en las runs 1–3 de onboarding (DC-31, Meta +18% churn D7 por vergüenza LATAM vs Opus/Gemini rigor desde el min 1).

---

## 19. Riesgos y decisiones

### 19.1 Riesgos
| Riesgo | Severidad | Mitigación |
|---|---|---|
| **El verbo es puzzle, no decisión (el foso no existe)** | Alta (el riesgo clave) | **Solver de papel (§14)** antes de un píxel; kill = pivotar de género |
| **El artefacto-puente no cruza el chat (viralidad humo)** | Alta | §8.3 sticker autocontenido (golpe sin click) + glance-gate ≥90% + K2 = activación atribuible, no reenvíos |
| **El click <5% en chat familiar mata el deep-link del sticker** | Alta (v1.3) | §8.3: deep-link al caption, no dentro del sticker; clip = encendedor en Reels/IG |
| **Audio asumido (juego ilegible en mute = default 85–90% LATAM)** | Alta (v1.3) | §19.4: `state_is_visual_complete`, test `mute_total` 100% binario, lint `no_bare_audio_emit` |
| **Daño social (spam/shaming) por optimizar K** | Media (v1.3) | §4.1/§18.1: veto goodwill bloqueante + gobernador anti-spam que bloquea; no escalar si block/mute ≥1.5% |
| **Money-shot deriva en live-ops encubierto** | Media (v1.3) | §10.2: cap G3 ≤0.8 d-h/dosis, casta doble, justificado por share no por retención |
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
- **Resueltas en v1.3 (consenso 3/3):** ✅ **1.0 directo a Steam** (orgánico-primario, no UA-pago; §16.2) · ✅ **Sticker autocontenido = puente PRIMARIO, clip = encendedor** (§8.3) · ✅ **Tells = predicado, no sujeto** (foso en el OUTPUT retrospectivo; §11.1) · ✅ **`state_is_visual_complete`** (visual-primario, audio-amplificador; §3.4/§19.4) · ✅ **Veto goodwill bloqueante + gobernador anti-spam en código** (§4.1/§18.1) · ✅ **Money-shot = motor único + slot, casta doble, cap G3 ≤0.8 d-h/dosis** (§10.2) · ✅ **Codex de Arrepentimientos terminable** (§9.x) · ✅ **Bucket social ~50 pares reales, 0 sintéticos** (§8.1).

### 19.3 Decisiones aún abiertas (para César) — 32 consolidadas del 2.º ciclo
> Lista única deduplicada de los 7 clústeres. **[experimento]** = lo zanja el dato/playtest; **[firma]** = apetito/principio del autor. Las **★** son las de mayor apalancamiento. No se presentan como cerradas.
>
> **★ Actualización (v1.3.1 — debate de RESOLUCIÓN de decisiones, 3 sub-debates multi-IA H1/H2/H3):** 22 de estas decisiones se llevaron a un debate de seguimiento que las forzó a una recomendación firme. Resultado: **12 a consenso 3/3, 5 a mayoría 2/3, 2 contestadas→experimento**; el resto sigue como firma del autor. La tabla maestra y los criterios kill están en `docs/research/2026-06-25-ordago-decisiones-resueltas/DECISIONES-RESUELTAS.md`. Ver §19.3.1.

### 19.3.1 Resoluciones del debate de decisiones (v1.3.1)
> Cada DC con la recomendación CONVERGIDA. Estado: 🟢 consenso 3/3 · 🟡 mayoría 2/3 · 🧪 experimento pre-comprometido · ✍️ sigue firma del autor.

**Onboarding/Codex/progresión (H1):**
- **DC-4 🟢** → **tutorial serializado de 7 reglas core / ≤5 verbalizadas en Manga 1**, Pactos por compresión-arquetipo en mangas 2-3; NO podar. *Kill: ejecución de Pacto ≥80% ∧ ≤5 verbalizadas ∧ time-to-win p50 ≤165 s.*
- **DC-5 🟡🧪** → **run continuo [25-35] min + auto-save por turno + victoria-parcial por manga** (híbrido). *Lo cierra A/B resume-rate 24 h ≥65%; si las "paredes" ganan ≥3 pp → capítulos.*
- **DC-6 🟢** → **N=12 / M=18** con capas de revelación por entrada (no abierto, no 16). *Sube a 16 solo si logra ≥7% completado D30 ∧ abandono 80-99% <5%.*
- **DC-8 🟢** → recompensa del 100% del Codex **estrictamente estética** (boss-en-solver prohibido por elegancia).
- **DC-9 🟢** → **hook 90 s p50**, banda-muerte >120 s; comprensión 1.ª jugada ≥85%.
- **DC-11 🟢** → **podar Diablo Fantasma + artefacto-puente del onboarding**; meta gateado tras Manga 1-2 + teaser silueta; nunca regla verbal antes de Manga 1.

**Entrega viral/audio/assets (H2):**
- **DC-16 🟡✍️** → **cero-backend, atribución 100% localStorage** (preserva el moat "0 servidor"); *del que cuelga DC-20.* Sigue firma (moat vs medibilidad).
- **DC-18 🟢** → **diferir el SEO-Engine**; solo landing-compendio estática + centinela de Search Velocity ≥600/región/4 sem (riesgo Core Update 2026 deindexa páginas programáticas).
- **DC-20 🟡** → reparto **60/25/15** (sticker/clip/atribución).
- **DC-21 🟢** → **3 nodos de grito: MX + Caribe + US-Centroamericano** (NO Rioplatense; +2.1× share justifica el 3× costo).
- **DC-22 🟡** → **lanzar la Textura de Sospecha COMPLETA con techo en código día 1** (`gain ≤0.8*master`, banda ∉ [500 Hz, 2 kHz]).
- **DC-23/24 🟢** → grito_glifo en **imagen + caption copiable estático**; emoji-artefacto **línea estática garantizada + 1 evento analítico**.
- **DC-25 🟢** → **5 money-shots full**, expansión 6-8 solo bajo doble gate G2/G3, **tope duro 8** (no 20).
- **DC-26 🟢** → **3 plantillas** de concepto (no 4); budget al Diablo jugable físico (cerámica/tinta), no a fidelidad de render.
- **DC-27 🟢** → **sin Condena endless como fuente de dosis de awe en 1.0**.

**Ética/Pactos/feel (H3) — los vetos éticos son inviolables; el debate calibró solo magnitud:**
- **DC-1 🟡🧪✍️** → **híbrido**: motor emergente por default + **cicatriz acoplada en 2-3 Pactos-ancla**. *Kill: recall run-1 ≥60% ∧ dominant_build_share <0.25.* El casting de los Pactos-ancla sigue firma.
- **DC-3 🟢** → **suerte gobierna el top-funnel (~70/30 en creatividades), skill gobierna el loop y ~100% del LTV/D30**.
- **DC-28 🟡✍️** → reciprocidad **arranque 0.25, calibrar al alza** (A/B saciedad ≥0.18 ∧ block <1.2%); el número fino (0.25↔0.22) sigue firma.
- **DC-29 🟢** → **epitafio post-run diferido, NUNCA mid-run**; carta, no número. *Kill: re-run<3 s ≤13%.*
- **DC-30 🟢** → **veto goodwill bloqueante** (invariante de compilación; CI rollback si block/mute ≥1.5%).
- **DC-31 🟢** → arrepentimiento: **frecuencia OFF (hasta 0%) en runs 1-3, texto/Romancero intactos siempre**. *Kill: churn D7 ≤38%.*
- **DC-32 🟡✍️** → epitafio **delay 1.5 s skipeable desde el frame 1** (A/B 3 celdas, aceptar solo si re-run<3 s ≤13%); la affordance fina (skipeable vs 0 s+botón) sigue firma.

**Siguen siendo FIRMA irreducible del autor (con el default sugerido del panel):** DC-16 (cero-backend vs beacon), casting de los Pactos-ancla de DC-1, affordance del epitafio DC-32, número fino de reciprocidad DC-28, **+ las heredadas de v1.2** (título, dirección de arte, cosmología de palos, multi-nodo cultural, recuperabilidad de Pactos, ¿AZOTH o ÓRDAGO primero?). Los **[experimento]** puros (banda EV DC-2, umbral K2 DC-17, LTV/CAC DC-15) los zanja el solver/CAC medido, no el debate.

**Heredadas de v1.2 (siguen abiertas):**
1. 🔶 **Banda exacta de spread de EV (§7.3/§14)** — la zanja el **solver de papel** ([10–15%], las 3 bandas solapan en [12%,13%]). *Primera cosa a falsar.* **[experimento].**
2. 🔶 **Dirección de arte (§11)** — A/B de feed con glance gate; no cerrar por intuición. **[firma].**
3. 🔶 **Título** — ÓRDAGO vs EL ENVITE / LA PARTIDA (cruza con el nodo cultural C-3). **[firma].**
4. 🔶 **Cosmología de palos (§7.1)** — fuertes vs ligeras (rec.: fuertes). **[firma].**
5. 🔶 **Multi-nodo cultural (C-3)** — interfaz `cultural_packs[]` día 1 + 1 pack MX profundo; resto post-EA. **[firma].**
6. 🔶 **Recuperabilidad de Pactos** — variante rara, no regla base. **[firma].**
7. 🔶 **¿AZOTH o ÓRDAGO primero?** — ÓRDAGO tiene cuña comercial más clara y barata; AZOTH mayor techo de distinción global. **[firma].**

**Economía y foso (A):**
8. 🔶 **Apetito de auto-sabotaje en Pactos (DC-1, §7.6)** — emergente (confiar en S4-verde) vs acoplado-a-mano (Pacto auto-saboteador ↔ Fullería que destraba). **[firma].**
9. 🔶 **Banda de EV objetivo (DC-2)** — delegada al solver; César fija el número viendo 100 tableros/seed. **[experimento].**
10. 🔶 **Dial revelar↔ocultar / suerte↔skill (DC-3)** — secuencia (suerte en marketing, skill en loop); el peso de cada capa es apetito de César. **[firma].**

**Onboarding y carga (E):**
11. 🔶 **Denominador de onboarding (DC-4, §13)** — ≤5 reglas podando Pactos vs tutorial serializado de 7 reglas en 3 micro-mangas. **Reco del panel: serializar.** **[firma].**
12. 🔶 **Run continuo vs capítulos (DC-5, §9.1)** — run continua + auto-save por turno vs 4 mangas con save entre mangas. **[firma].**
13. 🔶 **Cardinalidad del Codex N/M (DC-6, §8/§13)** — N=16/M=24 (Gemini) vs N=12/M=18 (Meta L1🟢) vs abierto (Opus ⚪). **[firma, sesgo a Meta por L1].**
14. 🔶 **Serialización de cascadas (DC-7)** — 100% Z3+ vs 1 solape Z3/run; resuelto para el money-shot (CX-4), abierto solo para solape DENTRO del loop. **[firma].**
15. 🔶 **Recompensa del 100% del Codex (DC-8)** — estrictamente estética vs desbloquea Diablo Fantasma como boss mecánico. **[firma].**
16. 🔶 **Hook 90 s vs 120 s (DC-9)** — casi resuelto en 90 s; cada 30 s = trade-off D1 vs feel/setup. **[firma].**
17. 🔶 **Biblia del Mundo (DC-10)** — ¿validar teorías de comunidad en updates o mantener hermética? **[firma].**
18. 🔶 **Poda de Diablo Fantasma + artefacto-puente del onboarding (DC-11)** — ¿podarlos del onboarding manteniéndolos como meta gateado? **[firma].**
19. 🔶 **¿Tease altera el seed de mañana o es cosmético? (DC-12)** — **[firma + experimento del lift].**

**Comercial (C):**
20. 🔶 **★ EA vs 1.0 → 1.0 DIRECTO ★ (DC-13, §16.2)** — unánime 3/3, triangulado. Única excepción: balance exige >5k simultáneos ∧ runway <4 m → EA táctico ≤6–9 m con precio final desde día 1. **[firma, reco fuerte 1.0].**
21. 🔶 **★ Precio ★ (DC-14, §16.2)** — $14.99 / $11.99 launch / $7.49 LATAM + español día 1 + disclaimer AR. **[firma].**
22. 🔶 **Umbral honesto del gate LTV/CAC (DC-15)** — ≥3 blended vs ≥1.5 hispanos/≥1.2 LATAM. **Lo zanja el CAC/CPWL medido en demo/Next Fest.** **[experimento].**

**Artefacto-puente (B):**
23. 🔶 **Beacon stateless vs cero-backend (DC-16)** — 1 endpoint stateless (medible) vs 0 servidor (atribución local, "0 servidor" como moat). **[firma].**
24. 🔶 **Umbral VERDE de K2 (DC-17)** — 3/100 (Opus) vs 0.18 (Meta); medir activación, no reenvíos. **[experimento real de tasa partida-desde-sticker LATAM].**
25. 🔶 **SEO Engine por-seed ahora (DC-18)** — diferir (reco 2/3); construir solo medidor de Search Velocity + landing-compendio. **[firma, reco diferir].**
26. 🔶 **Pre-compromiso si K2 sale KILL (DC-19)** — el fix es de PRODUCTO (sticker no autocontenido), no de copy; definirlo ANTES evita racionalizar. **[firma].**
27. 🔶 **Reparto sticker/clip (DC-20)** — ~60–70% sticker (Meta 60/25/15 vs Opus 70/30). **[firma].**

**Audio (D):**
28. 🔶 **★ Nº de nodos de grito 2 vs 3 y CUÁLES (DC-21, §19.4) ★** — 2 nodos (Opus MX+Caribe / Gemini MX+Rioplatense-AR por ancestro Truco) vs 3 nodos (Meta L1 MX+Caribe+US-Centroamericano, +2.1× share justifica 3× costo). **Reco: si 2 → MX+AR; si 3 → MX+AR+Caribe.** **[firma].** *(Única sin evidencia que la zanje.)*
29. 🔶 **Textura de Sospecha completa al lanzamiento (con techo) vs MVP diferido (DC-22)** — reco: completa con techo gain+banda. **[firma].**
30. 🔶 **grito_glifo en caption copiable además de la imagen (DC-23)** — reco: ambos. **[firma].**
31. 🔶 **Emoji-artefacto: UI copiable dinámica vs línea estática garantizada (DC-24)** — reco: línea garantizada + 1 evento analítico. **[firma].**

**Awe (F) y Ética (G):**
32. 🔶 **Nº de money-shots full (DC-25, §10.2)**: 5 + medir G2, subir a 6.º–8.º solo si superan G2/G3 — **no 20** · **Reparto de arte (DC-26)** al beat+sonido y al Diablo jugable · **¿Condena suma dosis? (DC-27)** solo si G3 aguanta · **Umbral de reciprocidad (DC-28)** dirección converge, número no — A/B solo el umbral · **Susurro mid-run vs epitafio (DC-29)** lo zanja `re-run<3s` · **Veto goodwill bloqueante vs advisory (DC-30)** reco 3/3 bloqueante · **Atenuar arrepentimiento runs 1–3 (DC-31)** · **Delay forzado ~1.5 s en epitafio (DC-32)** lo zanja la métrica. **[firma + métrica].**

### 19.4 Arquitectura de audio y accesibilidad (NUEVO — v1.3, D + B#22 · P1-10/P1-11, P2-9..13)
Bajo la doctrina **`state_is_visual_complete`** (§3.4): el juego es **100% legible en silencio** (mute=default 85–90% LATAM); el audio **amplifica, nunca porta** información.
- **Emisor simétrico no-nullable (D#67 / P1-10 🟢, WCAG 1.3.3 + Xbox XAG 103):** todo cue de estado se emite por `emitStateCue(visual, audio)` con **`visual` no-nullable**; lint **`no_bare_audio_emit`**; test **`mute_total`** corre la suite con `master=0` y **el 100% de los eventos producen un cambio visual o falla el build** (binario).
- **Doctrina `state_is_visual_complete` (D#32 / P1-11 🟢):** el oracle `mute_total` pasa al 100% **ANTES** de que cualquier capa de audio de estado entre a producción.
- **Audio de estado — 3 capas con techo (D#32 / P2-12 🟢/🟡):** (1) **leitmotiv de Trampa** en loop ≤ −18 LUFS; (2) **textura de Sospecha** con curva log que **satura al 80% de gain en `suspicion=0.7`** (invariante `suspicion_audio_gain ≤ 0.8*master`); (3) **3 firmas de resultado** ≤1.2–1.5 s. **Techo de banda: la Sospecha ∉ [500 Hz, 2 kHz]** (no enmascara voz/música). **`audio_layers_active ≤ 2`.** Gate **`eyes_closed_test ≥75%`** (kill <60%). **KPI ético `quit_rate ≤ baseline`; PROHIBIDO medir `Cheating_Success_Rate`** (sería pay-to-hear).
- **Firma de identidad (D#22 / P2-10 🟢):** firma 2–3 s **inline ≤35 KB, precargada en el 1.er frame**; `AudioContext.resume()` en el handler del 1.er evento semántico. KPI **`firma_heard_first_session` ≥58% Android / ≥38% iOS-MX** (kill <45%/<30%). North-star de negocio: medido pero **no bloqueante**.
- **WKWebView / autoplay (B#22 / D#22 / P2-9 🟢):** **muted+playsinline**, audio se arma en el 1.er evento semántico (no tap accidental), demo <1.5 s, linters `no_autoplay_without_gesture` / `first_tap_arms_audio`, fallback flash+vibración si `play()` falla.
- **`grito_glifo` en el sticker (D#23 / P2-11 🟢/🟡):** campo **no-null** en `RunDigest` (linter `digest_has_grito_glifo`); gemelo visual onomatopéyico **Posada estampado en el arte** (no sello pegado), **≤2 palabras legibles a 96×96 px** (OCR-gate `glifo_ocr_legible`), contraste ≥4.5:1. KPI: reenvío +15%, repetición ≥20% <48 h, bloqueo <0.25%.
- **`text_glyph` emoji-artefacto (D#17 / P2-13 🟢/⚪):** `RunDigest.text_glyph` siempre presente y copiable (`🃏👹🔥 … ¡ÓRDAGO!`); KPI **separado** `text_glyph_share_rate` **≥4% sem-1**; degradar a fallback silencioso si <1.0 jugada/10 shares. **Nunca se mata** (costo ~0): es red de seguridad (23% de sesiones MX sin datos), **NO un 3.er canal**.
- **Multi-nodo de grito como DATA (D / §19.3-DC-21):** `cultural_packs[node].grito = {audio, glifo, locale}` + fallback default; **el nº de nodos (2 vs 3) es decisión de César.**

### 19.5 Guardarraíles éticos — los 10 "NUNCA" (NUEVO — v1.3, G + D, inviolables por código)
> De G (3 fixes rechazados + corolarios), reforzado por D. **No son recomendaciones: son invariantes de compilación/release.**
1. **NUNCA un bot falso** ("Pacto/Diablo Compasivo") disfrazado de ayuda humana (falsa prueba social). Si César quiere asistencia, debe ser un NPC del Romancero **claramente identificado como bot** — transparencia, no engaño.
2. **NUNCA un sticker de burla NOMINAL a un humano.** Burla AL DIABLO (enemigo común) = depósito; burla a tu primo nombrado = withdraw tóxico.
3. **NUNCA estrechar el bucket dinámicamente (50→30) para retener** (ansiedad manufacturada).
4. **NUNCA exponer deuda individual** como HUD/contador/shaming (#16).
5. **NUNCA CTA / ad / oferta / ranking post-derrota** (#70): no se monetiza la frustración.
6. **NUNCA números/EV en el arrepentimiento** — mostrar la carta, no la cifra (#41).
7. **NUNCA "liberar slot de Maña por cooperación"** — rompe el trade-off faustiano §7.6d.
8. **NUNCA medir `Cheating_Success_Rate`** ni atar el audio a la tasa de éxito de fullerías (sería pay-to-hear, rompe fairness) (D#32).
9. **NUNCA escalar una variante que sube K si el grafo se silencia** (block/mute ≥1.5%) — vetar, no escalar (#37/#42).
10. **NUNCA asumir audio** — todo evento de estado debe ser legible en mute (D#67).

---

*Fin del macro GDD v1.3. Siguiente paso lógico: (1) el **solver de papel** del generador de bifurcación con los pasos **S4–S7** (§14.0) — valida o mata el foso, la dominancia de Maña y el escalado del umbral del Diablo por un finde, ANTES de un píxel; (2) el **micro-GDD del prototipo** — las ~3 Trampas + 3 Fullerías + 3 Pactos concretos con números, las reglas de siembra de la Mesa viva, las matas con sus valores, los umbrales de la primera Manga, y el spec del `RunDigest` → ficha-sticker autocontenida (`grito_glifo`, `text_glyph`) + emisor `emitStateCue(visual, audio)`. Plan maestro de este ciclo: `docs/research/2026-06-25-ordago-debate-diseno-v2/META-SINTESIS-v1.3.md`.*
