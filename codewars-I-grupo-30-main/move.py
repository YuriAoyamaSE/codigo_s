'''
Módulo que gera a movimentação do robô apenas pelos espaços válidos, de forma aleatória, impedindo a repetição de caminhos,
exceto nos casos em que ele estiver encurralado (nesse caso, necessariamente retornando pelos últimos passos até que encontre 
um ponto no qual haja um espaço válido).
'''

from random import choice
from mapper import print_map


def find_exit(current_position: tuple, maze: list) -> None:
    """
    Faz o robô tentar achar a saída do labirinto

    Args:
        possible_destinations: verifica os possíveis próximos passos do robô
        current_position (tuple): retorna a posição atual do robô
        maze (list): modelo do labirinto em formato de lista

    Returns: None
    """
    moves_stack = [current_position]

    while True:

        possible_destinations = verify_surrounds(current_position, maze)

        if possible_destinations and possible_destinations[0] == 'Win':
            move(current_position, possible_destinations[1], maze)
            print("Vitória!")
            break

        elif possible_destinations:
            destination = choice(possible_destinations)
            move(current_position, destination, maze)
            moves_stack.append(destination)
            current_position = destination

        else:
            moves_stack.pop()
            last_position = moves_stack[-1]
            move(current_position, last_position, maze)
            current_position = last_position


def move(current_position: tuple, destination: tuple, maze: list) -> list:
    """
    Movimenta o robô pelo labirinto.

    Args: 
        current_position (tuple): indica a posição atual do robô, posição inicial
        destination (tuple): indica a próxima posição, posição final
        maze (list): modelo do labirinto em formato de lista
        
    Returns: (list) labirinto atualizado como uma lista
    """
    maze[current_position[0]][current_position[1]] = '.'
    maze[destination[0]][destination[1]] = 'X'

    print_map(maze)

    return maze


def verify_surrounds(current_position: tuple, maze: list) -> list:
    """
    Verifica os possíveis próximos passos do robô
    Args:
        current_position (tuple): tupla com as coordenadas da posição atual do robô, no formato (l,c), sendo l = linha e c = coluna
        maze (list): modelo do labirinto em formato de lista
    Returns:
        Se algum dos possíveis próximos passos do robô for a saída ('S'):
            (list) lista contendo o string 'Win', para identificar que o robô alcançou a saída, e a coordenada da posição da saída no formato [l,c], sendo l = linha e c = coluna
        Caso contrário: 
            (list) lista das coordenadas dos quatro possíveis destinos do robô (norte, sul, leste e oeste) no formato [l,c], sendo l = linha e c = coluna
    """
    north = (current_position[0] - 1, current_position[1])
    south = (current_position[0] + 1, current_position[1])
    east = (current_position[0], current_position[1] + 1)
    west = (current_position[0], current_position[1] - 1)

    positions = {
        north: maze[north[0]][north[1]],
        south: maze[south[0]][south[1]],
        east: maze[east[0]][east[1]],
        west: maze[west[0]][west[1]]
    }

    possible_destinations = []

    for position, character in positions.items():
        # Se o robô encontrar a Saída, ela será o único possível destino
        if character == 'S':
            return ['Win', position]
        elif character == ' ':
            possible_destinations.append(position)

    return possible_destinations

