RONDA 3 — CIERRE DATA L1 + RED TEAM

Vengo con la navaja puesta: si el objeto no cruza WhatsApp sin que tu tía pregunte "¿qué es esto?", no hay foso, no hay economía, no hay #1. La data de plataforma en LATAM manda sobre la intuición de diseño.

Resolución de los 3 cruxes

1. Formato del objeto-puente: texto plano vs imagen-sticker PNG
CIERRO hacia IMAGEN-STICKER PNG generada localmente (<80KB), con texto plano solo como fallback automático.

Dato decisivo: WhatsApp concentra 12.4% del consumo de información en México, por encima de Facebook 11% y YouTube 10.7%, y lo que se mueve ahí no es código, es visual. En estudios de uso, 56% de usuarios usa stickers siempre o frecuentemente (32% + 24%), y el ecosistema de stickers personalizados domina sobre los predeterminados. Un grid de texto se lee como "predeterminado genérico", el PNG con "Le robé el alma a @primo" se lee como humillación personal, que es lo que dispara i en K = i × c. 

Peso no es excusa: Profeco mide 1 MB por mensaje de texto y 1 MB por imagen en WhatsApp, así que la imagen no añade fricción. El texto plano queda como fallback para feature phones, no como canónico. 

2. Soporte del clip: móvil co-primario vs exclusivo PC
CIERRO hacia CLIP EXCLUSIVO PC para generación, con distribución móvil vía asset pre-renderizado (WebP animado <300KB), no codificación en navegador.

Dato decisivo: la codificación client-side en móvil "choke the main thread, exhaust browser heap memory, and lock the user's interface". En LATAM, 87% de los gamers usa smartphones, mayormente gama media-baja. Pedirles que rendericen MP4 a 60fps es matar B5 (fricción cero). 

Pero el video importa: Reels obtienen entre doble y 12 veces más alcance que posts, y en crisis de alcance los Reels logran "entre 2 y 12 veces más alcance". Solución de clase mundial: el cliente Steam genera el clip de 6-8s con audio firma (<500KB) y lo sube; la demo web móvil solo sirve una versión pre-hecha ligera, sin encodear nada. No diferimos a vertical slice, lo construimos ya, pero separado por plataforma. 

3. Banda de spread de EV: ≤15% vs 15-25%
CIERRO hacia BANDA DUAL: rechazar si spread >20%, contar como "duda real" solo si ≤15% a 2-3 turnos.

Dato decisivo no es de plataforma, es de falsabilidad. Gemini tenía razón en que <10% se siente ajedrez seco, Opus tenía razón en que >20% es trampa de novato. La banda 15-25% que proponía Gemini permite dominancia que el propio KPI de entropía declararía emergencia. Mi fix: el solver garantiza liveness con 20% como tope duro de re-siembra, pero solo los tableros ≤15% suman al contador de foso vivo. Es medible en papel antes de un píxel, y cruza con el test del experto.

Posición DEFINITIVA

Palanca 1 — Artefacto-puente

Ganador: sistema dual con UNA fuente (RunDigest). A) Sticker-imagen PNG generada en cliente (<80KB) con grid dibujado + línea verbo "Le robé el alma a @primo +X%" + deep-link. B) Clip 6-8s con audio firma generado solo en PC Steam (<500KB), distribuido en móvil como WebP animado pre-renderizado. Texto plano solo fallback. Confianza 🟢 por data L1 WhatsApp 12.4% y uso stickers 56%. 

Palanca 2 — Generador + foso vivo

Ganador: invariante verificado por solver ANTES de arte. Regla: ≥2 jugadas Pareto-no-dominadas, spread EV ≤15% para contar como duda real, re-siembra si >20% (máx 8 intentos). Instrumentación: entropía Shannon de builds ganadores semanal (alarma caída >15%), y test del experto vía Diablo Fantasma como proxy de brecha skill. Confianza 🟡 (cifra calibrada en vertical slice).

Palanca 3 — Economía

Ganador: separar loops. Adquisición: demo web móvil → wishlist (CAC >0). Retención: Diablo Fantasma + sticker (CAC∼0). Modelo 3 columnas realista: USA $14.99 neto ∼$10.49, Hispanos-USA $14.99, LATAM $149 MXN (∼$7.49). Gate LTV/CAC ≥3 por segmento antes de vertical slice. Backend propio para leaderboards. Confianza 🟢 por mobile-first 87%. 

C-1 — Plataforma

Voto final: HÍBRIDO. Steam premium como producto completo, demo web móvil ultraligera (<10MB, carga <2s en 4G) como primera mitad del artefacto. Trade-off aceptado: +15% scope para mantener dos builds, y riesgo de piratería parcial de la demo (mitigado porque solo es 1 mano, sin meta). Lo acepto porque sin fricción cero en WhatsApp, el K-factor no compone.

Cambio de mayor apalancamiento al GDD v1.2

Convertir el artefacto-puente de "código de texto copiable" a "sticker-imagen PNG generada localmente con deep-link jugable", porque ese es el único formato que los hispanos reenvían sin vergüenza y que convierte la comprensión en acción viral medible.
Fuentes