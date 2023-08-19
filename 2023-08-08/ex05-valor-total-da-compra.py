def calcular_valor(quantidade_de_laranjas: int) -> float:
    """
        Deve retornar o valor total das laranjas compradas baseado a quantidade.
        >>> calcular_valor(12)
        3.6
        >>> calcular_valor(10)
        3.5
    """
    if (quantidade_de_laranjas < 12):
        valor_da_laranja = 0.35
    else:
        valor_da_laranja = 0.3

    valor_total = round(quantidade_de_laranjas * valor_da_laranja, 2)

    return valor_total

def comprar_laranjas():
    quantidade_de_laranjas: int = int(input("Digite a quantidade de laranjas que deseja comprar: "))

    valor_total = calcular_valor(quantidade_de_laranjas)

    return print(f"O valor total das laranjas é: {valor_total:.2f}")

comprar_laranjas()