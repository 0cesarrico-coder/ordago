"""
ÓRDAGO — Motor del solver de papel (§14.0).
Mecánica determinista, desacoplada de render: enumeración de jugadas, puntuación
Puntos×Suerte con motor de Pactos (acumuladores de run), ejes (tempo/escala/defensa),
Pareto, EV situacional y políticas de bot (greedy-1ply / greedy-EV / lookahead-k).

El render (game/) NO vive aquí. Esto es headless → simulación Monte Carlo gratis.
"""
from __future__ import annotations
import random
from dataclasses import dataclass, field
from itertools import combinations
from content import (
    construir_baraja, PACTOS, FULLERIAS, TRAMPAS, OROS, ESPADAS, BASTOS,
    TARGET_BASE, ESCOBA_LIMPIA_BONUS, MESA_INICIAL, MESA_MIN, MESA_MAX, MANO_TAM,
    TRAMPA_PENALTY, TRAMPA_F3_BONUS, ESCOBA_BONUS_FLAT,
)


# ----------------------------- Build helpers --------------------------------
def build_info(build):
    """build = lista de ids (Pactos y/o Fullerías). Devuelve sets/flags útiles."""
    pactos = [b for b in build if b in PACTOS]
    fullerias = [b for b in build if b in FULLERIAS]
    n_full_break = sum(1 for f in fullerias if FULLERIAS[f]["rompe"])
    return {
        "pactos": pactos,
        "fullerias": fullerias,
        "tiene_P1": "P1_oro" in pactos,
        "tiene_P2": "P2_filo" in pactos,
        "tiene_P3": "P3_bosque" in pactos,
        "rompe": {FULLERIAS[f]["rompe"] for f in fullerias if FULLERIAS[f]["rompe"]},
        "tiene_ojo": "F0_ojo" in fullerias,
        "n_full_break": n_full_break,   # nº de Fullerías que rompen Trampas (utilidad universal)
    }


@dataclass
class RunState:
    """Acumuladores de motor por run (la Escala = crecimiento de estos)."""
    veta_oro: int = 0          # P1: +1 por Oro capturado → +veta Puntos por escoba futura
    bloque_bosque: int = 0     # P3: +1 por Basto capturado → +bloque Puntos por escoba futura
    suerte_filo: float = 0.0   # P2: +0.1 por Espada capturada → +Suerte base por run
    primera_escoba_envite_hecha: bool = False


# ----------------------------- Trampa context -------------------------------
def trampa_context(trampa_id, bi):
    """Modelo de PENALIZACIÓN (§7.6d auto-balance): comer la Trampa en crudo (sin la
    Fullería que la rompe) cuesta ×TRAMPA_PENALTY al Envite. Romperla = sin penalización
    (y un pequeño bonus para Doble Filo). El detalle mecánico (target 13, Oros bloqueados…)
    vive en el prototipo; aquí modelamos su EFECTO NETO sobre el trade-off de slots."""
    if trampa_id is None:
        return dict(target=TARGET_BASE, oros_bloqueados=False, activa=False, penalty=1.0)
    roto = trampa_id in bi["rompe"]
    # Penalización PROGRESIVA (sin cliff): comer la Trampa cuesta menos cuantas más
    # Fullerías llevas (maña general); romperla con la exacta = sin penalización.
    if roto:
        penalty = TRAMPA_F3_BONUS if trampa_id == "T3_primer_nulo" else 1.0
    else:
        penalty = min(0.95, TRAMPA_PENALTY + 0.11 * bi["n_full_break"])
    return dict(target=TARGET_BASE, oros_bloqueados=False, activa=True, penalty=penalty)


# ----------------------------- Play enumeration -----------------------------
@dataclass(frozen=True)
class Play:
    hand_idx: int
    subset_idx: tuple           # índices en la mesa capturados
    captured: tuple             # cartas capturadas (hand card + subset)
    empties_mesa: bool


def enumerate_plays(hand, mesa, tctx, bi):
    """Todas las capturas legales: 1 carta de mano + subconjunto de Mesa que suma target."""
    target = tctx["target"]
    oros_bloq = tctx["oros_bloqueados"]
    plays = []
    # mesa usable (excluye Oros si bloqueados)
    usable_mesa = [i for i, c in enumerate(mesa)
                   if not (oros_bloq and c.palo == OROS)]
    for hi, hc in enumerate(hand):
        if oros_bloq and hc.palo == OROS:
            continue
        # valores posibles de la carta de mano (F1 comodín en figuras)
        hvals = {hc.v}
        if "F1_lectura_falsa" in bi["fullerias"] and hc.v >= 8:
            hvals = set(range(1, 11))   # figura comodín
        for hv in hvals:
            need = target - hv
            if need < 0:
                continue
            if need == 0:
                plays.append(_mk_play(hi, (), hc, mesa))
                continue
            # subconjuntos de la mesa usable que suman need
            for r in range(1, len(usable_mesa) + 1):
                for combo in combinations(usable_mesa, r):
                    if sum(mesa[i].v for i in combo) == need:
                        plays.append(_mk_play(hi, combo, hc, mesa))
    # dedup por (hand_idx, subset)
    seen = {}
    for p in plays:
        seen[(p.hand_idx, p.subset_idx)] = p
    return list(seen.values())


def _mk_play(hi, combo, hc, mesa):
    captured = (hc,) + tuple(mesa[i] for i in combo)
    empties = len(combo) == len(mesa)
    return Play(hand_idx=hi, subset_idx=tuple(sorted(combo)),
                captured=captured, empties_mesa=empties)


# ----------------------------- Scoring --------------------------------------
def score_play(play, rs: RunState, bi, tctx, primera_del_envite=False):
    """Devuelve dict con score, puntos, suerte y ejes (tempo/escala/defensa).
    NO muta rs (eso lo hace apply_play)."""
    cap = play.captured
    oros = sum(1 for c in cap if c.palo == OROS)
    espadas = sum(1 for c in cap if c.palo == ESPADAS)
    bastos = sum(1 for c in cap if c.palo == BASTOS)
    matas = [c for c in cap if c.mata]

    puntos = sum(c.puntos_base for c in cap) + ESCOBA_BONUS_FLAT
    if play.empties_mesa:
        puntos += ESCOBA_LIMPIA_BONUS
    # BASELINE SIMÉTRICO POR SLOT: cada Maña equipada (Pacto O Fullería) da +3/escoba.
    # Así el baseline total ≈ constante (3 slots) sin importar el mix → comprime el poder
    # entre builds. La diferencia entre builds vive SOLO en los efectos secundarios:
    #   Pacto = escala/motor (afinidad, premia previsión) · Fullería = mitigación de Trampa.
    puntos += 3 * len(bi["pactos"])
    puntos += 5 * bi["n_full_break"]   # Fullería: más baseline (no tiene motor/escala que el Pacto sí)
    # secundarios de Pacto (condicionales, modestos)
    if bi["tiene_P1"]:
        puntos += 1 * oros
    if bi["tiene_P3"]:
        puntos += 1 * len(cap)
    if any(m.mata == "as_bastos" for m in matas):
        puntos += 4
    # engine adds (acumulado ANTES de esta captura)
    if bi["tiene_P1"]:
        puntos += rs.veta_oro
    if bi["tiene_P3"]:
        puntos += rs.bloque_bosque

    suerte = 1.0
    if bi["tiene_P2"]:
        suerte += min(rs.suerte_filo, 0.4)        # techo al stack de Suerte
        if espadas > 0:
            suerte *= 1.10                         # modesto: un slot ≈ un slot (no multiplicativo dominante)
    if any(m.mata == "as_espadas" for m in matas):
        suerte *= 1.10
    suerte = min(suerte, 1.8)                       # techo duro (U-invertida de Kao)

    score = puntos * suerte

    # Trampa: penalización neta por comerla en crudo (sin la Fullería que la rompe)
    if tctx["activa"]:
        score *= tctx["penalty"]

    # --- Ejes de decisión (DECORRELACIONADOS a propósito, §7.3) ---
    tempo = score
    # ESCALA = sembrar motor: SOLO cartas-semilla de BAJO valor (v≤4) de tu afinidad,
    # NO Matas ni cartas altas. Así el jugador greedy-tempo las IGNORA (bajo puntos),
    # y solo el previsor las planta. Esto separa tempo de escala.
    seeds = 0
    for c in cap:
        if c.mata or c.v > 4:
            continue
        if ((bi["tiene_P1"] and c.palo == OROS) or
                (bi["tiene_P2"] and c.palo == ESPADAS) or
                (bi["tiene_P3"] and c.palo == BASTOS)):
            seeds += 1
    escala = seeds * 6.0
    # DEFENSA = peligro negado al Diablo (Matas/cartas altas) + limpiar la Mesa.
    # Capturar una Mata por DEFENSA cuesta tempo si no encaja con tu motor.
    defensa = sum(c.danger for c in cap) + (10 if play.empties_mesa else 0)

    return dict(score=score, puntos=puntos, suerte=suerte,
                tempo=tempo, escala=escala, defensa=defensa,
                oros=oros, espadas=espadas, bastos=bastos)


def apply_play(play, rs: RunState, bi):
    """Muta rs con el motor sembrado por esta captura. El motor crece SOLO con
    cartas-semilla de bajo valor (v≤4) de tu afinidad — las mismas que mide la Escala,
    así la previsión (plantarlas) paga y el greedy-tempo (que las ignora) no las acumula.
    Acumuladores con techo (anti-runaway / U-invertida)."""
    cap = play.captured
    if bi["tiene_P1"]:
        rs.veta_oro = min(3, rs.veta_oro +
                          sum(1 for c in cap if c.palo == OROS and c.v <= 4 and not c.mata))
    if bi["tiene_P3"]:
        rs.bloque_bosque = min(3, rs.bloque_bosque +
                               sum(1 for c in cap if c.palo == BASTOS and c.v <= 4 and not c.mata))
    if bi["tiene_P2"]:
        rs.suerte_filo = min(0.6, rs.suerte_filo +
                             0.08 * sum(1 for c in cap if c.palo == ESPADAS and c.v <= 4 and not c.mata))


# ----------------------------- EV situacional -------------------------------
def ev_play(sc, manos_left, total_manos, remaining, mesa_danger):
    """EV escalar dependiente de estado: temprano/cómodo premia escala/defensa;
    tarde/urgente premia tempo. Produce divergencia (foso)."""
    tempo_n = sc["tempo"] / 40.0
    escala_n = sc["escala"] / 12.0
    defensa_n = sc["defensa"] / 16.0
    urgency = max(0.0, min(1.5, remaining / max(1.0, manos_left * 22.0)))
    w_tempo = 1.15 + 1.7 * urgency
    w_escala = 0.7 * (manos_left / max(1, total_manos))
    w_defensa = 0.4 + 0.45 * mesa_danger
    return w_tempo * tempo_n + w_escala * escala_n + w_defensa * defensa_n


def pareto_front(vectors):
    """Índices de vectores no-dominados en (tempo, escala, defensa). Maximización."""
    n = len(vectors)
    nd = []
    for i in range(n):
        dominated = False
        for j in range(n):
            if i == j:
                continue
            a, b = vectors[j], vectors[i]
            if (a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2] and
                    (a[0] > b[0] or a[1] > b[1] or a[2] > b[2])):
                dominated = True
                break
        if not dominated:
            nd.append(i)
    return nd


# ----------------------------- Mesa / siembra -------------------------------
class Mazo:
    def __init__(self, rng):
        self.cartas = construir_baraja()
        rng.shuffle(self.cartas)
        self.i = 0

    def draw(self, n):
        out = self.cartas[self.i:self.i + n]
        self.i += len(out)
        return out

    def restantes(self):
        return len(self.cartas) - self.i


def mesa_danger_factor(mesa):
    if not mesa:
        return 0.0
    return min(1.0, sum(c.danger for c in mesa) / (len(mesa) * 4.0))


def _pareto_count(mesa, hand, tctx, bi, rs):
    plays = enumerate_plays(hand, mesa, tctx, bi)
    if len(plays) < 2:
        return (1 if plays else 0), plays
    vecs = []
    for p in plays:
        sc = score_play(p, rs, bi, tctx)
        vecs.append((sc["tempo"], sc["escala"], sc["defensa"]))
    return len(pareto_front(vecs)), plays


def _ensure_divergence(mesa, hand, tctx, bi, rs, mazo, rng, max_tries=8):
    """Siembra intencional del Diablo (§7.3.2): si la Mesa no admite ≥2 jugadas
    Pareto-no-dominadas, perturba cartas de la Mesa (re-siembra sobre ejes) hasta
    lograrlo o agotar 8 intentos. Determinista por el rng del seed."""
    best = list(mesa)
    best_n, _ = _pareto_count(best, hand, tctx, bi, rs)
    if best_n >= 2:
        return best, 0
    in_play = set(hand) | set(mesa)
    supply = [c for c in construir_baraja() if c not in in_play]
    rng.shuffle(supply)
    si = 0
    cur = list(mesa)
    used = 0
    for t in range(max_tries):
        used += 1
        cand = list(cur)
        k = 1 + (t % 2)
        for _ in range(k):
            if si >= len(supply):
                break
            idx = rng.randrange(len(cand))
            cand[idx] = supply[si]
            si += 1
        n, _ = _pareto_count(cand, hand, tctx, bi, rs)
        if n > best_n:
            best_n, best = n, cand
        cur = cand
        if best_n >= 2:
            break
    return best, used


# ----------------------------- Simulación de apuesta ------------------------
def simulate_apuesta(rng, mazo, rs, bi, umbral, manos, trampa_id, policy,
                     en_envite=False, collect_decision_stats=False):
    """Juega una apuesta. Devuelve (score_total, info)."""
    tctx = trampa_context(trampa_id if en_envite else None, bi)
    # Mesa inicial
    mesa = mazo.draw(MESA_INICIAL)
    hand = mazo.draw(MANO_TAM)
    score_total = 0.0
    total_manos = manos
    pareto_counts = []
    ev_spreads = []
    working_sets = []
    primera_envite_pendiente = en_envite

    reseeds_total = 0
    for turno in range(manos):
        # Siembra: mantener mesa en [MESA_MIN, MESA_MAX]
        while len(mesa) < MESA_MIN and mazo.restantes() > 0:
            mesa.append(mazo.draw(1)[0] if mazo.restantes() else None)
            mesa = [c for c in mesa if c is not None]
        # Siembra INTENCIONAL del Diablo (§7.3.2): garantizar ≥2 jugadas Pareto
        # divergentes; re-siembra acotada sobre ejes (≤8 intentos).
        mesa, used = _ensure_divergence(mesa, hand, tctx, bi, rs, mazo, rng)
        reseeds_total += used
        plays = enumerate_plays(hand, mesa, tctx, bi)
        if not plays:
            # sin jugada: descarta la carta más baja a la Mesa y repón
            if hand:
                low = min(range(len(hand)), key=lambda i: hand[i].v)
                mesa.append(hand.pop(low))
            _repon(hand, mazo)
            continue

        remaining = umbral - score_total
        mdf = mesa_danger_factor(mesa)
        scored = []
        for p in plays:
            sc = score_play(p, rs, bi, tctx,
                            primera_del_envite=(primera_envite_pendiente))
            ev = ev_play(sc, manos - turno, total_manos, remaining, mdf)
            scored.append((p, sc, ev))

        if collect_decision_stats:
            vecs = [(s["tempo"], s["escala"], s["defensa"]) for _, s, _ in scored]
            nd = pareto_front(vecs)
            pareto_counts.append(len(nd))
            # spread EV entre las 2 mejores jugadas DISTINTAS (dedup de empates de palo:
            # misma (tempo,escala,defensa) = misma decisión por otra ruta → no cuenta).
            uniq = {}
            for p, s, ev in scored:
                key = (round(s["tempo"], 1), round(s["escala"], 1), round(s["defensa"], 1))
                if key not in uniq or ev > uniq[key]:
                    uniq[key] = ev
            evs = sorted(uniq.values(), reverse=True)
            if len(evs) >= 2 and evs[0] > 1e-9:
                ev_spreads.append((evs[0] - evs[1]) / evs[0])
            working_sets.append(len(plays))

        chosen = _choose(scored, policy, rng, rs, bi, tctx, mazo, manos - turno,
                         total_manos, remaining, mdf)
        p, sc, _ = chosen
        score_total += sc["score"]
        apply_play(p, rs, bi)
        if primera_envite_pendiente:
            primera_envite_pendiente = False
        # remover capturadas de mesa y mano
        mesa = [c for k, c in enumerate(mesa) if k not in p.subset_idx]
        hand.pop(p.hand_idx)
        _repon(hand, mazo)

    info = dict(pareto_counts=pareto_counts, ev_spreads=ev_spreads,
                working_sets=working_sets)
    return score_total, info


def _repon(hand, mazo):
    while len(hand) < MANO_TAM and mazo.restantes() > 0:
        hand.extend(mazo.draw(1))


def _choose(scored, policy, rng, rs, bi, tctx, mazo, manos_left, total_manos,
            remaining, mdf):
    if policy == "greedy_1ply":
        return max(scored, key=lambda x: x[1]["tempo"])
    if policy == "greedy_ev":
        return max(scored, key=lambda x: x[2])
    if policy.startswith("lookahead"):
        k = int(policy.split("_")[1])
        return _lookahead_choice(scored, k, rs, bi, tctx, manos_left,
                                 total_manos, remaining, mdf)
    return max(scored, key=lambda x: x[2])


def _lookahead_choice(scored, k, rs, bi, tctx, manos_left, total_manos,
                      remaining, mdf):
    """Evalúa cada jugada por: score inmediato + valor del motor que deja montado.
    Aproxima el futuro con el crecimiento de acumuladores (escala) ponderado por
    manos restantes — sin re-sembrar (barato y monótono en k)."""
    best = None
    best_val = -1e18
    for p, sc, ev in scored:
        # simular el efecto en rs
        rs2 = RunState(rs.veta_oro, rs.bloque_bosque, rs.suerte_filo,
                       rs.primera_escoba_envite_hecha)
        apply_play(p, rs2, bi)
        # valor futuro estimado: el motor extra rinde en las próximas (manos_left-1) escobas
        engine_now = _engine_per_escoba(rs, bi)
        engine_after = _engine_per_escoba(rs2, bi)
        delta_engine = engine_after - engine_now
        horizon = max(0, min(k, manos_left - 1))
        future = delta_engine * horizon
        val = sc["score"] + future
        if val > best_val:
            best_val = val
            best = (p, sc, ev)
    return best


def _engine_per_escoba(rs, bi):
    """Puntos extra que el motor acumulado añade a una escoba promedio."""
    val = 0.0
    if bi["tiene_P1"]:
        val += rs.veta_oro
    if bi["tiene_P3"]:
        val += rs.bloque_bosque
    if bi["tiene_P2"]:
        val += rs.suerte_filo * 20.0
    return val
