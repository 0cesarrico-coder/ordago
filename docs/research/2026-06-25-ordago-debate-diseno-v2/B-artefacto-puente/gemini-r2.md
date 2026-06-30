# Clúster B · Ronda 2 — ASIENTO OPUS (Diseñador de Sistemas de Crecimiento)

---

## 1. STEELMAN

### Gemini (Estratega de Valor/Mercado)
El acierto de Gemini es vincular la conversión visual al foso real del juego (**Trampa vs. Fullería**) en lugar de imitar a *Balatro*. Su tesis de que la tensión del "Pillado" retiene más que el "Barrido" matemático es impecable (**L2 🟢**). Su propuesta de un **Codex de Seeds** (`ordago.gg/d/<seedhash>`) automatizado es brillante: convierte un consumible viral efímero en infraestructura de adquisición orgánica permanente, capturando el tráfico de alta intención que los competidores premium ignoran.

### Meta AI (Data L1/Red Team)
Meta AI aterriza el diseño en el barro de la infraestructura real de LATAM. Su análisis de las limitaciones de WhatsApp (limite de reenvíos, WebP de ≤100KB/≤500KB, **L1 🟢**) y las restricciones de `WKWebView` (bloqueo de autoplay con audio, **L1 🟢**) es inapelable. Su visión de que **"WhatsApp quema el grafo y Reels lo enciende"** es la separación funcional exacta que el sistema necesita para no malgastar recursos de ingeniería en clips con audio pesados que mueren en el in-app browser.

---

## 2. ATAQUE

*   **A la landing SEO de Gemini ("Codex autogenerado indexable por Google"):** Generar una página HTML indexable por cada run individual de la demo web es un **dev-trap y un suicidio de SEO técnico**. Google penaliza el *thin content* y los millones de seeds vacíos generarán indexación basura (soft-404s), hundiendo el dominio `ordago.gg`. Además, exige un servidor dinámico crawlable, traicionando el principio de **0 servidor** e inflando costos de hosting de forma absurda antes de validar el juego. **L3 🟡**.
*   **Al "No SSR por seed" de Meta AI (#19):** Su solución para evitar el timeout del scraper es rendirse y servir un `og:image` 100% estático y genérico ("te acaban de robar el alma"). Esto destruye el **chisme relacional** ("María te ganó por 2"), que es el principal multiplicador de CTR en dark social. El miedo de Meta AI al timeout del scraper se soluciona con mi arquitectura híbrida: el HTML inicial sirve una imagen cacheada estática como *fallback* instantáneo (<50ms), mientras el cliente hornea el PNG dinámico en background y lo sube a la CDN keyed por nonce para el siguiente salto. **L4 🟢**.
*   **A la distribución 70/30 (Sticker/Clip) de Meta AI:** Minimizar el Clip como "solo para Reels" e ignorar su rol en la demo web reduce la *watchability* de la propia partida. El loop de juego de la demo web *necesita* el clip de 6s como recompensa visual de la primera mano jugada. Sin él, el jugador de la demo web no entiende la tensión y el sticker que genera nace muerto.

---

## 3. CONVERGENCIA

### Convergemos en (Consenso):
*   **Muerte definitiva del Romancero (#25):** Se difiere post-lanzamiento.
*   **Límites de peso físicos:** Stickers estáticos <80KB (WebP) y animados <300KB (WebP/GIF) generados 100% en cliente.
*   **Comportamiento de WKWebView (#22):** Audio *muted* por defecto con `playsinline`, activado únicamente tras interacción del usuario.
*   **Estructura del Clip (0-8s):** Estructura fija de Gancho (0-1.5s) -> Quiebre (1.5-4s) -> Sospecha/Tensión (4-6s) -> Desenlace/Pillado (6-8s).

### CONTESTADO:
*   `CONTESTADO: Personalización del preview`: ¿Estático genérico por seed (Meta AI) o Híbrido dinámico CDN keyed por nonce (OPUS)?
*   `CONTESTADO: Arquitectura Web`: ¿Codex indexable con HTML dinámico/Schema (Gemini) o Aplicación SPA estática 0-servidor con beacons stateless (OPUS)?
*   `CONTESTADO: K2 Atribución`: ¿Atribución transparente por deep-link + nonce local (OPUS) o asumir pérdida de tracking en Dark Social (Meta AI)?

---

## 4. REFINA: RESOLUCIÓN DE CLASE MUNDIAL

Aseguramos la ignición del Clúster B mediante cuatro compuertas (Gates) técnicas e inalterables:

```
[Tráfico Reels/TikTok] ──(Hold-rate >45% @ 3s)──> [Demo Web 0-servidor] ──(Nonce-Link)──> [WhatsApp: Sticker <80KB + Texto] ──(K2 >0.35)──> [Wishlist Steam]
```

### El Framework de Validación Falsable (Ignición):

| # | Gate / Objeto | Métrica de Éxito | KILL TRIGGER | Nivel Evidencia | Confianza |
|---|---|---|---|---|---|
| **G1** | **K2-Activación (Sticker)** | **K2** = (Invitados de demo que completan 1 mano via nonce-link) / (Clicks en demo web). Objetivo: **≥0.35** | **<0.15** → El sticker no incita a jugar. Rediseñar copy relacional. | **L2 (Chen)** | 🟢 |
| **G2** | **Performance OG-Image (#19)** | CDN entrega fallback estático a Scraper en **<80ms** (p95). Upload del PNG dinámico (cliente a CDN) en **<300ms** tras fin de mano. | **>150ms** fallback / **>500ms** upload → Causa previews rotos. | **L1 (Docs API)** | 🟢 |
| **G3** | **Watch-Time del Duelo (#60)** | Hold-rate del clip de 6s en Reels/TikTok: **>45% al segundo 3**; **>25% completion** a 8s. | **<15% completion** → El clip es aburrido. Cambiar el "Pillado" por más caos. | **L1 (Mosseri)** | 🟢 |
| **G4** | **Fricción WKWebView (#22)** | Demo Web inicia en iOS/Android *in-app browser* en **<1.5s** (Lighthouse Mobile). Autoplay en silencio activo instantáneo. | **>2.5s** o video pausado esperando tap → Muerte del drop-off. | **L1 (Safari Specs)** | 🟢 |

### Implementación del Tracking K2 (0-Servidor, Sin Cuentas):
Para evitar el costo de base de datos, implementamos el **atribución por Token de Generación Local (Nonce)**:
1. El usuario A juega la demo (`ordago.gg/d/<seed>`). Al terminar, el cliente genera un `nonce_padre` aleatorio de 8 caracteres y lo guarda en `localStorage`.
2. El botón de compartir copia al portapapeles: `ordago.gg/d/<seed>?ref=<nonce_padre>` + un Sticker WebP que lleva embebido el `nonce_padre` en sus metadatos EXIF.
3. Cuando el usuario B abre el link y **completa** la mano, la demo web emite un beacon HTTP POST stateless de 1 byte a un recolector de telemetría: `{p: "nonce_padre", c: "nonce_hijo"}`.
4. **K2 se calcula semanalmente** contando el ratio de padres únicos que tienen al menos un hijo registrado con `mano_completada=true`.

---

## 5. DECISIÓN DE CÉSAR

*   **Decisión 1: El dilema del SEO vs. 0-servidor.**
    *   *Recomendación:* **Rechazar el indexador de Gemini.** Mantener la demo web como SPA estática montada sobre CDN (Cloudflare Pages/Vercel). El tráfico SEO debe canalizarse no a través de millones de seeds basura, sino de una **única Landing de Compendio** estática que liste los 100 seeds más jugados de la semana (actualizada vía script cron una vez al día). Esto conserva el foso técnico de 0-servidor, evita penalizaciones de Google, y cuesta $0.
*   **Decisión 2: Personalización de la previsualización (OG-Image).**
    *   *Recomendación:* **Aprobar la arquitectura híbrida de OPUS.** No podemos irnos con el texto estático y genérico de Meta AI porque destruye el CTR. Al cargar la demo web, el backend sirve inmediatamente un tag HTML con `og:image` apuntando a la imagen genérica de la seed. Al terminar la partida, el cliente renderiza un canvas con el chisme personalizado ("Te gané por 2"), hace un `PUT` directo y firmado desde el cliente a un bucket de S3/R2 con CDN, y actualiza el link del portapapeles. El scraper que lee el link dinámico mostrará la humillación exacta.