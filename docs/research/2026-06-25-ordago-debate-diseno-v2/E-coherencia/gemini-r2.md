# RONDA 2 — CROSS-REVIEW · Clúster E — Coherencia interna y carga cognitiva de las capas v1.2 · ÓRDAGO

Mantengo mi asiento: **Diseñador de Sistemas + sustracción/elegancia (A5, A1)**. Lidero PODA, JERARQUÍA Z y la economía cognitiva del espacio de decisión.

---

## 1. STEELMAN (Mis competidores tienen razón en...)

*   **A Meta AI (L1 Data Móvil) 🟢:** Su advertencia sobre el colapso de rendimiento en WebGL/DOM en gama media LATAM ($<100$ objetos activos, degradación crítica) es inapelable. Igualmente, su métrica de onboarding es un baño de realidad: exigir 7 reglas simultáneas antes de la primera victoria ahoga la retención D1. Su propuesta de un *time-to-first-meaningful-choice* $<90$ s es un estándar de retención móvil superior a mi estimación de 120s.
*   **A Gemini (Estratega de Valor/Narrativa) 🟢:** Su limitación táctica a un máximo de 3 siluetas activas con pistas simultáneas en el Codex es brillante; evita la parálisis de completitud sin alterar la cardinalidad $N=16$. Su idea de usar el "Hueco de Mañana" para ofrecer un rumor/pista narrativa en lugar de un mero aviso visual activa el sistema de búsqueda (SEEKING de Panksepp) de forma orgánica y offline.

---

## 2. ATAQUE (Errores, debilidades y fixes que empeoran el juego)

*   **Contra Meta AI (El peligro de podar el Core Loop):** Meta propone bajar a 4-5 reglas core eliminando los Pactos del tutorial para asegurar un D1 $>35\%$. **Grave error de diseño de sistemas.** Si quitas el trade-off "Pacto vs Fullería" del inicio, el juego es simplemente la *Escoba de 15* con skins. El jugador no entenderá por qué el juego es único.
    *   *Mi Fix por Sustracción Temporal:* No podes la regla; **serializa su introducción**. El primer win se divide en 3 manos (mangas) guiadas: Mano 1 introduce Sumar 15 y Mesa (Reglas 1-2); Mano 2 introduce Trampa y Fullería (Reglas 3-4); Mano 3 introduce Maña y Pacto (Reglas 5-7). El jugador gana en la mano 3. Aprendizaje progresivo, cero pérdida de identidad.
*   **Contra Meta AI (Sesiones híbrido-casuales vs Premium Flow):** Proponer "mangas guardables cada 6-8 minutos" para fragmentar la sesión rompe el estado de flujo cognitivo propio de los deckbuilders premium (*Inscryption*, *Balatro*).
    *   *Mi Fix:* La duración de la run se mantiene en [25, 35] min en p50, pero se implementa un **Auto-save de estado de mesa instantáneo al final de cada turno** (serialización JSON en local, costo de escritura $<50$ ms). El jugador puede cerrar la app en cualquier segundo y retomar exactamente en el mismo estado.
*   **Contra Gemini (Scope-creep de textos reactivos):** Proponer que el flavor text de victoria cambie dinámicamente según la Fullería exacta jugada contra un Diablo específico genera una matriz de 16 Diablos $\times$ 24 cartas = 384 strings únicos. Esto es sobrediseño narrativo de bajo impacto.
    *   *Mi Fix:* El flavor text reacciona únicamente al **arquetipo de victoria** (ej: Victoria Limpia con Maña vs Victoria Sucia con Sospecha), reduciendo la matriz a solo 2 variantes por Diablo (32 strings en total).

---

## 3. CONVERGENCIA (Lo acordado y cerrado)

*   **CONTESTADO: Cardinalidad del Codex.** Queda fijada en $N=16$ Diablos y $M=24$ Fullerías/Pactos como base premium invariable (Gemini 🟢).
*   **CONTESTADO: El "Hueco de Mañana".** Será un sistema pasivo (sin timers de energía), mostrando la silueta del siguiente Diablo + 1 rumor narrativo que actúe como incentivo táctico para la siguiente run (Gemini 🟢 / Meta AI 🟢).
*   **CONTESTADO: Rendimiento técnico visual.** Límite estricto de $\le 100$ componentes de renderizado activos en pantalla y un máximo de 3 elementos animados simultáneamente para garantizar $\ge 55$ fps en dispositivos móviles de gama media (Meta AI 🟢).
*   **CONTESTADO: Compartido social.** El sticker exportable prioriza la identidad ("Soy Escobero" + emblema estético del Diablo derrotado) por sobre estadísticas complejas de build, optimizando el CTR en pantallas pequeñas (Meta AI 🟢 / Gemini 🟢).

---

## 4. REFINAMIENTO DE LA RESOLUCIÓN CLASE MUNDIAL

### A. Jerarquía Z y Scheduler de Eventos (Poda Visual)
Para garantizar legibilidad daltónica en pantallas de $100\times100$ px (gama baja) y un rendimiento de 60fps en WebGL:
*   **Regla dura del Scheduler:** Los eventos visuales de estado (Z3) y feedback (Z4) se encolan en una corrutina fifo. Queda prohibido el solapamiento temporal de animaciones de *Trampa Activa* y *Barra de Sospecha*.
    $$\Delta t(\text{Animación}_a, \text{Animación}_b) \ge 300\text{ ms}$$

### B. Métrica de Complejidad Cognitiva de Onboarding
El tester debe ser capaz de verbalizar el loop sin soporte externo tras la primera victoria (Mano 3).
*   **Fórmula de Carga Percibida ($C$):**
    $$C = \text{Reglas Activas} \times \text{Canales de Feedback Activos} \le 12$$
    *(Si hay 4 reglas activas en la Mano 1, solo se permiten 3 canales visuales de feedback simultáneos).*

### C. Invariantes del Loop de Pacing
*   **T1 (First Meaningful Choice):** El primer trade-off real de Maña ocurre antes de los **90 segundos** de juego (p50).
*   **T2 (Duración de Run):** $\Sigma(\text{Dientes}) \in [25, 35]$ minutos en p50. P90 $\le 40$ minutos.
*   **T3 (Frecuencia de Contrapeso):** En un modelo de simulación de 1000 seeds (vía solver §14), la viabilidad de la estrategia de "Pacto" (EV superior a "Fullería") debe ser $\ge 20\%$ y $\le 50\%$, asegurando que la Fullería no domine de forma absoluta (no es un "impuesto", es una decisión).

---

## 5. DECISIÓN DE CÉSAR

1.  **¿La recompensa del 100% del Codex es estrictamente estética** (Cantar de ciego ilustrado/Skins) para proteger el valor anti-FOMO premium, **o desbloquea el "Diablo Fantasma" como boss mecánico final?** (Opus y Gemini votamos estético para evitar *fatiga de grind*; César decide si prefiere el impacto de un secret boss).
2.  **¿Onboarding estricto de 4 reglas (Meta AI) o Tutorial Serializado de 7 reglas (Opus)?** (Meta sacrifica el flavor inicial del trade-off por retención pura; Opus asegura la identidad mecánica del juego desde el minuto 3 en 3 micro-mangas).

*Confianza en la arquitectura de sistemas: 🟢 Alta. Confianza en el comportamiento del solver §14 en p50: 🟡 Media.*