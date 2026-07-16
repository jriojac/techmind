# Plan de Implementación

## Proyecto

**TechMind – Organización Inteligente del Conocimiento Técnico**

---

# Objetivo

Definir la estrategia de implementación del proyecto manteniendo la arquitectura aprobada y aplicando un enfoque incremental que minimice riesgos técnicos y permita entregar valor al final de cada Sprint.

---

# Metodología

Se utilizará **Scrum adaptado para Hackathon**, con las siguientes características:

- Desarrollo incremental.
- Integración continua.
- Releases al finalizar cada Sprint.
- Pull Requests para integrar cambios.
- Rama `main` protegida.
- Arquitectura congelada durante la implementación.
- Documentación ligera y actualizada.

---

# Roadmap de Implementación

## Sprint 0 — Preparación del Proyecto

**Release:** `v0.1.0`

### Objetivo

Preparar el entorno de desarrollo y establecer la base del proyecto.

### Alcance

- Configuración del repositorio.
- Estructura inicial del proyecto.
- Convenciones de desarrollo.
- Estrategia de ramas.
- Configuración del entorno.
- Contratos entre Backend y Ciencia de Datos.
- Refinamiento del Product Backlog.

### Resultado esperado

Proyecto preparado para iniciar el desarrollo.

---

## Sprint 1 — Ciencia de Datos

**Release:** `v0.2.0`

### Objetivo

Construir y validar el modelo de clasificación.

### Alcance

- Dataset.
- Limpieza de datos.
- Análisis exploratorio (EDA).
- Vectorización TF-IDF.
- Entrenamiento del modelo.
- Evaluación.
- Exportación del modelo (`model.joblib`).
- Estructura base del Backend.

### Resultado esperado

Modelo entrenado listo para integrarse con la API.

---

## Sprint 2 — Backend e Integración

**Release:** `v0.3.0`

### Objetivo

Integrar el modelo de Ciencia de Datos con FastAPI.

### Alcance

- Configuración de FastAPI.
- Endpoint `POST /predict`.
- Carga del modelo mediante Joblib.
- Validaciones con Pydantic.
- Manejo de errores.
- Pruebas de integración.
- Documentación OpenAPI / Swagger.

### Resultado esperado

API REST completamente funcional.

---

## Sprint 3 — Entrega Final

**Release:** `v1.0.0`

### Objetivo

Preparar el producto para su presentación y despliegue.

### Alcance

- Docker.
- Despliegue en Oracle Cloud Infrastructure (OCI).
- Configuración final.
- Pruebas End-to-End.
- Optimización.
- Documentación final.
- Preparación de la demostración del Hackathon.

### Resultado esperado

Producto desplegado y listo para evaluación.

---

# Hitos

| Hito | Sprint | Resultado |
|------|--------|-----------|
| H1 | Sprint 0 | Proyecto preparado |
| H2 | Sprint 1 | Modelo entrenado |
| H3 | Sprint 2 | API REST funcional |
| H4 | Sprint 3 | Sistema desplegado |

---

# Releases

| Versión | Sprint | Descripción |
|----------|--------|-------------|
| v0.1.0 | Sprint 0 | Base del proyecto |
| v0.2.0 | Sprint 1 | Modelo entrenado |
| v0.3.0 | Sprint 2 | API REST integrada |
| v1.0.0 | Sprint 3 | Entrega final |

---

# Estrategia de Desarrollo

La implementación seguirá un enfoque incremental donde cada Sprint entregue un incremento funcional del sistema.

El orden de construcción será:

1. Preparación del proyecto.
2. Ciencia de Datos.
3. Integración con Backend.
4. Despliegue y entrega final.

Este enfoque permite reducir riesgos técnicos, validar tempranamente el modelo de Machine Learning y mantener una integración continua durante todo el Hackathon.