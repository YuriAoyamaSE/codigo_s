'''
Módulo que gera um labirinto de forma automática e aleatória.
'''

from random import choice, randint, shuffle
from start_position import random_start_position


def maze_exit(maze: list) -> tuple:
    """Determina uma coordenada aleatória de saída do labirinto, dentre as quatro paredes exteriores (laterais, em cima e embaixo)

    Args:
        maze (list):  Mapa do labirinto em formato de lista de listas

    Returns:
        tuple: Tupla com as coordenadas da saída do labirinto
    """

    while 1:
        possible_exits = []

        for line in range(1, len(maze) - 1):
            possible_exits.append((line, 0))
            possible_exits.append((line, -1))

        for column in range(1, len(maze[0]) - 1):
            possible_exits.append((0, column))
            possible_exits.append((-1, column))

        exit_position = possible_exits[randint(0, len(possible_exits) - 1)]

        if exit_position[0] == 0:
            if (maze[1][exit_position[1]]) == ' ':
                break
        elif exit_position[0] == -1:
            if (maze[len(maze) - 2][exit_position[1]]) == ' ':
                break
        elif exit_position[1] == 0:
            if (maze[exit_position[0]][1]) == ' ':
                break
        elif exit_position[1] == -1:
            if (maze[exit_position[0]][len(maze[0]) - 2]) == ' ':
                break

    maze[exit_position[0]][exit_position[1]] = 'S'
    return maze


def verify_surrounds(current_position: tuple, maze: list) -> list:
    """Verifica se as quatro posições no entorno da posição atual do "wall_construct" no mapa do labirinto são possíveis destinações, condicionando a válidas as destinações equivalentes a "0" ou "1" no mapa

    Args:
        current_position (tuple): Posição atual no labirinto
        maze (list): Mapa do labirinto em formato de lista de listas

    Returns:
        list: Lista as tuplas das coordenadas de todos os possíveis destinos, que sejam equivalentes no mapa a "0" ou "1"
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
        if character == "0" or character == "1":
            possible_destinations.append(position)

    return possible_destinations


def maze_grid(maze_size: list) -> list:
    """Gera o mapa do escopo inicial do labirinto, com base no tamanho determinado (altura x largura)

    Args:
        maze_size (list): Lista composta por altura, largura do labirinto a ser criado

    Returns:
        list: Mapa do escopo inicial do labirinto em formato de lista de listas
    """
    maze = []
    for linha in range(maze_size[0]):
        if linha == 0 or linha == maze_size[0]-1:
            maze.append(list("#" * maze_size[1]))
            continue
        linha_interna = "#"+"0"*(maze_size[1]-2)+"#"
        maze.append(list(linha_interna))
    return maze


def wall_construct(maze, position) -> list:
    """Desenha caminhos, paredes e possíveis novos caminhos no labirinto, substituindo os "0" por " ", "#" e "1", na posição selecionada e seus arredores

    Args:
        maze (_type_): Mapa do labirinto em formato de lista de listas
        position (_type_): Posição no qual serão construídos os caminhos, paredes e possíveis novos caminhos

    Returns:
        list: Mapa do labirinto em formato de lista de listas
    """

    maze[position[0]][position[1]] = " "
    destinations = verify_surrounds(position, maze)
    if len(destinations) != 0:
        shuffle(destinations)
        position = destinations.pop()
        for destination in destinations:
            maze[destination[0]][destination[1]] = choice(
                ["#", "#", "#", "#", "#", "1", "1"])
        wall_construct(maze, position)
    return maze


def search_str(string: str, maze: list):
    """Procura se há uma determinada string em alguma posição do labirinto, linha a linha

    Args:
        string (str): String que está sendo procurada no labirinto
        maze (list): Mapa do labirinto em formato de lista de listas

    Returns:
        None: Se não for encontrada a String em nenhum local do labirinto
        list: Se a string for encontrada no labirinto, retorna uma lista com as coordenadas
    """
    for line in maze:
        for element in maze[maze.index(line)]:
            if element == string:
                return [maze.index(line), maze[maze.index(line)].index(element)]
    return None


def generate_maze(height: int, width: int) -> list:
    """Gera um labirinto automática e aleatoriamente, com a altura e largura determinados

    Args:
        height (int): Altura do labirinto a ser gerado
        width (int): Largura do labirinto a ser gerado

    Returns:
        list: Mapa do labirinto em formato de lista de listas, versão final, com todos os caminhos sendo percorríveis até a saída
    """

    while True:
        maze = maze_grid([height, width])
        posicao_inicial = random_start_position(maze)
        wall_construct(maze, posicao_inicial)

        while True:
            position = search_str("1", maze)
            if position:
                wall_construct(maze, position)
            else:
                while search_str("0", maze):
                    position = search_str("0", maze)

                    maze[position[0]][position[1]] = "#"
                break

        # Garante que a proporção de caminhos (strings de espaço: " ") em comparação ao total de espaços ocupados pelo labirinto (itens da lista de listas do labirinto) esteja dentro de um limite pré-determinado (nesse caso, 0.33)
        maze_line = []
        for linha in maze:
            maze_line.extend(linha)
        paredes = maze_line.count("#")
        caminhos = maze_line.count(" ")
        total = paredes + caminhos
        if caminhos < (total*0.33):
            continue
        else:
            break

    maze = maze_exit(maze)

    return maze

