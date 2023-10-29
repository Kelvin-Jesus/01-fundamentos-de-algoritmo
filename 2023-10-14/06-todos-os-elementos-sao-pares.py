def todosOsElementosSaoPares(lista: list) -> bool:
    """ Recebe uma lista de números e retorna True caso todos os itens sejam par
    e caso contrário, False.
    >>> todosOsElementosSaoPares([2, 4, 5, 6, 4])
    False
    >>> todosOsElementosSaoPares([2, 4, 6, 8, 10])
    True
    >>> todosOsElementosSaoPares([22, 68, 20, 120])
    True
    >>> todosOsElementosSaoPares([2, 4, 1, 7, 10])
    False
    """
    if len(lista) == 0:
        return True
    
    if lista[0] % 2 != 0:
        return False

    return todosOsElementosSaoPares(lista[1:]) 