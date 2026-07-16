# Guía de Contribución

Bienvenido a **TechMind – Organización Inteligente del Conocimiento Técnico**.

Este documento describe la forma oficial de colaborar en el proyecto y las buenas prácticas que deberá seguir todo el equipo durante el desarrollo.

---

# 1. Objetivo

El objetivo de esta guía es mantener un proceso de desarrollo ordenado, consistente y alineado con la arquitectura definida para el proyecto.

Todas las contribuciones deberán respetar la documentación oficial y los estándares establecidos.

---

# 2. Antes de Comenzar

Antes de desarrollar una nueva funcionalidad, es recomendable revisar la documentación disponible.

- README.md
- Software Design Specification (SDS)
- Architecture Decision Records (ADR)
- System Architecture
- Repository Structure
- Engineering Standards
- Technical Roadmap

Comprender la arquitectura antes de escribir código reducirá retrabajos y facilitará la integración de cambios.

---

# 3. Flujo de Trabajo

El proyecto utiliza una estrategia de ramas basada en Git Flow simplificado.

```text
main
│
└── develop
    │
    ├── feature/backend
    ├── feature/data-science
    ├── feature/frontend
    ├── feature/documentation
    └── feature/devops
```

## main

Contiene únicamente versiones estables del proyecto.

No se desarrollan funcionalidades directamente sobre esta rama.

---

## develop

Es la rama principal de integración.

Todas las nuevas funcionalidades deberán integrarse primero en esta rama.

---

## feature/*

Cada funcionalidad se desarrolla en una rama independiente.

Ejemplos:

```text
feature/backend

feature/frontend

feature/data-science

feature/documentation
```

---

# 4. Clonar el Proyecto

```bash
git clone <URL_DEL_REPOSITORIO>

cd TechMind
```

Cambiar a la rama de desarrollo:

```bash
git checkout develop
```

Crear una nueva rama:

```bash
git checkout -b feature/nombre-funcionalidad
```

---

# 5. Convención de Ramas

Utilizar nombres descriptivos.

Ejemplos:

```text
feature/backend-api

feature/model-training

feature/frontend-ui

feature/documentation

feature/tests
```

Evitar nombres genéricos como:

```text
prueba

cambios

nuevo

test
```

---

# 6. Convención de Commits

Los mensajes de commit deberán ser claros y descriptivos.

Ejemplos:

```text
feat: add prediction endpoint

fix: correct preprocessing pipeline

docs: update system architecture

refactor: simplify classifier service

test: add backend unit tests
```

Prefijos recomendados:

| Prefijo | Uso |
|----------|-----|
| feat | Nueva funcionalidad |
| fix | Corrección de errores |
| docs | Documentación |
| refactor | Refactorización |
| test | Pruebas |
| chore | Tareas de mantenimiento |

---

# 7. Pull Requests

Antes de crear un Pull Request verificar:

- El código compila correctamente.
- Las pruebas existentes continúan funcionando.
- No se introducen cambios fuera del alcance de la funcionalidad.
- La documentación se actualiza cuando corresponde.

Todo Pull Request deberá dirigirse hacia la rama `develop`.

---

# 8. Revisión de Código

Durante la revisión se verificará:

- Cumplimiento de la arquitectura.
- Cumplimiento de los estándares.
- Legibilidad del código.
- Ausencia de duplicación.
- Simplicidad de la solución.
- Calidad general de la implementación.

---

# 9. Buenas Prácticas

- Mantener funciones pequeñas.
- Evitar duplicación de código.
- Escribir código legible.
- Utilizar nombres descriptivos.
- Documentar únicamente cuando aporte valor.
- Mantener sincronizada la documentación con la implementación.
- Respetar los principios KISS, bajo acoplamiento y alta cohesión.

---

# 10. Documentación Oficial

La documentación del proyecto se encuentra en el directorio `docs/`.

Antes de proponer cambios arquitectónicos, consultar:

- Software Design Specification (SDS)
- Architecture Decision Records (ADR)
- System Architecture
- Repository Structure
- Engineering Standards

---

# 11. Contacto del Equipo

Las dudas relacionadas con arquitectura o decisiones técnicas deberán discutirse con el equipo antes de ser implementadas.

La arquitectura aprobada constituye la línea base del proyecto y no deberá modificarse sin una justificación técnica.