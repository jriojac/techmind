# Changelog

Todos los cambios relevantes del proyecto **TechMind** se documentan en este archivo.

Este documento registra la evolución funcional y técnica del proyecto, incluyendo los componentes de **Backend**, **Data Science** y, posteriormente, **Frontend**.

El formato utilizado sigue la especificación de **Keep a Changelog** y el versionado del proyecto utiliza **Semantic Versioning (SemVer)**.

---

## Tipos de Cambios

Las versiones podrán incluir las siguientes categorías:

- **Added** para nuevas funcionalidades.
- **Changed** para cambios en funcionalidades existentes.
- **Deprecated** para funcionalidades que serán eliminadas.
- **Removed** para funcionalidades eliminadas.
- **Fixed** para correcciones de errores.
- **Security** para mejoras relacionadas con seguridad.

---

## [Unreleased]

### Backend

- Desarrollo del componente Backend.

### Data Science

- Desarrollo del Sprint **DS-05 – Análisis Exploratorio de Datos (EDA)**.

### Frontend

- Pendiente de inicio.

---

## [0.4.0] - 2026-07-22

### Added

#### Data Science

##### Preprocesamiento

- Implementación de `TextCleaner`.
- Implementación de `TextNormalizer`.
- Implementación de `StopwordsRemover`.
- Implementación de `Tokenizer`.
- Implementación de `Lemmatizer`.
- Implementación de `PreprocessingPipeline`.

##### Validación

- Implementación de `DatasetValidator`.
- Implementación del modelo de validación del Dataset Maestro.
- Implementación de validaciones estructurales.
- Implementación de validaciones de columnas obligatorias.
- Implementación de validaciones de tipos de datos.

##### Scripts

- Implementación de `validation_runner.py`.
- Implementación de `dataset_validator.py`.
- Implementación de `preprocessing_validator.py`.
- Implementación de `quality_report.py`.
- Implementación de `benchmark.py`.

##### Testing

- Nuevas pruebas para el pipeline de preprocesamiento.
- Nuevas pruebas para los validadores del dataset.
- Nuevas pruebas para los componentes de limpieza y normalización.
- Incremento de la suite automatizada hasta **109 pruebas aprobadas**.

##### Documentación

- Reestructuración completa del `README.md` del componente Data Science.
- Actualización de la documentación técnica del pipeline.
- Actualización de la arquitectura del componente.
- Documentación de la estructura del repositorio.
- Documentación del proceso de preprocesamiento.

### Changed

#### Data Science

- Refactorización de la arquitectura del componente para mejorar la modularidad.
- Consolidación del Dataset Maestro como base del proceso de entrenamiento.
- Optimización del flujo de validación de datos.
- Estandarización del pipeline de preprocesamiento.
- Mejora de la organización interna del proyecto.

### Fixed

#### Data Science

- Correcciones menores detectadas durante la integración del pipeline.
- Ajustes en el proceso de validación del dataset.
- Corrección de inconsistencias en la documentación técnica.

---

## [0.3.0] - 2026-07-19

### Added

#### Data Science

##### Arquitectura de Adquisición de Datos

- Implementación de la arquitectura modular para la adquisición de documentos.
- Definición de la separación entre Readers, Loaders y modelos de dominio.
- Incorporación del patrón Factory para la creación de Readers y Loaders.

##### Readers

- Implementación de `BaseReader`.
- Implementación de `TextReader`.
- Implementación de `JsonReader`.
- Implementación de `CsvReader`.
- Implementación de `PdfReader`.
- Implementación de `ReaderFactory`.

##### Loaders

- Implementación de `BaseLoader`.
- Implementación de `GitHubLoader`.
- Implementación de `TechnicalDocsLoader`.
- Implementación de `StackExchangeLoader`.
- Implementación de `HuggingFaceLoader`.
- Implementación de `MockLoader`.
- Implementación de `LoaderFactory`.

##### Dataset Maestro

- Implementación del modelo de dominio `DocumentRecord`.
- Definición del esquema del Dataset Maestro.
- Integración de múltiples fuentes de información en un único modelo de datos.
- Incorporación del proceso de construcción del Dataset Maestro.

##### Testing

- Implementación de pruebas unitarias para Readers.
- Implementación de pruebas unitarias para Loaders.
- Implementación de pruebas para Factories.
- Validación del proceso de adquisición de datos.
- Incorporación de **61 pruebas automatizadas**.

##### Documentación

- Documentación de la arquitectura del componente.
- Documentación del proceso de adquisición del dataset.
- Documentación de la estructura inicial del proyecto.

### Changed

#### Data Science

- Consolidación de la arquitectura de adquisición basada en Readers y Loaders.
- Mejora de la organización interna del componente.
- Estandarización del modelo de datos utilizado durante la construcción del Dataset Maestro.

### Fixed

#### Data Science

- Correcciones menores derivadas de las pruebas de integración.
- Ajustes en la estructura de documentación del componente.

---

## [0.2.0] - 2026-07-15

### Added

#### Proyecto

##### Arquitectura

- Definición de la arquitectura general del proyecto TechMind.
- Aprobación de la arquitectura para los componentes Backend y Data Science.
- Definición del flujo de integración entre componentes.

##### Organización

- Organización inicial de la estructura del repositorio.
- Definición de la estructura de directorios del proyecto.
- Incorporación de la documentación técnica inicial.

##### Ingeniería

- Definición de los estándares de desarrollo.
- Definición de las convenciones de documentación.
- Definición del flujo de trabajo basado en Git.
- Planificación inicial del roadmap del proyecto.

##### Data Science

- Inicio del desarrollo del componente Data Science.
- Definición de la arquitectura del componente.
- Planificación de los Sprints DS-01 y DS-02.

##### Backend

- Inicio del desarrollo del componente Backend.
- Definición de la estrategia de integración con Data Science.

### Changed

#### Proyecto

- Consolidación de la organización técnica del repositorio.
- Estandarización de la documentación del proyecto.

---

## [0.1.0] - 2026-07-14

### Added

#### Proyecto

##### Inicialización

- Creación del repositorio del proyecto.
- Configuración inicial del entorno de desarrollo.
- Definición de la estructura base del repositorio.

##### Configuración

- Configuración inicial del control de versiones mediante Git.
- Incorporación de los archivos base del proyecto.
- Configuración inicial de dependencias.

##### Documentación

- Creación de la documentación inicial del proyecto.
- Definición de los documentos técnicos principales.
- Incorporación del archivo `README.md`.
- Incorporación del archivo `CHANGELOG.md`.

---
