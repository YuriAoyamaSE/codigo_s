'''
Bootcamp Python /código[s]
Stone e How Bootcamps
Code Wars I
Projeto do Labirinto
Nome do Projeto: "The Almost One Line Solution"
Equipe: Igor Gabryell Mendes Melo
        Pedro Henrique Prestes Conceição
        Thainara Lessa Furforo
        Vítor Mateus de Brito
        Yuri Aoyama da Costa
'''

import os
from mapper import *
from maze_generator import *
from move import *
from start_position import *


def main():
    '''
    Função principal do desafio do labirinto.
    Nela o jogador deverá escolher um nível para jogar, sendo as opções: 3 ou 4.
    Caso opte pelo nível 3, o jogo irá rodar com o mapa padrão armazenado no arquivo 'map.txt', e o usuário deverá 
    escolher a posição inicial no labirinto para o robô começar a andar.
    Caso opte pelo nível 4, o usuário deverá escolher a altura e a largura do labirinto a ser gerado automaticamente, 
    e posteriormente poderá selecionar se quer escolher a posição inicial no labirinto para o robô começar a andar, 
    ou se prefere que seja gerada uma posição inicial aleatória no mapa.
    '''
    os.system('cls')
    print('*'*49 + '\nBEM VINDO AO JOGO: "THE ALMOST ONE LINE SOLUTION"\n' +
          '*'*49, end='\n\n')
    level = input('Digite o nível desejado para jogar (3 ou 4): ')

    while level != '3' and level != '4':
        level = input(
            '\nEntrada inválida! Digite o nível desejado para jogar (3 ou 4): ')

    if level == '3':
        maze = read_map_file('map.txt')
        print_map(maze)
        current_position = user_start_position(maze)
        find_exit(current_position, maze)

    elif level == '4':
        height = int(input('Digite o número de linhas para o labirinto: '))
        width = int(input('Digite o número de colunas para o labirinto: '))
        maze = generate_maze(height, width)
        print_map(maze)
        position = input(
            'Como o jogo deve começar?\nDigite 1 para selecionar a coordenada inicial no labirinto\nDigite 2 para que o computador selecione uma posição inicial aleatória\nDigite sua opção: ')
        while position != '1' and position != '2':
            position = input('\nOpção inválida!\nComo o jogo deve começar?\nDigite 1 para selecionar a coordenada inicial no labirinto\nDigite 2 para que o computador selecione uma posição inicial aleatória\nDigite sua opção: ')
        if position == '1':
            current_position = user_start_position(maze)
        else:
            current_position = random_start_position(maze)
        find_exit(current_position, maze)


if (__name__ == '__main__'):
    main()

