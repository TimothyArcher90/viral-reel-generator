# PROMPTS EXACTOS — Reels estilo aztec.lab (HyperFrames)

Fuente analizada: los 4 videos de Descargas (720x1280, 30 fps, h264). Tiempos leídos de hojas de contacto cada 3 s: **±1,5 s**. Colores **medidos por píxel** donde se indica "medido"; el resto es "estimado".
Los textos salen de lo que se lee en pantalla (la transcripción de audio no terminó de correr).

| # | Archivo | Duración | Qué es |
|---|---------|----------|--------|
| V1 | Comenta Claude… | 137,0 s | Presentador + panel crema superior con demos de la skill de Instagram |
| V2 | Comenta Link… | 111,2 s | Presentador + tarjetas de pasos y planes de Google AI |
| V3 | Comente cajita… | 171,1 s | Presentador + B-roll de casa/WhatsApp/web + rótulos grandes |
| V4 | Comenta "Triplica"… | 115,3 s | Presentador + títulos grandes + capturas de la app de Claude |

---

## 0. SISTEMA COMÚN (pégalo siempre antes de cualquier prompt)

```
Usa HyperFrames (skill hyperframes + hyperframes-core + hyperframes-animation). Remotion solo si algo no se puede en HyperFrames.
Lienzo 1080x1920, 30 fps, 9:16. Las medidas de abajo están en px sobre 1080 de ancho.

CAPA BASE (nunca se toca): el video del presentador, <video> a pantalla completa, object-fit cover, sin filtros ni escalado extra. Es el 100% del plano; todo lo demás se superpone.

SUBTÍTULOS (pista editable aparte, NUNCA quemados):
- Palabra a palabra, grupos de 2 a 3 palabras, minúsculas.
- Fuente Plus Jakarta Sans, peso 800, ~64 px, interlineado 1.05, centrado.
- Color base #FFFFFF. UNA palabra clave por grupo en verde menta ≈ #A8E6A0 (estimado), en cursiva (skewX -8°).
- Sombra: 0 2px 10px rgba(0,0,0,.45). Sin caja de fondo.
- Entrada por grupo: scale .92→1 + opacity 0→1 en 0,08 s, sin salida (corte seco al siguiente grupo).
- Posición vertical: centro en y = 77 % de la altura (≈ y 1480) por defecto.
  En V1 va justo debajo del panel superior (y ≈ 54 %).
- Máx. 2 líneas, ancho máx. 86 % del lienzo, margen seguro de 60 px a cada lado y zona segura de UI de Reels (no pisar los 250 px inferiores ni los 180 px superiores con texto crítico, salvo los títulos grandes que van arriba).

TARJETAS / PANELES (siempre OPACOS, nunca semitransparentes):
- Panel superior: ancho completo, alto 42–50 % del lienzo, esquinas inferiores 0 (se pega al borde superior). Fondo crema.
- Tarjetas internas blancas #FFFFFF, radio 24 px, sombra 0 8px 24px rgba(0,0,0,.10), padding 36 px.
- Entrada de panel: translateY(-100%)→0 en 0,35 s con ease back.out(1.4). Salida: fade+translateY(-20px) en 0,25 s.
- Entrada de filas/checklist: stagger 0,18 s, cada fila opacity .35→1 y la fila "activa" pasa a fondo blanco con check verde.

PALETA (medida):
- Crema V1 #F1ECE7 con rejilla de 1 px cada 24 px en #E9E3DC.
- Crema rosado V2 #FBEEEA.
- Naranja mascota #D97656 (medido).
- Verde UI #6DDB62 (medido), texto sobre verde #14351B.
- Rojo manuscrito ≈ #C8452E (estimado).
- Amarillo etiqueta ≈ #F2C94C (estimado).
- Negro de texto #111111; gris secundario #6B6B6B.

TIPOGRAFÍA: títulos y UI Plus Jakarta Sans 800 con tracking -0.03em; texto de apoyo Inter 500; mono (etiquetas, sellos) JetBrains Mono 700 en MAYÚSCULAS con tracking +0.12em; manuscrito Caveat 700 rotado -3° para notas rojas.

SELLOS ("GRATIS", "FORMATO PROBADO", "PARRILLA COMPLETA", "SEMANA ENTERA", "DESPUÉS"): JetBrains Mono, borde 3 px verde #3FA35B, fondo verde 12 %, rotación -4°, radio 6 px, entran con scale 1.4→1 y rebote en 0,2 s.

TÍTULOS GRANDES SOBRE EL PRESENTADOR (V3 y V4):
- Línea pequeña: Plus Jakarta Sans 300, blanco, ~110 px. Línea clave: peso 800, ~150 px, verde ≈ #8FE58A. Centrados, y entre 8 % y 24 % de la altura. Sombra 0 6px 24px rgba(0,0,0,.5).
- Entrada: palabras con y +30→0 y opacity 0→1, stagger 0,06 s.

CIFRAS: toda cifra rotulada es una afirmación de marca. Antes de renderizar, lista cada cifra y márcala "VERIFICAR". No inventes ni omitas ninguna.

ENTREGABLES: (1) overlays en ProRes 4444 con canal alfa para Premiere; (2) subtítulos como .srt con tiempos por palabra; (3) MP4 de referencia con todo compuesto, libx264 -crf 17 -preset slow -pix_fmt yuv420p. Antes de renderizar corre `npx hyperframes check` y un dry-run local con clips sintéticos.
```

---

## V1 — "Comenta CLAUDE" (137 s) · Skills de Instagram

```
[Pega el SISTEMA COMÚN]

Reel de 137 s. Presentador en cámara, panel crema con rejilla ocupando el 50 % superior (0–960 px) durante TODO el video; el presentador visible en la mitad inferior; subtítulos justo debajo del panel.

MASCOTA: robot pixel-art de cuerpo naranja #D97656, ojos "> <" en negro, 3 patitas. Es el hilo conductor: camina, se conecta con cables negros, señala.

LÍNEA DE TIEMPO (±1,5 s):
00–03  Logo de Instagram (cuadrado redondeado con degradado) rebotando; la mascota entra caminando desde la izquierda con una varita blanca. Sombra elíptica gris bajo el logo.
03–06  La mascota se conecta con un cable negro curvo a un teléfono (marco negro 8 px, radio 40 px) que muestra el perfil "aztec.lab · IA y Automatización · 118 publicaciones · 0 seguidores · 19 seguidos" y una rejilla 3x3 vacía.
06–09  Sello inclinado "+40.000 EN 3 MESES" (verde) y el contador de seguidores sube de 0 a 41,3 mil (cuenta animada, 1,5 s, ease out). [CIFRA: VERIFICAR]
09–12  Aparece "13 SKILLS" (título 800, negro) y debajo una rejilla de mini-tarjetas con la mascota de colores distintos y nombres: ig-reel, ig-viral, ig-caption, ig-carousel, ig-story, ig-profile, ig-human, ig-comment, ig-reply, ig-dm, ig-repurpose, ig-audit, ig-plan (entran en cascada 0,08 s). Nota manuscrita roja: "¡nos encantaron!".
15–18  Tarjeta blanca "LA SKILL": etiqueta amarilla "LA SKILL" en mono; icono negro con la mascota + mini logo IG; "instagram-agent-skill" con cursor parpadeante; "de Jake Schincariol · GitHub"; "13 skills de Claude que te ayudan a manejar tu Instagram."; píldoras mono "13 skills", "Claude Code", "Instagram". Sello verde "GRATIS" sobre la esquina.
18–21  Mensaje directo: burbuja "aztec.lab · ¡Hola! Aquí está el link 👇" + enlace azul "github.com/…/instagram-agent-skill". Debajo, cuadro de comentario con la palabra "CLAUDE" escribiéndose + botón azul "Publicar". Nota roja: "comenta la palabra…".
21–27  Tarjeta "Guía de instalación" (etiqueta "AZTEC LAB · PDF") con checklist: "1. Abre Claude Code", "2. Pega el link del skill", "3. Prueba un comando /ig-…". Nota roja: "te llega por DM al comentar".
27–36  Ventana de chat de Claude ("¿En qué te ayudo hoy?", caja "Escribe un mensaje…"); flecha roja "aquí ↓"; el usuario escribe "/" y se despliega la lista /ig-viral, /ig-audit, /ig-plan, /ig-comment, /ig-reply, /ig-repurpose.
36–42  Vuelve "13 SKILLS" con 6 destacadas con borde rojo; nota "lista completa → en la guía".
42–60  /ig-viral: píldora "/ig-viral skill" arriba; mosaico de miniaturas de reels con vistas (4.659 · 14,4 mil · 30,5 mil), una con "PARTE 2"; luego miniatura + tarjeta "IDEA · PARA AZTEC.LAB — Mismo formato, tu historia" con chips "+ tu experiencia", "+ tu opinión"; sello "FORMATO PROBADO".
60–75  /ig-audit: perfil aztec.lab, línea de escaneo roja barriendo; anillo de puntaje 58 (rojo) → 91 (verde) con checklist "Bio: promesa más clara / Destacadas: falta la guía / 3 reels fijados con CTA"; sello "DESPUÉS".
75–90  /ig-plan: calendario LUN–DOM que se llena con bloques de colores REEL (naranja), STORY (rosa), CAROUSEL (azul), LIVE (morado) con check; sellos "PARRILLA COMPLETA" y "PROGRAMADO ✓". Nota roja "los más tiempo nos ahorra".
90–102 /ig-comment: reproductor de video + lista de comentarios, respuesta redactada resaltada en amarillo suave.
102–114 /ig-reply: "Comentarios en tu reel" con 4 comentarios clasificados con etiquetas PREGUNTA, PALABRA CLAVE, BOTS; respuesta a @andres.pyme.
114–126 /ig-repurpose: miniatura de YouTube "COLD EMAIL · CURSO COMPLETO · 2:36:13" con una tijera cortándola en fragmentos naranjas; los fragmentos caen en una semana LUN–DOM de reels grises; sello "SEMANA ENTERA" y cinta amarilla "9:16 · LISTOS PARA INSTAGRAM".
126–137 CIERRE: tarjeta "Comenta [CLAUDE] y te llega:" (CLAUDE en píldora naranja #D97656 con texto blanco) con 3 checks que aparecen uno a uno: "El link del skill", "La guía para instalarlo", "La lista de todos los comandos"; nota "todo por DM". Después tarjeta con "① Síguenos @aztec.lab [Siguiendo]" y "② Comenta [CLAUDE]" con el campo escribiéndose; nota "+ la guía completa por DM". Los últimos 3 s, solo el presentador, sin panel.

Subtítulos: palabra clave en verde cursiva, justo debajo del panel.
```

---

## V2 — "Comenta Link" (111 s) · Gemini gratis para estudiantes

```
[Pega el SISTEMA COMÚN]

Reel de 111 s. Presentador con portátil, plano completo. Tarjetas ARRIBA (alto 20–42 % según la tarjeta), subtítulos en el tercio inferior (y 77 %).

00–03  Insignia blanca redondeada con la estrella de Gemini (✦ degradado azul/rojo/amarillo) y "Gemini" en 800, centrada sobre el portátil, scale .8→1.
09–12  Tarjeta crema rosado #FBEEEA: píldora verde #6DDB62 "PASO 1" (mono, texto #14351B) + título "Pide el link en los comentarios" (800, -0.04em, #14351B) + campo de comentario simulado (avatar verde, "Agrega un comentario…", "Publicar" azul claro).
12–15  Tarjeta oscura #1A1A1A: icono incógnito + "PASO 2" (píldora verde) + "Ábrelo en incógnito" con "incógnito" en verde.
15–21  Capturas de pantalla (Chrome, Google One "personal account", "Accede a tu cuenta") a ancho completo arriba, con zoom lento (scale 1→1.06). Píldora oscura "Paso 2 · Modo incógnito" y píldora roja claro "Cuenta corporativa abierta = ✗ no te deja" (texto rojo oscuro sobre #FCE4DC).
21–36  TARJETA PLAN 1: eyebrow mono "PLAN 1 · GRATIS"; "✦ Google AI Plus" (800) a la izquierda; a la derecha precio tachado gris "19.900 COP" y arriba píldora verde "0 COP" (50 px, 800) con "durante 12 meses" debajo. Lista de 5 filas, TODAS en gris al 35 % al inicio y activándose de una en una (blanco + check verde) sincronizadas con la voz: "2x límites de uso en Gemini", "Modelo Flash Thinking", "400 GB de almacenamiento", "Gemini en Gmail", "Gemini Notebook" (con micro-etiqueta "antes NotebookLM"). Al final, píldora oscura "Para ser gratis, ¡muy bien!".
45–66  TARJETA PLAN 2: eyebrow "PLAN 2 · 20 MIL"; "✦ Google AI Pro"; precio "79.000 COP" tachado → píldora "20.000" (verde, "COP/mes · ≈ US$6–7") con sello "-74 %" en rojo; píldora oscura "EL QUE RECOMIENDO". Filas: "Antigravity — Agente de IA para programar (Como Claude Code o Codex)", "YouTube Premium", "5 TB de almacenamiento" (fila final con píldora verde "= Infinito"), "+ Todo lo del plan gratis". [CIFRAS 19.900 / 79.000 / 20.000 / -74 % / US$6–7: VERIFICAR contra Google One Colombia]
66–90  Capturas de la página de oferta para estudiantes de Google One (planes "0 COP durante 12 meses" y "20.000 COP"), formulario de datos y pantalla "Sube tu comprobante de inscripción": a ancho completo arriba, desplazamiento vertical suave.
90–105 Solo presentador.
105–111 Cierre: "Comenta" (300, blanco, 70 px) + "Link" (800, verde, ~190 px, entre comillas) centrados al 60 % de altura; luego "o aún" en subtítulo.

Pasos 1 y 2 se presentan en ese orden; cada tarjeta dura mientras el presentador la nombra y sale con fade.
```

---

## V3 — "Comente Cajita" (171 s) · Caso real, B-roll y prueba social

```
[Pega el SISTEMA COMÚN]

Reel de 171 s. Presentador (camiseta azul marino, luego gris) alternado con B-roll vertical en pantalla completa. Subtítulos más pequeños (≈ 48 px), blancos, con palabras clave en verde, y y = 77 %.

00–03  Insignia arriba a la izquierda: rectángulo verde oscuro #0F3D1F, borde verde #6DDB62 3 px, radio 14 px, rotación -3°, texto "CAJITA MÁGICA" (mono pequeño) + "PARTE 2" (800, 64 px) blanco/verde.
03–12  Corte a B-roll doméstico (niña en rosa jugando junto a una repisa), sin presentador; subtítulos de la voz. Título grande "Sin necesidad de / Una pantalla" (línea 1 ligera blanca, línea 2 800 verde) a media altura.
12–21  Captura de WhatsApp oscuro: chat "Olivia y los abuelos" con notas de voz transcritas; subtítulo "haciendo la hermana" etc.
21–39  B-roll de niños usando la cajita (roja tipo camión de bomberos; luego versión turquesa junto a una ventana); reencuadre 9:16 con caras difuminadas.
39–51  Captura de Instagram Insights: Reel con 1.494.903 vistas; 137K me gusta, 26,9K comentarios, 6,4K compartidos; luego sección de comentarios (aztec.lab responde "Enviado!"). [CIFRAS: VERIFICAR contra Insights real]
51–57  Presentador (camiseta azul) 4 s.
57–90  B-roll de construcción: pantalla de videollamada, manos con placa, impresión 3D, caja de madera. Subtítulos "la montamos en… probando vamos…".
90–120 Impresora 3D trabajando, luego captura de la web: "Una voz familiar. Dos botones para compartirla." (crema, titular azul/rojo) y animación "Pruébala. Tu voz va y vuelve." con teléfono mostrando WhatsApp.
120–150 Presentador (camiseta gris). Rótulo "ChatGPT se encargó de:" (línea pequeña blanca ligera, ~44 px) + línea clave verde 800 (~110 px) que cambia: "Hacer la impresión 3D" → "Monto la página web" → "Pidió los materiales". Entrada y salida por palabras, 0,25 s.
150–171 CIERRE: "Comente" (300 blanco) + "“Cajita”" (800 verde, ~190 px) centrado a 65 %; subtítulos finales "la clase donde enseñamos gratis".

Nota: las caras de menores van siempre difuminadas (bloque gris-pixelado), no es opcional.
```

---

## V4 — "Comenta Triplica" (115 s) · 3 códigos secretos

```
[Pega el SISTEMA COMÚN]

Reel de 115 s. Presentador de pie/sentado con una bola naranja en la mano, plano completo sin panel. Los números y frases entran como títulos grandes en el tercio superior (y 8–24 %). Las capturas de la app de Claude entran como tarjeta blanca centrada (ancho 84 %, radio 28 px, sombra fuerte) sobre el tercio medio, con el presentador asomando por debajo.

00–06  Título: "3 codigos" (300, blanco, ~112 px) + "Secretos" (800, verde #8FE58A, ~150 px), alineado a la izquierda del eje, sombra marcada. Sin subtítulos durante los 3 primeros segundos.
06–12  "#1" (800, verde, ~110 px) centrado + frase en cursiva ligera blanca ~52 px entre comillas: “Despliega subagentes adversariales”, con cursor azul #1E90FF parpadeando (12x90 px) al final de la frase (efecto de escritura).
12–32  Capturas de la app de Claude (cada una 1,6–2,5 s): bienvenida, prompt "Claude, estoy mirando qué precio ponerle a un producto…", panel "Tareas en segundo plano" con 4 subagentes (El Escéptico, Cliente Hostil, El Competidor, El Auditor), respuestas y veredicto. Transiciones: fade 0,2 s.
32–50  "#2" + “Contéstame en inglés/español técnico simplificado” (misma tipografía que #1). Capturas de resultados.
50–66  "#3" + “Por favor hazme todas las preguntas que consideres necesarias para darme la mejor respuesta” (3 líneas, 46 px). Capturas del chat "Comparación de manzanas y peras para la digestión" con preguntas y archivos .pptx/.pdf generados. Subtítulo "un prompt" cuando se menciona.
66–84  "Bonus" (800, verde, ~130 px) arriba; luego "Para transformar / Su carrera" (línea pequeña blanca + línea verde 800).
84–95  "Comenten" (300, blanco, ~80 px) + "Triplica" (800, verde, ~190 px) + "y les envío el link…" (300, blanco, ~44 px), centrado a y 60 %.
95–115 BLOQUE DE FECHA, fijo arriba hasta el final: "Lunes" (800, blanco, 80 px) / "31 de" (blanco 800) + "Agosto" (verde 800), ambos ~130 px / bandera de Colombia circular 64 px + "7:30pm" (300, 80 px) / a la derecha, alineado a la derecha, "Completamente" (300, 36 px) + "¡Gratis!" (800, verde, 64 px). Últimos 4 s: "100% ¡Gratis!" grande (800, verde, ~170 px) centrado a 70 %. [FECHA Y HORA: VERIFICAR; hoy es 3/11/2026, el reel dice 31 de agosto]

Subtítulos estándar (y 77 %) todo el tiempo, excepto mientras haya tarjeta de Claude centrada (se suben a y 88 % o se ocultan).
```

---

## ALERTAS (decisiones mías que deberías revisar)

- Fuentes: Plus Jakarta Sans, Inter, JetBrains Mono y Caveat son mi identificación visual, **no confirmada**. Si tienes el manual de marca de aztec.lab, sustitúyelas.
- Cifras que aparecen en pantalla y **no pude verificar**: +40.000 seguidores / 41,3 mil / 16,9 mil, precios de Google (19.900 / 79.000 / 20.000 COP, −74 %, US$6–7), 1.494.903 vistas, fecha "31 de agosto" (el reel ya está desactualizado: hoy es 3-nov-2026).
- V3 usa material de terceros (llamada de Zoom, clips de familias): para recrearlo necesitas tus propias grabaciones.
- Fuera de alcance: transcripción de audio (whisper no alcanzó a terminar) y tiempos al segundo exacto (muestreo cada 3 s).
