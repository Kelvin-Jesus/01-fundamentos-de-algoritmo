def maximo(numero1: int, numero2: int) -> int:
    """
        Recebe dois números inteiros e retorna 
        o maior entre eles.
        >>> maximo(10, 20)
        20
        >>> maximo(4, 2)
        4
    """
    if numero1 > numero2:
        maior:int = numero1
    else:
        maior:int = numero2
    
    return maior

def ler_maximo():
    n1 = int(input("Digite o primeiro número:"))
    n2 = int(input("Digite o segundo número:"))
    maior = maximo(n1, n2)
    print(f"O maior número é {maior}")

ler_maximo()
