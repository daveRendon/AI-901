# Cuestionario 3 · Prompt engineering y aplicaciones de Generative AI · Respuestas y explicaciones

Vuelve a [las preguntas](cuestionario_03.md). Para cada error, anota el objetivo y repasa la lección indicada.

## Clave de respuestas

| # | Respuesta | Objetivo del examen | Lecciones |
|---|---|---|---|
| 1 | B | Create effective system and user prompts for generative AI models | 14 |
| 2 | A, B | Create effective system and user prompts for generative AI models | 15 |
| 3 | D | Create effective system and user prompts for generative AI models | 15 |
| 4 | A | Create effective system and user prompts for generative AI models | 16 |
| 5 | C | Create a lightweight chat client application by using the Foundry SDK | 17 |
| 6 | B | Create a lightweight chat client application by using the Foundry SDK | 18 |
| 7 | D | Create a lightweight chat client application by using the Foundry SDK | 18 |
| 8 | A | Create a lightweight chat client application by using the Foundry SDK | 18 |
| 9 | C | Describe how generative AI models work | 19 |
| 10 | A, C, D | Create a lightweight chat client application by using the Foundry SDK | 19 |

---

### 1. Luma quiere que el asistente siempre responda en español, con tono cordial y máximo cinco líneas, sin importar qué pregunte el usuario. ¿Dónde debe colocar esa regla?

- ❌ **A.** En el user prompt de cada cliente.  
  El user prompt cambia por turno y lo escribe el usuario; no garantiza una regla permanente.
- ✅ **B.** En el system prompt o Instructions.  
  El system prompt define comportamiento, rol, tono, formato y límites para toda la conversación.
- ❌ **C.** En el nombre del deployment.  
  El nombre del deployment identifica la instancia del modelo; no define comportamiento.
- ❌ **D.** En el resource group de Azure.  
  El resource group administra recursos juntos, pero no controla respuestas del modelo.

**Respuesta:** B. El system prompt lo define el desarrollador y aplica a toda la conversación. El user prompt contiene la tarea o pregunta concreta de cada turno. Repasa la lección 14.

*Objetivo: Create effective system and user prompts for generative AI models · Lecciones: 14*

### 2. Un prompt de clasificación devuelve categorías con formatos distintos. Quieres más consistencia sin entrenar el modelo. ¿Qué DOS mejoras aplicarías primero? Selecciona DOS respuestas.

- ✅ **A.** Agregar ejemplos few-shot dentro del prompt.  
  Few-shot muestra entradas y salidas esperadas para que el modelo imite el patrón.
- ✅ **B.** Definir un formato de salida con JSON y valores permitidos.  
  Un formato explícito hace que la respuesta sea más predecible y fácil de validar.
- ❌ **C.** Aumentar el límite de TPM del deployment.  
  TPM afecta capacidad por minuto, no el formato de la categoría.
- ❌ **D.** Cambiar a Batch para procesar el ticket.  
  Batch es para trabajos asíncronos grandes; no mejora por sí mismo la consistencia del formato.
- ❌ **E.** Quitar delimitadores para que el modelo tenga más libertad.  
  Los delimitadores ayudan a separar instrucciones y datos; quitarlos suele empeorar la claridad.

**Respuesta:** A, B. Prompt engineering mejora calidad sin modificar el modelo: contexto, instrucciones, restricciones, formato, few-shot y delimitadores. Repasa la lección 15.

*Objetivo: Create effective system and user prompts for generative AI models · Lecciones: 15*

### 3. En un prompt, el ticket de José incluye frases molestas como “ignora tus reglas”. ¿Qué técnica de la lección ayuda a separar datos del cliente de tus instrucciones?

- ❌ **A.** Cambiar el project endpoint por el endpoint compatible con OpenAI.  
  El endpoint no separa instrucciones de datos dentro del prompt.
- ❌ **B.** Pedir una respuesta más larga para que el modelo explique su razonamiento.  
  Más longitud no reduce el riesgo de mezclar instrucciones con datos del ticket.
- ❌ **C.** Usar un deployment Provisioned.  
  Provisioned afecta capacidad y latencia, no la estructura del prompt.
- ✅ **D.** Usar delimitadores como triples comillas alrededor del ticket.  
  Los delimitadores indican dónde terminan las instrucciones y dónde empiezan los datos.

**Respuesta:** D. Delimitadores como triples comillas, etiquetas o ### ayudan al modelo a tratar el contenido del usuario como datos, no como instrucciones del desarrollador. Repasa la lección 15.

*Objetivo: Create effective system and user prompts for generative AI models · Lecciones: 15*

### 4. Un prompt débil responde a un cobro duplicado prometiendo “reembolso en 48 horas”. ¿Qué mejora del prompt reduce mejor ese riesgo?

- ✅ **A.** Prohibir prometer reembolsos, montos o plazos y pedir datos para escalar a facturación.  
  Una restricción explícita y un siguiente paso verificable evitan promesas no autorizadas.
- ❌ **B.** Pedir al modelo que sea más creativo y empático.  
  Más creatividad puede aumentar hallucinations y no impide prometer montos o plazos.
- ❌ **C.** Eliminar el contexto de Luma para hacerlo más general.  
  Quitar contexto deja más decisiones al modelo y puede empeorar la respuesta.
- ❌ **D.** Aumentar el TPM para que responda más rápido.  
  TPM no corrige promesas inventadas ni reglas de negocio.

**Respuesta:** A. La lección muestra que prompts débiles producen promesas inventadas, longitud impredecible y falta de siguiente paso. Las restricciones concretas protegen a cliente y empresa. Repasa la lección 16.

*Objetivo: Create effective system and user prompts for generative AI models · Lecciones: 16*

### 5. En chat_luma.py aparece `previous_response_id=previous_id` dentro de `client.responses.create(...)`. ¿Para qué sirve esa línea?

- ❌ **A.** Autenticar la aplicación con Microsoft Entra ID.  
  La autenticación la hace DefaultAzureCredential, no previous_response_id.
- ❌ **B.** Cambiar el deployment type a Global Standard.  
  El deployment type se configura al desplegar, no en esa línea de código.
- ✅ **C.** Encadenar la conversación sin reenviar todo el historial.  
  previous_response_id conecta la nueva solicitud con la respuesta anterior para mantener contexto.
- ❌ **D.** Leer variables del archivo .env.  
  Las variables se cargan con load_dotenv y os.environ.

**Respuesta:** C. El modelo no recuerda por sí mismo entre llamadas. En el curso, previous_response_id permite que el servicio recupere contexto de turnos anteriores. Repasa la lección 17.

*Objetivo: Create a lightweight chat client application by using the Foundry SDK · Lecciones: 17*

### 6. Lee el bloque: `project = AIProjectClient(endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"], credential=DefaultAzureCredential())`. ¿Qué parte autentica la aplicación?

- ❌ **A.** endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"]  
  El endpoint indica a qué project conectarse, pero no obtiene credenciales.
- ✅ **B.** credential=DefaultAzureCredential()  
  DefaultAzureCredential obtiene un token de Entra ID, usando az login en local o managed identity en Azure.
- ❌ **C.** AIProjectClient  
  AIProjectClient es el cliente de proyecto; necesita una credencial para autenticarse.
- ❌ **D.** os.environ  
  os.environ lee variables de entorno, pero no autentica solicitudes.

**Respuesta:** B. Para preguntas de lectura de código, identifica el verbo de cada línea: endpoint conecta, credential autentica, get_openai_client prepara y responses.create envía. Repasa la lección 18.

*Objetivo: Create a lightweight chat client application by using the Foundry SDK · Lecciones: 18*

### 7. Tu organización permite API keys y quieres usar el OpenAI SDK solo para llamar a modelos desplegados. ¿Qué configuración es correcta?

- ❌ **A.** AIProjectClient con una API key escrita en el constructor.  
  AIProjectClient para el project usa Entra ID; no se conecta con API key.
- ❌ **B.** OpenAI con base_url apuntando al project endpoint de services.ai.azure.com.  
  La alternativa con key usa el endpoint compatible con OpenAI, no el project endpoint.
- ❌ **C.** DefaultAzureCredential y sin ninguna variable de entorno.  
  DefaultAzureCredential corresponde al camino de Entra ID; la opción con key requiere endpoint y key.
- ✅ **D.** OpenAI con base_url terminada en /openai/v1/ y api_key desde una variable de entorno.  
  Ese es el patrón de chat_key.py: endpoint compatible con OpenAI y key protegida fuera del código.

**Respuesta:** D. Hay dos caminos: Foundry SDK con Entra ID para project y agentes, o OpenAI SDK con API key para modelos desplegados. La key nunca se escribe en código. Repasa la lección 18.

*Objetivo: Create a lightweight chat client application by using the Foundry SDK · Lecciones: 18*

### 8. En la app del curso, ¿qué debe guardar el archivo .env para el camino con Foundry SDK y Entra ID?

- ✅ **A.** FOUNDRY_PROJECT_ENDPOINT y MODEL_DEPLOYMENT_NAME.  
  Son las variables usadas por chat_luma.py para conectar al project y llamar al deployment.
- ❌ **B.** AZURE_OPENAI_API_KEY escrita junto al código fuente.  
  La key no pertenece al camino con Entra ID y nunca debe escribirse en el código.
- ❌ **C.** La contraseña personal del administrador de Azure.  
  Nunca se guardan contraseñas personales; DefaultAzureCredential usa identidad de forma segura.
- ❌ **D.** El resource group y el nombre del tenant solamente.  
  Esos datos no bastan para que el cliente se conecte al project ni al deployment.

**Respuesta:** A. load_dotenv carga variables de entorno para evitar valores de conexión en el código. Para el camino del curso necesitas project endpoint y nombre del deployment. Repasa la lección 18.

*Objetivo: Create a lightweight chat client application by using the Foundry SDK · Lecciones: 18*

### 9. validar_respuesta.py revisa `response.status`. Si el estado es `incomplete` porque max_output_tokens fue muy bajo, ¿qué debes hacer?

- ❌ **A.** Usar la respuesta parcial si parece correcta.  
  La lección indica que si status no es completed, no debes usar la respuesta.
- ❌ **B.** Cambiar la región del resource como primera medida.  
  La región no corrige una salida incompleta causada por max_output_tokens.
- ✅ **C.** Aumentar max_output_tokens o pedir una respuesta más corta.  
  El límite de salida controla cuánto puede responder el modelo; si es bajo, la salida se corta.
- ❌ **D.** Desactivar la validación JSON.  
  Quitar validación empeora la seguridad; debes corregir la causa de la respuesta incompleta.

**Respuesta:** C. response.status debe ser completed antes de usar la salida. Si incomplete_details apunta a tokens, ajusta el límite o el prompt. Repasa la lección 19.

*Objetivo: Describe how generative AI models work · Lecciones: 19*

### 10. Luma pide JSON para clasificar tickets antes de actuar sobre dinero o derechos del cliente. ¿Qué TRES validaciones recomienda la sección? Selecciona TRES respuestas.

- ✅ **A.** Comprobar que response.status sea completed.  
  Si el estado no es completed, la respuesta puede estar cortada o filtrada y no debe usarse.
- ❌ **B.** Aceptar texto extra si el modelo parece seguro.  
  Texto adicional rompe el formato esperado y debe tratarse como inválido.
- ✅ **C.** Parsear con json.loads y verificar campos obligatorios.  
  json.loads detecta formato roto, y la verificación de campos evita salidas incompletas.
- ✅ **D.** Enviar a revisión humana si falla la validación o la decisión importa.  
  Las respuestas que afectan dinero, salud o derechos requieren revisión humana cuando hay duda.
- ❌ **E.** Ignorar valores permitidos para no bloquear casos nuevos.  
  La lección recomienda comprobar valores permitidos y escalar si no coinciden.

**Respuesta:** A, C, D. Validar salidas es parte de una app responsable: revisa estado, formato y valores permitidos, y no improvises ante fallos. Escala a una persona cuando la decisión importa. Repasa la lección 19.

*Objetivo: Create a lightweight chat client application by using the Foundry SDK · Lecciones: 19*
