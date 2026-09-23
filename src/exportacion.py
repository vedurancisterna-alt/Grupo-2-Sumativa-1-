from pathlib import Path


def exportar_dataset(datos, ruta_salida):
    """
    Exporta un DataFrame a formato CSV.

    La función crea automáticamente la carpeta de destino
    cuando esta no existe.

    Parámetros
    ----------
    datos : pandas.DataFrame
        Dataset que se desea exportar.

    ruta_salida : str o Path
        Ruta donde se guardará el archivo CSV.

    Retorna
    -------
    pathlib.Path
        Ruta del archivo exportado.
    """
    ruta_salida = Path(ruta_salida)

    ruta_salida.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    datos.to_csv(
        ruta_salida,
        index=False,
        encoding="utf-8-sig"
    )

    return ruta_salida