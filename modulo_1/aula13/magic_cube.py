"""
How Bootcamps - Stone - /código[s]
Autor: Henrique Junqueira Branco

Enunciado:
Quadrado mágico: Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 4, com números de 1 a 16:
01  05  09  16
06  07  02  10
08  03  04  11
12  15  14  13
Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. 
Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. 
Usar um vetor (lista) de 1 a 16 parece ser mais simples que usar uma matriz 4x4.

Extra: Permita que o usuário indique o tamanho do cubo mágico (2x2, 3x3, 4x4, etc.)
"""

from itertools import permutations
from string import digits

def get_cube_size() -> int:
    while True:
        n = input("Digite o tamanho do cubo mágico (1 = 1x1; 2 = 2x2; 3 = 3x3 ...): ").strip()
        if n.isnumeric() and n != "0":
            return int(n)
        else:
            print(f"{n} não é uma entrada válida.\nO tamanho escolhido deve ser inteiro e positivo.\n1, 2, 3, 4 ...")


# Primeira versão: até 3x3. Problema de memória na geração das permutações(list_permutation)
def cube_generator(cube_size: int) -> list[tuple]:
    if cube_size == 1:
        return [(1)]
    list_permutation = list(permutations(range(1, cube_size**2 + 1)))
    magic_cube_list = []

    for roll in list_permutation: 
        diagonal_1 = [roll[i] for i in range(0, cube_size**2, cube_size + 1)]
        diagonal_2 = [roll[i] for i in range(cube_size-1, cube_size**2 -1, cube_size - 1)]
        parameter = sum(diagonal_1)

        if parameter != sum(diagonal_2):
            continue
        
        for counter in range(cube_size):
            globals()[f"line_{counter}"] = roll[cube_size * counter : cube_size * (counter + 1)]
            globals()[f"column_{counter}"] = [roll[i] for i in range(counter, cube_size**2, cube_size)]
            if parameter != sum(globals()[f"line_{counter}"]):
                break
            elif parameter != sum(globals()[f"column_{counter}"]):
                break          
            elif counter == cube_size - 1:
                magic_cube_list.append(roll)

    return magic_cube_list


def print_cube(cube_size: int, magic_cube_list: list[tuple]) -> None:
    if cube_size == 1:
        print("1")
        return None

    for roll in magic_cube_list:
        for i in range(cube_size):
            line = roll[cube_size * i : cube_size * (i + 1)]
            num_size = len(str(len(line))) + 1
            line = [str(line[i]).zfill(num_size) for i in range(len(line))]
            print("  ".join(line))
        print()
    return None


cube_size = get_cube_size()
magic_cube_list = cube_generator(cube_size)
print_cube(cube_size, magic_cube_list)
print(f"Total de cubos mágicos {cube_size}x{cube_size}: {len(magic_cube_list)}")
