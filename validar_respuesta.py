"""Sección 4 · Lección 19. Validar estado y formato de una respuesta antes de usarla."""
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
project = AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
                          credential=DefaultAzureCredential())
client = project.get_openai_client()
deployment = os.environ["MODEL_DEPLOYMENT_NAME"]

instructions = """Clasifica el ticket y responde SOLO con JSON válido, sin texto adicional:
{"categoria": "facturacion | falla_tecnica | cambio_plan | otro", "prioridad": 1,
 "resumen": "máximo 25 palabras", "requiere_humano": false}"""
DATA = Path(__file__).resolve().parent / "data"
ticket = (DATA / "ticket_8413.txt").read_text(encoding="utf-8")

response = client.responses.create(
    model=deployment, instructions=instructions,
    input=ticket, max_output_tokens=2000)

if response.status != "completed":
    print("Incompleta:", response.incomplete_details)
else:
    try:
        datos = json.loads(response.output_text)
        permitidas = {"facturacion", "falla_tecnica", "cambio_plan", "otro"}
        assert datos["categoria"] in permitidas
        print("Clasificación válida:", datos)
    except (json.JSONDecodeError, KeyError, AssertionError):
        print("Formato inválido: enviar a revisión humana")
