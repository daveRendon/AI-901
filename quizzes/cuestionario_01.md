# Cuestionario 1 · Fundamentos de IA y Responsible AI

> **Sección:** 2 · **Lecciones:** 4–8 · **Preguntas:** 10 · **Tiempo sugerido:** 15 minutos

Practica cómo identificar cargas de trabajo de IA, cómo funcionan los modelos generativos y cómo aplicar Responsible AI en escenarios de Luma.

Responde sin consultar tus notas. Cuando termines, compara con [las respuestas y explicaciones](cuestionario_01_respuestas.md).

---

### 1. Luma recibe un mensaje de voz de José y quiere guardarlo como texto dentro del ticket antes de analizarlo. ¿Qué carga de trabajo resuelve primero esa necesidad?

- **A.** Text analysis, porque detecta entidades y sentimiento en texto existente.
- **B.** Speech recognition, porque convierte voz en texto.
- **C.** Computer vision, porque interpreta señales del router.
- **D.** Information extraction, porque produce campos estructurados.

### 2. Un cliente sube una foto de su factura. Luma necesita obtener número de cuenta, fecha y total en JSON. ¿Qué carga de trabajo es la más adecuada?

- **A.** Computer vision, porque la entrada es una imagen.
- **B.** Generative AI, porque redactará una respuesta al cliente.
- **C.** Information extraction, porque convierte documentos o imágenes en campos estructurados.
- **D.** Speech, porque procesa entradas no textuales.

### 3. Un compañero dice que un LLM responde copiando una frase completa de su memoria. ¿Cuál explicación corrige mejor esa idea?

- **A.** El modelo predice el siguiente token, lo agrega al texto y repite el proceso.
- **B.** El modelo busca una respuesta exacta en una base de datos interna de documentos.
- **C.** El modelo solo aplica reglas escritas a mano por el desarrollador.
- **D.** El modelo recuerda todas las conversaciones anteriores del usuario.

### 4. En una prueba de Luma, las respuestas se cortan antes de terminar. El equipo configuró un max output tokens muy bajo. ¿Qué cambio atiende directamente el problema?

- **A.** Cambiar el resource group del proyecto.
- **B.** Usar un prompt más creativo con temperature alta.
- **C.** Aumentar max output tokens o pedir una respuesta más corta.
- **D.** Mover el deployment a Batch.

### 5. En el piloto de Luma, los tickets de zonas rurales reciben menor prioridad y los números de tarjeta aparecen en logs visibles para todo el equipo. ¿Qué DOS principios están más directamente en riesgo? Selecciona DOS respuestas.

- **A.** Fairness
- **B.** Transparency
- **C.** Inclusiveness
- **D.** Privacy and Security

### 6. El asistente de Luma inventa que un reembolso se aprobará en 48 horas, aunque esa política no existe. ¿Qué control aplica mejor Reliability and Safety?

- **A.** Aumentar la cuota TPM del deployment.
- **B.** Hacer grounding en políticas oficiales y probar casos difíciles.
- **C.** Ocultar el nombre del cliente en la interfaz.
- **D.** Permitir que el modelo responda sin restricciones para ser más útil.

### 7. Luma quiere que una persona definida revise las respuestas automáticas sobre reembolsos y que exista auditoría periódica. ¿Qué principio aplica principalmente?

- **A.** Transparency
- **B.** Fairness
- **C.** Accountability
- **D.** Inclusiveness

### 8. El canal de voz de Luma falla con algunos acentos y no ofrece alternativa para clientes con discapacidad auditiva. ¿Qué acción refleja mejor Inclusiveness?

- **A.** Subir temperature para que el modelo responda con más variedad.
- **B.** Probar con usuarios diversos y ofrecer chat, subtítulos o texto.
- **C.** Ocultar los datos personales en las transcripciones.
- **D.** Publicar una página que explique que el sistema usa IA.

### 9. Estás preparando el piloto de Luma Asistente. ¿Qué DOS decisiones son controles de Responsible AI enseñados en la sección? Selecciona DOS respuestas.

- **A.** Ocultar PII, cifrar datos y limitar acceso con RBAC.
- **B.** Desactivar content filters para reducir rechazos.
- **C.** Permitir que el agente apruebe reembolsos sin revisión.
- **D.** Exigir revisión humana en respuestas sobre dinero.

### 10. Un analista dice que Fairness significa dar exactamente la misma prioridad a todos los tickets. ¿Cuál respuesta corrige mejor esa confusión?

- **A.** Fairness evita sesgos que perjudican a grupos y se revisa comparando resultados por segmento.
- **B.** Fairness consiste en explicar al cliente cómo funciona el sistema.
- **C.** Fairness significa proteger tarjetas y contraseñas.
- **D.** Fairness se logra usando siempre el modelo más grande disponible.
