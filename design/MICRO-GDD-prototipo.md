# ÓRDAGO — Micro-GDD del prototipo (números concretos para el solver + el vertical slice)

> Instancia el GDD macro v1.3.2 (§7, §14) en **números falsables**. Es la fuente de verdad del
> contenido del prototipo. El solver de papel (`solver/ordago_solver.py`) implementa EXACTAMENTE
> estos números; el prototipo web (`game/`) los reusa vía `game/src/content.js`.
> Orden de falsación (GDD §14): **el solver valida/mata el foso ANTES de un píxel.**

---

## 1. La baraja (40 cartas)

Baraja española: 4 palos × 10 valores. Sin 8 ni 9 físicos; las figuras valen para el Escoba:
- **Valores de Escoba (`v`)**: 1,2,3,4,5,6,7, **Sota=8, Caballo=9, Rey=10**.
- **Palos**: 🪙 Oros (O), 🍷 Copas (C), ⚔️ Espadas (E), 🌳 Bastos (B).
- **`puntos_base`** (peso de puntuación): cartas normales = `v`. **Matas** (legendarias, §7.5) con base alta:

| Mata | Palo | `v` | `puntos_base` | Efecto |
|---|---|---|---|---|
| As de Espadas | E | 1 | 28 | la más alta; ×1.3 Suerte al capturarla |
| As de Bastos | B | 1 | 22 | +10 Puntos en bloque |
| Siete de Espadas | E | 7 | 18 | cuenta como Espada para Pactos de filo |
| Siete de Oros | O | 7 | 16 | genera 2 Reales al capturarla |

(El público hispano las reconoce sin tutorial; el global las descubre por captura — §7.5.)

## 2. El verbo: Escoba sobre Mesa viva

- **Objetivo (`target`)**: sumar **15** con (1 carta de tu mano) + (subconjunto de la Mesa). Captura = *Escoba*.
- Cada turno juegas **1 carta de la mano**; capturas el subconjunto de Mesa que con ella suma `target`.
- Si tras la captura la **Mesa queda vacía** → **Escoba limpia**: +5 Puntos bonus.
- Si ninguna jugada suma `target`, juegas una carta "a la Mesa" (la dejas; no puntúa) y pasas turno.

### 2.1 Puntuación: Puntos × Suerte (§7.7)
- `Puntos` (azul) = Σ `puntos_base` de cartas capturadas (+ bonus de Escoba limpia + Pactos aditivos).
- `Suerte` (rojo) = multiplicador, arranca en **1.0**; los Pactos/Matas ×Suerte lo elevan (orden izq→der).
- **Score de la jugada = `Puntos × Suerte`**. El score de la apuesta = Σ de jugadas hasta agotar manos.

### 2.2 Los tres ejes de decisión (§7.3 — el generador de bifurcación)
Cada Escoba candidata se evalúa en 3 ejes que **no** se maximizan a la vez:
- **Tempo** = Puntos que anota YA (Σ puntos_base capturados, × Suerte actual).
- **Escala** = valor futuro hacia TU build: Σ sobre cartas capturadas de su *afinidad* con el/los Pacto(s) equipados (p.ej. Oros si llevas Pacto del Oro). Alimenta el motor, puntúa poco ahora.
- **Defensa** = peligro negado al Diablo: Σ `danger` de cartas capturadas + bonus si dejas la Mesa vacía (le niegas material de Carnada/Bloqueo). `danger(carta)` = alto para Matas y para cartas que habilitan la siembra-Carnada del Diablo.

**Postcondición de siembra (INVARIANTE, §7.3.2):** tras sembrar, la Mesa DEBE admitir **≥2 jugadas Pareto-no-dominadas** en (tempo, escala, defensa). Si no → **re-siembra acotada ≤8 intentos** sobre ejes. Siembra **100% determinista por seed**.

**Banda de spread de EV (§7.3.3 — a falsar por el solver, no por argumento):** el spread entre la mejor y la 2ª jugada Pareto (en EV escalar situacional) debe caer en **[10%, 15%]** (objetivo). `<8%` = ajedrez seco; `>18%` = autorrevela. **El número final lo fija el solver.**

## 3. Trampas ↔ Fullerías ↔ Pactos (el sistema dual, §7.6)

### 3.1 Las 3 Trampas del Diablo (en cada Envite)
| id | Nombre | Efecto sobre el verbo | Fullería que la rompe |
|---|---|---|---|
| T1 | **El Trece** | `target` baja a **13** esta Manga | F1 Lectura Falsa |
| T2 | **Oros Malditos** | las cartas de **Oros no pueden** usarse en capturas | F2 Contrabando |
| T3 | **Primer Robo Nulo** | la **1.ª Escoba del Envite puntúa 0** | F3 Doble Filo |

### 3.2 Las 3 Fullerías (tu maña — ocupan ranura de Maña)
| id | Nombre | Efecto | Rompe |
|---|---|---|---|
| F1 | **Lectura Falsa** | 1×/Manga: una figura se lee como CUALQUIER `v∈[1,10]` que elijas | T1 (y abre composición) |
| F2 | **Contrabando** | permite usar **1 Oro** en captura pese a la Trampa; +1 carta de Mesa robable | T2 |
| F3 | **Doble Filo** | tu **1.ª Escoba del Envite puntúa ×2** | T3 |
| F0 | **Ojo del Tahúr** (maestría) | resalta jugadas que suman target (solucionador parcial) | — (no de Envite) |

### 3.3 Los 3 Pactos Oscuros (poder pasivo — ocupan ranura de Maña toda la run)
| id | Nombre | Afinidad | Efecto |
|---|---|---|---|
| P1 | **Pacto del Oro** | 🪙 Oros | **+3 Puntos** por cada Oro capturado en la Escoba |
| P2 | **Pacto del Filo** | ⚔️ Espadas | **×1.4 Suerte** si la Escoba incluye ≥1 Espada |
| P3 | **Pacto del Bosque** | 🌳 Bastos | **+2 Puntos** por cada carta capturada (premia barridos grandes) |

> **Complementariedad Pacto↔Fullería (P1-6, §7.3):** existe ≥1 estado de Mesa con `EV(Pacto) > EV(Fullería)`; viabilidad de tomar Pacto ∈ [20%, 50%]; ninguna Fullería domina en >85% de seeds. **Lo verifica el solver.**

### 3.4 La economía de Maña (§7.6d)
- **3 ranuras**. Cada ranura = **1 Fullería O 1 Pacto**. Tomar un Pacto ocupa la ranura toda la run.
- Builds extremas a falsar (S4): **0F/3P**, **3F/0P**, **2P/1F**, **1P/2F**.
- Auto-balance: la Trampa del Envite escala para que jugar sin maña (0 Fullerías) duela.

## 4. Estructura: La Partida (prototipo = Manga 1 completa)

- **Manga = 3 apuestas**: chica → grande → **Envite** (boss con Trampa). Prototipo: **Manga 1**.
- **Umbrales del Diablo (Manga 1)** — a calibrar por el solver (S5, ratio score/umbral ∈ [0.95,1.15]):
  - Apuesta **chica**: umbral **30**, manos disponibles **5**.
  - Apuesta **grande**: umbral **55**, manos **6**.
  - **Envite** (Trampa activa): umbral **85**, manos **7**.
- Mesa inicial: **4 cartas**; cada turno el Diablo siembra hasta mantener **5–6** cartas en Mesa.
- Mano del jugador: **3 cartas**, repón a 3 tras cada turno (mientras haya mazo).

## 5. `RunDigest` → ficha-sticker (§8.3 — spec mínima para el prototipo)
Fuente única serializada al terminar la run (cliente, 0 servidor):
```
RunDigest = {
  seed, resultado: "ganó"|"perdió", manga_alcanzada,
  mejor_escoba: int, trampas_rotas: int, margen: int,
  arquetipo: string (2 palabras, derivado de la build: "Escobero del Oro"...),
  grito_glifo: string (no-null, ≤2 palabras Posada), text_glyph: string (emoji copiable),
  constraint_flags: [ "0_fullerias" | "escoba_perfecta" | "sin_pacto_corrompido" | ... ]
}
```

## 6. Gates del solver (§14.0 — VERDE/AMARILLO/KILL)
El solver corre y reporta:
- **Pareto postcondición**: ≥2 jugadas Pareto-no-dominadas en ≥95/100 tableros.
- **Banda EV**: spread mejor↔2ª Pareto en [10%,15%] (mediana).
- **S4 Dominancia de Maña**: 🟢 ninguna build >55% winrate ∧ Sharpe <1.3× la 2ª · 🔴 KILL >60% o Sharpe >1.5×.
- **S5 Escalado del umbral**: mediana `score/umbral` ∈ [0.95,1.15], p10>0.8, p90<1.6 = 🟢.
- **S6 Composabilidad**: working-set ≤6 reglas en >70% de builds óptimas; "Ojo del Tahúr" no en >85%.
- **S7 FTUE/Maestría**: FTUE ≥1 dominante-tempo (spread <8%); Maestría ≥2 Pareto en banda.
- **Test del experto**: `bot_lookahead_k − bot_greedy_1ply` crece monótono con k; KILL si se aplana a k≥2.
- **KILL de cimiento**: si >20% de tableros converge a 1 jugada dominante → el verbo es puzzle → pivotar.

*Estos números son la hipótesis del autor anclada al GDD; el solver los confirma o los mata.*
