def somarListaPorUmInteiro(lista: list, x: int) -> list:
    """ Recebe uma lista de números inteiros e um 
    número inteiro x e retorna uma nova lista com a soma de todos os elementos
    da lista por x
    >>> somarListaPorUmInteiro([1, 2, 3, 4], 2)
    [3, 4, 5, 6]
    >>> somarListaPorUmInteiro([1, 2, 3, 4], 3)
    [4, 5, 6, 7]
    """
    listaDeItensSomados = []

    for item in lista:
        listaDeItensSomados.append(item + x)
    
    return listaDeItensSomados