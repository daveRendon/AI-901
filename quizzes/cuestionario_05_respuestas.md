# Cuestionario 5 · Text analysis, Azure Language y Speech · Respuestas y explicaciones

Vuelve a [las preguntas](cuestionario_05.md). Para cada error, anota el objetivo y repasa la lección indicada.

## Clave de respuestas

| # | Respuesta | Objetivo del examen | Lecciones |
|---|---|---|---|
| 1 | A | Describe common text analysis techniques, including keyword extraction, entity detection, sentiment analysis, and summarization | 25 |
| 2 | B, C | Describe common text analysis techniques, including keyword extraction, entity detection, sentiment analysis, and summarization | 25 |
| 3 | C | Build a lightweight application that includes text analysis | 26, 29 |
| 4 | B, C | Build a lightweight application that includes text analysis | 27, 28 |
| 5 | B | Build a lightweight application that includes text analysis | 28 |
| 6 | C | Identify features and capabilities of speech recognition and speech synthesis | 30 |
| 7 | D | Identify features and capabilities of speech recognition and speech synthesis | 30 |
| 8 | A, D | Respond to spoken prompts by using a deployed multimodal model | 31 |
| 9 | A | Build a lightweight application by using Azure Speech in Foundry Tools | 32 |
| 10 | D | Identify features and capabilities of speech recognition and speech synthesis | 33 |

---

### 1. Un supervisor de Luma quiere saber rápidamente quién escribió un ticket, qué producto menciona, dónde ocurrió el problema y en qué fecha empezó. ¿Qué técnica de text analysis debe reconocer en el examen?

- ✅ **A.** Named entity recognition.  
  Entity recognition identifica personas, productos, ubicaciones y fechas en el texto.
- ❌ **B.** Key phrase extraction.  
  Key phrases indican temas principales, pero no clasifican cada nombre o fecha como entidad.
- ❌ **C.** Sentiment analysis.  
  Sentiment analysis clasifica la emoción o polaridad del texto, no quién, qué, dónde y cuándo.
- ❌ **D.** Speech synthesis.  
  Speech synthesis convierte texto en audio; no analiza entidades de un ticket.

**Respuesta:** A. La lección 25 distingue keywords, entidades, sentimiento y resumen. Identificar nombres, fechas, lugares o productos es named entity recognition. Repasa la lección 25.

*Objetivo: Describe common text analysis techniques, including keyword extraction, entity detection, sentiment analysis, and summarization · Lecciones: 25*

### 2. Luma automatiza notas para agentes humanos a partir de tickets largos. ¿Qué DOS afirmaciones sobre summarization son correctas según la lección? Selecciona DOS respuestas.

- ❌ **A.** El resumen extractivo siempre genera oraciones nuevas más naturales.  
  Generar oraciones nuevas corresponde al resumen abstractivo, no al extractivo.
- ✅ **B.** El resumen extractivo selecciona y copia oraciones relevantes del texto original.  
  El enfoque extractivo conserva oraciones del texto, por eso suele ser fiel pero fragmentado.
- ✅ **C.** El resumen abstractivo redacta texto nuevo y puede introducir errores.  
  Los modelos generativos producen resúmenes abstractivos: naturales, compactos y con riesgo de error.
- ❌ **D.** La summarization solo sirve para audio, no para texto de tickets.  
  La lección usa summarization sobre tickets de texto y conversaciones.

**Respuesta:** B, C. Extractivo copia partes relevantes; abstractivo redacta una versión nueva. El examen puede preguntar por la diferencia porque afecta fidelidad y riesgo de errores. Repasa la lección 25.

*Objetivo: Describe common text analysis techniques, including keyword extraction, entity detection, sentiment analysis, and summarization · Lecciones: 25*

### 3. Debes redactar PII en miles de transcripciones con la misma estructura de salida, confidence scores y resultados consistentes ante la misma entrada. ¿Qué enfoque recomienda el curso?

- ❌ **A.** Un modelo de propósito general con un prompt conversacional.  
  El modelo general es flexible, pero puede variar y no devuelve confidence scores comparables.
- ❌ **B.** Un prompt de image generation con restricciones.  
  Image generation crea imágenes; no redacta datos personales de texto.
- ✅ **C.** Azure Language en Foundry Tools.  
  Azure Language ofrece tareas especializadas, estructura fija, resultados deterministas y confidence scores.
- ❌ **D.** SpeechSynthesizer con una neural voice.  
  SpeechSynthesizer convierte texto en audio; no detecta ni redacta PII.

**Respuesta:** C. Las palabras estructura, consistencia y confidence score apuntan a Azure Language. La flexibilidad y varias tareas en una llamada apuntan a un modelo general. Repasa las lecciones 26 y 29.

*Objetivo: Build a lightweight application that includes text analysis · Lecciones: 26, 29*

### 4. Comparas analizar_ticket.py con lenguaje_luma.py. ¿Qué DOS diferencias del código reflejan los dos enfoques de text analysis? Selecciona DOS respuestas.

- ❌ **A.** analizar_ticket.py recibe confidence scores por entidad automáticamente.  
  El modelo general no devuelve confidence scores en esa demo.
- ✅ **B.** analizar_ticket.py pide JSON al modelo y valida la salida con json.loads.  
  El modelo general recibe instrucciones para devolver un JSON definido por el desarrollador.
- ✅ **C.** lenguaje_luma.py usa TextAnalyticsClient y métodos como detect_language o recognize_pii_entities.  
  Azure Language expone métodos específicos por tarea mediante TextAnalyticsClient.
- ❌ **D.** lenguaje_luma.py combina keywords, entidades, sentimiento y resumen en una sola llamada.  
  Azure Language usa un método por tarea; la demo detecta idioma y PII por separado.

**Respuesta:** B, C. La demo de modelo general combina tareas con prompts y JSON; Azure Language usa un cliente especializado, esquema fijo y scores por resultado. Repasa las lecciones 27 y 28.

*Objetivo: Build a lightweight application that includes text analysis · Lecciones: 27, 28*

### 5. En lenguaje_luma.py, `lang = client.detect_language(docs)[0].primary_language`. ¿Qué información espera imprimir el programa para el idioma?

- ❌ **A.** Un archivo WAV con la pronunciación del texto.  
  Eso corresponde a text-to-speech, no a language detection.
- ✅ **B.** El nombre del idioma, su código ISO 639-1 y un confidence score.  
  detect_language devuelve el idioma principal con name, iso6391_name y confidence_score.
- ❌ **C.** Un resumen abstractivo del ticket y sus keywords.  
  Esa salida pertenece a la demo con modelo general, no a detect_language.
- ❌ **D.** La lista de voices disponibles en Azure Speech.  
  Las voices pertenecen a Azure Speech, no a Azure Language.

**Respuesta:** B. Azure Language devuelve resultados estructurados. En language detection, la estructura incluye nombre del idioma, código ISO y confidence score para decidir enrutamiento. Repasa la lección 28.

*Objetivo: Build a lightweight application that includes text analysis · Lecciones: 28*

### 6. Luma quiere que su respuesta hablada use una voz natural en español de México y controle pausas, velocidad y cómo se leen números o fechas. ¿Qué opción corresponde?

- ❌ **A.** Speech recognition con language identification.  
  Speech recognition convierte voz en texto; no genera una respuesta hablada.
- ❌ **B.** TextAnalyticsClient con recognize_pii_entities.  
  TextAnalyticsClient analiza texto; no controla voces ni pausas de salida.
- ✅ **C.** Text-to-speech con una neural voice y SSML.  
  Azure Speech TTS usa neural voices y SSML para pronunciación, pausas, velocidad y énfasis.
- ❌ **D.** Batch transcription con WAV PCM.  
  Batch transcription sirve para transcribir audio largo, no para sintetizar voz.

**Respuesta:** C. La lección 30 distingue STT y TTS. Para leer texto en voz alta con naturalidad se usa speech synthesis; SSML controla pronunciación, pausas, ritmo y cómo leer números o fechas. Repasa la lección 30.

*Objetivo: Identify features and capabilities of speech recognition and speech synthesis · Lecciones: 30*

### 7. Luma quiere que su app lea en voz alta el estado de un caso para clientes con baja visión. ¿Qué capacidad de Azure Speech corresponde?

- ❌ **A.** Speech recognition, porque convierte audio del micrófono en texto.  
  Recognition o STT va de voz a texto; aquí se necesita texto a voz.
- ❌ **B.** Language detection, porque identifica el idioma del ticket.  
  Detectar idioma no genera audio para el cliente.
- ❌ **C.** Object detection, porque ubica objetos en una imagen.  
  Object detection es computer vision, no síntesis de voz.
- ✅ **D.** Speech synthesis, porque convierte texto o SSML en audio con una voz sintética.  
  Synthesis o TTS recibe texto y genera audio, ideal para leer respuestas en voz alta.

**Respuesta:** D. La lección 30 enfatiza la dirección: speech recognition convierte voz en texto; speech synthesis convierte texto en voz. Para accesibilidad y lectura en voz alta, usa TTS. Repasa la lección 30.

*Objetivo: Identify features and capabilities of speech recognition and speech synthesis · Lecciones: 30*

### 8. En pregunta_hablada.py envías `pregunta.wav` a un modelo de audio. ¿Qué DOS detalles son correctos según la demo? Selecciona DOS respuestas.

- ✅ **A.** El audio viaja codificado en base64 dentro de un contenido input_audio.  
  La demo lee el WAV, lo codifica en base64 y lo envía con type input_audio.
- ❌ **B.** La API exige transcribir primero el archivo con SpeechRecognizer.  
  El modelo multimodal entiende la voz directamente; no hay transcripción previa en el código.
- ❌ **C.** La autenticación del ejemplo usa una API key de SpeechConfig.  
  El código usa DefaultAzureCredential con get_bearer_token_provider para Entra ID.
- ✅ **D.** modalities=["text"] pide que la respuesta llegue como texto.  
  El ejemplo solicita una salida de texto, aunque los modelos de audio también pueden responder con audio.

**Respuesta:** A, D. Los modelos multimodales de audio aceptan la voz como parte del prompt. El curso muestra input_audio en base64 y salida en texto con chat completions. Repasa la lección 31.

*Objetivo: Respond to spoken prompts by using a deployed multimodal model · Lecciones: 31*

### 9. En voz_luma.py, una grabación corta se transcribe con `recognize_once_async().get()`. ¿Qué debes revisar para saber si la transcripción fue exitosa?

- ✅ **A.** El valor de result.reason, buscando RecognizedSpeech.  
  ResultReason indica éxito, NoMatch o Canceled; siempre debe revisarse.
- ❌ **B.** El nombre de la neural voice configurada para synthesis.  
  La voice afecta TTS, no si STT reconoció correctamente el audio.
- ❌ **C.** El tamaño del archivo respuesta.wav.  
  respuesta.wav se genera en synthesis, después de la transcripción.
- ❌ **D.** La cantidad de entidades PII encontradas.  
  PII corresponde a Azure Language, no al resultado básico del SpeechRecognizer.

**Respuesta:** A. SpeechRecognizer convierte audio en texto y devuelve un ResultReason. RecognizedSpeech indica éxito, NoMatch que no se entendió voz y Canceled un error como credenciales o red. Repasa la lección 32.

*Objetivo: Build a lightweight application by using Azure Speech in Foundry Tools · Lecciones: 32*

### 10. Luma desea transcribir cada noche llamadas de soporte de 20 minutos en grandes volúmenes. ¿Qué opción evita el uso incorrecto de recognize_once?

- ❌ **A.** Text to speech con SSML para controlar pausas y énfasis.  
  TTS genera audio; no transcribe llamadas.
- ❌ **B.** Image generation con un prompt sobre la llamada.  
  Image generation crea imágenes y no procesa audio.
- ❌ **C.** recognize_once para cada archivo completo.  
  recognize_once reconoce una sola frase corta, no llamadas largas.
- ✅ **D.** Batch transcription o continuous recognition para audio largo o por lotes.  
  La lección recomienda continuous o batch cuando la duración o el volumen superan una frase corta.

**Respuesta:** D. recognize_once es para frases cortas. Para llamadas largas se usa continuous recognition; para grandes volúmenes procesados periódicamente, batch transcription es adecuado. Repasa la lección 33.

*Objetivo: Identify features and capabilities of speech recognition and speech synthesis · Lecciones: 33*
