"""Sección 8 · Lección 37. Aplicación ligera con capacidades de visión."""
import base64
import mimetypes
import os
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
DATA = Path(__file__).resolve().parent / "data"
_project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential())
_client = _project.get_openai_client()

INSTRUCCIONES = ("Eres un técnico de soporte de Luma. Describe solo lo que ves en la imagen. "
                 "Si la imagen no es clara, dilo y pide otra foto. Dame la respuesta en JSON con tres campos: equipo, luces y accion_sugerida")


def diagnosticar_foto(ruta_imagen: str | Path,
                      pregunta: str = "¿Qué indican las luces del router?") -> str:
    tipo = mimetypes.guess_type(str(ruta_imagen))[0] or "image/jpeg"
    with open(ruta_imagen, "rb") as f:
        imagen = base64.b64encode(f.read()).decode("utf-8")
    contenido = [
        {"type": "input_text", "text": pregunta},
        {"type": "input_image", "image_url": f"data:{tipo};base64,{imagen}"}]
    response = _client.responses.create(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        instructions=INSTRUCCIONES,
        input=[{"role": "user", "content": contenido}])
    return response.output_text


if __name__ == "__main__":
    print(diagnosticar_foto(DATA / "router_cliente.jpg"))
