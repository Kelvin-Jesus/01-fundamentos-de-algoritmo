def calcularMultiplicacao(x: int, y: int) -> int:
    """ Recebe dois inteiros x e y e retorna a multiplicação 
    deles através de soma sucessiva.
    >>> calcularMultiplicacao(3, 5)
    15
    >>> calcularMultiplicacao(2, 10)
    20
    >>> calcularMultiplicacao(10, 10)
    100
    """
    if x == 1:
        return y

    return y + calcularMultiplicacao(x - 1, y)