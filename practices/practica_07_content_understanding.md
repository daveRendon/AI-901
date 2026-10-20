# Práctica 7 · Content Understanding

- **Sección:** 9 · Content Understanding y extracción de información
- **Lecciones:** 39–43
- **Duración estimada:** 65 minutos
- **Nivel:** Intermedio
- **Habilidades medidas:**
  - `Implement AI solutions for information extraction by using Foundry`
  - `Identify AI workloads`

## Objetivo

Convertirás documentos, imágenes, audio y video en datos estructurados con Content Understanding. Compararás Read, Layout, Invoice/Receipt, un custom analyzer de etiqueta, analyzers de audio/video y el cliente [extraer_factura.py](../extraer_factura.py).

## Lo que vas a construir

Un recorrido por el playground de Content Understanding y una app Python que usa `begin_analyze`, `poller.result()` y reglas de validación sobre facturas y recibos.

## Requisitos

- [ ] Project en una región compatible con Content Understanding.
- [ ] Acceso a **Build, Services, Content Understanding**.
- [ ] Rol con acceso de datos al Foundry resource.
- [ ] `.env` con `CU_ENDPOINT` y `FACTURA_URL`.
- [ ] Archivos [Factura_Luma.pdf](../data/Factura_Luma.pdf), [etiqueta_router.jpg](../data/etiqueta_router.jpg), [etiqueta_router_reflejo.jpg](../data/etiqueta_router_reflejo.jpg), [llamada_soporte.wav](../data/llamada_soporte.wav), [video_router.mp4](../data/video_router.mp4), [recibo_luma.jpg](../data/recibo_luma.jpg).
- [ ] Paquete `azure-ai-contentunderstanding` instalado.

## Costo y limpieza

Algunos analyzers despliegan modelos generativos por detrás y pueden generar costo. Usa muestras pequeñas, cancela despliegues si solo revisarás resultados preparados y elimina analyzers custom de prueba que no usarás. Conserva `CU_ENDPOINT` para la práctica final.

## Pasos

### Parte 1 · Entender analyzers y campos

1. Recuerda: OCR/Read lee texto, pero no sabe qué significa cada valor.
2. Recuerda: Layout agrega estructura, como tablas y párrafos.
3. Recuerda: un analyzer de dominio o custom asigna valores a campos con significado.
4. Un schema define campos, tipos, método y descripción.
5. `extract` toma valores visibles.
6. `generate` redacta o deduce un valor nuevo.
7. `classify` elige entre categorías cerradas.
8. Cada campo puede incluir confidence score y grounding.
9. ✅ Punto de control: sabes por qué “leer texto” no basta para integrar datos.

### Parte 2 · Probar Read y Layout con factura

1. En el project, entra a **Build**.
2. Abre **Services**.
3. Selecciona **Content Understanding**.
4. Elige **OCR/Read** con modalidad **Document**.
5. Sube o selecciona una muestra; si usas la factura de Luma, usa [Factura_Luma.pdf](../data/Factura_Luma.pdf).
6. Ejecuta **Run analysis**.
7. Revisa **Markdown**: texto extraído.
8. Revisa **Paragraphs**: agrupación del texto.
9. Revisa **Result**: JSON con líneas y posiciones.
10. Cambia a **Layout**.
11. Ejecuta sobre el mismo documento.
12. Revisa **Tables** si aparecen.
13. ✅ Punto de control: puedes distinguir texto, estructura y JSON sin campos de negocio.

### Parte 3 · Probar Invoice o Receipt

1. En Content Understanding, abre el grupo **Procurement**.
2. Selecciona **Invoice** para facturas o **Receipt** para recibos.
3. Si el portal pide desplegar modelos, decide si continuar según costo y permisos.
4. Analiza [Factura_Luma.pdf](../data/Factura_Luma.pdf) si tu entorno lo permite.
5. Revisa **Fields**: proveedor/cliente, fecha, conceptos, total u otros campos disponibles.
6. Revisa **Result**: JSON que recibirá la app.
7. Compara conceptos con la factura de José: `Plan Hogar 200 Mbps` aparece dos veces.
8. Abre la pestaña **Code**.
9. Observa `ContentUnderstandingClient` y `begin_analyze`.
10. ✅ Punto de control: entiendes por qué un analyzer de dominio devuelve campos con significado.

### Parte 4 · Crear custom analyzer de etiqueta

1. Cambia la modalidad a **Image**.
2. Sube [etiqueta_router.jpg](../data/etiqueta_router.jpg).
3. Ejecuta OCR y revisa el texto detectado.
4. Crea un analyzer custom llamado `luma-etiqueta-analyzer`.
5. Agrega el campo `modelo` con método `extract`.
6. Agrega `numero_serie` con método `extract`.
7. Agrega `mac` con método `extract` y descripción: `Seis pares hexadecimales`.
8. Agrega `estado_equipo` con método `classify` y opciones `sin_danos` y `danado`.
9. Ejecuta el analyzer.
10. Revisa **Fields** y **Result**.
11. Compara valores: `Luma X300`, `LX300-26-041256`, `3C:84:6A:12:9F:0B`.
12. ✅ Punto de control: obtuviste campos, scores y ubicación desde una imagen.

### Parte 5 · Probar una etiqueta difícil

1. Sube [etiqueta_router_reflejo.jpg](../data/etiqueta_router_reflejo.jpg).
2. Ejecuta `luma-etiqueta-analyzer`.
3. Revisa si algún campo baja su confidence score.
4. Revisa si algún campo queda vacío.
5. Considera correcto un campo vacío si la evidencia no es clara.
6. Decide un umbral, por ejemplo 0.8, para revisión humana.
7. ✅ Punto de control: entiendes que un valor inventado es peor que un campo vacío o de baja confianza.

### Parte 6 · Analizar audio y video

1. En Content Understanding, cambia a modalidad **Audio**.
2. Sube [llamada_soporte.wav](../data/llamada_soporte.wav).
3. Ejecuta el analyzer disponible.
4. Revisa transcripción, marcas de tiempo y resumen si aparecen.
5. Agrega campos de ejemplo si el portal lo permite: `motivo`, `resumen`, `sentimiento`, `compromiso`.
6. Usa `classify` para motivo y sentimiento; usa `generate` para resumen y compromiso.
7. Cambia a modalidad **Video**.
8. Sube [video_router.mp4](../data/video_router.mp4).
9. Revisa segmentos, descripciones, fotogramas clave y transcripción.
10. Compara JSON de audio contra JSON de video.
11. ✅ Punto de control: ves que Content Understanding es multimodal y asíncrono para contenido pesado.

### Parte 7 · Configurar `.env` para Python

1. En la pestaña **Code** o inicio del recurso, copia el endpoint de Content Understanding.
2. Completa en `.env`:
   ```env
   CU_ENDPOINT=https://<recurso>.services.ai.azure.com/
   FACTURA_URL=https://stai901luma3eknm.blob.core.windows.net/datos-curso/Factura_Luma.pdf
   ```
3. Para probar recibo después, ten a mano:
   ```env
   FACTURA_URL=https://stai901luma3eknm.blob.core.windows.net/datos-curso/recibo_luma.jpg
   ```
4. Ejecuta `az login` si la sesión expiró.
5. ✅ Punto de control: la app puede autenticar con Entra ID y acceder al contenido por URL.

### Parte 8 · Ejecutar `extraer_factura.py`

1. Abre [extraer_factura.py](../extraer_factura.py).
2. Revisa `ContentUnderstandingClient`.
3. Revisa `begin_analyze(analyzer_id=..., inputs=[AnalysisInput(url=...)])`.
4. Revisa `poller.result()`.
5. Revisa `extraer_y_validar`: umbral, suma de conceptos y duplicados.
6. Ejecuta:
   ```powershell
   python extraer_factura.py
   ```
7. Esperado: campos de la factura y sección `AVISOS:`.
8. Busca aviso de posible cobro duplicado para `Plan Hogar 200 Mbps`.
9. ✅ Punto de control: la app extrae campos y aplica reglas de negocio, pero no decide reembolsos.

### Parte 9 · Probar recibo con `prebuilt-receipt`

1. En [extraer_factura.py](../extraer_factura.py), localiza el valor por defecto `analyzer_id="prebuilt-invoice"`.
2. Cambia temporalmente a `prebuilt-receipt`.
3. En `.env`, cambia `FACTURA_URL` a:
   ```env
   FACTURA_URL=https://stai901luma3eknm.blob.core.windows.net/datos-curso/recibo_luma.jpg
   ```
4. Ejecuta el script.
5. Revisa que los campos cambian porque cambió el analyzer.
6. Vuelve a `prebuilt-invoice` y a la factura si vas a continuar con el caso final.
7. ✅ Punto de control: cambiar analyzer no cambia el patrón del cliente; cambia los campos esperados.

### Parte 10 · Validar antes de procesar

1. Usa umbral de confianza, por ejemplo 0.8.
2. Valida formatos: fechas, montos, cuenta `4821-0098`.
3. Valida reglas: suma de conceptos contra total.
4. Detecta duplicados en el mismo periodo.
5. Exige campos obligatorios: cuenta y total.
6. Guarda o muestra evidencia/ubicación para revisión humana.
7. Escala si hay score bajo, campo faltante o regla de negocio fallida.
8. ✅ Punto de control: completaste extracción más validación, no solo una llamada al servicio.

## Retos opcionales

- Agrega un campo custom `requiere_revision` con método `classify` en una prueba de imagen.
- Define un schema de audio para clasificar llamadas de facturación frente a falla técnica.
- Ajusta el umbral de `extraer_y_validar` a 0.9 y compara avisos.

## Si algo falla

| Síntoma | Causa probable | Solución |
|---|---|---|
| Content Understanding no aparece | Región no compatible | Crea o usa un project en región compatible indicada por el portal. |
| 403 Forbidden | Falta rol de datos | Asigna el rol requerido sobre el Foundry resource. |
| `FACTURA_URL` no se puede analizar | URL no accesible públicamente o caducada | Usa la URL pública del Readme o publica tu archivo correctamente. |
| Campos vacíos en etiqueta con reflejo | Imagen difícil o baja confianza | Enviar a revisión o pedir otra foto. |
| Suma no coincide | Extracción dudosa o documento inconsistente | Revisa fields, scores y documento original. |
| SDK cambia nombres de campos | Versión del servicio distinta | Revisa la pestaña **Result** del portal y adapta el parsing. |
| Análisis de video tarda mucho | Operación pesada y asíncrona | Espera el resultado y evita archivos grandes en laboratorio. |

## Comprueba lo aprendido

1. Un PDF ya tiene texto extraído por OCR, pero necesitas el total normalizado. ¿Qué tipo de analyzer necesitas?
2. Una foto con reflejo produce `mac` con score bajo. ¿Debe tu sistema crear el caso automáticamente?
3. Cambias de factura a recibo y mantienes el mismo código cliente. ¿Qué parámetro debe cambiar?

## Siguiente paso

Continúa con [Práctica 8 · Caso completo Luma Soporte](practica_08_caso_completo_luma_soporte.md).
