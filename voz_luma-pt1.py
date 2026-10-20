
import os
from pathlib import Path
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

# Force loading the .env from the project folder
load_dotenv(
    Path(__file__).resolve().parent / ".env",
    override=True
)

# Read endpoint and key
speech_endpoint = os.environ["SPEECH_ENDPOINT"].strip()
speech_key = os.environ["SPEECH_KEY"].strip()

# Show the actual endpoint being used
print("Speech endpoint:", speech_endpoint)

# Validate endpoint
if "<" in speech_endpoint or ">" in speech_endpoint:
    raise ValueError(
        "SPEECH_ENDPOINT contains a placeholder. "
        "Update the .env file with your real Azure endpoint."
    )

speech_config = speechsdk.SpeechConfig(
    subscription=speech_key,
    endpoint=speech_endpoint
)

speech_config.speech_recognition_language = "es-CO"

# Use the audio inside the data folder
audio_file = Path(__file__).resolve().parent / "data" / "mensaje.wav"

audio_in = speechsdk.audio.AudioConfig(
    filename=str(audio_file)
)

recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_in
)

print("Reconociendo voz...")

result = recognizer.recognize_once_async().get()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Cliente dijo:", result.text)
else:
    print("No se reconoció voz:", result.reason)

    if result.reason == speechsdk.ResultReason.Canceled:
        print("Error:", result.cancellation_details.error_details)
