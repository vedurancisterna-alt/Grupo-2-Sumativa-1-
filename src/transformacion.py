import pandas as pd


def filtrar_periodo(datos, fecha_inicio, fecha_fin):
    """
    Filtra el dataset según un período de fechas definido.

    Parámetros
    ----------
    datos : pandas.DataFrame
        Dataset que contiene la variable Fecha.

    fecha_inicio : str
        Fecha inicial del período de análisis.

    fecha_fin : str
        Fecha final del período de análisis.

    Retorna
    -------
    pandas.DataFrame
        Copia del dataset correspondiente al período seleccionado.
    """
    resultado = datos.copy()

    resultado["Fecha"] = pd.to_datetime(
        resultado["Fecha"],
        format="mixed",
        errors="raise"
    )

    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = pd.to_datetime(fecha_fin)

    if fecha_inicio > fecha_fin:
        raise ValueError(
            "La fecha de inicio no puede ser posterior "
            "a la fecha de término."
        )

    resultado = resultado[
        resultado["Fecha"].between(
            fecha_inicio,
            fecha_fin,
            inclusive="both"
        )
    ].copy()

    if resultado.empty:
        raise ValueError(
            "El filtrado temporal no encontró registros "
            "en el período seleccionado."
        )

    return resultado


def filtrar_centrales(datos, centrales):
    """
    Filtra el dataset según las centrales definidas para el estudio.

    Parámetros
    ----------
    datos : pandas.DataFrame
        Dataset original o previamente preparado.

    centrales : list
        Lista de centrales que forman parte del alcance del estudio.

    Retorna
    -------
    pandas.DataFrame
        Copia del dataset que contiene únicamente
        las centrales seleccionadas.
    """
    datos_filtrados = datos[
        datos["Central"].isin(centrales)
    ].copy()

    if datos_filtrados.empty:
        raise ValueError(
            "El filtrado no encontró registros "
            "para las centrales seleccionadas."
        )

    return datos_filtrados


def transformar_ancho_largo(
    datos,
    columnas_base,
    columnas_hora
):
    """
    Transforma los datos horarios del CEN
    desde formato ancho a formato largo.

    Parámetros
    ----------
    datos : pandas.DataFrame
        Dataset filtrado para el estudio.

    columnas_base : list
        Variables que deben mantenerse durante
        la transformación.

    columnas_hora : list
        Columnas correspondientes a Hora 1 a Hora 24.

    Retorna
    -------
    pandas.DataFrame
        Dataset transformado a granularidad
        central-fecha-hora.
    """
    datos_long = datos.melt(
        id_vars=columnas_base,
        value_vars=columnas_hora,
        var_name="Hora",
        value_name="Generacion_MWh"
    )

    datos_long["Hora"] = (
        datos_long["Hora"]
        .str.extract(r"(\d+)")
        .astype(int)
    )

    datos_long["Generacion_MWh"] = pd.to_numeric(
        datos_long["Generacion_MWh"],
        errors="raise"
    )

    return datos_long


def crear_dia_semana(datos):
    """
    Crea la variable Dia_Semana a partir de Fecha.

    Parámetros
    ----------
    datos : pandas.DataFrame
        Dataset que contiene la variable Fecha.

    Retorna
    -------
    pandas.DataFrame
        Copia del dataset con la variable
        Dia_Semana incorporada.
    """
    resultado = datos.copy()

    resultado["Fecha"] = pd.to_datetime(
        resultado["Fecha"],
        errors="raise"
    )

    dias_espanol = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }

    resultado["Dia_Semana"] = (
        resultado["Fecha"]
        .dt.dayofweek
        .map(dias_espanol)
    )

    return resultado


def crear_id_observacion(datos):
    """
    Construye un identificador único para cada observación
    central-fecha-hora.

    Los espacios del nombre de la central se reemplazan
    por guiones bajos para mantener el formato utilizado
    originalmente en el proyecto.

    Parámetros
    ----------
    datos : pandas.DataFrame
        Dataset con las columnas Central, Fecha y Hora.

    Retorna
    -------
    pandas.DataFrame
        Copia del dataset con ID_Observacion incorporado.
    """
    resultado = datos.copy()

    resultado["Fecha"] = pd.to_datetime(
        resultado["Fecha"],
        errors="raise"
    )

    resultado["ID_Observacion"] = (
        resultado["Central"]
        .astype(str)
        .str.replace(" ", "_", regex=False)
        + "_"
        + resultado["Fecha"].dt.strftime("%Y%m%d")
        + "_H"
        + resultado["Hora"]
        .astype(str)
        .str.zfill(2)
    )

    return resultado