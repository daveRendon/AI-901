"""Sección 6 · Lección 27. Text analysis con un modelo de propósito general (salida JSON)."""
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential())
client = project.get_openai_client()

instrucciones = """Analiza el ticket. Responde SOLO con JSON, con el resumen en español:
{"keywords": [], "entidades": [{"texto": "", "tipo": ""}],
 "sentimiento": "positive|neutral|negative", "resumen": ""}"""

DATA = Path(__file__).resolve().parent / "data"
ticket = (DATA / "ticket_ingles.txt").read_text(encoding="utf-8")
response = client.responses.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    instructions=instrucciones, input=ticket)
analisis = json.loads(response.output_text)
print(json.dumps(analisis, indent=2, ensure_ascii=False))
