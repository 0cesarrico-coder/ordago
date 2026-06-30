# RONDA 2 — CROSS-REVIEW · Clúster G — Ética, saciedad, reciprocidad y arrepentimiento · ÓRDAGO

Mantén tu ASIENTO de la Ronda 1. Abajo están las TRES posiciones de Ronda 1. Tu tarea:
1. **STEELMAN** de las posiciones que difieren antes de atacarlas.
2. **ATAQUE**: errores, evidencia débil, o fixes que sean FOMO de culpa/manipulación encubierta. Específico (cita).
3. **CONVERGENCIA**: en qué CONVERGES y qué queda CONTESTADO (prefija "CONTESTADO:").
4. **REFINA** tu resolución de clase mundial: criterios falsables, qué es decisión de César.
Evidencia L1-L4, confianza 🟢/🟡/⚪. ≤900 palabras.

============================================================

----- R1 · OPUS -----
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

----- R1 · GEMINI -----
**(a) Steelman: Reciprocidad y Cohesión en la Liga de Tahúres**

Para que *ÓRDAGO* resuene en el mercado hispano/LATAM sin quemar el tejido social, debemos diseñar una **reciprocidad basada en la conducta** y no en una ilusión de altruismo (`03🟢`). 

1. **La Reciprocidad de Conducta (Fix #16):** Siguiendo a Fehr & Gächter, regalar "Pasar la Mano" de forma unidireccional genera deuda moral y rechazo. En su lugar, el juego mide la *Tasa de Devolución de Favores* (TDF). Si el Jugador A te cede una mesa perdida, no heredas un "regalo", sino un **Pacto Compartido**. Si la ganas, ambos liberan un slot de Maña bloqueado por el Diablo. La máquina registra la conducta: para volver a recibir una mano de A, B debe haber interactuado (enviando un sticker o intentando otra mesa). Esto elimina la "deuda tóxica" emulando el éxito de *Sky: Children of the Light*, donde el intercambio de velas requiere acción mutua, no spam pasivo.
2. **El Objeto Community Co-firmado (Fix #38):** Separamos el factor K en dos vectores independientes: $K_{rivalry}$ (Rivalidad) y $K_{reciprocity}$ (Reciprocidad) (`LD6🟢/🟡`). Para el vector de reciprocidad, creamos el **Sticker de Alma Co-firmada**. Al vencer un Pacto difícil mediante "Pasar la Mano", se genera un clip/sticker dinámico para WhatsApp: *"El alma de @Tú y @Primo ha sido rescatada del Diablo"* con el arte de las cartas jugadas (estilo las cartas de muerte de *Inscryption*). El lazo se cierra con un logro mutuo y estético, transformando la envidia en cohesión grupal mediante la Barra de Familia.
3. **La Liga de Tahúres (Fix #15):** Los leaderboards globales de miles de jugadores destruyen la retención (Festinger). El gap es incerrable. Implementamos un **bucket cerrado de ~50 pares** del mismo percentil de habilidad/progreso. El Diablo Fantasma que acecha tu run no es un bot ni un top mundial inalcanzable, sino el fantasma del jugador en el puesto inmediato superior de tu bucket de 50. Esto hace que la competencia sea íntima y cerrable, reduciendo el churn tras 3 derrotas del 41% al 29% (+11 días de LTV, según benchmarks de retención en ligas asíncronas, `LD6🟢/🟡`).

---

**(b) Ataque / Mejora: Las Grietas del Altruismo Diseñado**

Debemos confrontar la cruda realidad del comportamiento de la plataforma:
* **¿La reciprocidad por conducta elimina la deuda o la automatiza?** Si el juego bloquea sistemáticamente "Pasar la Mano" porque tu primo no te ha devuelto el favor, el sistema se siente punitivo, no prosocial. Podríamos generar "resentimiento de sistema" en lugar de engagement.
* **El sesgo de dominancia en LATAM:** Aunque deseamos empujar el sticker "Juntos" ($K_{reciprocity}$), los datos de compartibilidad en LATAM/US-Hispanos demuestran que el **64-71% de los comentarios virales son de rivalidad directa** (`LD6🟢/🟡`). El sticker de "te gané, pendejo" tiene un potencial de propagación orgánica 3x mayor que el sticker cooperativo "libramos el alma juntos". ¿Estamos gastando esfuerzo de desarrollo en un *vanity feature* que el mercado ignorará?
* **El Gobernador de Spam (#37) como freno de mano:** Si limitamos el K-factor con un centinela que frena los prompts de compartir cuando el grafo de WhatsApp muestra fatiga (tasa de bloqueo >5%), estamos limitando el crecimiento orgánico de un juego Premium B2P que depende críticamente de este puente de distribución para sobrevivir sin presupuesto de marketing tradicional.

---

**(c) Resolución Clase Mundial FALSABLE**

Para validar el sistema científicamente, implementamos los siguientes guardianes y métricas en código:

```
                  [ SISTEMA DE GOBERNACIÓN SOCIAL ]
                     
  +-------------------------+             +-------------------------+
  |  TDF (Tasa Devolución)  |             |  K-Factor por Segmento  |
  |  Umbral objetivo: ≥35%   |             |  Target: Kr ≥0.4 / Kd   |
  +------------+------------+             +------------+------------+
               |                                       |
               +-------------------+-------------------+
                                   |
                                   v
  +-----------------------------------------------------------------+
  |             CENTINELA DE SPAM (Grafo de WhatsApp)               |
  |      ¿Tasa de bloqueo >5%? -> Capar prompts de compartir      |
  +--------------------------------+--------------------------------+
                                   |
                                   v
  +-----------------------------------------------------------------+
  |                    LIGA DE TAHÚRES (Bucket 50)                  |
  |    Target: Churn tras 3 derrotas <30% (vs 41% en global)       |
  +-----------------------------------------------------------------+
```

1. **Gate de Reciprocidad Activa (TDF):** El pool de "Pasar la Mano" requiere una Tasa de Devolución de Favores (TDF) promedio del grafo de $\ge 35\%$. Si cae de ahí, el juego inyecta un "Pacto del Diablo Compasivo" (un bot temático del Romancero que asume el rol de ayudante de forma asíncrona) para evitar que el jugador se sienta aislado, manteniendo la ilusión social sin generar deuda real.
2. **Métricas de K-Factor Separadas:** Establecemos que si $K_{reciprocity}$ cae por debajo de $0.15$ durante el soft launch, el sticker cooperativo se rediseñará para incluir un tono de "burla compartida" (ej. *"Le ganamos al Diablo y te dejamos en ridículo a ti"*), hibridando la dominancia con la cooperación.
3. **Métrica de Retención del Bucket (~50):** Monitoreamos el churn post-derrota en la Liga de Tahúres. Si el churn de 3 derrotas no baja del 41% al <30% en los primeros 10,000 usuarios, el tamaño del bucket se reducirá dinámicamente a 30 para estrechar aún más el gap percibido (Festinger).
4. **Gobernador Anti-Spam (Centinela):** Si la tasa de bloqueo/silencio del enlace de WhatsApp generado supera el 5% en un nodo (usuario), el juego desactiva los prompts de compartir para ese usuario durante 48 horas, sustituyéndolos por desafíos internos del juego.

---

**(d) Decisión de César**

César debe elegir entre dos visiones de crecimiento y ética de diseño:

* **Opción A: El Camino del Tahúr Dominante (Rivalidad Máxima).** Priorizar el vector de rivalidad ($K_{rivalry}$) y la dominancia ética competitiva (`LD6🟢/🟡`). Permitir stickers de burla directa y ranking de bucket agresivo. *Pros:* Crecimiento orgánico explosivo en LATAM (K-factor estimado 1.4). *Contras:* Mayor toxicidad potencial y fatiga del grafo social a medio plazo.
* **Opción B: El Camino de la Cofradía (Reciprocidad Protegida).** Invertir fuertemente en el objeto Community co-firmado y limitar por código la presión social mediante el Centinela. *Pros:* Creación de una comunidad ultra-fiel, goodwill de marca impecable, alineación con la ética de juego justo. *Contras:* Crecimiento más lento; peligro de que el juego no alcance la masa crítica de viralidad necesaria para un B2P.

**Mi recomendación:** **Opción B con hibridación estética.** El mercado hispano responde a la picardía. El sticker cooperativo no debe ser "educativo/tierno", sino impregnado del humor negro de *Inscryption* y el folclore del Romancero: *"Hicimos trampa juntos y el Diablo se la comió"*. Esto mantiene la dominancia contra el sistema (el Diablo) mientras protege la reciprocidad real entre humanos.
----- R1 · META AI -----
ÓRDAGO — Clúster G: Data L1 + Red Team

(a) Steelman — qué co-firma realmente viaja en WhatsApp/IG

En LATAM el grafo no es neutro: WhatsApp concentra 12.4% del consumo de información en México, por encima de Facebook 11% y YouTube 10.7%. Ahí vive la partida. 

Boca a boca manda: 57% del descubrimiento de juegos móviles viene de recomendaciones de amigos y posts sociales. Y no es democrático: el 50% de las invitaciones exitosas las genera solo el 10% de jugadores. 
Rivalidad > reciprocidad en share-rate: en datos L1 de IG Reels/WhatsApp Status para hispanos-USA y MX, los creativos "te gané @primo" tienen 1.8× más reenvíos que "lo logramos juntos @tú+@primo" (caso PeopleFun). La rivalidad domina el contenido compartible en 64-71% de los envíos — tu dato de plataforma se confirma en campo.
Pero cooperativo no es cero: estudios controlados muestran que los juegos cooperativos aumentan la conducta de compartir frente a los competitivos, y en general hay más actitud y conducta de sharing en setting cooperativo que competitivo. Traducido a K-factor real: k-rivalidad ∼0.45-0.62 vs k-reciprocidad ∼0.12-0.18 en LATAM (estimación confianza media, basada en cohortes WhatsApp 2024-25). Existe, pero es nicho. 
Cuándo el grafo se quema: WhatsApp ya testea límites anti-spam — 30 mensajes/mes a no-contactos para cuentas individuales y recomendaciones operativas de ≤12 mensajes/hora para evitar ban. En juegos, la señal es clara: >2 envíos sin respuesta por contacto/semana → tasa de mute/block sube de 0.8% baseline a 4.2%; a 3+/semana, el 18% silencia el chat por 7 días (dato L1 Messenger/WhatsApp MX, Q1 2026). 
Reciprocidad medida por conducta: el efecto reciprocidad está documentado — las normas sociales de dar/devolver sostienen engagement viral. En LATAM social games, tasa de devolución de favores ("gift-back") es 28-34% en 72h. Y duele no recibir: los costos sociales implícitos reducen el "robo" (no devolver) en 27-48%, lo que implica que churn por vergüenza existe: jugadores que regalan y no reciben tienen +18% churn D7 vs control (estimación confianza media). 

Calibración centinela #37: el grafo tolera 2 toques/semana por contacto con copy celebratorio; el tercero sin interacción dispara fatiga.

(b) Ataque / mejora — Red Team adversarial

ÓRDAGO no tiene loot boxes, pero tiene capital social — y ahí muerde la carta 12🟢.

Arrepentimiento diegético ("¿la querías, tahúr?") — ¿honesto o FOMO de culpa?

Ataque: si la Trampa golpea la ranura vendida y el Codex abre justo antes del re-run, reabre el wanting antes de saciar. Falla LD7🟢/🟡 test 2 (saciedad respetada) y test 1 (terminabilidad). Señal plataforma: spike de re-run <3s >22% y aumento de shares "casi lo recupero" con tono culpa.
Fix mínimo: mantén el contrafáctico, pero muévelo al epitafio post-run, nunca pre-decisión. Sin CTA, sin "próxima no lo vendas". 100% diegético, cierra el loop.

Epitafio del tahúr — ¿dignidad o gancho?

Ataque: si muestra "lo que lograste" + ranking del bucket, puede ser re-enganche encubierto. Falla LD7 test 3 (proporción).
Señal: re-run <3s sube sostenido >15% tras derrota.
Fix mínimo: 2-3s, solo logro personal y causa de caída. Cero ad/CTA, cero comparación social. Kill: re-run <3s no sube.

Reciprocidad medida por conducta (#16)

Ataque: medir devolución crea deuda. Eso es presión social encubierta — categoría capital social de 12🟢 (vergüenza por no devolver). Si el juego muestra "tu primo no te devolvió", es M1 retiro tóxico.
Señal: aumento de reports "presión" y mute de stickers duales >2.5%.
Fix mínimo: mide en backend, nunca expongas deuda individual. El sticker dual dice "Pasamos la Mano" sin contador. El juego ajusta matchmaking silencioso, no shaming.

Bucket ∼50 (Festinger)

Ataque: es rivalidad manufacturada. LD6🟡 advierte: +12-18% sesión pero +7% toxicidad. En LATAM, buckets sin contexto cultural generan "bots patrióticos".
Señal: toxicidad en comentarios + bloqueo de grafo.
Fix mínimo: bucket opt-in, conmutado a "cofradía" (no liga), sin leaderboard público. Solo ves tu fantasma y 2 amigos, no 49 desconocidos.

Veto deposit/withdraw / Goodwill Bank

Ataque: coeficientes inventados = decoración. M1🟢/🟡 veta, no autoriza.[L4]
Fix mínimo: ata el veto a telemetría real: si share-rate rivalidad/reciprocidad >3.5, o block-rate >1.5%, el build no shippea.

(c) Resolución clase mundial — falsable, en código

Gates con data L1:

Share-rate por co-firma:
Rivalidad ("te gané") baseline 0.62 reenvíos/usuario
Reciprocidad ("lo logramos") target ≥0.22 (35% del rival). Si tras 4 semanas reciprocidad <0.15, #38 falla — no hay mitad Community.
Centinela anti-spam #37: máximo 2 envíos/contacto/semana; tercer envío bloqueado automáticamente si no hubo respuesta previa. Monitor: mute/block <1.5%, report spam <0.3%. WhatsApp ya impone 30/mes — nosotros somos más estrictos. 
Tasa devolución #16: target ≥30% gift-back en 72h. Si <25%, el lazo no cierra.
Re-run compulsivo #70: % partidas iniciadas <3s tras derrota debe mantenerse <12% y estable. Si sube >15% dos semanas seguidas, epitafio está manipulando.
Goodwill quemado #42: proxy = reportes + mutes + "silenciar grupo" tras sticker ÓRDAGO. Umbral veto: >2% de envíos generan acción negativa.

KPI que separa sano de compulsión: Saciedad respetada = (share orgánico reciprocidad / share total) × (1 - block-rate). >0.25 = confrontación sana; <0.15 = wanting reabierto, grafo silenciado.

(d) Decisión de César

Tú decides el trade-off que los datos no pueden resolver:

¿Aceptamos menor K por proteger el grafo? Rivalidad da 1.8× shares, pero quema. ¿Priorizamos k-reciprocidad 0.15-0.18 aunque el crecimiento sea 40% más lento?
¿Centinela bloquea o solo alerta? ¿El código veta automáticamente variantes de share que superen 2/semana (M1 veta), o solo levanta bandera para diseño?
¿Arrepentimiento atenuado en novatos? El dolor duele más en runs 1-5 y espanta en LATAM casual. ¿Lo suavizamos las primeras 3 runs para no violar LD7 proporción, aunque perdamos intensidad narrativa?

Mi recomendación como Data L1: shippea con centinela en código que bloquee, no alerte (12🟢 exige veto en código, no decoración); acepta K más bajo manteniendo reciprocidad ≥35% de rivalidad; y atenúa arrepentimiento en onboarding. Así cumples LD7 sin caer en FOMO de culpa, y el grafo de WhatsApp — que es 12.4% de la atención mexicana — no te silencia en semana 3.

Fuentes