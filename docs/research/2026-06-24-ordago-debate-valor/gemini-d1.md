=== PORTAL DE OPINIÓN DEL PANEL · RONDA 1 ===

**DE: ESTRATEGA DE PROPUESTA DE VALOR + VOZ DEL JUGADOR**  
**PARA: César (Lead Designer)**

*Análisis cruzado desde la frialdad del JTBD (Estratega) y el calor de la primera sesión en una cantina de Durango o un piso de Vallecas (Voz del Jugador).*

---

### DECISIÓN 3 — Costo de los Pactos Oscuros (§7.6)

*   **Tu recomendación:** **OPCIÓN C: "El Trato de Alquiler de Ranura" (Slot-Sharing Trade-off) + "La Carta Empeñada" (Collateral Card).**
*   **Por qué es la de clase mundial:** 
    La Opción A (quemar permanentemente una Fullería) es un costo prohibitivo que induce a la aversión a la pérdida; el jugador hispano prefiere no jugar a sentir que le "robaron" su juguete táctico (*Voz del Jugador*). La Opción B es genérica y aditiva (clásico mazo inflado). 
    La **Opción C** unifica los dos sistemas bajo la regla de **Elegancia (A1 🟢)**: el jugador tiene un número estricto de ranuras (p. ej., 3 ranuras de "Maña"). En ellas puede equipar una *Fullería* (acción táctica activa: robar de la mesa, forzar un 15 falso) o un *Pacto Oscuro* (modificador pasivo brutal, pero que introduce una "Carta de Condena" en el mazo). El trade-off es inmediato y dinámico: *¿Prefiero el seguro de vida de una trampa activa o el multiplicador codicioso del pacto pasivo?* Esto evita el power-creep, respeta la **Saciedad Alcanzable (LD7 🟢)** al no crear espirales de muerte de las que no se puede salir, y eleva la toma de decisiones estratégicas.
*   **Riesgo principal + su mitigación:** 
    *Riesgo:* Que el jugador ignore los Pactos Oscuros si percibe que las Fullerías activas son indispensables para sobrevivir a las Trampas del Diablo.  
    *Mitigación:* "La Carta Empeñada": Permitir que un Pacto Oscuro se equipe *gratis* en una ranura bloqueada temporalmente, pero si el jugador no supera la siguiente Manga, esa carta empeñada (una Mata o una Fullería clave) se pierde para siempre de la run.
*   **Test/criterio de kill más barato para validarla:** 
    En el prototipo de papel (§14), ofrece a 10 jugadores 3 ranuras libres. Dales Trampas duras. Si >80% de los testers prefiere mantener siempre 3 Fullerías y 0 Pactos, el acople es asimétrico; si la distribución de ranuras se mantiene cerca del 50/50 (Fullerías/Pactos) en runs ganadoras, el sistema es elegante y sobrevive.

---

### DECISIÓN 4 — Bucketing del Diablo Fantasma (§8)

*   **Tu recomendación:** **OPCIÓN C: "La Escalera de Almas" (Dynamic Ghost Ladder with Real Identity).**
*   **Por qué es la de clase mundial:** 
    La Opción A (percentil puro) es fría y desalienta al jugador medio que se ve en el 45% global (*Voz del Jugador*). La Opción B (delta puramente matemático del 5%) se siente artificial, como una IA de autito que frena para esperarte; mata el alma del motor **Action-Social 41% de LATAM/MX (LD4 🟡)**. 
    La **Opción C** hace honor al **Mito Comprimido (A3 🟡)**: el juego te empareja con el fantasma de un **jugador real e identificado por su nombre** cuyo score en la semilla diaria esté exactamente entre un **5% y un 15% por encima de tu mejor puntuación actual**. Al ganarle, la UI muestra un estallido de fuego fatuo: *"Has liberado el alma de [Nombre_Del_Jugador]"* (Serious Fun, **LD2 🟡**), te quedas con sus Reales sobrantes para la siguiente manga, y su fantasma es reemplazado por el del siguiente rival en la escalera. El gap es siempre cerrable (**Festinger/LD6 🟢**), pero el pique es 100% humano y diegético.
*   **Riesgo principal + su mitigación:** 
    *Riesgo:* En los primeros días del juego o en semillas poco jugadas, la falta de "fantasmas reales" en el bucket exacto del jugador.  
    *Mitigación:* "Los Diablos del Romancero": bots pre-diseñados temáticamente con nombres de leyendas folk (p. ej., "El Charro Negro", "El Chacho de Cantina") que actúan como placeholders con builds pre-calculadas hasta que la base de datos se pueble.
*   **Test/criterio de kill más barato para validarla:** 
    Corre un test cerrado de 3 días con un canal de Discord de 30 personas con una leaderboard estática de Google Sheets vs. un bot de Discord que les manda un mensaje: *"Tu Diablo hoy es [Compañero], su score es +8% que el tuyo"*. Mide el volumen de insultos lúdicos y capturas de pantalla compartidas. Si el engagement de chat sube un **50%** con el emparejamiento directo vs. la leaderboard fría, "La Escalera" es verde para producción.

---

### DECISIÓN 5 — Asistencia de UI al verbo "sumar 15" (§7.2/§6.1)

*   **Tu recomendación:** **OPCIÓN D: "La Mano Limpia" (Gamified UI Assistance with Score Multiplier).**
*   **Por qué es la de clase mundial:** 
    La fatiga mental de calcular constantemente sumas de 15 con el desfase de que la Sota es 10 visualmente pero vale 8 es un **bounce-moment masivo en los primeros 5 minutos** para el jugador global y el hispano cansado tras el trabajo (*Voz del Jugador*, Serious Fun **LD2 🟡**). Sin embargo, darle la solución masticada (Opción A) destruye el "Fiero" del avistamiento cognitivo (Hard Fun **LD2 🟢**) y convierte el juego en un clicker aburrido en la run 10.
    La **Opción D** resuelve esto gamificando la UI mediante la **Elegancia de Trade-off (A1 🟢)**: la asistencia pasiva de Gemini (resaltar acumulado y cartas viables en mesa al seleccionar) está activada por defecto. Sin embargo, existe un modificador global de run llamado **"Mano Limpia" (Clean Hand)**. Si el jugador lo activa (lo que desactiva por completo la asistencia visual y le obliga a calcular de memoria), recibe un **multiplicador pasivo permanente de x1.20 Suerte (Mult)** en todas sus Escobas. Esto convierte la comodidad de la UI en una decisión de diseño de alto nivel: los novatos aprenden sin dolor (**Estética-Sistema, A5 🟡**), y los veteranos "juegan a lo tahúr real", asumiendo la carga cognitiva a cambio de romper el juego con números gigantes.
*   **Riesgo principal + su mitigación:** 
    *Riesgo:* Que la diferencia entre jugar con y sin asistencia rompa el balance de las tablas de clasificación del Diablo Fantasma.  
    *Mitigación:* Marcar las puntuaciones en el leaderboard con un icono de "Ojo de Pícaro" (asistido) o "Mano Limpia" (sin asistencia). Los jugadores de "Mano Limpia" tienen su propia categoría de orgullo social (**Action-Social/Mastery, LD3 🟢**).
*   **Test/criterio de kill más barato para validarla:** 
    En el prototipo digital rápido (Godot/Love2D, §15): pon a 10 personas a jugar 3 runs con asistencia visual y luego desactívala sin recompensa. Mide el tiempo de abandono. Si el abandono sube >40%, la asistencia es vital. Luego, introduce el multiplicador de "Mano Limpia" y mide cuántos testers hardcore *eligen voluntariamente* desactivar la ayuda para buscar el high-score. Si ≥40% de los jugadores experimentados toma el riesgo, la Opción D es clase mundial.

---

### CONCLUSIÓN DEL PANEL

> **"La decisión que más mueve la aguja hacia clase mundial de las tres es la DECISIÓN 5 (Asistencia de UI "Mano Limpia") porque soluciona simultáneamente el mayor cuello de botella de retención de la primera sesión (la fatiga aritmética del onboarding, A5🟡) y lo convierte en un sistema profundo de riesgo-recompensa y orgullo social para el endgame (A1🟢 / LD3🟢), sin gastar un solo centavo en arte ni comprometer la pureza mecánica del juego."**