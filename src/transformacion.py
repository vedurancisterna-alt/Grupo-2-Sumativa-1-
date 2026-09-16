import pandas as pd


def transformar_ancho_largo(datos, columnas_base, columnas_hora):
	"""
	Transforma los datos horarios del CEN desde formato ancho
	a formato largo.

	Parámetros
	----------
	datos : pandas.DataFrame
		Dataset filtrado por las centrales del estudio.

	columnas_base : list
		Variables que deben mantenerse durante la transformación.

	columnas_hora : list
		Columnas Hora 1 a Hora 24.

	Retorna
	-------
	pandas.DataFrame
		Dataset transformado a granularidad central-fecha-hora.
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
