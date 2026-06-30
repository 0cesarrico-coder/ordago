# Opus — Ronda 1 · Clúster G: Ética, saciedad, reciprocidad y arrepentimiento

> Asiento: Diseñador de Sistemas + ética en código. Las tres máquinas que lidero —arrepentimiento faustiano diegético, cierre digno en derrota, veto deposit/withdraw en code-review— se especifican como **mecanismos falsables**, no como deseos. Cito cartas con su confianza. Donde el GDD no dice nada, lo marco **[SUPUESTO]**.

---

## (a) Steelman — spec de las 3 máquinas

### Máquina 1 — Arrepentimiento faustiano diegético (#41/#73)

El trade-off ya existe (§7.6d: un Pacto ocupa una ranura toda la run = la maña que le vendiste al Diablo). Lo que falta es el **espejo del contrafáctico**. Spec:

- **Disparador exacto (falsable, en código):** se arma una `RegretSituation` SOLO cuando se cumplen **las tres** condiciones simultáneas — (1) una Trampa del Diablo golpea una ranura que está **ocupada por un Pacto** (no una vacía, no una con Fullería); (2) en el catálogo de Fullerías de ESTA run existía una Fullería que **habría roto exactamente esa Trampa**; (3) el jugador **no la tiene equipada porque vendió la ranura al Pacto**. Sin las tres, no hay susurro. Esto evita el arrepentimiento "ambiental" (culpa de fondo): el arrepentimiento solo aparece cuando la elección del jugador (02🟢, autonomía REAL) produjo el daño concreto. Nace de **dotación + autonomía**, no de culpa impuesta.
- **Qué muestra el contrafáctico:** un beat breve y diegético —el Diablo voltea la Fullería-que-rompía y la enseña medio segundo: *"¿La querías, tahúr?"*— y la vuelve a guardar. **No** un panel de daño, **no** "perdiste X de EV". Muestra el **camino no tomado** (la carta), no un castigo numérico.
- **Cierre "El Camino que Vendiste":** en el resumen de run aparece UNA línea por Pacto vendido que se volvió contra ti, fría y elegante: *"Vendiste la ranura de [Fullería] por [Pacto]. El Diablo cobró."* Es inventario de decisiones, no reproche. **[SUPUESTO]** el copy exacto.
- **Codex "Arrepentimientos":** colección **terminable** (LD7🟢: terminabilidad · saciedad · proporción). Cada Pacto tiene UN arrepentimiento desbloqueable la primera vez que te muerde; una vez completo, **deja de aparecer el susurro** (la saciedad se respeta — no "siempre falta una culpa"). Es un bestiario de tus propias trampas, no un loop de FOMO.

Por qué es sano (12🟢, test maestro "¿lo querría si entendiera el diseño?"): un jugador que entiende el diseño **quiere** que el juego le restriegue lo que sacrificó —es lo que hace Inscryption/StS y lo que convierte el cálculo de spreadsheet en drama. Lo querría porque **él** eligió vender la ranura.

### Máquina 2 — Epitafio del tahúr (#70, cierre digno en derrota)

§9 da catarsis al GANAR pero nada al perder, y la dotación (06🟢) hace que la **derrota** pese más (te confiscó tu mejor carta). Spec del beat de 2–3 s:

- **Estructura:** (a) **logro** — "Derrotaste a 4 Diablos · Tu mejor Escoba: 38 · Sobreviviste a la Condena 2 veces" (endowment del **esfuerzo**, no del trofeo); (b) **cierre** — una línea de permiso para parar: *"El Diablo gana esta mano. La baraja te espera cuando quieras."* Luego el botón de reintento aparece **después** del beat, nunca antes.
- **Reglas duras (en código):** **CERO** ad/CTA/oferta post-derrota (12🟢 B2P: no review-bait, no monetizar la frustración). El "reintentar" no se pre-resalta ni se auto-enfoca durante los 2–3 s. El beat **no se puede skipear** los primeros ~1.5 s (da permiso de parar; no lo conviertas en pared de fricción — ver ataque).

### Máquina 3 — Veto deposit/withdraw en code-review (#42/#55/#37)

El FOSO tiene gate-en-código (solver §14); la saciedad/goodwill no. La igualamos:

- **Clasificación obligatoria:** toda feature de **retorno, share o social** lleva en su PR una etiqueta falsable `goodwill: deposit | withdraw | neutral` con justificación. M1 (M1🟢/🟡/⚪) **puede VETAR** (proxy en rojo → revierte) pero **NUNCA AUTORIZAR**; prohibido el argumento "el saldo aguanta" (simétrico a la Ley de 3 motores §4.1). Un `withdraw` no se mergea sin un `deposit` que lo compense en el mismo ciclo, o sin veto explícito de César.
- **#55 — KPI-centinela atado a gate de release:** ratio **para-satisfecho-vs-encadena** (jugadores que paran tras cerrar vs. los que re-arrancan <3 s). Si cae bajo umbral, **el build no pasa** (función de release, no disciplina). [SUPUESTO] umbral exacto.
- **#37 — gobernador del grafo:** centinela de **sentimiento-spam / tasa-de-bloqueo** del grafo en §18 (sensor superior al proxy K_grafo). Regla de copy: *celebra, no degrada*. Si **K sube pero el grafo se silencia** (bloqueos/mutes suben) → vetar la variante, no escalar.
- **Community real como depósitos (#38/#16/#15):** reciprocidad medida **por conducta** (#16: tasa de devolución de favores tras "Pasar la Mano"), no por proxy de oxitocina; **k-factor de RECIPROCIDAD separado del de RIVALIDAD por segmento** en §18 (#38); **bucket persistente ~50 pares por percentil** (#15) que puebla el Diablo Fantasma con un PAR real, no con el #3.847 global (Festinger: el leaderboard global mata). Estos tres son los `deposit` que sostienen la mitad Community.

---

## (b) Ataque / mejora (atacándome a mí mismo)

1. **"¿La querías, tahúr?" ¿es FOMO de culpa encubierto?** Riesgo real (cruza 12/LD7). Cruza la línea si: (i) aparece en ranuras vacías o con Fullería (culpa ambiental); (ii) se repite tras completar el Codex (no satura → viola LD7🟢 saciedad); (iii) usa lenguaje de pérdida fabricada ("perdiste 40 de daño") en vez de mostrar el camino. **Fix:** las 3 condiciones del disparador + el Codex que **silencia** el susurro al completarse + mostrar la **carta**, no el número. Si no satura, es dark pattern (LD7🟢).

2. **El epitafio "lo que lograste" ¿re-engancha manipulando?** Sí, si el logro está calibrado para picar el ego ("¡tan cerca!") o si el reintento se pre-enfoca. Cruza la línea cuando el beat pasa de **dar permiso de parar** a **empujar a seguir**. **Fix:** métrica de control (c) — si re-run <3 s **sube sostenido**, el epitafio se volvió compulsión y se revierte. El logro reporta esfuerzo agregado, nunca "te faltó 1 punto".

3. **Medir reciprocidad por conducta ¿reintroduce presión de deuda?** Este es el ataque más fino. #16 quería **evitar** la señal de deuda (Fehr & Gächter: regalar sin recibir = deuda). Si la *tasa de devolución* se le **muestra al jugador** ("le debes 2 a tu primo"), reintroducimos exactamente el tell de deuda que descartamos. **Fix duro:** la tasa de devolución es **métrica interna de salud del bonding (telemetría)**, JAMÁS un HUD ni un nudge al jugador. Mide bonding real sin presionarlo.

4. **El bucket ~50 ¿liga sana o manufacturada?** Sano = comparación con **pares reales** de tu percentil (Festinger: comparación con semejantes motiva). Manufacturado/oscuro = si rellenamos con bots disfrazados de humanos o si el bucket se re-baraja para mantenerte ansioso. **Fix:** bucket poblado por **humanos reales del grafo/percentil**; si no hay 50 reales, el daily dice "tu mejor marca", no inventa rivales. Falsable: auditar que ningún Diablo Fantasma sea sintético.

---

## (c) Resolución clase mundial — gates binarios falsables

- **Arrepentimiento:** ✅ si en playtest **≥35% [SUPUESTO]** de testers verbaliza *"casi lo recupero"* / *"la próxima no lo vendo"* **Y** el re-run compulsivo / ansiedad reportada **NO** sube vs. control. Si sube ansiedad → es FOMO de culpa → kill.
- **Epitafio:** ✅ si re-run <3 s tras derrota **NO sube sostenido** entre builds. Sube sostenido → compulsión → revertir el beat de logro.
- **Veto:** ✅ **ninguna** feature de retorno/share pasa code-review sin etiqueta `deposit/withdraw`; build **no pasa** si centinela para-satisfecho-vs-encadena <umbral; si K sube **y** el grafo se silencia → variante **vetada** (no escalada).
- **Reciprocidad (#16):** ✅ **tasa de devolución de favores** medida como telemetría interna (no HUD); si ~0 → el bonding no existe, revisar "Pasar la Mano".
- **Community (#38):** ✅ **k-factor de reciprocidad separado del de rivalidad por segmento**; si k-reciprocidad ~0 → **corregir el claim §8.1** ("Community") en vez de fingirlo.

---

## (d) Decisión de César (trade-offs que SOLO él decide)

1. **Explicitud del contrafáctico:** **susurro diegético** (mi recomendación — el Diablo voltea la carta medio segundo) **vs. pantalla dedicada** "El Camino que Vendiste". Recomiendo susurro + línea fría en el resumen; la pantalla dedicada arriesga cruzar a culpa (LD7). **Tuya la decisión.**
2. **Veto deposit/withdraw: ¿bloqueante de merge o advisory?** Recomiendo **bloqueante** para features de retorno/share/social (es el único modo de que sea máquina y no deseo, 12🟢/M1🟢), **advisory** para el resto. **Tuya.**
3. **Coeficientes del Goodwill Bank (capa-instrumento, coef. [L4]):** recomiendo **fijarlos a ojo al inicio** y **re-calibrar por A/B** solo el umbral del gate de release una vez haya datos — no calibrar por A/B la dirección del veto (eso lo decide la teoría M1, no el test). **Tuya la calibración.**
4. **Umbral del centinela para-satisfecho-vs-encadena (#55):** qué ratio bloquea el build. Recomiendo empezar conservador y endurecer. **Tuya.**

---

### Confianza de la entrega
Cartas ancla: 06🟢 (dotación/loss-aversion, versión descriptiva WTA>>WTP), 02🟢 (SDT/autonomía real), M1🟢/🟡/⚪ (goodwill veta pero no autoriza), LD7🟢/🟡 (saciedad: terminabilidad·saciedad·proporción), 12🟢 (keystone, ética B2P en código). Marcados **[SUPUESTO]:** copys exactos, umbrales numéricos (35%, ratios de gate). Todo lo demás se ancla al GDD provisto.
