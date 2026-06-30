# ÓRDAGO · Clúster C · RONDA 1 · OPUS — Modelador de unit-economics + riesgo

## Tesis central
El gate "LTV/CAC≥3 por columna" no falla por ser exigente, sino por estar **anclado a un estimador (WL→venta) cuya varianza cruzada es de 10-20× (VECES, no %)** — es precisión alucinada. Y para un B2P-sin-MTX, **LTV ≈ neto de una transacción ≈ una constante**; la única variable viva del ratio es el CAC. Por tanto el gate honesto NO es "predecir el LTV" sino **"acotar el CAC bajo tres escenarios de demanda y matar el proyecto si el escenario MEDIANO no cierra ≥3"**. Y EA, para un roguelike loop-puro, es una **decisión de capital negativa por defecto** (el 1.0 mediano 2025 rinde ~40% del EA; solo ~20% supera su EA). Recomiendo **1.0 directo** salvo una sola condición falsable.

---

## #47 (LIDERAZGO) — Gate LTV/CAC≥3 sobre un WL→venta no-forecasteable

**(a) STEELMAN del fix.** Convertir el gate de punto a banda es correcto. La aritmética del LTV es robusta porque es casi determinista:

| | USA general | Hispanos-USA | LATAM |
|---|---|---|---|
| Precio | $14.99 | $14.99 | ~$7.49 |
| Neto −30% Steam | $10.49 | $10.49 | ~$5.24 |
| − Refund 8-14% (uso 11%) | ~$9.34 | ~$9.34 | ~$4.66 |
| **LTV honesto (≈1 tx)** | **~$9.3** 🟡 | **~$9.3** 🟡 | **~$4.7** 🟡 |

El gate ≥3 ⇒ **CAC techo = LTV/3**: **USA ≤$3.1 · Hispanos-USA ≤$3.1 · LATAM ≤$1.55**. Esto es falsable: o el CAC blended cabe bajo el techo, o no.

**(b) ATAQUE/MODO DE FALLO.** El fix mueve la incertidumbre del LTV (estable) al **volumen** vía WL→venta, que es justo el predictor roto. El error es usar la dispersión WL→venta para estimar *unidades*, cuando para el GATE solo importa el **CAC realizado**, que es **medible ex-post y casi independiente del volumen orgánico**. Segundo fallo: el gate "por columna" puede pasar en USA y fallar en LATAM y aun así el proyecto ser viable (LATAM es motor de volumen/viralidad, no de margen) → un gate AND por columna **mata proyectos sanos**.

**(c) RESOLUCIÓN — stress-test de 3 escenarios.** Reanclar el gate a lo falsable. Dato fresco **[L2🟢 GameDiscoverCo 2024-25]:** WL→venta Sem-1 mediana ≈ **0.15-0.17×** para >10k WL (más alta que el 0.10× del GDD), pero **varianza 10-20×**; outliers reales Peak 266×, InZOI 3.2×. Uso bandas conservadoras sobre WL:

- **Cola baja 0.05× · Mediana 0.12× · Cola alta 0.17×** (multiplicador sobre WL Sem-1).
- Con **WL de entrada = 7,000** (mínimo del propio GDD): ventas Sem-1 = **350 / 840 / 1,190**.
- Revenue Sem-1 a blend ~$8/u (mezcla USA+hispanos+LATAM): **~$2.8k / ~$6.7k / ~$9.5k**.

**Gate reformulado (falsable):** el proyecto pasa a vertical slice solo si **CAC_blended_realizado ≤ LTV/3 en el escenario MEDIANO** Y el **payback de la inversión de UA se recupera con ventas ≤ escenario cola-baja** (margen de seguridad). El gate ya **no es por columna AND**; es **blended ponderado por mezcla**, con LATAM como dilución de margen aceptada. El CAC entra como **dato medido en la demo/Next Fest**, no como forecast.

**Leading-indicators que sustituyen al lagging (WL→venta):**
1. **% que cruza la 2ª hora de la demo** (retención del loop; falsable D0). Gate 🟡 ≥35-40%.
2. **Horas-hasta-primera-review** post-demo (proxy de boca-a-boca).
3. **WL/día y su aceleración** durante Next Fest (Gemini lidera el umbral Popular Upcoming).
4. **CAC del clip-puente** (render-worker) vs WL incrementales que genera → ROAS del artefacto.

---

## #46/#59 (LIDERAZGO) — ÁRBOL DE DECISIÓN EA vs 1.0 · ★ DECISIÓN DE CÉSAR ★

**Datos [L2🟢 GameDiscoverCo 2025, verificado hoy]:** de **225 graduados EA 2025, solo ~20% (45) superó su EA**; **revenue 1.0 mediano ≈ 40% del EA** (cayó de ~70% en 2023); EA mediano **437 días** (media 643); EA >12m sin updates → interés −80%.

**Árbol (nodos → KPI-gatillo):**

```
RAÍZ: ¿el set de cartas necesita balance comunitario que NO se puede simular in-house?
├─ NO  ──────────────────────────────► 1.0 DIRECTO  ◄═══ DEFAULT (recomendado)
│        (roguelike loop-puro, set acotado, balanceable por playtest cerrado)
└─ SÍ (condición ÚNICA válida)
     ├─ ¿WL ≥ 7,000 al abrir EA?            NO → posponer, seguir acumulando WL
     │   SÍ ↓
     ├─ ¿precio EA = precio final $14.99?   NO → corregir (prohibido "truco de subida")
     │   SÍ ↓
     ├─ ¿cadencia de updates ≤ 1 mes garantizada por roadmap?  NO → 1.0 directo
     │   SÍ ↓
     └─ EA = EL LANZAMIENTO (no "dos picos"). Ventana EA ≤ 6-9 meses, no 437 días.
```

**Razón inválida explícita:** "dos picos de revenue" — los datos 2025 dicen que el segundo pico es **40% del primero**, no un segundo lanzamiento. EA fragmenta el único momento de máxima visibilidad de un B2P.

**(d) DECISIÓN DE CÉSAR — recomendación.** **1.0 DIRECTO.** 🟢 alta confianza.
- **Trade-off de capital:** EA adelanta caja (~bueno para runway) pero **destruye expectativa de revenue total** (40% mediano en el 2º acto) y **quema la ventana de descubrimiento** (saturación Balatro-likes, L6) en un producto incompleto. Para loop-puro sin contenido episódico, el riesgo de reseñas "es bueno pero le falta" en Mixed (que halvea conversión, ver #45) es alto.
- **Qué evidencia lo cambiaría:** si el playtest cerrado revela que **el balance del set requiere N>~5k jugadores reales** para converger (imposible in-house) → EA por la rama válida, con los 3 gates. O si el runway exige caja antes del 1.0 y no hay alternativa de financiación → EA táctico, asumiendo el haircut del 40%.
- **Orden de falsación:** (1) ¿balance necesita masa? → (2) ¿WL≥7k? → (3) ¿runway aguanta a 1.0? Solo si (1)=SÍ y (3) aprieta, EA.

---

## Pase de riesgo a los demás huecos
- **#36 Demo/Next Fest:** gate ≥2,000 WL es el **piso de munición** del escenario cola-baja; sin él, 0.05×·2k = 100 ventas Sem-1 = inviable. El CAC del render-worker debe entrar en el payback.
- **#45 Banda de review:** salir de Mixed→Mostly Positive **~2× la conversión del MISMO tráfico** [L3🟡] → es el **activo financiero #1 de cola larga**; vale más que +1k WL.
- **#58 WL/día sin velocidad:** WL frío (bundles, regalos, tráfico no-orgánico) infla el numerador del gate sin convertir → reportar **WL/día con fuente y cohorte**, no acumulado.
- **#66 KPIs 1ª hora:** son los leading-indicators del §c; deben estar instrumentados en la demo o el gate vuelve a ser fe.
- **#30/#44/#43 Anti-decaimiento cultural:** la señal (neutros −85% búsquedas 18m, mito ~70% 36m) es **[L1] DÉBIL** ⚪ y sostiene TODO el LTV de cola larga → debe volverse **KPI medido (búsquedas de marca/mes, retención de wishlist a 6m)** o el LTV largo es fe. Kill cultural **por nodo del sweet spot** (hispanos-USA ≠ USA general ≠ LATAM), no mono-métrica.

---

## Lo que sé y las otras IAs probablemente no
- La **dispersión WL→venta es inutilizable para forecast pero el CAC es medible ex-post** → el gate debe pivotar de "predecir unidades" a "acotar CAC bajo el techo LTV/3". Esto disuelve el problema de Carless sin pelearlo.
- **Cuantificación dura del haircut EA:** revenue 1.0 mediano = **40% del EA en 2025** (era 70% en 2023) → la economía de "dos picos" está muerta a nivel de mediana. [L2🟢, verificado 2026-06-25]
- LTV de B2P-sin-MTX es **una constante (~$9.3 USA / ~$4.7 LATAM neto-refund)**, no una distribución → el modelo entero se reduce a CAC.

## Vacíos — qué necesito
- **De Gemini:** umbral de **WL/día y de WL-total** para entrar a *Popular Upcoming* y el peso del algoritmo de Steam en WL orgánico (numerador del gate); cómo el timing de Next Fest mueve la cola alta.
- **De Meta AI:** **CAC/CPI/eCPM reales por segmento** (USA general, hispanos-USA, LATAM) y **CTR del clip-puente** por formato/UGC → son los únicos inputs vivos del gate. Sin ellos, los techos CAC ($3.1 / $3.1 / $1.55) son razonamiento ⚪, no dato.

**Sources:** [GameDiscoverCo — wishlist conversions 2024-25](https://newsletter.gamediscover.co/p/the-state-of-steam-wishlist-conversions) · [GameDiscoverCo — EA graduates 2025](https://newsletter.gamediscover.co/p/the-state-of-steam-early-access-graduates) · [GameDiscoverCo — new WL→first-week expectations](https://newsletter.gamediscover.co/p/steam-the-new-wishlists-to-first)
