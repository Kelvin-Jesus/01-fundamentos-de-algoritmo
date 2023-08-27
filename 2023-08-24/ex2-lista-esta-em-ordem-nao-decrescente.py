def lista_eh_nao_decrescente(lista: list) -> bool:
    """
    Recebe uma lista de inteiros e retorna verdadeiro caso a lista esteja em ordem não decrescente
    >>> lista_eh_nao_decrescente([1, 2, 3, 4, 5])
    True
    >>> lista_eh_nao_decrescente([5, 4, 3, 2, 1])
    False
    """
    tamanho_da_lista = len(lista)
    for indice in range(1, tamanho_da_lista):
        if lista[indice] < lista[indice - 1]:
            return False

    return True