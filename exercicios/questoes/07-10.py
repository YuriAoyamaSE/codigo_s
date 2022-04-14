"""
Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores.
A cada jogada, verifique se a posição está livre.
Verifique também quando um jogador venceu a partida.
Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual cada elemento é outra lista, também com três elementos.

Exemplo do jogo:

X | O |
---+---+---
  | X | X
---+---+---
  |   | O
Em que cada posição pode ser vista como um número. Confira a seguir um exemplo das posições mapeadas para a mesma posição de seu teclado numérico.

7 | 8 | 9
---+---+---
4 | 5 | 6
---+---+---
1 | 2 | 3
"""



def imprimir_tabuleiro(grid:list[int]) ->None:
    tabuleiro = (f"""
         {grid[7]} | {grid[8]} | {grid[9]}
        ---+---+---
         {grid[4]} | {grid[5]} | {grid[6]}
        ---+---+---
         {grid[1]} | {grid[2]} | {grid[3]}
        """)
    print(tabuleiro)


def iniciar_jogo() -> list:
    print("Escolha a posição conforme o esquema abaixo: ")
    grid = list(range(10))
    imprimir_tabuleiro(grid)
    print("Jogador 1: X")
    print("Jogador 2: O")
    grid = grid = [" "]*10
    input("Aperte Enter para iniciar")
    return grid


def jogada(grid:list,rodada:int) -> list:
    if rodada%2 == 0:
        print("Vez do Jogador 1")
        marca = "X"
    else:
        print("Vez do Jogador 2")
        marca = "O"

    while True:
        posicao = int(input("Escolha a posição: "))
        if grid[posicao] != " ":
          print("Posição inválida. Tente de novo.")
        else:
          grid[posicao] = marca
          return grid

def vitoria(grid):
    vencedor = False
    combinacoes = ([1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7])
    for bloco in combinacoes:
        if grid[bloco[0]] == grid[bloco[1]] and grid[bloco[0]] == grid[bloco[2]] and grid[bloco[0]] != " ":
            vencedor = grid[bloco[0]]
            break
    return vencedor

tabuleiro = iniciar_jogo()
rodada = 0

while rodada < 9:
    imprimir_tabuleiro(tabuleiro)
    tabuleiro = jogada(tabuleiro,rodada)
    vencedor = vitoria(tabuleiro)
    if vencedor:
        break
    rodada += 1

imprimir_tabuleiro(tabuleiro)
if vencedor == "X":
    print("Vitória do Jogador 1!")
elif vencedor == "O":
    print("Vitória do Jogador 2!")
else:
    print("Empate!")
    
    
    