import pandas as pd
from pathlib import Path


def cargar_datos_cen(ruta_archivo):
    """
    Carga el archivo CSV de Generación Real del CEN.

    Parámetros
    ----------
    ruta_archivo : str o Path
        Ruta del archivo CSV original.

    Retorna
    -------
    pandas.DataFrame
        Dataset cargado desde la fuente.
    """

    ruta_archivo = Path(ruta_archivo)

    if not ruta_archivo.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo fuente: {ruta_archivo}"
        )

    datos = pd.read_csv(
        ruta_archivo,
        sep=";",
        decimal=",",
        encoding="utf-8-sig"
    )

    return datos
