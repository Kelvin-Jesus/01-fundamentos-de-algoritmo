def somaItensDoArray(arrayDeNumeros: list) -> float:
    """ Recebe um array de números e retorna a soma total dos elementos.
    >>> somaItensDoArray([1, 2, 3])
    6
    >>> somaItensDoArray([2, 2, 8])
    12
    >>> somaItensDoArray([3, 3, 3])
    9
    >>> somaItensDoArray([347, 6798, 2345])
    9490
    """
    if len(arrayDeNumeros) == 0:
        return 0

    return somaItensDoArray(arrayDeNumeros[:len(arrayDeNumeros) - 1]) + arrayDeNumeros[-1]
