def maiorElementoDaDiagonalPrincipal(matriz: list) -> int: 
    """
    Recebe uma matriz e retorna o maior elemento da diagonal principal.
    >>> matriz: list = [
    ...     [ 1,  4,  7],
    ...     [10, 13, 16],
    ...     [19, 22, 25],
    ... ]
    >>> maiorElementoDaDiagonalPrincipal(matriz)
    25
    """
    quantidadeDeLinhas = len(matriz)
    quantidadeDeColunas = len(matriz[0])
    maiorElementoDiagonalPrincipal = matriz[0][0]

    for linha in range(0, quantidadeDeLinhas):
        for coluna in range(0, quantidadeDeColunas):
            if linha == coluna and matriz[linha][coluna] > maiorElementoDiagonalPrincipal:
                maiorElementoDiagonalPrincipal = matriz[linha][coluna]
                
    return maiorElementoDiagonalPrincipal

def divideMaiorElementoDaDiagonalPrincipal(matriz: list, maiorElementoDaDiagonal: int) -> list:
    """
    Recebe uma matriz e retorna uma matriz com os elementos da matriz original
    divididos pelo maior elemento da diagonal principal.
    >>> matriz: list = [
    ...     [ 1,  4,  7],
    ...     [10, 13, 16],
    ...     [19, 22, 25],
    ... ]
    >>> divideMaiorElementoDaDiagonalPrincipal(matriz, maiorElementoDaDiagonalPrincipal(matriz))
    [[0.04, 0.16, 0.28], [0.4, 0.52, 0.64], [0.76, 0.88, 1.0]]
    """
    novaMatriz = []

    for linha in matriz:
        novaLinha = []

        for valor in linha:
            novoValor = valor / maiorElementoDaDiagonal
            novaLinha.append(novoValor)

        novaMatriz.append(novaLinha)

    return novaMatriz