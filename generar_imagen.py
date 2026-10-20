"""Sección 8 · Lección 36. Generar una imagen con un modelo de image generation."""

import base64
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Carpeta data dentro del directorio del proyecto
OUTPUT = Path.cwd() / "data"
OUTPUT.mkdir(parents=True, exist_ok=True)

client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_V1_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"]
)

img = client.images.generate(
    model="gpt-image-2",  # Nombre del deployment
    prompt=(
        "Ilustración plana de un router blanco con tres "
        "luces verdes, vista frontal, fondo claro, "
        "sin texto ni logotipos"
    ),
    n=1,
    size="1024x1024"
)

# Guardar imagen en la carpeta data
image_path = OUTPUT / "router_ayuda.png"
image_path.write_bytes(
    base64.b64decode(img.data[0].b64_json)
)

print(f"Imagen guardada en: {image_path}")