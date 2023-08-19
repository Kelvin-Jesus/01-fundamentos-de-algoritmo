def idadeMaisVelha(idade1, idade2, idade3, idade4 :int) -> int:
    """ Recebe a idade de 4 pessoas e retorna a idade da mais velha
        >>> idadeMaisVelha(10, 20, 30, 10)
        30
        >>> idadeMaisVelha(15, 34, 22, 86)
        86
        >>> idadeMaisVelha(15, 94, 22, 86)
        94
    """
    if (idade1 >= idade2 and idade1 >= idade3 and idade1 >= idade4):
        maisVelha = idade1
    elif (idade2 >= idade3 and idade2 >= idade4):
        maisVelha = idade2
    elif (idade3 >= idade4):
        maisVelha = idade3
    else:
        maisVelha = idade4

    return maisVelha

def mediaIdadeDasPessoas(idade1, idade2, idade3, idade4 :int) -> float:
    """ Recebe a idade de 4 pessoas e retorna a média de idade
        >>> mediaIdadeDasPessoas(10, 20, 30, 10)
        17.5
        >>> mediaIdadeDasPessoas(15, 34, 22, 86)
        39.25
    """
    mediaDeIdade = (idade1 + idade2 + idade3 + idade4) / 4

    return mediaDeIdade

def idade():
    idade1 = int(input("Digite a idade da primeira pessoa: "))
    idade2 = int(input("Digite a idade da segunda pessoa: "))
    idade3 = int(input("Digite a idade da terceira pessoa: "))
    idade4 = int(input("Digite a idade da quarta pessoa: "))

    mediaIdade = mediaIdadeDasPessoas(idade1, idade2, idade3, idade4)
    idadePessoaMaisVelha = idadeMaisVelha(idade1, idade2, idade3, idade4)

    print("A média de idade das quatro pessoas é: ", mediaIdade)
    print("A idade da pessoa mais velha é: ", idadePessoaMaisVelha)

idade()