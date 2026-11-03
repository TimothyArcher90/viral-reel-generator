# ¿Qué será el output? Opciones y plan

## Respuesta corta

**No un editor de video nuevo.** Un editor completo con timeline propio es reinventar CapCut: meses de trabajo para peor resultado. Lo que sí: un **estudio de capas dirigido por chat** que construye todo y te lo entrega como **borrador de CapCut editable** (más paquete de respaldo). Tú terminas en CapCut, con control total.

## Lo que ya verifiqué (no es teoría)

- El MCP de CapCut está vivo: **66 borradores legibles**, formato no cifrado, ffmpeg y transcripción disponibles.
- Puede **crear y modificar borradores** con: pistas de video (con in/out), overlays de imagen con posición y escala, audio con fades, **textos editables** y **subtítulos desde .srt como pista de texto**.
- Ya existe `capcut_auto_edit`: quita silencios y muletillas, transcribe, pone subtítulos y deja el borrador (cortes no destructivos sobre el original).
- Premiere también está conectado por MCP (requiere el panel abierto): sirve como destino alternativo.

## Lo que NO he verificado todavía (y por qué importa)

1. **Si CapCut importa video con canal alfa** (ProRes 4444 / WebM VP9) y lo respeta en un borrador. Define cómo entran los títulos sobre el presentador. Se prueba en 10 min.
2. **Si CapCut usa Geist** en los textos del borrador. Requiere instalar la fuente en Windows (cambia configuración del sistema: te pido OK antes).
3. **Resaltado de palabra clave por color dentro de un subtítulo nativo.** El MCP aplica un solo color por segmento; el efecto "palabra a palabra con una palabra en lima" necesita otra vía (ver subtítulos).

## Opciones de producto

### A — Chat + borrador de CapCut (empezar aquí)
Hablas con Claude; él transcribe, propone el guion de capas, genera las capas y entrega el borrador en CapCut.
- **Control:** alto. Todo cambio pasa por ti antes de renderizar (guion de capas aprobado).
- **Edición de clips:** cortes por transcripción (quitar silencios, muletillas, tomas repetidas), recorte y reorden, sin tocar `01_RAW`.
- **Salida:** borrador de CapCut + overlays + .srt + MP4 de referencia.
- **Costo de construir:** días. Reutiliza lo existente.
- **Límite:** sin interfaz visual propia; ves el resultado en CapCut o en fotogramas de vista previa.

### B — Dashboard local con chat al lado (siguiente paso)
Página en `127.0.0.1` con: lista del **guion de capas** (cada capa con su tiempo), vista previa por fotogramas, chat, botones **Abrir en CapCut** / **Exportar a Premiere**.
- **Control:** el más alto. Ves y bloqueas cada capa; el chat edita el guion ("sube la gráfica 2 s", "cambia el título").
- **Edición de clips:** *edición por texto* (clic en una frase de la transcripción para cortarla o moverla), como Descript, pero la salida es una lista de cortes que se exporta a CapCut.
- **Costo:** 2–3 semanas de trabajo repartido. Se construye DESPUÉS de aprobar el primer video con la opción A.
- **Límite:** no hay arrastrar y soltar libre de clips; para eso está CapCut.

### C — Editor completo tipo CapCut en el navegador (no recomendado)
Timeline multipista propio con arrastrar, mezclar y efectos.
- **Costo:** meses; decenas de casos borde (audio, códecs, rendimiento). **Se descarta**: CapCut ya es ese editor y ya lo usas.

### D — Destino Premiere en vez de CapCut
Mismo estudio, pero entregando `.prproj` por MCP con overlays ProRes 4444 alfa. Mejor calidad de alfa que CapCut; hay que tener el panel abierto. **Queda como segunda salida**, no la principal.

**Recomendación: A ahora → B cuando el primer video salga bien → D como salida alternativa. C no.**

## Subtítulos que se vean profesionales

El efecto de los reels de referencia: grupos de 2–3 palabras, entrada con pop corto, **una palabra clave en color**, sombra suave. Tres formas:

| Opción | Cómo | Editable | Aspecto |
|---|---|---|---|
| S1 Nativo | Textos de CapCut, uno por grupo, Geist, trazo y sombra | Sí, total | Bueno, sin resaltado de palabra dentro del grupo |
| S2 Capa animada | HyperFrames renderiza los subtítulos con el efecto exacto (alfa) | No (es video) | El mejor |
| **S3 Híbrido (recomendado)** | **Misma transcripción alimenta (a) pista .srt editable en CapCut y (b) capa animada HyperFrames.** Si corriges una palabra, se corrige en el JSON de palabras y se vuelve a renderizar la capa en ~1 min | **Sí: la fuente de verdad es editable** | El mejor |

Regla de la casa: nunca quemados de forma irreparable. S3 la cumple: la capa animada es regenerable y el .srt viaja siempre.
Si CapCut no respeta alfa, el plan B para texto claro es una capa de fondo negro con mezcla "Aclarar" (Screen), que no necesita alfa.

## Entrada de la persona: cómo va el video

1. Entra a `01_RAW` (intocable) con foto o clip de la persona.
2. Whisper → transcripción con tiempos por palabra.
3. Se propone el **guion de capas** (JSON, ver `specs/ejemplo-guion-de-capas.json`).
4. Apruebas en el chat (o en el dashboard).
5. Se generan las capas: infografías y títulos (HyperFrames), mapas (Electric Eye), gráficas de precios (Ride the Lightning), subtítulos.
6. Se compone el borrador de CapCut con todo en pistas separadas y nombradas.
7. Cada cifra rotulada se verifica antes del render.

## Plan por fases (cada una termina en algo que ves)

| Fase | Qué se hace | Cómo sabes que sirve |
|---|---|---|
| 0 (hecha hoy) | Marca como código, esquema del guion de capas, repo | Está en `main` |
| 1 | **3 pruebas gratis:** alfa en CapCut, Geist en CapCut, borrador de ejemplo | Abres el borrador y ves los 3 resultados |
| 2 | **Primer video real** con la opción A y subtítulos S3 | Tú lo abres en CapCut y lo juzgas |
| 3 | Recetas reusables (pasos con panel, comparativa, 3 códigos, mapa, gráfica) | Un video nuevo en menos de 30 min |
| 4 | Dashboard (opción B) | Editas el guion con el chat y ves los fotogramas |
| 5 | Salida a Premiere (opción D) y versión 16:9 derivada | Mismo timeline, dos destinos |

## Riesgos honestos

- El alfa en CapCut es la incógnita más importante; se resuelve en la Fase 1 antes de invertir más.
- Instalar Geist en Windows es un cambio de sistema: se pide OK.
- Los datos de Yahoo y Coin Metrics no sirven para contenido monetizado (el compilador de Ride the Lightning avisa).
- Las 4 referencias son de terceros: se copian mecánica y ritmo, no su marca, textos ni mascota.
- El estudio corre en tu PC; si está apagada no hay render. Para 24/7 habría que mover solo la parte ligera a la nube, no el render.

## Qué necesito de ti

1. **El video de la persona** (Fase 2). Mientras tanto avanzo la Fase 1.
2. **OK para instalar Geist en Windows** (solo tu usuario, sin admin).
3. Elegir: ¿empezamos con **A** y pasamos a **B**, como recomiendo?
