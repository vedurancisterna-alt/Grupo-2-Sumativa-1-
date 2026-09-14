# Proyecto de Ciencia de Datos – Sumativa 1

## Análisis reproducible de generación eléctrica horaria en centrales CMPC a partir de datos públicos del CEN

Este repositorio corresponde al desarrollo de la **Sumativa 1** del curso **Programación para la Ciencia de Datos**, asociada a las Fases 1 y 2 del proyecto transversal.

El proyecto utiliza datos públicos de **Generación Real** publicados por el **Coordinador Eléctrico Nacional (CEN)** y se concentra en tres centrales asociadas en la fuente a **BIOENERGÍAS FORESTALES SPA**:

- `TER CMPC LAJA`
- `TER CMPC PACIFICO`
- `TER CMPC SANTA FE`

El período de estudio comprende desde el **1 de enero hasta el 31 de agosto de 2026**.

El trabajo desarrollado en esta etapa incluye la definición de la problemática, configuración del entorno reproducible, carga de datos, exploración, transformación, validación, visualización y generación de un dataset procesado apto para las fases posteriores del proyecto.

---

## Problemática

La fuente pública del CEN presenta la información de Generación Real en formato ancho: cada registro corresponde a una combinación central–fecha y contiene 24 columnas horarias (`Hora 1` a `Hora 24`).

Para desarrollar un análisis horario consistente es necesario establecer una única granularidad de trabajo y evitar mezclar observaciones diarias y horarias dentro de una misma tabla.

Por ello, el proyecto implementa un flujo reproducible que carga el archivo público del CEN, verifica su estructura, selecciona las tres centrales definidas en el alcance, transforma las 24 columnas horarias a formato largo, valida calidad e integridad, genera visualizaciones y exporta un dataset procesado reproducible.

La **unidad de observación final** es una central en una fecha y una hora determinada, con su generación eléctrica reportada en MWh.

---

## Fuente de datos

La fuente utilizada corresponde a la publicación pública **Generación Real** del Coordinador Eléctrico Nacional.

**Fuente oficial:**  
https://www.coordinador.cl/operacion/graficos/operacion-real/generacion-real-/

**Diccionario de datos CEN:**  
https://www.coordinador.cl/wp-content/uploads/2022/11/B43-DIN-04-Diccionario-de-Datos-Web-SIP.pdf

El archivo original utilizado por el proyecto se conserva localmente como:

```text
data/raw/generacion_real_cen_ene_ago_2026.csv
```

Este archivo no se versiona en Git debido a su tamaño y porque puede obtenerse nuevamente desde la fuente pública.

> El proyecto declara la fuente como de acceso público. No se atribuye una licencia abierta específica mientras esta no haya sido verificada expresamente en los términos de publicación.

---

## Características del dataset

### Dataset original

- **359.891 registros**
- **33 columnas**
- período **01-01-2026 a 31-08-2026**
- 24 columnas horarias: `Hora 1` a `Hora 24`
- variables descriptivas como año, mes, central, coordinado, tipo y subtipo

Para las tres centrales seleccionadas se obtienen **729 registros originales**, equivalentes a 243 fechas por central.

### Dataset procesado

La transformación ancho → largo genera:

- **17.496 observaciones**
- **13 variables**
- **3 centrales**
- granularidad horaria
- sin duplicados de la clave analítica
- sin valores negativos de generación
- sin valores faltantes en el dataset procesado validado

Archivo:

```text
data/processed/dataset_cen_centrales_cmpc_ene_ago_2026.csv
```

---

## Variables del dataset procesado

1. `ID_Observacion`
2. `Año`
3. `Mes`
4. `Llave`
5. `Central`
6. `Coordinado`
7. `Grupo_Reporte`
8. `Tipo`
9. `Subtipo`
10. `Fecha`
11. `Dia_Semana`
12. `Hora`
13. `Generacion_MWh`

---

## Tratamiento de los valores 0 MWh

Los registros con generación igual a `0 MWh` se conservan como observaciones válidas.

El proyecto **no interpreta automáticamente estos valores como detenciones, fallas o mantenciones**, ya que la fuente seleccionada no entrega por sí sola evidencia suficiente para atribuirles una causa operacional específica.

---

## Objetivo general

Analizar de manera reproducible el comportamiento de la generación eléctrica horaria de las centrales **TER CMPC Laja, TER CMPC Pacífico y TER CMPC Santa Fe**, utilizando datos públicos de Generación Real del Coordinador Eléctrico Nacional correspondientes al período enero–agosto de 2026, con el propósito de caracterizar sus patrones temporales, comparar su comportamiento y documentar las decisiones de preparación, validación y análisis de los datos.

---

## Objetivos específicos

1. Verificar la procedencia, estructura y calidad inicial de los datos públicos utilizados.
2. Seleccionar reproduciblemente los registros correspondientes a las tres centrales del alcance.
3. Transformar la estructura original de 24 columnas horarias a formato largo.
4. Validar duplicados, integridad temporal, tipos de datos, valores faltantes y valores negativos.
5. Caracterizar estadísticamente la generación horaria de cada central.
6. Analizar los registros con generación igual a `0 MWh` sin atribuir automáticamente una causa operacional.
7. Comparar el comportamiento temporal de las centrales mediante indicadores y visualizaciones.
8. Mantener reproducibilidad técnica y trazabilidad mediante Jupyter Notebook, Git, GitHub y dependencias documentadas.

---

## Estructura del proyecto

```text
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
│   │   └── generacion_real_cen_ene_ago_2026.csv
│   └── processed/
│       └── dataset_cen_centrales_cmpc_ene_ago_2026.csv
│
├── docs/
│   └── evidencias/
│
├── src/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Fase 1 – Definición del proyecto

`F1/F1_definicion.ipynb` contiene:

- problemática;
- fuente pública;
- caracterización inicial;
- unidad de observación;
- preguntas centrales;
- objetivos;
- alcance y exclusiones;
- supuestos;
- reproducibilidad y trazabilidad diferenciadas;
- registro de decisiones;
- configuración del entorno;
- localización reproducible del proyecto;
- carga inicial;
- validaciones de estructura y alcance.

---

## Fase 2 – Preparación, transformación y validación

`F2/F2_preparacion_datos.ipynb` implementa:

1. carga del archivo público del CEN;
2. validación del esquema;
3. exploración inicial;
4. conversión y validación de fecha;
5. selección de centrales;
6. transformación ancho → largo;
7. creación de `Hora`, `Dia_Semana` e `ID_Observacion`;
8. validaciones de calidad;
9. análisis descriptivo y de registros `0 MWh`;
10. validación temporal;
11. visualizaciones exploratorias;
12. función reutilizable de validación;
13. pruebas de casos normales, límite y excepción;
14. exportación y relectura del dataset procesado.

---

## Reproducibilidad

La **reproducibilidad** es la capacidad de volver a ejecutar el proceso desde la fuente pública utilizando el código y el entorno documentado.

El proyecto utiliza:

- Jupyter Notebook;
- rutas relativas;
- entorno virtual de Python;
- `requirements.txt`;
- validaciones automáticas;
- fuente pública identificada;
- transformación codificada de inicio a fin.

### Instalación de dependencias

Desde la raíz del proyecto:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## Instrucciones de ejecución

### 1. Preparar el archivo fuente

Descargar desde el CEN la información de Generación Real correspondiente a enero–agosto de 2026 y guardarla como:

```text
data/raw/generacion_real_cen_ene_ago_2026.csv
```

### 2. Ejecutar F1

Abrir:

```text
F1/F1_definicion.ipynb
```

Seleccionar el kernel del entorno virtual, ejecutar **Restart Kernel** y luego **Run All**.

### 3. Ejecutar F2

Abrir:

```text
F2/F2_preparacion_datos.ipynb
```

Reiniciar el kernel, ejecutar todas las celdas y comprobar la creación de:

```text
data/processed/dataset_cen_centrales_cmpc_ene_ago_2026.csv
```

---

## Trazabilidad y control de versiones

La **trazabilidad** es la capacidad de reconstruir la evolución del proyecto, sus modificaciones y decisiones.

Se utiliza:

- Git;
- GitHub;
- ramas de trabajo;
- commits descriptivos;
- historial de cambios;
- documentación integrada en notebooks;
- README actualizado.

Los archivos de `data/raw` no se versionan. El dataset procesado sí se incluye para permitir verificar el resultado del procesamiento.

---

## Validaciones técnicas

Entre las principales verificaciones implementadas se encuentran:

- existencia del archivo fuente;
- esquema y columnas esperadas;
- centrales del alcance presentes;
- número esperado de registros;
- número esperado de observaciones finales;
- unicidad de `ID_Observacion`;
- ausencia de duplicados central–fecha–hora;
- ausencia de valores faltantes;
- ausencia de generación negativa;
- cobertura temporal;
- 24 observaciones horarias por central y fecha;
- exportación y relectura;
- prueba con duplicado artificial;
- manejo controlado de archivo inexistente.

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

## Estado actual del proyecto

- Fase 1 actualizada y ejecutada sin errores.
- Fase 2 actualizada, validada y ejecutada.
- Dataset procesado generado.
- Fuente pública CEN incorporada.
- Ejecución reproducible verificada mediante `Restart Kernel + Run All`.
- Pendiente: actualización de evidencias, mapa conceptual e informe técnico integrado.

---

## Integrantes

- Verónica Durán Cisterna
- Raúl Moya Arriagada
- Daniela Rojas Vilches
- Manuel Sánchez Cárcamo

---

## Referencias principales

- Coordinador Eléctrico Nacional. *Generación Real*.  
  https://www.coordinador.cl/operacion/graficos/operacion-real/generacion-real-/
- Coordinador Eléctrico Nacional. *Diccionario de Datos Web SIP*.  
  https://www.coordinador.cl/wp-content/uploads/2022/11/B43-DIN-04-Diccionario-de-Datos-Web-SIP.pdf
- Python Software Foundation. *Python Documentation*.  
  https://docs.python.org/
- Pandas Development Team. *Pandas Documentation*.  
  https://pandas.pydata.org/docs/
- NumPy Developers. *NumPy Documentation*.  
  https://numpy.org/doc/
- Matplotlib Development Team. *Matplotlib Documentation*.  
  https://matplotlib.org/stable/

  
