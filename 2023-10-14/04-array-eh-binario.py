def arrayEhBinario(lista: list) -> bool:
    """ Recebe um array binário e deve verificar se realmente 
    só possue valores binários
    >>> arrayEhBinario([0, 1, 0, 0, 1, 1, 0])
    True
    >>> arrayEhBinario([0, 1, 2, 0, 1, 3])
    False
    """
    if len(lista) == 0:
        return True

    if lista[0] != 0 and lista[0] != 1:
        return False

    return arrayEhBinario(lista[1:])
    
    