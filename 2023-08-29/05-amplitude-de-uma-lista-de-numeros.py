def aplitudeDeUmaLista(lista: list) -> int:
    """ Recebe uma lista de números inteiros e retorna a amplitude
    da lista, ou seja, a diferença entre o maior e o menor número da lista.
    >>> aplitudeDeUmaLista([1, 2, 3, 4])
    3
    >>> aplitudeDeUmaLista([1, 20, 3, 1, 12])
    19
    >>> aplitudeDeUmaLista([1, 1, 1, 1])
    0
    """

    return max(lista) - min(lista)

def aplitudeDeUmaLista2(lista: list) -> int:
    """ Recebe uma lista de números inteiros e retorna a amplitude
    da lista, ou seja, a diferença entre o maior e o menor número da lista.
    Versão 2: sem usar a função max() e min().
    >>> aplitudeDeUmaLista2([1, 2, 3, 4])
    3
    >>> aplitudeDeUmaLista2([1, 20, 3, 1, 12])
    19
    >>> aplitudeDeUmaLista2([1, 1, 1, 1])
    0
    """
    menorNumero = lista[0]
    maiorNumero = lista[0]

    for numero in lista:
        if numero < menorNumero:
            menorNumero = numero
        if numero > maiorNumero:
            maiorNumero = numero

    return maiorNumero - menorNumero