"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!

A palavra secreta é representada por uma linha de traços em cada letra da pala@vra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

import forca

secret_word = forca.get_secret_word()
correct_letters = list("_" * len(secret_word))
missed_letters = []
attempts = 6

print("||||||||||||||||||||||||||||||||||")
print("|| Bem vindos ao jogo da Forca! ||")
print("||||||||||||||||||||||||||||||||||")
print()


while forca.game_continue(missed_letters, attempts, correct_letters):
    forca.print_game_board(correct_letters,missed_letters, attempts)
    user_letter = forca.read_input_player(missed_letters, correct_letters)
    forca.guess_letter(user_letter, secret_word, missed_letters, correct_letters)
    print()

forca.game_score(secret_word, correct_letters)

print("||||||||||||||||||||||||||||||||||")
print("||         FIM DE JOGO          ||")
print("||||||||||||||||||||||||||||||||||")

