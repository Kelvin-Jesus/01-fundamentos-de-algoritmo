def sorteado(numeroAhChecarSeFoiSorteado: int, sorteados: list) -> bool:
    """
    Produz True se *n* for um dos numeros em * sorteados *. False caso
    contrario.
    >>> sorteados = [1, 7, 10, 40, 41, 60]
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
    if numeroAhChecarSeFoiSorteado in sorteados:
        foiSorteado = True
    else:
        foiSorteado = False
    
    return foiSorteado

def numero_acertos(aposta: list, sorteados: list) -> int:
    """
    Determina quantoas números da *aposta* estão em sorteados*
    >>> numero_acertos([1, 2, 3, 4, 5, 6], [8, 12, 20, 41, 52, 57])
    0
    >>> numero_acertos([8, 12, 20 , 4, 5, 6], [8, 12, 20, 41, 52, 57])
    3
    >>> numero_acertos([8, 12, 20, 41, 52, 57], [8, 12, 20, 41, 52, 57])
    6
    """
    acertos: int = 0

    for numeroDaAposta in aposta:
        if (sorteado(numeroDaAposta, sorteados)):
            acertos += 1

    return acertos