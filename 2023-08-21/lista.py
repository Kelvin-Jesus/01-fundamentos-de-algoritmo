from dataclasses import dataclass

@dataclass
class SeisNumeros:
    a: int
    b: int
    c: int
    d: int
    e: int
    f: int

def sorteado(n: int, sorteados: SeisNumeros) -> bool:
    """
    Produz True se *n* for um dos numeros em * sorteados *. False caso
    contrario.
    >>> sorteados = SeisNumeros (1, 7, 10, 40, 41, 60)
    >>> sorteado(1, sorteados)
    True
    >>> sorteado(7, sorteados)
    True
    >>> sorteado(10, sorteados)
    True
    >>> sorteado(40, sorteados)
    True
    >>> sorteado(41, sorteados)
    True
    >>> sorteado(60, sorteados)
    True
    >>> sorteado(2, sorteados)
    False
    """
    if n == sorteados.a:
        sorteado = True
    elif n == sorteados.b:
        sorteado = True
    elif n == sorteados.c:
        sorteado = True 
    elif n == sorteados.d:
        sorteado = True
    elif n == sorteados.e:
        sorteado = True
    elif n == sorteados.f:
        sorteado = True
    else:
        sorteado = False
    
    return sorteado

def numero_acertos(aposta: SeisNumeros, sorteados: SeisNumeros) -> int:
    """
    Determina quantoas números da *aposta* estão em sorteados*
    >>> numero_acertos(SeisNumeros(1, 2, 3, 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    0
    >>> numero_acertos(SeisNumeros(8, 12, 20 , 4, 5, 6), SeisNumeros(8, 12, 20, 41, 52, 57))
    3
    >>> numero_acertos(SeisNumeros(8, 12, 20, 41, 52, 57), SeisNumeros(8, 12, 20, 41, 52, 57))
    6
    """
    acertos = 0
    if sorteado(aposta.a, sorteados):
        acertos += 1
    if sorteado(aposta.b, sorteados):
        acertos += 1
    if sorteado(aposta.c, sorteados):
        acertos += 1
    if sorteado(aposta.d, sorteados):
        acertos += 1
    if sorteado(aposta.e, sorteados):
        acertos += 1
    if sorteado(aposta.f, sorteados):
        acertos += 1

    return acertos