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
