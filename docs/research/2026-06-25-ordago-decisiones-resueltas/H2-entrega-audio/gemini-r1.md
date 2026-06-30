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