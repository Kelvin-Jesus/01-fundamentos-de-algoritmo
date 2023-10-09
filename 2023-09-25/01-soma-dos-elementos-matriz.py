def somaDosElementosDaMatriz(matriz: list) -> int: 
    """
    Recebe uma matriz e retorna a soma de todos os 
    seus elementos.
    >>> matrizDeUmaPA: list = [
    ...     [1, 4, 7],
    ...     [10, 13, 16],
    ...     [19, 22, 25],
    ...     [28, 31, 34],
    ... ]
    >>> matrizFibonacci: list = [
    ...     [0, 1, 1],
    ...     [2, 3, 5],
    ...     [8, 13, 21],
    ...     [34, 55, 89],
    ... ]
    >>> somaDosElementosDaMatriz(matrizDeUmaPA)
    210
    >>> somaDosElementosDaMatriz(matrizFibonacci)
    232
    """
    quantidadeDeLinhas = len(matriz)
    quantidadeDeColunas = len(matriz[0])
    somaDosElementos = 0

    for linha in range(0, quantidadeDeLinhas):
        for coluna in range(0, quantidadeDeColunas):
            somaDosElementos += matriz[linha][coluna]
    
    return somaDosElementos