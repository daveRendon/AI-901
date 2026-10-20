# Práctica 6 · Vision y generación de imágenes

- **Sección:** 8 · Computer Vision y generación de imágenes
- **Lecciones:** 34–38
- **Duración estimada:** 55 minutos
- **Nivel:** Intermedio
- **Habilidades medidas:**
  - `Implement AI solutions with computer vision and image-generation capabilities by using Foundry`
  - `Identify AI workloads`

## Objetivo

Interpretarás imágenes con un modelo multimodal, generarás una imagen nueva con un modelo de image generation y ejecutarás una app ligera de visión. Validarás resultados visuales, fotos borrosas y uso de URLs públicas.

## Lo que vas a construir

Una ilustración `data/router_ayuda.png` con [generar_imagen.py](../generar_imagen.py) y diagnósticos de fotos con [vision_luma.py](../vision_luma.py).

## Requisitos

- [ ] Práctica 2 completada: `gpt-5-mini` activo y `.env` con `FOUNDRY_PROJECT_ENDPOINT`.
- [ ] Endpoint v1 y key para image generation en `AZURE_OPENAI_V1_ENDPOINT` y `AZURE_OPENAI_API_KEY`.
- [ ] Deployment de image generation llamado `gpt-image-1-mini` o ajuste del script al nombre que uses.
- [ ] Archivos [router_jose.jpg](../data/router_jose.jpg), [router_jose_borrosa.jpg](../data/router_jose_borrosa.jpg), [router_cliente.jpg](../data/router_cliente.jpg).
- [ ] URL pública de prueba del Readme: `https://stai901luma3eknm.blob.core.windows.net/datos-curso/router_cliente.jpg`.

## Costo y limpieza

Las imágenes generadas consumen más cómputo que texto. Genera pocas variaciones y conserva solo `data/router_ayuda.png` si lo usarás. Mantén `gpt-5-mini` para visión y borra deployments de image generation al final si no los necesitas.

## Pasos

### Parte 1 · Probar visión en el playground

1. Abre el playground de `gpt-5-mini` en `luma-soporte`.
2. En **Instructions**, escribe: `Eres un técnico de soporte de Luma. Describe solo lo que ves en la imagen. Si la imagen no es clara, dilo y pide otra foto.`
3. Inicia **New chat**.
4. Usa el botón de imagen para subir [router_jose.jpg](../data/router_jose.jpg).
5. Pregunta: `¿Qué indican las luces de este equipo? Responde en tres puntos.`
6. Esperado: identifica la luz de internet en rojo y sugiere revisar o reiniciar.
7. Sube [router_jose_borrosa.jpg](../data/router_jose_borrosa.jpg).
8. Repite la pregunta.
9. Esperado: admite que no distingue con claridad y pide otra foto.
10. Pide formato: `Responde en JSON con equipo, luces y accion_sugerida.`
11. Abre la pestaña **Code** del playground y observa `input_text` + `input_image`.
12. ✅ Punto de control: el modelo interpreta imagen y texto en el mismo mensaje y reconoce incertidumbre.

### Parte 2 · Desplegar modelo de image generation

1. En la lista de modelos, selecciona **Deploy a base model**.
2. En el catálogo, filtra por **Direct from Azure** si corresponde.
3. Filtra por inference task **Text to image**.
4. Selecciona `gpt-image-1-mini` si está disponible.
5. Si no está disponible, usa otro modelo de texto a imagen que el portal permita, como `FLUX.2-pro`.
6. Despliega con configuración por defecto.
7. Anota el deployment name.
8. Si tu deployment no se llama `gpt-image-1-mini`, ajusta [generar_imagen.py](../generar_imagen.py) antes de ejecutarlo.
9. ✅ Punto de control: tienes un modelo de image generation listo o sabes por qué no está disponible en tu región.

### Parte 3 · Generar en el image playground

1. Abre el image playground del modelo desplegado.
2. Prueba el prompt débil: `Un router.`
3. Observa estilo, fondo, encuadre y posible texto inventado.
4. Prueba el prompt refinado: `Ilustración plana de un router blanco con tres luces verdes, vista frontal, centrado, fondo claro, colores suaves, sin texto ni logotipos.`
5. Compara ambos resultados.
6. Cambia un solo detalle: luces verdes por una luz roja.
7. Genera de nuevo.
8. Observa cómo un cambio controlado del prompt cambia la imagen.
9. ✅ Punto de control: entiendes la fórmula sujeto, estilo, composición, iluminación y restricciones.

### Parte 4 · Ejecutar `generar_imagen.py`

1. Abre la pestaña **Code** del modelo de imagen.
2. Copia el endpoint v1 y la key a `.env`:
   ```env
   AZURE_OPENAI_V1_ENDPOINT=https://<recurso>.openai.azure.com/openai/v1/
   AZURE_OPENAI_API_KEY=<tu-key>
   ```
3. Abre [generar_imagen.py](../generar_imagen.py).
4. Revisa `client.images.generate`.
5. Revisa `n=1` y `size="1024x1024"`.
6. Ejecuta:
   ```powershell
   python generar_imagen.py
   ```
7. Espera más que en una respuesta de texto.
8. Abre `data/router_ayuda.png` cuando se cree.
9. ✅ Punto de control: la imagen se guardó como PNG decodificando base64.

### Parte 5 · Ejecutar `vision_luma.py` con foto local

1. Abre [vision_luma.py](../vision_luma.py).
2. Revisa la función `diagnosticar_foto`.
3. Observa que codifica la imagen local como data URL.
4. Observa `input_text` y `input_image` en el contenido.
5. Ejecuta:
   ```powershell
   python vision_luma.py
   ```
6. Esperado: diagnóstico de [router_cliente.jpg](../data/router_cliente.jpg) con luces visibles.
7. Cambia temporalmente la llamada principal para usar `router_jose_borrosa.jpg`.
8. Ejecuta de nuevo.
9. Esperado: indica que la imagen no es clara.
10. Regresa a `router_cliente.jpg` si quieres conservar el estado.
11. ✅ Punto de control: una app Python usa el mismo modelo de chat para capacidades de visión.

### Parte 6 · Probar una URL pública

1. En [vision_luma.py](../vision_luma.py), observa que el código actual usa data URL local.
2. Para probar URL pública, cambia el contenido de `input_image` a:
   ```python
   {"type": "input_image", "image_url": "https://stai901luma3eknm.blob.core.windows.net/datos-curso/router_cliente.jpg"}
   ```
3. Mantén la parte `input_text` igual.
4. Ejecuta el script.
5. Esperado: diagnóstico equivalente sin leer archivo local.
6. Vuelve al código original si quieres conservar la demo local.
7. ✅ Punto de control: entiendes que `input_image` acepta URL pública o datos base64.

### Parte 7 · Validar resultados visuales

1. Pregunta al modelo qué parte de la imagen respalda la respuesta.
2. Pide separar “lo visible” de “lo supuesto”.
3. No uses conteos pequeños o texto diminuto como decisión automática.
4. Para números de serie o totales, usa Content Understanding en la práctica 7.
5. Si la foto está borrosa, pide otra foto en vez de adivinar.
6. Si la decisión afecta reemplazos o cobros, manda a revisión humana.
7. Trata fotos con rostros, direcciones o documentos como datos personales.
8. ✅ Punto de control: sabes cuándo una respuesta visual convincente no es suficiente.

## Retos opcionales

- Cambia el prompt de imagen para generar una versión con luz roja y otra con fondo oscuro.
- Pide a `vision_luma.py` salida JSON con `equipo`, `luces`, `accion_sugerida` y `incertidumbre`.
- Compara `router_jose.jpg` contra `router_cliente.jpg` y redacta una regla de aceptación.

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| Modelo de imagen no aparece | Región, cuota o acceso no compatible | Cambia región o usa otro modelo de Text to image disponible. |
| 401 con image generation | Key o endpoint v1 incorrectos | Revisa `AZURE_OPENAI_V1_ENDPOINT` y `AZURE_OPENAI_API_KEY`. |
| `images.generate` falla por modelo | Deployment no se llama `gpt-image-1-mini` | Ajusta el parámetro `model` al nombre real del deployment. |
| Imagen borrosa produce diagnóstico seguro | Instrucciones no exigen incertidumbre | Agrega “si no es clara, dilo y pide otra foto”. |
| El modelo inventa número de serie | Estás usando descripción general | Usa Content Understanding con campos específicos. |
| URL pública no funciona | La URL no es accesible desde el servicio | Usa data URL base64 o publica el archivo correctamente. |

## Comprueba lo aprendido

1. Necesitas crear una ilustración nueva para una página de ayuda. ¿Por qué no usarías un modelo multimodal de visión?
2. Una foto borrosa genera una respuesta muy segura. ¿Qué instrucción y qué proceso humano agregas?
3. Tu aplicación necesita guardar el número de serie de una etiqueta. ¿Qué práctica siguiente resuelve mejor esa tarea?

## Siguiente paso

Continúa con [Práctica 7 · Content Understanding](practica_07_content_understanding.md).
