def listaEhNaoDecrescente(lista: list) -> bool:
    """ Recebe uma lista de inteiros e retorna verdadeiro caso a 
    lista esteja em ordem não decrescente
    >>> listaEhNaoDecrescente([1, 2, 3, 4, 5])
    True
    >>> listaEhNaoDecrescente([5, 4, 3, 2, 1])
    False
    >>> listaEhNaoDecrescente([1, 4, 8, 2, 1])
    False
    >>> listaEhNaoDecrescente([1, 4, 8, 8, 11])
    True
    """
    if len(lista) < 2:
        return True
    
    if lista[0] > lista[1]:
        return False

    return listaEhNaoDecrescente(lista[1:])