"""
ÓRDAGO — SOLVER DE PAPEL (§14.0). El gate `balance-check` de la metodología studio.
Valida o MATA el foso ANTES de un píxel: Pareto postcondición, banda EV, S4–S7,
test del experto, KILL de cimiento.

Anti-fabricación: TODA validación vive en este código; el veredicto se deriva de
agregados grandes escritos a disco (results/*.json) con timestamp, no de afirmaciones.

Uso:
    python3 ordago_solver.py [--seeds N] [--decision-runs N] [--quick]
"""
from __future__ import annotations
import argparse, json, math, os, random, statistics as st, time
from content import APUESTAS_MANGA1, BUILDS_EXTREMAS, TRAMPAS
from engine import (
    Mazo, RunState, build_info, simulate_apuesta,
)

RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")
TRAMPA_IDS = list(TRAMPAS.keys())


# --------------------------------------------------------------------------
def simulate_run(seed, build_ids, policy, collect=False):
    """Una Manga 1 completa (3 apuestas). Devuelve dict con score/umbral por apuesta,
    win global, y stats de decisión opcionales."""
    rng = random.Random(seed)
    bi = build_info(build_ids)
    # Trampa del Envite fijada por seed (determinista)
    trampa_id = TRAMPA_IDS[seed % len(TRAMPA_IDS)]
    mazo = Mazo(rng)
    rs = RunState()
    apuestas_out = []
    win = True
    dstats = dict(pareto_counts=[], ev_spreads=[], working_sets=[])
    for ap in APUESTAS_MANGA1:
        en_envite = ap["trampa"] is not None
        # mazo se recicla por apuesta (nueva baraja barajada) — cada apuesta es una mesa nueva
        mazo_ap = Mazo(random.Random(seed * 31 + ap["umbral"]))
        score, info = simulate_apuesta(
            rng, mazo_ap, rs, bi, ap["umbral"], ap["manos"], trampa_id, policy,
            en_envite=en_envite, collect_decision_stats=collect)
        ratio = score / ap["umbral"]
        passed = score >= ap["umbral"]
        win = win and passed
        apuestas_out.append(dict(id=ap["id"], score=round(score, 2),
                                 umbral=ap["umbral"], ratio=round(ratio, 3),
                                 passed=passed))
        if collect:
            for k in dstats:
                dstats[k].extend(info[k])
    return dict(seed=seed, build=build_ids, trampa=trampa_id, win=win,
                apuestas=apuestas_out, dstats=dstats)


# --------------------------------------------------------------------------
def gate_decision_depth(seeds, policy="greedy_ev"):
    """Pareto postcondición + banda EV + KILL de cimiento + working-set (S6)."""
    pareto_counts, ev_spreads, working_sets = [], [], []
    # usar una mezcla de builds para no sesgar
    builds = list(BUILDS_EXTREMAS.values())
    for i in seeds:
        b = builds[i % len(builds)]
        r = simulate_run(i, b, policy, collect=True)
        pareto_counts.extend(r["dstats"]["pareto_counts"])
        ev_spreads.extend(r["dstats"]["ev_spreads"])
        working_sets.extend(r["dstats"]["working_sets"])
    n = len(pareto_counts)
    ge2 = sum(1 for c in pareto_counts if c >= 2)
    eq1 = sum(1 for c in pareto_counts if c <= 1)
    pareto_pct = ge2 / n if n else 0
    dominant_pct = eq1 / n if n else 0
    med_spread = st.median(ev_spreads) if ev_spreads else 0
    spread_in_band = sum(1 for s in ev_spreads if 0.10 <= s <= 0.15) / len(ev_spreads) if ev_spreads else 0
    ws_le6 = sum(1 for w in working_sets if w <= 6) / len(working_sets) if working_sets else 0
    return dict(
        n_decisions=n,
        pareto_ge2_pct=round(pareto_pct, 4),
        dominant_le1_pct=round(dominant_pct, 4),
        median_ev_spread=round(med_spread, 4),
        ev_spread_in_band_pct=round(spread_in_band, 4),
        working_set_le6_pct=round(ws_le6, 4),
        median_working_set=st.median(working_sets) if working_sets else 0,
        # veredictos
        verdict_pareto="GREEN" if pareto_pct >= 0.95 else ("YELLOW" if pareto_pct >= 0.85 else "KILL"),
        verdict_foundation="KILL" if dominant_pct > 0.20 else "GREEN",
        verdict_ev_band=("GREEN" if 0.10 <= med_spread <= 0.15 else
                         ("YELLOW" if 0.07 <= med_spread <= 0.18 else "RED")),
    )


def gate_s4_mana_dominance(n_seeds, policy="lookahead_2"):
    """S4: ninguna build extrema domina. winrate + Sharpe del margen."""
    rows = {}
    for name, build in BUILDS_EXTREMAS.items():
        wins = 0
        margins = []   # margen FIRMADO: min_ratio - 1 (negativo si pierde)
        for s in range(n_seeds):
            r = simulate_run(s, build, policy)
            wins += 1 if r["win"] else 0
            min_ratio = min(a["ratio"] for a in r["apuestas"])
            margins.append(min_ratio - 1.0)
        wr = wins / n_seeds
        mean_m = st.mean(margins)
        std_m = st.pstdev(margins) or 1e-9
        sharpe = mean_m / std_m   # firmado: perdedores consistentes → muy negativo
        rows[name] = dict(winrate=round(wr, 4), mean_margin=round(mean_m, 3),
                          sharpe=round(sharpe, 3))
    by_wr = sorted(rows.values(), key=lambda v: v["winrate"], reverse=True)
    top_wr = by_wr[0]["winrate"]
    second_wr = by_wr[1]["winrate"] if len(by_wr) > 1 else 0.0
    wr_gap = top_wr - second_wr
    n_viable = sum(1 for v in rows.values() if v["winrate"] >= 0.10)
    # Dominancia (fiel a GDD §14 S4): GREEN = ninguna build >55% winrate Y ≥3 builds viables
    # (no exige clustering perfecto; el spread de viabilidad es sano en un deckbuilder).
    if top_wr > 0.62 or n_viable < 2:
        verdict = "KILL"
    elif top_wr > 0.55 or n_viable < 3:
        verdict = "YELLOW"
    else:
        verdict = "GREEN"
    return dict(builds=rows, top_winrate=round(top_wr, 4),
                wr_gap_top2=round(wr_gap, 4), n_viable=n_viable, verdict=verdict)


def gate_s5_threshold_scaling(n_seeds, build=("P1_oro", "P2_filo", "F1_lectura_falsa"),
                              policy="lookahead_2"):
    """S5: mediana score/umbral ∈ [0.95,1.15], p10>0.8, p90<1.6 (jugador competente)."""
    per_band = {ap["id"]: [] for ap in APUESTAS_MANGA1}
    for s in range(n_seeds):
        r = simulate_run(s, list(build), policy)
        for a in r["apuestas"]:
            per_band[a["id"]].append(a["ratio"])
    bands = {}
    overall = []
    for band, ratios in per_band.items():
        ratios_sorted = sorted(ratios)
        overall.extend(ratios)
        bands[band] = dict(
            median=round(st.median(ratios), 3),
            p10=round(_pct(ratios_sorted, 10), 3),
            p90=round(_pct(ratios_sorted, 90), 3),
        )
    med = st.median(overall)
    p10 = _pct(sorted(overall), 10)
    p90 = _pct(sorted(overall), 90)
    green = (0.95 <= med <= 1.15) and p10 > 0.8 and p90 < 1.6
    yellow = (0.85 <= med <= 1.25)
    verdict = "GREEN" if green else ("YELLOW" if yellow else "KILL")
    return dict(bands=bands, overall_median=round(med, 3),
                overall_p10=round(p10, 3), overall_p90=round(p90, 3),
                verdict=verdict)


def gate_expert_test(n_seeds, build=("P1_oro", "P2_filo", "P3_bosque")):
    """Test del experto: score medio crece monótono con la profundidad de lookahead.
    KILL si se aplana en k≥2 (el verbo no premia ver más allá → puzzle)."""
    policies = ["greedy_1ply", "lookahead_1", "lookahead_2", "lookahead_3"]
    means = {}
    for pol in policies:
        totals = []
        for s in range(n_seeds):
            r = simulate_run(s, list(build), pol)
            totals.append(sum(a["score"] for a in r["apuestas"]))
        means[pol] = round(st.mean(totals), 2)
    seq = [means[p] for p in policies]
    # crecimiento de greedy_1ply → lookahead_3
    monotonic = all(seq[i + 1] >= seq[i] - 0.5 for i in range(len(seq) - 1))
    gain_total = (seq[-1] - seq[0]) / seq[0] if seq[0] else 0
    gain_k2_k3 = (seq[3] - seq[2]) / seq[2] if seq[2] else 0
    # KILL si no hay ganancia significativa de profundidad o se aplana ya en k2
    flat_at_k2 = gain_k2_k3 < 0.005 and (seq[2] - seq[1]) / max(seq[1], 1) < 0.005
    verdict = "GREEN" if (monotonic and gain_total >= 0.03 and not flat_at_k2) else (
        "YELLOW" if gain_total >= 0.01 else "KILL")
    return dict(means_by_policy=means, total_gain_pct=round(gain_total, 4),
                gain_k2_to_k3=round(gain_k2_k3, 4), monotonic=monotonic,
                verdict=verdict)


def gate_s7_ftue_mastery(seeds):
    """S7: perfil FTUE (build novato simple, debe tener una dominante-tempo legítima)
    vs Maestría (debe ofrecer ≥2 Pareto en banda). Aproximación con dos builds."""
    # FTUE: build sin engine (3F_0P) en apuesta chica → debe haber jugada dominante clara
    ftue = gate_decision_depth(seeds, policy="greedy_1ply")
    # Maestría: build con engine, política experta
    mastery = gate_decision_depth(seeds, policy="lookahead_2")
    verdict = "GREEN" if (mastery["pareto_ge2_pct"] >= 0.90) else "YELLOW"
    return dict(ftue_pareto_ge2=ftue["pareto_ge2_pct"],
                mastery_pareto_ge2=mastery["pareto_ge2_pct"], verdict=verdict)


def _pct(sorted_list, p):
    if not sorted_list:
        return 0
    k = (len(sorted_list) - 1) * p / 100.0
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_list[int(k)]
    return sorted_list[f] * (c - k) + sorted_list[c] * (k - f)


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", type=int, default=1500)
    ap.add_argument("--decision-runs", type=int, default=700)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    if args.quick:
        args.seeds, args.decision_runs = 300, 200

    t0 = time.time()
    os.makedirs(RESULTS_DIR, exist_ok=True)
    print(f"[ÓRDAGO solver] seeds={args.seeds} decision_runs={args.decision_runs}")

    decision_seeds = range(args.decision_runs)
    print("· gate: profundidad de decisión (Pareto + banda EV + cimiento)…")
    g_dec = gate_decision_depth(decision_seeds)
    print("· gate: S4 dominancia de Maña…")
    g_s4 = gate_s4_mana_dominance(args.seeds)
    print("· gate: S5 escalado del umbral…")
    g_s5 = gate_s5_threshold_scaling(args.seeds)
    print("· gate: test del experto…")
    g_exp = gate_expert_test(min(args.seeds, 800))
    print("· gate: S7 FTUE/Maestría…")
    g_s7 = gate_s7_ftue_mastery(range(min(args.decision_runs, 400)))

    results = dict(
        meta=dict(timestamp=time.strftime("%Y-%m-%dT%H:%M:%S"),
                  seeds=args.seeds, decision_runs=args.decision_runs,
                  elapsed_s=round(time.time() - t0, 1)),
        decision_depth=g_dec, s4_mana_dominance=g_s4,
        s5_threshold=g_s5, expert_test=g_exp, s7_ftue_mastery=g_s7,
    )
    # veredicto global
    verdicts = {
        "pareto": g_dec["verdict_pareto"],
        "foundation": g_dec["verdict_foundation"],
        "ev_band": g_dec["verdict_ev_band"],
        "s4_mana": g_s4["verdict"],
        "s5_threshold": g_s5["verdict"],
        "expert": g_exp["verdict"],
        "s7": g_s7["verdict"],
    }
    results["verdicts"] = verdicts
    n_kill = sum(1 for v in verdicts.values() if v == "KILL")
    n_soft = sum(1 for v in verdicts.values() if v in ("YELLOW", "RED"))
    if any(v in ("KILL", "RED") for v in [verdicts["foundation"], verdicts["pareto"]]):
        overall = "KILL — el foso no existe (verbo puzzle); reestructurar o pivotar"
    elif n_kill > 0:
        overall = "RED — un gate crítico falla; recalibrar contenido"
    elif n_soft > 0:
        overall = ("YELLOW — foso VALIDADO (decisión real, no puzzle); amarillos = calibración "
                   "de balance fino a terminar con telemetría/playtest humano. Proceder al prototipo.")
    else:
        overall = "GREEN — foso validado; proceder al prototipo jugable"
    results["overall"] = overall

    outpath = os.path.join(RESULTS_DIR, "solver_report.json")
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    _print_report(results)
    print(f"\n→ JSON: {outpath}  ({results['meta']['elapsed_s']}s)")
    return results


def _print_report(r):
    print("\n" + "=" * 64)
    print("VEREDICTO DEL SOLVER — Manga 1 prototipo")
    print("=" * 64)
    d = r["decision_depth"]
    print(f"Pareto ≥2 jugadas no-dominadas: {d['pareto_ge2_pct']*100:.1f}%  [{d['verdict_pareto']}]")
    print(f"Cimiento (≤1 dominante):        {d['dominant_le1_pct']*100:.1f}%  [{d['verdict_foundation']}]")
    print(f"Mediana spread EV:              {d['median_ev_spread']*100:.1f}%  [{d['verdict_ev_band']}]  (banda objetivo 10–15%)")
    print(f"Working-set ≤6:                 {d['working_set_le6_pct']*100:.1f}%  (mediana {d['median_working_set']})")
    s4 = r["s4_mana_dominance"]
    print(f"\nS4 Dominancia de Maña: top winrate={s4['top_winrate']*100:.1f}%  gap_top2={s4['wr_gap_top2']*100:.1f}pp  viables={s4['n_viable']}/6  [{s4['verdict']}]")
    for name, v in s4["builds"].items():
        print(f"    {name:10s} wr={v['winrate']*100:5.1f}%  margin={v['mean_margin']:.2f}  sharpe={v['sharpe']:.2f}")
    s5 = r["s5_threshold"]
    print(f"\nS5 Umbral: mediana score/umbral={s5['overall_median']}  p10={s5['overall_p10']}  p90={s5['overall_p90']}  [{s5['verdict']}]")
    for b, v in s5["bands"].items():
        print(f"    {b:8s} med={v['median']}  p10={v['p10']}  p90={v['p90']}")
    e = r["expert_test"]
    print(f"\nTest del experto: {e['means_by_policy']}  gain={e['total_gain_pct']*100:.1f}%  [{e['verdict']}]")
    s7 = r["s7_ftue_mastery"]
    print(f"S7 FTUE/Maestría: ftue={s7['ftue_pareto_ge2']*100:.0f}% maestría={s7['mastery_pareto_ge2']*100:.0f}%  [{s7['verdict']}]")
    print("\n" + "-" * 64)
    print(f"VEREDICTO GLOBAL: {r['overall']}")
    print("-" * 64)


if __name__ == "__main__":
    main()
