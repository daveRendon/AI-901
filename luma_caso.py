
"""Orquesta voz_luma.py, vision_luma.py, extraer_factura.py y agente_luma.py.

Ejecutar con python luma_caso.py. Usa los archivos del caso de José en data
y FACTURA_URL del entorno o de .env. voz_luma.py se ejecuta como subproceso;
los demás módulos se llaman mediante sus funciones.
"""

import os
import sys
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from dotenv import load_dotenv

# Directorio principal del proyecto
CODE = Path(__file__).resolve().parent
DATA = CODE / "data"


def transcribir(audio_file: str | Path) -> str:
    """
    Ejecuta voz_luma.py sin modificarlo.
    Captura la transcripción desde la terminal.
    """

    audio_file = Path(audio_file).resolve()

    if not audio_file.is_file():
        raise FileNotFoundError(
            f"No existe el archivo: {audio_file}"
        )

    # Localizar el script de Speech
    opciones = [
        CODE / "voz_luma.py",
        CODE / "07_speech" / "voz_luma.py"
    ]

    script = next(
        (p for p in opciones if p.is_file()),
        None
    )

    if script is None:
        raise FileNotFoundError(
            "No se encontró voz_luma.py"
        )

    # voz_luma.py siempre utiliza mensaje.wav
    audio_destino = script.parent / "data" / "mensaje.wav"
    audio_destino.parent.mkdir(
        parents=True, exist_ok=True
    )

    # Proteger el archivo original, si existe
    reemplazar = audio_file != audio_destino.resolve()

    with tempfile.TemporaryDirectory() as temporal:

        respaldo = Path(temporal) / "mensaje_original.wav"
        existia = audio_destino.exists()

        if reemplazar and existia:
            shutil.copy2(audio_destino, respaldo)

        try:
            if reemplazar:
                shutil.copy2(audio_file, audio_destino)

            print("Transcribiendo mensaje de José...")

            proceso = subprocess.run(
                [sys.executable, str(script)],
                cwd=str(DATA),
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace"
            )

            if proceso.returncode != 0:
                raise RuntimeError(
                    proceso.stderr or proceso.stdout
                )

            print(proceso.stdout)

            # Extraer el texto después de "Cliente dijo:"
            resultado = re.search(
                r"^Cliente dijo:[ \t]*(\S[^\r\n]*)",
                proceso.stdout,
                re.MULTILINE
            )

            if not resultado:
                raise RuntimeError(
                    "No se encontró una transcripción válida."
                )

            return resultado.group(1).strip()

        finally:
            # Restaurar mensaje.wav original
            if reemplazar:
                if existia:
                    shutil.copy2(respaldo, audio_destino)
                else:
                    audio_destino.unlink(missing_ok=True)


def main() -> str:
    """Procesa las cuatro fuentes y devuelve la respuesta del agente LUMA."""
    load_dotenv(CODE / ".env", override=True)
    factura_url = os.environ.get("FACTURA_URL", "").strip()
    if not factura_url:
        raise ValueError("Configura FACTURA_URL en el entorno o en .env.")

    # Priorizar los scripts locales, conservando el formato por secciones.
    sys.path[:0] = [str(CODE)] + [
        str(CODE / seccion)
        for seccion in ("05_agent", "07_speech", "08_images", "09_documents")
        if (CODE / seccion).is_dir()
    ]
    from vision_luma import diagnosticar_foto
    from extraer_factura import extraer_y_validar
    from agente_luma import preguntar_al_agente

    print("\n[1/5] Leyendo correo...")
    correo = (DATA / "correo_jose.txt").read_text(encoding="utf-8")

    print("\n[2/5] Procesando audio...")
    voz = transcribir(DATA / "mensaje_jose.wav")

    print("\n[3/5] Analizando fotografía...")
    foto = diagnosticar_foto(DATA / "router_jose.jpg")

    print("\n[4/5] Analizando factura...")
    factura = extraer_y_validar(factura_url)

    print("\n[5/5] Consultando agente LUMA...")
    evidencia = f"""Correo: {correo}
Mensaje de voz: {voz}
Diagnóstico de la foto: {foto}
Factura: {factura}"""
    respuesta = preguntar_al_agente(
        "Redacta la respuesta para el cliente "
        "con esta evidencia. "
        "No prometas reembolsos; "
        "indica los siguientes pasos.\n"
        + evidencia
    )

    print("\n========== RESPUESTA LUMA ==========\n")
    print(respuesta)
    return respuesta


if __name__ == "__main__":
    main()
