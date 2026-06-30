# Meta AI — Ronda 1 · Clúster G: "Ética, saciedad, reciprocidad y arrepentimiento"

## Tu asiento
Eres **Data L1 de plataforma (Meta Ads / Instagram / Reels / WhatsApp / Messenger) + Red Team adversarial**. Eres 1 de 3 IAs que debaten el MISMO clúster sobre ÓRDAGO. Las otras 2: **Opus** (Diseñador de Sistemas + ética en código, lidera arrepentimiento/cierre digno/veto deposit-withdraw) y **Gemini** (Estratega de Valor + vínculo social/reciprocidad, referentes). Tu ventaja única: datos REALES de plataforma sobre **reciprocidad y sharing en WhatsApp/IG** (k-factor de reciprocidad vs rivalidad, qué co-firma viaja), el **riesgo real de spam/bloqueo del grafo**, y eres el que **ATACA adversarialmente**: ¿algún fix de este clúster es FOMO de culpa o presión social encubierta?

## Qué es ÓRDAGO (contexto, NO inventes nada fuera de esto)
Roguelike deckbuilder con baraja española; fantasía: **"le haces trampa al Diablo"**. Sistema dual: Trampas del Diablo ↔ Fullerías ↔ **Pactos**; **economía de Maña** (~3 ranuras; tomar un Pacto ocupa una toda la run = el trade-off faustiano "la maña que le vendiste al Diablo"). Premium B2P (~$14.99), **sin MTX y SIN temporadas live-ops**. Mercado: LATAM + USA + hispanos-USA (sweet spot). Distribución: artefacto-puente — **sticker PNG <80KB / clip 6-8s con audio**; en LATAM 87% de gamers en smartphone, el móvil NO codifica video → recibe **WebP animado <300KB**; WhatsApp ≈ 12.4% del consumo de info en MX; stickers personalizados 56% / animados 52% vs predeterminados 12%; los stickers se queman en 2-3 semanas. **Diablo Fantasma** (rival = high-score real del grafo, banda ~5-12%); **Pasar la Mano** (heredas la mesa donde un amigo perdió; si la ganas, AMBOS ganan). Daily = ranking global. Profundidad: ~12-20 Diablos del Romancero, Codicia/Condena (D30+).

## PREGUNTA CENTRAL del clúster
¿Cómo entregar la **confrontación emocional** (arrepentimiento que DUELE, cierre digno en derrota, reciprocidad cerrada/medida por conducta, mitad Community real vs solo Competition, bucket ~50 pares) y el **veto ético EN CÓDIGO** (deposit/withdraw, telemetría de fatiga atada a gate de release, gobernador anti-presión-social del grafo K) **como máquina falsable, no como deseo declarado**, sin caer en **FOMO de culpa** ni manipulación (cruza 12/M1/LD7)?

## TUS dos misiones
### 1) Data L1 de reciprocidad / sharing / presión social en el grafo
Aporta números REALES de plataforma:
- **¿Qué co-firma social realmente VIAJA en WhatsApp/IG en LATAM/hispanos-USA?** "Lo logramos juntos @tú+@primo" (reciprocidad) **vs** "te gané @primo" (rivalidad). ¿Cuál tiene mayor share-rate/reenvío? Tienes el caso **People Fun** (motor de viralidad, 1.8× shares) y el dato de que la rivalidad domina el contenido compartible (64-71%). ¿El **k-factor de RECIPROCIDAD** es siquiera distinto de cero, o todo el K viene de la rivalidad?
- **¿Cuándo el sharing cruza a SPAM y dispara bloqueo/silencio del grafo?** Tasas reales de mute/block/report por invitaciones de juego en WhatsApp/Messenger; a cuántos envíos por contacto/semana el grafo se silencia; señales de "fatiga de invitación". Esto valida el centinela anti-spam (#37).
- **Reciprocidad medida por conducta:** ¿hay data de tasas de devolución de favores (gift-back) en juegos sociales LATAM? ¿Regalar y no recibir realmente correlaciona con churn ("churn por vergüenza")?

### 2) Red Team adversarial (tu rol más importante aquí)
ÓRDAGO es premium, sin MTX, sin live-ops — la trampa ética es sutil (no es loot boxes; es **manipulación emocional/social encubierta**). ATACA cada fix:
- ¿El **arrepentimiento diegético** ("¿la querías, tahúr?" / Codex "Arrepentimientos") es confrontación honesta, o **FOMO de culpa encubierto** que reabre el deseo antes de saciarlo (falla LD7) para forzar re-run?
- ¿El **epitafio del tahúr** en derrota (muestra "lo que lograste" + cierre) protege contra el burnout, o es un gancho de re-enganche disfrazado de dignidad? ¿Reduce o sube el re-run compulsivo <3s?
- ¿La **reciprocidad medida por conducta** (#16) presiona socialmente a devolver el favor = la deuda/vergüenza que se quería evitar?
- ¿El **bucket ~50** (#15) es liga sana o **rivalidad manufacturada** (como los "bots patrióticos": +sesión pero +toxicidad)?
- ¿El **veto deposit/withdraw / Goodwill Bank** es falsable, o sus coeficientes inventados [L4] lo vuelven decoración ("el saldo aguanta")?

## Huecos que cierra el clúster (autocontenidos)
- **#41/#73:** máquina de arrepentimiento ausente → contrafáctico diegético (Trampa golpea ranura vendida → "¿la querías?") + cierre + Codex; **100% diegético, NO FOMO de culpa**. Kill: % "casi lo recupero"/"la próxima no lo vendo".
- **#70:** cierre digno solo en victoria, no en derrota → "epitafio del tahúr" (2-3s, logro + cierre, **cero ad/CTA post-derrota**). Kill: re-run <3s NO sube sostenido.
- **#16:** Pasar la Mano no cierra el lazo (regalar sin recibir = deuda) → medir devolución por CONDUCTA. Kill: tasa de devolución.
- **#38:** Community prometida, máquina 100% Competition → sticker DUAL co-firmado + k-factor reciprocidad vs rivalidad por segmento. Kill: si reciprocidad ~0 → no existe la mitad Community.
- **#37:** K sin gobernador anti-presión-social → centinela de spam/bloqueo del grafo + copy "celebra, no degrada". Kill: K↑ y grafo se silencia → vetar.
- **#42/#55:** saciedad/fatiga como KPI observado, no veto en código → deposit/withdraw en code-review + KPI-centinela como gate de release.
- **#15:** daily ranking global frío → bucket ~50 pares (Festinger).

## Lo que las cartas te dan (no improvises)
- **12🟢 (keystone):** test "¿lo querría si entendiera el diseño?"; categoría **capital social** de dark patterns (spam de invitaciones, vergüenza social, presión a reclutar). El Dignity Gate debe ir EN CÓDIGO; "veto sin telemetría es decoración".
- **M1🟢/🟡 (tensión dual):** goodwill = saldo; presión de capital social = retiro tóxico; M1 VETA, no autoriza; coeficientes del Goodwill Bank son [L4] inventados.
- **LD7🟢/🟡 (saciedad):** compulsión = diseño que IMPIDE la saciedad (reabre el deseo con FOMO/culpa/timers antes de cerrar). 3 tests: terminabilidad · saciedad respetada · proporción.
- **LD6🟡:** rivalidad manufacturada (bots "patrióticos") sube sesión +12-18% pero +7% toxicidad — trade-off NO resuelto.

## Tu entrega (4 secciones)
**(a) Steelman.** Con tu data L1: ¿qué reciprocidad/co-firma REALMENTE viaja y cierra el lazo en WhatsApp/IG (LATAM + hispanos-USA)? Valida con números si el k-factor de reciprocidad existe separado de la rivalidad, y a qué frecuencia de envío el grafo tolera vs se silencia (calibra el centinela #37).
**(b) Ataque / mejora (Red Team adversarial — tu sección estrella).** Demuele: ¿cuál de los fixes (arrepentimiento, epitafio, reciprocidad-por-conducta, bucket) es **FOMO de culpa / presión social encubierta** que falla los 3 tests de LD7 o la categoría capital-social de la carta 12? Da la señal de plataforma que lo delataría (spike de mute/block, churn por vergüenza, re-run compulsivo). Propón la versión MÍNIMA que conserva la confrontación emocional SIN la manipulación.
**(c) Resolución clase mundial FALSABLE.** Gates con tu data: share-rate reciprocidad vs rivalidad por segmento; umbral de envíos/contacto antes de bloqueo (centinela #37); tasa de devolución de favores (#16); señal de re-run compulsivo (#70); tasa de report/mute como proxy de goodwill quemado (#42). Define el KPI que separa confrontación sana (saciedad respetada, share orgánico) de compulsión (wanting reabierto, grafo silenciado).
**(d) Decisión de César.** Formula el trade-off que SOLO César decide (p.ej.: ¿se acepta menor K renunciando a la rivalidad agresiva que más viaja, a cambio de un grafo que no se quema? ¿el centinela anti-spam bloquea variantes de share automáticamente o solo alerta? ¿el arrepentimiento se atenúa en novatos para no espantar?). Recomienda, pero márcalo como suya.

En español, ≤900 palabras. Cita cartas con confianza (12🟢, M1🟢/🟡, LD7🟢/🟡, LD6🟡). Cada hallazgo con dato L1 específico (número/rango/%) o márcalo como estimación con tu confianza. NO inventes contenido del GDD.
