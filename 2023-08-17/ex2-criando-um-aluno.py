from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    ra: int
    curso: str

def cria_aluno(nome: str, ra: int, curso: str) -> Aluno:
    """ Recebe os dados de um aluno, cria e retorna uma
     estrutura de dados que represente um aluno
    >>> cria_aluno('Kelvin', 394587, 'Informática').nome
    'Kelvin'
    >>> cria_aluno('Kelvin', 394587, 'Informática').curso
    'Informática'
    >>> cria_aluno('Kelvin', 394587, 'Informática').ra
    394587
    """
    aluno = Aluno(nome, ra, curso)

    return aluno

def mostra_aluno_na_tela(aluno: Aluno):
    print(aluno)

def entrada():
    aluno_nome: str = input("Digite o nome do aluno: ")
    aluno_ra: int = int(input("Digite o ra do aluno: "))
    aluno_curso: str = input("Digite o curso do aluno: ")

    aluno = cria_aluno(aluno_nome, aluno_ra, aluno_curso)
    mostra_aluno_na_tela(aluno)

# entrada()
