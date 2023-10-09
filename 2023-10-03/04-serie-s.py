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

def calculaValorDaSerie(n: int) -> float:
    """ Recebe um inteiro n > 0 e retorna o valor da série S: 1+1/2!+1/3!+1/n!
    >>> calculaValorDaSerie(1)
    1
    >>> calculaValorDaSerie(2)
    1.5
    """
    if n == 1:
        return 1
    
    termoAtualDaSerie = 1 / calculaFatorial(n)
    return termoAtualDaSerie + calculaValorDaSerie(n - 1)