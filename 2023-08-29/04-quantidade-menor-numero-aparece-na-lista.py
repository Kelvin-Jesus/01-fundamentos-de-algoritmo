def quantidadeDeVezesMenorNumeroApareceNaLista(lista: list) -> int:
    """ Recebe uma lista de números inteiros e retorna a quantidade 
    de vezes que o menor número aparece na lista.
    >>> quantidadeDeVezesMenorNumeroApareceNaLista([1, 2, 3, 4])
    1
    >>> quantidadeDeVezesMenorNumeroApareceNaLista([1, 20, 3, 1, 12])
    2
    >>> quantidadeDeVezesMenorNumeroApareceNaLista([1, 1, 1, 1])
    4
    >>> quantidadeDeVezesMenorNumeroApareceNaLista([2, 2, 2, 2, 6, 6, 3, 2])
    5
    """
    menorNumero = lista[0]
    quantidadeDeVezesMenorNumero = 0

    for numero in lista:
        if numero < menorNumero:
            menorNumero = numero
            quantidadeDeVezesMenorNumero = 0
        
        if numero == menorNumero:
            quantidadeDeVezesMenorNumero += 1
    
    return quantidadeDeVezesMenorNumero
        