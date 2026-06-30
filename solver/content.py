"""
ÓRDAGO — Contenido del prototipo (fuente de verdad para el solver).
Implementa EXACTAMENTE los números de design/MICRO-GDD-prototipo.md.
Mantener sincronizado con game/src/content.js (el prototipo web reusa estos números).
"""
from dataclasses import dataclass

# --- Palos ---
OROS, COPAS, ESPADAS, BASTOS = "O", "C", "E", "B"
PALOS = [OROS, COPAS, ESPADAS, BASTOS]
PALO_NOMBRE = {OROS: "Oros", COPAS: "Copas", ESPADAS: "Espadas", BASTOS: "Bastos"}

# Valores de Escoba: 1..7 + Sota(8) Caballo(9) Rey(10)
VALORES = list(range(1, 11))  # 1..10
NOMBRE_VALOR = {8: "Sota", 9: "Caballo", 10: "Rey"}


@dataclass(frozen=True)
class Carta:
    v: int           # valor de Escoba (1..10)
    palo: str        # O/C/E/B
    puntos_base: int # peso de puntuación
    danger: int      # peligro negado al Diablo si la capturas (eje Defensa)
    mata: str = ""   # id de Mata si es legendaria

    @property
    def id(self):
        return f"{self.v}{self.palo}"

    def __repr__(self):
        nom = NOMBRE_VALOR.get(self.v, str(self.v))
        return f"{nom}{self.palo}"


# --- Matas (legendarias, §7.5) — base alta + efectos ---
MATAS = {
    ("E", 1): dict(puntos_base=13, danger=6, mata="as_espadas"),   # ×1.3 Suerte al capturar
    ("B", 1): dict(puntos_base=11, danger=6, mata="as_bastos"),    # +6 Puntos en bloque
    ("E", 7): dict(puntos_base=10, danger=5, mata="siete_espadas"),
    ("O", 7): dict(puntos_base=9, danger=5, mata="siete_oros"),    # +2 Reales
}


def _danger_normal(v: int) -> int:
    if v >= 9:   # Caballo, Rey
        return 3
    if v >= 6:
        return 2
    return 1


def construir_baraja():
    """40 cartas: 4 palos × valores 1..10 (figuras 8/9/10)."""
    baraja = []
    for palo in PALOS:
        for v in VALORES:
            esp = MATAS.get((palo, v))
            if esp:
                baraja.append(Carta(v=v, palo=palo, **esp))
            else:
                baraja.append(Carta(v=v, palo=palo,
                                    puntos_base=v, danger=_danger_normal(v)))
    assert len(baraja) == 40
    return baraja


# --- Trampas del Diablo (§3.1) ---
# target_override: cambia el objetivo de suma; oros_bloqueados: Oros no capturables;
# primer_robo_nulo: la 1ª Escoba del Envite puntúa 0.
TRAMPAS = {
    "T1_trece":        dict(nombre="El Trece", target_override=13),
    "T2_oros_malditos": dict(nombre="Oros Malditos", oros_bloqueados=True),
    "T3_primer_nulo":  dict(nombre="Primer Robo Nulo", primer_robo_nulo=True),
}

# --- Fullerías (§3.2) — ocupan ranura de Maña ---
FULLERIAS = {
    "F1_lectura_falsa": dict(nombre="Lectura Falsa", rompe="T1_trece", comodin_figura=True),
    "F2_contrabando":   dict(nombre="Contrabando", rompe="T2_oros_malditos", permite_oro=True),
    "F3_doble_filo":    dict(nombre="Doble Filo", rompe="T3_primer_nulo", primera_x2=True),
    "F0_ojo":           dict(nombre="Ojo del Tahúr", rompe=None, solucionador=True),  # maestría
}

# --- Pactos Oscuros (§3.3) — ocupan ranura de Maña toda la run ---
PACTOS = {
    "P1_oro":    dict(nombre="Pacto del Oro", afinidad=OROS,    add_por_palo=3),
    "P2_filo":   dict(nombre="Pacto del Filo", afinidad=ESPADAS, mult_si_palo=1.4),
    "P3_bosque": dict(nombre="Pacto del Bosque", afinidad=BASTOS, add_por_carta=2),
}

# --- Estructura: Manga 1 (§4) — umbrales a calibrar por el solver (S5) ---
APUESTAS_MANGA1 = [
    dict(id="chica",  umbral=228, manos=5, trampa=None),
    dict(id="grande", umbral=378, manos=6, trampa=None),
    dict(id="envite", umbral=358, manos=7, trampa="T1_trece"),  # la Trampa se fija por seed
]

# Penalización al Envite por "comer la Trampa en crudo" (sin la Fullería que la rompe).
# Brutal a propósito (§7.6d auto-balance): el poder puro (0F) no debe muscular el Envite.
TRAMPA_PENALTY = 0.55       # ×score base en el Envite si la Trampa NO está rota (piso, progresivo)
TRAMPA_F3_BONUS = 1.12      # Doble Filo: pequeño bonus si rompes T3
ESCOBA_BONUS_FLAT = 16      # bonus plano por captura — el Escoba base es el término DOMINANTE
                            # (como en Balatro la mano base puntúa; Pactos/Fullerías son modificadores)

MESA_MIN, MESA_MAX = 5, 6   # tamaño de Mesa sostenido por la siembra
MESA_INICIAL = 4
MANO_TAM = 3
TARGET_BASE = 15
ESCOBA_LIMPIA_BONUS = 5

# Builds extremas a falsar (S4, §3.4)
BUILDS_EXTREMAS = {
    "0F_3P": ["P1_oro", "P2_filo", "P3_bosque"],
    "3F_0P": ["F1_lectura_falsa", "F2_contrabando", "F3_doble_filo"],
    "2P_1F": ["P1_oro", "P2_filo", "F1_lectura_falsa"],
    "1P_2F": ["P1_oro", "F1_lectura_falsa", "F2_contrabando"],
    # builds de control adicionales
    "filo_x2F": ["P2_filo", "F2_contrabando", "F3_doble_filo"],
    "bosque_mix": ["P3_bosque", "P1_oro", "F2_contrabando"],
}
