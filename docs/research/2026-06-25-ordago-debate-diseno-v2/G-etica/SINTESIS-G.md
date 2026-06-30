# SÍNTESIS — Clúster G · Ética, saciedad, reciprocidad y arrepentimiento

> Fusión de Opus (Diseñador de Sistemas + ética en código), Gemini (crecimiento/cohesión LATAM) y Meta AI (Data L1 + Red Team). Referee R2 dictaminó **CONVERGED** (contested=8, flipped=5, consensus=8/16). Cartas ancla: 02🟢 (autonomía real), 06🟢 (dotación/loss-aversion), 12🟢 (keystone ética B2P en código), M1🟢/🟡/⚪ (goodwill veta, no autoriza), LD6🟢/🟡 (competición/cohesión), LD7🟢/🟡 (terminabilidad·saciedad·proporción).

---

## 1. Veredicto

El clúster **convergió en una espina dorsal ética compartida**: las tres máquinas (arrepentimiento faustiano terminable, cierre digno en derrota, veto goodwill en código) se especifican como mecanismos falsables, no deseos. Opus rechazó como **manipulación encubierta** tres "fixes" de crecimiento de Gemini (bot falso, burla nominal, estrechar bucket) y Meta los respaldó con data L1; Gemini no los re-defendió en R2 → se zanjan a favor de la postura ética. Lo único "vivo" (delay del epitafio, momento exacto del contrafáctico, umbrales numéricos) lo resuelve un experimento o la firma de César, no más debate.

---

## 2. Resoluciones de clase mundial por hueco

### #41/#73 — Arrepentimiento faustiano diegético, CONTRAFÁCTUAL post-run, no pre-decisión · CONSENSO 3/3 · 🟢
**Cambio GDD (§7.6d + nuevo §9.x "Codex de Arrepentimientos"):** se arma una `RegretSituation` SOLO si se cumplen las **3 condiciones** (criterios falsables, en código): (1) una Trampa del Diablo golpea una ranura **ocupada por un Pacto**; (2) en el catálogo de ESTA run existía una Fullería que **rompía exactamente esa Trampa**; (3) el jugador **no la tiene** porque vendió la ranura al Pacto. Sin las tres → no hay susurro (evita culpa ambiental; nace de dotación 06🟢 + autonomía 02🟢). Muestra la **carta** sacrificada ~0.5s (*"¿La querías, tahúr?"*), **NUNCA un número/EV/"perdiste X de daño"**. Codex terminable: 1 entrada por Pacto; al completarse, `has_experienced_regret[pact_id]=TRUE` y el susurro se **apaga permanente** (LD7🟢 saciedad).
- **Matiz no zanjado por debate (lo decide un playtest, no más rondas):** momento del beat. Meta retiró su R1 y converge con Opus en "diegético + silenciado por Codex"; queda el matiz **mid-run silencioso vs. epitafio post-run**. El gate `re-run<3s` decide: si in-situ reabre wanting (re-run sube), se mueve a post-run.
- **Gate falsable:** ✅ si en playtest una fracción de testers verbaliza *"la próxima no lo vendo"* [umbral SUPUESTO, p.ej. ≥35% ⚪ sin baseline] **Y** `re-run<3s` NO sube >12% vs control **Y** el Codex silencia el susurro al completarse. Cualquiera roto → FOMO de culpa → **kill**.

### #70 — Epitafio de derrota: logro + permiso de parar, CERO CTA · CONSENSO 3/3 · 🟢
**Cambio GDD (§9 "Catarsis", extender a la derrota):** beat de 2-3s con (a) **logro/esfuerzo** agregado ("Derrotaste a 4 Diablos · Tu mejor Escoba: 38 · sobreviviste 2 Condenas" — endowment del esfuerzo 06🟢, **nunca "te faltó 1 punto"**); (b) **cierre con permiso de parar** (*"El Diablo gana esta mano. La baraja te espera cuando quieras"*). **Prohibido por código:** CERO ad/CTA/oferta, CERO ranking/bucket/comparación social en este flujo (12🟢: no monetizar la frustración).
- **CONTESTADO vivo (Opus vs Meta) — lo zanja la métrica, no el debate:** ¿delay forzado/unskippable ~1.5s? Opus a favor ("permiso de parar"); Meta en contra con data L1 ("delays >1s en pantallas de pérdida correlacionan +9% re-run <3s = empuje, no permiso"; debe ser skipeable desde frame 1). **Se zanja con el gate `re-run<3s`**, no con más rondas.
- **Gate falsable:** ✅ si `re-run<3s` se mantiene **<12% y estable** entre builds; si sube >15% dos builds seguidos → compulsión → **revertir el beat de logro** (y, si aplica, quitar el delay).

### #16 — Reciprocidad medida por CONDUCTA como telemetría interna, NUNCA HUD de deuda · CONSENSO 3/3 · 🟢
**Cambio GDD (§ social "Pasar la Mano" + §18 telemetría):** la **Tasa de Devolución de Favores (TDF / gift-back)** se computa **solo en backend** para ajustar matchmaking silencioso. **Prohibido por código** exponer deuda individual, contador o shaming ("tu primo no te devolvió") — eso reintroduciría exactamente el tell de deuda tóxica (Fehr & Gächter; capital social de 12🟢) que el fix descarta. El sticker dual dice *"Pasamos la Mano"* sin contador.
- **Data L1 (Meta):** gift-back en social games LATAM = 28-34% en 72h; no devolver tiene costo social que reduce el "robo" 27-48%, pero regalar-sin-recibir = **+18% churn D7** → por eso la presión NUNCA se muestra; se gestiona en backend.
- **Gate falsable:** ✅ TDF ≥30% gift-back en 72h 🟡 (Meta: 28-34%); si <25% → "Pasar la Mano" no cierra el lazo, revisar. Si TDF ~0 → el bonding no existe.

### #38 — Community real co-firmada vs. solo Competition · CONSENSO 3/3 (en dirección) · 🟡
**Cambio GDD (§8.1 claim "Community" + §18 K-factor):** separar **K_rivalidad ≠ K_reciprocidad** por segmento como vectores independientes. La mitad Community se sostiene con **stickers de Alma Co-firmada** ("El alma de @Tú y @Primo fue rescatada del Diablo", arte de cartas jugadas, estilo Inscryption) — **humor negro dirigido AL DIABLO (enemigo común), no a un humano nombrado**.
- **Data L1 (Meta):** rivalidad domina el share (1.8× reenvíos "te gané @primo" vs "lo logramos juntos", caso **PeopleFun**; 64-71% de lo compartible es rivalidad; 57% del descubrimiento es boca a boca; 50% de invites exitosos del 10% de jugadores). **k-rivalidad real 0.45-0.62 vs k-reciprocidad 0.12-0.18.** → Rivalidad = motor de viralidad; reciprocidad = foso de retención. **Coexisten.**
- **CONTESTADO, resuelto contra Gemini-R1:** su target K-reciprocidad ≥0.4 es fantasía con datos actuales → **target realista 0.20-0.25** (≈35-40% de la rivalidad).
- **Gate falsable:** ✅ k-reciprocidad ≥0.20 a 4 semanas 🟡; si <0.15 → no hay mitad Community → **corregir el claim §8.1**, no fingirlo.

### #37 — Gobernador anti-spam / bloqueo del grafo, EN CÓDIGO · CONSENSO 3/3 · 🟢
**Cambio GDD (§18 centinela del grafo):** centinela que **bloquea por código, no solo alerta**. Máx **2 envíos/contacto/semana**; el 3.º se auto-bloquea si no hubo respuesta previa. Regla de copy: **celebra, no degrada**. Si **K sube pero el grafo se silencia** (block/mute suben) → **vetar la variante, no escalarla**.
- **Data L1 (Meta):** WhatsApp = 12.4% de la atención informativa en MX (recurso finito); ya impone 30 msg/mes a no-contactos y ≤12/hora anti-ban; **>2 envíos/semana sin respuesta → block sube de 0.8% a 4.2%; al 3.º, 18% silencia 7 días.** El 5% de Gemini era "tarde" → adoptamos umbral más estricto.
- **Gate falsable:** ✅ block/mute <1.5%, report-spam <0.3%; si supera → el build **no shippea**.

### #42 — Goodwill veto deposit/withdraw en code-review BLOQUEANTE · CONSENSO 3/3 · 🟢
**Cambio GDD (§proceso/CI + Ley de 3 motores §4.1):** toda feature de **retorno/share/social** lleva en su PR etiqueta falsable `goodwill: deposit | withdraw | neutral` con justificación. **M1 puede VETAR (proxy en rojo → revierte) pero NUNCA AUTORIZAR**; prohibido el argumento "el saldo aguanta" (simétrico al solver §14 del FOSO). Un `withdraw` no se mergea sin un `deposit` que lo compense en el mismo ciclo, o sin veto explícito de César. Gate de compilación: si `share-rate rivalidad/reciprocidad >3.5` **o** `block-rate >1.5%` → build **Unstable**, despliegue bloqueado; auto-rollback de la variante.

### #55 — Telemetría de fatiga atada a gate de release · CONSENSO 3/3 (dirección) · 🟡
**Cambio GDD (§18 KPI-centinela + gate de release):** KPI **para-satisfecho-vs-encadena** (paran tras cerrar vs. re-arrancan <3s) atado al gate (función de release, no disciplina). **KPI maestro de saciedad (Meta, data L1):** `(share_reciprocidad / share_total) × (1 − block_rate)` → **>0.25 = confrontación sana; <0.15 = wanting reabierto / grafo silenciado → vetar variante.**
- **Gate falsable:** ✅ ratio para-satisfecho >1.2 🟡; si <1.0 → veto. (Umbral exacto = decisión de César, abajo.)

### #15 — Bucket social ~50 pares reales del percentil · CONSENSO 3/3 · 🟢
**Cambio GDD (§18 liga/cofradía):** **bucket cerrado de ~50 pares del mismo percentil** (Festinger: comparación con semejantes motiva; el leaderboard global mata, churn ~41% post-3-derrotas). El **Diablo Fantasma** se puebla con un **PAR REAL** del bucket, no el #3.847 global ni un bot. **Sin leaderboard global público; opt-in/cofradía.** Si no hay 50 reales, el daily dice "tu mejor marca", **no inventa rivales**. Falsable: auditar que **ningún Diablo Fantasma sea sintético**.
- **CONTESTADO, resuelto contra Gemini-R1:** estrechar el bucket dinámicamente (50→30) para bajar churn = **ansiedad manufacturada** (LD6🟡: +7% toxicidad con buckets sin contexto cultural) → **prohibido re-barajar para retener.**

---

## 3. Decisiones de César (trade-offs que el dato no resuelve)

1. **Umbral de reciprocidad / ratio para-satisfecho:** dirección converge, número no (Opus ≥35%-de-rivalidad / ratio 0.35 SUPUESTO; Gemini ≥0.15; Meta ≥0.20-0.25 / ratio >1.2). **Recomendación 3/3:** empezar conservador y endurecer; **calibrar por A/B SOLO el umbral del gate, NUNCA la dirección del veto** (esa la fija la teoría M1, no el test). Firma César con datos de soft-launch.
2. **Susurro diegético (mid-run silencioso) vs. pantalla/epitafio post-run** para el contrafáctico (#41). Recomendación: susurro 0.5s + línea fría en resumen; lo zanja el gate `re-run<3s`. Tuya la elección del default.
3. **Veto goodwill: BLOQUEANTE vs. advisory.** Recomendación 3/3: **bloqueante** para retorno/share/social (12🟢/M1🟢 exigen máquina, no deseo); advisory para el resto. Tuya.
4. **Atenuar arrepentimiento en runs 1-3 de onboarding** (Meta: +18% churn D7 por vergüenza en LATAM casual 🟡; Opus/Gemini-spec prefieren rigor desde el minuto 1 por fidelidad al Romancero). Trade-off LD7-proporción vs. intensidad narrativa. **Tuya.**
5. **¿Delay forzado ~1.5s en el epitafio?** (Opus sí = permiso de parar; Meta no = +9% re-run). Lo zanja la métrica; tú firmas el default que se prueba primero.

---

## 4. Guardarraíles éticos (lo que NO se hace — los 3 fixes rechazados)

1. **NUNCA un bot falso ("Pacto/Diablo Compasivo") disfrazado de ayuda humana** para "mantener la ilusión social" (Gemini R1). Es **falsa prueba social / dark pattern**: mentir al jugador sobre la naturaleza humana de su vínculo. Viola 12🟢 (honestidad B2P) y 02🟢 (autonomía real). Rechazado por Opus, respaldado por Meta ("¿lo querrías si tu primo es un bot? No"). *Si César quiere asistencia, debe ser un NPC del Romancero CLARAMENTE identificado como bot del sistema — transparencia, no engaño.*
2. **NUNCA sticker de burla NOMINAL a un humano** ("te dejamos en ridículo a ti", Gemini R1). Burlarse **del Diablo = depósito**; burlarse de **tu primo nombrado = withdraw tóxico** (M1🟢) y presión social directa (capital social, 12🟢). El humor negro va contra el enemigo común, no contra una persona nombrada.
3. **NUNCA estrechar el bucket dinámicamente (50→30) para bajar churn** (Gemini R1). Re-barajar para mantener al jugador cerca del rival = **ansiedad manufacturada**, contrario al Festinger sano (pares reales semejantes). Prohibido re-dimensionar el bucket *para* retener.
- **Corolarios:** prohibido exponer deuda individual como HUD (#16); prohibido CTA/ad/ranking post-derrota (#70); prohibido "liberar slot de Maña por cooperación" (rompe el trade-off faustiano §7.6d); prohibido números/EV en el arrepentimiento (mostrar carta, no cifra).

---

## 5. Para el GDD v1.3 — lista accionable (§ → qué)

- **§7.6d + nuevo §9.x (Codex de Arrepentimientos):** disparador `RegretSituation` de 3 condiciones; muestra carta 0.5s sin número; `has_experienced_regret[pact_id]` apaga el susurro permanente (terminable, LD7🟢).
- **§9 (Catarsis → extender a Derrota):** epitafio 2-3s con logro/esfuerzo + permiso de parar; CERO CTA/ad/ranking por código; gate `re-run<3s` <12% estable.
- **§8.1 (claim "Community"):** condicionarlo a k-reciprocidad ≥0.20 a 4 semanas; si <0.15, corregir el claim (no fingirlo). Stickers de Alma Co-firmada (humor negro contra el Diablo).
- **§18 (telemetría/social):** TDF/gift-back solo backend (≥30%/72h, <25% revisar); K_rivalidad ≠ K_reciprocidad por segmento; centinela del grafo en código (máx 2 envíos/contacto/semana, 3.º auto-bloqueado; block/mute <1.5%, report-spam <0.3%); KPI maestro saciedad `(share_recip/total)×(1−block-rate)` >0.25 sano / <0.15 veto; bucket cerrado ~50 pares reales, Diablo Fantasma real (auditar 0 sintéticos), sin re-barajar para retener.
- **§4.1 (Ley de 3 motores) + §proceso/CI:** etiqueta `goodwill: deposit|withdraw|neutral` obligatoria en PRs de retorno/share/social; M1 veta no autoriza; veto bloqueante de compilación; auto-rollback si `share rivalidad/reciprocidad >3.5` o `block-rate >1.5%`.
- **§ gate de release:** ratio para-satisfecho-vs-encadena atado al release (umbral exacto = César).
- **Pendiente de firma de César:** umbrales numéricos (#55/#16/#38), mid-run vs post-run del contrafáctico, veto bloqueante vs advisory, atenuación de arrepentimiento en onboarding, delay del epitafio.
