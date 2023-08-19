from dataclasses import dataclass
import math

@dataclass
class IntervaloDeTempo:
    horas: int
    minutos: int

def calcula_minutos_em_horas(minutos: int) -> IntervaloDeTempo:
    """
    Recebe um inteiro que representa um intervalo de tempo em minutos e
    retorna o tempo em horas e minutos. 
    >>> calcula_minutos_em_horas(131).horas
    2
    >>> calcula_minutos_em_horas(131).minutos
    11
    >>> calcula_minutos_em_horas(119).horas
    1
    >>> calcula_minutos_em_horas(119).minutos
    59
    """
    horas = math.floor(minutos / 60)
    minutos_restantes = minutos - (60 * horas)
    if minutos_restantes < 0:
        minutos_restantes = 0

    print(f"horas: {horas} | minutos {minutos_restantes}")
    # horas_minutos = HorasMinutos()
    return IntervaloDeTempo(horas, minutos_restantes)

def ler_tempo():
    minutos: int = int(input("Digite a quantidade de tempo em minutos: "))
    intervalo_de_tempo = calcula_minutos_em_horas(minutos)

    print(f"A quantidade de minutos digitados representam {intervalo_de_tempo.horas} em horas e {intervalo_de_tempo.minutos} minutos")

ler_tempo()