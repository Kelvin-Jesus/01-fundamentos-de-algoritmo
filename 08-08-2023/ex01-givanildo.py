def checaSenha(senha: str) -> bool:
    """ Recebe a senha e verifica se ela é igual a senha definida pelo Givanildo
    >>> checaSenha("ei")
    False
    >>> checaSenha("Giva123")
    True
    """
    senhaDoGivanildo = "Giva123"
    return senha == senhaDoGivanildo

def senha():
    senhaDigitada = input("Digite a senha:")
    senhaEstaCorreta = checaSenha(senhaDigitada)

    if ( senhaEstaCorreta == False ):
        print("Senha está incorreta! Acesso negado!")
    else:
        print("Senha está correta! Acesso autorizado!")

senha()
