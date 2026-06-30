# ÓRDAGO — Style Bible (1 página) + catálogo Concept-Visual-First

> El ancla barata que el GDD §11 (v1.3.2) exige ANTES de generar arte: shape language +
> color script + regla de tono + "qué sí / qué no". Reescribir la dirección de arte a mitad
> del pipeline es el desperdicio más caro de un estudio chico. **La dirección FINAL es decisión
> del usuario (§11 / §19.3 #2 = firma):** este doc + los mockups la teean, NO la cierran.

## Regla de tono
**Cantina barroca latinoamericana, cálida y teatral — NO fría ni abstracta.** Folk del Día de
Muertos por **grabado tipo Posada** (dominio público) + velas, oro sucio, naipe gastado. El Diablo
es un **tahúr tramposo carismático**, no terror gore. Humor pícaro del trickster que le gana al poder.

## Shape language (lenguaje de formas)
- **Naipe:** esquinas redondeadas suaves, papel con textura/desgaste; figuras (Sota/Caballo/Rey)
  con ilustración tradicional de fondo y el **valor de juego 8/9/10 GRANDE** al frente (§7.2).
- **Diablo:** siluetas de calaca/Posada, líneas de grabado (filigrana), cuernos; reconocible a 100×100 px.
- **Maña:** Fullería = silueta "tuya" (mano, ojo); Pacto = silueta "corrupta" (cadena, tinta). Distinguibles por FORMA, no solo color (§7.6e).
- **Mesa:** tapete de cantina (fieltro verde gastado), velas, manchas de vino/oro.

## Color script (hex + FUNCIÓN, no solo paleta bonita) — canal redundante (§10)
| Función | Color | Refuerzo no-cromático |
|---|---|---|
| Fondo cantina | `#1a0e14` → `#2a1622` | — |
| **Puntos** (azul) | `#6f9bd1` | glifo/etiqueta numérica |
| **Suerte** (rojo) | `#d4495e` | aspa "×" |
| **Manos** (verde) | `#6fb36f` | pips contables |
| **Reales/oro** | `#e8b13a` | "R" / 🪙 |
| Diablo / peligro | `#7a1f2b` | silueta de cuernos |
| Acierto / Escoba limpia | `#7fd18a` | barrido + destello |
> Saturado SOLO en lo accionable (jerarquía de valor) para no romper el glance-gate @100×100 px grises.

## Qué SÍ / Qué NO
- **SÍ:** Posada dominio público · folk MX auténtico (cempasúchil, papel picado, oro sucio) · velas · naipe gastado · humor pícaro.
- **NO:** Catrinas de marcas, personajes de películas, barajas comerciales (riesgo IP §11) · "boutique en Tulum"/blanqueamiento (maximalismo identitario, no minimalismo aséptico) · gore/terror · re-teñir colores funcionales por palo.

## Las dos direcciones a A/B-testear (el crux §11 — decide el USUARIO con data de feed)
- **Lado A — Claroscuro boutique premium** (negro/oro-vela; tipo Inscryption/Cult of the Lamb): alto CTR en trailers. *Riesgo: blanqueamiento.*
- **Lado B — Maximalismo identitario** (oro sucio, cempasúchil, papel picado, color y textura): autenticidad, mitiga apropiación, es lo que LATAM guarda. *Restricción: jerarquía de valor para no romper el glance-gate.*

---

## Catálogo de conceptos visuales a generar (Concept-Visual-First, prioridad)
> Generar con modelo de imagen de FRONTERA (Nano Banana Pro / Gemini 3 Pro Image vía Higgsfield),
> 2–4 variantes A/B por concepto, ancladas a esta página. **El usuario elige el ganador antes de
> reemplazar los "rectángulos" del prototipo por arte.** El prototipo actual (`game/`) es la
> referencia de COMPOSICIÓN/layout contra la que se valida cada mockup (smoke + screenshot).

| # | Pantalla / asset | Por qué importa | Variantes |
|---|---|---|---|
| B0 | **Key-art / capsule de Steam** | superficie de conversión más cara; glance-gate ≥90% @100×100 grises (§11) | A claroscuro / B maximalista |
| B1 | **Pantalla de juego (HUD+Mesa+mano)** | la composición que separa "amateur" de estudio; ancla = el prototipo actual | A/B paleta |
| B2 | **El Diablo-tahúr** (sembrando, pillándote, resquebrajándose) | money-shot §10.2; reacción física legible muda | 3 poses |
| B3 | **Carta/naipe** (número, figura 8/9/10, Mata, Marcada) | legibilidad del valor; identidad del palo por forma | set |
| B4 | **Ficha-sticker (RunDigest §8.3)** | el artefacto-puente; chisme legible @100×100 grises | 2 layouts |
| B5 | **Cantina** (tienda de Maña) | el trade-off faustiano legible (Pacto corrupto vs Fullería tuya) | A/B |
| B6 | **Trampa sobre la Mesa** (Oros agrietados, HUD reescribe 13) | el corazón dual debe LEERSE, no memorizarse (§7.6e) | set |

**Flujo:** ancla de estilo validada → fan-out image-to-image → mockups de layout completo →
**el usuario elige** → implementar el ganador en código → verificar (screenshot vs mockup).
