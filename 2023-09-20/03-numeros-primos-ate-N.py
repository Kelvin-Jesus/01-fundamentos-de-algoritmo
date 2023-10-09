def ehPrimo(n: int) -> bool:
    if n == 1:
        return False

    numeroEhPrimo = True

    for numero in range(2, n):
        if n % numero == 0:
            numeroEhPrimo = False

    return numeroEhPrimo

def numerosPrimosAteN(n: int) -> list:
    """
    Recebe um número inteiro n e retorna uma lista com todos os números primos até N
    >>> numerosPrimosAteN(10)
    [2, 3, 5, 7]
    >>> numerosPrimosAteN(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    numerosPrimos = []

    for numero in range(2, n+1):
        if ehPrimo(numero):
            numerosPrimos.append(numero)

    return numerosPrimos