def todosFalsos(listaDeBooleanos: list) -> bool:
    """"Recebe uma lista de booleanos e retorna True se todos 
    os elementos da lista forem False
    >>> todosFalsos([False, False, False, False])
    True
    >>> todosFalsos([False, False, True, False])
    False
    """
    retorno = True
    for booleano in listaDeBooleanos:
        if booleano is True:
            retorno = False
            break

    return retorno