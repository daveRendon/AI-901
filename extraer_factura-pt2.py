
import os
import re
from pathlib import Path
from collections import defaultdict
from decimal import Decimal

from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import (
    AnalysisInput,
    ArrayField,
    ObjectField,
)

load_dotenv()

ENDPOINT = os.environ["CU_ENDPOINT"]
ARCHIVO = os.environ["FACTURA_URL"]
ANALYZER = os.getenv("ANALYZER_ID", "prebuilt-invoice")


def valor(campos, nombre):
    campo = campos.get(nombre)
    return campo.value if campo is not None else None


def importe(campos, nombre):
    campo = campos.get(nombre)
    if campo is None:
        return None

    dato = campo.value
    if isinstance(dato, dict):
        interno = dato.get("Amount")
        dato = interno.value if interno is not None else None

    return Decimal(str(dato)) if dato is not None else None


def mostrar(nombre, campo, nivel=0):
    prefijo = " " * nivel
    confianza = getattr(campo, "confidence", None)
    score = (
        f"{confianza:.2f}"
        if confianza is not None else "N/D"
    )

    if isinstance(campo, ObjectField):
        print(f"{prefijo}{nombre}:")
        for clave, hijo in (campo.value or {}).items():
            mostrar(clave, hijo, nivel + 2)

    elif isinstance(campo, ArrayField):
        print(f"{prefijo}{nombre}:")
        for indice, hijo in enumerate(campo.value or [], 1):
            mostrar(f"Concepto {indice}", hijo, nivel + 2)

    else:
        print(f"{prefijo}{nombre}: {campo.value}")
        print(f"{prefijo}  Confidence: {score}")


def validar_factura(campos):
    print("\n===== VALIDACION DE IMPORTES =====")

    lista = campos.get("LineItems")
    if not isinstance(lista, ArrayField) or not lista.value:
        print("No se encontraron conceptos para validar.")
        return

    conceptos = []
    for item in lista.value:
        if isinstance(item, ObjectField):
            conceptos.append(item.value or {})

    montos = [importe(c, "TotalAmount") for c in conceptos]

    if not montos or any(m is None for m in montos):
        print("AVISO: Faltan importes de conceptos.")
    else:
        suma = sum(montos, Decimal("0"))
        subtotal = importe(campos, "SubtotalAmount")
        total = importe(campos, "TotalAmount")

        # Preferimos subtotal porque total puede incluir impuestos.
        if subtotal is not None:
            esperado = subtotal
            etiqueta = "subtotal"
            calculado = suma
        else:
            esperado = total
            etiqueta = "total"
            calculado = (
                suma
                + (importe(campos, "TotalTaxAmount") or Decimal("0"))
                - (importe(campos, "TotalDiscountAmount") or Decimal("0"))
            )

        print(f"Suma calculada: {calculado:.2f}")

        if esperado is None:
            print("AVISO: No se pudo extraer un total comparable.")
        else:
            print(f"{etiqueta.capitalize()} factura: {esperado:.2f}")
            if abs(calculado - esperado) <= Decimal("0.01"):
                print("OK: Los importes coinciden.")
            else:
                print("AVISO: Existe una diferencia. Revisar factura.")

    print("\n===== DETECCION DE DUPLICADOS =====")

    grupos = defaultdict(list)

    for numero, concepto in enumerate(conceptos, 1):
        descripcion = str(valor(concepto, "Description") or "")
        descripcion = " ".join(descripcion.casefold().split())

        fecha = valor(concepto, "Date")
        periodo = str(fecha)[:7] if fecha else None

        if periodo is None:
            meses = re.search(
                r"\b(enero|febrero|marzo|abril|mayo|junio|"
                r"julio|agosto|septiembre|octubre|"
                r"noviembre|diciembre)\b",
                descripcion,
            )
            periodo = meses.group(0) if meses else None

        if descripcion:
            grupos[(descripcion, periodo)].append(numero)

    encontrados = False

    for (descripcion, periodo), numeros in grupos.items():
        if len(numeros) > 1:
            encontrados = True
            print(f"POSIBLE DUPLICADO: {descripcion}")
            print(f"Conceptos: {numeros}")
            print(f"Periodo: {periodo or 'no identificado'}")
            print("Requiere revision por facturacion.")

    if not encontrados:
        print("No se detectaron descripciones duplicadas.")


def main():
    credencial = DefaultAzureCredential()
    cliente = ContentUnderstandingClient(
        endpoint=ENDPOINT,
        credential=credencial,
    )

    try:
        print(f"Analizando con: {ANALYZER}")

        if ARCHIVO.startswith(("https://", "http://")):
            poller = cliente.begin_analyze(
                analyzer_id=ANALYZER,
                inputs=[AnalysisInput(url=ARCHIVO)],
            )
        else:
            ruta = Path(ARCHIVO)
            if not ruta.is_absolute():
                ruta = Path(__file__).resolve().parent / ruta

            poller = cliente.begin_analyze_binary(
                analyzer_id=ANALYZER,
                binary_input=ruta.read_bytes(),
            )

        resultado = poller.result()

        if not resultado.contents:
            print("No se devolvio contenido.")
            return

        campos = resultado.contents[0].fields or {}

        print("\n===== CAMPOS EXTRAIDOS =====")
        for nombre, campo in campos.items():
            mostrar(nombre, campo)

        if ANALYZER == "prebuilt-invoice":
            validar_factura(campos)

    finally:
        cliente.close()
        credencial.close()


if __name__ == "__main__":
    main()
