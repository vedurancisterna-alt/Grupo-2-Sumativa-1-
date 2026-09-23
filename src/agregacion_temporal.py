"""
Patrón Strategy: agregación temporal de la generación eléctrica.

Este módulo resuelve el Objetivo específico 1 del proyecto:
"Caracterizar la distribución horaria, diaria y mensual de la generación
eléctrica de las tres centrales seleccionadas."

En vez de tres bloques de código repetidos (uno por nivel de agregación),
cada nivel es una clase intercambiable que implementa el mismo contrato
(EstrategiaAgregacion). Agregar un nivel nuevo (por ejemplo, por día de
la semana) no modifica nada existente: solo se agrega una clase más.

Referencia de patrón: Gamma, E., Helm, R., Johnson, R., & Vlissides, J.
(1994). Design Patterns: Elements of Reusable Object-Oriented Software.
Addison-Wesley.
"""

from __future__ import annotations
import pandas as pd


class EstrategiaAgregacion:
    """Contrato común de toda estrategia de agregación temporal.

    Cada estrategia debe implementar `agregar`, que recibe el dataset
    procesado (formato largo) y devuelve la generación agregada según
    su propio criterio temporal.
    """

    etiqueta: str = "sin definir"

    def agregar(self, df: pd.DataFrame) -> pd.Series:
        raise NotImplementedError("Cada estrategia debe implementar agregar().")


class AgregacionHoraria(EstrategiaAgregacion):
    """Generación promedio por central y hora del día (perfil horario)."""

    etiqueta = "horaria"

    def agregar(self, df: pd.DataFrame) -> pd.Series:
        return (
            df.groupby(["Central", "Hora"])["Generacion_MWh"]
            .mean()
            .rename("Generacion_MWh_promedio")
        )


class AgregacionDiaria(EstrategiaAgregacion):
    """Generación total por central y fecha."""

    etiqueta = "diaria"

    def agregar(self, df: pd.DataFrame) -> pd.Series:
        return (
            df.groupby(["Central", "Fecha"])["Generacion_MWh"]
            .sum()
            .rename("Generacion_MWh_total")
        )


class AgregacionMensual(EstrategiaAgregacion):
    """Generación total por central y mes."""

    etiqueta = "mensual"

    def agregar(self, df: pd.DataFrame) -> pd.Series:
        return (
            df.groupby(["Central", "Mes"])["Generacion_MWh"]
            .sum()
            .rename("Generacion_MWh_total")
        )


class AgregacionPorDiaSemana(EstrategiaAgregacion):
    """Generación promedio por central y día de la semana.

    Nivel adicional, no pedido explícitamente en el objetivo, pero
    demuestra la extensibilidad del patrón: se agrega sin tocar
    ninguna de las clases anteriores ni el caracterizador que las usa.
    """

    etiqueta = "dia_semana"

    def agregar(self, df: pd.DataFrame) -> pd.Series:
        return (
            df.groupby(["Central", "Dia_Semana"])["Generacion_MWh"]
            .mean()
            .rename("Generacion_MWh_promedio")
        )


class CaracterizadorTemporal:
    """Aplica una estrategia de agregación sin conocer cuál es.

    Uso:
        caracterizador = CaracterizadorTemporal(AgregacionHoraria())
        perfil_horario = caracterizador.caracterizar(df)

        # Cambiar de estrategia no requiere tocar esta clase:
        caracterizador.estrategia = AgregacionMensual()
        perfil_mensual = caracterizador.caracterizar(df)
    """

    def __init__(self, estrategia: EstrategiaAgregacion):
        self.estrategia = estrategia

    def caracterizar(self, df: pd.DataFrame) -> pd.Series:
        return self.estrategia.agregar(df)


def comparar_centrales(df: pd.DataFrame, estrategia: EstrategiaAgregacion) -> pd.DataFrame:
    """Aplica una estrategia y reordena el resultado para comparar
    directamente las tres centrales lado a lado (Objetivo específico 2).
    """
    caracterizador = CaracterizadorTemporal(estrategia)
    resultado = caracterizador.caracterizar(df)
    return resultado.unstack(level="Central")


if __name__ == "__main__":
    # Ejemplo mínimo de uso con datos sintéticos, solo para verificar
    # que el módulo corre de forma independiente.
    datos_ejemplo = pd.DataFrame({
        "Central": ["TER CMPC LAJA"] * 4 + ["TER CMPC PACIFICO"] * 4,
        "Fecha": pd.to_datetime(["2026-01-01"] * 8),
        "Hora": [1, 2, 3, 4, 1, 2, 3, 4],
        "Mes": [1] * 8,
        "Dia_Semana": ["Jueves"] * 8,
        "Generacion_MWh": [10, 12, 8, 15, 20, 18, 22, 19],
    })

    for estrategia in [AgregacionHoraria(), AgregacionDiaria(),
                        AgregacionMensual(), AgregacionPorDiaSemana()]:
        caracterizador = CaracterizadorTemporal(estrategia)
        print(f"\n--- Estrategia: {estrategia.etiqueta} ---")
        print(caracterizador.caracterizar(datos_ejemplo))
