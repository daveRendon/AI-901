# Cuestionario 4 · AI Agents con Microsoft Foundry · Respuestas y explicaciones

Vuelve a [las preguntas](cuestionario_04.md). Para cada error, anota el objetivo y repasa la lección indicada.

## Clave de respuestas

| # | Respuesta | Objetivo del examen | Lecciones |
|---|---|---|---|
| 1 | C | Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction | 20 |
| 2 | A, C | Create and test a single-agent solution in the Foundry portal | 21 |
| 3 | B | Create and test a single-agent solution in the Foundry portal | 21 |
| 4 | D | Create and test a single-agent solution in the Foundry portal | 22 |
| 5 | A | Create and test a single-agent solution in the Foundry portal | 22 |
| 6 | B, E | Create a lightweight client application for an agent | 23 |
| 7 | C | Create a lightweight client application for an agent | 23 |
| 8 | D | Create a lightweight client application for an agent | 23 |
| 9 | B | Create and test a single-agent solution in the Foundry portal | 24 |
| 10 | A | Create and test a single-agent solution in the Foundry portal | 21, 24 |

---

### 1. Luma quiere que un sistema responda si un router específico tiene garantía. El sistema debe buscar la política oficial, decidir si necesita más datos y responder dentro de límites definidos. ¿Qué describe mejor esa solución?

- ❌ **A.** Un modelo desplegado, porque recibe tokens y genera tokens sin herramientas.  
  El modelo por sí solo genera texto, pero no recuerda entre llamadas ni usa tools para buscar o actuar.
- ❌ **B.** Una aplicación tradicional, porque el desarrollador programa cada paso y cada llamada.  
  Una aplicación puede usar el modelo, pero aquí el sistema decide los pasos y qué tool usar para cumplir un objetivo.
- ✅ **C.** Un agent, porque combina modelo, instrucciones y tools para realizar tareas en nombre del usuario.  
  El agent persigue un objetivo, decide pasos y usa tools dentro de límites definidos.
- ❌ **D.** Un índice de conocimiento, porque almacena documentos de políticas.  
  El índice aporta knowledge, pero no decide ni responde por sí mismo como un agent.

**Respuesta:** C. En la lección 20 se separan modelo, aplicación y agent. Si el sistema decide qué pasos seguir y qué tool usar para cumplir un objetivo, el concepto correcto es agent, no solo modelo ni aplicación. Repasa la lección 20.

*Objetivo: Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction · Lecciones: 20*

### 2. Estás diseñando las instrucciones de luma-soporte-agent antes de crearlo. ¿Qué DOS reglas pertenecen a esas instrucciones según el curso? Selecciona DOS respuestas.

- ✅ **A.** Para garantías o políticas, usar siempre file search sobre documentos de Luma.  
  La instrucción obliga a usar file search para basar la respuesta en documentos de Luma.
- ❌ **B.** Confirmar reembolsos cuando el cliente ya proporcionó el número de cuenta.  
  El agente no debe prometer ni confirmar reembolsos; debe informar y escalar cuando corresponda.
- ✅ **C.** Citar el documento usado y decirlo si la información no está disponible.  
  Las instrucciones piden citar la fuente y admitir cuando los documentos no contienen la respuesta.
- ❌ **D.** Pedir datos de tarjeta para validar la identidad antes de responder.  
  El curso establece que el asistente no pide contraseñas ni datos de tarjeta.

**Respuesta:** A, C. Las instrucciones del agent definen rol, uso de tools, citas y límites. Para Luma, file search y citas reducen respuestas de memoria, mientras que reembolsos y datos sensibles están fuera de alcance. Repasa la lección 21.

*Objetivo: Create and test a single-agent solution in the Foundry portal · Lecciones: 21*

### 3. Un agent de Luma solo debe informar políticas internas almacenadas en documentos. El equipo propone agregar MCP para crear tickets y aprobar reembolsos. ¿Qué control aplica mejor el principio de mínimo privilegio?

- ❌ **A.** Habilitar todas las tools para evitar limitar al agent.  
  Dar más tools de las necesarias aumenta el riesgo de acciones incorrectas o no autorizadas.
- ✅ **B.** Empezar con file search y agregar acciones solo si existen aprobaciones y permisos controlados.  
  El curso recomienda empezar con knowledge y añadir acciones solo con controles como aprobación humana y mínimo privilegio.
- ❌ **C.** Usar web search porque puede encontrar información actual sobre cualquier política.  
  Las políticas internas deben venir de documentos o índices empresariales, no de internet.
- ❌ **D.** Mover todas las reglas al prompt del usuario para que el cliente decida.  
  Los límites deben estar en las instrucciones del agent, no depender del usuario.

**Respuesta:** B. Knowledge lee para responder; acciones cambian otros sistemas. Si el objetivo es informar políticas, file search es suficiente y las acciones requieren aprobación, identidad y permisos mínimos. Repasa la lección 21.

*Objetivo: Create and test a single-agent solution in the Foundry portal · Lecciones: 21*

### 4. En el portal, ya configuraste gpt-5-mini con instrucciones y subiste politicas_luma.docx como file search. Quieres convertir esa configuración en un agent con nombre propio para usarlo después desde código. ¿Qué acción sigue?

- ❌ **A.** Abrir web search y guardar la consulta como fuente de conocimiento.  
  Web search no convierte la configuración del playground en un agent.
- ❌ **B.** Copiar las instrucciones en cada llamada de la aplicación cliente.  
  Cuando guardas el agent, las instrucciones viven dentro del agent y el cliente no las reenvía.
- ❌ **C.** Cambiar el deployment a un modelo de image generation.  
  La tarea es de soporte conversacional con file search, no de generación de imágenes.
- ✅ **D.** Seleccionar Save as agent y nombrarlo luma-soporte-agent.  
  Save as agent crea un agent con nombre y versión a partir de la configuración del playground.

**Respuesta:** D. La lección 22 muestra el flujo: modelo, instructions, file search y luego Save as agent. Foundry crea luma-soporte-agent con versión y definición YAML. Repasa la lección 22.

*Objetivo: Create and test a single-agent solution in the Foundry portal · Lecciones: 22*

### 5. Después de guardar la versión 1 de luma-soporte-agent, un evaluador pregunta “¿Cubren routers de otra marca?”. Los documentos de Luma no contienen esa política. ¿Cuál es el comportamiento esperado?

- ✅ **A.** Decir que no lo sabe con base en los documentos disponibles.  
  Las instrucciones piden no inventar y reconocer cuando la información no está en los documentos.
- ❌ **B.** Responder con una práctica común de la industria de routers.  
  Responder de memoria o con conocimiento genérico rompe el grounding requerido.
- ❌ **C.** Confirmar un reemplazo si el cliente proporciona número de serie.  
  El agent no debe prometer reemplazos; además la pregunta está fuera de la política disponible.
- ❌ **D.** Buscar la respuesta en la web pública aunque sea una política interna.  
  Para políticas internas de Luma, la fuente correcta es el documento indexado, no web search.

**Respuesta:** A. Las pruebas de comportamiento incluyen preguntas cubiertas, exclusiones, temas fuera de alcance y casos sin información. El agent debe preferir una negativa honesta a una respuesta inventada. Repasa la lección 22.

*Objetivo: Create and test a single-agent solution in the Foundry portal · Lecciones: 22*

### 6. Revisa este cliente Python para un agent: usa AIProjectClient, get_openai_client y client.responses.create(...). ¿Qué DOS afirmaciones son correctas para consumir luma-soporte-agent? Selecciona DOS respuestas.

- ❌ **A.** Puede autenticarse con una API key del project igual que un endpoint de modelo simple.  
  El acceso al project y a sus agents requiere Microsoft Entra ID; la lección advierte desconfiar de API key.
- ✅ **B.** agent_reference identifica el nombre y la versión del agent.  
  La referencia incluye name, version y type para indicar qué agent usará la Responses API.
- ❌ **C.** El cliente debe reenviar model e instructions en cada turno.  
  En un agent, el modelo, las instrucciones y las tools viven dentro del agent guardado.
- ❌ **D.** get_openai_client envía la pregunta final al agent.  
  get_openai_client prepara la conexión; la solicitud se envía con responses.create.
- ✅ **E.** conversations.create permite mantener el historial en el servicio.  
  La conversation guarda el historial y el código envía su id en cada turno.

**Respuesta:** B, E. El cliente de la lección 23 usa AIProjectClient con DefaultAzureCredential, una conversation y responses.create con extra_body que contiene agent_reference. No envía model ni instructions porque ya pertenecen al agent. Repasa la lección 23.

*Objetivo: Create a lightweight client application for an agent · Lecciones: 23*

### 7. En agente_luma.py, ¿qué línea es la que realmente envía la pregunta del cliente al agent según el curso?

- ❌ **A.** project = AIProjectClient(endpoint=..., credential=DefaultAzureCredential())  
  Esa línea crea el cliente del project y configura la autenticación, pero no envía una pregunta.
- ❌ **B.** client = project.get_openai_client()  
  Esa línea obtiene el cliente compatible con OpenAI; solo prepara la conexión.
- ✅ **C.** response = client.responses.create(input=pregunta, extra_body=AGENTE, ...)  
  responses.create es la llamada que envía la entrada al agent mediante agent_reference.
- ❌ **D.** conversation = client.conversations.create()  
  Esa línea crea el historial, pero no ejecuta la respuesta del agent.

**Respuesta:** C. El tip de examen de la lección 23 indica que responses.create envía la solicitud. AIProjectClient, get_openai_client y conversations.create preparan identidad, conexión e historial. Repasa la lección 23.

*Objetivo: Create a lightweight client application for an agent · Lecciones: 23*

### 8. El equipo agregó una instrucción nueva y guardó la versión 2 del agent. La aplicación sigue usando agent_reference con version "1". ¿Qué ocurrirá al ejecutar la aplicación sin cambios?

- ❌ **A.** La aplicación fallará porque solo puede existir una versión activa del agent.  
  Las versiones permiten que varias aplicaciones sigan apuntando a versiones distintas.
- ❌ **B.** La aplicación usará automáticamente la versión más reciente.  
  El código referencia explícitamente nombre y versión; no cambia solo a la versión nueva.
- ❌ **C.** La aplicación deberá reenviar las instrucciones nuevas en input.  
  Las instrucciones viven dentro del agent, no en el input del cliente.
- ✅ **D.** La aplicación seguirá usando el comportamiento de la versión 1 hasta cambiar la versión en el código.  
  La lección muestra que apuntar a version 1 mantiene el comportamiento anterior aunque exista version 2.

**Respuesta:** D. Las versiones permiten probar cambios sin romper aplicaciones existentes. Para adoptar la nueva instrucción, el cliente debe cambiar agent_reference a la versión correspondiente. Repasa la lección 23.

*Objetivo: Create a lightweight client application for an agent · Lecciones: 23*

### 9. Una respuesta del agent sobre garantías suena correcta, pero no incluye cita ni evidencia de haber llamado a file search. ¿Cuál es la mejor forma de validarla?

- ❌ **A.** Aceptar la respuesta porque el texto coincide con lo esperado.  
  Una respuesta puede sonar correcta y aun así ser incorrecta si no usó la fuente adecuada.
- ✅ **B.** Revisar trazas, response.output y citas para confirmar la llamada a file search.  
  La lección 24 recomienda validar tools con trazas, response.output, citas y evaluations.
- ❌ **C.** Pedir al cliente que confirme si la política le parece razonable.  
  La validación debe basarse en fuentes y tool calls, no en opinión del cliente.
- ❌ **D.** Agregar web search para que la respuesta tenga más contexto.  
  La política de garantía debe venir del documento de Luma, no de la web pública.

**Respuesta:** B. El comportamiento correcto incluye usar file search antes de responder sobre políticas y citar el documento. En código, response.output puede mostrar elementos como file_search_call. Repasa la lección 24.

*Objetivo: Create and test a single-agent solution in the Foundry portal · Lecciones: 24*

### 10. Luma quiere que el agent prepare una solicitud de reembolso por cobro duplicado, pero que nadie cobre ni prometa nada hasta que facturación revise el caso. ¿Qué patrón es el más adecuado?

- ✅ **A.** Aprobación humana antes de ejecutar una acción con impacto.  
  Las acciones con impacto, como reembolsos, requieren aprobación previa y accountability.
- ❌ **B.** Permitir siempre la tool de pagos para reducir fricción.  
  Eso viola mínimo privilegio y aumenta el riesgo de acciones no autorizadas.
- ❌ **C.** Usar solo un prompt largo para sustituir la revisión de facturación.  
  Las instrucciones ayudan, pero no reemplazan controles para acciones de alto impacto.
- ❌ **D.** Desactivar guardrails para que el agent siga la intención del usuario.  
  Los guardrails protegen entradas y salidas; no deben desactivarse para acciones sensibles.

**Respuesta:** A. Las lecciones 21 y 24 conectan acciones con controles: mínimo privilegio, aprobaciones y supervisión humana. Para reembolsos, el agent prepara evidencia y escala, no decide solo. Repasa las lecciones 21 y 24.

*Objetivo: Create and test a single-agent solution in the Foundry portal · Lecciones: 21, 24*
