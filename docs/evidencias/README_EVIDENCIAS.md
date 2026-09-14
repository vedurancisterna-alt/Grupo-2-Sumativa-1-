# Evidencias de ejecución y trazabilidad

## Sumativa 1 – Programación para la Ciencia de Datos

Este directorio contiene las evidencias asociadas a la ejecución reproducible de los notebooks F1 y F2, la preparación y validación del conjunto de datos, las visualizaciones generadas y el control de versiones del proyecto.

El proyecto utiliza como fuente los datos públicos de **Generación Real del Coordinador Eléctrico Nacional (CEN)** para el período comprendido entre enero y agosto de 2026.

El alcance analítico considera las centrales:

- TER CMPC LAJA
- TER CMPC PACIFICO
- TER CMPC SANTA FE

La fuente original contiene **359.891 registros y 33 variables**. Luego de seleccionar el alcance y transformar las mediciones horarias desde formato ancho a formato largo, el conjunto de datos procesado contiene **17.496 observaciones y 13 variables**.

---

## 01_F1_ejecucion_completa.png

**Propósito:** evidenciar la correcta ejecución de las validaciones iniciales desarrolladas en `F1/F1_definicion.ipynb`.

La captura muestra la ejecución satisfactoria de las validaciones mediante instrucciones `assert`, verificando que:

- la fuente contiene al menos 2.000 registros;
- la fuente contiene al menos 12 variables;
- el subconjunto seleccionado contiene 729 registros originales;
- el alcance considera exactamente tres centrales.

La salida obtenida registra:

- Registros fuente: 359.891
- Variables fuente: 33
- Registros del alcance: 729
- Centrales del alcance: 3

La ausencia de errores durante la ejecución permite comprobar que las condiciones iniciales definidas para el proyecto se cumplen.

---

## 02_F2_validacion_final.png

**Propósito:** evidenciar la preparación, transformación y validación final del conjunto de datos analítico desarrollado en `F2/F2_preparacion_datos.ipynb`.

F2 transforma la estructura original de la fuente, que presenta 24 columnas horarias (`Hora 1` a `Hora 24`), a un formato largo con una única unidad de observación:

> Una observación representa la generación eléctrica registrada para una central durante una hora determinada, expresada en MWh.

El dataset procesado contiene:

- 17.496 observaciones;
- 13 variables;
- tres centrales;
- período enero–agosto de 2026.

Las validaciones implementadas comprueban, entre otros aspectos, la estructura esperada, identificadores únicos, ausencia de duplicados, control de valores faltantes y ausencia de valores negativos de generación.

Los valores iguales a **0 MWh se conservan como observaciones válidas reportadas por la fuente**, sin atribuir automáticamente una causa operacional.

---

## 03_F2_visualizaciones.png

**Propósito:** evidenciar la aplicación de herramientas de análisis y visualización sobre el conjunto de datos preparado.

El notebook F2 incorpora visualizaciones orientadas a explorar el comportamiento de la generación eléctrica de las centrales seleccionadas, incluyendo análisis temporal, comportamiento horario y presencia de registros con generación igual a 0 MWh.

Estas visualizaciones permiten complementar las validaciones numéricas y facilitan la identificación de patrones en los datos procesados.

---

## 04_git_historial_commits.png

**Propósito:** evidenciar la trazabilidad y el uso de control de versiones mediante Git y GitHub.

La captura del historial permite observar:

- desarrollo mediante commits;
- utilización de ramas;
- integración de trabajo colaborativo;
- Pull Requests;
- evolución de F1 y F2;
- migración desde el conjunto de datos utilizado inicialmente hacia la fuente pública del CEN;
- retiro de datasets privados del versionamiento;
- actualización de la documentación del proyecto.

El historial se conserva como evidencia de la evolución del proyecto y de las decisiones implementadas durante su desarrollo.

---

## 05_estructura_repositorio.png

**Propósito:** evidenciar la organización técnica del proyecto.

La estructura separa los principales componentes del trabajo:

- `F1/`: definición y configuración inicial del proyecto.
- `F2/`: preparación, transformación, exploración y validación de datos.
- `data/processed/`: dataset analítico generado por F2.
- `data/raw/`: archivos fuente disponibles localmente y excluidos del versionamiento.
- `docs/evidencias/`: evidencias de ejecución y trazabilidad.
- `src/`: directorio destinado a código reutilizable del proyecto.
- `.gitignore`: reglas de exclusión de archivos que no deben versionarse.
- `README.md`: documentación general del proyecto.
- `requirements.txt`: dependencias necesarias para reproducir el entorno.

Los datos `raw` se mantienen localmente para permitir la ejecución de los notebooks, pero se encuentran excluidos del control de versiones mediante `.gitignore`.

---

## Reproducibilidad y trazabilidad

En este proyecto se distinguen ambos conceptos:

**Reproducibilidad:** capacidad de volver a ejecutar el flujo utilizando el mismo código, dependencias y fuente de datos para obtener resultados consistentes.

**Trazabilidad:** capacidad de reconstruir la evolución del proyecto mediante commits, ramas, Pull Requests, documentación y evidencias de las decisiones adoptadas.

Las evidencias contenidas en este directorio complementan los notebooks, el README principal y el historial del repositorio.
