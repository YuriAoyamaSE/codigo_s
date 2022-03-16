def calcula_media(lst: list) -> float:
    return sum(lst) / len(lst)

def calcula_media_ponderada(valores: list, pesos: tuple or None = None) -> float:
    """ Calcula média ponderada quando as notas possuem pesos distintos"""
    if not pesos:
        pesos = (1,)*len(valores)
    
    numerador = 0
    divisor = sum(pesos)
    for valor, peso in zip(valores, pesos):
        numerador += valor*peso
    return numerador / divisor


