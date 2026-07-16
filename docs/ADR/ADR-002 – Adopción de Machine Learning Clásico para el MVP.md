
---
| ADR     | Decisión                                                          | Tipo                   |
| ------- | ----------------------------------------------------------------- | ---------------------- |
| ADR-001 | Adopción de una Arquitectura Basada en Backend y Ciencia de Datos | Arquitectura           |
| ADR-002 | Adopción de Machine Learning Clásico para el MVP                  | Arquitectura           |
| ADR-003 | Integración mediante llamada directa a `predict()`                | Arquitectura           |
| ADR-004 | Backend como único punto de acceso al sistema                     | Arquitectura           |
| ADR-005 | Uso de Oracle Cloud Infrastructure                                | Infraestructura        |
| ADR-006 | Exclusión de IA Generativa y Arquitecturas RAG                    | Alcance Arquitectónico |


---
# ADR-002 – Adopción de Machine Learning Clásico para el MVP

| Campo | Valor |
|--------|-------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **ADR** | 002 |
| **Estado** | Aceptado |
| **Versión** | 1.0 |
| **Fecha** | Julio 2026 |

---

# 1. Contexto

TechMind tiene como objetivo organizar contenido técnico mediante técnicas de procesamiento de texto y aprendizaje automático.

Durante la etapa de diseño arquitectónico se evaluaron diferentes enfoques para resolver el problema, incluyendo modelos tradicionales de Machine Learning y tecnologías basadas en Inteligencia Artificial Generativa.

La solución debía satisfacer los objetivos funcionales del MVP, respetar el tiempo disponible del Hackathon y mantener una arquitectura simple, mantenible y de bajo costo operativo.

---

# 2. Problema

Era necesario seleccionar una estrategia de procesamiento de texto que permitiera:

- Clasificar contenido técnico.
- Extraer palabras clave relevantes.
- Recomendar documentos similares.
- Obtener resultados reproducibles.
- Reducir la complejidad del sistema.
- Facilitar el desarrollo y mantenimiento del MVP.

---

# 3. Decisión

Se adopta un enfoque basado en Machine Learning clásico utilizando algoritmos de Scikit-Learn.

La solución emplea principalmente:

- TF-IDF para la representación vectorial del texto.
- Logistic Regression para la clasificación.
- Cosine Similarity para la recomendación de contenido relacionado.
- Joblib para la persistencia de los artefactos del modelo.

Este enfoque constituye el núcleo del componente de Ciencia de Datos.

---

# 4. Justificación

Las técnicas de Machine Learning clásico permiten resolver los objetivos funcionales del MVP sin incorporar infraestructura adicional ni dependencias asociadas a modelos generativos.

La solución ofrece un comportamiento determinista, facilita la evaluación mediante métricas tradicionales y simplifica el proceso de entrenamiento y despliegue.

Asimismo, este enfoque reduce el consumo de recursos computacionales y elimina la dependencia de servicios externos durante la ejecución del sistema.

---

# 5. Alternativas Evaluadas

## Modelos de IA Generativa (LLM)

**Resultado:** No seleccionados.

Aunque ofrecen capacidades avanzadas de comprensión del lenguaje, exceden los requerimientos funcionales del MVP e incrementan significativamente la complejidad técnica y operativa del proyecto.

---

## Arquitecturas RAG

**Resultado:** No seleccionadas.

Requieren infraestructura adicional, almacenamiento vectorial y componentes que no aportan un beneficio proporcional para el alcance definido del Hackathon.

---

## Modelos basados en Deep Learning

**Resultado:** No seleccionados.

Su entrenamiento y mantenimiento demandan mayores recursos computacionales y un volumen de datos superior al disponible para el proyecto.

---

# 6. Consecuencias

## Positivas

- Arquitectura más simple.
- Fácil entrenamiento del modelo.
- Resultados reproducibles.
- Bajo consumo de recursos.
- Despliegue sencillo.
- Independencia de servicios externos.
- Menor complejidad de mantenimiento.

## Negativas

- Menor capacidad para comprender relaciones semánticas complejas.
- El rendimiento depende directamente de la calidad del dataset y del proceso de entrenamiento.

---

# 7. Impacto Arquitectónico

Esta decisión define el núcleo tecnológico del componente de Ciencia de Datos.

Todos los procesos de entrenamiento, predicción y recomendación fueron diseñados considerando un enfoque de Machine Learning clásico.

La adopción de modelos generativos en futuras versiones requerirá una revisión de esta decisión y probablemente implicará cambios significativos en la arquitectura del sistema.

---

# 8. Referencias

- SDS v0.1 – Capítulo 4. Contexto del Proyecto.
- SDS v0.1 – Capítulo 5. Alcance del MVP.
- SDS v0.1 – Capítulo 8. Componente Ciencia de Datos.
- SDS v0.1 – Capítulo 10. Integración Backend ↔ Ciencia de Datos.

---

# Estado

**Aceptado**

Esta decisión permanecerá vigente durante el desarrollo del MVP y establece la base tecnológica del componente de Ciencia de Datos.