def validar_dimensiones(datos, filas_esperadas=17496, columnas_esperadas=13):
    """
    Valida las dimensiones esperadas del dataset.
    """
    assert len(datos) == filas_esperadas, (
        f"El dataset debe contener {filas_esperadas} observaciones."
    )

    assert datos.shape[1] == columnas_esperadas, (
        f"El dataset debe contener {columnas_esperadas} variables."
    )

    return True


def validar_nulos(datos):
    """
    Valida que el dataset no contenga valores nulos.
    """
    cantidad_nulos = int(datos.isna().sum().sum())

    assert cantidad_nulos == 0, (
        f"Se detectaron {cantidad_nulos} valores nulos."
    )

    return cantidad_nulos


def validar_duplicados(datos):
    """
    Valida que no existan registros completamente duplicados.
    """
    cantidad_duplicados = int(datos.duplicated().sum())

    assert cantidad_duplicados == 0, (
        f"Se detectaron {cantidad_duplicados} registros duplicados."
    )

    return cantidad_duplicados


def validar_ids_unicos(datos):
    """
    Valida que ID_Observacion sea único.
    """
    ids_duplicados = int(
        datos["ID_Observacion"].duplicated().sum()
    )

    assert ids_duplicados == 0, (
        f"Se detectaron {ids_duplicados} identificadores duplicados."
    )

    return ids_duplicados


def validar_generacion_no_negativa(datos):
    """
    Valida que no existan valores negativos de generación.
    """
    negativos = int(
        (datos["Generacion_MWh"] < 0).sum()
    )

    assert negativos == 0, (
        f"Se detectaron {negativos} valores negativos de generación."
    )

    return negativos


def validar_cantidad_centrales(datos, cantidad_esperada=3):
    """
    Valida la cantidad de centrales presentes en el dataset.
    """
    cantidad_centrales = int(
        datos["Central"].nunique()
    )

    assert cantidad_centrales == cantidad_esperada, (
        f"Se esperaban {cantidad_esperada} centrales "
        f"y se encontraron {cantidad_centrales}."
    )

    return cantidad_centrales


def validar_granularidad_horaria(datos):
    """
    Valida que cada combinación central-fecha
    contenga exactamente 24 observaciones horarias.
    """
    conteo_horas = datos.groupby(
        ["Central", "Fecha"]
    ).size()

    combinaciones_invalidas = int(
        (~conteo_horas.eq(24)).sum()
    )

    assert combinaciones_invalidas == 0, (
        "No todas las combinaciones central-fecha "
        "contienen exactamente 24 observaciones."
    )

    return combinaciones_invalidas


def validar_dataset_procesado(datos):
    """
    Coordina las validaciones individuales del dataset procesado.

    Retorna un resumen de los controles ejecutados.
    """
    validar_dimensiones(datos)
    nulos = validar_nulos(datos)
    duplicados = validar_duplicados(datos)
    ids_duplicados = validar_ids_unicos(datos)
    negativos = validar_generacion_no_negativa(datos)
    centrales = validar_cantidad_centrales(datos)
    granularidad_invalida = validar_granularidad_horaria(datos)

    resultados = {
        "filas": len(datos),
        "columnas": datos.shape[1],
        "nulos": nulos,
        "duplicados_exactos": duplicados,
        "ids_duplicados": ids_duplicados,
        "negativos": negativos,
        "centrales": centrales,
        "fechas": int(datos["Fecha"].nunique()),
        "granularidad_invalida": granularidad_invalida
    }

    return resultados
