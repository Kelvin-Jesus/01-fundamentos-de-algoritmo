def calculaPotencia(base: int, potencia: int) -> int:
    """ Recebe um valor base != 0 que será elevado a um natural n.
    >>> calculaPotencia(2, 2)
    4
    >>> calculaPotencia(5, 2)
    25
    >>> calculaPotencia(10, 4)
    10000
    """
    if potencia == 0:
        return 1

    return calculaPotencia(base, potencia - 1) * base