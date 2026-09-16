# Evidencias técnicas – Sumativa 1

Este directorio contiene las evidencias de ejecución, validación, estructura y control de versiones correspondientes a las Fases 1 y 2 del proyecto de Ciencia de Datos.

Las evidencias fueron actualizadas después de incorporar las observaciones realizadas al proyecto y buscan demostrar la reproducibilidad, validación técnica, modularización y trazabilidad del trabajo desarrollado.

---

## 01_F1_pregunta_objetivos.png

**Evidencia:** definición investigativa del proyecto.

Permite verificar la incorporación de la pregunta de investigación:

> ¿Qué patrones temporales de generación eléctrica caracterizan a las centrales TER CMPC Laja, TER CMPC Pacífico y TER CMPC Santa Fe durante el período enero–agosto de 2026?

Además, evidencia el objetivo general y los objetivos específicos que orientan el análisis.

**Criterios asociados:** definición del problema, pregunta de investigación, objetivos y articulación del proyecto.

---

## 02_F1_ejecucion_reproducible.png

**Evidencia:** ejecución técnica de F1.

Permite verificar que `F1/F1_definicion.ipynb` contiene código ejecutado para configurar/localizar el proyecto, acceder a la fuente y efectuar verificaciones iniciales.

El notebook fue comprobado mediante:

`Restart Kernel → Run All`

sin errores de ejecución.

**Criterios asociados:** reproducibilidad, entorno técnico, notebook F1 y documentación integrada.

---

## 03_F2_validacion_final.png

**Evidencia:** validación integral del dataset procesado.

Permite verificar los principales controles realizados sobre el resultado final:

- 17.496 observaciones;
- 13 variables;
- 0 valores nulos;
- 0 duplicados exactos;
- 0 identificadores duplicados;
- 0 valores negativos de generación;
- 3 centrales;
- 24 observaciones por central y fecha.

La validación utiliza la función modularizada disponible en:

`src/validacion.py`

**Criterios asociados:** preprocesamiento, validación técnica, modularización y calidad de datos.

---

## 04_F2_pruebas_tecnicas.png

**Evidencia:** pruebas del pipeline.

Documenta la ejecución de pruebas correspondientes a:

- caso normal;
- caso límite mediante introducción controlada de un duplicado artificial;
- caso de excepción mediante intento controlado de acceso a un archivo inexistente.

Estas pruebas permiten comprobar que el pipeline responde de manera esperada tanto frente a datos válidos como frente a situaciones anómalas.

**Criterios asociados:** pruebas, manejo de excepciones y validación técnica.

---

## 05_F2_analisis_ceros.png

**Evidencia:** caracterización de registros con generación igual a 0 MWh.

El dataset contiene 4.438 observaciones con generación igual a 0 MWh, equivalentes aproximadamente al 25,37 % del total.

La distribución presenta diferencias entre las centrales analizadas.

Estos valores se conservan como observaciones válidas y no se atribuyen automáticamente a fallas, detenciones o mantenciones, debido a que la fuente utilizada no proporciona evidencia suficiente para establecer una causa operacional.

**Criterios asociados:** exploración, análisis descriptivo, decisiones metodológicas y documentación del procesamiento.

---

## 06_git_historial_commits.png

**Evidencia:** historial de control de versiones.

Permite observar commits descriptivos, integración de contribuciones, ramas y merges utilizados durante el desarrollo.

Entre los cambios registrados se encuentran:

- actualización de F1 y F2;
- modularización del pipeline;
- incorporación del diccionario de datos CEN;
- eliminación del dataset procesado obsoleto;
- actualización del README;
- integración de contribuciones realizadas en paralelo.

**Criterios asociados:** Git, GitHub, trazabilidad, trabajo colaborativo y control de versiones.

---

## 07_estructura_repositorio.png

**Evidencia:** organización técnica del repositorio.

Permite verificar la existencia y separación de:

- `F1/`;
- `F2/`;
- `data/raw/`;
- `data/processed/`;
- `docs/`;
- `docs/evidencias/`;
- `src/`;
- `README.md`;
- `requirements.txt`;
- `.gitignore`.

También permite comprobar la modularización implementada mediante:

- `src/carga.py`;
- `src/transformacion.py`;
- `src/validacion.py`.

**Criterios asociados:** estructura del repositorio, organización del código, modularización, reproducibilidad y documentación.

---

## Síntesis de evidencias

Las evidencias permiten relacionar los principales componentes de la Sumativa 1 con su implementación verificable:

| Componente | Evidencia |
|---|---|
| Pregunta de investigación y objetivos | `01_F1_pregunta_objetivos.png` |
| Ejecución reproducible F1 | `02_F1_ejecucion_reproducible.png` |
| Validación final F2 | `03_F2_validacion_final.png` |
| Pruebas normal, límite y excepción | `04_F2_pruebas_tecnicas.png` |
| Caracterización de 0 MWh | `05_F2_analisis_ceros.png` |
| Historial Git/GitHub | `06_git_historial_commits.png` |
| Estructura y modularización | `07_estructura_repositorio.png` |

Estas evidencias complementan los notebooks, el README, el código modularizado y el historial del repositorio, permitiendo verificar la ejecución y evolución del proyecto.
