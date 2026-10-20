# Cuestionario 2 · Microsoft Foundry: modelos y deployments · Respuestas y explicaciones

Vuelve a [las preguntas](cuestionario_02.md). Para cada error, anota el objetivo y repasa la lección indicada.

## Clave de respuestas

| # | Respuesta | Objetivo del examen | Lecciones |
|---|---|---|---|
| 1 | C | Deploy a model and interact with it in the Foundry portal | 9 |
| 2 | A | Deploy a model and interact with it in the Foundry portal | 9 |
| 3 | D | Identify an appropriate AI model, based on capabilities | 10 |
| 4 | B, C | Identify an appropriate AI model, based on capabilities | 10 |
| 5 | B | Identify appropriate model deployment options and configuration parameters | 11 |
| 6 | A, B, C | Identify appropriate model deployment options and configuration parameters | 11 |
| 7 | A | Identify appropriate model deployment options and configuration parameters | 11 |
| 8 | C | Deploy a model and interact with it in the Foundry portal | 12 |
| 9 | D | Deploy a model and interact with it in the Foundry portal | 13 |
| 10 | D | Identify appropriate model deployment options and configuration parameters | 13 |

---

### 1. Luma quiere aislar el trabajo de soporte y facturación dentro del mismo Foundry resource, con archivos y evaluaciones separados. ¿Qué debe crear?

- ❌ **A.** Dos tenants de Microsoft Entra ID.  
  El tenant representa la organización; no es el mecanismo normal para aislar equipos dentro de un resource.
- ❌ **B.** Dos subscriptions para el mismo equipo.  
  La subscription es límite de facturación y cuota, pero el escenario pide aislar espacios de trabajo.
- ✅ **C.** Varios Foundry projects dentro del resource.  
  Los projects aíslan agentes, archivos, índices y evaluaciones dentro de un Foundry resource.
- ❌ **D.** Un solo deployment con más TPM.  
  Un deployment es una instancia de modelo; no separa archivos ni evaluaciones de equipos.

**Respuesta:** C. La jerarquía es tenant, subscription, resource group, Foundry resource y project. Para aislar equipos dentro del mismo resource, usa varios projects. Repasa la lección 9.

*Objetivo: Deploy a model and interact with it in the Foundry portal · Lecciones: 9*

### 2. ¿Cuál descripción distingue mejor un Foundry resource de un Foundry project?

- ✅ **A.** El resource es infraestructura con endpoints y cuota; el project es el espacio de trabajo de desarrollo.  
  El resource vive en Azure y aloja endpoints y deployments; el project agrupa trabajo de la solución.
- ❌ **B.** El resource contiene solo archivos; el project contiene la subscription.  
  La subscription está por encima del resource, y los archivos pertenecen al project.
- ❌ **C.** El project expone las keys de Azure; el resource solo guarda evaluaciones.  
  Las keys y endpoints pertenecen al resource; evaluaciones y agentes se organizan en projects.
- ❌ **D.** No hay diferencia: ambos nombres se usan para el mismo objeto.  
  La lección enfatiza que resource y project son niveles distintos.

**Respuesta:** A. El Foundry resource es el recurso de Azure con endpoints, deployments y cuota compartida. El Foundry project es el espacio aislado para construir agentes, archivos, índices, evaluaciones y código. Repasa la lección 9.

*Objetivo: Deploy a model and interact with it in the Foundry portal · Lecciones: 9*

### 3. Los clientes de Luma deben encontrar artículos de ayuda por significado, aunque no usen las mismas palabras del título. ¿Qué tipo de modelo elegirías?

- ❌ **A.** Image generation  
  Image generation crea imágenes nuevas; no convierte texto en representaciones para búsqueda semántica.
- ❌ **B.** Modelo realtime de audio  
  Los modelos de audio sirven para conversación por voz o audio, no para comparar significado de textos.
- ❌ **C.** LLM más grande disponible  
  Un LLM puede ayudar, pero la necesidad específica de búsqueda por significado apunta a vectores.
- ✅ **D.** Embeddings  
  Los embeddings convierten texto en vectores para comparar significados aunque cambien las palabras.

**Respuesta:** D. La modalidad de entrada y salida descarta opciones. Para búsqueda semántica, el catálogo ofrece modelos de embeddings que generan vectores. Repasa la lección 10.

*Objetivo: Identify an appropriate AI model, based on capabilities · Lecciones: 10*

### 4. Estás comparando modelos para un asistente de Luma. ¿Qué DOS criterios de selección aparecen en la lección? Selecciona DOS respuestas.

- ❌ **A.** Elegir siempre el modelo con más parámetros.  
  La regla del curso es usar el modelo más pequeño que cumpla la tarea con calidad suficiente.
- ✅ **B.** Revisar modalidades de entrada y salida.  
  Las modalidades son el filtro más rápido para saber si el modelo acepta y produce lo que necesitas.
- ✅ **C.** Comprobar disponibilidad, región, deployment type y cuota.  
  Un modelo que no está disponible en tu región o no tiene cuota no sirve para la solución.
- ❌ **D.** Ignorar costo si el modelo aparece primero en el catálogo.  
  El costo por tokens, imagen o minuto es uno de los criterios de decisión.
- ❌ **E.** Cambiar a Provisioned antes de hacer pruebas de calidad.  
  Provisioned es una opción de capacidad, no un criterio inicial que reemplace pruebas de calidad.

**Respuesta:** B, C. La lección propone comparar capacidad, modalidades, calidad, costo, latencia, contexto y disponibilidad. No elijas por tamaño o posición en el catálogo. Repasa la lección 10.

*Objetivo: Identify an appropriate AI model, based on capabilities · Lecciones: 10*

### 5. Una empresa necesita que las solicitudes se procesen dentro de la Unión Europea y quiere pagar por token. ¿Qué deployment type corresponde?

- ❌ **A.** Global Standard  
  Global Standard puede procesar en cualquier región de Azure y no cumple residencia por zona.
- ✅ **B.** Data Zone Standard  
  Data Zone Standard procesa dentro de una zona como EU y se paga por token.
- ❌ **C.** Provisioned  
  Provisioned reserva capacidad y se paga por PTU, no es la opción por token pedida.
- ❌ **D.** Developer  
  Developer se menciona para evaluar modelos fine-tuned, no para producción con residencia EU por token.

**Respuesta:** B. Residencia por zona apunta a Data Zone Standard. Si además quiere pagar por token, encaja mejor que Provisioned. Repasa la lección 11.

*Objetivo: Identify appropriate model deployment options and configuration parameters · Lecciones: 11*

### 6. Al crear un deployment de gpt-5-mini para Luma, ¿qué TRES elementos se configuran en el deployment, no en cada solicitud? Selecciona TRES respuestas.

- ✅ **A.** Deployment name que usará el código.  
  El nombre del deployment se define al desplegar y es lo que se pasa como model en el código.
- ✅ **B.** Versión del modelo y política de actualización.  
  La versión fija o actualización automática es una configuración del deployment.
- ✅ **C.** Límite de tokens por minuto asignado.  
  El rate limit en TPM se toma de la cuota y se asigna al deployment.
- ❌ **D.** Pregunta concreta del usuario.  
  La pregunta del usuario viaja en cada solicitud como input o user prompt.
- ❌ **E.** temperature de una llamada individual.  
  temperature, si el modelo la admite, es un parámetro de la solicitud.

**Respuesta:** A, B, C. El deployment define modelo, versión, tipo, región, TPM y guardrails. La solicitud define instrucciones, input, formato y parámetros como max output tokens o temperature. Repasa la lección 11.

*Objetivo: Identify appropriate model deployment options and configuration parameters · Lecciones: 11*

### 7. Un script de pruebas empieza a recibir errores 429 al llamar al deployment de Luma. ¿Qué interpreta y qué haría primero?

- ✅ **A.** Superó el límite de uso; reasignaría TPM, probaría otra región o pediría más cuota.  
  El 429 indica demasiadas solicitudes o tokens por minuto frente al límite asignado.
- ❌ **B.** El nombre del deployment no existe; cambiaría el archivo .env.  
  Un deployment inexistente suele producir 404 o DeploymentNotFound, no 429.
- ❌ **C.** La API key expiró; escribiría la key en el código.  
  No debes escribir keys en código, y 429 no indica autenticación.
- ❌ **D.** El modelo no admite español; cambiaría el prompt a inglés.  
  La cuota no depende del idioma del prompt en ese sentido.

**Respuesta:** A. La cuota se mide en tokens por minuto por subscription, región, modelo y deployment type. Superarla produce 429. Repasa la lección 11.

*Objetivo: Identify appropriate model deployment options and configuration parameters · Lecciones: 11*

### 8. En el playground, el equipo agrega Instructions para que el asistente responda solo sobre Luma, breve y en español. ¿Qué demuestra la prueba?

- ❌ **A.** Que hay que crear otro resource group para cambiar el tono.  
  El tono se controla con instrucciones, no con resource groups.
- ❌ **B.** Que el deployment type cambió automáticamente a Provisioned.  
  Las instrucciones no cambian el tipo de deployment.
- ✅ **C.** Que las instrucciones modifican el comportamiento sin tocar el deployment.  
  El playground permite probar prompts e instrucciones sobre el mismo deployment.
- ❌ **D.** Que el modelo recuerda conversaciones de días anteriores sin historial.  
  El modelo no recuerda entre llamadas; el playground envía el historial de la conversación actual.

**Respuesta:** C. El playground sirve para probar prompts, comparar modelos y capturar una configuración reutilizable. Las Instructions cambian rol, alcance, tono y límites. Repasa la lección 12.

*Objetivo: Deploy a model and interact with it in the Foundry portal · Lecciones: 12*

### 9. Un desarrollador usará AIProjectClient para conectarse al project luma-soporte sin secretos en el código. ¿Qué necesita?

- ❌ **A.** Una API key pegada en chat_luma.py.  
  El curso evita secretos en código, y AIProjectClient no usa API key para el project.
- ❌ **B.** Solo el endpoint compatible con OpenAI terminado en /openai/v1/.  
  Ese endpoint corresponde a la alternativa con OpenAI SDK y key, no al project client.
- ❌ **C.** El rol Foundry Account Owner para todos los usuarios.  
  Para desarrollar, Foundry User es el rol de mínimo privilegio; Account Owner es excesivo.
- ✅ **D.** Microsoft Entra ID con DefaultAzureCredential y un rol como Foundry User.  
  AIProjectClient se conecta al project endpoint con Entra ID y permisos RBAC.

**Respuesta:** D. Para un Foundry project, el curso usa AIProjectClient, project endpoint y DefaultAzureCredential. En local usa az login; en Azure puede usar managed identity. Repasa la lección 13.

*Objetivo: Deploy a model and interact with it in the Foundry portal · Lecciones: 13*

### 10. Al terminar el curso, Luma quiere evitar costos innecesarios y confirmar que no sigue consumiendo. ¿Cuál plan coincide con la lección?

- ❌ **A.** Borrar solo el project y omitir la revisión de costos porque Standard cobra solo si se usa.  
  La lección recomienda borrar recursos dedicados y verificar Cost Management; además algunos deployments cobran por tiempo.
- ❌ **B.** Dejar Provisioned activo porque no cobra si nadie lo llama.  
  Provisioned cobra por capacidad reservada aunque no se use.
- ❌ **C.** Subir el TPM de pruebas para absorber cualquier script en ciclo.  
  En pruebas se recomienda TPM bajo para limitar sorpresas de consumo.
- ✅ **D.** Borrar deployments no usados, eliminar el resource group y revisar Cost Management al día siguiente.  
  La limpieza recomendada elimina recursos juntos y verifica costos después.

**Respuesta:** D. Controla gasto con budgets, alertas y TPM bajo en pruebas. Al terminar, borra recursos dedicados y verifica Cost Management. Repasa la lección 13.

*Objetivo: Identify appropriate model deployment options and configuration parameters · Lecciones: 13*
