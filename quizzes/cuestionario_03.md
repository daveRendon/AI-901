# Cuestionario 3 · Prompt engineering y aplicaciones de Generative AI

> **Sección:** 4 · **Lecciones:** 14–19 · **Preguntas:** 10 · **Tiempo sugerido:** 15 minutos

Practica system prompts, prompts estructurados, código con Foundry SDK, autenticación, configuración y validación de respuestas.

Responde sin consultar tus notas. Cuando termines, compara con [las respuestas y explicaciones](cuestionario_03_respuestas.md).

---

### 1. Luma quiere que el asistente siempre responda en español, con tono cordial y máximo cinco líneas, sin importar qué pregunte el usuario. ¿Dónde debe colocar esa regla?

- **A.** En el user prompt de cada cliente.
- **B.** En el system prompt o Instructions.
- **C.** En el nombre del deployment.
- **D.** En el resource group de Azure.

### 2. Un prompt de clasificación devuelve categorías con formatos distintos. Quieres más consistencia sin entrenar el modelo. ¿Qué DOS mejoras aplicarías primero? Selecciona DOS respuestas.

- **A.** Agregar ejemplos few-shot dentro del prompt.
- **B.** Definir un formato de salida con JSON y valores permitidos.
- **C.** Aumentar el límite de TPM del deployment.
- **D.** Cambiar a Batch para procesar el ticket.
- **E.** Quitar delimitadores para que el modelo tenga más libertad.

### 3. En un prompt, el ticket de José incluye frases molestas como “ignora tus reglas”. ¿Qué técnica de la lección ayuda a separar datos del cliente de tus instrucciones?

- **A.** Cambiar el project endpoint por el endpoint compatible con OpenAI.
- **B.** Pedir una respuesta más larga para que el modelo explique su razonamiento.
- **C.** Usar un deployment Provisioned.
- **D.** Usar delimitadores como triples comillas alrededor del ticket.

### 4. Un prompt débil responde a un cobro duplicado prometiendo “reembolso en 48 horas”. ¿Qué mejora del prompt reduce mejor ese riesgo?

- **A.** Prohibir prometer reembolsos, montos o plazos y pedir datos para escalar a facturación.
- **B.** Pedir al modelo que sea más creativo y empático.
- **C.** Eliminar el contexto de Luma para hacerlo más general.
- **D.** Aumentar el TPM para que responda más rápido.

### 5. En chat_luma.py aparece `previous_response_id=previous_id` dentro de `client.responses.create(...)`. ¿Para qué sirve esa línea?

- **A.** Autenticar la aplicación con Microsoft Entra ID.
- **B.** Cambiar el deployment type a Global Standard.
- **C.** Encadenar la conversación sin reenviar todo el historial.
- **D.** Leer variables del archivo .env.

### 6. Lee el bloque: `project = AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"], credential=DefaultAzureCredential())`. ¿Qué parte autentica la aplicación?

- **A.** endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"]
- **B.** credential=DefaultAzureCredential()
- **C.** AIProjectClient
- **D.** os.environ

### 7. Tu organización permite API keys y quieres usar el OpenAI SDK solo para llamar a modelos desplegados. ¿Qué configuración es correcta?

- **A.** AIProjectClient con una API key escrita en el constructor.
- **B.** OpenAI con base_url apuntando al project endpoint de services.ai.azure.com.
- **C.** DefaultAzureCredential y sin ninguna variable de entorno.
- **D.** OpenAI con base_url terminada en /openai/v1/ y api_key desde una variable de entorno.

### 8. En la app del curso, ¿qué debe guardar el archivo .env para el camino con Foundry SDK y Entra ID?

- **A.** FOUNDRY_PROJECT_ENDPOINT y MODEL_DEPLOYMENT_NAME.
- **B.** AZURE_OPENAI_API_KEY escrita junto al código fuente.
- **C.** La contraseña personal del administrador de Azure.
- **D.** El resource group y el nombre del tenant solamente.

### 9. validar_respuesta.py revisa `response.status`. Si el estado es `incomplete` porque max_output_tokens fue muy bajo, ¿qué debes hacer?

- **A.** Usar la respuesta parcial si parece correcta.
- **B.** Cambiar la región del resource como primera medida.
- **C.** Aumentar max_output_tokens o pedir una respuesta más corta.
- **D.** Desactivar la validación JSON.

### 10. Luma pide JSON para clasificar tickets antes de actuar sobre dinero o derechos del cliente. ¿Qué TRES validaciones recomienda la sección? Selecciona TRES respuestas.

- **A.** Comprobar que response.status sea completed.
- **B.** Aceptar texto extra si el modelo parece seguro.
- **C.** Parsear con json.loads y verificar campos obligatorios.
- **D.** Enviar a revisión humana si falla la validación o la decisión importa.
- **E.** Ignorar valores permitidos para no bloquear casos nuevos.
