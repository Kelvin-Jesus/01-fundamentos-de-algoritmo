def calculaIdadeEmDias(dias: int, meses: int, anos: int) -> int:
    """ Calcula a idade de uma pessoa em dias
        >>> calculaIdadeEmDias(25, 6, 15)
        5680
        >>> calculaIdadeEmDias(1, 0, 22)
        8031
    """
    return anos * 365 + meses * 30 + dias