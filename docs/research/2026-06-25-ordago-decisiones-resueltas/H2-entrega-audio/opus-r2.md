# OPUS R2 — Cross-review · H2 Entrega viral/audio/assets · ÓRDAGO

Asiento: Diseñador de Sistemas + arquitectura/scope. Reviso posiciones ajenas y converjo.

---

## DC-16 · Beacon stateless vs cero-backend
**STEELMAN Meta:** Su 🟢 L1 es el dato más duro del grupo: 61% reenvío nativo sin abrir link, 23% sesiones MX con datos agotados, r=0.91 localStorage↔K2. Si eso es real, un beacon mide solo el 36-42% restante y sesga hacia los conectados.
**ATAQUE/CAMBIO:** Meta confunde "medir el reenvío" con "medir la activación atribuible". Mi beacon NO intercepta el forward (imposible y no es el punto): registra `{nonce, ts}` cuando una sesión NUEVA arranca portando nonce. El 23% sin datos no abre el juego web tampoco, así que no es población perdida para K2 — es población no-activada. r=0.91 local es una correlación interna no auditable; sin ground-truth server-side ES infalsable. Pero Meta tiene razón en que el coste/ruido de fingerprinting es real → mantengo opt-in y sin PII.
**RECOMENDACIÓN FINAL:** **1 endpoint edge stateless opt-in** (nonce, sin PII/cookies) + contador local. El beacon es aditivo, mide activación no reenvío. **🟡** (lo sube a 🟢 el experimento K2). Gate KILL ya definido: <5% de sesiones nuevas portan nonce → desmantelar.

## DC-18 · SEO Engine por-seed AHORA vs diferir
**Convergencia total** (los 3 difieren): diferir engine, lanzar landing-compendio estática + medidor Search Velocity. Solo discrepa el umbral del gate (Gemini 1500, yo 500, Meta 600).
**ATAQUE:** El 1500/mes de Gemini es optimismo sin fuente; el 580 mediana L1 de Meta (MX 620/AR 540/US-Hisp 590) es el dato real para indie premium pre-launch. Fijar el gate en 1500 nunca dispara y mata una palanca viva.
**RECOMENDACIÓN FINAL:** **Diferir engine; landing estática top-100 + centinela.** Gate VERDE = **≥600 búsq/mes/región sostenido 4 semanas** (Meta L1, no mi 500 ni el 1500 de Gemini). **🟢.**

## DC-20 · Reparto sticker/clip/atribución
**STEELMAN Gemini (50/40):** el clip es el encendedor del deep-link móvil; sin peso en clip no alimentas el funnel de descubrimiento orgánico IG/Reels.
**ATAQUE:** El dato L1 de Meta lo refuta: sticker 61% reenvío vs clip 4.7% click-to-share, mute 87%. 40% en clip sobre-invierte en el canal de menor retorno viral. Meta propone 60/25/15; yo venía de 65/25/10. Diferencia = solo el split atribución, y con DC-16 confirmado como beacon real (no 100% local), 15% de esfuerzo en instrumentación se justifica más que mi 10%.
**RECOMENDACIÓN FINAL:** **60/25/15** (cedo a Meta). Sticker domina, clip secundario, atribución 15% porque el beacon de DC-16 sí necesita instrumentación de producto. **🟡** (gobernado por G2: si clip ≥4.5× share-con-audio, rebalancear a 50/35/15).

## DC-21 · Nodos de grito: cuántos y cuáles
**STEELMAN Meta (3 nodos):** tiene el dato L1 que yo pedía en R1: frase local +2.1× share (MX 2.2/Caribe 2.3/US-CA 2.0), Rioplatense solo 1.4× y colisiona semánticamente con Truco. Costo 3× = $1,800 vs $600, trivial frente a CAC≈0.
**STEELMAN Gemini (AR en vez de Caribe):** Río de la Plata = hogar del Truco, ancestro de ÓRDAGO. Pero Meta lo mata con dato: 1.4× share y colisión semántica → AR es el peor nodo para el GRITO viral (aunque sea buen mercado de juego).
**ATAQUE a mi propio R1:** dije MX+Caribe (2 nodos) "hasta tener baseline". Meta APORTÓ ese baseline (L1). Mi condición de falsación era exactamente "si US-CA da ≥2× share, añadir 3er nodo" — Meta reporta 2.0×. Mi propia regla me obliga a ceder.
**RECOMENDACIÓN FINAL:** **3 nodos: MX + Caribe + US-Centroamericano** (no AR para el grito). **🟢** dado el L1 de Meta. Test tri-nodo confirma post-launch (KILL nodo <1.5×).

## DC-22 · Textura de Sospecha completa vs MVP diferido
**STEELMAN Gemini (diferir):** con mute 87%, gastar en textura ambiental que solo oye el 13% es mal ROI; concentrar audio-awe en el pico del money-shot.
**ATAQUE:** Falacia de coste hundido invertida — la capa YA está diseñada; diferir paga el coste de re-abrir el sistema de audio post-launch (más caro). Meta aporta el dato decisivo: con el techo (banda ∉[500-2k], gain ≤0.8) los reportes "audio molesto" bajan -34% y eyes_closed_test 78%. El techo en código convierte el riesgo ético en invariante testeable por CI, no en promesa.
**RECOMENDACIÓN FINAL:** **Lanzar completa CON techo desde día 1** (3 invariantes como assert en CI). **🟡** — gate de código + test ciego de Meta (VERDE: eyes_closed ≥75% Y quit ≤baseline). Coincido con Meta, contra Gemini.

## DC-23/24 · grito_glifo en caption + emoji-artefacto
**Convergencia de los 3:** glifo en imagen Y caption copiable; emoji-artefacto = línea estática garantizada + 1 evento analítico. Discrepancia menor: Gemini sugiere "UI copiable", Meta y yo decimos estática + evento.
**ATAQUE:** Meta aporta el porqué L1: WhatsApp sanitiza metadata .webp y congela 1er frame → el caption-texto es el ÚNICO vector buscable que sobrevive (forward con texto +22%). Emoji 9.8% share = red de seguridad, no 3er canal (si >20% canibaliza el sticker).
**RECOMENDACIÓN FINAL:** **Glifo en imagen + caption copiable estático; emoji-artefacto línea estática + 1 evento.** UI copiable dinámica solo si copy-rate >15% sostenido. **🟢.**

## DC-25 · Nº money-shots full al lanzamiento
**Convergencia de los 3:** lanzar con **5**, expandir 6º-8º bajo doble gate, tope duro en 8 (no 20).
**ATAQUE/refuerzo:** Meta aporta el mecanismo de fatiga L1: frequency >2.7/7d → CTR -31% a día 14; 5 jefes = cadencia 17.8 días (cubre la ventana); share-to-wishlist frío 0.033 → 0.018 tras 10 creadores (<0.02 = kill). Esto valida mi tope duro: expandir sin gate es "live-ops encubierto".
**RECOMENDACIÓN FINAL:** **5 money-shots; expansión 6-8 SOLO si G2 ≥4.5× share-con-audio 0-72h Y G3 ≤0.8 d-h/dosis. Tope duro 8.** **🟢.**

## DC-26 · 3 vs 4 plantillas de beat
**STEELMAN Meta+Gemini (3 plantillas):** Meta L1 es contundente — refrescar background +4% CTR (ns) vs cambio de CONCEPTO +28% reset de fatiga; recodificación WebP pierde 62% detalle, lo que importa es el Diablo jugable físico (resquebraja/tinta), no la 4ª plantilla. El budget de la 4ª no compra reset adicional.
**CAMBIO (cedo):** mi 4 plantillas asumía "variedad percibida marginal" sin dato; Meta muestra que la variedad que resetea fatiga es de CONCEPTO, no de plantilla — y 3 conceptos distintos > 4 plantillas similares. La 4ª no aporta si comparte rig (que era mi argumento de que era barata — pero barata-e-inútil sigue siendo gasto).
**RECOMENDACIÓN FINAL:** **3 plantillas de beat**, budget concentrado en BEAT+SONIDO + Diablo jugable a fidelidad de render. **🟡** (Meta L1 me hace ceder de 4→3; gobernado por G3).

## DC-27 · ¿Condena endless suma dosis de awe?
**STEELMAN Meta/Gemini (NO):** Meta L1 — jefe #10 endless cae -19% share vs #1 (rompe G1 ≤15%), G3 sube a 1.1 d-h/dosis (>0.8), habituación supera novedad. Gemini: endless diluye el clímax narrativo del Diablo.
**ATAQUE/matiz:** Mi R1 (sí, condicional a G3) y su NO convergen en la práctica: yo dije "suma awe SOLO mientras G3 aguante" — Meta muestra que G3 NO aguanta (1.1 > 0.8) y el share cae -19%. Es decir: mi propia condición se incumple → mi recomendación condicional colapsa al NO. No hay contradicción real, hay un dato que cierra mi condicional en negativo.
**RECOMENDACIÓN FINAL:** **No incluir condena endless como fuente de dosis de awe al lanzamiento.** El endless puede existir como modo de juego, pero NO se le asigna producción de money-shots/dosis (rompe G3 y G1 por dato L1). Reabrir solo si cohorte 14d muestra caída ≤12% Y G3 ≤0.8. **🟡** (cedo mi condicional ante el L1 de Meta).

---

**Síntesis de mi asiento:** Mi aporte de arquitectura (invariantes en código, beacon sin-PII, gate G3 contra live-ops encubierto) se mantiene y de hecho se refuerza: el techo de DC-22 y el tope de DC-25 son asserts testeables, no promesas. CEDÍ en 4 decisiones ante el L1 de Meta (DC-20 a 60/25/15, DC-21 a 3 nodos, DC-26 a 3 plantillas, DC-27 al NO), porque mi propio criterio de falsación de R1 se cumplió con su dato. Mantengo firme DC-16 (beacon, contra Meta) y DC-22 (completa+techo, contra Gemini) porque ahí la arquitectura verificable gana al "100% local infalsable" y al "diferir más caro".
