from enum import Enum

class TiposDeVoto(Enum):
    primeiroCandidato = 1
    segundoCandidato = 2
    votoEmBranco = 3

def contar_votos(lista_de_votos: list, voto: TiposDeVoto) -> int:
    """
    Recebe o tipo do voto(candidato ou em branco), uma lista de votos e retorna a contagem de votos
    >>> contar_votos([1, 2, 3, 1], TiposDeVoto.primeiroCandidato.value)
    2
    >>> contar_votos([1, 2, 3, 1], TiposDeVoto.votoEmBranco.value)
    1
    >>> contar_votos([1, 2, 2, 1], TiposDeVoto.segundoCandidato.value)
    2
    """
    contador = 0
    for voto_do_eleitor in lista_de_votos:
        if voto_do_eleitor == voto:
            contador += 1
    return contador

def votos(lista_de_votos: list) -> str:
    """
    Recebe uma lista de votos e retorna o resultado.
    >>> votos([1, 3, 2, 3, 2, 3, 3, 3, 1])
    'Mais de 50% de votos em branco, uma nova eleição deve ser convocada!'
    >>> votos([])
    'A Lista não pode estar vazia.'
    >>> votos([1, 2, 1, 3])
    'O primeiro canditado venceu a eleição!'
    >>> votos([2, 2, 1, 3])
    'O segundo canditado venceu a eleição!'
    """
    if len(lista_de_votos) <= 0:
        return "A Lista não pode estar vazia."

    votos_primeiro_candidato: int = contar_votos(lista_de_votos, TiposDeVoto.primeiroCandidato.value)
    votos_segundo_candidato: int = contar_votos(lista_de_votos, TiposDeVoto.segundoCandidato.value)
    votos_em_branco: int = contar_votos(lista_de_votos, TiposDeVoto.votoEmBranco.value)

    votos_em_branco_eh_mais_da_metade = votos_em_branco > round(len(lista_de_votos) / 2)

    if votos_em_branco_eh_mais_da_metade:
        return "Mais de 50% de votos em branco, uma nova eleição deve ser convocada!"
    elif votos_primeiro_candidato > votos_segundo_candidato:
        return "O primeiro canditado venceu a eleição!"
    elif votos_primeiro_candidato < votos_segundo_candidato:
        return "O segundo canditado venceu a eleição!"
    else:
        return "A eleição resultou em empate!"