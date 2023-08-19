def calcula_imposto(salario: float) -> float:
    """
        Calcular o valor do imposto de renda a partir do salário
        de um funcionário e considerando a faixa salarial.
        >>> calcula_imposto(500)
        0
        >>> calcula_imposto(1200)
        120.0
        >>> calcula_imposto(2500)
        500.0
    """
    if salario < 1000:
        imposto = 0
    elif salario < 2000:
        imposto = salario * 0.10
    else:
        imposto = salario * 0.20
    return imposto