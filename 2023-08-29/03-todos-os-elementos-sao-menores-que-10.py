def elementosDaListaSaoMenoresQue10(lista: list) -> bool:
    """ Recebe uma lista de números inteiros e retorna True se 
    todos os elementos forem menores que 10.
    >>> elementosDaListaSaoMenoresQue10([1, 2, 3, 4])
    True
    >>> elementosDaListaSaoMenoresQue10([1, 20, 3, 4, 12])
    False
    """
    retorno = True
    for numero in lista:
        if numero >= 10:
            retorno = False
            break

    return retorno