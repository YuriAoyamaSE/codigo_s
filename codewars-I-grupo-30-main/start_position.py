'''
Módulo que gera uma posição inicial dentro do mapa do labirinto.
'''

import re
from random import randrange


def user_start_position(maze_map: list) -> tuple:
    '''
    Recebe uma posição inicial do usuário, validando para que seja em formato válido, uma coordenada possível dentro do mapa do labirinto, e não seja parede

    Args:
        maze_map (list): Mapa do labirinto em formato de lista de listas

    Returns:
        (tuple): Tupla com as coordenadas da posição inicial determinada pelo usuário
    '''
    coordinate_pattern = re.compile("[0-9][,][0-1]?[0-9]")

    # Validando formato do input
    while True:
        start_position = input(
            "Digite a posição inicial. Linha (0-9) x Coluna (0-19) no formato l,c (Ex: 5,5): ").strip()
        if not coordinate_pattern.match(start_position):
            print("Entrada inválida. Tente de novo.")

        # Validação de espaço vazio, caso o formato inserido esteja ok
        else:
            coordinate = tuple(map(int, (start_position.split(","))))
            if maze_map[coordinate[0]][coordinate[1]] == " ":
                return coordinate
            else:
                print("Entrada inválida: local é uma parede. Tente de novo.")


def random_start_position(maze_map: list) -> tuple:
    '''
    Seleciona um ponto inicial válido dentro do mapa, que seja igual a '0' ou igual a ' '

    Args:
        maze_map (list): Mapa do labirinto em formato de lista de listas
        
    Returns:
        (tuple): Tupla com as coordenadas da posição inicial determinada aleatoriamente pela função
    '''

    while True:
        coordinate = (randrange(len(maze_map)), randrange(len(maze_map[0])))
        if maze_map[coordinate[0]][coordinate[1]] == " " or maze_map[coordinate[0]][coordinate[1]] == '0':
            return coordinate
        else:
            return random_start_position(maze_map)

