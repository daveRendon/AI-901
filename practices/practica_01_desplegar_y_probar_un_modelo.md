# Práctica 1 · Desplegar y probar un modelo

- **Sección:** 3 · Microsoft Foundry: modelos y deployments
- **Lecciones:** 12–13
- **Duración estimada:** 35 minutos
- **Nivel:** Inicial
- **Habilidades medidas:**
  - `Identify AI model components and configurations`
  - `Implement generative AI apps and agents by using Foundry`

## Objetivo

Crearás el project `luma-soporte`, desplegarás `gpt-5-mini` y comprobarás su comportamiento en el playground. También dejarás anotados el endpoint, el nombre del deployment, la región y las decisiones de costo para usarlos en las siguientes prácticas.

## Lo que vas a construir

Un project de Microsoft Foundry con un deployment `gpt-5-mini` Global Standard probado con instrucciones de Luma Soporte.

## Requisitos

- [ ] Subscription de Azure activa con permisos para crear recursos.
- [ ] Acceso al portal `ai.azure.com` y experiencia **New Foundry** activa si aparece el interruptor.
- [ ] Rol con permisos para crear el project y el deployment.
- [ ] Región con cuota para `gpt-5-mini`; si no hay cuota, usar otra región o un modelo alternativo indicado por el portal.
- [ ] Archivo [data/prueba_playground.txt](../data/prueba_playground.txt).
- [ ] Un lugar seguro para anotar `FOUNDRY_PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT_NAME`, región y tipo de deployment.

## Costo y limpieza

Los deployments Standard cobran por tokens procesados. Mantén límites de TPM bajos para pruebas y crea un budget con alertas al 50, 80 y 100 %. Conserva el project y el deployment para las prácticas 2–8; al terminar el curso, borra el resource group dedicado y revisa Cost Management al día siguiente.

## Pasos

### Parte 1 · Crear el project de Foundry

1. Entra a `https://ai.azure.com` con la cuenta de Azure del curso.
2. Cierra paneles de bienvenida si aparecen.
3. Activa **New Foundry** si el portal lo muestra.
4. Crea un project llamado `luma-soporte`.
5. Abre **Advanced options** antes de confirmar.
6. Revisa el **Foundry resource** propuesto por el portal.
7. Selecciona tu subscription del curso.
8. Crea o selecciona un resource group dedicado, por ejemplo `rg-ai901-curso`.
9. Elige una región recomendada por Foundry; la demo usa East US 2, pero tu región puede ser distinta.
10. Si tus permisos no permiten recursos recomendados, desmarca esa opción y continúa con el project básico.
11. Selecciona **Create** y espera a que el project termine de crearse.
12. En la página de inicio, localiza **Project endpoint**, **Azure OpenAI endpoint** y la zona donde aparece la API key.
13. Copia solo lo necesario en tus notas; si copias una key, guárdala como secreto y no la pegues en capturas.
14. ✅ Punto de control: ves el project `luma-soporte` abierto y puedes volver a su página de inicio.

### Parte 2 · Desplegar `gpt-5-mini`

1. En el project, abre **Discover**.
2. Entra a **Models**.
3. Busca `gpt-5-mini`.
4. Abre la ficha del modelo y revisa capacidades: texto, imagen, ventana de contexto, precios y disponibilidad.
5. Selecciona **Deploy**.
6. Usa la configuración por defecto cuando esté disponible.
7. Confirma que el deployment name sea `gpt-5-mini` o anota el nombre exacto si lo cambias.
8. Revisa el **deployment type**; en la demo es **Global Standard**.
9. Revisa el límite de tokens por minuto asignado por tu cuota.
10. Confirma el despliegue.
11. Si aparece error de cuota, intenta otra región compatible o un modelo alternativo como `gpt-5-nano` si el portal lo propone.
12. ✅ Punto de control: el deployment aparece creado correctamente en la lista de modelos del project.

### Parte 3 · Probar sin instrucciones

1. Abre el playground que aparece al terminar el deployment.
2. Si necesitas más espacio, oculta el menú lateral.
3. Abre [data/prueba_playground.txt](../data/prueba_playground.txt).
4. Envía primero el prompt: `Mi router se desconecta cada noche. ¿Qué puedo hacer?`
5. Observa si la respuesta es útil pero genérica o demasiado larga.
6. Anota una frase de la respuesta para compararla después.
7. ✅ Punto de control: el modelo responde, pero todavía no está limitado al estilo ni al alcance de Luma.

### Parte 4 · Agregar Instructions de Luma

1. En el panel izquierdo del playground, localiza **Instructions**.
2. Pega el bloque `# Instructions (system prompt)` de [data/prueba_playground.txt](../data/prueba_playground.txt): asistente de Luma Soporte, español, tono cordial, máximo 5 líneas, solo internet residencial y dispositivos Luma, y escalamiento si no sabe.
3. Inicia un chat nuevo con **New chat**.
4. Repite: `Mi router se desconecta cada noche. ¿Qué puedo hacer?`
5. Envía el seguimiento: `Ya lo reinicié y sigue igual.`
6. Envía el prompt fuera de alcance: `¿Me recomiendas una película para hoy?`
7. Compara la respuesta con la prueba sin instrucciones.
8. ✅ Punto de control: el modelo responde breve, en español, mantiene el contexto del seguimiento y rechaza con amabilidad el tema fuera de alcance.

### Parte 5 · Guardar configuración para código

1. Regresa a la página de inicio del project.
2. Copia el **Project endpoint**.
3. Anota el deployment name exacto: `gpt-5-mini` salvo que lo hayas cambiado.
4. Anota la región y el deployment type.
5. Anota si usaste un modelo alternativo por falta de cuota.
6. No pegues la API key en documentos compartidos ni en GitHub.
7. Para la práctica 2, estos valores irán en `.env`:
   ```env
   FOUNDRY_PROJECT_ENDPOINT=https://<recurso>.services.ai.azure.com/api/projects/<project>
   MODEL_DEPLOYMENT_NAME=gpt-5-mini
   ```
8. ✅ Punto de control: tienes endpoint, deployment name, región y tipo de deployment guardados de forma segura.

### Parte 6 · Revisar presupuesto y acceso

1. En Azure portal, abre **Cost Management** para tu subscription o resource group.
2. Crea un budget mensual pequeño para laboratorios.
3. Configura alertas al 50 %, 80 % y 100 %.
4. Revisa quién tiene acceso al project.
5. Para desarrollo, usa el rol **Foundry User** con mínimo privilegio.
6. Recuerda que `AIProjectClient` requiere Microsoft Entra ID, no API key.
7. Mantén el resource group dedicado para poder eliminar todo al final.
8. ✅ Punto de control: tienes una política básica de costo y sabes qué borrar cuando termines.

## Retos opcionales

- Cambia una sola regla de las Instructions, por ejemplo máximo 3 líneas, y compara.
- Prueba otra pregunta fuera de alcance y verifica que el modelo no conteste temas generales.
- Revisa el límite de TPM del deployment y anota cómo cambiaría si tuvieras un laboratorio con más alumnos.

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| No puedes crear el project | Permisos insuficientes o subscription equivocada | Verifica la cuenta, subscription y permisos de creación de recursos. |
| `gpt-5-mini` no aparece | Modelo no disponible en tu región o subscription | Cambia de región o elige un modelo compatible indicado por el portal. |
| Error de cuota al desplegar | No hay TPM disponible | Baja TPM, cambia región o usa otro modelo para el laboratorio. |
| El playground responde genérico | No pegaste las Instructions o seguiste el chat anterior | Pega Instructions e inicia **New chat**. |
| Responde temas fuera de Luma | El system prompt no limita el alcance | Revisa la regla “Solo hablas de internet residencial y dispositivos Luma”. |
| Costos inesperados | Dejaste deployments que no usarás o no revisaste consumo | Borra deployments no necesarios y revisa Cost Management. |

## Comprueba lo aprendido

1. Tu deployment existe, pero el código futuro recibe `DeploymentNotFound`. ¿Qué dato deberías comparar primero entre portal y `.env`?
2. Un compañero quiere pegar la API key en un script de ejemplo para ahorrar tiempo. ¿Qué alternativa más segura usarás en las siguientes prácticas?
3. El modelo contesta una pregunta de películas aunque el curso es de soporte técnico. ¿Qué parte del prompt debes reforzar?

## Siguiente paso

Continúa con [Práctica 2 · Prompts y cliente de chat](practica_02_prompts_y_cliente_de_chat.md).
