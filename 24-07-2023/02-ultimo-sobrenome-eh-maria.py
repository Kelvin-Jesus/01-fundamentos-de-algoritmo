def ultimo_sobrenome_eh_silva(nome: str) -> bool:
    """
        Recebe o nome digitado pelo usuário e 
        retorna verdadeiro se o primeiro nome é Maria
        >>> ultimo_sobrenome_eh_silva('maria Silva')
        True
        >>> ultimo_sobrenome_eh_silva('Maria angela')
        False
        >>> ultimo_sobrenome_eh_silva('Flávia Alessandra')
        False
    """
    return nome.split()[-1].lower() == "silva"

def le_nome():
    nome: str = input("Digite um nome: ")

    if ultimo_sobrenome_eh_silva(nome):
        return print("Último nome é \"silva\"")

    print("Último nome NÃO é \"silva\"")

le_nome()