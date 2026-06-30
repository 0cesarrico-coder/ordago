# DECISIONES RESUELTAS · ÓRDAGO — Consolidado del debate multi-IA (H1·H2·H3)

> Fusión fiel de las tres síntesis de sub-debate (H1 onboarding/Codex, H2 entrega/audio, H3 ética/feel).
> Tres asientos por debate: Opus (Diseñador de Sistemas / elegancia) · Gemini (Retención/Valor B2P) · Meta-AI (Data L1 + Red Team móvil LATAM).
> No se inventa consenso: lo que una silla mantuvo contestado tras R2 sigue contestado, con su experimento pre-comprometido.

---

## 1 · Resumen ejecutivo

De las ~22 decisiones que César dejó abiertas tras la v1.3, el debate resolvió **22**: **11 a consenso 3/3** (DC-4, DC-8, DC-9, DC-11, DC-18, DC-21, DC-23/24, DC-25, DC-26, DC-27, DC-3, DC-30 — nota: el bloque suma 12 porque DC-23/24 va fusionada y DC-30 fue unánime), **6 a mayoría 2/3** (DC-6 que cerró 3/3 en R2 partiendo de mayoría, DC-16, DC-20, DC-22, DC-28, DC-32 — las dos últimas como convergencia 2/3), y el resto quedó **resuelto pero con experimento pre-comprometido que puede revertir el default** (DC-5 continuo-vs-capítulos, DC-1 híbrido auto-sabotaje, más los kill-gates de cada fila). **4-5 decisiones siguen siendo firma irreducible de César**: DC-16 (arquitectura cero-backend vs beacon), DC-1 (casting de los 2-3 Pactos-ancla con cicatriz), DC-32 (affordance del epitafio: skipeable vs 0s+botón), DC-28 (número fino de reciprocidad 0.25 vs 0.22) y el tono/identidad del tahúr. La dirección de los vetos éticos (H3) es inviolable en todos los casos; el debate solo calibra magnitud.

**Conteo por estado:**
- **Consenso 3/3:** 12 filas (DC-4, DC-8, DC-9, DC-11, DC-18, DC-21, DC-23/24, DC-25, DC-26, DC-27, DC-3, DC-30). DC-6 entró como mayoría y cerró 3/3 en R2.
- **Mayoría 2/3 (o convergencia 2/3):** 5 filas (DC-16, DC-20, DC-22, DC-28, DC-32).
- **Contestado → experimento pre-comprometido (default fijado, A/B puede revertir):** DC-5, DC-1 (más el experimento que acompaña a cada fila resuelta).
- **Firma irreducible de César:** DC-16, DC-1, DC-32, DC-28 + tono/identidad del tahúr.

---

## 2 · Tabla maestra de decisiones resueltas

### Grupo H1 — Onboarding, Codex y Progresión

| DC | Tema | Recomendación FINAL | Estado | Conf. | Kill / experimento |
|----|------|---------------------|--------|-------|--------------------|
| **DC-4** | Denominador onboarding | Tutorial serializado: 7 reglas en 3 micro-mangas, ≤5 verbalizadas en Manga 1; Pactos emergen en Manga 2-3 por compresión-arquetipo. NO se podan. | **Consenso 3/3** | 🟢 | Gate compuesto: fullería-con-Pacto sin ayuda ≥80% Y verbalizadas ≤5 Y TTW p50 ≤165s. Kill: D1 <35% o TTW p50 >180s → podar a 5 core. |
| **DC-5** | Run continuo vs capítulos | Run continuo [25-35]min con auto-save por turno + "victoria parcial" explícita al cerrar cada manga. | **Contestado → experimento** (2/3 continuo: Opus+Gemini; Meta sostiene 4 mangas×6-8min) | 🟡 | A/B n≥4.000 móvil LATAM. Gate: resume-rate 24h ≥65% Y mediana sesión ∈[25-35]min. Si Meta-paredes gana resume-rate ≥3pp (o continuo <50%) → capítulos. |
| **DC-6** | Cardinalidad Codex | N=12 base / M=18 total, 2-3 capas de revelación por entrada. | **Mayoría 2/3 → 3/3 en R2** (Gemini cedió N=16/24→12/18; Opus ratificó) | 🟢 | A/B n≥6.000 LATAM Android, N12 vs N16. Subir a 16 SOLO si ≥7% completado a D30 Y abandono 80-99% <5%. Si falla uno, N=12 inamovible. |
| **DC-8** | Recompensa 100% Codex | Estrictamente estética (cantar de ciego completo + skin/marco/taunt). NO boss mecánico. | **Consenso 3/3** | 🟢 | Boss-en-solver prohibido por elegancia, no por A/B. Si estética inerte (90→100 <20%): recompensa meta FUERA del solver, nunca boss. |
| **DC-9** | Hook 90s vs 120s | 90s para `time_to_first_fullería_jugada` p50; banda-muerte dura >120s. | **Consenso 3/3** | 🟢 | Gate seguridad: comprensión-de-primera-jugada ≥85%. Si comprensión cae >10pp vs 120s → subir a 120s. |
| **DC-11** | Poda Diablo Fantasma + artefacto-puente | Podar del onboarding; reintroducir como meta gateado tras consolidar el core (post-Manga 1-2) + teaser visual. NUNCA regla verbalizada antes de Manga 1. | **Consenso 3/3 en el principio; timing contestado** (Opus post-M1 / Meta post-M2 / Gemini post-1ª-run) | 🟢 | Gate: 0 sistemas-meta nombrados antes de Manga 1 Y D1-return ≥ rama-teaser. Si D1-after-win <50% → revelación cinemática post-victoria. |

### Grupo H2 — Entrega viral, audio y assets

| DC | Tema | Recomendación FINAL | Estado | Conf. | Kill / experimento |
|----|------|---------------------|--------|-------|--------------------|
| **DC-16** | Beacon vs cero-backend | Cero-backend: atribución 100% `localStorage` (regla "generó sticker <24h"; UTMs locales en caption). NO beacon edge. | **Mayoría 2/3** (Meta+Gemini cero-backend; Opus mantuvo beacon opt-in aditivo) | 🟡 | Reabrir beacon SOLO si discrepancia >15% entre K2 local y cohorte server-side, o block-rate >0.3% por fingerprinting. |
| **DC-18** | SEO Engine por-seed | Diferir el engine; lanzar SOLO landing-compendio estática curada (top-100 seeds, cron $0) + medidor centinela Search Velocity. | **Consenso 3/3** | 🟢 | Activar engine si Search Velocity ≥600 búsq/mes/región sostenido 4 semanas (MX/AR/US-Hisp). KILL/diferir: <400. |
| **DC-20** | Reparto sticker/clip/atribución | 60 / 25 / 15 (sticker / clip / atribución). | **Mayoría 2/3** (Opus cedió a 60/25/15; Meta=60/25/15; Gemini osciló) | 🟡 | Rebalancear a 50/35/15 si el clip supera G2 ≥4.5× share-con-audio 0-72h. |
| **DC-21** | Nodos de grito (cuántos/cuáles) | 3 nodos: MX "¡No manches!" + Caribe "¡Échale!" + US-Centroamericano "¡Dale!". (NO Rioplatense para el grito.) | **Consenso 3/3** (Opus pasó de 2→3 tras L1 de Meta) | 🟢 | Test tri-nodo 7d, n=3k/variante. VERDE: ≥2.0×. KILL nodo: <1.5× share baseline. |
| **DC-22** | Textura de Sospecha (completa vs diferida) | Lanzar completa CON techo en código día 1 (`suspicion_gain ≤ 0.8·master`, banda ∉ [500Hz,2kHz], `audio_layers_active ≤ 2`) como asserts CI. | **Mayoría 2/3** (Opus+Meta completa+techo; Gemini diferir a filtro básico) | 🟡 | Test ciego 48h, n≥200. VERDE: eyes_closed ≥75% Y quit ≤baseline. KILL/diferir: falla cualquiera, o >20% reporta "estresante-negativo". |
| **DC-23/24** | grito_glifo en caption + emoji-artefacto | Glifo en imagen Y caption copiable (estático) + línea emoji-artefacto Wordle-style estática garantizada + 1 evento analítico de copia. (NO UI copiable dinámica.) | **Consenso 3/3** | 🟢 | UI copiable dinámica SOLO si copy-rate >15% sostenido. Emoji canibaliza si share >20%. |
| **DC-25** | Nº money-shots full al lanzamiento | Lanzar con 5 money-shots de jefe; expandir 6º-8º SOLO bajo doble gate. Tope duro en 8 (no 20). | **Consenso 3/3** | 🟢 | Expandir si candidato G2 ≥4.5× share-con-audio 0-72h Y G3 ≤0.8 d-h/dosis. KILL beat: share-to-wishlist <0.02. |
| **DC-26** | 3 vs 4 plantillas de beat | 3 plantillas de CONCEPTO (no 4); budget concentrado en BEAT+SONIDO y en el Diablo jugable a fidelidad de render. | **Consenso 3/3** (Opus cedió 4→3 ante L1 de Meta) | 🟢 | Bajar/ajustar si la rotación por concepto no resetea fatiga, o si G2 del clip del Diablo <3% share. |
| **DC-27** | ¿Condena endless suma dosis de awe? | No en 1.0: el endless puede existir como modo, pero NO se le asigna producción de money-shots/dosis de awe. | **Consenso 3/3** (Opus cedió su condicional ante el dato) | 🟢 | Reabrir SOLO si cohorte 14d (n=5k) muestra caída de share ≤12% Y G3 ≤0.8 sostenido. |

### Grupo H3 — Ética, Pactos y feel (dirección de vetos INVIOLABLE; solo se calibra magnitud)

| DC | Tema | Recomendación FINAL | Estado | Conf. | Kill / experimento |
|----|------|---------------------|--------|-------|--------------------|
| **DC-1** | Auto-sabotaje en Pactos | Híbrido: motor emergente por default + cicatriz acoplada-a-mano en 2-3 Pactos-ancla. | **Contestado → síntesis** (Gemini/Meta acoplado; Opus R1 emergente; Opus R2 cierra híbrido) | 🟡 | Gate: `recall_correcto_run1 ≥60%` (MX n=3k) Y `dominant_build_share <0.25` Y `working_set ≤ presupuesto S6`. Si recall <60% → acoplar más; si S6 se desborda → reducir acoplados. |
| **DC-3** | Dial suerte↔skill (peso) | Suerte gobierna top-funnel (CTR/share/UA, ~70/30 en creatividades); skill gobierna el cuerpo del loop y ~100% del LTV/D30. | **Consenso 3/3** | 🟢 | Falsador: si `D30 correlaciona con varianza de seed` > que con métricas de decisión → motor mal. Cohorte D30: win-rate ajustado vs seed-luck. |
| **DC-28** | Umbral de reciprocidad | Arranque en 0.25 (calibrar al alza si la saciedad baja). | **Convergencia 2/3 → 0.25** (Opus R2 cayó a 0.22; Gemini y Meta-R2 en 0.25) | 🟡 | A/B oculto 0.20/0.25/0.30; escalar celda con `saciedad ≥0.18` Y `block <1.2%`. Si saciedad <0.15 → subir; si fabrica bloqueos legítimos → bajar. **Solo el número, nunca la dirección.** |
| **DC-29** | Susurro del arrepentimiento | Epitafio post-run (diferido), nunca mid-run; muestra carta, no número. | **Contestado → resuelto** (Gemini mid-run vs Opus/Meta post-run; 2 asientos + 2 datos L1 zanjan post-run) | 🟢 | Gate: `re-run<3s ≤13%`. Si post-run sube re-run<3s >15% → es compulsión, se atenúa/quita. |
| **DC-30** | Veto goodwill: bloqueante vs advisory | Bloqueante (veto invariante de compilación; M1 veta, nunca autoriza — "el saldo aguanta" prohibido). | **Consenso 3/3** (guardarraíl fundacional; no se somete a test de monetización) | 🟢 | Gate CI: build Unstable + auto-rollback si `share rivalidad/reciprocidad >3.5` O `block/mute ≥1.5%`. El falsador toca SOLO el umbral, jamás la dirección. |
| **DC-31** | Atenuar arrepentimiento en runs 1-3 | Frecuencia OFF (hasta 0% susurros) en runs 1-3; texto / fidelidad al Romancero intactos siempre. | **Contestado → síntesis** (Meta-R2 OFF 100%; Gemini no-atenuar; Opus cierra "OFF de frecuencia, texto íntegro") | 🟢 | A/B onboarding control-on vs off runs 1-3 (n≈5k MX). Gate: `churn D7 ≤38%`; si cohorte-frecuencia-plena `churn D7 > +12%` vs control → frecuencia aún más baja. Nunca se falsea el texto. |
| **DC-32** | Delay forzado ~1.5s en epitafio | Delay 1.5s SKIPEABLE desde frame 1 (permiso de parar sin secuestrar el control). | **Convergencia 2/3 → skipeable** (Meta-R2 cedió a 1.5s skipeable; Gemini forzado; Opus R2 a 0s+botón) | 🟡 | 3 celdas A/B: 0s / skipeable / forzado. Aceptar delay solo si `re-run<3s ≤13%` (o baja de >22% a <14%) sin subir churn D1. Si skipeable iguala al forzado → volver a 0s. |

---

## 3 · Lo que SIGUE siendo firma de César (irreducible a apetito/dato)

- **DC-16 — Arquitectura cero-backend vs beacon (🟡, único contestado de H2):** el dato L1 LATAM favorece cero-backend (un beacon captaría <36% de eventos por forward nativo de WhatsApp), pero la pregunta de fondo —"¿aceptas volar a ciegas en atribución de ignición con tal de mantener el moat de cero-servidor?"— es apuesta de producto. *Default sugerido del panel:* cero-backend duro (Meta+Gemini); Opus deja abierto un beacon edge opt-in sin PII como señal aditiva.
- **DC-1 — Casting de los 2-3 Pactos-ancla con cicatriz acoplada:** la síntesis fija el híbrido (emergente por default + cicatriz a mano en pocos Pactos), pero *qué* Pactos merecen la cicatriz narrativa memorable (la "ceguera", etc.) y cuáles viven emergentes es elección de diseño anclada al Romancero. *Default sugerido:* 2-3 Pactos-ancla con cicatriz, el resto emergente, sujeto al gate de recall ≥60% / working-set S6.
- **DC-32 — Affordance del epitafio (skipeable vs 0s+botón):** empate de *feel* — la pausa, ¿se siente como respeto al duelo o como fricción? La mayoría R2 quedó en "1.5s skipeable frame-1"; Opus R2 derivó a "0s + botón explícito de salir". *Default sugerido:* 1.5s skipeable frame-1, las 3 celdas A/B deciden. El **tono de cierre** (crujido de cartas, "La baraja te espera") es autor puro.
- **DC-28 — Número fino de reciprocidad (0.25 vs 0.22):** el arranque exacto está entre el L1 de Meta (0.22) y el punto premium de Gemini (0.25). *Default sugerido:* arrancar en 0.25 y dejar que el A/B de saciedad lo afine. La **dirección del veto es inviolable**; solo se calibra magnitud.
- **DC-20 — Los 15 puntos de atribución (🟡, atado a DC-16):** si César elige cero-backend duro, esos 15 puntos podrían replegarse al sticker (postura 70/25/5 de Gemini). Decisión derivada de su llamada en DC-16.
- **Tono / identidad del tahúr** (cantar de ciego, Mesa viva, folklore del Romancero): estética irreducible. Las IAs optimizan retención; la voz del producto la pone César.
- **Topes de capacidad de pipeline (DC-25/27, ⚪):** el "tope 8" de money-shots y el N por sprint del endless quedan abiertos hasta que César confirme la capacidad real del pipeline de arte.

---

## 4 · Anotaciones para el GDD v1.3 (§19.3 — Lista de decisiones de César)

```
DC-1  → RESUELTO (reco): Híbrido — motor emergente por default + cicatriz acoplada en 2-3 Pactos-ancla [contestado→síntesis, 🟡; casting de los anclas = firma César]
DC-3  → RESUELTO (reco): Suerte gobierna top-funnel (~70/30 creatividades); skill gobierna loop y ~100% LTV/D30 [Consenso 3/3, 🟢]
DC-4  → RESUELTO (reco): Tutorial serializado 7 reglas en 3 micro-mangas, ≤5 verbalizadas en Manga 1; Pactos emergen M2-3; NO podar [Consenso 3/3, 🟢]
DC-5  → RESUELTO (reco): Run continuo [25-35]min + auto-save por turno + victoria-parcial por manga [contestado→experimento 2/3, 🟡]
DC-6  → RESUELTO (reco): Codex N=12 base / M=18 total, 2-3 capas de revelación por entrada [Mayoría 2/3→3/3 en R2, 🟢]
DC-8  → RESUELTO (reco): Recompensa 100% Codex estrictamente estética; NO boss mecánico [Consenso 3/3, 🟢]
DC-9  → RESUELTO (reco): Hook 90s para time_to_first_fullería_jugada p50; >120s = banda-muerte [Consenso 3/3, 🟢]
DC-11 → RESUELTO (reco): Podar Diablo Fantasma del onboarding; meta gateado post-Manga 1-2 + teaser visual; 0 reglas-meta verbalizadas antes de Manga 1 [Consenso 3/3 en principio, timing contestado, 🟢]
DC-16 → RESUELTO (reco): Cero-backend, atribución 100% localStorage; NO beacon edge [Mayoría 2/3, 🟡; arquitectura = firma César]
DC-18 → RESUELTO (reco): Diferir SEO engine; landing-compendio estática curada + centinela Search Velocity [Consenso 3/3, 🟢]
DC-20 → RESUELTO (reco): Reparto 60/25/15 (sticker/clip/atribución) [Mayoría 2/3, 🟡; atado a DC-16]
DC-21 → RESUELTO (reco): 3 nodos de grito — MX "¡No manches!" + Caribe "¡Échale!" + US-CA "¡Dale!"; NO Rioplatense [Consenso 3/3, 🟢]
DC-22 → RESUELTO (reco): Textura de Sospecha completa CON techo en código día 1 (asserts CI) [Mayoría 2/3, 🟡]
DC-23/24 → RESUELTO (reco): grito_glifo en imagen + caption copiable estático + línea emoji-artefacto estática + 1 evento de copia; NO UI copiable dinámica [Consenso 3/3, 🟢]
DC-25 → RESUELTO (reco): Lanzar 5 money-shots de jefe; expandir 6º-8º bajo doble gate; tope duro 8 [Consenso 3/3, 🟢; tope = capacidad pipeline (⚪)]
DC-26 → RESUELTO (reco): 3 plantillas de CONCEPTO (no 4); budget a BEAT+SONIDO y Diablo jugable a fidelidad de render [Consenso 3/3, 🟢]
DC-27 → RESUELTO (reco): Endless SIN producción de money-shots/dosis de awe en 1.0 [Consenso 3/3, 🟢]
DC-28 → RESUELTO (reco): Umbral de reciprocidad arranca en 0.25 (calibrar al alza si baja saciedad) [Convergencia 2/3, 🟡; número fino = firma César; dirección inviolable]
DC-29 → RESUELTO (reco): Epitafio post-run (diferido), nunca mid-run; muestra carta, no número [contestado→resuelto, 🟢]
DC-30 → RESUELTO (reco): Veto goodwill BLOQUEANTE (invariante de compilación; M1 veta, nunca autoriza) [Consenso 3/3, 🟢]
DC-31 → RESUELTO (reco): Frecuencia OFF (hasta 0%) de susurros en runs 1-3; texto/Romancero intactos siempre [contestado→síntesis, 🟢]
DC-32 → RESUELTO (reco): Delay 1.5s SKIPEABLE desde frame 1 en epitafio [Convergencia 2/3, 🟡; affordance + tono de cierre = firma César]
```
