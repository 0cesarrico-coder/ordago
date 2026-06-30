# Meta AI — Ronda 1 · CLÚSTER E "Coherencia interna y carga cognitiva de las capas v1.2"

## Tu asiento
Eres **Data L1 (plataforma) + Red Team** del debate. Aportas lo que SOLO TÚ tienes: comportamiento real de usuarios móviles LATAM/hispanos (Instagram/WhatsApp/Reels/Facebook), tolerancia a carga cognitiva, abandono, y patrones de retención. Tu trabajo: **atacar el over-engineering**. Tres preguntas-red-team guían todo: **(1) ¿la carga cognitiva de ≥6-7 capas mata la retención en móvil?** **(2) ¿qué SIMPLIFICAN los juegos que escalan (no los que mueren)?** **(3) ¿dónde la v1.2 está añadiendo sistema donde un juego real PODARÍA?** Eres 1 de 3 IAs sobre la MISMA pregunta; Opus lleva sustracción/jerarquía, Gemini lleva curiosidad/coherencia narrativa.

## El juego (autocontenido)
ÓRDAGO: roguelike deckbuilder con **baraja española**. Verbo: Escobas (sumar 15) sobre una **Mesa viva** que el Diablo siembra; **Trampas** alteran la regla, **Fullerías** las rompen (suben una barra de **Sospecha**); **Pactos** encadenan cascadas. Sistema dual + **economía de Maña** (~3 ranuras: Fullería *o* Pacto). 4 Mangas × 3 apuestas; run ~25-35 min. Capas v1.2 apiladas sobre la MISMA pantalla: Mesa viva sembrada, Trampa manifiesta, barra de Sospecha, ranuras de Maña, cascadas de Pactos, modo aprendiz, glance gate, 4 canales redundantes de color, Codex/Romancero (~12-20 Diablos), Diablo Fantasma, artefacto-puente. Mercado: **LATAM + USA general + hispanos-USA** (sweet spot); 87% de gamers LATAM en smartphone gama media/baja; B2P Steam premium con **demo web jugable móvil** (touchpoint de adquisición). SIN MTX ni live-ops.

## La pregunta central del Clúster E
La v1.2 apiló ≥6-7 capas sobre la MISMA pantalla/sesión sin reconciliar jerarquía, presupuesto temporal, ni cardinalidad. **¿Qué se CONSOLIDA/PODA para que la suma de buenos sistemas NO sea papilla?** Tú eres la voz que duda de TODO sistema que no se gane su renta en retención real.

## Los huecos a atacar (con § · porqué · fix propuesto — cuestiónalos)
- **#5 Jerarquía de saliencia Z (§10/§11, COMPL).** *Fix:* §10.2 presupuesto de saliencia + serializar pillado-Sospecha vs cascada-T3. **Red team:** ¿una Mesa densa + cascadas + Sospecha + Trampa en un teléfono a 360p ya es papilla HOY? ¿Cuántos elementos animados simultáneos toleran tus usuarios antes de bounce? ¿La demo web móvil se ve como "muy ocupada"?
- **#6/#3 Presupuesto cognitivo ≤7±2 reglas-core (§7.6/§4.1, COMPL).** *Fix:* gate que cuente reglas verbalizadas (≤5 para el dual; ≤7±2 para la 1ª victoria). **Red team:** ¿7 reglas antes de la 1ª victoria es DEMASIADO para retención D1 en hybrid-casual LATAM? ¿Cuál es el techo real de reglas que un juego que ESCALA pide antes del primer "win"? ¿Qué pasa con la tasa de abandono en el tutorial cuando hay 6-7 sistemas?
- **#48/#49 Presupuesto temporal de run (§9, CONTRA/REGR).** *Fix:* Σ(dientes)∈[25,35] p50, p90≤40; KPI `time_to_first_fullería_jugada` ~120s. **Red team:** ¿una run de 25-35 min es viable en MÓVIL (sesiones reales de WhatsApp-gaming son cortas)? ¿La demo web pierde gente antes del min 5? ¿El "first trap-break en 120s" llega tarde para enganchar?
- **#24 Codex sin estado terminal / anti-FOMO (§8/§6.4, PROM).** *Fix:* "X/N huecos" + beat 100% + extender anti-FOMO. **Red team:** ¿el grid de ~12-20 huecos sin timer RETIENE sin FOMO, o necesita el gancho de urgencia que tú ves convertir? ¿Qué hace que una colección móvil retenga D30 sin live-ops?
- **#26 Biblia de mundo / ambigüedad (§12, RESID).** *Fix:* biblia de 1 pág + linkeo Diablo→hecho/ambigüedad. **Red team:** ¿el lore/ambigüedad mueve ALGÚN número en hybrid-casual, o es esfuerzo que no convierte? ¿El UGC de lore existe en tu data para este género, o solo el brag competitivo?
- **#39 Expression visible en el sticker (§4/§8.3, CONTRA).** *Fix:* sticker exhibe siluetas de build SIN solución. **Red team:** ¿qué hace que un sticker se reenvíe REALMENTE en WhatsApp/Reels? ¿La "firma-de-build visible" añade share-rate o es ruido que ensucia la silueta? (Recuerda: stickers personalizados ~56% vs predeterminados ~12%; se queman en 2-3 sem.)
- **#12 Tease del hueco de mañana (§8.4, RESID).** *Fix:* silueta cerrable-pero-bloqueada SIN timer. **Red team:** ¿el tease-sin-timer mueve retorno D7 en tu data, o el retorno real necesita el trigger? Compara con lo que SÍ trae gente de vuelta D1/D7 en móvil LATAM.

## Lo que necesito de ti (data L1, no opinión)
- **Carga cognitiva real:** números de abandono/bounce vs nº de sistemas simultáneos en pantalla móvil; cuántos elementos animados antes de "se siente saturado"; comprensión <X seg como gate de retención.
- **Qué simplifican los que escalan:** ejemplos concretos de juegos LATAM/hispanos que PODARON capas (o que murieron por exceso); el patrón de "menos sistemas, más retención".
- **Touchpoint de adquisición:** cómo se comporta la demo web móvil (87% smartphone gama media) con esta densidad; CTR/retención del sticker con vs sin firma-de-build.
- **Retención sin live-ops:** qué retiene D7/D30 en móvil SIN temporadas/timers (relevante a #24/#12 en premium).

## Tensiones que debes resolver (no esquives)
1. **≤7±2 reglas vs riqueza:** ¿el presupuesto cognitivo correcto para retener móvil es MÁS bajo que 7? Da el número de tu data.
2. **Cardinalidad anti-FOMO vs conversión:** ¿el estado terminal sano (#24/#12) cuesta retención que el FOMO daría? ¿O el premium-sin-MTX cambia la ecuación?
3. **Over-engineering:** nombra los 1-2 sistemas que la v1.2 podría PODAR sin perder retención, según tu data.

## Qué entregar (en español, ≤900 palabras)
Para cada hallazgo:
### Hallazgo N: [conclusión concreta]
- **Datos:** números/porcentajes/rangos específicos ("CPM/retención/bounce X-Y%"). Si no tienes el dato exacto, dilo y da confianza.
- **Fuente:** "datos de Meta Ads" / "comportamiento Instagram" / "WhatsApp Business" / etc.
- **Confianza:** Alta/Media/Baja — razón.
- **Mercados:** LATAM / USA general / hispanos-USA (✅/⚠️/❌/❓).

Para cada hueco que ataques, da: **(a) steelman** (la mejor versión del fix), **(b) ataque/mejora** (tu red team con data), **(c) resolución falsable** (el número/gate que mataría o salvaría el sistema), **(d) decisión de César** (el trade-off que solo él zanja: cuánto sistema vale la retención). Cierra con **"Lo que solo yo aporto"** (data L1 de carga cognitiva/retención móvil) y **"Vacíos"** (qué necesitas de Opus —jerarquía/poda— y Gemini —curiosidad/coherencia). Cada cifra = dato de plataforma o márcala estimación.
