# Cuestionario 1 · Fundamentos de IA y Responsible AI · Respuestas y explicaciones

Vuelve a [las preguntas](cuestionario_01.md). Para cada error, anota el objetivo y repasa la lección indicada.

## Clave de respuestas

| # | Respuesta | Objetivo del examen | Lecciones |
|---|---|---|---|
| 1 | B | Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction | 5 |
| 2 | C | Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction | 5 |
| 3 | A | Describe how generative AI models work | 6 |
| 4 | C | Describe how generative AI models work | 6 |
| 5 | A, D | Describe principles of responsible AI | 7 |
| 6 | B | Describe principles of responsible AI | 7 |
| 7 | C | Describe principles of responsible AI | 8 |
| 8 | B | Describe principles of responsible AI | 7 |
| 9 | A, D | Describe principles of responsible AI | 7 |
| 10 | A | Describe principles of responsible AI | 8 |

---

### 1. Luma recibe un mensaje de voz de José y quiere guardarlo como texto dentro del ticket antes de analizarlo. ¿Qué carga de trabajo resuelve primero esa necesidad?

- ❌ **A.** Text analysis, porque detecta entidades y sentimiento en texto existente.  
  Text analysis puede usarse después, pero la entrada inicial es audio y aún no existe el texto.
- ✅ **B.** Speech recognition, porque convierte voz en texto.  
  Speech recognition, o speech-to-text, transforma el audio del cliente en texto para el ticket.
- ❌ **C.** Computer vision, porque interpreta señales del router.  
  Computer vision trabaja con imágenes o video, no con un mensaje de voz.
- ❌ **D.** Information extraction, porque produce campos estructurados.  
  Information extraction podría extraer campos luego, pero el primer problema es transcribir audio.

**Respuesta:** B. Usa el método de tres preguntas: entra audio, necesitas texto y no hay una acción de varios pasos. Eso apunta a Speech recognition antes de cualquier análisis posterior. Repasa la lección 5.

*Objetivo: Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction · Lecciones: 5*

### 2. Un cliente sube una foto de su factura. Luma necesita obtener número de cuenta, fecha y total en JSON. ¿Qué carga de trabajo es la más adecuada?

- ❌ **A.** Computer vision, porque la entrada es una imagen.  
  La entrada es una imagen, pero el resultado pedido son campos estructurados, no una descripción visual.
- ❌ **B.** Generative AI, porque redactará una respuesta al cliente.  
  El escenario no pide redactar contenido nuevo; pide convertir datos de una factura a campos.
- ✅ **C.** Information extraction, porque convierte documentos o imágenes en campos estructurados.  
  Cuando necesitas cuenta, fecha y total en JSON, la clave es extraer información estructurada.
- ❌ **D.** Speech, porque procesa entradas no textuales.  
  Speech procesa audio o voz, no facturas fotografiadas.

**Respuesta:** C. El resultado esperado distingue mejor la carga de trabajo que el tipo de entrada. Una foto de una factura con salida JSON es information extraction. Repasa la lección 5.

*Objetivo: Identify scenarios for common AI workloads, including generative and agentic AI, text analysis, speech, computer vision, and information extraction · Lecciones: 5*

### 3. Un compañero dice que un LLM responde copiando una frase completa de su memoria. ¿Cuál explicación corrige mejor esa idea?

- ✅ **A.** El modelo predice el siguiente token, lo agrega al texto y repite el proceso.  
  La lección explica que el texto se construye token por token mediante probabilidades y muestreo.
- ❌ **B.** El modelo busca una respuesta exacta en una base de datos interna de documentos.  
  Un LLM no responde buscando necesariamente un documento exacto; genera contenido nuevo paso a paso.
- ❌ **C.** El modelo solo aplica reglas escritas a mano por el desarrollador.  
  Eso describe software basado en reglas, no un modelo entrenado con patrones de datos.
- ❌ **D.** El modelo recuerda todas las conversaciones anteriores del usuario.  
  El modelo no recuerda entre llamadas; la aplicación debe enviar o encadenar el contexto.

**Respuesta:** A. Un LLM moderno usa tokens, embeddings y attention dentro de una arquitectura transformer. Su salida se genera como una secuencia de predicciones, no como una copia completa. Repasa la lección 6.

*Objetivo: Describe how generative AI models work · Lecciones: 6*

### 4. En una prueba de Luma, las respuestas se cortan antes de terminar. El equipo configuró un max output tokens muy bajo. ¿Qué cambio atiende directamente el problema?

- ❌ **A.** Cambiar el resource group del proyecto.  
  El resource group ayuda a administrar recursos, pero no controla la longitud de cada respuesta.
- ❌ **B.** Usar un prompt más creativo con temperature alta.  
  Temperature afecta variación, no evita que la respuesta se corte por falta de tokens.
- ✅ **C.** Aumentar max output tokens o pedir una respuesta más corta.  
  Si el límite de salida es demasiado bajo, debes aumentarlo o reducir la longitud solicitada.
- ❌ **D.** Mover el deployment a Batch.  
  Batch es para trabajos asíncronos grandes; no soluciona una respuesta truncada por límite de tokens.

**Respuesta:** C. max output tokens limita la longitud de la respuesta. Si el límite es insuficiente, el modelo puede dejar la salida incompleta. Repasa la lección 6.

*Objetivo: Describe how generative AI models work · Lecciones: 6*

### 5. En el piloto de Luma, los tickets de zonas rurales reciben menor prioridad y los números de tarjeta aparecen en logs visibles para todo el equipo. ¿Qué DOS principios están más directamente en riesgo? Selecciona DOS respuestas.

- ✅ **A.** Fairness  
  La prioridad menor para un segmento de clientes puede ser un sesgo que perjudica a un grupo.
- ❌ **B.** Transparency  
  Transparency trata de informar que se usa IA y explicar capacidades y límites.
- ❌ **C.** Inclusiveness  
  Inclusiveness se centra en diseñar para todas las personas, por ejemplo accesibilidad.
- ✅ **D.** Privacy and Security  
  Los datos de tarjeta expuestos en logs son un riesgo claro de privacidad y seguridad.

**Respuesta:** A, D. El primer riesgo es trato desigual por segmento; el segundo es exposición de datos personales. Son causas distintas y corresponden a Fairness y Privacy and Security. Repasa la lección 7.

*Objetivo: Describe principles of responsible AI · Lecciones: 7*

### 6. El asistente de Luma inventa que un reembolso se aprobará en 48 horas, aunque esa política no existe. ¿Qué control aplica mejor Reliability and Safety?

- ❌ **A.** Aumentar la cuota TPM del deployment.  
  La cuota controla capacidad por minuto; no evita que el modelo invente políticas.
- ✅ **B.** Hacer grounding en políticas oficiales y probar casos difíciles.  
  Grounding y pruebas con casos inesperados reducen hallucinations y mejoran la confiabilidad.
- ❌ **C.** Ocultar el nombre del cliente en la interfaz.  
  Eso ayuda a privacidad, pero no corrige la falta de confiabilidad de la respuesta.
- ❌ **D.** Permitir que el modelo responda sin restricciones para ser más útil.  
  Quitar restricciones aumenta el riesgo de respuestas inventadas o inseguras.

**Respuesta:** B. Reliability and Safety exige que el sistema funcione como se espera, incluso ante casos raros. Basar respuestas en políticas y validar con pruebas reduce plazos inventados. Repasa la lección 7.

*Objetivo: Describe principles of responsible AI · Lecciones: 7*

### 7. Luma quiere que una persona definida revise las respuestas automáticas sobre reembolsos y que exista auditoría periódica. ¿Qué principio aplica principalmente?

- ❌ **A.** Transparency  
  Transparency sería explicar al cliente que interactúa con IA y cuáles son sus límites.
- ❌ **B.** Fairness  
  Fairness se enfoca en evitar sesgos o trato desfavorable a grupos.
- ✅ **C.** Accountability  
  Asignar responsables, supervisión y auditoría corresponde a Accountability.
- ❌ **D.** Inclusiveness  
  Inclusiveness busca que la solución funcione para personas con diferentes necesidades.

**Respuesta:** C. Transparency ayuda a entender el sistema; Accountability define quién responde por él y cómo se supervisa. En reembolsos automáticos, la revisión humana es clave. Repasa la lección 8.

*Objetivo: Describe principles of responsible AI · Lecciones: 8*

### 8. El canal de voz de Luma falla con algunos acentos y no ofrece alternativa para clientes con discapacidad auditiva. ¿Qué acción refleja mejor Inclusiveness?

- ❌ **A.** Subir temperature para que el modelo responda con más variedad.  
  La variación de respuesta no resuelve barreras de acceso al canal.
- ✅ **B.** Probar con usuarios diversos y ofrecer chat, subtítulos o texto.  
  La inclusión exige diseñar para distintas capacidades, acentos y formas de acceso.
- ❌ **C.** Ocultar los datos personales en las transcripciones.  
  Eso es importante para Privacy and Security, no la acción principal de accesibilidad.
- ❌ **D.** Publicar una página que explique que el sistema usa IA.  
  Eso apoya Transparency, pero no da alternativas accesibles.

**Respuesta:** B. Inclusiveness significa que la solución sirva a todas las personas. En un canal de voz, debes probar con usuarios diversos y ofrecer alternativas accesibles. Repasa la lección 7.

*Objetivo: Describe principles of responsible AI · Lecciones: 7*

### 9. Estás preparando el piloto de Luma Asistente. ¿Qué DOS decisiones son controles de Responsible AI enseñados en la sección? Selecciona DOS respuestas.

- ✅ **A.** Ocultar PII, cifrar datos y limitar acceso con RBAC.  
  Son controles directos para Privacy and Security.
- ❌ **B.** Desactivar content filters para reducir rechazos.  
  La lección recomienda mantener guardrails y content filters como ayuda de seguridad.
- ❌ **C.** Permitir que el agente apruebe reembolsos sin revisión.  
  Las decisiones importantes requieren responsables, supervisión y, a menudo, revisión humana.
- ✅ **D.** Exigir revisión humana en respuestas sobre dinero.  
  La revisión humana apoya Accountability y reduce riesgos en decisiones importantes.

**Respuesta:** A, D. Las herramientas ayudan, pero las decisiones de Responsible AI son de diseño: proteger datos, usar controles de acceso y mantener humanos responsables cuando importa. Repasa la lección 7.

*Objetivo: Describe principles of responsible AI · Lecciones: 7*

### 10. Un analista dice que Fairness significa dar exactamente la misma prioridad a todos los tickets. ¿Cuál respuesta corrige mejor esa confusión?

- ✅ **A.** Fairness evita sesgos que perjudican a grupos y se revisa comparando resultados por segmento.  
  La lección aclara que equidad no es dar lo mismo a todos, sino evitar perjuicios injustos.
- ❌ **B.** Fairness consiste en explicar al cliente cómo funciona el sistema.  
  Esa explicación corresponde principalmente a Transparency.
- ❌ **C.** Fairness significa proteger tarjetas y contraseñas.  
  Proteger datos personales corresponde a Privacy and Security.
- ❌ **D.** Fairness se logra usando siempre el modelo más grande disponible.  
  El tamaño del modelo no garantiza ausencia de sesgos ni trato justo.

**Respuesta:** A. Fairness se evalúa observando si grupos reciben trato desfavorable sin razón válida. La mitigación es medir por segmentos y corregir datos o reglas que causan sesgo. Repasa la lección 8.

*Objetivo: Describe principles of responsible AI · Lecciones: 8*
