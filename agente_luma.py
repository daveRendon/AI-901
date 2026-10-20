"""Sección 5 · Lección 23. Cliente de Python para luma-soporte-agent.

Para conectarte a un project y a sus agentes necesitas Microsoft Entra ID (az login);
la autenticación con API key no está disponible para AIProjectClient.
"""
import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

load_dotenv()
_project = AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
                           credential=DefaultAzureCredential())
_client = _project.get_openai_client()
AGENTE = {"agent_reference": {"name": os.environ.get("AGENT_NAME", "luma-soporte-agent"),
                              "version": os.environ.get("AGENT_VERSION", "4"),
                              "type": "agent_reference"}}


def preguntar_al_agente(pregunta: str, conversation_id: str | None = None) -> str:
    """Envía una pregunta al agente y devuelve el texto de la respuesta."""
    extra = {"conversation": conversation_id} if conversation_id else {}
    response = _client.responses.create(input=pregunta, extra_body=AGENTE, **extra)
    return response.output_text


if __name__ == "__main__":
    conversation = _client.conversations.create()
    while True:
        pregunta = input("Cliente: ")
        if pregunta.lower() == "salir":
            break
        print("Agente:", preguntar_al_agente(pregunta, conversation.id))
