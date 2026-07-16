
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
# ADR-004 – Adopción de Oracle Cloud Infrastructure para el MVP

| Campo | Valor |
|--------|-------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **ADR** | 004 |
| **Estado** | Aceptado |
| **Versión** | 1.0 |
| **Fecha** | Julio 2026 |

---

# 1. Contexto

El proyecto TechMind requiere almacenar los artefactos generados durante el desarrollo y disponer de una infraestructura que permita publicar el MVP.

Adicionalmente, el Hackathon ONE establece como requisito la integración con al menos un servicio de Oracle Cloud Infrastructure (OCI).

Era necesario seleccionar una plataforma que permitiera cumplir este requerimiento manteniendo una arquitectura simple y alineada con los objetivos del proyecto.

---

# 2. Problema

Era necesario definir una infraestructura que permitiera:

- Almacenar los artefactos generados por el proyecto.
- Facilitar el despliegue del Backend.
- Cumplir los requisitos del Hackathon.
- Reducir la complejidad operativa.
- Permitir una evolución gradual del sistema.

---

# 3. Decisión

Se adopta Oracle Cloud Infrastructure (OCI) como plataforma de infraestructura para el MVP.

Inicialmente se utilizarán los siguientes servicios:

- OCI Object Storage para almacenar modelos, datasets y documentación.
- OCI Compute como opción para el despliegue del Backend cuando sea requerido.

La incorporación de nuevos servicios de OCI deberá justificarse en función de las necesidades del proyecto y del valor que aporten al MVP.

---

# 4. Justificación

Oracle Cloud Infrastructure satisface los requerimientos del Hackathon y proporciona los servicios necesarios para soportar la arquitectura definida en el SDS.

La utilización inicial de un número reducido de servicios mantiene la infraestructura simple y evita incrementar la complejidad operativa del proyecto.

Esta decisión también permite ampliar el uso de OCI en futuras versiones sin modificar la arquitectura general del sistema.

---

# 5. Alternativas Evaluadas

## Infraestructura completamente local

**Resultado:** No seleccionada.

Aunque simplifica el desarrollo inicial, no cumple con el requisito de integración con Oracle Cloud Infrastructure establecido por el Hackathon.

---

## Otros proveedores Cloud

**Resultado:** No seleccionados.

Servicios como AWS, Microsoft Azure o Google Cloud Platform ofrecen capacidades similares, pero no satisfacen el requerimiento específico del Hackathon de utilizar Oracle Cloud Infrastructure.

---

## Uso intensivo de múltiples servicios OCI

**Resultado:** No seleccionado.

Se descartó incorporar servicios adicionales que no aportaran valor directo al MVP, con el objetivo de mantener una infraestructura sencilla y fácil de administrar.

---

# 6. Consecuencias

## Positivas

- Cumplimiento de los requisitos del Hackathon.
- Infraestructura alineada con la arquitectura del sistema.
- Centralización de los artefactos del proyecto.
- Facilidad para futuras ampliaciones.
- Baja complejidad operativa.
- Integración sencilla con el Backend.

## Negativas

- Dependencia parcial de Oracle Cloud Infrastructure para determinadas funcionalidades.
- Posibles limitaciones asociadas a la disponibilidad de recursos o cuotas del entorno utilizado.

---

# 7. Impacto Arquitectónico

Esta decisión define la infraestructura oficial del MVP.

La arquitectura del sistema mantiene desacoplada la lógica de negocio de los servicios de infraestructura, permitiendo que futuras modificaciones en la plataforma puedan evaluarse sin afectar significativamente a los componentes Backend y Ciencia de Datos.

---

# 8. Referencias

- SDS v0.1 – Capítulo 6. Arquitectura General.
- SDS v0.1 – Capítulo 9. Infraestructura (OCI).
- SDS v0.1 – Capítulo 11. Evolución del MVP.

---

# Estado

**Aceptado**

Oracle Cloud Infrastructure constituye la plataforma de infraestructura adoptada para el desarrollo y despliegue del MVP de TechMind.