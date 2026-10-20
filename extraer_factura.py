"""Sección 9 · Lección 43. Content Understanding: extraer y validar los campos de una factura.

La estructura exacta de los campos depende del analyzer y de la versión de la API.
Si un nombre de campo no coincide, revisa la pestaña Result del playground.
"""
import os
from collections import Counter
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput

load_dotenv()


def analizar(url: str, analyzer_id: str = "prebuilt-invoice") -> dict:
    client = ContentUnderstandingClient(
        endpoint=os.environ["CU_ENDPOINT"],
        credential=DefaultAzureCredential(), api_version="2025-11-01")
    poller = client.begin_analyze(analyzer_id=analyzer_id, inputs=[AnalysisInput(url=url)])
    return poller.result().as_dict()


def _valor(campo: dict):
    for k, v in campo.items():
        if k.startswith("value"):
            if isinstance(v, dict) and "amount" in v:   # valueCurrency
                return v["amount"]
            return v
    return None


def extraer_y_validar(url: str, umbral: float = 0.8) -> str:
    campos = analizar(url)["contents"][0].get("fields", {})
    lineas, avisos, conceptos, importes = [], [], [], []
    for nombre, campo in campos.items():
        valor, conf = _valor(campo), campo.get("confidence")
        if isinstance(valor, list):                      # conceptos de la factura
            for item in valor:
                obj = item.get("valueObject", {}) if isinstance(item, dict) else {}
                desc = next((_valor(c) for k, c in obj.items() if "desc" in k.lower()), None)
                monto = next((_valor(c) for k, c in obj.items() if "amount" in k.lower()), None)
                if desc:
                    conceptos.append(desc)
                if isinstance(monto, (int, float)):
                    importes.append(monto)
            continue
        lineas.append(f"{nombre}: {valor} (confidence {conf})")
        if conf is not None and conf < umbral:
            avisos.append(f"{nombre} con confidence {conf:.2f}: revisión humana")
    total = next((_valor(c) for n, c in campos.items()
                  if "total" in n.lower() or "amountdue" in n.lower()), None)
    if importes and isinstance(total, (int, float)) and abs(sum(importes) - total) > 0.01:
        avisos.append(f"La suma de conceptos ({sum(importes)}) no coincide con el total ({total})")
    duplicados = [c for c, n in Counter(conceptos).items() if n > 1]
    if duplicados:
        avisos.append(f"Posible cobro duplicado: {', '.join(map(str, duplicados))}")
    return "\n".join(lineas + ["AVISOS:"] + (avisos or ["ninguno"]))


if __name__ == "__main__":
    print(extraer_y_validar(os.environ["FACTURA_URL"]))
