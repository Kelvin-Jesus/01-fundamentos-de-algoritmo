def calculaFatorial(n: int) -> int:
    """ Recebe um inteiro n e retorna o seu fatorial.
    >>> calculaFatorial(3)
    6
    >>> calculaFatorial(5)
    120
    """
    if n == 0:
        return 1

    return calculaFatorial(n - 1) * n
