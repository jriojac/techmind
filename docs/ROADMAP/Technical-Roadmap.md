# Technical Roadmap

# TechMind – Organización Inteligente del Conocimiento Técnico

| Campo | Valor |
|--------|-------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **Documento** | Technical Roadmap |
| **Clasificación** | Documentación Técnica |
| **Versión** | 1.1 |
| **Estado** | Vigente |
| **Fecha** | Julio 2026 |

---

# Control de Versiones

| Versión | Fecha | Autor(es) | Descripción |
|----------|-------|-----------|-------------|
| 1.0 | Julio 2026 | Equipo TechMind | Primera versión del Technical Roadmap. |
| 1.1 | Julio 2026 | Equipo TechMind | Actualización del Roadmap para alinearlo con el avance documentado del proyecto y los Sprints DS-01 a DS-04. |

---

# Tabla de Contenido

1. Objetivo
2. Alcance
3. Visión General
4. Roadmap del MVP
5. Evolución del Producto
6. Capacidades Futuras
7. Exclusiones
8. Referencias

---

# 1. Objetivo

El presente documento describe la evolución técnica prevista para TechMind desde la construcción del Producto Mínimo Viable (MVP) hasta futuras versiones del sistema.

Su propósito es proporcionar una visión estratégica de la evolución funcional y tecnológica del proyecto, manteniendo la coherencia con la arquitectura definida en el Software Design Specification (SDS) y con las decisiones registradas en los Architecture Decision Records (ADR).

Este documento no constituye un cronograma de desarrollo ni un plan de gestión del proyecto.

---

# 2. Alcance

El Technical Roadmap incluye:

- Evolución prevista del MVP.
- Evolución funcional del producto.
- Evolución técnica de los componentes del sistema.
- Capacidades previstas para futuras versiones.
- Visión de crecimiento del proyecto.

No forman parte de este documento:

- Especificación de la arquitectura.
- Decisiones arquitectónicas.
- Planificación detallada de tareas.
- Gestión del proyecto.
- Cronogramas operativos.

El Roadmap se actualizará progresivamente conforme los distintos componentes del proyecto generen documentación técnica aprobada.

---

# 3. Visión General

TechMind evoluciona mediante incrementos técnicos que incorporan nuevas capacidades al sistema sin modificar los principios arquitectónicos definidos en el Software Design Specification (SDS).

Cada Sprint representa un avance funcional documentado, permitiendo construir progresivamente una plataforma para la organización inteligente del conocimiento técnico.

El Roadmap refleja la evolución prevista del proyecto y se actualizará conforme los distintos componentes (Ciencia de Datos, Backend, Frontend e Infraestructura) incorporen nuevas funcionalidades y documentación técnica aprobada.

```mermaid
flowchart LR

idea["Idea"]

plan["Arquitectura"]

mvp["MVP"]

stable["Versión Estable"]

growth["Evolución del Producto"]

future["Capacidades Futuras"]

idea --> plan

plan --> mvp

mvp --> stable

stable --> growth

growth --> future
```

---

# 4. Roadmap Técnico del MVP

# 4. Roadmap del MVP

El desarrollo del MVP se realiza mediante Sprints técnicos que incorporan nuevas capacidades al proyecto de forma incremental.

Al momento de esta versión, el avance documentado corresponde principalmente al componente de Ciencia de Datos. Conforme otros componentes del proyecto generen documentación técnica aprobada, este Roadmap incorporará sus respectivos hitos.

| Sprint | Componente | Objetivo | Estado |
|---------|------------|----------|:------:|
| DS-01 | Ciencia de Datos | Definición de la arquitectura del componente | ✅ |
| DS-02 | Ciencia de Datos | Investigación y selección de fuentes de información | ✅ |
| DS-03 | Ciencia de Datos | Construcción del Dataset Maestro | ✅ |
| DS-04 | Ciencia de Datos | Limpieza, validación y preprocesamiento del dataset | ✅ |
| DS-05 | Ciencia de Datos | Ingeniería de características | ⏳ |
| DS-06 | Ciencia de Datos | Entrenamiento del modelo | ⏳ |
| DS-07 | Ciencia de Datos | Evaluación y optimización del modelo | ⏳ |
| DS-08 | Ciencia de Datos | Integración de inferencia y validación final | ⏳ |

> **Nota:** Este Roadmap representa el avance técnico documentado del proyecto hasta la fecha. Los hitos de Backend, Frontend, QA e Infraestructura se incorporarán conforme cada equipo publique su documentación técnica oficial.

---

# 5. Evolución del Producto

La evolución de TechMind se basa en la incorporación progresiva de capacidades funcionales y técnicas, preservando la arquitectura definida en el Software Design Specification (SDS).

Cada versión incrementa las capacidades del sistema sin comprometer los principios de modularidad, bajo acoplamiento y mantenibilidad.

---

## MVP v1.0

### Objetivo

Entregar una primera versión funcional capaz de clasificar documentación técnica mediante un modelo de Machine Learning integrado a una API REST.

### Capacidades

- API REST para clasificación de documentos.
- Construcción del Dataset Maestro.
- Pipeline de validación y preprocesamiento.
- Entrenamiento inicial del modelo.
- Clasificación automática de documentos.
- Documentación técnica completa.
- Despliegue inicial utilizando Oracle Cloud Infrastructure (OCI).

---

## Versión 1.1

### Objetivo

Incrementar la calidad del modelo y mejorar el rendimiento general del sistema.

### Capacidades

- Optimización del entrenamiento.
- Ajuste de hiperparámetros.
- Incorporación de nuevas métricas de evaluación.
- Mejora de la calidad de clasificación.
- Optimización del pipeline de procesamiento.

---

## Versión 2.0

### Objetivo

Consolidar una plataforma preparada para escenarios de mayor escala y evolución continua.

### Capacidades

- Versionado de modelos.
- Automatización del entrenamiento.
- Monitoreo del desempeño del modelo.
- Administración de múltiples modelos.
- Optimización del proceso de recomendación.
- Mejoras en observabilidad y mantenimiento.

---

# 6. Capacidades Futuras

Las siguientes capacidades podrán evaluarse una vez concluido el MVP y de acuerdo con las prioridades del proyecto.

| Categoría | Capacidad | Estado |
|-----------|-----------|--------|
| Machine Learning | Nuevos algoritmos de clasificación | Futuro |
| Machine Learning | Reentrenamiento programado | Futuro |
| Machine Learning | Versionado de modelos | Futuro |
| Machine Learning | Métricas avanzadas | Futuro |
| Automatización | Automatización del pipeline | Futuro |
| Backend | Versionado de API | Futuro |
| Plataforma | Dashboard administrativo | Futuro |

La incorporación de estas capacidades deberá evaluarse considerando la arquitectura vigente y las decisiones registradas en los Architecture Decision Records (ADR).

---

# 7. Exclusiones

El presente Roadmap describe la evolución técnica prevista para TechMind, pero no constituye un compromiso sobre funcionalidades futuras ni un plan detallado de implementación.

En esta versión no se consideran como parte del alcance:

- Implementación de modelos generativos (LLM).
- Arquitecturas RAG (Retrieval-Augmented Generation).
- Sistemas conversacionales o asistentes virtuales.
- Clasificación multilingüe.
- Clasificación multimodal (imágenes, audio o video).
- Procesamiento en tiempo real.
- Integraciones con sistemas de terceros.
- Automatizaciones no relacionadas con el proceso principal de clasificación.

Estas capacidades podrán evaluarse en futuras versiones del proyecto mediante nuevos requerimientos y decisiones arquitectónicas formalizadas en los Architecture Decision Records (ADR).

---

# 8. Referencias

La planificación descrita en este Roadmap se encuentra alineada con la documentación técnica oficial del proyecto.

## Documentación de Arquitectura

- Software Design Specification (SDS)
- Architecture Decision Records (ADR)

## Documentación de Ciencia de Datos

- DS-01 – Arquitectura del Componente de Ciencia de Datos
- DS-02 – Investigación y Selección del Dataset
- DS-03 – Construcción del Dataset Maestro
- DS-04 – Limpieza, Validación y Preprocesamiento
- DS-05 – Ingeniería de Características (Planificado)
- DS-06 – Entrenamiento del Modelo (Planificado)
- DS-07 – Evaluación y Optimización (Planificado)
- DS-08 – Integración e Inferencia (Planificado)

## Documentación del Proyecto

- Git Development Workflow
- README del repositorio