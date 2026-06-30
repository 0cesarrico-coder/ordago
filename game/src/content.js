// ÓRDAGO — contenido del prototipo (espejo de solver/content.py, números VALIDADOS por el solver).
// Data-driven: toda regla/efecto vive aquí; el motor (engine.js) los interpreta; la UI no conoce balance.

export const PALOS = { O: 'Oros', C: 'Copas', E: 'Espadas', B: 'Bastos' };
export const PALO_GLYPH = { O: '🪙', C: '🍷', E: '⚔️', B: '🌳' };
export const PALO_COLOR = { O: '#d9a531', C: '#c0455e', E: '#5b7fb0', B: '#5a8c5a' };
export const NOMBRE_VALOR = { 8: 'Sota', 9: 'Caballo', 10: 'Rey' };

// Matas legendarias (§7.5) — base alta + efectos. clave "palo-valor".
export const MATAS = {
  'E-1': { puntos_base: 13, danger: 6, mata: 'as_espadas', nota: '×1.1 Suerte al capturarla' },
  'B-1': { puntos_base: 11, danger: 6, mata: 'as_bastos', nota: '+4 Puntos en bloque' },
  'E-7': { puntos_base: 10, danger: 5, mata: 'siete_espadas', nota: 'cuenta como filo' },
  'O-7': { puntos_base: 9, danger: 5, mata: 'siete_oros', nota: '+2 Reales' },
};

export const TARGET_BASE = 15;
export const ESCOBA_LIMPIA_BONUS = 5;
export const ESCOBA_BONUS_FLAT = 16;       // el Escoba base DOMINA (Pactos/Fullerías son modificadores)
export const TRAMPA_PENALTY = 0.55;        // comer la Trampa en crudo (progresivo +0.11/Fullería)
export const TRAMPA_F3_BONUS = 1.12;
export const MESA_MIN = 5, MESA_MAX = 6, MESA_INICIAL = 4, MANO_TAM = 3;

// Trampas del Diablo (§3.1) — efecto mecánico real en el prototipo.
export const TRAMPAS = {
  T1_trece:        { nombre: 'El Trece', desc: 'Ahora hay que sumar 13', target: 13, rompePor: 'F1_lectura_falsa' },
  T2_oros_malditos:{ nombre: 'Oros Malditos', desc: 'Los Oros no cuentan en capturas', oros_bloqueados: true, rompePor: 'F2_contrabando' },
  T3_primer_nulo:  { nombre: 'Primer Robo Nulo', desc: 'Tu 1ª Escoba no puntúa', primer_nulo: true, rompePor: 'F3_doble_filo' },
};

// Fullerías (§3.2) — ocupan ranura de Maña.
export const FULLERIAS = {
  F1_lectura_falsa: { nombre: 'Lectura Falsa', desc: 'Una figura se lee como el valor que elijas', rompe: 'T1_trece', icon: '👁' },
  F2_contrabando:   { nombre: 'Contrabando', desc: 'Usa Oros pese a la Trampa', rompe: 'T2_oros_malditos', icon: '🤞' },
  F3_doble_filo:    { nombre: 'Doble Filo', desc: 'Tu 1ª Escoba puntúa ×2', rompe: 'T3_primer_nulo', icon: '🗡' },
  F0_ojo:           { nombre: 'Ojo del Tahúr', desc: 'Resalta las sumas de 15 (maestría)', rompe: null, icon: '🔮', solucionador: true },
};

// Pactos Oscuros (§3.3) — ocupan ranura de Maña toda la run.
export const PACTOS = {
  P1_oro:    { nombre: 'Pacto del Oro', afinidad: 'O', desc: '+1 Punto por Oro · siembra Veta (+Puntos/Escoba)', icon: '🪙' },
  P2_filo:   { nombre: 'Pacto del Filo', afinidad: 'E', desc: '×1.1 Suerte con Espada · stack de Suerte', icon: '⚔️' },
  P3_bosque: { nombre: 'Pacto del Bosque', afinidad: 'B', desc: '+1 Punto por carta · siembra Bloque', icon: '🌳' },
};

// Estructura: Manga 1. El solver calibró el FOSO con umbrales-stress (228/378/358 a winrate ~50%
// con build óptima). La Manga 1 es ONBOARDING (§5/§13: el novato debe poder ganar su 1ª partida),
// así que se aligera ~18% para un primer-win satisfactorio sin tocar la mecánica validada.
export const APUESTAS_MANGA1 = [
  { id: 'chica',  nombre: 'La Chica',  umbral: 185, manos: 5, trampa: null },
  { id: 'grande', nombre: 'La Grande', umbral: 305, manos: 6, trampa: null },
  { id: 'envite', nombre: 'El Envite del Diablo', umbral: 300, manos: 7, trampa: 'SEED' }, // se fija por seed
];

export const TRAMPA_IDS = Object.keys(TRAMPAS);

// Build inicial del prototipo: 2 Pactos + 1 Fullería (3 slots reales). El asistente "modo
// aprendiz" (resaltar sumas de 15) es GRATIS en el prototipo (§13.1 capa 2), no ocupa slot.
export const BUILD_INICIAL = ['P1_oro', 'P3_bosque', 'F1_lectura_falsa'];

export function nombreCarta(c) {
  const n = NOMBRE_VALOR[c.v] || c.v;
  return `${n} de ${PALOS[c.palo]}`;
}

export function dangerNormal(v) { return v >= 9 ? 3 : v >= 6 ? 2 : 1; }

export function construirBaraja() {
  const baraja = [];
  for (const palo of Object.keys(PALOS)) {
    for (let v = 1; v <= 10; v++) {
      const esp = MATAS[`${palo}-${v}`];
      baraja.push(esp
        ? { v, palo, ...esp }
        : { v, palo, puntos_base: v, danger: dangerNormal(v), mata: '' });
    }
  }
  return baraja; // 40 cartas
}
