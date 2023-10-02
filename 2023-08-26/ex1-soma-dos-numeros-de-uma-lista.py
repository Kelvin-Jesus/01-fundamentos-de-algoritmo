def somaInterios(lista: list) -> int:
    """Recebe um alista de números inteiros e retorna a soma desses elementos
    >>> somaInterios([1, 2, 3, 4])
    10
    >>> somaInterios([1, 2, 3, 4, 5])
    15
    """
    somaDosInteiros = 0

    for numero in lista:
        somaDosInteiros += numero

    return somaDosInteiros