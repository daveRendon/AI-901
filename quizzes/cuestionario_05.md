# Cuestionario 5 · Text analysis, Azure Language y Speech

> **Sección:** 6 y 7 · **Lecciones:** 25–33 · **Preguntas:** 10 · **Tiempo sugerido:** 15 minutos

Preguntas de escenario sobre análisis de texto, Azure Language, speech-to-text, text-to-speech y modelos multimodales de audio.

Responde sin consultar tus notas. Cuando termines, compara con [las respuestas y explicaciones](cuestionario_05_respuestas.md).

---

### 1. Un supervisor de Luma quiere saber rápidamente quién escribió un ticket, qué producto menciona, dónde ocurrió el problema y en qué fecha empezó. ¿Qué técnica de text analysis debe reconocer en el examen?

- **A.** Named entity recognition.
- **B.** Key phrase extraction.
- **C.** Sentiment analysis.
- **D.** Speech synthesis.

### 2. Luma automatiza notas para agentes humanos a partir de tickets largos. ¿Qué DOS afirmaciones sobre summarization son correctas según la lección? Selecciona DOS respuestas.

- **A.** El resumen extractivo siempre genera oraciones nuevas más naturales.
- **B.** El resumen extractivo selecciona y copia oraciones relevantes del texto original.
- **C.** El resumen abstractivo redacta texto nuevo y puede introducir errores.
- **D.** La summarization solo sirve para audio, no para texto de tickets.

### 3. Debes redactar PII en miles de transcripciones con la misma estructura de salida, confidence scores y resultados consistentes ante la misma entrada. ¿Qué enfoque recomienda el curso?

- **A.** Un modelo de propósito general con un prompt conversacional.
- **B.** Un prompt de image generation con restricciones.
- **C.** Azure Language en Foundry Tools.
- **D.** SpeechSynthesizer con una neural voice.

### 4. Comparas analizar_ticket.py con lenguaje_luma.py. ¿Qué DOS diferencias del código reflejan los dos enfoques de text analysis? Selecciona DOS respuestas.

- **A.** analizar_ticket.py recibe confidence scores por entidad automáticamente.
- **B.** analizar_ticket.py pide JSON al modelo y valida la salida con json.loads.
- **C.** lenguaje_luma.py usa TextAnalyticsClient y métodos como detect_language o recognize_pii_entities.
- **D.** lenguaje_luma.py combina keywords, entidades, sentimiento y resumen en una sola llamada.

### 5. En lenguaje_luma.py, `lang = client.detect_language(docs)[0].primary_language`. ¿Qué información espera imprimir el programa para el idioma?

- **A.** Un archivo WAV con la pronunciación del texto.
- **B.** El nombre del idioma, su código ISO 639-1 y un confidence score.
- **C.** Un resumen abstractivo del ticket y sus keywords.
- **D.** La lista de voices disponibles en Azure Speech.

### 6. Luma quiere que su respuesta hablada use una voz natural en español de México y controle pausas, velocidad y cómo se leen números o fechas. ¿Qué opción corresponde?

- **A.** Speech recognition con language identification.
- **B.** TextAnalyticsClient con recognize_pii_entities.
- **C.** Text-to-speech con una neural voice y SSML.
- **D.** Batch transcription con WAV PCM.

### 7. Luma quiere que su app lea en voz alta el estado de un caso para clientes con baja visión. ¿Qué capacidad de Azure Speech corresponde?

- **A.** Speech recognition, porque convierte audio del micrófono en texto.
- **B.** Language detection, porque identifica el idioma del ticket.
- **C.** Object detection, porque ubica objetos en una imagen.
- **D.** Speech synthesis, porque convierte texto o SSML en audio con una voz sintética.

### 8. En pregunta_hablada.py envías `pregunta.wav` a un modelo de audio. ¿Qué DOS detalles son correctos según la demo? Selecciona DOS respuestas.

- **A.** El audio viaja codificado en base64 dentro de un contenido input_audio.
- **B.** La API exige transcribir primero el archivo con SpeechRecognizer.
- **C.** La autenticación del ejemplo usa una API key de SpeechConfig.
- **D.** modalities=["text"] pide que la respuesta llegue como texto.

### 9. En voz_luma.py, una grabación corta se transcribe con `recognize_once_async().get()`. ¿Qué debes revisar para saber si la transcripción fue exitosa?

- **A.** El valor de result.reason, buscando RecognizedSpeech.
- **B.** El nombre de la neural voice configurada para synthesis.
- **C.** El tamaño del archivo respuesta.wav.
- **D.** La cantidad de entidades PII encontradas.

### 10. Luma desea transcribir cada noche llamadas de soporte de 20 minutos en grandes volúmenes. ¿Qué opción evita el uso incorrecto de recognize_once?

- **A.** Text to speech con SSML para controlar pausas y énfasis.
- **B.** Image generation con un prompt sobre la llamada.
- **C.** recognize_once para cada archivo completo.
- **D.** Batch transcription o continuous recognition para audio largo o por lotes.
