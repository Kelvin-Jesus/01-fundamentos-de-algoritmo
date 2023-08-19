from enum import Enum,auto

class ClassificacaoDoNome(Enum):
    LONGO = auto()
    MEDIANO = auto()
    CURTO = auto()

def classifica_nome(nome: str) -> str:
    """
    Recebe um nome como string e retorna se o nome é 
    'curto', 'longo' ou 'mediano' baseado na quantidade de caracteres
    >>> classifica_nome('Kelvin').name
    'MEDIANO'
    >>> classifica_nome('Alexandre').name
    'LONGO'
    >>> classifica_nome('Ana').name
    'CURTO'
    """
    tamanho_do_nome = len(nome.strip())
    if tamanho_do_nome <= 4:
        classificacao_do_nome = ClassificacaoDoNome.CURTO
    elif tamanho_do_nome <= 8 and tamanho_do_nome > 4:
        classificacao_do_nome = ClassificacaoDoNome.MEDIANO
    else:
        classificacao_do_nome = ClassificacaoDoNome.LONGO
    
    return classificacao_do_nome

def le_nome():
    nome: str = input("Digite um nome a ser classificado: ")
    classificacao = classifica_nome(nome)

    print(f"O nome {nome} é classificado como: {classificacao.name}")

le_nome()