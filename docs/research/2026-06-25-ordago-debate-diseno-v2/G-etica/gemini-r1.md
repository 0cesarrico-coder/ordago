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