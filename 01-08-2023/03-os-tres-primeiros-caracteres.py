def tresPrimeiros(texto: str) -> str:
    """ Retorna apenas os três primeiros caracteres da string recebida como argumento.
        >>> tresPrimeiros('Kelvin')
        'Kel'
        >>> tresPrimeiros('Gabriella')
        'Gab'
    """
    return texto[0:3]