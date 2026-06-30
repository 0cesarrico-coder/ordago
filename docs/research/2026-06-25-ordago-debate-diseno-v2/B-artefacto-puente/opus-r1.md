# Clúster B · Ronda 1 — ASIENTO OPUS (Diseñador de Sistemas de Crecimiento)

> Lente: K compone solo si el nodo NUEVO genera su propio output reinvertible (C2). Mi trabajo: que el grafo sea **crecimiento compuesto** y no fuego de paja, y blindar cada promesa con un **gate falsable barato** que la mate antes de un píxel. Evidencia etiquetada L1–L4 / 🟢🟡⚪.

---

## (a) STEELMAN — por qué la composición de K + gates falsables son el delta correcto

La v1.2 hizo lo difícil bien: definió un **artefacto-puente atómico** (A=PNG <80KB, B=clip 6-8s) y entendió que con B2P sin MTX **LTV≈1 venta**, así que el grafo no es marketing — es el **único** camino a LTV/CAC≥3. Eso es razonamiento de clase mundial: ata la supervivencia financiera a un invariante de producto, no a un presupuesto de UA. **L4 🟢** (la aritmética B2P es deductiva).

El delta que falta es **la diferencia entre K lineal y K compuesto**. Un loop donde solo los dueños de Steam generan artefactos tiene K efectivo acotado por la base pagada: cada invitado es una hoja muerta. La corrección #27 (la **demo web genera SU sticker desde la 1ª mano, cliente, 0 servidor**) es exactamente el invariante de C2: el nodo nuevo —que ni pagó— produce output reinvertible. Eso convierte un árbol de profundidad 1 en uno de profundidad N. **Es el fix más importante del clúster y todo lo demás es residual frente a él.** **L2 🟢** (Chen: viral SIN nodo-que-reinvierte = lineal).

Y los gates falsables son correctos porque **un gate que se corre en 100×100px gris cuesta centavos y mata una promesa que costaría semanas de arte**. El glance-gate (#40), el motion-gate (#62), el reaction-gate (#65) y el first-frame-gate del DUELO (#60) son todos la misma familia: *"si el artefacto no comunica el MOAT a un downscale mudo, no se exporta"*. Eso es el principio C1 ("el frame nunca debe mentir") promovido de checklist de arte a **gate de build**. **L2 🟢**.

---

## (b) ATAQUE / MEJORA — dónde mis propios fixes se auto-engañan

1. **"K de 2ª generación" es un vanity metric esperando nacer.** Si lo defino como "shares originados en nodos no-Steam", lo inflo trivialmente: un usuario demo que comparte 5 veces a chats muertos marca K2 alto con cero invitados nuevos jugando. **El modo de fallo es medir SHARES en vez de ACTIVACIONES.** K2 honesto = *invitado-de-demo que a su vez genera una 1ª-mano nueva atribuible*. Sin esa atribución encadenada, K2 miente. **L4 🟡**.

2. **El "naipe del Romancero" (#25) añade scope con retorno diferido y no falsable a tiempo.** Su KPI (lore_share D30–D60) llega *después* del launch — no protege la decisión de construirlo ahora. Riesgo real: gastar arte/sistema en un 2º artefacto mientras el sticker competitivo (el que SÍ mueve CAC en semana 1) está sin pulir. **Es residual, no de ignición.**

3. **El motion-gate (#62) puede rechazar clips que SÍ convierten.** Un juez que exige "nombrar qué pasó en 3s a 360p mudo" sesga hacia clips *legibles* y mata clips *emocionalmente virales pero caóticos* (el caos a veces ES el hook). Modo de fallo: optimizo claridad y pierdo sorpresa. El gate debe ser **piso de legibilidad del MOAT, no techo de complejidad**.

4. **El og:image estático (#19) pierde el chisme dinámico.** Estático <100ms cachea por seedhash — pero el gancho relacional ("María te ganó por 2") es *por-partida*, no por-seed. Si lo congelo por seed pierdo el "por 2". Modo de fallo: velocidad a costa del gancho que convierte.

---

## (c) RESOLUCIÓN DE CLASE MUNDIAL — objeto, métrica, verde, KILL

**Set mínimo de gates que un build NO pasa sin cumplir (los 4 de ignición):**

| # | Objeto/Gate | Métrica | VERDE | KILL |
|---|---|---|---|---|
| **G1 (#27)** composición | demo web genera sticker+emoji 1ª mano, cliente | **K2-activación** = invitados-de-demo que generan 1ª-mano nueva / nodos-demo | ≥0.35 | <0.15 → loop lineal, rehacer ignición |
| **G2 (#19)** OG | og:image+title estático por seedhash, CDN | latencia entrega scraper | <100ms p95 entrega; <300ms p95 generación post-mano | scraper no recibe <100ms → preview muerto |
| **G3 (#40)** glance relacional | RunDigest→sticker a 100×100px gris | % lee el chisme relacional ("por mucho/poco") | ≥90% (n≥20) | <90% → rehacer silueta |
| **G4 (#60)** first-frame DUELO | clip canónico = arco del pillado | % lee "le hace trampa al Diablo" sin audio, 1er frame | ≥80% | <80% → re-encuadrar clip |

**Resolver "medir K2 sin instrumentación que mienta" (el problema duro):**
La trampa es servidor. La solución es **atribución por deep-link encadenado, 0 backend de identidad**: cada sticker/clip lleva el `seedhash` + un **token de generación local** (nonce en el PNG/URL). Cuando un invitado abre `ordago.gg/d/<seed>?ref=<nonce>` y **completa su 1ª mano**, su cliente emite SU nonce hijo y un único beacon `{ref_padre, nonce_hijo, completó_mano:true}`. **K2 solo cuenta aristas con `completó_mano=true`** — no shares, no aperturas. Esto es 1 endpoint de telemetría stateless (no identidad, no cuentas), barato, y **no puede inflarse compartiendo a chats muertos** porque exige una mano jugada río abajo. **L4 🟡** (diseño; falta validar tasa de beacon-loss en WhatsApp LATAM — pedir L1 a Meta AI).

**Arreglo del og dinámico (G2):** dos capas. Capa-seed estática (instantánea, cacheada) como *fallback* + capa-partida que se hornea **al terminar la mano** (<300ms, cliente sube PNG a CDN keyed por nonce). El scraper que llega tarde recibe el genérico-de-seed (vivo); el que llega a tiempo recibe el chisme "por 2". **Nunca bloquea el preview por esperar el dato dinámico.**

**Arreglo del motion-gate (G3'→residual, NO de ignición):** el gate es **piso**: juez solo debe nombrar *"¿hubo trampa? ¿quién gana?"* (el MOAT), **no** "describe todo". Clips caóticos pasan si el MOAT es legible. Umbral: ≥70% nombra trampa+ganador a 360p mudo 3s. Esto evita rechazar virales caóticos.

**Prioridad de construcción:**
1. **PRIMERO G1** (composición cliente-side) — sin esto el grafo no compone y nada más importa.
2. **G2 + G3 + G4** (primer contacto + legibilidad del MOAT) — son el "el artefacto vende el DUELO, no un barrido genérico".
3. **Residual** (post-ignición verde): #56 momento-clip-como-invariante-de-run, #57 SEO/Search Velocity, #65 reaction-gate, #25 Romancero. Todos valiosos para *perdurabilidad*, ninguno bloquea el launch.

**Invariante de run (#56), barato:** "una run no termina sin ≥1 momento transmisible (telemetría detecta pico tensión-resuelta)". KPI clips/hora-stream ≥1 en 30min. KILL: 30min sin pico → el loop no produce watchability, revisar densidad de Trampas/Fullerías. Esto **sí** lo construiría temprano si el costo es solo telemetría (reusa el detector de pico del exportador).

---

## (d) DECISIÓN DE CÉSAR

**Decisión 1 — ¿Cuánto backend para K2 en demo web?**
Recomiendo: **1 endpoint stateless de beacon (sin cuentas, sin identidad)**, no más. Construir G1 client-side + atribución por nonce encadenado con `completó_mano=true`. **Costo de equivocarse alto en ambos lados:** sin atribución → no sabes si el grafo compone y vuelas a ciegas el único KPI que decide LTV/CAC; con backend de identidad completo → scope creep que retrasa launch y traiciona el espíritu "0 servidor". El nonce-beacon es el mínimo que no miente. **Recomendación firme.**

**Decisión 2 — ¿Romancero (lore) ahora o después?**
Recomiendo: **después.** Es residual; su KPI no es falsable pre-launch y compite por arte con el sticker competitivo que mueve CAC en semana 1. Costo de equivocarse si lo cortas: pierdes algo de UGC-de-teoría D30–D60 (perdurabilidad), recuperable en parche. Costo si lo metes ahora: retrasas la ignición, que es existencial. **Asimetría clara → diferir.**

**Decisión 3 — ¿Qué pasa si G1 sale <0.15 (KILL)?**
César debe pre-comprometerse a una respuesta: **si la demo no genera composición, el problema no es el artefacto sino que la 1ª-mano-web no es lo bastante satisfactoria para querer compartir.** El fix entonces es *producto* (la demo), no *crecimiento*. Definir esto antes evita racionalizar un KILL como "mala instrumentación".
