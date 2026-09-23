# Proyecto de Ciencia de Datos – Sumativa 1

## Análisis reproducible de generación eléctrica horaria en centrales CMPC a partir de datos públicos del CEN

Este repositorio corresponde al desarrollo de la **Sumativa 1** del curso **Programación para la Ciencia de Datos**, asociada a las Fases 1 y 2 del proyecto transversal.

El proyecto utiliza datos públicos de **Generación Real** publicados por el **Coordinador Eléctrico Nacional (CEN)** y se concentra en tres centrales asociadas en la fuente a **BIOENERGÍAS FORESTALES SPA**:

- `TER CMPC LAJA`
- `TER CMPC PACIFICO`
- `TER CMPC SANTA FE`

El período de estudio comprende desde el **1 de enero hasta el 31 de agosto de 2026**.

En esta etapa se desarrollan la definición del problema de investigación, configuración del entorno reproducible, obtención y carga de datos, exploración, preparación, transformación, validación técnica y generación del dataset procesado que servirá de base para las fases posteriores.

---

## Pregunta de investigación

**¿Qué patrones temporales de generación eléctrica caracterizan a las centrales TER CMPC Laja, TER CMPC Pacífico y TER CMPC Santa Fe durante el período enero–agosto de 2026?**

Esta pregunta orienta el proyecto desde una perspectiva analítica y permite articular las etapas de preparación desarrolladas en F1 y F2 con los análisis que se profundizarán posteriormente.

---

## Problemática

La fuente pública del CEN presenta la información de Generación Real en formato ancho: cada registro corresponde a una combinación central–fecha y contiene 24 columnas horarias (`Hora 1` a `Hora 24`).

Esta estructura es adecuada para la publicación de los datos, pero requiere ser transformada para desarrollar análisis temporales a nivel horario mediante herramientas de ciencia de datos.

Por ello, el proyecto implementa un flujo reproducible que permite cargar la fuente, verificar su estructura, delimitar el alcance a las tres centrales seleccionadas, transformar las 24 columnas horarias a formato largo, construir variables analíticas y validar la integridad del resultado.

La **unidad de observación final** corresponde a una central en una fecha y hora determinada, con su generación eléctrica reportada en MWh.

---

## Objetivo general

Caracterizar los patrones temporales de generación eléctrica de las centrales **TER CMPC Laja, TER CMPC Pacífico y TER CMPC Santa Fe** durante el período enero–agosto de 2026, utilizando datos públicos de Generación Real del Coordinador Eléctrico Nacional y un proceso reproducible de preparación y validación de datos.

---

## Objetivos específicos

1. Caracterizar la distribución horaria, diaria y mensual de la generación eléctrica de las tres centrales seleccionadas.
2. Comparar los patrones temporales de generación entre TER CMPC Laja, TER CMPC Pacífico y TER CMPC Santa Fe.
3. Caracterizar la frecuencia y distribución temporal de los registros con generación igual a `0 MWh`, sin atribuir una causa operacional no respaldada por la fuente.
4. Identificar regularidades y diferencias en el comportamiento temporal de las centrales que sirvan de base para las fases posteriores del proyecto.

---

## Fuente de datos

La fuente utilizada corresponde a la publicación pública **Generación Real** del Coordinador Eléctrico Nacional:

**Fuente oficial:**  
https://www.coordinador.cl/operacion/graficos/operacion-real/generacion-real-/

**Diccionario de Datos Web SIP:**  
https://www.coordinador.cl/wp-content/uploads/2022/11/B43-DIN-04-Diccionario-de-Datos-Web-SIP.pdf

El diccionario utilizado como respaldo documental también se encuentra incorporado en:

```text
docs/B43-DIN-04-Diccionario-de-Datos-Web-SIP.pdf
```

El archivo original utilizado para el procesamiento se conserva localmente como:

```text
data/raw/generacion_real_cen_ene_ago_2026.csv
```

El archivo fuente no se versiona en Git debido a su tamaño y porque puede obtenerse nuevamente desde la fuente pública.

> El proyecto identifica la información como una fuente de acceso público. No se atribuye una licencia abierta específica mientras esta no haya sido verificada expresamente en los términos de publicación del CEN.

---

## Características del dataset

### Dataset original

La descarga correspondiente al período analizado contiene:

- **359.891 registros**
- **33 columnas**
- período **01-01-2026 a 31-08-2026**
- 24 columnas horarias: `Hora 1` a `Hora 24`
- variables descriptivas de la fuente como año, mes, central, coordinado, tipo y subtipo

Al delimitar el alcance a las tres centrales seleccionadas se obtienen **729 registros en formato ancho**, equivalentes a **243 fechas por central**.

### Dataset procesado

La transformación ancho → largo genera:

- **17.496 observaciones**
- **13 variables**
- **3 centrales**
- **243 fechas por central**
- **24 observaciones por central y fecha**
- granularidad horaria
- sin valores faltantes
- sin duplicados de la clave analítica
- sin identificadores duplicados
- sin valores negativos de generación

Archivo procesado:

```text
data/processed/dataset_cen_centrales_cmpc_ene_ago_2026.csv
```

El dataset procesado anterior utilizado durante etapas preliminares del proyecto fue retirado para evitar inconsistencias entre fuentes y versiones.

---

## Variables del dataset procesado

| Variable | Rol analítico |
|---|---|
| `ID_Observacion` | Identificador único |
| `Año` | Variable temporal |
| `Mes` | Variable temporal discreta |
| `Llave` | Identificador proveniente de la fuente |
| `Central` | Variable categórica nominal |
| `Coordinado` | Variable categórica |
| `Grupo_Reporte` | Variable categórica |
| `Tipo` | Variable categórica |
| `Subtipo` | Variable categórica |
| `Fecha` | Variable temporal |
| `Dia_Semana` | Variable temporal derivada |
| `Hora` | Variable temporal discreta |
| `Generacion_MWh` | Variable cuantitativa continua de interés |

Dentro del alcance correspondiente exclusivamente a las tres centrales seleccionadas, las variables `Coordinado`, `Tipo` y `Subtipo` presentan un único valor observado. Por lo tanto, no aportan variabilidad para comparar las centrales dentro de este subconjunto, aunque se conservan para mantener contexto y trazabilidad respecto de la fuente.

---

## Tratamiento de los registros con 0 MWh

Los registros con generación igual a `0 MWh` se conservan como observaciones válidas.

En el dataset procesado se identificaron **4.438 registros con generación igual a 0 MWh**, equivalentes aproximadamente al **25,37 %** de las observaciones.

Su distribución no es homogénea entre las tres centrales, por lo que estos registros constituyen un elemento relevante para la caracterización temporal posterior.

El proyecto **no interpreta automáticamente estos valores como detenciones, fallas o mantenciones**, ya que la fuente seleccionada no proporciona por sí sola evidencia suficiente para atribuirles una causa operacional específica.

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
|
├── F3/
│   └── F3_nucleo_algoritmico.ipynb
│
├── data/
│   ├── raw/
│   │   └── generacion_real_cen_ene_ago_2026.csv
│   └── processed/
│       └── dataset_cen_centrales_cmpc_ene_ago_2026.csv
│
├── docs/
│   ├── B43-DIN-04-Diccionario-de-Datos-Web-SIP.pdf
│   └── evidencias/
│
├── src/
│   ├── __init__.py
│   ├── carga.py
│   ├── transformacion.py
│   └── validacion.py
│   ├── nucleo_poo.py
│   └── agregacion_temporal.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Modularización del código

Parte de la lógica reutilizable del pipeline fue separada del notebook y organizada en módulos Python dentro de `src/`.

### `src/carga.py`

Contiene la función responsable de comprobar la existencia y cargar el archivo de Generación Real del CEN.

### `src/transformacion.py`

Contiene la transformación desde el formato ancho original, con 24 columnas horarias, al formato largo utilizado para el análisis.

### `src/validacion.py`

Contiene las reglas de validación del dataset procesado, descompuestas en funciones atómicas e independientes (`validar_sin_nulos`, `validar_sin_duplicados`, `validar_sin_duplicados_exactos`, `validar_no_negativos`, `validar_granularidad`, `validar_categorias_esperadas`), cada una probable por separado. `validar_dataset_procesado()` compone estas reglas para mantener compatibilidad con F2, recibiendo los valores esperados (centrales, filas, columnas) como parámetros con valor por defecto en vez de escritos dentro de la lógica — permitiendo ampliar el período o el alcance del proyecto sin modificar el código.

### `src/nucleo_poo.py`

Contiene la clase base `Transformador`, sus tres clases derivadas y la clase `Pipeline` que las compone. Reutiliza `carga.py`, `transformacion.py` y `validacion.py` sin reimplementar su lógica.

### `src/agregacion_temporal.py`

Contiene las clases del patrón Strategy para agregación temporal (`AgregacionHoraria`, `AgregacionDiaria`, `AgregacionMensual`, `AgregacionPorDiaSemana`) y `CaracterizadorTemporal`, que las aplica de forma intercambiable.

---

## Fase 1 – Definición del proyecto

`F1/F1_definicion.ipynb` contiene:

- pregunta de investigación;
- problemática;
- objetivo general y objetivos específicos;
- fuente pública y diccionario de datos;
- alcance temporal y analítico;
- unidad de observación;
- variables y roles;
- supuestos y exclusiones;
- reproducibilidad y trazabilidad como conceptos diferenciados;
- registro de decisiones;
- configuración del entorno;
- localización reproducible de la raíz del proyecto;
- carga inicial y validación de estructura.

---

## Fase 2 – Preparación, transformación y validación

`F2/F2_preparacion_datos.ipynb` implementa:

1. carga reproducible mediante `src/carga.py`;
2. validación del esquema de la fuente;
3. exploración inicial;
4. conversión y validación de fechas;
5. selección reproducible de las tres centrales;
6. transformación ancho → largo mediante `src/transformacion.py`;
7. construcción de variables derivadas;
8. validaciones de calidad e integridad;
9. comprobación de variables con varianza cero;
10. caracterización descriptiva de registros `0 MWh`;
11. validación de 24 observaciones por central y fecha;
12. visualizaciones exploratorias;
13. validación integral mediante `src/validacion.py`;
14. pruebas de caso normal, límite y excepción;
15. exportación y relectura del dataset procesado.

---

## Fase 3 – Núcleo algorítmico, eficiencia y programación orientada a objetos

`F3/F3_nucleo_algoritmico.ipynb` reorganiza el pipeline de F2 bajo un diseño orientado a objetos, sin modificar su lógica ni sus resultados. Implementa:

1. una clase base `Transformador` (método plantilla) que define el contrato `ajustar()` / `transformar()`, con control de estado y copia defensiva del DataFrame;
2. tres clases derivadas —`FiltradorCentrales`, `TransformadorAnchoLargo`, `ConstructorVariablesDerivadas`— que heredan de `Transformador` y encapsulan, respectivamente, el filtro de centrales, la transformación ancho→largo y la construcción de variables derivadas (`Dia_Semana`, `ID_Observacion`);
3. una clase `Pipeline` que compone y ejecuta las tres anteriores de forma polimórfica, sin consultar en ningún punto el tipo concreto de cada paso;
4. verificación de equivalencia funcional: el resultado de `Pipeline(...).ejecutar()` se contrasta con `pd.testing.assert_frame_equal` contra el dataset procesado oficial de F2, confirmando que la reorganización en clases preserva exactamente la semántica del pipeline original;
5. comparación de eficiencia entre dos implementaciones de la transformación ancho→largo (vectorizada con `pandas.melt`, usada en producción, e iterativa con `iterrows`, solo para contraste), midiendo tiempo con `timeit` y memoria con `tracemalloc` sobre las 729 filas reales del proyecto, con verificación previa de equivalencia entre ambas;
6. patrón de diseño **Strategy** para la agregación temporal: cuatro clases intercambiables (`AgregacionHoraria`, `AgregacionDiaria`, `AgregacionMensual`, `AgregacionPorDiaSemana`) que implementan un contrato común, aplicadas mediante `CaracterizadorTemporal` sin que este conozca cuál estrategia recibe — lo que responde directamente a los Objetivos específicos 1 y 2 del proyecto (caracterizar y comparar los patrones temporales entre las tres centrales).

Sobre recursividad: el pipeline tiene tres pasos fijos y conocidos, no un problema de profundidad variable, por lo que se optó por división funcional en clases en lugar de recursividad.

---

## Decisiones de preprocesamiento

La inspección de la fuente no identificó valores nulos ni registros duplicados exactos dentro del dataset utilizado, por lo que no fue necesario aplicar procedimientos de imputación.

Tampoco se aplicó normalización o escalamiento a `Generacion_MWh`, debido a que en esta fase se busca preservar la magnitud original reportada en MWh para su posterior caracterización descriptiva.

Las principales operaciones de preparación corresponden al casting de tipos, delimitación del alcance, transformación estructural ancho–largo, construcción de variables derivadas y validación de integridad.

---

## Reproducibilidad

La **reproducibilidad** corresponde a la capacidad de volver a ejecutar el procesamiento desde la fuente utilizando el código, estructura y entorno documentados.

El proyecto utiliza:

- Python;
- Jupyter Notebook;
- entorno virtual `.venv`;
- `requirements.txt`;
- rutas relativas;
- módulos reutilizables en `src/`;
- validaciones automáticas;
- fuente pública identificada;
- transformación codificada de inicio a fin.

### Instalación de dependencias

Desde la raíz del proyecto:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Este comando utiliza el intérprete Python del entorno virtual del proyecto e instala las dependencias registradas en `requirements.txt`.

---

## Instrucciones de ejecución

### 1. Preparar la fuente

Descargar desde el CEN la información de Generación Real correspondiente a enero–agosto de 2026 y guardarla como:

```text
data/raw/generacion_real_cen_ene_ago_2026.csv
```

### 2. Instalar las dependencias

Desde la raíz del repositorio ejecutar:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Ejecutar F1

Abrir:

```text
F1/F1_definicion.ipynb
```

Seleccionar el kernel correspondiente al entorno virtual del proyecto, ejecutar **Restart Kernel** y posteriormente **Run All**.

### 4. Ejecutar F2

Abrir:

```text
F2/F2_preparacion_datos.ipynb
```

Seleccionar el mismo kernel, ejecutar **Restart Kernel** y posteriormente **Run All**.

Al finalizar debe generarse:

```text
data/processed/dataset_cen_centrales_cmpc_ene_ago_2026.csv
```

La ejecución completa debe finalizar sin errores y superar las validaciones técnicas incorporadas en el notebook y en `src/validacion.py`.

### 5. Ejecutar F3

Abrir:

```text
F3/F3_nucleo_algoritmico.ipynb
```

Seleccionar el mismo kernel del entorno virtual, ejecutar **Restart Kernel** y posteriormente **Run All**. El notebook depende del dataset procesado de F2 (`data/processed/dataset_cen_centrales_cmpc_ene_ago_2026.csv`) para la verificación de equivalencia, por lo que F2 debe ejecutarse primero.

---

## Trazabilidad y control de versiones

La **trazabilidad** corresponde a la capacidad de reconstruir la evolución del proyecto, sus modificaciones, decisiones y contribuciones.

Para ello se utilizan:

- Git para el control de versiones local;
- GitHub como repositorio remoto y plataforma de colaboración;
- ramas de trabajo;
- commits descriptivos;
- merges que preservan el trabajo colaborativo;
- historial de cambios;
- notebooks documentados;
- README;
- evidencias de ejecución.

Los archivos de `data/raw/` no se versionan. El dataset procesado sí se incorpora al repositorio para permitir verificar el resultado final del pipeline.

---

## Validaciones técnicas

Las principales verificaciones implementadas incluyen:

- existencia del archivo fuente;
- esquema y columnas esperadas;
- presencia de las centrales definidas;
- dimensiones esperadas;
- unicidad de `ID_Observacion`;
- ausencia de duplicados central–fecha–hora;
- ausencia de valores faltantes;
- ausencia de generación negativa;
- cobertura temporal;
- exactamente 24 observaciones por central y fecha;
- variables categóricas sin variación dentro del alcance;
- exportación y relectura del resultado;
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

## Vinculación con las fases del proyecto

### Materializado en F1, F2 y F3

En la Sumativa 2 se encuentran implementados y verificables:

- definición del problema y pregunta de investigación;
- objetivos;
- fuente y alcance;
- entorno reproducible;
- carga y exploración;
- transformación;
- validación;
- modularización;
- dataset procesado;
- control de versiones y trazabilidad;
- jerarquía de clases orientada a objetos (Transformador/Pipeline);
- comparación de eficiencia entre implementaciones;
- patrón de diseño Strategy.

### Proyectado para F4

Las fases posteriores profundizarán la caracterización de los patrones temporales identificados, las comparaciones entre centrales y los análisis necesarios para responder integralmente la pregunta de investigación.

Esta separación permite distinguir entre los componentes actualmente implementados y aquellos que forman parte de la continuidad del proyecto.

---

## Estado actual

- F1 actualizado y ejecutado mediante `Restart Kernel + Run All`.
- F2 actualizado y ejecutado mediante `Restart Kernel + Run All`.
- F3 implementado: jerarquía Transformador/Pipeline (POO), patrón Strategy para agregación temporal, comparación de eficiencia melt vs. iterrows, equivalencia funcional verificada contra F2.
- Pipeline modularizado en `src/`.
- Dataset procesado CEN validado.
- Dataset procesado obsoleto retirado.
- Diccionario de datos CEN incorporado en `docs/`.
- Fuente pública documentada.
- Git y GitHub sincronizados.
- Pendiente de actualización final: evidencias, mapa conceptual e informe técnico integrado.

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
  