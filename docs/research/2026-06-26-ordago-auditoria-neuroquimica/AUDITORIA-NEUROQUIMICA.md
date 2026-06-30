# ÓRDAGO v1.3.1 — Auditoría de principios de psicología · neuroquímica · emoción

> **Pregunta:** ¿el GDD ya tiene los MEJORES principios para un juego **adictivo Y satisfactorio**?
> **Método:** 10 auditores en paralelo, uno por sistema neuroquímico/emocional, anclado a su(s) carta(s)
> del `game-design-brain`, midiendo cobertura en la v1.3.1 + el balance adicción↔satisfacción + huecos.
> **Fecha:** 2026-06-26.

## Veredicto global

**SÍ — y de forma poco común.** 10/10 sistemas presentes; **9 a clase-mundial, 1 sólido**; promedio **~90/100**.
Lo raro: ÓRDAGO no solo *incluye* los principios — **cablea la LÍNEA entre adicción sana y compulsión en CÓDIGO**
(no en buena intención). Internaliza la distinción **wanting≠liking (Berridge)**: pone la incertidumbre/RPE en la
HABILIDAD (liking), no en loot monetizado (wanting); confina el variable-ratio al meta-loop y deja el core
**determinista por skill**; y diseña la **saciedad** como invariante (Codex terminable, epitafio con permiso de parar,
veto goodwill en CI, los 10 "NUNCA"). Es B2P sin MTX → esquiva las trampas de F2P por construcción.

## Tabla de scores

| # | Sistema | Carta(s) | Nivel | Score | Hueco |
|---|---------|----------|-------|-------|-------|
| 1 | Dopamina / RPE / schedules | 00, 05 🟢 | clase-mundial | **93** | pity-timer/bad-luck-protection sin número (micro-GDD) |
| 2 | Competencia / maestría / flow | 01, 04 🟢 | clase-mundial | **90** | sin DDA (deliberado); falta nudge para que suban de Codicia |
| 3 | Autonomía / SDT | 02 🟢 | clase-mundial | **88** | autonomía SOCIAL escasa (no eliges a quién retar) |
| 4 | Loss-aversion / dotación | 06 🟢 | clase-mundial | **92** | Endowed Progress Effect no cableado (barras desde 0) |
| 5 | Curiosidad / SEEKING / FOMO | LD5, LD7, 07 🟢 | clase-mundial | **91** | ninguno material; nombrar los 3 tests LD7 como gate |
| 6 | **Hook / hábitos D1/D7** | 08 🟢/🟡 | **sólido** | **82** | **el único gran sistema SIN gate falsable + no reconcilia premium vs F2P** |
| 7 | Juice / game-feel | 09 🟢 | clase-mundial | **92** | sin gate de la U-invertida (juice medio vs extremo); háptico sin fallback |
| 8 | Tensión / riesgo / alivio | 10 🟢/🟡 | clase-mundial | **93** | telemetría del arco de ansiedad no falsable (fatiga por sobre-tensión) |
| 9 | Social / oxitocina / identidad | 03, 11 🟢 | clase-mundial | **92** | regalo unidireccional podado; pertenencia a grupo débil |
| 10 | **Ética adicción↔satisfacción (EJE CRÍTICO)** | 12, LD7, M1 🟢 | clase-mundial | **91** | sin gate de sesión-maratón/tiempo (vulnerabilidad adulta) |

**Promedio ≈ 90.4 / 100.**

## Lo que está de clase mundial (los diferenciadores)

1. **El eje adictivo↔satisfactorio resuelto, no maximizado.** La mayoría de los juegos maximizan la adicción;
   ÓRDAGO maximiza "adictivo **Y** satisfactorio". Los 3 tests falsables de LD7 (terminabilidad / saciedad /
   proporción) los **aprueba los tres** con número; el Goodwill Bank de M1 es **veto bloqueante en CI**, no deseo.
2. **wanting≠liking aplicado correctamente.** Incertidumbre sana (RPE de habilidad/exploración) en el CORE;
   variabilidad solo en el META; recompensa garantizada de fondo. No se monetiza la incertidumbre.
3. **Maestría legible + techo que CRECE, medible por solver** (S5/S7, delta lookahead_k vs greedy) — rarísimo
   verlo falsable en un GDD.
4. **Tensión/alivio de manual:** arco de Sospecha de 3 tiempos, near-miss "te la paso tahúr" (paradoja verificada
   de Clark 2009), riesgo DECIDIBLE no dado oculto, alivio recompensado, curva serrada pico↔valle.
5. **Pérdida anclada SIEMPRE a algo genuinamente ganado** (la carta capturada, el Pacto equipado) + cobro con
   dignidad + cierre digno en derrota sin CTA. Loss-aversion para PROTEGER, no para vender miedo.

## Patrón transversal en los huecos (el verdadero hallazgo)

El patrón que la v1.3 mató en la capa de ENTREGA (foso/puente/audio/ética con umbral V/🟡/KILL) tiene un
**residuo en la capa EMOCIONAL/ENGAGEMENT**: cuatro sistemas siguen como "máquina sin gate falsable":
- **Hook D1/D7** (#6) — el más material: sin invariante propio + sin reconciliar que en premium el D1/D7 es
  **proxy de viralidad/Playtime-Depth, NO KPI de retención-para-monetizar**.
- **Game-feel** (#7) — sin gate de la zona Medio-Alto de la U-invertida de Kao (juice medio vs extremo).
- **Arco de ansiedad** (#8) — sin KPI-centinela de fatiga por sobre-tensión (p.ej. abandono tras N pillados).
- **Uso compulsivo por tiempo** (#10) — sin nudge/gate de sesión-maratón (el único eje de LD7/12 sin invariante).

## Plan de cierre (todo barato — instrumentación + 4 adiciones menores; NADA de cimiento)

**P1 — convertir los 4 sistemas emocionales en invariantes falsables (igual que el resto):**
- §8.4: gate del lazo D1/D7 (umbral V/🟡/KILL de "% retorno D7 atribuible a trofeo vs daily vs artefacto") +
  nota de aplicabilidad premium (D1/D7 = proxy de viralidad/Playtime-Depth, no retención-para-monetizar).
- §10: gate de game-feel (A/B juice medio vs extremo sobre tiempo de juego / motivación, replicando Kao) +
  presupuesto numérico "juice/segundo" análogo al `C ≤12/mano`.
- §9/§18: KPI-centinela de fatiga del arco de Sospecha (abandono tras N pillados seguidos).
- §18.1/§19.5: gate de sesión-maratón (nudge tras N runs seguidas) — cierra la vulnerabilidad adulta por tiempo.

**P2 — adiciones baratas de alto retorno:**
- **Endowed Progress Effect** (#4): barras del Codex/Codicia que arrancan con casillas regaladas, nunca en 0/N.
- **Autonomía social opt-in** (#3): elegir qué semilla/Diablo del grafo enfrentar entre 2-3, o curar qué trofeo
  exhibe la Cantina — elección significativa, sin romper "0 sintéticos / una escalera real".
- **pity-timer invisible** (#1): bad-luck-protection numerado en el botín de la Cantina (micro-GDD).
- Nombrar los **3 tests de LD7** como aserción explícita junto a los gates D30 (trazabilidad).

**P3 — post-1.0:** loop de regalo unidireccional puro (la oxitocina más barata, hoy podada) + pertenencia a
grupo persistente (gremio/familia con barra común).

## Conclusión

El diseño neuroquímico/emocional de ÓRDAGO **ya es de clase mundial** y, sobre todo, está del lado correcto de la
línea: **adictivo de forma sana y satisfactoria**, con la ética cableada en código. Lo que falta NO son principios
nuevos — es **instrumentar 4 sistemas emocionales como gates falsables** (cerrar el mismo patrón que la v1.3 ya
aplicó a la entrega) + 4 adiciones baratas. Ninguna toca el cimiento.
