# Práctica 4 · Text analysis y Azure Language

- **Sección:** 6 · Text Analysis y Azure Language
- **Lecciones:** 25–29
- **Duración estimada:** 50 minutos
- **Nivel:** Intermedio
- **Habilidades medidas:**
  - `Implement AI solutions for text and speech by using Foundry`
  - `Identify AI workloads`

## Objetivo

Compararás dos enfoques de text analysis: un modelo general con prompts y Azure Language en Foundry Tools. Extraerás keywords, entidades, sentimiento, resumen, idioma y PII, y decidirás cuándo usar confidence scores.

## Lo que vas a construir

Ejecuciones de [analizar_ticket.py](../analizar_ticket.py) con tres tickets y [lenguaje_luma.py](../lenguaje_luma.py) con detección de idioma y PII.

## Requisitos

- [ ] Práctica 2 completada: `.env` con `FOUNDRY_PROJECT_ENDPOINT` y `MODEL_DEPLOYMENT_NAME`.
- [ ] Project `luma-soporte` con `gpt-5-mini` activo.
- [ ] Acceso a **Build, Services, Azure Language**.
- [ ] Endpoint y key de Azure Language para `LANGUAGE_ENDPOINT` y `LANGUAGE_KEY`.
- [ ] Archivos [ticket_8413.txt](../data/ticket_8413.txt), [ticket_positivo.txt](../data/ticket_positivo.txt), [ticket_ingles.txt](../data/ticket_ingles.txt), [etiqueta_aleman.txt](../data/etiqueta_aleman.txt).
- [ ] Paquete `azure-ai-textanalytics` instalado por `requirements.txt`.

## Costo y limpieza

Las llamadas al modelo consumen tokens y Azure Language cobra por uso. Mantén muestras pequeñas. Conserva el recurso y variables para prácticas posteriores; no guardes textos con PII sin redactar.

## Pasos

### Parte 1 · Reconocer las cuatro técnicas

1. Abre [ticket_8413.txt](../data/ticket_8413.txt).
2. Identifica keywords probables: router Luma X300, desconexiones nocturnas, factura de agosto, internet estable.
3. Identifica entidades: José Pérez, 3 de septiembre, Luma X300, Ciudad de México.
4. Identifica sentimiento: negativo por “Estoy muy molesto”.
5. Redacta un resumen de una oración.
6. Recuerda la diferencia: entidades son quién, qué, dónde y cuándo; keywords son temas principales.
7. ✅ Punto de control: puedes explicar qué salida esperas antes de ejecutar cualquier servicio.

### Parte 2 · Probar text analysis en el playground

1. Abre el playground de `gpt-5-mini`.
2. En **Instructions**, escribe: `Eres un asistente que analiza textos de soporte técnico.`
3. Inicia **New chat**.
4. Pega el texto de [ticket_8413.txt](../data/ticket_8413.txt).
5. Pide: `Resume este ticket en una sola oración.`
6. Ahora pide: `Extrae keywords, entidades con tipo, sentimiento y resumen. Responde solo con JSON.`
7. Inicia otro chat nuevo y envía exactamente el mismo prompt.
8. Compara keywords y redacción del resumen.
9. Observa que lo esencial se mantiene, pero puede haber variación.
10. ✅ Punto de control: viste flexibilidad y variación del modelo general.

### Parte 3 · Ejecutar `analizar_ticket.py`

1. Abre [analizar_ticket.py](../analizar_ticket.py).
2. Revisa que usa `AIProjectClient` y `DefaultAzureCredential`.
3. Revisa el schema JSON solicitado: `keywords`, `entidades`, `sentimiento`, `resumen`.
4. Desde la raíz, ejecuta:
   ```powershell
   python analizar_ticket.py
   ```
5. Revisa que imprima JSON con acentos correctos.
6. Si falla `json.loads`, refuerza el prompt para pedir solo JSON o valida manualmente.
7. ✅ Punto de control: tienes JSON con las cuatro técnicas en una llamada.

### Parte 4 · Probar otros tickets

1. En [analizar_ticket.py](../analizar_ticket.py), localiza la línea que lee `ticket_8413.txt`.
2. Cambia temporalmente a `ticket_positivo.txt`.
3. Ejecuta el programa.
4. Esperado: sentimiento `positive` y resumen de satisfacción.
5. Cambia temporalmente a `ticket_ingles.txt`.
6. Ejecuta el programa.
7. Observa si el resumen sale en inglés; si necesitas español fijo, agrega esa restricción a las instrucciones.
8. Regresa el archivo a `ticket_8413.txt` si quieres conservar el estado original.
9. ✅ Punto de control: entiendes que un modelo general puede analizar otros idiomas, pero debes pedir el idioma de salida.

### Parte 5 · Abrir Azure Language en Foundry Tools

1. En el project, entra a **Build**.
2. Abre **Services**.
3. Selecciona **Azure Language**.
4. Abre **Language detection**.
5. Prueba una muestra del portal con **Detect**.
6. Pega el contenido de [etiqueta_aleman.txt](../data/etiqueta_aleman.txt).
7. Ejecuta **Detect**.
8. Esperado: German, código `de`, con confidence score alto.
9. Cambia a **Text PII Redaction**.
10. Pega un texto con nombre y correo de José.
11. Ejecuta y revisa texto redactado, categorías y scores.
12. ✅ Punto de control: Azure Language devuelve estructura fija y confidence scores.

### Parte 6 · Copiar configuración desde Code

1. En el playground de Azure Language, abre la pestaña **Code**.
2. Copia el endpoint de tu recurso.
3. Copia la key si usarás `AzureKeyCredential`.
4. Completa `.env`:
   ```env
   LANGUAGE_ENDPOINT=https://<recurso>.cognitiveservices.azure.com/
   LANGUAGE_KEY=<tu-key>
   ```
5. No pegues la key en capturas ni en archivos fuera de `.env`.
6. Si tu organización prefiere Entra ID, recuerda que `TextAnalyticsClient` también acepta `DefaultAzureCredential` con roles adecuados.
7. ✅ Punto de control: tu `.env` contiene Language endpoint y key, sin secretos en el código.

### Parte 7 · Ejecutar `lenguaje_luma.py`

1. Abre [lenguaje_luma.py](../lenguaje_luma.py).
2. Revisa `TextAnalyticsClient`.
3. Revisa `detect_language(docs)`.
4. Revisa `recognize_pii_entities(docs, language="es")`.
5. Ejecuta:
   ```powershell
   python lenguaje_luma.py
   ```
6. Esperado: idioma `Spanish`, código `es`, score cercano a 1.0.
7. Esperado: texto redactado con asteriscos para nombre y correo.
8. Esperado: entidades PII con categoría y score.
9. Ejecuta una segunda vez.
10. Compara: con la misma entrada y versión, el resultado debe ser consistente.
11. ✅ Punto de control: contrastaste estructura y consistencia frente al modelo general.

### Parte 8 · Interpretar confidence scores

1. Revisa los scores que imprime `lenguaje_luma.py`.
2. Define un umbral de laboratorio, por ejemplo 0.8.
3. Si un score está por encima, procesa o redacta automáticamente.
4. Si está por debajo, envía a revisión o redacta de forma conservadora si se trata de PII.
5. No interpretes 0.9 como “90 % de verdad”; es seguridad del modelo en esa predicción.
6. No compares scores entre Azure Language y otros servicios.
7. ✅ Punto de control: puedes justificar un umbral según el riesgo del caso.

### Parte 9 · Comparar enfoques

1. Anota cuándo usar modelo general: varias tareas, lenguaje natural, conversación y formato flexible.
2. Anota cuándo usar Azure Language: esquema fijo, consistencia, confidence scores y PII regulada.
3. Para Luma, decide qué usarías para resumir un ticket y redactar respuesta.
4. Para Luma, decide qué usarías para redactar PII en miles de transcripciones.
5. ✅ Punto de control: la decisión no es “uno mejor que otro”, sino requisito contra capacidad.

## Retos opcionales

- Agrega al prompt de `analizar_ticket.py`: “el resumen siempre en español”.
- Cambia el documento de `lenguaje_luma.py` por el contenido de `ticket_8413.txt`.
- Diseña una regla: PII con score menor a 0.8 va a revisión humana.

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| JSON inválido en `analizar_ticket.py` | El modelo agregó texto fuera del JSON | Refuerza “SOLO JSON”, valida y considera structured outputs. |
| Variación entre ejecuciones | Comportamiento normal de modelo generativo | Usa prompts más específicos o Azure Language para estructura fija. |
| `LANGUAGE_KEY` no existe | `.env` incompleto | Copia endpoint y key desde la pestaña **Code**. |
| 401 en Azure Language | Key o endpoint no corresponden | Verifica que ambos sean del mismo recurso. |
| 403 en Azure Language con Entra ID | Falta rol de datos | Asigna el rol adecuado sobre el recurso. |
| Score medio en PII | Incertidumbre del servicio | Revisión humana o redacción conservadora según el riesgo. |
| Esperabas resumen de Azure Language | En esta demo se usan Language detection y PII | Usa modelo general para resumen conversacional o una capacidad compatible del portal. |

## Comprueba lo aprendido

1. Tu pipeline debe redactar correos en miles de tickets con el mismo esquema y scores. ¿Qué enfoque eliges?
2. El modelo general devuelve keywords distintas en dos ejecuciones. ¿Es necesariamente un fallo?
3. Azure Language detecta PII con score 0.62 y tu umbral es 0.8. ¿Qué debería hacer la aplicación antes de guardar el texto?

## Siguiente paso

Continúa con [Práctica 5 · Speech y audio](practica_05_speech_y_audio.md).
