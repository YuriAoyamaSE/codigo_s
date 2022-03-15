"""
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor (lista) de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

"""

def mostra_quadrado_magico():
    vetor = list(range(1,10))
    matriz = {}

    for _ in range(3):
        matriz[linha01] = [1,2,3]

    for key in matriz:
        print(matriz[key]) 
