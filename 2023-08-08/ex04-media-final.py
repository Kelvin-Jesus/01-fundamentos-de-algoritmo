def media_final(nota: float) -> str:
    """ 
        Recebe a média final de um aluno e retorna o conceito da média.
        >>> media_final(0.0)
        'D'
        >>> media_final(6.0)
        'C'
        >>> media_final(7.4)
        'B'
        >>> media_final(9.7)
        'A'
    """

    if (nota >= 0.0 and nota <= 4.9):
        return 'D'
    elif (nota >= 5.0 and nota <= 6.9):
        return 'C'
    elif (nota >= 7.0 and nota <= 8.9):
        return 'B'
    else:
        return 'A'
    
def media():
    media_do_aluno: float = float(input("Digite a média final: "))

    print("O conceito da média final é: " + media_final(media_do_aluno))

media()