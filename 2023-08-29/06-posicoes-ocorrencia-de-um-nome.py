def posicoesOcorrenciasListaDeNomes(lista: list, nome: str) -> list:
    """ Recebe uma lista de nomes e um nome e retorna um dicionário
    com as posições em que o nome aparece na lista.
    >>> posicoesOcorrenciasListaDeNomes(['Ana', 'Bia', 'Ana', 'Ana', 'Bia'], 'Ana')
    [0, 2, 3]
    >>> posicoesOcorrenciasListaDeNomes(['Ana', 'Bia', 'Ana', 'Ana', 'Bia'], 'Bia')
    [1, 4]
    >>> posicoesOcorrenciasListaDeNomes(['Ana', 'Bia', 'Ana', 'Ana', 'Bia'], 'Maria')
    []
    """
    posicoes = []
    quantidadeDeNomes = len(lista)
    
    for indice in range(quantidadeDeNomes):
        if lista[indice] == nome:
            posicoes.append(indice)

    return posicoes