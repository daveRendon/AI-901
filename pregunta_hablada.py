
import os
import base64
from pathlib import Path

from dotenv import load_dotenv
from azure.identity import (
    DefaultAzureCredential,
    get_bearer_token_provider
)
from azure.core.exceptions import AzureError
from openai import (
    OpenAI,
    APIConnectionError,
    APIStatusError
)

# 1. Load environment variables
ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env", override=True)

endpoint = os.environ["AZURE_OPENAI_V1_ENDPOINT"].strip()
deployment = os.getenv(
    "AUDIO_DEPLOYMENT_NAME",
    "gpt-audio-mini"
)

# 2. Microsoft Entra ID authentication
credential = DefaultAzureCredential()

token_provider = get_bearer_token_provider(
    credential,
    "https://ai.azure.com/.default"
)

# 3. Azure OpenAI v1 client
client = OpenAI(
    base_url=endpoint,
    api_key=token_provider,
    timeout=60.0,
    max_retries=0
)

# 4. Load WAV file
audio_file = ROOT / "data" / "pregunta_molesta.wav"

if not audio_file.exists():
    raise FileNotFoundError(
        f"No se encontró el archivo: {audio_file}"
    )

audio = base64.b64encode(
    audio_file.read_bytes()
).decode("utf-8")

# 5. Prepare audio input
contenido = [
    {
        "type": "text",
        "text": "Escucha la pregunta y responde en español."
    },
    {
        "type": "input_audio",
        "input_audio": {
            "data": audio,
            "format": "wav"
        }
    }
]

# 6. Authenticate and send request
try:
    print("Autenticando con Microsoft Entra ID...")

    # Validate authentication before API request
    token_provider()
    print("Autenticación Entra ID correcta.")

    print("Endpoint:", endpoint)
    print("Deployment:", deployment)
    print("Procesando audio...")

    completion = client.chat.completions.create(
        model=deployment,
        modalities=["text"],
        messages=[
            {
                "role": "user",
                "content": contenido
            }
        ]
    )

    print("\nRespuesta:")
    print(completion.choices[0].message.content)

except AzureError as e:
    print("Error de autenticación Azure:")
    print(type(e).__name__, str(e))

except APIConnectionError as e:
    print("Error de conexión:")
    print(str(e))
    cause = e.__cause__
    while cause:
        print("Causa:", repr(cause))
        cause = cause.__cause__

except APIStatusError as e:
    print("Error HTTP:", e.status_code)
    print("Detalle:", str(e))

finally:
    client.close()
    credential.close()
