from enum import Enum,auto 

class CorSemaforo(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()

def proxima_cor(cor: str) -> CorSemaforo:
    """
        Recebe a cor atual do semáforo e retorna qual será a próxima cor
    >>> proxima_cor('verde').name
    'AMARELO'
    >>> proxima_cor('amarelo').name
    'VERMELHO'
    >>> proxima_cor('vermelho').name
    'VERDE'
    """
    if cor.lower() == 'verde':
        proxima_cor_semaforo = CorSemaforo.AMARELO
    elif cor.lower() == 'vermelho':
        proxima_cor_semaforo = CorSemaforo.VERDE
    else:
        proxima_cor_semaforo = CorSemaforo.VERMELHO

    return proxima_cor_semaforo

def le_cor():
    cor: str = input("Escolha uma cor(Verde, Amarelo, Verde): ")
    proxima = proxima_cor(cor)
    print(f"A próxima cor do semáforo será: {proxima.name.lower()}")

# le_cor()