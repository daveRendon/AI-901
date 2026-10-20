# AI-901 en español · Azure AI Fundamentals con Microsoft Foundry

Repositorio oficial del curso de Udemy **AI-901 en español**. Aquí encontrarás el código de Python de cada demo, los archivos de datos, las prácticas guiadas, los cuestionarios por sección y el simulacro de examen.

A lo largo del curso construirás **Luma Soporte AI**, una solución de soporte técnico para los routers de Luma que entiende **texto, voz, imágenes y documentos** y responde con evidencia, usando **Microsoft Foundry** y **Python**.

## El examen AI-901

| Dominio | Peso |
|---|---|
| Identify AI concepts and capabilities | 40–45 % |
| Implement AI solutions by using Microsoft Foundry | 55–60 % |

Calificación mínima para aprobar: **700**.

- [Examen AI-901: Azure AI Fundamentals](https://learn.microsoft.com/es-es/credentials/certifications/exams/ai-901/?WT.mc_id=AZ-MVP-5000671)
- [Guía de estudio oficial de AI-901](https://learn.microsoft.com/es-es/credentials/certifications/resources/study-guides/ai-901?WT.mc_id=AZ-MVP-5000671)
- [Certificación Microsoft Certified: Azure AI Fundamentals](https://learn.microsoft.com/es-es/credentials/certifications/azure-ai-fundamentals/?WT.mc_id=AZ-MVP-5000671)

---

## Requisitos

- Una **subscription de Azure** con permisos para crear recursos.
- **Python 3.10** o superior.
- **Visual Studio Code**.
- **Azure CLI** ([instalación](https://learn.microsoft.com/es-es/cli/azure/install-azure-cli?WT.mc_id=AZ-MVP-5000671)).

## Preparación del entorno

### 1. Clona el repositorio

```bash
git clone https://github.com/daveRendon/AI-901.git
cd AI-901
```

### 2. Crea un entorno virtual e instala las dependencias

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3. Inicia sesión en Azure

El curso usa **Microsoft Entra ID** (autenticación sin keys) siempre que es posible. `DefaultAzureCredential` toma tu sesión de `az login` en local y una managed identity cuando el código se ejecuta en Azure.

```bash
az login
```

### 4. Configura tus variables de entorno

Copia la plantilla y completa los valores de tus recursos:

```bash
# Windows (PowerShell)
Copy-Item .env.example .env
# macOS / Linux
cp .env.example .env
```

> **Nunca subas `.env` a GitHub.** Ya está incluido en `.gitignore`.

| Variable | Se usa en | Para qué sirve |
|---|---|---|
| `FOUNDRY_PROJECT_ENDPOINT` | Sección 4 en adelante | Endpoint de tu project de Foundry (Entra ID) |
| `MODEL_DEPLOYMENT_NAME` | Sección 4 en adelante | Nombre del deployment del modelo de chat |
| `AZURE_OPENAI_V1_ENDPOINT` | Secciones 4 y 8 | Endpoint compatible con OpenAI (opción con API key) |
| `AZURE_OPENAI_API_KEY` | Secciones 4 y 8 | API key del endpoint anterior |
| `AZURE_OPENAI_ENDPOINT` | Sección 7 | Endpoint del modelo de audio |
| `AUDIO_DEPLOYMENT_NAME` | Sección 7 | Deployment del modelo de audio |
| `AGENT_NAME`, `AGENT_VERSION` | Sección 5 | Agente `luma-soporte-agent` |
| `LANGUAGE_ENDPOINT`, `LANGUAGE_KEY` | Sección 6 | Azure Language en Foundry Tools |
| `SPEECH_ENDPOINT`, `SPEECH_KEY` | Sección 7 | Azure Speech en Foundry Tools |
| `CU_ENDPOINT` | Sección 9 | Azure Content Understanding en Foundry Tools |
| `FACTURA_URL` | Lección 43 y caso final | URL pública de `data/Factura_Luma.pdf` |

### 5. Controla el gasto desde el primer día

- Crea un **resource group dedicado** para el curso.
- Configura un **budget con alertas** ([cómo hacerlo](https://learn.microsoft.com/es-es/azure/cost-management-billing/costs/tutorial-acm-create-budgets?WT.mc_id=AZ-MVP-5000671)).
- Mantén los secretos **fuera del código**.
- Cuando termines o pauses el curso, elimina los recursos que ya no uses (Lección 13).

---

## Estructura del repositorio

```text
AI-901/
├── Readme.md
├── requirements.txt          # Dependencias de Python
├── .env.example              # Plantilla de variables de entorno
├── .gitignore
│
├── chat_luma.py              # Sección 4  · Cliente de chat con el Foundry SDK
├── chat_key.py               # Sección 4  · Alternativa con API key (endpoint compatible con OpenAI)
├── validar_respuesta.py      # Sección 4  · Validar estado y formato JSON de una respuesta
├── agente_luma.py            # Sección 5  · Cliente de Python para el agente
├── analizar_ticket.py        # Sección 6  · Text Analysis con un modelo general
├── lenguaje_luma.py          # Sección 6  · Azure Language en Foundry Tools
├── pregunta_hablada.py       # Sección 7  · Prompt hablado con un modelo multimodal
├── voz_luma.py               # Sección 7  · Azure Speech: reconocimiento y síntesis
├── voz_luma-pt1.py           # Sección 7  · Parte 1: speech recognition
├── voz_luma-pt2.py           # Sección 7  · Parte 2: speech synthesis (fragmento)
├── vision_luma.py            # Sección 8  · Aplicación ligera con visión
├── generar_imagen.py         # Sección 8  · Generación de imágenes
├── extraer_factura.py        # Sección 9  · Extraer y validar los campos de la factura
├── extraer_factura-pt2.py    # Sección 9  · Variante: todos los campos con su confianza
├── luma_caso.py              # Sección 10 · Caso completo Luma Soporte
│
├── data/
│   ├── prueba_playground.txt                  # Sección 3  · Prueba en el playground
│   ├── prompt_clasificacion.txt               # Sección 4  · Prompts
│   ├── prompt_mejorado.txt
│   ├── instrucciones_luma_agent.txt           # Sección 5  · Instrucciones del agente
│   ├── instrucciones_luma_agent-optimized.txt #              (versión optimizada)
│   ├── politicas_luma.docx                    #              Políticas para file search
│   ├── ticket_8413.txt                        # Sección 6  · Tickets de soporte
│   ├── ticket_positivo.txt
│   ├── ticket_ingles.txt
│   ├── etiqueta_aleman.txt
│   ├── pregunta.wav                           # Sección 7  · Audio de entrada y salida
│   ├── pregunta_molesta.wav
│   ├── mensaje.wav
│   ├── respuesta.wav
│   ├── router_cliente.jpg                     # Sección 8  · Imágenes del router
│   ├── router_jose_borrosa.jpg
│   ├── router_ayuda.png                       #              (generada por generar_imagen.py)
│   ├── Factura_Luma.pdf                       # Sección 9  · Documento, imagen, audio y video
│   ├── recibo_luma.jpg
│   ├── etiqueta_router.jpg
│   ├── etiqueta_router_reflejo.jpg
│   ├── llamada_soporte.wav
│   ├── video_router.mp4
│   ├── correo_jose.txt                        # Sección 10 · Caso de José
│   ├── router_jose.jpg
│   └── mensaje_jose.wav
│
├── practices/
│   ├── README.md                              # Índice de las 8 prácticas guiadas
│   └── practica_01_… a practica_08_….md
│
├── quizzes/
│   ├── cuestionario_01.md … cuestionario_06.md                    # Preguntas
│   ├── cuestionario_01_respuestas.md … cuestionario_06_respuestas.md  # Respuestas explicadas
│   ├── cuestionario_01_udemy.csv … cuestionario_06_udemy.csv      # Formato de importación de Udemy
│   └── source/cuestionario_01.yaml … cuestionario_06.yaml         # Fuente de cada cuestionario
│
└── mock-exam/
    ├── simulacro.md                           # Simulacro de examen de 50 preguntas
    ├── simulacro_respuestas.md                # Respuestas y hoja de resultados por área
    ├── simulacro_udemy.csv                    # Formato de importación de Udemy
    └── source/simulacro.yaml                  # Fuente del simulacro
```

> `.env` y `.venv/` no se suben al repositorio (están en `.gitignore`).

## Cómo usar este repositorio

Cada sección del curso sigue el mismo ciclo:

1. **Concepto**: la idea y cómo se evalúa en el examen.
2. **Demo**: el código de esta carpeta, explicado línea por línea.
3. **Práctica**: repites la demo por tu cuenta con la guía de [`practices/`](practices/README.md).
4. **Quiz**: compruebas lo aprendido con [`quizzes/`](quizzes/) y revisas por qué cada opción es correcta o incorrecta en los archivos `_respuestas.md`.
5. **Microsoft Learn**: profundizas con los recursos oficiales de cada lección.

Ejecuta los scripts **desde la raíz del repositorio**, por ejemplo:

```bash
python chat_luma.py
```

---

## Mapa del curso

### Sección 1 · Orientación y preparación para AI-901

Lecciones 1–3: qué vas a construir, requisitos del entorno y cómo usar prácticas, código y cuestionarios.

### Sección 2 · Conceptos de IA y Responsible AI

Lecciones 4–8: tipos de problema, cargas de trabajo, GenAI y tokens, y los seis principios de Responsible AI.

- Quiz: [`cuestionario_01.md`](quizzes/cuestionario_01.md) · Respuestas: [`cuestionario_01_respuestas.md`](quizzes/cuestionario_01_respuestas.md)

### Sección 3 · Microsoft Foundry: modelos y deployments

Lecciones 9–13: recursos y projects de Foundry, selección de modelos, deployment, región, cuotas, acceso y limpieza.

- Práctica: [`practica_01_desplegar_y_probar_un_modelo.md`](practices/practica_01_desplegar_y_probar_un_modelo.md)
- Datos: `data/prueba_playground.txt`
- Quiz: [`cuestionario_02.md`](quizzes/cuestionario_02.md) · Respuestas: [`cuestionario_02_respuestas.md`](quizzes/cuestionario_02_respuestas.md)

### Sección 4 · Prompt engineering y aplicaciones de Generative AI

Lecciones 14–19: system y user prompts, contexto y formato de salida, y un cliente de chat con el Foundry SDK.

| Lección | Código | Datos |
|---|---|---|
| 15 · Contexto, instrucciones y formato de salida | | `prompt_clasificacion.txt` |
| 16 · Predice la respuesta y mejora un prompt | | `prompt_mejorado.txt` |
| 17 · Demo: cliente de chat con Foundry SDK | [`chat_luma.py`](chat_luma.py) | |
| 18 · Lectura del código, autenticación y configuración | [`chat_key.py`](chat_key.py) | |
| 19 · Comprobación de resultados y limitaciones | [`validar_respuesta.py`](validar_respuesta.py) | |

- Práctica: [`practica_02_prompts_y_cliente_de_chat.md`](practices/practica_02_prompts_y_cliente_de_chat.md)
- Quiz: [`cuestionario_03.md`](quizzes/cuestionario_03.md) · Respuestas: [`cuestionario_03_respuestas.md`](quizzes/cuestionario_03_respuestas.md)

### Sección 5 · AI Agents con Microsoft Foundry

Lecciones 20–24: modelo, aplicación y agente; instrucciones, herramientas y alcance; crear y consumir un single-agent.

| Lección | Código | Datos |
|---|---|---|
| 21 · Instrucciones, herramientas y alcance del agente | | `instrucciones_luma_agent.txt` |
| 22 · Demo: crear y probar un single-agent | | `instrucciones_luma_agent.txt`, `politicas_luma.docx` |
| 23 · Demo: cliente de Python para el agente | [`agente_luma.py`](agente_luma.py) | |

- Práctica: [`practica_03_crear_y_consumir_un_agente.md`](practices/practica_03_crear_y_consumir_un_agente.md)
- Quiz: [`cuestionario_04.md`](quizzes/cuestionario_04.md) · Respuestas: [`cuestionario_04_respuestas.md`](quizzes/cuestionario_04_respuestas.md)

> El cliente del agente requiere **Microsoft Entra ID** (`az login`); `AIProjectClient` no admite API key.

### Sección 6 · Text Analysis y Azure Language

Lecciones 25–29: entidades, sentimiento, keywords y resumen con un modelo general y con Azure Language.

| Lección | Código | Datos |
|---|---|---|
| 27 · Demo: Text Analysis con un modelo general | [`analizar_ticket.py`](analizar_ticket.py) | `ticket_8413.txt`, `ticket_positivo.txt`, `ticket_ingles.txt` |
| 28 · Demo: respuestas estructuradas con Azure Language | [`lenguaje_luma.py`](lenguaje_luma.py) | `etiqueta_aleman.txt` |

- Práctica: [`practica_04_text_analysis_y_azure_language.md`](practices/practica_04_text_analysis_y_azure_language.md)

### Sección 7 · Speech, audio y modelos multimodales

Lecciones 30–33: speech recognition, speech synthesis y prompts hablados con un modelo multimodal.

| Lección | Código | Datos |
|---|---|---|
| 31 · Demo: responder a un prompt hablado con un modelo multimodal | [`pregunta_hablada.py`](pregunta_hablada.py) | `pregunta.wav`, `pregunta_molesta.wav` |
| 32 · Demo: aplicación con Azure Speech en Foundry Tools | [`voz_luma.py`](voz_luma.py) | `mensaje.wav` |

- Práctica: [`practica_05_speech_y_audio.md`](practices/practica_05_speech_y_audio.md)
- Quiz: [`cuestionario_05.md`](quizzes/cuestionario_05.md) · Respuestas: [`cuestionario_05_respuestas.md`](quizzes/cuestionario_05_respuestas.md)

### Sección 8 · Computer Vision y generación de imágenes

Lecciones 34–38: interpretar imágenes con un prompt, generar imágenes y crear una aplicación ligera con visión.

| Lección | Código | Datos |
|---|---|---|
| 35 · Demo: interpretar una imagen con un prompt | | `router_cliente.jpg`, `router_jose_borrosa.jpg` |
| 36 · Demo: generar una imagen a partir de una descripción | [`generar_imagen.py`](generar_imagen.py) | |
| 37 · Demo: aplicación ligera con capacidades de visión | [`vision_luma.py`](vision_luma.py) | `router_cliente.jpg` |
| 38 · Comprobación de resultados visuales | | `router_jose_borrosa.jpg` |

- Práctica: [`practica_06_vision_y_generacion_de_imagenes.md`](practices/practica_06_vision_y_generacion_de_imagenes.md)

### Sección 9 · Content Understanding y extracción de información

Lecciones 39–43: extracción de campos de documentos, imágenes, audio y video con Content Understanding.

| Lección | Código | Datos |
|---|---|---|
| 40 · Demo: extraer campos de documentos y formularios | | `Factura_Luma.pdf`, `recibo_luma.jpg` |
| 41 · Demo: extracción de una imagen | | `etiqueta_router.jpg`, `etiqueta_router_reflejo.jpg` |
| 42 · Demo: extracción de audio y video | | `llamada_soporte.wav`, `video_router.mp4` |
| 43 · Demo: cliente ligero y comprobación de campos | [`extraer_factura.py`](extraer_factura.py) | `Factura_Luma.pdf` |

- Práctica: [`practica_07_content_understanding.md`](practices/practica_07_content_understanding.md)
- Quiz: [`cuestionario_06.md`](quizzes/cuestionario_06.md) · Respuestas: [`cuestionario_06_respuestas.md`](quizzes/cuestionario_06_respuestas.md)

### Sección 10 · Proyecto práctico: Luma Soporte AI

Lecciones 44–46: resuelves la solicitud completa de José reutilizando el chat, el agente, la voz, la visión y la extracción de documentos.

| Lección | Código | Datos |
|---|---|---|
| 44 · Luma Soporte: resolver una solicitud con evidencia | | `correo_jose.txt`, `router_jose.jpg` |
| 45 · Demo: reutilizar chat, agente y extracción | [`luma_caso.py`](luma_caso.py) | `mensaje_jose.wav` |
| 46 · Resolver fallos de acceso, cuota y configuración | | |

- Práctica: [`practica_08_caso_completo_luma_soporte.md`](practices/practica_08_caso_completo_luma_soporte.md)

### Sección 11 · Repaso final y preparación para el examen

Lecciones 47–48: mapa de repaso por dominio, simulacro y plan de estudio de 7 días.

- Simulacro: [`simulacro.md`](mock-exam/simulacro.md)
- Respuestas y hoja de resultados por área: [`simulacro_respuestas.md`](mock-exam/simulacro_respuestas.md)

---

## Solución de problemas

Cuando algo falle, revisa en este orden: **código → endpoint → identidad → deployment → cuota** (Lección 46).

| Código | Significado habitual | Qué revisar |
|---|---|---|
| **401** | Autenticación | `az login`, la API key o la variable de entorno correcta |
| **403** | Autorización | El rol asignado a tu identidad en el recurso de Foundry |
| **404** | Deployment o endpoint incorrecto | `MODEL_DEPLOYMENT_NAME` y el endpoint en `.env` |
| **429** | Límite de cuota o de ritmo | La cuota del deployment; espera y vuelve a intentarlo |

## Recursos de Microsoft Learn

- [Curso oficial AI-901T00](https://learn.microsoft.com/es-es/training/courses/ai-901t00?WT.mc_id=AZ-MVP-5000671)
- [Learning path: conceptos de IA](https://learn.microsoft.com/es-es/training/paths/ai-concepts/?WT.mc_id=AZ-MVP-5000671)
- [Learning path: aplicaciones y agentes de IA en Azure](https://learn.microsoft.com/es-es/training/paths/get-started-ai-apps-agents/?WT.mc_id=AZ-MVP-5000671)
- [Practice assessments para certificaciones de Microsoft](https://learn.microsoft.com/es-es/credentials/certifications/practice-assessments-for-microsoft-certifications?WT.mc_id=AZ-MVP-5000671)
- [Control de acceso basado en roles en Microsoft Foundry](https://learn.microsoft.com/es-es/azure/foundry/concepts/rbac-foundry?WT.mc_id=AZ-MVP-5000671)

## Siguientes pasos

- Certifícate en **AI-901**.
- Amplía lo aprendido con [RAG](https://learn.microsoft.com/es-es/training/modules/rag-fundamentals/?WT.mc_id=AZ-MVP-5000671) y [Foundry IQ](https://learn.microsoft.com/es-es/training/modules/get-started-foundry-iq/?WT.mc_id=AZ-MVP-5000671).
- Extiende Luma Soporte con tus propios casos.
- Avanza hacia [Azure AI Engineer Associate](https://learn.microsoft.com/es-es/credentials/certifications/azure-ai-engineer/?WT.mc_id=AZ-MVP-5000671).

## Autor

**Dave R** · Microsoft MVP

- Artículos sobre Azure y Microsoft Foundry: [medium.com/@daverendon](https://medium.com/@daverendon)

## Licencia

© 2026 Dave Rendon. **Todos los derechos reservados.**

Puedes clonar, ejecutar y modificar este material **solo para tu aprendizaje personal** y para preparar el examen AI-901. No está permitido redistribuirlo, publicarlo, venderlo, usarlo para impartir formación, reutilizar los cuestionarios o el simulacro, ni usarlo para entrenar modelos de IA sin una licencia comercial previa, por escrito y de pago. Cualquier uso autorizado debe dar crédito completo al autor.

Consulta los términos completos en [LICENSE](LICENSE).

Microsoft, Azure y Microsoft Foundry son marcas comerciales de Microsoft. Este curso no está afiliado ni respaldado por Microsoft.
