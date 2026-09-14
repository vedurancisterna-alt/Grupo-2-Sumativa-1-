# Proyecto de Ciencia de Datos – Sumativa 1

## Análisis de generación y excedentes energéticos en plantas de celulosa CMPC

Este repositorio corresponde al desarrollo de la *Sumativa 1* del curso Programación para la Ciencia de Datos, asociada a las Fases 1 y 2 del proyecto transversal.

El proyecto analiza un conjunto de datos con registros horarios de variables energéticas correspondientes a plantas de celulosa de CMPC durante el año 2026.

El trabajo desarrollado en esta etapa se concentra en la definición del problema, configuración de un entorno reproducible, exploración inicial, preparación, transformación y validación de los datos.

---

## Problemática

Las plantas de celulosa consideradas en el proyecto cuentan con sistemas de generación eléctrica asociados a sus procesos productivos.

El dataset disponible contiene registros horarios de variables relacionadas con turbogeneradores (TG), autoproducción o excedentes (AP) y otras mediciones energéticas correspondientes principalmente a las plantas Santa Fe, Pacífico y Laja, además de variables asociadas a Santa Fe Energía y Bucalemu.

Para realizar análisis posteriores es necesario disponer de información correctamente estructurada y validada. La exploración inicial permitió identificar, entre otros aspectos:

- variables de medición originalmente interpretadas como texto debido al uso de coma decimal;
- una marca temporal repetida;
- períodos consecutivos con mediciones iguales a cero;
- necesidad de validar la consistencia de la variable de fecha y día de la semana;
- necesidad de conservar la trazabilidad entre los datos originales y los datos procesados.

Por esta razón, se implementa un flujo reproducible de preparación y validación mediante Python, Pandas y Jupyter Notebook.

---

## Objetivo general

Analizar el comportamiento energético de las plantas consideradas en el dataset a partir de registros horarios de generación y autoproducción/excedentes durante 2026, con el propósito de caracterizar su comportamiento temporal, preparar información confiable para el análisis y generar indicadores que permitan identificar patrones y variaciones relevantes.

---

## Objetivos específicos

1. Evaluar la estructura y calidad inicial del conjunto de datos.
2. Transformar las variables energéticas a formatos adecuados para el análisis.
3. Validar la estructura temporal y la consistencia de los registros.
4. Analizar la presencia de valores cero y su comportamiento temporal sin asumir automáticamente que corresponden a errores.
5. Preparar un dataset procesado manteniendo la trazabilidad respecto del archivo original.
6. Implementar funciones y pruebas automáticas que permitan reproducir y validar el procesamiento.
7. Generar una base preparada para las posteriores etapas de análisis y visualización.

---

## Dataset

El archivo utilizado en las Fases 1 y 2 corresponde a:

data/raw/dataset_proyecto_vf.csv

El dataset contiene:

- *5.833 registros*
- *17 variables*
- registros horarios entre enero y septiembre de 2026;
- variables de generación asociadas a turbogeneradores;
- variables de autoproducción/excedentes;
- variables temporales y otras mediciones energéticas.

El archivo original ubicado en data/raw se mantiene sin modificaciones.

Como resultado de la Fase 2 se genera:

data/processed/dataset_proyecto_procesado.csv

Este archivo contiene los datos preparados y validados para las etapas posteriores del proyecto.

---

## Estructura del proyecto

text
Proyecto/
│
├── F1/
│   └── F1_definicion.ipynb
│
├── F2/
│   └── F2_preparacion_datos.ipynb
│
├── data/
│   ├── raw/
│   │   └── dataset_proyecto_vf.csv
│   └── processed/
│       └── dataset_proyecto_procesado.csv
│
├── docs/
│   └── evidencias/
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt


---

## Fase 1 – Definición del proyecto

El notebook F1/F1_definicion.ipynb contiene la definición inicial del proyecto y la configuración del entorno reproducible.

En esta fase se desarrollan:

- definición de la problemática;
- preguntas centrales del proyecto;
- objetivo general y objetivos específicos;
- alcance y exclusiones;
- supuestos iniciales;
- articulación entre las fases F1, F2, F3 y F4;
- configuración del entorno Python;
- carga inicial reproducible del dataset;
- validaciones básicas de estructura.

---

## Fase 2 – Preparación y validación de datos

El notebook F2/F2_preparacion_datos.ipynb implementa el flujo reproducible de preparación de datos.

Las principales actividades desarrolladas son:

- carga del dataset original;
- exploración de dimensiones y variables;
- evaluación de valores nulos y registros duplicados;
- conversión de variables con coma decimal a formato numérico;
- transformación y validación de la variable Fecha;
- revisión de marcas temporales duplicadas;
- evaluación de continuidad horaria;
- validación de Dia_Semana;
- análisis descriptivo de las variables energéticas;
- identificación de valores iguales a cero;
- análisis de bloques consecutivos de ceros;
- implementación de funciones reutilizables;
- pruebas automáticas mediante assert;
- exportación y verificación del dataset procesado.

Los registros con valores cero y la marca temporal repetida se conservan cuando no existe evidencia suficiente para clasificarlos automáticamente como errores.

---

## Reproducibilidad

El proyecto utiliza un entorno virtual de Python y registra sus dependencias en:

requirements.txt

Para instalar las dependencias del proyecto desde la terminal:

bash
pip install -r requirements.txt


Los notebooks deben ejecutarse respetando el orden de sus celdas.

Para comprobar la reproducibilidad se recomienda reiniciar el kernel y ejecutar todas las celdas desde el inicio.

El flujo de F2 verifica automáticamente condiciones como:

- conservación de las dimensiones del dataset;
- ausencia de valores nulos generados por las transformaciones;
- correcta conversión de Fecha;
- conversión de las variables de medición a formato numérico;
- correcta exportación y recuperación del dataset procesado.

---

## Tecnologías utilizadas

- Python
- Jupyter Notebook
- Visual Studio Code
- Pandas
- NumPy
- Matplotlib
- Git
- GitHub

---

## Control de versiones

El proyecto utiliza Git y GitHub para mantener trazabilidad sobre los cambios realizados.

Los avances se registran mediante commits descriptivos asociados a las distintas etapas del proyecto. Esto permite identificar modificaciones, correcciones y contribuciones realizadas durante el desarrollo de las Fases 1 y 2.

---

## Estado actual del proyecto

- Fase 1: definición del proyecto y configuración inicial completada.
- Fase 2: preparación, transformación y validación del dataset completada.
- Dataset procesado generado y validado.
- Flujo F2 probado mediante ejecución reproducible desde el inicio.
- Próximas etapas: análisis, visualización e interpretación de resultados correspondientes a las fases posteriores del proyecto.

---

## Integrantes

- Veronica Duran Cisterna
- Raúl Moya
- Daniela Rojas - Manuel Sánchez

---

## Consideraciones

Las interpretaciones operacionales de las variables energéticas deben ser validadas antes de utilizarlas para establecer relaciones causales, económicas o de desempeño operacional.

Los valores negativos, positivos o iguales a cero no son clasificados automáticamente como errores, ya que pueden responder a convenciones de medición o condiciones propias del sistema energético analizado.
