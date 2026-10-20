# Práctica 5 · Speech y audio

- **Sección:** 7 · Speech, audio y modelos multimodales
- **Lecciones:** 30–33
- **Duración estimada:** 55 minutos
- **Nivel:** Intermedio
- **Habilidades medidas:**
  - `Implement AI solutions for text and speech by using Foundry`
  - `Identify AI workloads`

## Objetivo

Responderás a una pregunta hablada con un modelo multimodal de audio, probarás Voice mode en el agente y construirás un pipeline clásico con Azure Speech: speech-to-text, modelo y text-to-speech.

## Lo que vas a construir

Ejecuciones de [pregunta_hablada.py](../pregunta_hablada.py) y [voz_luma.py](../voz_luma.py), más pruebas con `pregunta.wav`, `pregunta_molesta.wav`, `mensaje.wav`, `mensaje_jose.wav` y `respuesta.wav`.

## Requisitos

- [ ] Práctica 3 completada: `luma-soporte-agent` existe.
- [ ] Modelo de audio desplegado, por ejemplo `gpt-4o-mini-audio-preview` u otro disponible en tu región.
- [ ] Azure Speech en **Build, Services** con key y endpoint.
- [ ] Variables en `.env`: `AZURE_OPENAI_ENDPOINT`, `AUDIO_DEPLOYMENT_NAME`, `SPEECH_ENDPOINT`, `SPEECH_KEY`.
- [ ] Archivos [pregunta.wav](../data/pregunta.wav), [pregunta_molesta.wav](../data/pregunta_molesta.wav), [mensaje.wav](../data/mensaje.wav), [mensaje_jose.wav](../data/mensaje_jose.wav).
- [ ] Paquete `azure-cognitiveservices-speech` instalado.

## Costo y limpieza

Los modelos de audio y Azure Speech cobran por uso. Usa audios cortos para pruebas. `voz_luma.py` crea `respuesta.wav`; puedes conservarlo o borrarlo al final si no lo necesitas.

## Pasos

### Parte 1 · Diferenciar STT, TTS y audio multimodal

1. Recuerda: speech recognition o STT convierte voz en texto.
2. Recuerda: speech synthesis o TTS convierte texto en voz.
3. El pipeline clásico usa STT, luego modelo, luego TTS.
4. Un modelo multimodal de audio recibe audio directamente como parte del prompt.
5. Voice Live permite conversación de voz en tiempo real con un agente.
6. Para audios largos, `recognize_once` no basta; usa continuous recognition o batch transcription.
7. ✅ Punto de control: sabes elegir entre control por etapas y modelo de audio directo.

### Parte 2 · Desplegar o verificar modelo de audio

1. En Foundry, abre el model catalog.
2. Busca `gpt-4o-mini-audio-preview` u otro modelo con entrada de audio.
3. Revisa disponibilidad regional.
4. Despliega con configuración por defecto si tienes cuota.
5. Anota el deployment name.
6. Completa en `.env`:
   ```env
   AZURE_OPENAI_ENDPOINT=https://<recurso>.openai.azure.com/
   AUDIO_DEPLOYMENT_NAME=gpt-4o-mini-audio-preview
   ```
7. Si el modelo no está disponible, usa otro modelo de audio compatible y ajusta `AUDIO_DEPLOYMENT_NAME`.
8. ✅ Punto de control: tienes un deployment de audio o una alternativa disponible.

### Parte 3 · Ejecutar `pregunta_hablada.py`

1. Abre [pregunta_hablada.py](../pregunta_hablada.py).
2. Observa `get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")`.
3. Observa que lee [pregunta.wav](../data/pregunta.wav) y lo codifica en base64.
4. Observa el mensaje con `input_audio` y formato `wav`.
5. Ejecuta:
   ```powershell
   python pregunta_hablada.py
   ```
6. Esperado: respuesta en texto con pasos para reiniciar el router Luma.
7. Cambia temporalmente el archivo de audio a `pregunta_molesta.wav`.
8. Ejecuta otra vez.
9. Observa si la respuesta reconoce el tono molesto con más empatía.
10. ✅ Punto de control: el modelo respondió a la voz sin transcripción previa en tu código.

### Parte 4 · Probar Voice mode en el agente

1. En el portal, abre `luma-soporte-agent`.
2. Activa **Voice mode** debajo del selector de modelo si aparece disponible.
3. Abre la configuración de voz.
4. Selecciona entrada y salida de voz.
5. Elige una voz en español de México.
6. Usa la vista previa para escucharla.
7. Guarda la configuración del agente.
8. Selecciona **Start session**.
9. Permite el acceso al micrófono.
10. Pregunta: `¿Cuánto dura la garantía de mi router?`
11. Activa subtítulos con el botón **cc**.
12. Haz seguimiento: `¿Y qué necesito para el reemplazo?`
13. Cierra la sesión y revisa la transcripción final.
14. ✅ Punto de control: el agente conversa en voz y usa sus instrucciones y conocimiento.

### Parte 5 · Probar Azure Speech en el portal

1. En el project, abre **Build**.
2. Entra a **Services**.
3. Abre **Azure Speech**.
4. Prueba **Speech to text** con una muestra o con `mensaje.wav`.
5. Revisa la transcripción.
6. Prueba **Text to speech** con una frase corta.
7. Elige español de México y escucha varias neural voices.
8. Abre la pestaña **Code** si está disponible.
9. Copia endpoint y key al `.env`:
   ```env
   SPEECH_ENDPOINT=https://<recurso>.cognitiveservices.azure.com/
   SPEECH_KEY=<tu-key>
   ```
10. ✅ Punto de control: tienes el endpoint y la key de Speech configurados de forma local.

### Parte 6 · Ejecutar `voz_luma.py`

1. Abre [voz_luma.py](../voz_luma.py).
2. Revisa `_config()`: `SpeechConfig` concentra key, endpoint e idioma `es-MX`.
3. Revisa `transcribir_frase`: usa `recognize_once_async().get()`.
4. Revisa `responder_con_voz`: usa `SpeechSynthesizer` y guarda en `respuesta.wav`.
5. Ejecuta:
   ```powershell
   python voz_luma.py
   ```
6. Esperado: imprime `Cliente dijo:` con la transcripción de `mensaje.wav`.
7. Esperado: crea `respuesta.wav`.
8. Reproduce el WAV desde tu explorador o editor.
9. ✅ Punto de control: tienes STT y TTS funcionando con Azure Speech.

### Parte 7 · Cambiar la voz

1. En [voz_luma.py](../voz_luma.py), localiza `responder_con_voz`.
2. Observa el valor por defecto: `es-MX-DaliaNeural`.
3. Cambia la llamada del bloque principal para pasar `voz="es-MX-JorgeNeural"`.
4. Ejecuta de nuevo:
   ```powershell
   python voz_luma.py
   ```
5. Reproduce `respuesta.wav`.
6. Compara la prosodia y la voz.
7. Si no modificas el archivo, también puedes probar el cambio desde una sesión interactiva o adaptar temporalmente el script.
8. ✅ Punto de control: misma respuesta textual, otra neural voice.

### Parte 8 · Continuous recognition con `mensaje_jose.wav`

1. Revisa la función `transcribir` en [voz_luma.py](../voz_luma.py).
2. Observa que usa `start_continuous_recognition()`.
3. Observa que junta partes reconocidas en una lista.
4. Abre [luma_caso.py](../luma_caso.py) y observa cómo importa `transcribir` ajustando `sys.path`.
5. Observa la llamada `transcribir(DATA / "mensaje_jose.wav")`.
6. Para practicar, puedes cambiar temporalmente el bloque principal de `voz_luma.py` para imprimir `transcribir(DATA / "mensaje_jose.wav")`.
7. Ejecuta `python voz_luma.py` después del cambio temporal.
8. Espera más que con `recognize_once`, porque `mensaje_jose.wav` dura alrededor de 40 segundos.
9. Revierte el cambio temporal si quieres conservar el script como venía.
10. ✅ Punto de control: entiendes por qué mensajes largos requieren continuous recognition.

### Parte 9 · Validar formatos y resultados

1. Usa WAV PCM de 16 kHz, 16 bits y mono para grabaciones nuevas.
2. Si usas MP3 u OGG, revisa configuración adicional del SDK.
3. Revisa siempre `result.reason`.
4. `RecognizedSpeech` significa éxito.
5. `NoMatch` indica que no se entendió la voz.
6. `Canceled` suele indicar credenciales, red o configuración.
7. Considera ruido, acentos, varias voces y privacidad.
8. Pide consentimiento antes de almacenar voz real de clientes.
9. ✅ Punto de control: tu práctica respeta formato, idioma y uso responsable.

## Retos opcionales

- Conecta `transcribir_frase(DATA / "mensaje.wav")` con tu agente y luego genera audio con la respuesta.
- Prueba SSML en el playground para cambiar pausas o énfasis.
- Graba tu propia pregunta en WAV y reemplaza `pregunta.wav`.

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| Modelo de audio no aparece | Región o cuota no compatible | Cambia región o usa otro modelo de audio disponible. |
| 401 con modelo de audio | Endpoint o token incorrecto | Revisa `AZURE_OPENAI_ENDPOINT` y `az login`. |
| `NoMatch` | Audio no entendible, idioma equivocado o ruido | Revisa calidad, `es-MX` y formato. |
| `Canceled` | Key, endpoint o red de Speech | Verifica `SPEECH_KEY` y `SPEECH_ENDPOINT`. |
| No se crea `respuesta.wav` | Carpeta o síntesis fallida | Revisa permisos y `ResultReason.SynthesizingAudioCompleted`. |
| Audio largo se corta | Usaste `recognize_once` | Usa continuous recognition o batch transcription. |
| Voz no disponible | Locale o nombre de voz incorrecto | Elige una voz del mismo locale en el portal. |

## Comprueba lo aprendido

1. Luma quiere transcribir llamadas de 20 minutos cada noche. ¿Por qué `recognize_once` no es la opción adecuada?
2. Una app necesita redactar PII antes de enviar texto al modelo. ¿Conviene pipeline clásico o modelo de audio directo?
3. El usuario oye una voz natural en español de México. ¿Qué propiedad del Speech SDK controla esa voz?

## Siguiente paso

Continúa con [Práctica 6 · Vision y generación de imágenes](practica_06_vision_y_generacion_de_imagenes.md).
