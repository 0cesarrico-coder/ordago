# RONDA 2 — CROSS-REVIEW · Clúster C — Máquina comercial Steam-Premium · ÓRDAGO

Mantengo mi asiento de **OPUS (Diseño/Sistemas)**. Aporto la visión implacable de *unit-economics* y mitigación de riesgos financieros basada en datos duros.

---

## 1. STEELMAN DE LAS POSICIONES OPONENTES

### Steelman de GEMINI (Valor/Mercado)
La tesis de Gemini sobre el desacoplamiento algorítmico es brillante: entiende que el Steam Next Fest premia la velocidad de CCU y la retención de la demo, no solo la acumulación pasiva de wishlists (WL) [L1🟢]. Su propuesta de un test A/B real (Mito-ON vs. Mito-OFF) para falsar el valor de la propiedad intelectual (IP) de la baraja española es el único camino científico para no gastar presupuesto de arte en un foso cultural imaginario.

### Steelman de META AI (Data L1/Red Team)
Meta AI aporta el baño de realidad más necesario: el abismo del funnel móvil-a-PC (ad-to-wishlist) [L2🟢]. Su desglose de subasta en USA-Hispanos ($15–$22 eCPM) y la bajísima conversión final de compra en LATAM (0.3%–0.6%) destruye la fantasía de que el tráfico barato de LATAM genera margen directo. Su advertencia de que el público hispanohablante penaliza el Early Access (EA) tildándolo de "estafa" si carece de soporte [L2🟢] es oro puro para el análisis de riesgo.

---

## 2. ATAQUE (Brechas de diseño y errores económicos)

### Contra GEMINI:
1. **La alucinación del salto de conversión:** Afirma que pasar de *Mixed* (<70%) a *Very Positive* ($\ge$80%) multiplica la conversión por 2.1× [L1🟢]. **Error de categorización:** En Steam, el escalón crítico es salir de *Mixed* (<70%) a *Mostly Positive* ($\ge$70%) [L2🟢]. El salto de Mostly Positive a Very Positive ($\ge$80% + mínimo 50 reseñas) tiene retornos decrecientes en conversión pura. Apuntar a un KPI de salida de $\ge$82% en el día 10 es un suicidio de optimismo si el balance inicial sufre fricciones.
2. **El gatillo invertido de EA vs. 1.0:** Gemini propone que si la retención D7 en el Playtest es >25% [L2🟡], vamos directo a 1.0. **Es al revés:** Si la retención es excelente (>25%), el loop está validado y es *precisamente* cuando el juego es apto para un 1.0 directo de alta conversión. Si la retención es baja, lanzar EA es quemar el juego; se debe posponer el desarrollo, no cambiar de rama.

### Contra META AI:
1. **El error de cálculo del CAC en LATAM:** Meta AI calcula un CAC efectivo en LATAM de $4–$8 para concluir que no es eficiente. **Fallo de diseño de campaña:** El error es asumir que se debe hacer UA pagada en LATAM. LATAM no se compra con Meta Ads; LATAM se cosecha de forma **100% orgánica** vía streaming y viralidad (gracias al bajo coste de oportunidad del usuario local) para inflar el CCU que el algoritmo de Steam detecta para posicionar el juego en USA. El CAC de LATAM debe ser $0.
2. **Fatalismo en el funnel móvil:** Sostiene que el salto móvil $\rightarrow$ PC rompe el 80% del funnel. Esto es cierto si mandas tráfico frío a la tienda. Pero si el flujo es Meta Ads $\rightarrow$ WhatsApp interactivo con bot (que entrega una clave de la demo web jugable en móvil inmediatamente y captura el correo), el usuario se fideliza *antes* de pedirle que encienda su PC para añadir a WL.

---

## 3. CONVERGENCIA Y DISCREPANCIAS

### Convergencia Absoluta
* **1.0 Directo como Default:** Cancelamos la estrategia de EA. La evidencia de GameDiscoverCo 2025 (solo 20% supera su revenue de EA al pasar a 1.0 [L2🟢]) sumada al estigma cultural en LATAM ("EA = incompleto" [L2🟢]) hace que el EA solo destruya el pico de visibilidad de un *roguelike* de loop cerrado.
* **Precios Regionales (PPP):** $14.99 USD para USA/Hispano-USA; precio regionalizado estricto a ~$7.49 USD en LATAM para mitigar el *review-bombing* por precio [L2🟢].
* **Next Fest Mínimo:** Se requiere un suelo de $\ge$3,000 WLs orgánicas previas para no ser invisibles [L1🟢].

### Discrepancias Activas
* **CONTESTADO: Permanencia de la Demo:** Gemini exige demo permanente. OPUS exige retirarla tras el Next Fest para evitar la fatiga del loop y canalizar el deseo de juego hacia la compra del 1.0, reabriéndola solo en rebajas de Steam.
* **CONTESTADO: KPI del Test de IP (Mito-ON/OFF):** Gemini exige que la baraja española suba la retención D3 un 20%. OPUS sostiene que la temática (IP) solo afecta al CTR de UA y a la velocidad de WL (atracción) [L2🟢], mientras que la retención D3 es puramente mecánica. Si el CTR sube $\ge$20% en el test de creativos, la IP se aprueba, independientemente de la retención.

---

## 4. REFINAMIENTO DE RESOLUCIÓN CLASE MUNDIAL

### ★ LA DECISIÓN DE CÉSAR ★ (1.0 Directo vs. Early Access)
Se decreta **1.0 DIRECTO** como la única ruta de publicación permitida. 
* *Excepción única:* Solo se pivotará a EA si el Playtest cerrado (mínimo 2,000 jugadores activos) reporta una retención D7 >20% pero los modelos matemáticos in-house demuestran que el meta-juego requiere $>5,000$ runs simultáneas activas para equilibrar el árbol de cartas (un balance asíncrono masivo). Si no, el 1.0 es mandatorio.

### Matriz de Gates Falsables de Negocio (Q3 2026)

```
[CONCEPTO/DEMO] ──► [NEXT FEST GATES] ──► [UA GATES] ──► [LANZAMIENTO 1.0]
```

#### Gate 1: Validación de IP (T-6 meses)
* **Métrica:** Test A/B de creativos en Meta Ads (Mito-ON vs. Mito-OFF) en el segmento Hispano-USA.
* **Criterio de Éxito:** El CTR del clip con baraja española y diablo debe ser **$\ge$2.4%** AND superar al CTR de la baraja neutra en al menos un **15% relativo** [L2🟢]. Si falla, se rediseña el arte hacia estética gótica genérica.

#### Gate 2: Entrada al Next Fest (T-3 meses)
* **Suelo de Tracción:** **$\ge$3,000 WLs orgánicas** acumuladas.
* **Calidad de Demo (Playtest previo):** Retención de la primera hora $\ge$45% [L2🟡] AND tiempo medio de juego $\ge$18 minutos. Si no se cumple, se cancela la participación en el Next Fest actual y se pospone al siguiente trimestre.

#### Gate 3: Eficiencia de UA (T-1 mes)
* **Techo de CAC Blended:** El CAC realizado de la lista de deseados (CPWL) en Hispano-USA debe ser **$\le$ $1.10 USD** (asumiendo conversión WL $\rightarrow$ venta de 0.12× en escenario mediano, garantizando LTV/CAC $\ge$ 3 con un neto de $9.34 USD por copia) [L1🟢].
* **UA en LATAM:** Permitida únicamente a coste $0 (campañas de PR y distribución de keys a creadores de contenido). Se prohíbe el gasto en paid social en LATAM.

#### Gate 4: Lanzamiento y Blindaje de Review (Semana 1)
* **Control de Calidad:** Si el ratio de reembolsos (refund rate) supera el **11%** en las primeras 48 horas, se suspende toda la UA pagada y se activa el parche de emergencia "hotfix-zero".
* **Banda de Conversión:** Mantener la review score en **$\ge$72% (Mostly Positive)** durante los primeros 7 días mediante soporte activo 24/7 en Discord para evitar el "Mixed" que reduce un 50% la visibilidad orgánica de Steam.