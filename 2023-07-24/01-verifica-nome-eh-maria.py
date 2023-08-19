def verifica_nome(nome: str) -> bool:
    """
        Recebe o nome digitado pelo usuário e 
        retorna verdadeiro se o primeiro nome é Maria
        >>> verifica_nome('maria ')
        True
        >>> verifica_nome('Maria angela')
        True
        >>> verifica_nome('Flávia Alessandra')
        False
    """
    return nome.split()[0].lower() == "maria"

def le_nome():
    nome = input("Digite o nome da pessoa: ")
    if verifica_nome(nome):
        return print("O primeiro nome é Maria")

    print("O primeiro nome não é Maria")

le_nome()