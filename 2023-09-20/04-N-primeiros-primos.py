def ehPrimo(n: int) -> bool:
    if n == 1:
        return False

    numeroEhPrimo = True

    for numero in range(2, n):
        if n % numero == 0:
            numeroEhPrimo = False

    return numeroEhPrimo

def NprimeirosNumerosPrimos(n: int) -> list:
    """ Recebe um número inteiro n e retorna uma lista com os n primeiros números primos.
    >>> NprimeirosNumerosPrimos(5)
    [2, 3, 5, 7, 11]
    >>> NprimeirosNumerosPrimos(10)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    numerosPrimos = []

    contador = 2
    while len(numerosPrimos) < n:
        if ehPrimo(contador):
            numerosPrimos.append(contador)

        contador += 1

    return numerosPrimos