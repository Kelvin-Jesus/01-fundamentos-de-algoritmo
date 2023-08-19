def calcula_hipotenusa(cateto_adjacente, cateto_oposto: float) -> float:
    """
        Recebe os valores dos catetos e retorna a valor da hipotenusa
        >>> calcula_hipotenusa(10, 10)
        14.14
        >>> calcula_hipotenusa(3, 4)
        5.0
    """
    return round(((cateto_adjacente ** 2) + (cateto_oposto ** 2)) ** (1/2), 2)

def ler_catetos():
    cateto_adjacente: float = float(input("Digite o valor do cateto adjacente: "))
    cateto_oposto: float = float(input("Digite o valor do cateto oposto: "))

    hipotenusa = calcula_hipotenusa(cateto_adjacente, cateto_oposto)
    print(f"O valor da hipotenusa é: {hipotenusa}")

ler_catetos()