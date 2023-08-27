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

def indice_maior_numero(lista: list) -> int:
    """
    Recebe uma lista de numeros inteiros e retorna o índice da primeira ocorrência do maior número. 
    >>> indice_maior_numero([10, 10, 9])
    0
    >>> indice_maior_numero([20, 44, 2, 2093])
    3
    """
    if len(lista) <= 0:
        return -1
    
    maior_numero_da_lista = maior_numero(lista)

    tamanho_da_lista = len(lista)
    for indice in range(tamanho_da_lista):
        if lista[indice] == maior_numero_da_lista:
            indice_maior_numero_da_lista = indice
            break

    
    return indice_maior_numero_da_lista