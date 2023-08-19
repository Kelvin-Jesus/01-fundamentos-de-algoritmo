def ultimo_nome_eh_silva(nome: str):
    """
        Recebe o nome digitado pelo usuário e 
        retorna verdadeiro se o primeiro nome é Maria
        >>> ultimo_nome_eh_silva('maria Silva')
        True
        >>> ultimo_nome_eh_silva('Maria angela')
        False
        >>> ultimo_nome_eh_silva('Anderson silva')
        True
    """
    return nome[-5:len(nome)].lower() == "silva"

def ler_nome():
    nome: str = input("Digite o nome: ")

    if ultimo_nome_eh_silva(nome):
        return print("Último nome é \"Silva\"")

    print("Último nome NÃO é \"Silva\"")

ler_nome()