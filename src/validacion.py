"""
Validación del dataset procesado — refactorizada en reglas atómicas.

Antes, validar_dataset_procesado() concentraba ocho comprobaciones en un
solo bloque, con tres valores (17.496 filas, 13 columnas, 3 centrales)
escritos directamente dentro del código. Eso significa que si el
período de estudio se amplía (por ejemplo, agregando septiembre) o se
incorpora una cuarta central, la función falla aunque los datos estén
perfectamente correctos, porque el valor esperado no es un parámetro
sino un número fijo dentro de la lógica.

Este módulo separa cada regla en su propia función, testeable de forma
independiente, y recibe los valores esperados como parámetros con
valores por defecto — visibles en la firma de la función, no ocultos
en el cuerpo. validar_dataset_procesado() se mantiene como función de
conveniencia que compone las reglas atómicas, para no romper el código
de F2 que ya la usa.
"""

from __future__ import annotations
import pandas as pd


def validar_sin_nulos(datos: pd.DataFrame, columnas: list[str] | None = None) -> int:
    """Valida que no existan valores nulos.

    Si `columnas` es None, revisa el DataFrame completo; si se entrega
    una lista, revisa solo esas columnas.
    """
    subconjunto = datos[columnas] if columnas is not None else datos
    nulos = int(subconjunto.isna().sum().sum())
    assert nulos == 0, f"Se detectaron {nulos} valores nulos."
    return nulos


def validar_sin_duplicados(datos: pd.DataFrame, columna_id: str) -> int:
    """Valida que no existan valores duplicados en la columna identificadora."""
    duplicados = int(datos[columna_id].duplicated().sum())
    assert duplicados == 0, (
        f"Se detectaron {duplicados} identificadores duplicados en '{columna_id}'."
    )
    return duplicados


def validar_sin_duplicados_exactos(datos: pd.DataFrame) -> int:
    """Valida que no existan filas completamente duplicadas (todas las columnas iguales)."""
    duplicados = int(datos.duplicated().sum())
    assert duplicados == 0, f"Se detectaron {duplicados} registros exactamente duplicados."
    return duplicados


def validar_no_negativos(datos: pd.DataFrame, columna: str) -> int:
    """Valida que una columna numérica no contenga valores negativos."""
    negativos = int((datos[columna] < 0).sum())
    assert negativos == 0, f"Se detectaron {negativos} valores negativos en '{columna}'."
    return negativos


def validar_granularidad(datos: pd.DataFrame, claves: list[str], esperado: int = 24) -> pd.Series:
    """Valida que cada combinación de las columnas `claves` tenga exactamente
    `esperado` observaciones (por defecto, 24 — una por hora).
    """
    conteo = datos.groupby(list(claves)).size()
    incumplidos = conteo[conteo != esperado]
    assert incumplidos.empty, (
        f"{len(incumplidos)} combinaciones de {list(claves)} no tienen "
        f"exactamente {esperado} observaciones."
    )
    return conteo


def validar_categorias_esperadas(datos: pd.DataFrame, columna: str, esperadas) -> set:
    """Valida que una columna categórica contenga EXACTAMENTE el conjunto de
    valores esperado (ni faltan ni sobran), en vez de solo un conteo fijo
    de categorías distintas.
    """
    presentes = set(datos[columna].dropna().unique())
    esperadas = set(esperadas)
    faltantes = esperadas - presentes
    inesperadas = presentes - esperadas
    assert not faltantes, f"Faltan categorías esperadas en '{columna}': {faltantes}"
    assert not inesperadas, f"Se encontraron categorías no esperadas en '{columna}': {inesperadas}"
    return presentes


def validar_dataset_procesado(
    datos: pd.DataFrame,
    centrales_esperadas=("TER CMPC LAJA", "TER CMPC PACIFICO", "TER CMPC SANTA FE"),
    filas_esperadas: int | None = 17496,
    columnas_esperadas: int | None = 13,
    columna_id: str = "ID_Observacion",
    columna_generacion: str = "Generacion_MWh",
    claves_granularidad=("Central", "Fecha"),
    horas_esperadas: int = 24,
) -> dict:
    """Valida dimensiones, integridad y granularidad del dataset procesado,
    componiendo las reglas atómicas de este módulo.

    Los valores esperados (centrales, filas, columnas) son parámetros con
    un valor por defecto igual al alcance actual del proyecto — visibles
    en la firma, no escritos dentro de la lógica. Si el período o el
    alcance cambian, se llama con otros valores (o con `filas_esperadas=None`
    / `columnas_esperadas=None` para omitir esa comprobación puntual) en
    vez de tener que editar el cuerpo de la función.
    """
    resultados = {
        "filas": len(datos),
        "columnas": datos.shape[1],
    }

    resultados["nulos"] = validar_sin_nulos(datos)
    resultados["duplicados_exactos"] = validar_sin_duplicados_exactos(datos)
    resultados["ids_duplicados"] = validar_sin_duplicados(datos, columna_id)
    resultados["negativos"] = validar_no_negativos(datos, columna_generacion)
    resultados["centrales"] = int(datos["Central"].nunique())
    resultados["fechas"] = int(datos["Fecha"].nunique())

    if filas_esperadas is not None:
        assert resultados["filas"] == filas_esperadas, (
            f"El dataset debe contener {filas_esperadas} observaciones "
            f"(tiene {resultados['filas']})."
        )

    if columnas_esperadas is not None:
        assert resultados["columnas"] == columnas_esperadas, (
            f"El dataset debe contener {columnas_esperadas} variables "
            f"(tiene {resultados['columnas']})."
        )

    if centrales_esperadas is not None:
        validar_categorias_esperadas(datos, "Central", centrales_esperadas)

    validar_granularidad(datos, list(claves_granularidad), esperado=horas_esperadas)

    return resultados
