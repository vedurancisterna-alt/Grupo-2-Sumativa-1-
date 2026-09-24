"""
Módulo de análisis algorítmico para la Fase 3.

Proyecto:
Caracterización de patrones temporales de generación eléctrica de las centrales
TER CMPC Laja, TER CMPC Pacífico y TER CMPC Santa Fe, enero-agosto de 2026.

Propósito:
- Detectar secuencias consecutivas de generación igual a 0 MWh.
- Comparar una solución iterativa y una solución recursiva.
- Ejecutar pruebas controladas.
- Medir tiempos de ejecución con timeit.
- Medir memoria con tracemalloc.
- Apoyar el análisis de complejidad temporal y espacial.

Importante:
Un registro de 0 MWh se trata como una observación válida del dataset.
Este módulo no atribuye causas operacionales a esos registros.
"""

from __future__ import annotations

import sys
import timeit
import tracemalloc
from numbers import Real
from typing import Iterable, Sequence

import pandas as pd


def _validar_valores(valores: Iterable[Real]) -> list[Real]:
    """
    Valida y convierte la entrada a lista.

    Parameters
    ----------
    valores : iterable de números
        Secuencia de valores de generación.

    Returns
    -------
    list
        Valores validados.

    Raises
    ------
    TypeError
        Si la entrada no es iterable o contiene elementos no numéricos.
    """
    if valores is None:
        raise TypeError("La entrada 'valores' no puede ser None.")

    try:
        lista = list(valores)
    except TypeError as exc:
        raise TypeError("'valores' debe ser una secuencia iterable.") from exc

    if not all(isinstance(valor, Real) for valor in lista):
        raise TypeError("Todos los elementos de 'valores' deben ser numéricos.")

    return lista


def secuencias_cero_iterativa(valores: Iterable[Real]) -> list[int]:
    """
    Detecta longitudes de secuencias consecutivas de valores iguales a 0
    mediante programación iterativa.

    Complejidad temporal: O(n)
    Espacio auxiliar: O(1), sin considerar la lista de resultados.
    """
    lista = _validar_valores(valores)

    secuencias: list[int] = []
    contador = 0

    for valor in lista:
        if valor == 0:
            contador += 1
        elif contador > 0:
            secuencias.append(contador)
            contador = 0

    if contador > 0:
        secuencias.append(contador)

    return secuencias


def _secuencias_cero_recursiva_interna(
    valores: Sequence[Real],
    indice: int,
    contador: int,
    secuencias: list[int],
) -> list[int]:
    """Implementación recursiva interna. La validación se realiza una sola vez."""
    # Caso base: se alcanzó el final de la secuencia.
    if indice == len(valores):
        if contador > 0:
            secuencias.append(contador)
        return secuencias

    # Caso recursivo: continúa una secuencia de ceros.
    if valores[indice] == 0:
        return _secuencias_cero_recursiva_interna(
            valores,
            indice + 1,
            contador + 1,
            secuencias,
        )

    # Si aparece un valor distinto de cero, se cierra la secuencia anterior.
    if contador > 0:
        secuencias.append(contador)

    return _secuencias_cero_recursiva_interna(
        valores,
        indice + 1,
        0,
        secuencias,
    )


def secuencias_cero_recursiva(valores: Iterable[Real]) -> list[int]:
    """
    Detecta longitudes de secuencias consecutivas de valores iguales a 0
    mediante recursividad.

    Complejidad temporal: O(n)
    Espacio auxiliar: O(n) por la pila de llamadas.

    Nota
    ----
    Esta implementación se utiliza con fines comparativos y pedagógicos.
    Python limita la profundidad de recursión, por lo que no es la opción
    recomendada para procesar directamente series extensas.
    """
    lista = _validar_valores(valores)

    # Se deja margen respecto del límite para evitar un RecursionError
    # durante las pruebas controladas.
    margen_seguridad = 50
    maximo_seguro = max(1, sys.getrecursionlimit() - margen_seguridad)

    if len(lista) > maximo_seguro:
        raise ValueError(
            "La secuencia es demasiado extensa para la implementación "
            f"recursiva controlada ({len(lista)} elementos). "
            f"Use como máximo {maximo_seguro} elementos o utilice la "
            "implementación iterativa."
        )

    return _secuencias_cero_recursiva_interna(lista, 0, 0, [])


def resumir_secuencias(secuencias: Sequence[int]) -> dict[str, float | int]:
    """
    Resume las secuencias detectadas sin atribuir causas operacionales.
    """
    if not secuencias:
        return {
            "numero_secuencias": 0,
            "duracion_maxima_horas": 0,
            "duracion_promedio_horas": 0.0,
            "total_horas_cero_en_secuencias": 0,
        }

    return {
        "numero_secuencias": len(secuencias),
        "duracion_maxima_horas": max(secuencias),
        "duracion_promedio_horas": sum(secuencias) / len(secuencias),
        "total_horas_cero_en_secuencias": sum(secuencias),
    }


def analizar_secuencias_por_central(
    datos: pd.DataFrame,
    columna_central: str = "Central",
    columna_fecha: str = "Fecha",
    columna_hora: str = "Hora",
    columna_generacion: str = "Generacion_MWh",
) -> pd.DataFrame:
    """
    Aplica la solución iterativa al dataset real y genera un resumen por central.

    El orden Fecha-Hora es importante porque el algoritmo analiza continuidad
    temporal entre observaciones.
    """
    requeridas = {
        columna_central,
        columna_fecha,
        columna_hora,
        columna_generacion,
    }
    faltantes = requeridas.difference(datos.columns)

    if faltantes:
        raise ValueError(
            "Faltan columnas requeridas: " + ", ".join(sorted(faltantes))
        )

    resultados = []

    for central, grupo in datos.groupby(columna_central):
        grupo_ordenado = grupo.sort_values([columna_fecha, columna_hora])
        valores = grupo_ordenado[columna_generacion].tolist()

        secuencias = secuencias_cero_iterativa(valores)
        resumen = resumir_secuencias(secuencias)
        resumen[columna_central] = central
        resultados.append(resumen)

    columnas = [
        columna_central,
        "numero_secuencias",
        "duracion_maxima_horas",
        "duracion_promedio_horas",
        "total_horas_cero_en_secuencias",
    ]

    return pd.DataFrame(resultados)[columnas]


def _medir_memoria(funcion, valores: Sequence[Real]) -> int:
    """Devuelve el pico aproximado de memoria, en bytes, durante una ejecución."""
    tracemalloc.start()
    try:
        funcion(valores)
        _, pico = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return pico


def comparar_implementaciones(
    valores: Iterable[Real],
    tamanos: Sequence[int] = (100, 250, 500, 750),
    repeticiones: int = 100,
) -> pd.DataFrame:
    """
    Compara tiempo y memoria de las implementaciones iterativa y recursiva.

    Para cada tamaño n:
    - verifica que ambas soluciones entreguen el mismo resultado;
    - mide tiempo promedio con timeit;
    - mide memoria máxima aproximada con tracemalloc.

    Los tiempos dependen del equipo donde se ejecute el código y, por lo tanto,
    deben obtenerse mediante ejecución real; no se fijan valores de antemano.
    """
    lista = _validar_valores(valores)

    if repeticiones <= 0:
        raise ValueError("'repeticiones' debe ser mayor que cero.")

    if not tamanos:
        raise ValueError("Debe indicarse al menos un tamaño de prueba.")

    limite_recursion = max(1, sys.getrecursionlimit() - 50)
    resultados = []

    for n in tamanos:
        if n <= 0:
            raise ValueError("Todos los tamaños de prueba deben ser mayores que cero.")

        if n > len(lista):
            raise ValueError(
                f"El tamaño n={n} supera la cantidad de datos disponibles "
                f"({len(lista)})."
            )

        if n > limite_recursion:
            raise ValueError(
                f"n={n} supera el tamaño recursivo controlado "
                f"({limite_recursion})."
            )

        muestra = lista[:n]

        resultado_iterativo = secuencias_cero_iterativa(muestra)
        resultado_recursivo = secuencias_cero_recursiva(muestra)

        equivalentes = resultado_iterativo == resultado_recursivo

        if not equivalentes:
            raise AssertionError(
                f"Las implementaciones no son equivalentes para n={n}."
            )

        tiempo_iterativo = timeit.timeit(
            lambda: secuencias_cero_iterativa(muestra),
            number=repeticiones,
        ) / repeticiones

        tiempo_recursivo = timeit.timeit(
            lambda: secuencias_cero_recursiva(muestra),
            number=repeticiones,
        ) / repeticiones

        memoria_iterativa = _medir_memoria(
            secuencias_cero_iterativa,
            muestra,
        )
        memoria_recursiva = _medir_memoria(
            secuencias_cero_recursiva,
            muestra,
        )

        resultados.append(
            {
                "n": n,
                "tiempo_iterativo_s": tiempo_iterativo,
                "tiempo_recursivo_s": tiempo_recursivo,
                "memoria_iterativa_bytes": memoria_iterativa,
                "memoria_recursiva_bytes": memoria_recursiva,
                "resultados_equivalentes": equivalentes,
            }
        )

    return pd.DataFrame(resultados)


def ejecutar_pruebas_controladas() -> dict[str, str]:
    """
    Ejecuta casos normales, límite y de excepción requeridos para F3.
    """
    resultados: dict[str, str] = {}

    # Caso normal.
    normal = [5, 0, 0, 3, 0, 8, 0, 0, 0]
    esperado = [2, 1, 3]

    assert secuencias_cero_iterativa(normal) == esperado
    assert secuencias_cero_recursiva(normal) == esperado
    resultados["caso_normal"] = "OK"

    # Caso límite: sin ceros.
    sin_ceros = [5, 3, 8]
    assert secuencias_cero_iterativa(sin_ceros) == []
    assert secuencias_cero_recursiva(sin_ceros) == []
    resultados["limite_sin_ceros"] = "OK"

    # Caso límite: todos los registros son cero.
    todos_ceros = [0, 0, 0]
    assert secuencias_cero_iterativa(todos_ceros) == [3]
    assert secuencias_cero_recursiva(todos_ceros) == [3]
    resultados["limite_todos_ceros"] = "OK"

    # Caso límite: secuencia vacía.
    assert secuencias_cero_iterativa([]) == []
    assert secuencias_cero_recursiva([]) == []
    resultados["limite_vacio"] = "OK"

    # Caso de excepción: dato no numérico.
    try:
        secuencias_cero_iterativa([0, "dato_invalido", 0])
    except TypeError:
        resultados["excepcion_tipo"] = "OK"
    else:
        raise AssertionError("No se detectó el dato no numérico.")

    return resultados


if __name__ == "__main__":
    print("Pruebas controladas F3")
    print(ejecutar_pruebas_controladas())

    ejemplo = [5, 0, 0, 3, 0, 8, 0, 0, 0]
    print("\nEjemplo iterativo:", secuencias_cero_iterativa(ejemplo))
    print("Ejemplo recursivo:", secuencias_cero_recursiva(ejemplo))
    print("Resumen:", resumir_secuencias(secuencias_cero_iterativa(ejemplo)))
