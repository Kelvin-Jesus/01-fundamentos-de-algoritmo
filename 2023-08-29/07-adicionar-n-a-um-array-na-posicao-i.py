def adicionaNaPosicaoI(lista: list, numeroAhInserir: int, indiceAhInserir: int) -> list:
    """ Recebe uma lista, um número e um índice e retorna a lista com o número
    inserido na posição indicada pelo índice.
    >>> adicionaNaPosicaoI([1, 2, 3, 4], 10, 2)
    [1, 2, 10, 3, 4]
    >>> adicionaNaPosicaoI([1, 2, 3, 4], 10, 0)
    [10, 1, 2, 3, 4]
    >>> adicionaNaPosicaoI([1, 2, 3, 4], 10, 4)
    [1, 2, 3, 4, 10]
    """
    novoArray = []
    tamanhoDaLista = len(lista) - 1
    tamanhoDaLista = indiceAhInserir if indiceAhInserir > tamanhoDaLista else tamanhoDaLista

    for indiceAtual in range(tamanhoDaLista+1):
        if indiceAtual == indiceAhInserir:
            novoArray.append(numeroAhInserir)
            if indiceAtual > tamanhoDaLista - 1:
                continue

        novoArray.append(lista[indiceAtual])
    
    return novoArray
