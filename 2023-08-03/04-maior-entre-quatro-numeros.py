def maximo(numero1, numero2, numero3: int) -> int:
    """ Recebe três valores como argumento e retorna o maior entre os três
        >>> maximo(1, 2, 3)
        3
        >>> maximo(10, 4, 2)
        10
    """
    if ( numero1 >= numero2 and numero1 >= numero3 ):
        maior: int = numero1
    elif ( numero2 >= numero3 ):
        maior = numero2
    else:
        maior = numero3 

    return maior