# Repository Structure

**Proyecto:** TechMind – Organización Inteligente del Conocimiento Técnico

**Versión:** 1.0

**Estado:** Aprobado

---

# 1. Propósito

Este documento describe la organización oficial del repositorio del proyecto **TechMind**.

Su objetivo es establecer una estructura consistente para el código fuente, la documentación, los modelos entrenados y las pruebas, facilitando el mantenimiento, la colaboración y la evolución del sistema.

La estructura aquí definida constituye la organización oficial del repositorio y deberá ser respetada durante todo el ciclo de vida del proyecto.

---

# 2. Organización General

El proyecto se organiza siguiendo una arquitectura monolítica modular.

Cada directorio posee una única responsabilidad claramente definida, evitando mezclar componentes de diferentes capas del sistema.

La estructura prioriza:

- Simplicidad.
- Separación de responsabilidades.
- Bajo acoplamiento.
- Alta cohesión.
- Facilidad de mantenimiento.

---

# 3. Estructura del Repositorio

```text
TechMind/
│
├── docs/
│   ├── ADR/
│   ├── Architecture/
│   ├── Roadmap/
│   ├── SDS/
│   └── Standards/
│
├── src/
│   ├── api/
│   ├── core/
│   ├── data_science/
│   ├── models/
│   └── utils/
│
├── tests/
│
├── datasets/
│
├── artifacts/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# 4. Descripción de Directorios

| Directorio | Responsabilidad |
|------------|-----------------|
| docs/ | Documentación oficial del proyecto. |
| src/ | Código fuente de la aplicación. |
| src/api/ | Endpoints y configuración del Backend FastAPI. |
| src/core/ | Configuración, constantes y lógica compartida. |
| src/data_science/ | Procesamiento de datos y ejecución del modelo de Machine Learning. |
| src/models/ | Modelos serializados y recursos asociados utilizados por la aplicación. |
| src/utils/ | Funciones auxiliares reutilizables. |
| tests/ | Pruebas unitarias e integración. |
| datasets/ | Conjuntos de datos utilizados para entrenamiento y evaluación. |
| artifacts/ | Modelos entrenados, métricas y otros artefactos generados durante el entrenamiento. |

---

# 5. Organización del Código Fuente

El directorio `src/` contiene exclusivamente el código fuente del sistema.

Cada módulo representa una responsabilidad específica dentro de la arquitectura.

No deberá existir lógica de negocio duplicada entre módulos.

La comunicación entre el Backend y el componente de Ciencia de Datos se realiza mediante la función pública:

```python
predict(title, text)
```

No deberán implementarse llamadas HTTP internas entre componentes.

---

# 6. Organización de la Documentación

Toda la documentación técnica del proyecto se almacena en el directorio `docs/`.

Cada categoría posee una responsabilidad específica.

| Carpeta | Contenido |
|----------|-----------|
| SDS | Diseño del software. |
| ADR | Decisiones arquitectónicas. |
| Architecture | Documentación técnica de arquitectura. |
| Roadmap | Evolución del proyecto. |
| Standards | Estándares de desarrollo. |

No deberán crearse nuevas categorías documentales sin una justificación arquitectónica.

---

# 7. Organización de Pruebas

Todas las pruebas deberán almacenarse dentro del directorio `tests/`.

La estructura de pruebas deberá reflejar la organización del código fuente siempre que sea posible.

Ejemplo:

```text
tests/
│
├── api/
├── core/
├── data_science/
└── utils/
```

Las pruebas deberán mantenerse independientes entre sí y ejecutarse de forma automatizada.

---

# 8. Convenciones del Repositorio

Para mantener la consistencia del proyecto se establecen las siguientes convenciones:

- Utilizar nombres de directorios en minúsculas.
- Utilizar `snake_case` para archivos y módulos de Python.
- Evitar directorios con múltiples responsabilidades.
- Mantener la documentación separada del código fuente.
- No almacenar archivos temporales dentro del repositorio.
- Los modelos entrenados deberán almacenarse únicamente en los directorios definidos para dicho propósito.

---

# 9. Buenas Prácticas

Durante el desarrollo deberán seguirse las siguientes recomendaciones:

- Mantener una estructura simple y fácil de comprender.
- Evitar dependencias innecesarias entre módulos.
- Reutilizar componentes antes de crear nuevos.
- Mantener la coherencia con la arquitectura definida en el SDS.
- Eliminar código obsoleto o no utilizado.
- Mantener sincronizada la documentación con la evolución del proyecto.

---

# 10. Referencias

Este documento complementa la documentación oficial del proyecto.

Para mayor información consultar:

- Software Design Specification (SDS)
- Architecture Decision Records (ADR)
- System Architecture
- Engineering Standards
- Technical Roadmap
