# Cuestionario 2 · Microsoft Foundry: modelos y deployments

> **Sección:** 3 · **Lecciones:** 9–13 · **Preguntas:** 10 · **Tiempo sugerido:** 15 minutos

Practica la jerarquía de Foundry, selección de modelos, deployment types, playground, acceso, cuotas, presupuesto y limpieza.

Responde sin consultar tus notas. Cuando termines, compara con [las respuestas y explicaciones](cuestionario_02_respuestas.md).

---

### 1. Luma quiere aislar el trabajo de soporte y facturación dentro del mismo Foundry resource, con archivos y evaluaciones separados. ¿Qué debe crear?

- **A.** Dos tenants de Microsoft Entra ID.
- **B.** Dos subscriptions para el mismo equipo.
- **C.** Varios Foundry projects dentro del resource.
- **D.** Un solo deployment con más TPM.

### 2. ¿Cuál descripción distingue mejor un Foundry resource de un Foundry project?

- **A.** El resource es infraestructura con endpoints y cuota; el project es el espacio de trabajo de desarrollo.
- **B.** El resource contiene solo archivos; el project contiene la subscription.
- **C.** El project expone las keys de Azure; el resource solo guarda evaluaciones.
- **D.** No hay diferencia: ambos nombres se usan para el mismo objeto.

### 3. Los clientes de Luma deben encontrar artículos de ayuda por significado, aunque no usen las mismas palabras del título. ¿Qué tipo de modelo elegirías?

- **A.** Image generation
- **B.** Modelo realtime de audio
- **C.** LLM más grande disponible
- **D.** Embeddings

### 4. Estás comparando modelos para un asistente de Luma. ¿Qué DOS criterios de selección aparecen en la lección? Selecciona DOS respuestas.

- **A.** Elegir siempre el modelo con más parámetros.
- **B.** Revisar modalidades de entrada y salida.
- **C.** Comprobar disponibilidad, región, deployment type y cuota.
- **D.** Ignorar costo si el modelo aparece primero en el catálogo.
- **E.** Cambiar a Provisioned antes de hacer pruebas de calidad.

### 5. Una empresa necesita que las solicitudes se procesen dentro de la Unión Europea y quiere pagar por token. ¿Qué deployment type corresponde?

- **A.** Global Standard
- **B.** Data Zone Standard
- **C.** Provisioned
- **D.** Developer

### 6. Al crear un deployment de gpt-5-mini para Luma, ¿qué TRES elementos se configuran en el deployment, no en cada solicitud? Selecciona TRES respuestas.

- **A.** Deployment name que usará el código.
- **B.** Versión del modelo y política de actualización.
- **C.** Límite de tokens por minuto asignado.
- **D.** Pregunta concreta del usuario.
- **E.** temperature de una llamada individual.

### 7. Un script de pruebas empieza a recibir errores 429 al llamar al deployment de Luma. ¿Qué interpreta y qué haría primero?

- **A.** Superó el límite de uso; reasignaría TPM, probaría otra región o pediría más cuota.
- **B.** El nombre del deployment no existe; cambiaría el archivo .env.
- **C.** La API key expiró; escribiría la key en el código.
- **D.** El modelo no admite español; cambiaría el prompt a inglés.

### 8. En el playground, el equipo agrega Instructions para que el asistente responda solo sobre Luma, breve y en español. ¿Qué demuestra la prueba?

- **A.** Que hay que crear otro resource group para cambiar el tono.
- **B.** Que el deployment type cambió automáticamente a Provisioned.
- **C.** Que las instrucciones modifican el comportamiento sin tocar el deployment.
- **D.** Que el modelo recuerda conversaciones de días anteriores sin historial.

### 9. Un desarrollador usará AIProjectClient para conectarse al project luma-soporte sin secretos en el código. ¿Qué necesita?

- **A.** Una API key pegada en chat_luma.py.
- **B.** Solo el endpoint compatible con OpenAI terminado en /openai/v1/.
- **C.** El rol Foundry Account Owner para todos los usuarios.
- **D.** Microsoft Entra ID con DefaultAzureCredential y un rol como Foundry User.

### 10. Al terminar el curso, Luma quiere evitar costos innecesarios y confirmar que no sigue consumiendo. ¿Cuál plan coincide con la lección?

- **A.** Borrar solo el project y omitir la revisión de costos porque Standard cobra solo si se usa.
- **B.** Dejar Provisioned activo porque no cobra si nadie lo llama.
- **C.** Subir el TPM de pruebas para absorber cualquier script en ciclo.
- **D.** Borrar deployments no usados, eliminar el resource group y revisar Cost Management al día siguiente.
