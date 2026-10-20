# Práctica 8 · Caso completo Luma Soporte

- **Sección:** 10 · Proyecto práctico: Luma Soporte AI
- **Lecciones:** 44–46
- **Duración estimada:** 60 minutos
- **Nivel:** Integrador
- **Habilidades medidas:**
  - `Implement generative AI apps and agents by using Foundry`
  - `Implement AI solutions for text and speech by using Foundry`
  - `Implement AI solutions with computer vision and image-generation capabilities by using Foundry`
  - `Implement AI solutions for information extraction by using Foundry`
  - `Identify AI workloads`

## Objetivo

Unirás chat, agente, Speech, visión y Content Understanding para resolver el caso #8413 de José con evidencia. Validarás criterios de aceptación, probarás una foto borrosa, revisarás la traza del agente y aplicarás la matriz de troubleshooting.

## Lo que vas a construir

La ejecución de [luma_caso.py](../luma_caso.py), que usa funciones de las prácticas anteriores para reunir correo, audio, foto y factura, y luego pedir a `luma-soporte-agent` una respuesta final.

## Requisitos

- [ ] Prácticas 3, 5, 6 y 7 completadas.
- [ ] `luma-soporte-agent` activo con `file search` y versión configurada en `.env`.
- [ ] Deployments activos: `gpt-5-mini`; opcionalmente modelo de audio si lo usas aparte.
- [ ] Azure Speech configurado: `SPEECH_ENDPOINT`, `SPEECH_KEY`.
- [ ] Content Understanding configurado: `CU_ENDPOINT`, `FACTURA_URL`.
- [ ] Archivos [correo_jose.txt](../data/correo_jose.txt), [mensaje_jose.wav](../data/mensaje_jose.wav), [router_jose.jpg](../data/router_jose.jpg), [router_jose_borrosa.jpg](../data/router_jose_borrosa.jpg).
- [ ] Sesión activa con `az login`.

## Costo y limpieza

Esta práctica llama varios servicios. Ejecuta pocas veces, revisa tokens y evita loops. Al finalizar el curso, elimina deployments no usados, borra el resource group dedicado, purga recursos si necesitas reutilizar nombres y revisa Cost Management al día siguiente.

## Pasos

### Parte 1 · Revisar la arquitectura del caso

1. Abre [luma_caso.py](../luma_caso.py).
2. Observa que agrega al `sys.path` las carpetas `05_agent`, `07_speech`, `08_images` y `09_documents`.
3. Revisa las funciones importadas: `transcribir`, `diagnosticar_foto`, `extraer_y_validar`, `preguntar_al_agente`.
4. Abre [correo_jose.txt](../data/correo_jose.txt).
5. Identifica las cuatro evidencias del caso: correo, mensaje de voz, foto del router y factura.
6. Mapea cada entrada a su workload: text analysis, speech, computer vision, information extraction y agentic AI.
7. ✅ Punto de control: entiendes qué pieza valida cada tipo de evidencia.

### Parte 2 · Verificar `.env`

1. Abre `.env`.
2. Verifica:
   ```env
   FOUNDRY_PROJECT_ENDPOINT=https://<recurso>.services.ai.azure.com/api/projects/<project>
   MODEL_DEPLOYMENT_NAME=gpt-5-mini
   AGENT_NAME=luma-soporte-agent
   AGENT_VERSION=1
   SPEECH_ENDPOINT=https://<recurso>.cognitiveservices.azure.com/
   SPEECH_KEY=<tu-key>
   CU_ENDPOINT=https://<recurso>.services.ai.azure.com/
   FACTURA_URL=https://stai901luma3eknm.blob.core.windows.net/datos-curso/Factura_Luma.pdf
   ```
3. Si usas la versión 2 del agente, ajusta `AGENT_VERSION=2`.
4. Ejecuta `az login` si cambiaste de cuenta o expiró la sesión.
5. No pegues keys en la terminal compartida ni en documentación.
6. ✅ Punto de control: tienes todas las variables necesarias para las funciones reutilizadas.

### Parte 3 · Ejecutar el caso completo

1. Desde la raíz del repo, ejecuta:
   ```powershell
   python luma_caso.py
   ```
2. Espera a que termine cada etapa; Content Understanding y continuous recognition pueden tardar.
3. Revisa la transcripción del mensaje de José.
4. Revisa el diagnóstico de la foto: luz de internet en rojo o pérdida de conexión.
5. Revisa la salida de factura: cuenta, total y aviso de concepto duplicado.
6. Revisa la respuesta final del agente.
7. ✅ Punto de control: obtienes una respuesta empática basada en evidencia, no solo una respuesta genérica.

### Parte 4 · Evaluar criterios de aceptación

1. Criterio 1: reconoce ambos problemas, falla técnica y cobro duplicado.
2. Criterio 2: usa evidencia, como luz roja y concepto repetido.
3. Criterio 3: cita o se basa en la política de Luma.
4. Criterio 4: no promete reembolsos, montos ni plazos.
5. Criterio 5: da un siguiente paso claro para router y facturación.
6. Criterio 6: escala el cobro duplicado a facturación.
7. Si falla un criterio, decide si debes ajustar instrucciones del agente, validaciones o evidencia.
8. ✅ Punto de control: puedes convertir calidad en una lista verificable.

### Parte 5 · Probar la foto borrosa

1. Abre [luma_caso.py](../luma_caso.py).
2. Localiza:
   ```python
   foto = diagnosticar_foto(DATA / "router_jose.jpg")
   ```
3. Cambia temporalmente a:
   ```python
   foto = diagnosticar_foto(DATA / "router_jose_borrosa.jpg")
   ```
4. Ejecuta de nuevo:
   ```powershell
   python luma_caso.py
   ```
5. Esperado: el diagnóstico indique que la foto no permite distinguir bien las luces.
6. Esperado: el agente pida una foto más clara en lugar de inventar.
7. Vuelve a `router_jose.jpg` si conservarás el script para futuras prácticas.
8. ✅ Punto de control: la solución falla de forma segura ante evidencia visual mala.

### Parte 6 · Revisar la traza en el portal

1. Abre `luma-soporte-agent` en Foundry.
2. Abre la conversación reciente o detalles de ejecución disponibles.
3. Revisa la traza de la respuesta final.
4. Busca llamada a `file search` cuando el agente menciona políticas.
5. Verifica que la respuesta no se basó solo en memoria del modelo.
6. Si la traza no muestra tools, repite una pregunta de política directamente en el playground del agente.
7. ✅ Punto de control: puedes demostrar grounding con documentos internos.

### Parte 7 · Aplicar troubleshooting de acceso

1. Si ves `DefaultAzureCredential failed`, ejecuta `az login` y elige la subscription correcta.
2. Si ves 401, revisa key, token o endpoint de otro recurso.
3. Si ves 403, revisa roles: **Foundry User** o rol de datos del servicio.
4. Si ves 404 o `DeploymentNotFound`, copia endpoint y deployment exactos desde el portal.
5. Recuerda: 401 es autenticación; 403 es autorización.
6. ✅ Punto de control: diagnosticas por código de error, no por adivinanza.

### Parte 8 · Aplicar troubleshooting de cuota y formato

1. Si ves 429, reduce ritmo, agrega espera o aumenta cuota.
2. Si un modelo no aparece, cambia región o elige otro modelo compatible.
3. Si la entrada no se acepta, convierte audio a WAV PCM o imagen a JPEG/PNG.
4. Si el JSON sale incorrecto, refuerza prompt, usa structured outputs cuando estén disponibles y valida.
5. Si Content Understanding no devuelve campos esperados, revisa la pestaña **Result** y adapta parsing.
6. ✅ Punto de control: sabes separar errores de cuota, región, formato y salida.

### Parte 9 · Validar coherencia entre fuentes

1. Compara correo y mensaje de voz: ambos hablan de molestia y cobro/servicio.
2. Compara foto y correo: foto con luz roja apoya problema técnico.
3. Compara factura y voz: factura con `Plan Hogar` repetido apoya cobro duplicado.
4. Si una fuente contradice otra, no lo resuelve la IA automáticamente.
5. Marca discrepancias para una persona.
6. ✅ Punto de control: la evidencia se valida entre fuentes, no de forma aislada.

### Parte 10 · Limpieza final de recursos

1. Decide si conservarás recursos para repasar antes del examen.
2. Si terminaste el curso, borra deployments que no uses.
3. En Azure portal, borra el resource group dedicado con **Delete resource group**.
4. Si necesitas reutilizar nombres, considera soft delete y purga del recurso Foundry según el portal.
5. Revisa Cost Management al día siguiente.
6. Borra `.env` solo si ya no usarás el repo local; nunca lo subas a GitHub.
7. ✅ Punto de control: no quedan recursos de laboratorio generando costo sin supervisión.

## Retos opcionales

- Convierte los criterios de aceptación en una pequeña lista de pruebas manuales para cada ejecución.
- Sustituye la factura por el recibo y observa qué parte del orquestador debes ajustar.
- Pide al agente una versión de respuesta más corta para SMS sin perder escalamiento humano.

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| `DefaultAzureCredential failed` | No hay sesión de Azure o expiró | Ejecuta `az login` y elige la subscription correcta. |
| 401 Unauthorized | Key incorrecta, token inválido o endpoint de otro recurso | Revisa key y que el endpoint sea del mismo recurso. |
| 403 Forbidden | Identidad sin rol necesario | Asigna **Foundry User** o rol de datos del servicio. |
| 404 o `DeploymentNotFound` | Deployment o endpoint incorrecto | Copia nombre exacto y project endpoint desde el portal. |
| 429 Too Many Requests | TPM o solicitudes superadas | Reduce ritmo, reintenta con espera o aumenta cuota. |
| Modelo no disponible | Región o deployment type no compatible | Cambia región o elige otro modelo. |
| Entrada no soportada | Audio o imagen en formato incompatible | Convierte a WAV PCM, JPEG o PNG. |
| Formato de salida incorrecto | El modelo agregó texto fuera del JSON | Refuerza prompt, usa structured outputs y valida. |
| La respuesta promete reembolso | Agente no respetó límites o evidencia incompleta | Refuerza instrucciones y exige revisión humana. |

## Comprueba lo aprendido

1. La foto está borrosa, pero factura y voz sí son claras. ¿Qué debe decir la respuesta final sobre la evidencia visual?
2. El caso muestra un cobro duplicado con score alto. ¿Por qué el agente no debe aprobar el reembolso?
3. La app funcionaba y en horas pico recibe 429. ¿Qué cambia: key, rol, deployment name o ritmo/cuota?

## Siguiente paso

Vuelve al [índice de prácticas](README.md) y repite las secciones donde tus criterios de aceptación o troubleshooting hayan fallado.
