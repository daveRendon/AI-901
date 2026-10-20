# Cuestionario 6 · Computer vision, generación de imágenes y Content Understanding

> **Sección:** 8 y 9 · **Lecciones:** 34–43 · **Preguntas:** 10 · **Tiempo sugerido:** 15 minutos

Preguntas de escenario sobre visión, generación de imágenes y extracción multimodal de información con Content Understanding.

Responde sin consultar tus notas. Cuando termines, compara con [las respuestas y explicaciones](cuestionario_06_respuestas.md).

---

### 1. Luma necesita ubicar todos los routers visibles en una foto de almacén y dibujar un rectángulo alrededor de cada uno. ¿Qué tarea de computer vision corresponde?

- **A.** Semantic segmentation, porque clasifica cada píxel de la imagen.
- **B.** Object detection, porque identifica qué objetos hay y dónde están con bounding boxes.
- **C.** Image classification, porque asigna una etiqueta a toda la imagen.
- **D.** Image generation, porque crea una imagen nueva de routers.

### 2. Vas a pedir a gpt-5-mini que interprete una foto borrosa de un router en el playground. ¿Qué DOS instrucciones mejoran la confiabilidad de la respuesta? Selecciona DOS respuestas.

- **A.** Pide que distinga lo visible de lo supuesto y que no invente detalles.
- **B.** Pide que genere una imagen más nítida antes de contestar.
- **C.** Indica que si la imagen no es clara, lo diga y pida otra foto.
- **D.** Evita cualquier formato estructurado para que el modelo responda libremente.

### 3. Marketing de Luma necesita una ilustración original de un router para la página de ayuda. ¿Qué prompt se alinea mejor con la guía del curso?

- **A.** Un router.
- **B.** Haz algo moderno con internet.
- **C.** Ilustración plana de un router blanco con tres luces verdes, vista frontal, fondo claro, sin texto ni logotipos.
- **D.** Copia el logotipo de una marca conocida y ponlo en el router.

### 4. En vision_luma.py, la app lee `router_cliente.jpg`, lo codifica en base64 y crea `data:image/jpeg;base64,...`. ¿Cómo se envía la imagen al modelo en la Responses API?

- **A.** Como parámetro `model`, reemplazando el nombre del deployment.
- **B.** Como archivo adjunto en SpeechConfig.
- **C.** Como analyzer_id de Content Understanding.
- **D.** Como una parte de contenido `input_image` junto con `input_text`.

### 5. El modelo multimodal afirma con seguridad que leyó el número de serie en una etiqueta borrosa. La app debe guardar ese valor en una base de datos. ¿Qué enfoque es más adecuado?

- **A.** Aceptar el texto porque el modelo multimodal responde con confianza.
- **B.** Usar Content Understanding con un campo numero_serie y revisar score y ubicación.
- **C.** Generar una imagen nueva con un número de serie más claro.
- **D.** Usar Speech recognition para convertir la etiqueta en texto.

### 6. Diseñas un custom analyzer para facturas de Luma. ¿Qué DOS conceptos de Content Understanding debes incluir para obtener datos integrables? Selecciona DOS respuestas.

- **A.** Un schema con campos, tipos y descripciones en lenguaje natural.
- **B.** Un prompt para que el usuario final elija manualmente cada campo.
- **C.** Métodos de campo como extract, generate o classify según el tipo de valor.
- **D.** Una llamada a SpeechSynthesizer para convertir los campos en audio.

### 7. En Content Understanding, analizas una factura escaneada. Primero obtienes líneas de texto; luego tablas y párrafos; finalmente campos como total y fecha. ¿Cuál es la secuencia correcta de analyzers?

- **A.** Image generation, Speech SDK y TextAnalyticsClient.
- **B.** Read, Layout y un analyzer de dominio o custom.
- **C.** Web search, code interpreter y MCP.
- **D.** Classification, detection y segmentation.

### 8. En una foto de etiqueta, el campo `estado_equipo` debe ser solo `sin_danos` o `danado`. ¿Qué método de campo del schema usa mejor esa lista cerrada?

- **A.** extract, porque copia siempre cualquier palabra visible.
- **B.** generate, porque redacta un resumen libre del equipo.
- **C.** read, porque OCR decide el significado de cada valor.
- **D.** classify, porque elige entre opciones definidas en enum.

### 9. Luma quiere analizar miles de llamadas grabadas para obtener motivo, sentimiento y compromiso del agente sin escucharlas manualmente. ¿Qué solución encaja mejor?

- **A.** Un analyzer de audio de Content Understanding con campos classify y generate.
- **B.** Un modelo de image generation con prompt de post-call analytics.
- **C.** Un prompt visual con input_image para cada llamada.
- **D.** Solo OCR/Read, porque las llamadas contienen palabras.

### 10. En extraer_factura.py, después de `poller = client.begin_analyze(...)`, el código llama a `poller.result()`. ¿Por qué es necesario?

- **A.** Porque begin_analyze solo inicia una operación asíncrona y hay que esperar el resultado.
- **B.** Porque result convierte el texto extraído en audio con una neural voice.
- **C.** Porque result cambia automáticamente de prebuilt-invoice a prebuilt-receipt.
- **D.** Porque result elimina la necesidad de validar campos y confidence scores.
