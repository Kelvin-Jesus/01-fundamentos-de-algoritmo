def modulo(numero: int) -> int:
    """
        Recebe um número inteiro e retorna seu módulo.
        >>> modulo(10)
        10
        >>> modulo(-4)
        4
    """
    if numero < 0:
        numero = numero * (-1)

    return numero

def entrada():
    numero = int(input("Digite o número:")) 
    moduloDeNumero = modulo(numero)
    print("O Módulo é", moduloDeNumero)

entrada()