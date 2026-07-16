# TechMind

## Nombre del Documento

Versión: 0.1

Estado: Draft

Última actualización: Julio 2026

Autor: Equipo TechMind


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


# ADR-001 – Adopción de una Arquitectura Basada en Backend y Ciencia de Datos

| Campo | Valor |
|--------|-------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **ADR** | 001 |
| **Estado** | Aceptado |
| **Versión** | 1.0 |
| **Fecha** | Julio 2026 |

---

# 1. Contexto

TechMind se desarrolla como un Producto Mínimo Viable (MVP) para el Hackathon ONE – Oracle Next Education.

El proyecto requiere integrar un componente Backend y un componente de Ciencia de Datos para procesar contenido técnico mediante técnicas de Machine Learning clásico.

Debido al tiempo limitado del Hackathon y a la necesidad de facilitar el trabajo paralelo del equipo, era necesario definir una arquitectura simple, modular y fácil de mantener.

---

# 2. Problema

Era necesario definir una arquitectura que permitiera:

- Separar claramente las responsabilidades de cada componente.
- Facilitar el desarrollo paralelo entre Backend y Ciencia de Datos.
- Reducir el acoplamiento entre los componentes.
- Simplificar la integración del sistema.
- Facilitar el despliegue del MVP.
- Permitir futuras evoluciones sin modificar la arquitectura principal.

---

# 3. Decisión

Se adopta una arquitectura compuesta por tres componentes principales:

- Backend
- Ciencia de Datos
- Oracle Cloud Infrastructure (OCI)

El Backend constituye el único punto de acceso al sistema mediante una API REST.

El componente de Ciencia de Datos será responsable del procesamiento del contenido y de la ejecución del modelo de Machine Learning.

La comunicación entre ambos componentes se realizará mediante una llamada directa a la función pública:

```python
predict(title, text)
```

El componente de Ciencia de Datos no expondrá servicios HTTP ni APIs independientes.

---

# 4. Justificación

Esta arquitectura fue seleccionada porque proporciona un equilibrio adecuado entre simplicidad, modularidad y mantenibilidad.

La separación entre Backend y Ciencia de Datos permite que ambos componentes evolucionen de manera independiente mientras se mantiene un contrato de integración estable.

Asimismo, esta decisión reduce la complejidad de la solución, evita la incorporación de infraestructura adicional y facilita el cumplimiento de los objetivos del MVP dentro del tiempo disponible para el Hackathon.

La arquitectura también permite incorporar futuras mejoras en el modelo de Machine Learning sin afectar el funcionamiento del Backend.

---

# 5. Alternativas Evaluadas

## Arquitectura basada en Microservicios

**Resultado:** No seleccionada.

Aunque proporciona una alta independencia entre componentes, introduce complejidad adicional en aspectos como despliegue, comunicación, monitoreo y mantenimiento, lo cual no aporta un beneficio proporcional para un MVP.

---

## Exponer Ciencia de Datos mediante una API independiente

**Resultado:** No seleccionada.

Esta alternativa requería mantener dos servicios HTTP y gestionar la comunicación entre ellos, incrementando el acoplamiento operativo y la complejidad del despliegue.

---

## Arquitectura Monolítica

**Resultado:** Parcialmente considerada.

Aunque simplifica el despliegue, dificulta la separación de responsabilidades entre Backend y Ciencia de Datos y limita la evolución independiente de ambos componentes.

---

# 6. Consecuencias

## Positivas

- Arquitectura simple y fácil de comprender.
- Separación clara de responsabilidades.
- Bajo acoplamiento entre componentes.
- Desarrollo paralelo entre Backend y Ciencia de Datos.
- Integración sencilla mediante una interfaz estable.
- Facilita el mantenimiento y la evolución del sistema.
- Reduce la complejidad del despliegue.

## Negativas

- El Backend y el componente de Ciencia de Datos se ejecutan dentro del mismo proceso de la aplicación.
- Si en el futuro se requiere escalabilidad independiente para cada componente, será necesario revisar esta decisión arquitectónica.

---

# 7. Impacto Arquitectónico

Esta decisión constituye la base de toda la arquitectura del sistema.

Los demás componentes del proyecto fueron diseñados considerando esta separación de responsabilidades y el contrato de integración definido entre Backend y Ciencia de Datos.

Cualquier modificación a esta decisión deberá evaluarse cuidadosamente, ya que podría afectar el diseño general del sistema y requerir cambios en múltiples componentes.

---

# 8. Referencias

- SDS v0.1 – Capítulo 6. Arquitectura General.
- SDS v0.1 – Capítulo 7. Componente Backend.
- SDS v0.1 – Capítulo 8. Componente Ciencia de Datos.
- SDS v0.1 – Capítulo 10. Integración Backend ↔ Ciencia de Datos.

---

# Estado

**Aceptado**

Esta decisión arquitectónica permanecerá vigente durante el desarrollo del MVP y servirá como base para las futuras decisiones documentadas en los Architecture Decision Records (ADR) del proyecto.