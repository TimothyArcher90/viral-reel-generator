"""Fase 1 · prueba de alfa: crea una capa RGBA (PNG) con tarjeta opaca, texto Geist en lima
y una caja semitransparente; luego ffmpeg la convierte a ProRes 4444 y WebM VP9 con alfa.
Uso: python -I scripts/prueba_alfa.py <carpeta_salida>
"""
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

raiz = Path(__file__).resolve().parent.parent
salida = Path(sys.argv[1])
salida.mkdir(parents=True, exist_ok=True)

fuente = ImageFont.truetype(str(raiz / "brand" / "fonts" / "Geist-VariableFont_wght.ttf"), 150)
try:
    fuente.set_variation_by_axes([600])
except Exception:
    pass

img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
d.rounded_rectangle((90, 200, 990, 460), 24, fill=(0x23, 0x23, 0x20, 255))      # tarjeta opaca
ancho = d.textlength("Secretos", font=fuente)
d.text(((1080 - ancho) / 2, 250), "Secretos", font=fuente, fill=(0xC6, 0xDD, 0x2E, 255))
d.rectangle((90, 1500, 990, 1640), fill=(0xC6, 0xDD, 0x2E, 128))                 # 50 % de alfa
png = salida / "capa.png"
img.save(png)

base = ["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-t", "6", "-i", str(png)]
subprocess.run(base + ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", str(salida / "alfa.mov")], check=True)
subprocess.run(base + ["-c:v", "libvpx-vp9", "-pix_fmt", "yuva420p", "-auto-alt-ref", "0", "-b:v", "2M", str(salida / "alfa.webm")], check=True)

# verificación: decodifica y mide el alfa real
for nombre, extra in (("alfa.mov", []), ("alfa.webm", ["-c:v", "libvpx-vp9"])):
    subprocess.run(["ffmpeg", "-v", "error", "-y"] + extra + ["-i", str(salida / nombre), "-vf", "alphaextract", "-frames:v", "1", "-update", "1", str(salida / f"a_{nombre}.png")], check=True)
    a = Image.open(salida / f"a_{nombre}.png").convert("L")
    print(nombre, "alfa fondo", a.getpixel((10, 10)), "| tarjeta", a.getpixel((120, 230)), "| caja 50%", a.getpixel((120, 1520)))
