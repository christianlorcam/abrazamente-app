# Orden de archivos
| ├── database
| └── database.sql
| ├── script
| └── script.js
└── index.html
└── style.css


# Plataforma Práctica de Salud Mental (MVP Beta 2 Semanas)

[cite_start]Este repositorio contiene el código fuente del Producto Mínimo Viable (MVP) para la Plataforma Práctica de Salud Mental, desarrollado bajo un enfoque ágil y psicoeducativo práctico en un ciclo de 2 semanas[cite: 1, 2, 3]. [cite_start]El sistema prioriza la autogestión diaria y la utilidad clínica inmediata sobre la teoría extensa[cite: 3, 5].

## 🛠️ Stack Tecnológico
* [cite_start]**Frontend:** HTML5, CSS3 (Responsive) y Vanilla JavaScript (ES6+)[cite: 4, 28].
* [cite_start]**Backend/Base de Datos:** Arquitectura ligera e independiente [cite: 4] [cite_start]con un modelo relacional para la gestión de usuarios, profesionales y formularios[cite: 27, 28].

---

## 🚀 Funcionalidades del MVP (Alcance Actual)

### [cite_start]1. Botiquín de Ayuda Inmediata y Explorador [cite: 8]
* [cite_start]**Ejercicios de Respiración:** Temporizador y reproductor interactivo guiado mediante JavaScript utilizando la técnica de caja (4-4-4-4)[cite: 9, 28].
* [cite_start]**Botón de Grounding:** Módulo interactivo basado en la técnica de enraizamiento 5-4-3-2-1[cite: 9].
* [cite_start]**Micro-Hábitos:** Tarjetas interactivas con acciones diarias simples basadas en Terapia Cognitivo Conductual (TCC)[cite: 10].

### [cite_start]2. Biblioteca Práctica y Monetización [cite: 11]
* [cite_start]**Material Rotativo:** Sección con liberación semanal de recursos gratuitos (videos, infografías o documentos cortos)[cite: 12].
* [cite_start]**Librería Recomendada (Afiliados Amazon):** Integración de enlaces de afiliado de Amazon para libros de autoayuda con rigor científico, crecimiento personal y organización[cite: 13, 14].

### [cite_start]3. Portal Exclusivo para Profesionales [cite: 15]
* [cite_start]**Material Clínico Descargable:** Repositorio privado para la descarga de fichas de atención, pautas de evaluación para supervisores y material de apoyo estandarizado[cite: 16].
* [cite_start]**Feedback y Mejora:** Sistema integrado de encuestas de pacientes y buzón de sugerencias operativo para optimizar el entorno virtual[cite: 17].

### [cite_start]4. Directorio Profesional y Derivación [cite: 18]
* [cite_start]**Vitrina Segmentada:** Listado clasificado de psicólogos, coaches y voluntarios/practicantes[cite: 19].
* [cite_start]**Políticas de Acceso:** Sistema de primera sesión gratuita para estudiantes en práctica[cite: 20].
* [cite_start]**Filtros de Búsqueda:** Clasificación lógica por áreas: Salud Mental, Desarrollo Profesional y Salud Alternativa/Holística[cite: 21].

---

## 👥 Asignación de Roles del Equipo

[cite_start]El desarrollo técnico y la documentación se distribuyen bajo la siguiente estructura de responsabilidades[cite: 22]:

| Área | Integrantes |
| :--- | :--- |
| **HTML y CSS (Frontend)** | [cite_start]Christian, Camila, Ariel, Jean Paul [cite: 23] |
| **Script (JavaScript Frontend/Lógica)** | [cite_start]Ricardo, Jean Paul, Ariel (Apoyo) [cite: 23] |
| **Base de Datos / Backend** | [cite_start]Jean Paul, Benjamín, Ricardo [cite: 23] |
| **Diseño Visual (UX/UI, Figma)** | [cite_start]Christian, Nancy (Apoyo), Camila [cite: 23] |
| **Fundamentos (Justificación/Solución)** | [cite_start]Nancy [cite: 23] |
| **Información Educativa & Contenido** | [cite_start]Nancy [cite: 23] |

---

## 📅 Cronograma de Desarrollo (Sprint de 2 Semanas)

### [cite_start]Semana 1: Estructura, Diseño y Lógica Frontend [cite: 26]
* [cite_start]**Miércoles:** Redacción de fundamentos, diseño de wireframes básicos y definición del modelo relacional de la base de datos[cite: 27].
* [cite_start]**Jueves:** Mockups finales, maquetación de la estructura base (`index.html`, navbar, footer) y filtrado de las 5 técnicas del botiquín[cite: 27].
* [cite_start]**Viernes:** Implementación de estilos CSS responsive, programación de la lógica interactiva del botiquín (JS) y creación física de la base de datos y sus tablas fundamentales[cite: 28].

### [cite_start]Semana 2: Backend, Enlaces e Integración [cite: 29]
* [cite_start]**Lunes:** Carga de libros e inserción de enlaces de afiliados, maquetación del Portal de Profesionales y programación de la lógica de filtros del directorio[cite: 30].
* [cite_start]**Martes:** Conexión de los formularios de registro (pacientes/voluntarios) a la base de datos, validaciones de inputs frontend (RUT, email) y revisión de rigor científico/disclaimers[cite: 30].
* [cite_start]**Miércoles:** Refactorización y consistencia del CSS general, ejecución de consultas SQL (`SELECT`) para renderizar dinámicamente los profesionales en el DOM y cierre del documento técnico[cite: 30].
* **Jueves:** Fase de Testing, QA y control de usabilidad sobre el botiquín, links de Amazon y descargas clínicas. [cite_start]Resolución de bugs[cite: 30, 31].
* [cite_start]**Viernes:** Subida de código a GitHub, despliegue en servidor de hosting (GitHub Pages, Vercel o Netlify) y preparación de la defensa técnica de la versión Beta[cite: 31].