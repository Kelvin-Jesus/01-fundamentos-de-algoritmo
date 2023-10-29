def maiorItemDoArray(lista: list) -> int:
    """ Recebe uma lista não vazia de inteiros e retorna o maior valor.
    >>> maiorItemDoArray([1, 3, 4, 8, 10])
    10
    >>> maiorItemDoArray([1, 2, 3, 5])
    5
    >>> maiorItemDoArray([1, 2, 15, 5])
    15
    """
    if len(lista) == 1:
        return lista[0]
    
    primeiroItem = lista[0]
    maiorItem = maiorItemDoArray(lista[1:])

    if primeiroItem > maiorItem:
        return primeiroItem
    else:
        return maiorItem
