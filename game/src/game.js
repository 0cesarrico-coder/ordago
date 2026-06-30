// ÓRDAGO — controlador de juego (máquina de estados de la Manga 1). Sin render.
import {
  APUESTAS_MANGA1, TRAMPA_IDS, TRAMPAS, FULLERIAS, PACTOS, MESA_MIN, MESA_INICIAL, MANO_TAM,
  construirBaraja,
} from './content.js';
import {
  makeRNG, shuffle, buildInfo, newRunState, trampaContext,
  enumeratePlays, scorePlay, applyPlay, sumasDisponibles,
} from './engine.js';

export class Game {
  constructor(seed, build) {
    this.seed = seed >>> 0;
    this.build = build.slice();
    this.rs = newRunState();
    this._cantinaCache = {};
    this.trampaId = TRAMPA_IDS[this.seed % TRAMPA_IDS.length]; // Trampa del Envite, fija por seed
    this.apuestaIndex = -1;
    this.status = 'intro';        // intro | playing | apuesta_won | cantina | won | lost
    this.log = [];
    this.reales = 8;              // moneda para la Cantina
  }

  get bi() { return buildInfo(this.build); }

  // Sub-semilla determinista por propósito (mazo de cada apuesta, ofertas de Cantina…).
  // Independiente de cuántas veces re-renderice la UI → "misma semilla → misma partida" (§8.3).
  subRng(salt) { return makeRNG((Math.imul(this.seed ^ salt, 0x9e3779b1) ^ (salt << 16)) >>> 0); }

  startApuesta(index) {
    this.apuestaIndex = index;
    const ap = APUESTAS_MANGA1[index];
    this.apuesta = ap;
    this.enEnvite = ap.trampa === 'SEED';
    this.tctx = trampaContext(this.enEnvite ? this.trampaId : null, this.bi);
    this.mazo = shuffle(construirBaraja(), this.subRng(1009 * (index + 1))); // mazo determinista por apuesta
    this.mi = 0;
    this.mesa = this.draw(MESA_INICIAL);
    this.hand = this.draw(MANO_TAM);
    this.scoreApuesta = 0;
    this.manosLeft = ap.manos;
    this.primeraEscobaHecha = false;
    this.status = 'playing';
    this.seedMesa();
    return this.getState();
  }

  draw(n) {
    const out = this.mazo.slice(this.mi, this.mi + n);
    this.mi += out.length;
    return out;
  }

  seedMesa() {
    while (this.mesa.length < MESA_MIN && this.mi < this.mazo.length) {
      this.mesa.push(this.draw(1)[0]);
    }
  }

  // Jugadas legales y resaltado de asistencia (Modo aprendiz / Ojo del Tahúr).
  asistencia() {
    return sumasDisponibles(this.hand, this.mesa, this.tctx, this.bi);
  }

  // Validar una selección concreta del jugador → devuelve la jugada o null.
  validarSeleccion(handIdx, mesaIdxs) {
    const plays = enumeratePlays(this.hand, this.mesa, this.tctx, this.bi);
    const key = handIdx + '|' + mesaIdxs.slice().sort((a, b) => a - b).join(',');
    return plays.find((p) => p.hand_idx === handIdx &&
      p.subset_idx.join(',') === mesaIdxs.slice().sort((a, b) => a - b).join(',')) || null;
  }

  // Resolver una Escoba. Devuelve resultado para que la UI lo "juicee".
  jugarEscoba(handIdx, mesaIdxs) {
    const play = this.validarSeleccion(handIdx, mesaIdxs);
    if (!play) return { ok: false, motivo: 'no suma 15' };
    const primera = this.enEnvite && !this.primeraEscobaHecha;
    const sc = scorePlay(play, this.rs, this.bi, this.tctx, primera);
    applyPlay(play, this.rs, this.bi);
    if (this.enEnvite) this.primeraEscobaHecha = true;
    this.scoreApuesta += sc.score;
    // remover capturadas
    const setIdx = new Set(play.subset_idx);
    const capturadas = this.mesa.filter((_, i) => setIdx.has(i));
    this.mesa = this.mesa.filter((_, i) => !setIdx.has(i));
    this.hand.splice(handIdx, 1);
    this.refillHand();
    this.seedMesa();
    this.manosLeft--;
    const res = {
      ok: true, escoba: true, score: sc.score, puntos: sc.puntos, suerte: sc.suerte,
      capturadas, escobaLimpia: play.empties_mesa, nulaT3: primera && sc.score === 0,
    };
    this.checkFin(res);
    return res;
  }

  // Pasar: dejar una carta en la Mesa (no puntúa), gastar una mano.
  pasar(handIdx) {
    const carta = this.hand.splice(handIdx, 1)[0];
    this.mesa.push(carta);
    this.refillHand();
    this.seedMesa();
    this.manosLeft--;
    const res = { ok: true, escoba: false, paso: true, carta };
    this.checkFin(res);
    return res;
  }

  refillHand() {
    while (this.hand.length < MANO_TAM && this.mi < this.mazo.length) this.hand.push(this.draw(1)[0]);
  }

  checkFin(res) {
    if (this.scoreApuesta >= this.apuesta.umbral) {
      this.reales += 5 + Math.floor((this.scoreApuesta - this.apuesta.umbral) / 20);
      if (this.apuestaIndex >= APUESTAS_MANGA1.length - 1) { this.status = 'won'; res.gano = 'manga'; }
      else { this.status = 'apuesta_won'; res.gano = 'apuesta'; }
    } else if (this.manosLeft <= 0 && !this.hayJugadaOPaso()) {
      this.status = 'lost'; res.perdio = true;
    } else if (this.manosLeft <= 0) {
      this.status = 'lost'; res.perdio = true;
    }
  }

  hayJugadaOPaso() { return this.manosLeft > 0; }

  // --- Cantina (§7.9): ofertas de Maña entre apuestas ---
  ofertasCantina() {
    // Cacheadas por apuesta: re-renderizar la Cantina NO re-rollea (determinismo §8.3).
    const key = this.apuestaIndex;
    if (this._cantinaCache[key]) return this._cantinaCache[key];
    const owned = new Set(this.build);
    const pool = [];
    const counter = TRAMPAS[this.trampaId].rompePor;
    if (counter && !owned.has(counter)) pool.push(counter);
    for (const id of [...Object.keys(PACTOS), ...Object.keys(FULLERIAS)]) {
      if (!owned.has(id) && id !== 'F0_ojo' && !pool.includes(id)) pool.push(id);
    }
    const shuffled = shuffle(pool, this.subRng(7001 * (key + 1)));
    const ofertas = shuffled.slice(0, 3).map((id) => ({
      id, tipo: PACTOS[id] ? 'pacto' : 'fulleria',
      data: PACTOS[id] || FULLERIAS[id], costo: PACTOS[id] ? 5 : 4,
      rompeEnvite: id === counter,
    }));
    this._cantinaCache[key] = ofertas;
    return ofertas;
  }

  // Equipar una oferta en una ranura (reemplaza slotIdx, conservando F0_ojo si se desea).
  equipar(ofertaId, slotIdx, costo) {
    if (this.reales < costo) return false;
    this.reales -= costo;
    this.build[slotIdx] = ofertaId;
    return true;
  }

  getState() {
    return {
      status: this.status, seed: this.seed,
      apuesta: this.apuesta, apuestaIndex: this.apuestaIndex,
      mesa: this.mesa, hand: this.hand, manosLeft: this.manosLeft,
      scoreApuesta: this.scoreApuesta, umbral: this.apuesta?.umbral,
      build: this.build, bi: this.bi, reales: this.reales,
      tctx: this.tctx, enEnvite: this.enEnvite, rs: this.rs,
      trampaEnvite: { id: this.trampaId, ...TRAMPAS[this.trampaId] },
    };
  }
}

