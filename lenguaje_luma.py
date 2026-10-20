
"""Sección 6 · Lección 28. Azure AI Language: análisis de texto."""

import os
from pathlib import Path

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import AzureError
from azure.ai.textanalytics import TextAnalyticsClient


# 1. Configuración
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

endpoint = os.environ["LANGUAGE_ENDPOINT"].strip()
key = os.environ["LANGUAGE_KEY"].strip()

client = TextAnalyticsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# 2. Texto de prueba
texto = (
    "Mi nombre es José Pérez y mi correo es "
    "jperez@azinsiders.net. Vivo en Ciudad de México. "
    "Contraté el servicio de internet residencial de Luma "
    "hace tres meses. Durante las últimas dos semanas, "
    "mi router ha presentado desconexiones frecuentes "
    "y velocidades muy bajas. "
    "Ayer llamé al soporte técnico de Luma, pero no "
    "lograron resolver mi problema. "
    "Estoy muy frustrado con la calidad del servicio. "
    "Necesito una solución urgente porque trabajo "
    "desde casa y dependo de una conexión estable."
)

docs = [texto]


def obtener_resultado(operacion, **kwargs):
    """Ejecuta una operación y valida el primer documento."""
    respuesta = operacion(docs, **kwargs)
    resultado = respuesta[0]

    if resultado.is_error:
        raise RuntimeError(resultado.error.message)

    return resultado


def ejecutar(nombre, funcion):
    """Muestra los resultados o el error de cada análisis."""
    print(f"\n=== {nombre} ===")
    try:
        funcion()
    except (AzureError, RuntimeError, ValueError) as error:
        print("Error:", str(error))


# 3. Detección de idioma
def detectar_idioma():
    resultado = obtener_resultado(client.detect_language)
    idioma = resultado.primary_language

    print("Idioma:", idioma.name)
    print("Código:", idioma.iso6391_name)
    print("Confianza:", round(idioma.confidence_score, 3))


# 4. Extracción de frases clave
def extraer_palabras_clave():
    resultado = obtener_resultado(
        client.extract_key_phrases,
        language="es"
    )

    for frase in resultado.key_phrases:
        print("-", frase)


# 5. Reconocimiento de entidades
def reconocer_entidades():
    resultado = obtener_resultado(
        client.recognize_entities,
        language="es"
    )

    for entidad in resultado.entities:
        print(
            f"- {entidad.text} | "
            f"Categoría: {entidad.category} | "
            f"Confianza: {entidad.confidence_score:.2f}"
        )


# 6. Análisis de sentimiento
def analizar_sentimiento():
    resultado = obtener_resultado(
        client.analyze_sentiment,
        language="es"
    )

    print("Sentimiento:", resultado.sentiment)
    print(
        "Positivo:",
        round(resultado.confidence_scores.positive, 3)
    )
    print(
        "Neutral:",
        round(resultado.confidence_scores.neutral, 3)
    )
    print(
        "Negativo:",
        round(resultado.confidence_scores.negative, 3)
    )

    print("\nSentimiento por oración:")

    for oracion in resultado.sentences:
        print(
            f"- {oracion.sentiment}: "
            f"{oracion.text.strip()}"
        )


# 7. Detección de información personal
def detectar_pii():
    resultado = obtener_resultado(
        client.recognize_pii_entities,
        language="es"
    )

    print("Texto anonimizado:")
    print(resultado.redacted_text)

    print("\nEntidades sensibles:")

    for entidad in resultado.entities:
        print(
            f"- {entidad.text} | "
            f"Categoría: {entidad.category}"
        )


# 8. Resumen extractivo
def generar_resumen():
    poller = client.begin_extract_summary(
        docs,
        language="es",
        max_sentence_count=3,
        order_by="Offset"
    )

    resultados = poller.result()

    for resultado in resultados:
        if resultado.is_error:
            print("Error:", resultado.error.message)
            continue

        for oracion in resultado.sentences:
            print("-", oracion.text)


# 9. Ejecutar todos los análisis
try:
    print("AZURE AI LANGUAGE | LUMA SOPORTE")
    print("=" * 50)

    ejecutar("DETECCIÓN DE IDIOMA", detectar_idioma)
    ejecutar("PALABRAS CLAVE", extraer_palabras_clave)
    ejecutar("ENTIDADES RECONOCIDAS", reconocer_entidades)
    ejecutar("ANÁLISIS DE SENTIMIENTO", analizar_sentimiento)
    ejecutar("DETECCIÓN DE PII", detectar_pii)
    ejecutar("RESUMEN EXTRACTIVO", generar_resumen)

finally:
    client.close()
