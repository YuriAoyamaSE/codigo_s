'''
Módulo que importa o mapa de um arquivo txt e o imprime na tela
'''

import os
from time import sleep


def print_map(maze: list) -> None:
    '''
    Imprime o mapa na tela, com uma suspensão de 0.3 segundos para iniciar
    Args:
        maze (list): modelo do labirinto em formato de lista
    Returns: None
    '''

    sleep(0.3)  # Esperar por 0.3 segundos
    os.system('cls')  # Limpa a tela antes de executar o restante do código

    for line in maze:
        line_str = ''
        for char in line:
            line_str += char
        print(line_str)

    return None


def read_map_file(path: str) -> list:
    """
    Lê o arquivo encontrado no caminho e gera o labirinto
    Args:
        path (string): caminho onde o arquivo .txt do labirinto está
    Returns: (list) labirinto como uma lista
    """

    with open(path, 'r') as file:
        maze = [[char for char in line] for line in file]
    for line in maze:
        if len(line) <= 20:
            break
        else:
            line.pop()

    return maze

