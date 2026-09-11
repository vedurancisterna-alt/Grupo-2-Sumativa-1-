# Proyecto de Ciencia de Datos – Sumativa 1

## Análisis y procesamiento de datos de motores eléctricos para la gestión del mantenimiento industrial

Este repositorio corresponde al desarrollo de la Sumativa 1 del curso, asociada a las Fases 1 y 2 del proyecto transversal.

El objetivo del proyecto es analizar, depurar, estandarizar y validar un conjunto de datos correspondiente a un inventario de motores eléctricos industriales, utilizando herramientas del ecosistema científico de Python.

La finalidad es mejorar la calidad, consistencia y trazabilidad de la información disponible, generando una base de datos procesada que pueda ser utilizada en posteriores etapas de análisis y visualización.

---

## Problemática

La gestión del mantenimiento industrial requiere disponer de información técnica confiable y estructurada sobre los activos.

Los inventarios de equipos pueden contener:

- valores faltantes;
- registros incompletos;
- diferencias de nomenclatura;
- identificadores inconsistentes;
- posibles duplicidades;
- ausencia de estandarización.

Estas condiciones pueden dificultar la trazabilidad de los motores eléctricos y limitar el uso analítico de la información.

Por esta razón, el proyecto implementa un flujo reproducible de procesamiento de datos mediante Python.

---

## Objetivo general

Analizar, depurar y estandarizar el inventario de motores eléctricos de una instalación industrial mediante herramientas de ciencia de datos en Python, con el propósito de evaluar la calidad de la información, mejorar la trazabilidad de los activos y generar una base de datos confiable para apoyar la gestión del mantenimiento.

---

## Objetivos específicos

1. Caracterizar la estructura y contenido del conjunto de datos.
2. Identificar valores faltantes, registros duplicados e inconsistencias.
3. Implementar procedimientos reproducibles de limpieza y transformación.
4. Estandarizar variables e identificadores relevantes.
5. Diseñar indicadores de calidad y completitud de los registros.
6. Validar técnicamente el dataset resultante.
7. Generar una base procesada para posteriores etapas de análisis y visualización.

---

## Estructura del proyecto

```text
Proyecto/
│
├── F1/
│   └── F1_definicion.ipynb
│
├── F2/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── evidencias/
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt