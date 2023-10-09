def somaNaturais(n: int) -> int:
    """ Recebe um inteiro natural e retorna a soma de todos os naturais menores que n.
    >>> somaNaturais(10)
    55
    >>> somaNaturais(5)
    15
    >>> somaNaturais(3)
    6
    """
    if n == 0:
        return 0

    return somaNaturais(n - 1) + n