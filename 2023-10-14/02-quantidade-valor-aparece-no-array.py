def quantidadeDeVezesQueXApareceNoArray(x: float, listaDeValores: list) -> int:
    """ Recebe um valor X e uma lista de valores. Apartir disso retorna a quantidade 
    de vezes que esse item apareceu no array.
    >>> quantidadeDeVezesQueXApareceNoArray(2, [2, 2, 2, 8])
    3
    >>> quantidadeDeVezesQueXApareceNoArray(8, [2, 8, 7, 8, 8, 3, 4, 3, 3, 5, 8, 9])
    4
    """
    if len(listaDeValores) == 0:
        return 0

    elif listaDeValores[0] == x:
        return 1 + quantidadeDeVezesQueXApareceNoArray(x, listaDeValores[1:])

    else:
        return quantidadeDeVezesQueXApareceNoArray(x, listaDeValores[1:])
