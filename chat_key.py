"""Sección 4 · Lección 18. Alternativa con API key y el endpoint compatible con OpenAI."""
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
# Termina en /openai/v1/
client = OpenAI(
    base_url=os.environ["AZURE_OPENAI_V1_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
)
response = client.responses.create(
    model=os.environ.get("MODEL_DEPLOYMENT_NAME", "gpt-5-mini"),
    instructions="Eres el asistente de Luma Soporte.",
    input="¿Cómo reinicio mi router?",
)
print(response.output_text)
