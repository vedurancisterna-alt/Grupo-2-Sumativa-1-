def validar_dataset_procesado(datos):
	"""
	Valida dimensiones, integridad y granularidad
	del dataset procesado.

	Parámetros
	----------
	datos : pandas.DataFrame
		Dataset final que se desea validar.

	Retorna
	-------
	dict
		Resumen de las validaciones realizadas.
	"""

	resultados = {
		"filas": len(datos),
		"columnas": datos.shape[1],
		"nulos": int(datos.isna().sum().sum()),
		"duplicados_exactos": int(datos.duplicated().sum()),
		"ids_duplicados": int(
			datos["ID_Observacion"].duplicated().sum()
		),
		"negativos": int(
			(datos["Generacion_MWh"] < 0).sum()
		),
		"centrales": int(datos["Central"].nunique()),
		"fechas": int(datos["Fecha"].nunique())
	}

	assert resultados["filas"] == 17496, (
		"El dataset debe contener 17.496 observaciones."
	)

	assert resultados["columnas"] == 13, (
		"El dataset debe contener 13 variables."
	)

	assert resultados["nulos"] == 0, (
		"Se detectaron valores nulos."
	)

	assert resultados["duplicados_exactos"] == 0, (
		"Se detectaron registros duplicados."
	)

	assert resultados["ids_duplicados"] == 0, (
		"Se detectaron identificadores duplicados."
	)

	assert resultados["negativos"] == 0, (
		"Se detectaron valores negativos de generación."
	)

	assert resultados["centrales"] == 3, (
		"El dataset debe contener exactamente tres centrales."
	)

	conteo_horas = datos.groupby(
		["Central", "Fecha"]
	).size()

	assert conteo_horas.eq(24).all(), (
		"No todas las combinaciones central-fecha "
		"contienen 24 observaciones."
	)

	return resultados
