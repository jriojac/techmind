
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
# ADR-005 – Exclusión de IA Generativa y Arquitecturas Avanzadas del Alcance del MVP

| Campo | Valor |
|--------|-------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **ADR** | 005 |
| **Estado** | Aceptado |
| **Versión** | 1.0 |
| **Fecha** | Julio 2026 |

---

# 1. Contexto

Durante la etapa de diseño arquitectónico se evaluó la posibilidad de incorporar tecnologías de Inteligencia Artificial Generativa y arquitecturas avanzadas para el procesamiento de contenido técnico.

Estas tecnologías ofrecen capacidades importantes para aplicaciones basadas en lenguaje natural, pero también introducen dependencias, infraestructura y complejidad adicionales.

Era necesario determinar si dichas tecnologías aportaban un valor proporcional a los objetivos definidos para el MVP del Hackathon ONE.

---

# 2. Problema

Era necesario establecer el alcance tecnológico del proyecto para:

- Mantener una arquitectura simple.
- Reducir la complejidad técnica.
- Cumplir los objetivos del MVP.
- Facilitar el desarrollo dentro del tiempo disponible.
- Minimizar dependencias externas.
- Favorecer el mantenimiento y la comprensión del sistema.

---

# 3. Decisión

Se excluye del alcance del MVP el uso de tecnologías de Inteligencia Artificial Generativa y arquitecturas avanzadas de procesamiento de lenguaje.

Entre las tecnologías excluidas se encuentran:

- Modelos de Lenguaje de Gran Escala (LLM).
- Arquitecturas Retrieval-Augmented Generation (RAG).
- LangChain.
- LangGraph.
- CrewAI.
- AutoGen.
- Agentes de Inteligencia Artificial.
- Bases de datos vectoriales.
- Frameworks de orquestación para IA Generativa.

El sistema se desarrollará utilizando exclusivamente técnicas de Machine Learning clásico, de acuerdo con la arquitectura definida en el SDS.

---

# 4. Justificación

La evaluación técnica concluyó que las funcionalidades requeridas por el MVP pueden implementarse mediante algoritmos tradicionales de Machine Learning.

La incorporación de tecnologías de IA Generativa aumentaría significativamente la complejidad de la arquitectura sin proporcionar un beneficio proporcional para el alcance del proyecto.

Esta decisión permite mantener una solución más sencilla, reproducible, de menor costo operativo y más fácil de comprender y mantener.

Asimismo, reduce la dependencia de servicios externos y facilita el despliegue del sistema.

---

# 5. Alternativas Evaluadas

## Modelos de Lenguaje de Gran Escala (LLM)

**Resultado:** No seleccionados.

Se descartaron por incrementar la complejidad del sistema y exceder las necesidades funcionales del MVP.

---

## Arquitecturas RAG

**Resultado:** No seleccionadas.

Requieren componentes adicionales como bases de datos vectoriales y mecanismos de recuperación que no aportan un beneficio proporcional para este proyecto.

---

## Frameworks para IA Generativa

**Resultado:** No seleccionados.

Herramientas como LangChain, LangGraph, CrewAI y AutoGen fueron evaluadas, pero se concluyó que introducirían una complejidad innecesaria para el alcance definido.

---

# 6. Consecuencias

## Positivas

- Arquitectura significativamente más simple.
- Menor complejidad de desarrollo.
- Reducción de dependencias externas.
- Menor consumo de recursos.
- Mayor facilidad de mantenimiento.
- Resultados reproducibles.
- Menor riesgo técnico durante el Hackathon.

## Negativas

- El sistema no contará con capacidades generativas propias de los LLM.
- Algunas funcionalidades avanzadas podrán considerarse únicamente en futuras versiones del proyecto.

---

# 7. Impacto Arquitectónico

Esta decisión define el límite tecnológico del MVP y condiciona el diseño de todos los componentes del sistema.

La arquitectura queda orientada exclusivamente al uso de técnicas de Machine Learning clásico, preservando la simplicidad y la separación de responsabilidades establecidas en el SDS.

La incorporación futura de tecnologías de IA Generativa requerirá una nueva evaluación arquitectónica y la emisión de un ADR que sustituya o complemente esta decisión.

---

# 8. Referencias

- SDS v0.1 – Capítulo 2. Filosofía del Proyecto.
- SDS v0.1 – Capítulo 4. Contexto del Proyecto.
- SDS v0.1 – Capítulo 5. Alcance del MVP.
- SDS v0.1 – Capítulo 6. Arquitectura General.
- ADR-002 – Adopción de Machine Learning Clásico.

---

# Estado

**Aceptado**

Esta decisión permanecerá vigente durante todo el desarrollo del MVP y garantiza que la arquitectura permanezca alineada con los principios de simplicidad, bajo acoplamiento y desarrollo incremental definidos para TechMind.