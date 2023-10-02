def maiorDaLista(lista: list) -> int:
    """Recebe uma lista de números inteiros e retorna o maior elemento
    >>> maiorDaLista([1, 2, 3, 4])
    4
    >>> maiorDaLista([1, 9, 3, 4, 5])
    9
    """
    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero

    return maior