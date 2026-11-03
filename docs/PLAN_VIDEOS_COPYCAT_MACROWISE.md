# PLAN — Videos "copycat" con línea gráfica MacroWise

Objetivo: tú das el video de la persona grabada; el sistema monta encima subtítulos animados, infografías, mapas y gráficas financieras animadas. Estructura y animaciones copiadas de los reels de aztec.lab; identidad 100 % MacroWise.

## 1. Veredicto sobre el dashboard local

**Sí, un dashboard local es lo correcto. No Railway.**
- Ya tienes dos estudios locales que funcionan así: Ride the Lightning (`http://127.0.0.1:5180`) y Electric Eye. Se abren con un icono de escritorio y tú no tocas terminal.
- El render de ProRes 4444 con alfa, el Chromium sin ventana y las series con licencia no encajan en un servidor barato; tu equipo (Ryzen 7 + RTX 4050) sí los aguanta.
- Las licencias de datos (Yahoo, Coin Metrics: uso no comercial) se controlan mejor en local, con el aviso del compilador.
- Railway se deja para después y solo para lo que deba correr 24/7 sin tu PC (el radar, el worker de Zappa). Si más adelante quieres que el equipo lo use desde fuera, se sube una versión que solo reciba el brief y use el render local como servicio.

**Cómo se vería (un solo icono "MacroWise Video Studio", puerto 5190):**
1. Sueltas el video de la persona + (opcional) una foto + el tema o guion.
2. Transcribe (Whisper) y propone un **guion de capas** con tiempos: qué sale en cada segundo (título, panel, mapa, gráfica, subtítulo).
3. Tú ves una vista previa por fotogramas y apruebas o cambias en lenguaje normal.
4. Genera las capas, compone y exporta.
5. Entrega: overlays ProRes 4444 con alfa + subtítulos .srt editables + MP4 de referencia + timeline abierto para Premiere.

## 2. Línea gráfica MacroWise (memorizada, aplica a TODOS los videos)

Traducción de lo que vi en aztec.lab a tu marca:

| En el original | En MacroWise |
|---|---|
| Panel crema `#F1ECE7` con rejilla | Panel **Warm Black `#1A1A17`**, rejilla 1 px en `#232320`, opaco |
| Tarjetas blancas | Tarjetas **Warm Dark `#232320`**, borde 1 px `#CBC6BC` al 30 %, texto Stone Light `#D6D1C8` |
| Verde del keyword | **Verde lima `#C6DD2E`** (tu color firma de portadas) |
| Naranja de la mascota | **Se elimina.** Sin mascota: logo MW (blanco con alfa) como firma |
| Notas manuscritas rojas | Anotaciones en **Geist Mono 700**, tracking 0.18em, oro `#C9A84C` |
| Sellos verdes inclinados | Etiquetas Geist Mono con borde 2 px (oro/teal/púrpura/terracota según el dato), sin rotación |
| Plus Jakarta Sans | **Geist 600**, tracking -0.03em |
| Mono genérico | **Geist Mono 700**, tracking 0.18em |

Color de cada dato (taxonomía de marca, no decoración): **oro** importes y valor · **teal** porcentajes y datos técnicos · **púrpura** geopolítica y macro · **terracota** costes, impuestos, pérdidas.

Reglas que se mantienen: sin neón, sin glow, sin degradados; tarjetas opacas; subtítulos blanco con sombra suave, palabra clave en lima; máster 9:16 y el 16:9 sale del mismo timeline; nada de repetir en pantalla lo que dice la voz (el texto añade); toda cifra verificada.

## 3. Qué copio de cada referencia (y de dónde sale cada capa)

| Capa | Copiado de | Herramienta |
|---|---|---|
| Subtítulos palabra a palabra, 2–3 palabras, keyword en color | los 4 | HyperFrames + Whisper (pista editable) |
| Panel superior que entra/sale, checklists que se activan una a una | V1, V2 | HyperFrames |
| Títulos grandes "#1 / #2 / #3", "Bonus", fecha del evento | V4 | HyperFrames |
| Tarjetas de precio / comparativa de planes | V2 | HyperFrames |
| Capturas de pantalla con zoom lento | V2, V4 | HyperFrames |
| Calendario semanal que se llena, anillos de puntaje, contadores | V1 | HyperFrames |
| **Mapas animados** (geopolítica, rutas, bloqueos) | tu pedido nuevo | **Electric Eye** (MCP) |
| **Gráficas de precios animadas** (acciones, commodities, BTC) | tu pedido nuevo | **Ride the Lightning** (MCP / CLI) |
| B-roll de apoyo | V3 | tus grabaciones o generado, nunca de terceros |

Cómo se acoplan: Electric Eye y Ride the Lightning ya exportan **MP4 + ProRes 4444 con alfa**. Esos clips entran como capas en HyperFrames (o directo en Premiere) en la caja que el guion de capas les asigne (panel superior 0–50 % de altura, o pantalla completa).

## 4. Fases

**Fase 0 — Kit de marca como código (hoy).** Tokens JSON + CSS con la tabla de arriba, Geist/Geist Mono incrustadas (los TTF están en `C:\Users\tante\Downloads\NUEVA IMAGEN MW-20260727T163921Z-1-001\NUEVA IMAGEN MW\TIPOGRAFIAS\`), logos con alfa. Biblioteca de componentes HyperFrames: subtítulo, panel, tarjeta, checklist, contador, título grande, etiqueta. Dry-run local con clips sintéticos y `hyperframes check`.

**Fase 1 — Primer video real (el que tú pases).** Con la persona ya grabada: transcripción, guion de capas, 2 infografías, 1 mapa, 1 gráfica de precio, subtítulos. Meta: **ver algo juzgable en minutos**, perfección después. Entrega los 3 formatos.

**Fase 2 — Recetas.** Cada estilo que apruebes se guarda como receta reusable (como las de macrowise-studio): "pasos con panel", "comparativa de planes", "3 códigos", "caso con mapa", "evolución de precio". Meta: **menos de 30 min por video**.

**Fase 3 — Dashboard local.** Un icono en el escritorio que reúne todo el flujo de la sección 1. Se construye después del primer video aprobado, no antes.

**Fase 4 — Opcional.** Datos vivos (Ride the Lightning ya tiene actualizador 24/7), versión 16:9 automática, publicación.

## 4b. Cosas que necesito de ti (solo lo que no puedo inventar)

- El **video de la persona** y, si quieres, su foto. Con eso arranca la Fase 1.
- El **tema y las cifras** que quieras rotular. Las verifico contra fuente oficial antes de ponerlas.
- Confirmar que **el verde lima `#C6DD2E` es la palabra clave de los subtítulos** (lo decidí yo por tu regla de portadas).

## 5. Límites y riesgos honestos

- **Licencias de datos:** Coin Metrics (CC BY-NC) y Yahoo (uso personal) no son aptos para contenido monetizado; para gráficas de marca usar FRED, Banco Mundial, NBP, GUS. Ride the Lightning lo avisa al compilar.
- **Stooq** bloquea descargas automáticas; GPW no tiene API estable.
- **Mapas históricos:** Electric Eye debe estar abierto en el navegador (`npm run iniciar`) para que el MCP responda.
- **Tiempos de las referencias:** muestreados cada 3 s, ±1,5 s.
- **Fuentes del original** (Plus Jakarta Sans, Caveat…) no se usan: son de aztec.lab, no de MacroWise.
- **Lo copiado es mecánica, no marca:** estructura, ritmo y animaciones. La mascota, el estilo manuscrito y los textos de aztec.lab no se reproducen.
- **Carpeta de marca en D:\Material de edición** no respondió a tiempo al leerla (error de lectura); usé la copia de Descargas. Conviene revisar ese disco.
- **Ruta de proyecto:** cada video irá en `D:\Material de edición\Edición por meses\<Mes>\<Mes Día>\<PROYECTO>\` con 00_DOCS … 06_EXPORT; `01_RAW` no se toca.
