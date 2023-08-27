def maior_numero(lista: list) -> int:
    """
    Recebe uma lista de números inteiros e retorna o maior entre eles.
    >>> maior_numero([1, 5, 3, 10])
    10
    >>> maior_numero([145, 234, 452, 94])
    452
    """
    maior_numero = 0
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
        
    return maior_numero