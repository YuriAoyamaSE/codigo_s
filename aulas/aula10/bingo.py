from collections import defaultdict
from random import randint, choice

def iniciar():
    global LETRAS, INTERVALO, bolas_restantes
    LETRAS = ("B", "I", "N", "G", "O") 
    INTERVALO = {"B":list(range(1,16)), "I":list(range(16,31)), "N":list(range(31,46)), "G":list(range(46,61)), "O":list(range(61,76))}
    bolas_restantes = INTERVALO

def gerar_cart() -> defaultdict:
    """Retorna uma cartela aleatória de bingo"""
    cartela = defaultdict(list) #vai iniciar como uma lista vazia, para não precisar iniciar cada letra como uma lista vazia

    for letra in LETRAS:
        intervalo_cartela = INTERVALO
        while len(cartela[letra]) < 5:
            num_aleatorio = choice(intervalo_cartela[letra])
            intervalo_cartela[letra].pop(intervalo_cartela[letra].index(num_aleatorio))
            cartela[letra].append(num_aleatorio)
            cartela[letra].sort()    
    return cartela

def imprimir_cart(cartela: dict[str, list[int]]):
    """Imprime a cartela formatada"""
    print("B   I   N   G   O")
    for i in range(5):
        linha = [str(elemento[i]).zfill(2) for elemento in cartela.values()]
        print("  ".join(linha))

def checar_cartela(bola_sorteada, cartela):
    letra = bola_sorteada[0]
    numero = int("".join(bola_sorteada[1:3]))
    if numero in cartela[letra]:
        indice = cartela[letra].index(numero)
        cartela[letra][indice] = "--"
    return cartela

def ganhou(cartela):
    for letra in cartela:
        if all([value == "--" for value in cartela[letra]]):
            return True
    for i in range(5):
        if all([cartela[letra][i] == "--" for letra in cartela]):
            return True
    return False
        
def sortear_bola() -> str:
    letra_sorteada = choice(list(bolas_restantes.keys()))
    num_sorteado = choice(bolas_restantes[letra_sorteada])
    INTERVALO[letra_sorteada].pop(INTERVALO[letra_sorteada].index(num_sorteado))
    if len(INTERVALO[letra_sorteada]) < 1:
        INTERVALO.pop(letra_sorteada)
    return letra_sorteada+str(num_sorteado)

def reiniciar():
    bolas_restantes = INTERVALO
    