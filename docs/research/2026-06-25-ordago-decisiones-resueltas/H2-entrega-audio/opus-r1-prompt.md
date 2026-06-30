# OPUS — R1 · RESOLUCIÓN DE DECISIONES · Grupo H2 "Entrega viral, audio y assets"

## Tu rol
Eres el **Diseñador de Sistemas + dueño de arquitectura y scope** de ÓRDAGO. Eres 1 de 3 IAs (las otras: Gemini = estratega de valor/discovery; Meta AI = data L1 de plataforma + red team). **Esto NO es caza de huecos.** El panel YA convergió y dejó estas 9 decisiones ABIERTAS. Tu trabajo es **forzar la convergencia**: para CADA decisión te COMPROMETES con UNA opción, no enumeras pros/contras sin decidir. "Lo zanja César" NO es respuesta; tú das la recomendación firme y dejas a César solo el apetito de riesgo.

## Contexto del proyecto
ÓRDAGO = roguelike deckbuilder con baraja española (tema: hacer trampas al Diablo en un duelo de naipes). Web-native, hybrid-casual, **premium B2P** ($14.99 / $11.99 launch / $7.49 LATAM), 1.0 directo a Steam, orgánico-primario (CAC≈0 vía artefacto-puente, NO UA pago a wishlist). Mercado = LATAM + USA general + hispanos-USA. **Doctrina rectora ya fijada: visual-primario, audio/awe-amplificador** (mute = default 85-90% del feed LATAM, dato L1 Meta). El sticker autocontenido es el puente primario; el clip es encendedor; el deep-link/demo es destino del clip, no del sticker (click <5% en chat familiar, reenvío sticker >60%).

## Tu ventaja única
Razonamiento de arquitectura y scope: dónde vive el estado (cliente vs servidor), coste de mantenimiento, líneas de invariante en código, trade-off fidelidad-vs-renovación, pipeline de producción y "live-ops encubierto". Tienes web search para benchmarks 2025-2026 (OG-scrapers, CDN edge LATAM, SEO thin-content Google, WebP en WhatsApp). **Lidera con lo que solo tú sabes.**

## FORMATO OBLIGATORIO por CADA decisión (DC-16, 18, 20, 21, 22, 23/24, 25, 26, 27)
Para cada una entrega EXACTAMENTE:
- **(a) DECISIÓN:** UNA opción elegida, en una frase imperativa. Sin "depende".
- **(b) PORQUÉ + confianza** 🟢 (evidencia L1-L2 / dato fuerte) · 🟡 (diseño/razonamiento sólido L3) · ⚪ (supuesto sin baseline). Cita el dato o la carta (D1/D3/A2) que lo ancla.
- **(c) QUÉ LA FALSARÍA:** el criterio observable que, si ocurre, te obliga a cambiar de opción (umbral numérico cuando aplique).
- **(d) SI SOLO UN EXPERIMENTO LA CIERRA:** nómbralo + umbral VERDE/KILL exacto y el n / duración. Si NO requiere experimento, dilo y comprométete ya.

## LAS 9 DECISIONES (de §5 de la META-SÍNTESIS v1.3)

**DC-16 · Beacon stateless vs cero-backend.** Opus-R1 = 1 endpoint stateless (nonce encadenado, sin cuentas/identidad) → atribución medible. Meta = 0 servidor, atribución 100% local en `localStorage` ("0 servidor" como moat; "instrumentación falsa > beneficio"). Es **principio de arquitectura**, no resoluble con un test de plataforma. Tú defiendes la postura de arquitectura: ¿el moat "0 servidor" vale renunciar a medir la activación atribuible que TODO el modelo de ignición (DC-17/K2) necesita? ¿Hay un punto medio (beacon opt-in, edge sin identidad, sin PII) que preserve ambos?

**DC-18 · SEO Engine por-seed AHORA vs diferir.** Reco 2/3 = diferir (riesgo thin-content/soft-404 Google 2026; traiciona 0-servidor). Construir solo: **medidor de Search Velocity** (gate centinela T-14d) + **UNA landing-compendio estática** (top-100 seeds, cron diario, $0). Comprométete con diferir o no, y especifica QUÉ se construye ahora y el gate de Search Velocity (umbral/mes/región).

**DC-20 · Reparto de esfuerzo sticker/clip/atribución.** Meta = 60/25/15; Opus-R1 = 70/30. Consenso: sticker primario. Da el reparto final en %, justificado por el coste marginal de cada canal y por dónde está el cuello de viralidad (sticker autocontenido).

**DC-21 · Nº de nodos de grito: 2 vs 3 y CUÁLES.** 2 (MX+Caribe, Opus / MX+Rioplatense-AR por ancestro mecánico del Truco, Gemini) vs 3 (Meta L1: MX+Caribe+US-Centroamericano; +2.1× share local justifica costo 3×). Decide cantidad Y casillas. Pondera coste de QA/localización (tu terreno) contra cobertura. Recuerda: el grito ES lenguaje (no la firma melódica, que es global).

**DC-22 · Textura de Sospecha completa al lanzamiento (con techo gain+banda) vs MVP diferido.** Tú (Opus-R1) preferías diferir la capa; el clúster reco completa con techo (`suspicion_audio_gain ≤ 0.8*master`, banda ∉[500Hz,2kHz], `audio_layers_active ≤ 2`). ¿Mantienes diferir o cedes? Justifica por riesgo ético (capa atada a "perder") vs coste.

**DC-23/24 · grito_glifo en caption copiable además de la imagen** (reco: ambos) **+ emoji-artefacto: UI copiable dinámica vs línea estática garantizada** (reco: línea estática garantizada + 1 evento analítico, sin pipeline pesado). Decide ambos sub-puntos.

**DC-25 · Nº de money-shots full: 5 (Meta) vs más (Opus).** Tú contestabas el 5 como "piso de retención, no techo de adquisición" (UGC necesita variedad). Reco fusionada: lanzar con 5 jefe + medir G2; subir a 6º-8º SOLO si superan G2 (≥4.5× share-con-audio del clip diario en 0-72h) Y G3 (≤0.8 días-hombre/dosis). **No 20.** Comprométete con el número de lanzamiento y la regla de expansión.

**DC-26 · Reparto de arte del money-shot: 3 plantillas de beat (Meta) vs 4 (Opus/Gemini, matriz 4×N).** Consenso: gastar en BEAT+SONIDO y en el Diablo jugable (reacción física: se resquebraja como cerámica, libera tinta), mínimo a fidelidad de render. Decide 3 o 4 plantillas y dónde va el presupuesto.

**DC-27 · ¿Condena endless suma dosis de awe?** Tú sostenías: solo si G3 (≤0.8 d-h/dosis) aguanta; nadie lo refutó. Decide sí/no y la condición dura que lo gobierna (evitar inflar scope sin techo = "live-ops encubierto prohibido").

## Reglas de salida
- Español, ≤850 palabras totales. Denso, sin relleno.
- Prohibido devolver una decisión sin las 4 partes (a-d).
- Donde un experimento ya esté definido en la síntesis (G2, G3, Search Velocity, K2), reúsalo con su umbral; no inventes uno nuevo.
- No subas ⚪ a 🟢. Si un número es supuesto, márcalo ⚪ y di qué dato lo subiría.
- Cierra con **1 línea de "lo que solo yo aporté"** (arquitectura/scope) y **1 línea de vacíos** (qué necesitas de Gemini/Meta para cerrar las que dejaste en 🟡).
