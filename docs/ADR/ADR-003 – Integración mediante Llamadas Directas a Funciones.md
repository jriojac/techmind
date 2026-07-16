
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
# ADR-003 – Integración mediante Llamadas Directas a Funciones

| Campo | Valor |
|--------|-------|
| **Proyecto** | TechMind – Organización Inteligente del Conocimiento Técnico |
| **ADR** | 003 |
| **Estado** | Aceptado |
| **Versión** | 1.0 |
| **Fecha** | Julio 2026 |

---

# 1. Contexto

La arquitectura de TechMind está compuesta por un componente Backend y un componente de Ciencia de Datos.

Era necesario definir un mecanismo de integración que permitiera intercambiar información entre ambos componentes de forma simple, eficiente y con un bajo nivel de acoplamiento.

Esta decisión debía facilitar el desarrollo del MVP y permitir que ambos componentes evolucionaran de manera independiente.

---

# 2. Problema

Era necesario establecer un mecanismo de integración que permitiera:

- Intercambiar información entre Backend y Ciencia de Datos.
- Reducir la complejidad de la solución.
- Evitar infraestructura adicional.
- Facilitar el desarrollo y las pruebas.
- Mantener un contrato estable entre componentes.

---

# 3. Decisión

Se adopta una integración mediante llamadas directas a funciones.

El componente de Ciencia de Datos expone una única interfaz pública:

```python
predict(title, text)
```

El Backend invoca directamente esta función durante el procesamiento de cada solicitud.

No se utilizarán protocolos HTTP, RPC, colas de mensajes ni mecanismos de comunicación entre procesos para la integración interna del sistema.

---

# 4. Justificación

La integración mediante llamadas directas reduce significativamente la complejidad de la arquitectura.

Esta decisión elimina la necesidad de mantener múltiples servicios en ejecución, simplifica el despliegue y reduce el número de puntos de fallo durante la operación del sistema.

Además, permite que Backend y Ciencia de Datos trabajen de forma independiente mientras mantienen un contrato de integración claramente definido.

---

# 5. Alternativas Evaluadas

## API REST entre componentes

**Resultado:** No seleccionada.

Aunque permite desacoplar los componentes físicamente, introduce un segundo servicio HTTP, mayor complejidad operativa y latencia adicional que no aportan valor al MVP.

---

## Arquitectura basada en Microservicios

**Resultado:** No seleccionada.

Requiere mecanismos adicionales para despliegue, monitoreo y comunicación entre servicios, aumentando la complejidad del sistema sin un beneficio proporcional.

---

## Comunicación mediante colas de mensajes

**Resultado:** No seleccionada.

Este mecanismo está orientado a arquitecturas distribuidas y procesamiento asíncrono, escenarios que no forman parte del alcance del MVP.

---

# 6. Consecuencias

## Positivas

- Integración simple.
- Bajo acoplamiento.
- Fácil mantenimiento.
- Menor latencia.
- Despliegue simplificado.
- Menor consumo de recursos.
- Pruebas de integración más sencillas.

## Negativas

- Ambos componentes se ejecutan dentro del mismo proceso.
- La separación física entre componentes requerirá revisar esta decisión en futuras versiones del sistema.

---

# 7. Impacto Arquitectónico

Esta decisión define el mecanismo oficial de comunicación entre Backend y Ciencia de Datos.

Mientras el contrato de integración permanezca estable, ambos componentes podrán evolucionar internamente sin afectar el resto del sistema.

En futuras versiones, si los requerimientos de escalabilidad cambian, esta decisión podrá revisarse para incorporar mecanismos de comunicación distribuidos.

---

# 8. Referencias

- SDS v0.1 – Capítulo 6. Arquitectura General.
- SDS v0.1 – Capítulo 8. Componente Ciencia de Datos.
- SDS v0.1 – Capítulo 10. Integración Backend ↔ Ciencia de Datos.

---

# Estado

**Aceptado**

Esta decisión permanecerá vigente durante el desarrollo del MVP y establece el mecanismo oficial de integración entre los componentes principales del sistema.