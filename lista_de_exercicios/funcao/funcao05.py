"""
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:
8  3  4 
1  5  9
6  7  2
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor (lista) de 1 a 9 parece ser mais simples que usar uma matriz 3x3.

"""

from itertools import permutations

def quadrado_magico():
    vetor = list(range(1,10))

    for vetor in list(permutations(vetor)):
        parametro = sum(vetor[:3]) #linha1
        condicoes = (
            parametro == sum(vetor[3:6]) #linha2
            and parametro == sum(vetor[6:]) #linha3
            and parametro == sum([vetor[0], vetor[3], vetor[6]]) #coluna1
            and parametro == sum([vetor[1], vetor[4], vetor[7]]) #coluna2
            and parametro == sum([vetor[2], vetor[5], vetor[8]]) #coluna3
            and parametro == sum([vetor[0], vetor[4], vetor[8]]) #diagonal1
            and parametro == sum([vetor[2], vetor[4], vetor[6]]) #diagonal2
        )
        if condicoes:        
            print(f"{vetor[0]}  {vetor[1]}  {vetor[2]}")
            print(f"{vetor[3]}  {vetor[4]}  {vetor[5]}")
            print(f"{vetor[6]}  {vetor[7]}  {vetor[8]}")
            print()


quadrado_magico()