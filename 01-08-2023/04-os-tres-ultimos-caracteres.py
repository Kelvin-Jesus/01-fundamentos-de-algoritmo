def tresUltimos(texto: str) -> str:
    """ Retorna apenas os três ũltimos caracteres da string recebida como argumento
        >>> tresUltimos('Kelvin')
        'vin'
        >>> tresUltimos('Gabriella')
        'lla'
    """
    return texto[-3:len(texto)]