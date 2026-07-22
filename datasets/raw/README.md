# Raw Dataset

## Descripción

Esta carpeta contiene los **datasets originales** utilizados por el componente de Ciencia de Datos.

Los archivos almacenados aquí representan la fuente de información inicial y **no deben ser modificados manualmente** durante el proceso de preprocesamiento.

Todos los procesos de limpieza, transformación y validación generan nuevos archivos en las carpetas correspondientes (`processed/`, `reports/`, etc.), preservando siempre los datos originales.

---

## Contenido esperado

Ejemplo de estructura:

```text
raw/
├── master_dataset_v1.csv
├── README.md
```

> El nombre del dataset puede variar según la versión del proyecto. El archivo utilizado por el pipeline deberá coincidir con la ruta definida en la configuración del componente.

---

## Formato esperado

El dataset debe estar en formato **CSV UTF-8** y contener, como mínimo, las columnas definidas en el modelo de datos del proyecto.

Ejemplo:

| Campo | Descripción |
|--------|-------------|
| document_id | Identificador único del documento |
| title | Título del documento |
| description | Descripción breve |
| content | Contenido completo |
| category | Categoría principal |
| subcategory | Subcategoría |
| programming_language | Lenguaje relacionado |
| framework | Framework asociado |
| technology | Tecnología principal |
| difficulty | Nivel de dificultad |
| author_name | Autor |
| author_role | Rol del autor |
| department | Área responsable |

---

## Reglas

- No modificar manualmente los registros.
- No eliminar columnas definidas en el esquema del proyecto.
- Mantener codificación UTF-8.
- Conservar el archivo original como fuente de referencia.
- Los archivos generados por los procesos de validación o limpieza no deben almacenarse en esta carpeta.

---

## Responsable

Equipo de Ciencia de Datos

Proyecto **AyniKortex – Organización Inteligente del Conocimiento Técnico**