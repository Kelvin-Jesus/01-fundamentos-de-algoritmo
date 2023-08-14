def tipo_de_triangulo(x, y, z: float) -> str:
    """ Recebe os 3 lados de um triangulo e retorna o seu tipo
        >>> tipo_de_triangulo(10, 10, 10)
        'Equilátero'
        >>> tipo_de_triangulo(10, 18, 10)
        'Isóceles'
        >>> tipo_de_triangulo(15, 20, 30)
        'Escaleno'
    """
    if (x == y and x == z):
        tipo_triangulo = "Equilátero"
    elif (x == y or x == z):
        tipo_triangulo = "Isóceles"
    else:
        tipo_triangulo = "Escaleno"

    return tipo_triangulo

def triangulo_eh_valido(x, y, z: float) -> bool:
    """ Recebe os 3 lados de um triangulo e se é um triângulo válido
        >>> triangulo_eh_valido(3, 4, 5)
        True
        >>> triangulo_eh_valido(10, 10, 10)
        True
        >>> triangulo_eh_valido(10, 2, 2)
        False
    """
    if (x < (y + z) and y < (x + z) and z < (x + y)):
        return True
    else:
        return False
    
def triangulo():
    primeiro_lado: float = float(input("Digite o valor do primeiro lado: "))
    segundo_lado: float = float(input("Digite o valor do segundo lado: "))
    terceiro_lado: float = float(input("Digite o valor do segundo lado: "))

    triangulo_valido = triangulo_eh_valido(primeiro_lado, segundo_lado, terceiro_lado)
    if (triangulo_valido == False):
        return print("Não é possível formar um triângulo com o valor informado!")
    
    qual_tipo_do_triangulo = tipo_de_triangulo(primeiro_lado, segundo_lado, terceiro_lado)
    return print("O triângulo é do tipo: " + qual_tipo_do_triangulo)

triangulo()