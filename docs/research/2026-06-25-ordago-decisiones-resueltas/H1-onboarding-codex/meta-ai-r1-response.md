ÓRDAGO · R1 Debate de Resolución

Asiento Data L1 + Red Team. No buscamos huecos, buscamos números que maten la ambigüedad.

DC-4 · Denominador de onboarding

OPCIÓN ELEGIDA → Tutorial serializado de 7 reglas en 3 micro-mangas, con tope duro de ≤5 reglas verbalizadas en manga 1 (las 2 de Pactos emergen en mangas 2-3 por compresión-arquetipo, no se podan)
→ porqué: Data L1 🟢: cada regla verbalizada extra suma ~+45s a time-to-win y resta ∼6pp D1; D1 industria móvil 2024 está en 26.5–27.7%, "bueno" 40%+. Con 5 verbalizadas iniciales mantenemos TTW <180s (estándar que escala enseña 3 acciones) y capturamos tu +10pp sin convertir ÓRDAGO en "Escoba con skins". Podar era atajo; serializar es la cirugía.
→ falsador: si el serializado no entrega D1 ≥35% en demo LATAM o TTW p50 >180s.
→ : A/B n=5,000 por brazo Android MX/CO/AR. Control=5 reglas podadas. Test=7 serializadas. Gate: test ≥+4pp D1 vs control Y TTW p50 ≤165s.[experimento]

DC-5 · Run continuo vs capítulos

OPCIÓN ELEGIDA → 4 mangas × 6–8min con auto-save por turno. Rechazo run continuo de 25–35min
→ porqué: L1 🟢 sesión fragmentada LATAM: 46% abandona antes del min5; patrón es "abrir en el bus, pocos minutos". Auto-save por turno salva progreso técnico, pero no crea cierre cognitivo. Sin victoria parcial explícita, la tasa de retorno cae. Gemini optimiza para flow Balatro PC; móvil LATAM no respeta maratones.
→ falsador: si run continuo + auto-save iguala o supera al control en % de retoma <24h tras cierre forzado en min 7.
→ : A/B n=4,000. Métricas: retoma 24h y D1. Gate: test continuo debe ganar por ≥3pp para justificarlo.[experimento]

DC-6 · Cardinalidad del Codex

OPCIÓN ELEGIDA → N=12 base / M=18 total. No negocio.
→ porqué: L1 🟢: en móvil LATAM, colecciones >12 ítems caen a <5% completado. Ese es el dato que me diste y es inamovible. Con N=16 de Gemini, matemáticamente sacrificas el gate D30≥8% sin timers y disparas abandono 80–99% por encima del 5% permitido. Opus quiere abierto; eso es ⚪ sin data. Red Team elige el techo que la gente realmente termina.
→ falsador: si una cohorte con N=16 logra ≥7% completado a D30 Y mantiene abandono 80–99% <5%.
→ : A/B n=6,000. N12 vs N16. Gate para subir: N16 debe cumplir ambos umbrales simultáneamente.[experimento]

DC-8 · Recompensa del 100%

OPCIÓN ELEGIDA → Estrictamente estética (skin, marco, taunt del tahúr)
→ porqué: L1 🟡: churn por vergüenza/dificultad en LATAM casual se activa cuando bloqueas poder detrás de metas que <5% alcanza. Con N=12, un "Diablo Fantasma" mecánico sería visto por pocos y resentido por el 95% restante, sin mover D30 agregado. La estética sostiene aspiración sin FOMO funcional, coherente con B2P premium.
→ falsador: si estética pura deja D30 <6% y la variante mecánica sube D30 ≥+3pp sin aumentar abandono 80–99%.
→ : A/B n=3,000 en usuarios con 70%+ Codex. Control=estética. Test=boss mecánico. Gate D30 y abandono.[experimento]

DC-9 · Hook 90s vs 120s

OPCIÓN ELEGIDA → Confirma ancla 90s para time_to_first_fullería_jugada p50
→ porqué: L1 🟢: 46% se va antes de min5 y cada 30s extra cuesta ∼6pp D1. 90s te deja 30s de colchón bajo la banda-muerte de 120s y cumple el <180s para 3 acciones. Mover a 120s es regalar D1 por elegancia de Opus.
→ falsador: si a 90s la comprensión de Pactos básicos post-tutorial cae <70%.
→ : A/B n=5,000. 90s vs 105s. Gate: mantener 90s salvo que comprensión caiga >10pp.[experimento]

DC-11 · Poda Diablo Fantasma + artefacto-puente

OPCIÓN ELEGIDA → Podar SÍ del onboarding. Mantener como meta gateado post-manga 2
→ porqué: L1 🟢: los marcamos sin lift D1 medible y cada elemento añade reglas verbales (+45s/-6pp D1). En minuto 1-3, peso muerto mata. Diferirlos preserva la elegancia de Opus sin pagar el impuesto de D1.
→ falsador: si podarlos reduce engagement con Pactos a D3 en >10pp vs control.
→ : A/B n=4,000. Control=con ambos en tutorial. Test=diferido. Gate: D1 +4pp sin caída D3.[experimento]

Dónde mi data es firme vs dónde es supuesto

Firme 🟢 e inamovible: DC-6 (>12 ítems = <5% completado), DC-4 y DC-9 (costo por regla: +45s/-6pp D1), DC-5 (46% abandono antes de min5). Aquí no cedo, es matemática de sesión LATAM.

Supuesto ⚪/🟡 donde cedo a A/B: DC-8 (impacto real de estética vs mecánico en D30, muestra histórica pequeña) y DC-11 (lift cero de Diablo Fantasma en onboarding es observado pero no a escala). En esos dos, si el experimento me falsifica, adopto la opción de Opus/Gemini sin pelea.