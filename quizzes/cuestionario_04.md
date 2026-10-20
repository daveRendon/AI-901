# Cuestionario 4 · AI Agents con Microsoft Foundry

> **Sección:** 5 · **Lecciones:** 20–24 · **Preguntas:** 10 · **Tiempo sugerido:** 15 minutos

Preguntas de escenario sobre agentes en Microsoft Foundry: diseño, creación en el portal, cliente Python y validación de comportamiento.

Responde sin consultar tus notas. Cuando termines, compara con [las respuestas y explicaciones](cuestionario_04_respuestas.md).

---

### 1. Luma quiere que un sistema responda si un router específico tiene garantía. El sistema debe buscar la política oficial, decidir si necesita más datos y responder dentro de límites definidos. ¿Qué describe mejor esa solución?

- **A.** Un modelo desplegado, porque recibe tokens y genera tokens sin herramientas.
- **B.** Una aplicación tradicional, porque el desarrollador programa cada paso y cada llamada.
- **C.** Un agent, porque combina modelo, instrucciones y tools para realizar tareas en nombre del usuario.
- **D.** Un índice de conocimiento, porque almacena documentos de políticas.

### 2. Estás diseñando las instrucciones de luma-soporte-agent antes de crearlo. ¿Qué DOS reglas pertenecen a esas instrucciones según el curso? Selecciona DOS respuestas.

- **A.** Para garantías o políticas, usar siempre file search sobre documentos de Luma.
- **B.** Confirmar reembolsos cuando el cliente ya proporcionó el número de cuenta.
- **C.** Citar el documento usado y decirlo si la información no está disponible.
- **D.** Pedir datos de tarjeta para validar la identidad antes de responder.

### 3. Un agent de Luma solo debe informar políticas internas almacenadas en documentos. El equipo propone agregar MCP para crear tickets y aprobar reembolsos. ¿Qué control aplica mejor el principio de mínimo privilegio?

- **A.** Habilitar todas las tools para evitar limitar al agent.
- **B.** Empezar con file search y agregar acciones solo si existen aprobaciones y permisos controlados.
- **C.** Usar web search porque puede encontrar información actual sobre cualquier política.
- **D.** Mover todas las reglas al prompt del usuario para que el cliente decida.

### 4. En el portal, ya configuraste gpt-5-mini con instrucciones y subiste politicas_luma.docx como file search. Quieres convertir esa configuración en un agent con nombre propio para usarlo después desde código. ¿Qué acción sigue?

- **A.** Abrir web search y guardar la consulta como fuente de conocimiento.
- **B.** Copiar las instrucciones en cada llamada de la aplicación cliente.
- **C.** Cambiar el deployment a un modelo de image generation.
- **D.** Seleccionar Save as agent y nombrarlo luma-soporte-agent.

### 5. Después de guardar la versión 1 de luma-soporte-agent, un evaluador pregunta “¿Cubren routers de otra marca?”. Los documentos de Luma no contienen esa política. ¿Cuál es el comportamiento esperado?

- **A.** Decir que no lo sabe con base en los documentos disponibles.
- **B.** Responder con una práctica común de la industria de routers.
- **C.** Confirmar un reemplazo si el cliente proporciona número de serie.
- **D.** Buscar la respuesta en la web pública aunque sea una política interna.

### 6. Revisa este cliente Python para un agent: usa AIProjectClient, get_openai_client y client.responses.create(...). ¿Qué DOS afirmaciones son correctas para consumir luma-soporte-agent? Selecciona DOS respuestas.

- **A.** Puede autenticarse con una API key del project igual que un endpoint de modelo simple.
- **B.** agent_reference identifica el nombre y la versión del agent.
- **C.** El cliente debe reenviar model e instructions en cada turno.
- **D.** get_openai_client envía la pregunta final al agent.
- **E.** conversations.create permite mantener el historial en el servicio.

### 7. En agente_luma.py, ¿qué línea es la que realmente envía la pregunta del cliente al agent según el curso?

- **A.** project = AIProjectClient(endpoint=..., credential=DefaultAzureCredential())
- **B.** client = project.get_openai_client()
- **C.** response = client.responses.create(input=pregunta, extra_body=AGENTE, ...)
- **D.** conversation = client.conversations.create()

### 8. El equipo agregó una instrucción nueva y guardó la versión 2 del agent. La aplicación sigue usando agent_reference con version "1". ¿Qué ocurrirá al ejecutar la aplicación sin cambios?

- **A.** La aplicación fallará porque solo puede existir una versión activa del agent.
- **B.** La aplicación usará automáticamente la versión más reciente.
- **C.** La aplicación deberá reenviar las instrucciones nuevas en input.
- **D.** La aplicación seguirá usando el comportamiento de la versión 1 hasta cambiar la versión en el código.

### 9. Una respuesta del agent sobre garantías suena correcta, pero no incluye cita ni evidencia de haber llamado a file search. ¿Cuál es la mejor forma de validarla?

- **A.** Aceptar la respuesta porque el texto coincide con lo esperado.
- **B.** Revisar trazas, response.output y citas para confirmar la llamada a file search.
- **C.** Pedir al cliente que confirme si la política le parece razonable.
- **D.** Agregar web search para que la respuesta tenga más contexto.

### 10. Luma quiere que el agent prepare una solicitud de reembolso por cobro duplicado, pero que nadie cobre ni prometa nada hasta que facturación revise el caso. ¿Qué patrón es el más adecuado?

- **A.** Aprobación humana antes de ejecutar una acción con impacto.
- **B.** Permitir siempre la tool de pagos para reducir fricción.
- **C.** Usar solo un prompt largo para sustituir la revisión de facturación.
- **D.** Desactivar guardrails para que el agent siga la intención del usuario.
