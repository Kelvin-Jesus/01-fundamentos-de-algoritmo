def cacaPalavraEmMatriz(matriz: list, palavra: str):
    """
    Função que recebe uma matriz de caracteres e uma palavra e 
    retorna uma lista de dicionários com as coordenadas de 
    cada ocorrência da palavra na matriz.
    >>> cacaPalavraEmMatriz([
    ...     ['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'],
    ...     ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'],
    ...     ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'],
    ...     ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'],
    ...     ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']
    ... ], "CASA") # doctest: +NORMALIZE_WHITESPACE
    [{'linhaInicio': 1, 'colunaInicio': 0, 'linhaFinal': 4, 'colunaFinal': 0}, 
    {'linhaInicio': 0, 'colunaInicio': 1, 'linhaFinal': 3, 'colunaFinal': 1}, 
    {'linhaInicio': 0, 'colunaInicio': 1, 'linhaFinal': 0, 'colunaFinal': 4}]
    """
    ocorrenciasVerticais = buscaVerticalmente(matriz, palavra)
    ocorrenciasHorizontais = buscaHorizontalmente(matriz, palavra)

    return ocorrenciasVerticais + ocorrenciasHorizontais   

def buscaVerticalmente(matriz, palavra):
    """
    Função que recebe uma matriz e uma palavra, a partir disso busca as ocorrências
    verticais dessa palavra na matriz.
    >>> buscaVerticalmente([
    ...     ['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'],
    ...     ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'],
    ...     ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'],
    ...     ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'],
    ...     ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']
    ... ], "CASA") # doctest: +NORMALIZE_WHITESPACE
    [{'linhaInicio': 1, 'colunaInicio': 0, 'linhaFinal': 4, 'colunaFinal': 0}, 
    {'linhaInicio': 0, 'colunaInicio': 1, 'linhaFinal': 3, 'colunaFinal': 1}]
    """
    quantidadeDeLinhas = len(matriz)
    quantidadeDeColunas = len(matriz[0])
    tamanhoPalavra = len(palavra)
    ocorrenciasDaPalavra = []

    for coluna in range(quantidadeDeColunas):
        for linha in range(quantidadeDeLinhas - tamanhoPalavra + 1):
            palavraNaLinha = []
            for i in range(tamanhoPalavra):
                palavraNaLinha.append(matriz[linha+i][coluna])

            if "".join(palavraNaLinha) == palavra:
                ocorrenciasDaPalavra.append({
                    "linhaInicio": linha, 
                    "colunaInicio": coluna, 
                    "linhaFinal": linha + tamanhoPalavra - 1,
                    "colunaFinal": coluna
                })

    return ocorrenciasDaPalavra
    
def buscaHorizontalmente(matriz, palavra):
    """
    Função que recebe uma matriz e uma palavra, a partir disso busca as ocorrências
    horizontais dessa palavra na matriz.
    >>> buscaHorizontalmente([
    ...     ['A', 'C', 'A', 'S', 'A', 'M', 'C', 'A', 'S', 'W', 'B'],
    ...     ['C', 'A', 'X', 'R', 'F', 'T', 'P', 'A', 'S', 'A', 'C'],
    ...     ['A', 'S', 'X', 'I', 'E', 'J', 'H', 'W', 'T', 'Q', 'A'],
    ...     ['S', 'A', 'E', 'O', 'W', 'M', 'Q', 'Z', 'O', 'D', 'B'],
    ...     ['A', 'C', 'Y', 'K', 'F', 'W', 'C', 'A', 'A', 'V', 'B']
    ... ], "CASA") # doctest: +NORMALIZE_WHITESPACE
    [{'linhaInicio': 0, 'colunaInicio': 1, 'linhaFinal': 0, 'colunaFinal': 4}]
    """
    quantidaDeLinhas = len(matriz)
    quantidadeDeColunas = len(matriz[0])
    tamanhoPalavra = len(palavra)
    ocorrenciasDaPalavra = []

    for linha in range(quantidaDeLinhas):
        for coluna in range(quantidadeDeColunas):
            string = "".join(matriz[linha][coluna:coluna+tamanhoPalavra])
            if string == palavra:
                ocorrenciasDaPalavra.append({
                    "linhaInicio": linha, 
                    "colunaInicio": coluna, 
                    "linhaFinal": linha,
                    "colunaFinal": coluna + tamanhoPalavra - 1
                })

    return ocorrenciasDaPalavra
