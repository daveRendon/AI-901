# Cuestionario 6 · Computer vision, generación de imágenes y Content Understanding · Respuestas y explicaciones

Vuelve a [las preguntas](cuestionario_06.md). Para cada error, anota el objetivo y repasa la lección indicada.

## Clave de respuestas

| # | Respuesta | Objetivo del examen | Lecciones |
|---|---|---|---|
| 1 | B | Identify features and capabilities of computer vision and image-generation models | 34 |
| 2 | A, C | Interpret visual input in prompts by using a deployed multimodal model | 35, 38 |
| 3 | C | Create new visual outputs by using generative models | 36 |
| 4 | D | Build a lightweight application that includes vision capabilities | 37 |
| 5 | B | Interpret visual input in prompts by using a deployed multimodal model | 38 |
| 6 | A, C | Extract information from documents and forms by using Azure Content Understanding in Foundry Tools | 39 |
| 7 | B | Extract information from documents and forms by using Azure Content Understanding in Foundry Tools | 40 |
| 8 | D | Extract information from images by using Content Understanding | 41 |
| 9 | A | Extract information from audio and video by using Content Understanding | 42 |
| 10 | A | Build a lightweight application with information extraction capabilities by using Content Understanding | 43 |

---

### 1. Luma necesita ubicar todos los routers visibles en una foto de almacén y dibujar un rectángulo alrededor de cada uno. ¿Qué tarea de computer vision corresponde?

- ❌ **A.** Semantic segmentation, porque clasifica cada píxel de la imagen.  
  Segmentation daría píxeles por clase; el escenario pide rectángulos alrededor de objetos.
- ✅ **B.** Object detection, porque identifica qué objetos hay y dónde están con bounding boxes.  
  Object detection responde qué objetos aparecen y dónde se ubican.
- ❌ **C.** Image classification, porque asigna una etiqueta a toda la imagen.  
  Classification diría que la imagen contiene routers, pero no ubicaría cada uno.
- ❌ **D.** Image generation, porque crea una imagen nueva de routers.  
  Image generation produce visuales nuevos; no analiza una foto existente.

**Respuesta:** B. La lección 34 resume: classification responde qué es, detection qué y dónde, segmentation qué píxeles y contextual analysis qué está pasando. Repasa la lección 34.

*Objetivo: Identify features and capabilities of computer vision and image-generation models · Lecciones: 34*

### 2. Vas a pedir a gpt-5-mini que interprete una foto borrosa de un router en el playground. ¿Qué DOS instrucciones mejoran la confiabilidad de la respuesta? Selecciona DOS respuestas.

- ✅ **A.** Pide que distinga lo visible de lo supuesto y que no invente detalles.  
  Separar visto de supuesto reduce detalles inventados y respuestas demasiado seguras.
- ❌ **B.** Pide que genere una imagen más nítida antes de contestar.  
  Interpretar la foto no requiere image generation; el modelo debe reconocer incertidumbre.
- ✅ **C.** Indica que si la imagen no es clara, lo diga y pida otra foto.  
  La lección 35 recomienda dar una salida explícita para la incertidumbre.
- ❌ **D.** Evita cualquier formato estructurado para que el modelo responda libremente.  
  Pedir lista, tabla o JSON ayuda a que la respuesta sea utilizable.

**Respuesta:** A, C. Los prompts con imágenes deben ser concretos, pedir evidencia y admitir incertidumbre. Un resultado visual convincente puede ser incorrecto, sobre todo con baja resolución o mal ángulo. Repasa las lecciones 35 y 38.

*Objetivo: Interpret visual input in prompts by using a deployed multimodal model · Lecciones: 35, 38*

### 3. Marketing de Luma necesita una ilustración original de un router para la página de ayuda. ¿Qué prompt se alinea mejor con la guía del curso?

- ❌ **A.** Un router.  
  Es débil: deja estilo, fondo, composición y restricciones al azar.
- ❌ **B.** Haz algo moderno con internet.  
  Es ambiguo y no define el sujeto ni restricciones necesarias.
- ✅ **C.** Ilustración plana de un router blanco con tres luces verdes, vista frontal, fondo claro, sin texto ni logotipos.  
  Define sujeto, estilo, composición, fondo y restricciones, como recomienda la lección.
- ❌ **D.** Copia el logotipo de una marca conocida y ponlo en el router.  
  El curso recomienda evitar marcas de terceros y usar generación responsable.

**Respuesta:** C. Un buen prompt de imagen especifica sujeto, estilo, composición, iluminación y restricciones. También debe evitar texto, logotipos o marcas de terceros cuando no corresponden. Repasa la lección 36.

*Objetivo: Create new visual outputs by using generative models · Lecciones: 36*

### 4. En vision_luma.py, la app lee `router_cliente.jpg`, lo codifica en base64 y crea `data:image/jpeg;base64,...`. ¿Cómo se envía la imagen al modelo en la Responses API?

- ❌ **A.** Como parámetro `model`, reemplazando el nombre del deployment.  
  model sigue siendo el deployment; la imagen viaja en el contenido del mensaje.
- ❌ **B.** Como archivo adjunto en SpeechConfig.  
  SpeechConfig pertenece a Azure Speech, no a una solicitud multimodal de visión.
- ❌ **C.** Como analyzer_id de Content Understanding.  
  analyzer_id se usa para extracción de información, no para prompts con visión.
- ✅ **D.** Como una parte de contenido `input_image` junto con `input_text`.  
  La solicitud multimodal combina texto e imagen en el mismo mensaje.

**Respuesta:** D. La lección 37 muestra un contenido con input_text e input_image. La imagen puede ser una URL pública o un data URL en base64; output_text trae la interpretación. Repasa la lección 37.

*Objetivo: Build a lightweight application that includes vision capabilities · Lecciones: 37*

### 5. El modelo multimodal afirma con seguridad que leyó el número de serie en una etiqueta borrosa. La app debe guardar ese valor en una base de datos. ¿Qué enfoque es más adecuado?

- ❌ **A.** Aceptar el texto porque el modelo multimodal responde con confianza.  
  La confianza en el lenguaje no garantiza que el texto pequeño se haya leído bien.
- ✅ **B.** Usar Content Understanding con un campo numero_serie y revisar score y ubicación.  
  Para campos específicos de una imagen, Content Understanding da schema, confidence score y grounding.
- ❌ **C.** Generar una imagen nueva con un número de serie más claro.  
  Generar una imagen no extrae ni valida el dato real del cliente.
- ❌ **D.** Usar Speech recognition para convertir la etiqueta en texto.  
  Speech recognition procesa audio, no texto visible en una imagen.

**Respuesta:** B. La lección 38 conecta visión con extracción: para leer campos específicos como un número de serie, usa Content Understanding, no una descripción general. Repasa la lección 38.

*Objetivo: Interpret visual input in prompts by using a deployed multimodal model · Lecciones: 38*

### 6. Diseñas un custom analyzer para facturas de Luma. ¿Qué DOS conceptos de Content Understanding debes incluir para obtener datos integrables? Selecciona DOS respuestas.

- ✅ **A.** Un schema con campos, tipos y descripciones en lenguaje natural.  
  El schema define qué valores quieres obtener y guía la extracción.
- ❌ **B.** Un prompt para que el usuario final elija manualmente cada campo.  
  La extracción debe estructurar automáticamente el contenido mediante el analyzer.
- ✅ **C.** Métodos de campo como extract, generate o classify según el tipo de valor.  
  extract toma valores visibles, generate deduce o redacta y classify elige categorías.
- ❌ **D.** Una llamada a SpeechSynthesizer para convertir los campos en audio.  
  SpeechSynthesizer no define ni extrae campos de documentos.

**Respuesta:** A, C. Content Understanding convierte contenido no estructurado en campos con significado. El analyzer usa un schema, métodos de campo, normalización, confidence scores y grounding. Repasa la lección 39.

*Objetivo: Extract information from documents and forms by using Azure Content Understanding in Foundry Tools · Lecciones: 39*

### 7. En Content Understanding, analizas una factura escaneada. Primero obtienes líneas de texto; luego tablas y párrafos; finalmente campos como total y fecha. ¿Cuál es la secuencia correcta de analyzers?

- ❌ **A.** Image generation, Speech SDK y TextAnalyticsClient.  
  Esas herramientas no corresponden a los niveles de análisis de documentos de Content Understanding.
- ✅ **B.** Read, Layout y un analyzer de dominio o custom.  
  Read devuelve texto, Layout estructura y dominio/custom devuelve campos con significado.
- ❌ **C.** Web search, code interpreter y MCP.  
  Son tools de agents, no analyzers para documentos.
- ❌ **D.** Classification, detection y segmentation.  
  Son tareas de computer vision, no niveles de extracción documental.

**Respuesta:** B. La lección 40 compara Read, Layout y analyzers de dominio. El objetivo es pasar de texto a estructura y luego a campos de negocio en JSON. Repasa la lección 40.

*Objetivo: Extract information from documents and forms by using Azure Content Understanding in Foundry Tools · Lecciones: 40*

### 8. En una foto de etiqueta, el campo `estado_equipo` debe ser solo `sin_danos` o `danado`. ¿Qué método de campo del schema usa mejor esa lista cerrada?

- ❌ **A.** extract, porque copia siempre cualquier palabra visible.  
  extract toma valores visibles; no elige entre categorías cerradas cuando debe clasificar el estado.
- ❌ **B.** generate, porque redacta un resumen libre del equipo.  
  generate produce un valor nuevo, pero aquí se requiere una categoría cerrada.
- ❌ **C.** read, porque OCR decide el significado de cada valor.  
  Read obtiene texto, pero no asigna por sí solo significado de campo.
- ✅ **D.** classify, porque elige entre opciones definidas en enum.  
  classify selecciona una categoría de una lista cerrada, como sin_danos o danado.

**Respuesta:** D. En la lección 41, modelo, número de serie y MAC usan extract porque están visibles; estado_equipo usa classify con opciones definidas. Repasa la lección 41.

*Objetivo: Extract information from images by using Content Understanding · Lecciones: 41*

### 9. Luma quiere analizar miles de llamadas grabadas para obtener motivo, sentimiento y compromiso del agente sin escucharlas manualmente. ¿Qué solución encaja mejor?

- ✅ **A.** Un analyzer de audio de Content Understanding con campos classify y generate.  
  Content Understanding extrae transcripción, resumen y campos definidos para audio.
- ❌ **B.** Un modelo de image generation con prompt de post-call analytics.  
  Image generation no procesa llamadas grabadas ni genera campos de audio.
- ❌ **C.** Un prompt visual con input_image para cada llamada.  
  input_image se usa para imágenes, no para grabaciones de llamadas.
- ❌ **D.** Solo OCR/Read, porque las llamadas contienen palabras.  
  OCR lee texto en imágenes; para audio se requiere transcripción y extracción de campos.

**Respuesta:** A. La lección 42 muestra que del audio se extraen transcripción, resumen y campos como motivo, sentimiento y compromiso. classify y generate convierten la conversación en un registro. Repasa la lección 42.

*Objetivo: Extract information from audio and video by using Content Understanding · Lecciones: 42*

### 10. En extraer_factura.py, después de `poller = client.begin_analyze(...)`, el código llama a `poller.result()`. ¿Por qué es necesario?

- ✅ **A.** Porque begin_analyze solo inicia una operación asíncrona y hay que esperar el resultado.  
  Content Understanding procesa el contenido como trabajo asíncrono; result espera a que termine.
- ❌ **B.** Porque result convierte el texto extraído en audio con una neural voice.  
  Eso corresponde a SpeechSynthesizer, no al poller de Content Understanding.
- ❌ **C.** Porque result cambia automáticamente de prebuilt-invoice a prebuilt-receipt.  
  El analyzer se define en begin_analyze; result no cambia el analyzer.
- ❌ **D.** Porque result elimina la necesidad de validar campos y confidence scores.  
  Después de obtener el resultado, la aplicación aún debe validar scores, formatos y reglas de negocio.

**Respuesta:** A. La lección 43 explica que begin_analyze envía el contenido y devuelve un poller. poller.result() espera el resultado; luego validas umbrales, formatos, duplicados y reglas de negocio. Repasa la lección 43.

*Objetivo: Build a lightweight application with information extraction capabilities by using Content Understanding · Lecciones: 43*
