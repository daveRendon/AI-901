
"""Sección 4 · Lección 17. Cliente de chat con el Foundry SDK (Entra ID, sin keys)."""

import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()

project = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential()
)

client = project.get_openai_client()
deployment = os.environ["MODEL_DEPLOYMENT_NAME"]

instructions = "Eres el asistente de Luma Soporte. Respondes en español,\n\
con tono cordial y en un máximo de 5 líneas.\n\
Solo hablas de internet residencial y dispositivos Luma.\n\
Si no sabes algo, dilo y ofrece escalar con una persona.\n\
"

previous_id = None

while True:
    pregunta = input("Tú: ").strip()

    if pregunta.lower() == "salir":
        print("Luma: ¡Hasta pronto!")
        break

    if not pregunta:
        continue

    # Parámetros de la solicitud
    params = {
        "model": deployment,
        "instructions": instructions,
        "input": pregunta,
        "store": True
    }

    # Enviar previous_response_id solamente si existe
    if previous_id is not None:
        params["previous_response_id"] = previous_id

    try:
        response = client.responses.create(**params)

        previous_id = response.id

        print("Luma:", response.output_text)

    except Exception as e:
        print(f"Error: {e}")
