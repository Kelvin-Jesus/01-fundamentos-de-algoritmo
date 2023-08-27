def soma_numeros(lista: list) -> int:
    """
    Recebe uma lista de valores a serem somados e retorna a 
    soma total de todos os itens da lista.
    >>> soma_numeros([1, 3, 5, 6, 4])
    19
    >>> soma_numeros([10, 10])
    20
    """
    soma = 0
    for numero in lista:
        soma += numero
    
    return soma
