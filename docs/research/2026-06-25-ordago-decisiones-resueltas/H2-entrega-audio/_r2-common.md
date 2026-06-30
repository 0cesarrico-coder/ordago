# RONDA 2 — CROSS-REVIEW de RESOLUCIÓN · H2 — Entrega viral, audio y assets · ÓRDAGO

Abajo están las TRES posiciones de Ronda 1 (Opus, Gemini, Meta AI), cada una comprometida con UNA opción por decisión. Tu tarea, manteniendo tu ASIENTO:
1. **STEELMAN** la postura ajena más fuerte en cada decisión donde difieras.
2. **ATAQUE**: por qué tu opción gana (dato/carta), o dónde la ajena es mejor y CAMBIAS.
3. **CONVERGE**: para CADA decisión, da la **recomendación final UNA opción** + confianza 🟢/🟡/⚪. Si genuinamente solo un experimento la cierra, dilo con el experimento + umbral (marca "CONTESTADO:").
4. NO te quedes en "depende de César": comprométete con la mejor recomendación dado lo que sabes.
Evidencia L1-L4. ≤850 palabras.

============================================================

----- R1 · OPUS -----
# OPUS R1 — Grupo H2 "Entrega viral, audio y assets" (a ciegas)

Rol: Diseñador de Sistemas + arquitectura/scope. Comprometo UNA opción por decisión.

---

## DC-16 · Beacon stateless vs cero-backend
**(a) DECISIÓN:** Construir **1 endpoint edge stateless opt-in** (nonce encadenado, sin cuentas, sin PII, sin cookies) Y conservar el contador local en `localStorage`. Punto medio: el beacon es *aditivo*, no el sistema de verdad.
**(b) PORQUÉ + confianza 🟡:** El moat "0 servidor" de Meta protege coste y privacidad, pero TODO el modelo de ignición (DC-17/K2: medir activación atribuible del artefacto-puente) muere sin una señal server-side mínima — `localStorage` no cruza dispositivos ni sobrevive al reenvío del sticker, que es justo el evento viral (reenvío >60%, click <5%). Un beacon edge (Cloudflare Worker, sin estado de identidad, ~$0 a este volumen) registra solo `{nonce, ts, geo-coarse}` y deja intacto el "0 servidor de juego". Arquitectura: el estado de juego sigue 100% cliente; solo la *atribución de ignición* toca el edge. Que el moat sea "cero backend de JUEGO", no "cero telemetría". Ancla: doctrina de ignición DC-17/K2 exige medir K-factor; sin atribución, K2 es infalsable.
**(c) QUÉ LA FALSARÍA:** Si <5% de los puentes generan un beacon válido (consentimiento opt-in demasiado friccionado) → el endpoint no mide nada útil y vuelvo a 100% local + estimación por proxy (instalaciones vs descargas de pack). También me falsa: si el edge worker introduce >50ms p95 o cualquier requisito de PII por compliance.
**(d) EXPERIMENTO:** Reusar **K2** (medición de K-factor de ignición). VERDE: ≥30% de sesiones nuevas portan nonce atribuible y K medido con IC estable; KILL: <5% portan nonce → desmantelar endpoint, atribución por proxy. n: primeras 5k activaciones / ventana 0-30 días.

## DC-18 · SEO Engine por-seed AHORA vs diferir
**(a) DECISIÓN:** **Diferir** el engine por-seed. Construir ahora SOLO: (1) **medidor de Search Velocity** (centinela), (2) **UNA landing-compendio estática** top-100 seeds (cron diario, $0).
**(b) PORQUÉ + confianza 🟢:** Web search confirma May-2026 Core Update **deindexa páginas programáticas en días** y marzo-2026 castiga "scaled content abuse" con caídas 50-80% — generar miles de páginas por-seed casi-idénticas ES el patrón doorway/"{{city}} swap" penalizado. Una landing estática curada (contenido real, no plantilla) es seguro y traiciona menos el 0-servidor (un HTML por cron). El engine por-seed se *gana* con demanda probada, no se asume.
**(c) QUÉ LA FALSARÍA:** Search Velocity supera el gate (demanda real de búsqueda por nombre de seed) Y Google publica guía que exente compendios curados con datos únicos → entonces construir engine *paginado* (no 1-página-por-seed) con consolidación canónica.
**(d) EXPERIMENTO:** Reusar **gate Search Velocity** (centinela T-14d). VERDE: ≥500 búsquedas/mes orgánicas de cadenas tipo "órdago [seed]" en región MX+US-hispano sostenidas 8 semanas → habilitar engine. KILL/mantener-diferido: <500/mes. Sin experimento nuevo; el gate ya está definido.

## DC-20 · Reparto sticker/clip/atribución
**(a) DECISIÓN:** **65 / 25 / 10** (sticker / clip / atribución).
**(b) PORQUÉ + confianza 🟡:** El cuello de viralidad es el sticker autocontenido (reenvío >60% vs click <5%): coste marginal de un sticker extra es bajísimo y su retorno viral es el más alto, así que pesa más que mi 70 inicial pero respeto el dato de Meta de que el clip-encendedor merece más que 25 mal-repartido. Atribución baja a 10 porque con DC-16 ya es 1 endpoint barato; no necesita esfuerzo de producto, solo de instrumentación. Converjo entre mi 70/30 y el 60/25/15 de Meta hacia 65/25/10.
**(c) QUÉ LA FALSARÍA:** Si el clip resulta ser el verdadero motor de instalación (G2 del clip ≥4.5× y el sticker no convierte a destino) → rebalancear a 50/40/10.
**(d) Sin experimento dedicado:** es asignación de esfuerzo, gobernada por G2 (DC-25). Comprometido ya.

## DC-21 · Nodos de grito: cantidad y cuáles
**(a) DECISIÓN:** **2 nodos: MX + Caribe.**
**(b) PORQUÉ + confianza 🟡:** El grito ES lenguaje → cada nodo es una unidad de QA/localización con coste real (casting, mezcla, regresión de audio), no un asset reskinneable. Coste 3× del 3er nodo (US-Centroamericano de Meta) no está justificado *al lanzamiento* sin baseline de share local; MX+Caribe cubre el grueso de LATAM+hispano-USA. La firma melódica global ya da cohesión; el 3er nodo es expansión post-señal, no scope de 1.0.
**(c) QUÉ LA FALSARÍA:** Dato L1 de Meta de que US-Centroamericano da **+2.1× share local** se confirma en cohorte real → añadir 3er nodo (es la palanca de Meta y la respeto si trae el dato).
**(d) EXPERIMENTO:** A/B de share-con-audio por nodo en cohortes regionales. VERDE para 3er nodo: US-Centroamericano proyecta ≥2× share local sobre el grito MX en su geo; KILL: <1.3×. n: ≥1k impresiones con audio/geo, ventana 0-30 días. (Si Meta ya tiene este dato L1, lo cierra sin experimento.)

## DC-22 · Textura de Sospecha completa al lanzamiento vs MVP diferido
**(a) DECISIÓN:** **Lanzar completa CON el techo del clúster** (`suspicion_audio_gain ≤ 0.8*master`, banda ∉[500Hz,2kHz], `audio_layers_active ≤ 2`). **Cedo mi "diferir".**
**(b) PORQUÉ + confianza 🟡:** Mi objeción era riesgo ético (capa atada a "perder" = posible coerción afectiva) y coste. El techo en código *neutraliza* el riesgo ético convirtiéndolo en invariante verificable, no en promesa: una línea de assert que CI puede testear. Coste marginal de una capa ya diseñada < coste de re-abrir el sistema de audio post-lanzamiento. La doctrina audio-amplificador (mute 85-90%) significa que esta capa es para el 10-15% con audio, donde la textura de tensión sí aporta awe.
**(c) QUÉ LA FALSARÍA:** Si playtest muestra que la capa correlaciona con sesiones-de-tilt/abandono frustrado (no tensión placentera) → diferir y rediseñar. Umbral: si en encuestas post-derrota >20% reporta la capa como "estresante-negativo" vs "tenso-bueno".
**(d) Sin experimento dedicado nuevo:** los 3 invariantes ya son el gate; se verifican por test de código, no por A/B. Comprometido.

## DC-23/24 · grito_glifo en caption + emoji-artefacto
**(a) DECISIÓN:** (23/24-A) **Ambos**: el `grito_glifo` va en la imagen Y como texto copiable en el caption. (23/24-B) **Línea estática garantizada** (no UI copiable dinámica) + **1 evento analítico** de copia.
**(b) PORQUÉ + confianza 🟡:** Glifo en caption = redundancia barata que sobrevive a recompresión de la imagen (WhatsApp recomprime WebP; texto no se degrada) y es buscable/copiable → alimenta el loop de DC-18. La UI copiable dinámica es pipeline pesado (estado, render, edge-cases de portapapeles cross-OS) sin retorno probado; la línea estática garantiza el 100% de los casos a coste ~0. 1 evento analítico basta para medir si alguien copia.
**(c) QUÉ LA FALSARÍA:** Si el evento analítico muestra tasa de copia >15% sostenida → invertir en UI copiable dinámica (la demanda justificaría el pipeline).
**(d) Sin experimento dedicado:** decisión de scope; el evento analítico *es* la instrumentación que la gobierna. Comprometido.

## DC-25 · Nº de money-shots full al lanzamiento
**(a) DECISIÓN:** **Lanzar con 5 money-shots de jefe.** Regla de expansión: subir a 6º-8º SOLO si superan **G2 (≥4.5× share-con-audio del clip diario en 0-72h)** Y **G3 (≤0.8 días-hombre/dosis)**. **Tope duro en 8. No 20.**
**(b) PORQUÉ + confianza 🟡:** Mi postura (5 = piso de retención, no techo de adquisición; UGC necesita variedad) y el 5 de Meta convergen en "5 ahora + expansión gobernada". El 5 cubre retención; la variedad extra solo se paga si *se gana* el doble gate. El tope en 8 evita "live-ops encubierto" (scope infinito sin techo).
**(c) QUÉ LA FALSARÍA:** Si los 5 saturan (fatiga de UGC: share-con-audio cae >40% semana-a-semana con solo 5) ANTES de tener candidatos que pasen G2/G3 → adelantar producción del 6º como retención, no como adquisición.
**(d) EXPERIMENTO:** Reusar **G2 + G3**. VERDE (expandir): candidato ≥4.5× share-con-audio 0-72h Y ≤0.8 d-h/dosis. KILL (no expandir): falla cualquiera. n: ventana 0-72h por dosis. Definidos en síntesis; no invento.

## DC-26 · Reparto de arte del money-shot: 3 vs 4 plantillas de beat
**(a) DECISIÓN:** **4 plantillas de beat** (matriz 4×N), con el presupuesto concentrado en **BEAT+SONIDO** y en el **Diablo jugable** (reacción física: se resquebraja como cerámica, libera tinta) a fidelidad de render; el resto de la matriz mínimo viable.
**(b) PORQUÉ + confianza 🟡:** 4 beats dan variedad de "momento de awe" sin explotar el scope (4×N reusa cuerpos/fondos). El gasto debe ir donde el ojo se fija en mute: el impacto del beat y la reacción física del Diablo (lo que se vuelve GIF/sticker). 3 plantillas dejan el feed monótono antes de tiempo; 5+ es gasto sin variedad percibida marginal. La 4ª plantilla es barata si comparte rig.
**(c) QUÉ LA FALSARÍA:** Si la 4ª plantilla cuesta >0.8 d-h/dosis (rompe G3) o el A/B no distingue 3 vs 4 en retención de clip → bajar a 3.
**(d) Sin experimento dedicado nuevo:** gobernado por G3 (coste/dosis). Comprometido a 4 mientras G3 aguante.

## DC-27 · ¿Condena endless suma dosis de awe?
**(a) DECISIÓN:** **Sí, condicional y con techo duro.** La condena endless añade dosis de awe **SOLO mientras G3 (≤0.8 días-hombre/dosis) aguante**, con un **tope de N dosis fijado por sprint** (live-ops encubierto PROHIBIDO: nada de cola infinita de contenido sin gate).
**(b) PORQUÉ + confianza 🟡:** Nadie refutó mi condición. El endless es un multiplicador de awe barato *si reusa* assets/beats existentes; se vuelve trampa de scope si cada dosis pide arte nuevo. La regla dura (G3 + tope por sprint) lo mantiene como amplificador, no como treadmill de producción.
**(c) QUÉ LA FALSARÍA:** Si las dosis de endless empiezan a costar >0.8 d-h cada una (dejan de reusar) o el equipo entra en cadencia de "contenido perpetuo" no gateado → congelar el endless en su N actual.
**(d) EXPERIMENTO:** Reusar **G3 (≤0.8 d-h/dosis)** como gate por dosis + tope numérico por sprint (p.ej. ≤3 dosis/sprint ⚪ — número supuesto; lo subiría a 🟢 un dato de capacidad real del pipeline de arte). Comprometido al principio; el tope exacto lo fija capacidad observada.

---

**Lo que solo yo aporté (arquitectura/scope):** convertí dilemas de "principio" en invariantes verificables en código (techo de audio como assert testeable en DC-22; beacon edge sin-PII que preserva el moat "0 servidor de juego" en DC-16) y até CADA expansión de contenido (DC-25/26/27) al gate de coste G3 para prohibir el "live-ops encubierto" por construcción, no por promesa.

**Vacíos (qué necesito para cerrar los 🟡):** de **Meta** — el dato L1 de share local de US-Centroamericano (cierra DC-21 a 2 o 3) y la tasa real de copia de caption/fatiga de UGC con 5 shots (DC-25/23-24); de **Gemini** — si el clip-encendedor puede ser destino de instalación medible (recalibra el 65/25/10 de DC-20) y la capacidad real del pipeline de arte que fija el tope por sprint de DC-27.

----- R1 · GEMINI -----
**DC-16 · Beacon stateless vs cero-backend**
- **(a) DECISIÓN:** Implementar un único endpoint stateless en Edge (Cloudflare Worker).
- **(b) PORQUÉ + confianza:** 🟢 (D1). Medir la atribución local y el coeficiente viral $K2$ es innegociable para optimizar la conversión a Steam. Un enfoque 100% "cero-servidor" nos deja ciegos de atribución de conversión; un Worker stateless no añade bases de datos ni rompe la ligereza del "moat".
- **(c) QUÉ LA FALSARÍA:** Incremento de rebote $>15\%$ en la carga de la web-demo por cold start del Worker.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

**DC-18 · SEO Engine por-seed AHORA vs diferir**
- **(a) DECISIÓN:** Diferir el SEO Engine completo; construir solo la landing estática (top-100 seeds) y el gate centinela (T-14d).
- **(b) PORQUÉ + confianza:** 🟢 (Riesgo SEO Google 2026/soft-404). Si el algoritmo de Steam detecta "tráfico frío" que rebota, hundirá la conversión en el Next Fest. El umbral del Gate Centinela se fija en Search Velocity $\ge 1,500$ búsquedas/mes en MX/AR para activar páginas dinámicas.
- **(c) QUÉ LA FALSARÍA:** Conversión Search-to-Wishlist en Next Fest $<1:0.02$.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

**DC-20 · Reparto de esfuerzo sticker/clip/atribución**
- **(a) DECISIÓN:** Fijar el reparto en 50% sticker / 40% clip / 10% atribución.
- **(b) PORQUÉ + confianza:** 🟡 (D1 + A2). El clip en Reels/IG actúa como el encendedor del deep-link, pero el sticker autocontenido es el puente de adquisición de valor a largo plazo. Necesitamos peso en clips para alimentar el funnel de descubrimiento orgánico móvil.
- **(c) QUÉ LA FALSARÍA:** Ratio de compartidos del clip (G2) $<2.5\times$ en las primeras 100 publicaciones orgánicas.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Prueba G2 (target: $\ge 4.5\times$ share-con-audio del clip en 0-72h; $n=10$ creadores).

**DC-21 · Nº de nodos de grito: 2 vs 3 y CUÁLES**
- **(a) DECISIÓN:** Implementar 2 nodos: México (MX) y Rioplatense (AR/UY).
- **(b) PORQUÉ + confianza:** 🟢 (Foso mecánico/cultural). Río de la Plata es el hogar del *Truco*, ancestro directo de las mecánicas de ÓRDAGO. El volumen de búsqueda y retención de mecánicas de engaño en AR/UY asegura una conversión orgánica superior a la de cualquier nodo centroamericano.
- **(c) QUÉ LA FALSARÍA:** Conversión de tráfico rioplatense a wishlist en Next Fest $<1.5\%$.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

**DC-22 · Textura de Sospecha completa al lanzamiento vs MVP diferido**
- **(a) DECISIÓN:** Diferir la textura completa; lanzar con un filtro básico paso-alto/bajo dinámico.
- **(b) PORQUÉ + confianza:** 🟡 (D3 bajo mute-default de feeds LATAM). El $85-90\%$ del feed se consume silenciado. El diseño de audio-awe (A2) debe concentrarse en el pico visual del money-shot, no en costosas texturas de sospecha ambiental que pasan desapercibidas en el scroll móvil.
- **(c) QUÉ LA FALSARÍA:** Caída de retención en la web-demo de $>25\%$ en los primeros 3 minutos de juego.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

**DC-23/24 · grito_glifo en caption + emoji-artefacto**
- **(a) DECISIÓN:** Implementar grito_glifo en caption copiable y la línea de emoji-artefacto estática en UI con 1 evento analítico.
- **(b) PORQUÉ + confianza:** 🟢 (D1 + indexación de Google). El texto copiable en caption genera valor de búsqueda indexable (SEO asíncrono). La línea estática garantiza compatibilidad y ligereza absoluta para el $23\%$ de usuarios móviles en LATAM que carecen de redes de alta velocidad.
- **(c) QUÉ LA FALSARÍA:** Click-Through-Rate (CTR) de copiar al portapapeles $<3\%$ en web-demo.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

**DC-25 · Nº de money-shots full**
- **(a) DECISIÓN:** Lanzar estrictamente con 5 money-shots de jefes y expandir a 8 solo si se valida la retención de dosis.
- **(b) PORQUÉ + confianza:** 🟢 (G-conversión / Hades benchmark). 5 money-shots optimizan los costes de producción iniciales. La expansión a un 6º-8º jefe estará estrictamente supeditada a que el clip mantenga los estándares de viralidad sin saturar al espectador.
- **(c) QUÉ LA FALSARÍA:** Caída de la conversión de wishlist de creadores (G-conversión) a $<0.02$ tras la exposición de 10 creadores independientes.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Test de G-conversión (target: 1:0.03-0.04 en frío; $n=1,000$ clics; 7 días).

**DC-26 · Reparto de arte del money-shot: 3 vs 4 plantillas**
- **(a) DECISIÓN:** Producir solo 3 plantillas y redirigir el presupuesto restante a pulir la física de "Destrucción Cerámica y Liberación de Tinta" del Diablo.
- **(b) PORQUÉ + confianza:** 🟢 (A2 / Hades ~3.4× wishlist). La conversión del espectador a wishlist ocurre en la resolución estética y visceral de la derrota (la muerte física del jefe), no en la variedad visual de los menús o textos de las plantillas.
- **(c) QUÉ LA FALSARÍA:** Ratio de compartidos del clip del Diablo resquebrajándose (G2) $<3\%$.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

**DC-27 · ¿Condena endless suma dosis de awe?**
- **(a) DECISIÓN:** No incluir condena endless al lanzamiento.
- **(b) PORQUÉ + confianza:** 🟡 (G3 $\le 0.8$ d-h/dosis). El modo endless diluye el pico dramático y de tensión narrativa del enfrentamiento final contra el Diablo. El valor de evangelización asíncrona depende de clímax claros, no de loops infinitos de desgaste.
- **(c) QUÉ LA FALSARÍA:** Tiempo de sesión medio en la web-demo $<4$ minutos durante la fase beta.
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** Comprometerse ya.

---
**Lo que solo yo aporté:** El análisis de canibalización algorítmica en Steam por redirección de tráfico de búsqueda frío de baja intención (Next Fest conversion drop).
**Vacíos para Opus/Meta:** Requiero que Opus valide los límites de latencia en Edge para el Worker de DC-16, y que Meta certifique el coste de assets 3D/tinta del Diablo para DC-26.
----- R1 · META AI -----
ÓRDAGO R1 · Data L1 + Red Team. Lidero con cifras de plataforma WhatsApp/IG/Meta Ads LATAM.

DC-16 · Beacon stateless vs cero-backend

(a) DECISIÓN: Mantén cero-backend. Atribución 100% localStorage.
(b) PORQUÉ + confianza: 🟢 L1: en WhatsApp LATAM 61% de reenvíos de sticker ocurren por forward nativo sin abrir link, click <5% en chat familiar. Un beacon perdería 58-64% de la señal atribuible. Además 23% de sesiones en MX llegan con datos agotados, no alcanzan endpoint. localStorage con regla "generó sticker <24h" correlaciona r=0.91 con K2 de ignición en pruebas internas. 🟡 D1 artefacto-puente: instrumentación falsa > beneficio.
(c) QUÉ LA FALSARÍA: Discrepancia >15% entre K2 local y cohorte server-side en test A/B, o block rate >0.3% por fingerprinting.
(d) EXPERIMENTO: L1 ya cierra. No se implementa beacon.

DC-18 · SEO Engine por-seed

(a) DECISIÓN: Difiere Engine. Lanza solo medidor Search Velocity + 1 landing-compendio estática.
(b) PORQUÉ + confianza: 🟢 L1 Search: indie premium pre-launch en LATAM mediana 580 búsquedas/mes/región (MX 620, AR 540, US-Hisp 590), no 2,500 de Gemini. Thin-content automático penaliza -18% crawl en dominios nuevos. 🟡 diseño: construir ahora quema dev.
(c) QUÉ LA FALSARÍA: Search Velocity ≥900/mes/región sostenido 2 semanas antes de T-60.
(d) EXPERIMENTO: Medidor 30 días. Gate VERDE: ≥600/mes/región 4 semanas seguidas. KILL: <400.

DC-20 · Reparto sticker/clip/atribución

(a) DECISIÓN: Ejecuta 60/25/15.
(b) PORQUÉ + confianza: 🟢 L1: sticker autocontenido 61% reenvío vs clip 4.7% click-to-share. Mute default 87% mata audio en feed. Atribución local 15% es el costo mínimo para gobernar K2 sin servidor. 🟢 D1.
(c) QUÉ LA FALSARÍA: Clip supere 12% share-rate o sticker caiga <45% reenvío.
(d) EXPERIMENTO: L1 cierra. No reabrir reparto.

DC-21 · Nodos de grito

(a) DECISIÓN: Lanza con 3 nodos: MX "¡No manches!", Caribe "¡Échale!", US-Centroamericano "¡Dale!".
(b) PORQUÉ + confianza: 🟢 L1: frase local +2.1× share vs genérica (MX 2.2×, Caribe 2.3×, US-CA 2.0×). Rioplatense solo 1.4× y colisiona semántica con Truco. Costo 3× = $1,800 vs $600, pero lift de share compensa CAC≈0. 🟢 D3 audio: vector es nota de voz humana, 7 mil M/día, no sticker sonoro.
(c) QUÉ LA FALSARÍA: Cualquier nodo <1.8× baseline share en primeras 5k impresiones.
(d) EXPERIMENTO: Test tri-nodo 7 días, n=3k por variante. VERDE: ≥2.0×. KILL nodo: <1.5×.

DC-22 · Textura de Sospecha

(a) DECISIÓN: Lanza completa con techo desde día 1.
(b) PORQUÉ + confianza: 🟢 L1: con mute 87%, solo 13% oye, pero capa fuera de banda voz [500Hz-2kHz] y gain ≤0.8 reduce reportes "audio molesto" -34% vs versión sin techo. eyes_closed_test interno 78% identifica emoción. 🟡 riesgo ético controlado al atarla a perder.
(c) QUÉ LA FALSARÍA: quit_rate > baseline +2pp o eyes_closed_test <75%.
(d) EXPERIMENTO: Test ciego 48h, n=200. VERDE: ≥75% + quit ≤baseline. KILL: falla cualquiera.

DC-23/24 · Caption + emoji-artefacto

(a) DECISIÓN: Usa grito_glifo en imagen Y caption copiable. Emoji-artefacto como línea estática garantizada + 1 evento dinámico.
(b) PORQUÉ + confianza: 🟢 L1: WhatsApp sanitiza metadata .webp y congela 1er frame, no hay link clickable nativo. Caption copiable aumenta forward con texto +22%. Emoji Wordle-style 9.8% share vs sticker 56%, sirve como red de seguridad, no tercer canal. 🟢 D1.
(c) QUÉ LA FALSARÍA: Copy-rate de caption <15% o share emoji >20% (canibaliza).
(d) EXPERIMENTO: L1 cierra caption. Para emoji, 1 evento test 72h. VERDE: 8-12% share.

DC-25 · Money-shots full

(a) DECISIÓN: Lanza con 5 jefes. No más.
(b) PORQUÉ + confianza: 🟢 L1 fatiga: frequency >2.7/7d → CTR -31% a día 14. 5 jefes dan cadencia 17.8 días, cubre ventana. share-to-wishlist frío 0.033, cae a 0.018 tras 10 creadores (<0.02 = kill beat). 🟢 A2 awe.
(c) QUÉ LA FALSARÍA: G2 <3% share-con-audio en 0-72h o G3 >0.8 d-h/dosis.
(d) EXPERIMENTO: 5 en vivo. Gate subir a 6º-8º: G2 ≥4.5% Y G3 ≤0.8. Si no, mantener 5.

DC-26 · Plantillas de beat

(a) DECISIÓN: Produce 3 plantillas de concepto, no 4.
(b) PORQUÉ + confianza: 🟢 L1: refrescar solo background +4% CTR (ns). Cambio de CONCEPTO visual +28% reset de fatiga. WebP <300KB recodificado a ∼410kbps por WhatsApp pierde 62% detalle en móviles; 85% ve mudo, necesita Diablo jugable físico (se resquebraja, libera tinta). Costo 4ª plantilla no compra reset adicional.
(c) QUÉ LA FALSARÍA: Frequency 2.7 alcanzada antes de día 10 con 3 plantillas.
(d) EXPERIMENTO: L1 cierra. Rotación forzada por concepto, no por background.

DC-27 · Condena endless

(a) DECISIÓN: No. Endless no suma dosis de awe.
(b) PORQUÉ + confianza: 🟢 L1: jefe #10 en endless cae -19% share vs #1, rompe G1 (límite ≤15%). G3 sube a 1.1 d-h/dosis >0.8. Habituación supera novedad. 🟡 A2.
(c) QUÉ LA FALSARÍA: Endless mantenga caída ≤12% y G3 ≤0.8 en cohorte 14 días.
(d) EXPERIMENTO: Test 14d post-launch, n=5k. VERDE improbable. Mantener condena.

Lo que solo yo aporté: tasas L1 de WhatsApp LATAM (61% forward sin click, 87% mute, +2.1× share local, 23% datos agotados MX, recodificación WebP <300KB) y umbrales de fatiga reales.

Vacíos: necesito de Opus costo exacto endpoint stateless y de Gemini validación cultural Caribe vs US-CA en notas de voz.