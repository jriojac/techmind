# Guía de Contribución

Bienvenido a **TechMind – Organización Inteligente del Conocimiento Técnico**.

Este documento establece las normas, procesos y buenas prácticas que deben seguir todos los colaboradores del proyecto para garantizar un desarrollo consistente, mantenible y alineado con la arquitectura definida.

La guía aplica a todos los componentes del proyecto, incluyendo **Backend**, **Data Science**, **Frontend** (cuando esté disponible), **DevOps** y **Documentación**.

---

# Objetivo

El objetivo de esta guía es establecer un proceso de desarrollo uniforme que facilite la colaboración entre los diferentes equipos, reduzca retrabajos y garantice la calidad del software durante todo el ciclo de vida del proyecto.

Todas las contribuciones deberán respetar:

- La arquitectura aprobada del proyecto.
- Los estándares de ingeniería.
- Las decisiones arquitectónicas (ADR).
- La documentación oficial.
- Las convenciones de desarrollo definidas por el equipo.

---

# Organización del Proyecto

TechMind está organizado en componentes independientes, cada uno con responsabilidades claramente definidas.

| Componente | Responsabilidad |
|------------|-----------------|
| Backend | Implementación de la lógica de negocio, APIs, persistencia e integración con Data Science. |
| Data Science | Construcción del dataset, preprocesamiento, entrenamiento, evaluación e inferencia del modelo de Machine Learning. |
| Frontend | Desarrollo de la interfaz de usuario e integración con Backend. |
| DevOps | Automatización, integración continua, despliegue y monitoreo de la infraestructura. |
| Documentación | Mantenimiento de la documentación técnica y funcional del proyecto. |

Cada componente evoluciona mediante Sprints específicos, pero todos siguen los mismos estándares de desarrollo y comparten una única arquitectura del sistema.

---

# Antes de Comenzar

Antes de implementar una nueva funcionalidad, todos los colaboradores deberán revisar la documentación oficial del proyecto.

Se recomienda consultar, como mínimo, los siguientes documentos:

- `README.md`
- `CHANGELOG.md`
- Software Design Specification (SDS)
- Architecture Decision Records (ADR)
- System Architecture
- Repository Structure
- Engineering Standards
- Technical Roadmap

Comprender la arquitectura y las decisiones técnicas antes de escribir código facilita la integración de cambios, reduce retrabajos y mantiene la consistencia del proyecto.

---

# Flujo de Trabajo

Actualmente, el proyecto se encuentra en una etapa temprana de desarrollo (MVP), por lo que el flujo de trabajo se mantiene simple para facilitar la colaboración entre los integrantes del equipo.

En esta etapa, la rama principal del proyecto es:

```text
main
```

Los cambios desarrollados por los integrantes del equipo son revisados e integrados en el repositorio principal antes de su publicación.

Conforme el proyecto evolucione y aumente el número de colaboradores activos, podrá adoptarse una estrategia de ramas más robusta (por ejemplo, `develop` y `feature/*`), sin afectar la organización del repositorio.

---

# Sincronización del Repositorio

Antes de comenzar a trabajar, es recomendable obtener la versión más reciente del repositorio:

```bash
git pull origin main
```

Una vez finalizada la funcionalidad:

```bash
git add .

git commit -m "feat: descripción de la funcionalidad"

git push origin main
```

Nota: Durante el desarrollo del MVP, la estrategia de control de versiones podrá evolucionar conforme se incorporen nuevos colaboradores y aumente la complejidad del proyecto

---

# Estándares de Desarrollo

Todo el código incorporado al proyecto deberá cumplir con los estándares de calidad definidos por el equipo.

El objetivo no es únicamente desarrollar funcionalidades, sino construir un software mantenible, escalable y fácil de comprender para cualquier integrante del proyecto.

---

## Principios de Diseño

Durante el desarrollo deberán priorizarse los siguientes principios:

- Responsabilidad Única (Single Responsibility Principle).
- Bajo acoplamiento entre componentes.
- Alta cohesión dentro de cada módulo.
- Modularidad.
- Reutilización de código.
- Simplicidad en las soluciones (KISS).
- Evitar duplicación de código (DRY).
- Legibilidad antes que complejidad.

Estos principios deberán aplicarse tanto en Backend como en Data Science y en los futuros componentes del proyecto.

---

## Convenciones de Código

Antes de incorporar código al proyecto, verificar que:

- Los nombres de clases, funciones y variables sean descriptivos.
- Cada módulo tenga una única responsabilidad claramente definida.
- No existan fragmentos de código duplicados.
- Se eliminen comentarios o código temporal antes de integrar los cambios.
- La estructura del proyecto se mantenga consistente con la arquitectura aprobada.

---

## Documentación del Código

La documentación debe complementar el código, no reemplazarlo.

Se recomienda:

- Utilizar nombres claros para clases y funciones.
- Documentar únicamente cuando aporte contexto o facilite el mantenimiento.
- Mantener sincronizada la documentación técnica con la implementación.
- Actualizar los documentos oficiales cuando una modificación afecte la arquitectura o el funcionamiento del sistema.

---

# Convención de Commits

Los mensajes de commit deberán describir claramente el propósito del cambio.

Se recomienda utilizar la siguiente convención:

| Prefijo | Descripción |
|----------|-------------|
| `feat` | Nueva funcionalidad |
| `fix` | Corrección de errores |
| `docs` | Cambios en la documentación |
| `refactor` | Mejora de la estructura del código sin modificar su comportamiento |
| `test` | Incorporación o actualización de pruebas |
| `chore` | Tareas de mantenimiento o configuración |

Ejemplos:

```text
feat: implementar pipeline de preprocesamiento

fix: corregir validación del dataset

docs: actualizar README del componente

refactor: simplificar DataLoaderFactory

test: agregar pruebas para Tokenizer

chore: actualizar dependencias
```

---

# Pruebas y Aseguramiento de la Calidad

La calidad del software es responsabilidad de todos los integrantes del proyecto.

Antes de integrar cualquier cambio al repositorio, se deberá verificar que la funcionalidad implementada cumple con los estándares definidos por el equipo y no afecta el comportamiento del sistema.

---

## Lista de Verificación

Antes de integrar cambios, comprobar que:

- La funcionalidad implementada cumple con los requisitos definidos.
- No se introducen errores en funcionalidades existentes.
- El código mantiene la estructura y arquitectura aprobadas.
- La documentación relacionada ha sido actualizada, cuando corresponda.
- No existen archivos temporales, dependencias innecesarias o código sin utilizar.

---

## Pruebas

Siempre que sea posible, los cambios deberán ser validados mediante pruebas.

Dependiendo del componente, estas podrán incluir:

### Backend

- Pruebas unitarias.
- Pruebas de integración.
- Validación de APIs.

### Data Science

- Validación del Dataset Maestro.
- Validación del pipeline de preprocesamiento.
- Validación de Readers y Loaders.
- Validación de scripts de procesamiento.
- Ejecución de la suite de pruebas automatizadas.

---

## Calidad de la Documentación

La documentación forma parte del producto y debe mantenerse sincronizada con la implementación.

Cuando un cambio afecte la arquitectura, el funcionamiento del sistema o la organización del proyecto, deberán actualizarse los documentos correspondientes.

Entre ellos:

- README.md
- CHANGELOG.md
- Software Design Specification (SDS)
- Architecture Decision Records (ADR)
- Technical Roadmap
- Engineering Standards

---

# Integración de Cambios

Durante la etapa actual del proyecto (MVP), la integración de cambios se realiza directamente sobre la rama principal del repositorio.

Antes de incorporar una nueva funcionalidad, se recomienda verificar que:

- El código ha sido probado.
- La funcionalidad cumple con el alcance definido.
- No existen conflictos con el trabajo realizado previamente.
- La documentación permanece actualizada.

El objetivo es mantener un historial de cambios claro, estable y fácil de mantener.

---

# Buenas Prácticas

Durante el desarrollo del proyecto se recomienda seguir las siguientes prácticas:

- Implementar una única funcionalidad a la vez.
- Mantener los cambios pequeños y fáciles de revisar.
- Priorizar la claridad del código sobre soluciones complejas.
- Evitar duplicación de código.
- Mantener una estructura modular.
- Respetar la arquitectura aprobada.
- Documentar los cambios relevantes.
- Mantener sincronizada la documentación con la implementación.
- Compartir las decisiones técnicas con el equipo antes de realizar cambios arquitectónicos.

---

# Documentación Oficial

La documentación técnica del proyecto se encuentra organizada en el directorio `docs/`.

Antes de realizar modificaciones importantes, se recomienda consultar la documentación oficial del proyecto para garantizar que los cambios sean consistentes con la arquitectura y los estándares establecidos.

Los principales documentos son:

- README
- CHANGELOG
- Software Design Specification (SDS)
- Architecture Decision Records (ADR)
- System Architecture
- Technical Roadmap
- Engineering Standards

---

# Consideraciones Finales

TechMind es un proyecto desarrollado de forma colaborativa y orientado a la construcción de una plataforma mantenible, escalable y de alta calidad.

El cumplimiento de esta guía contribuye a mantener la consistencia del código, facilitar la colaboración entre los integrantes del equipo y reducir el esfuerzo de mantenimiento a medida que el proyecto evoluciona.

---

