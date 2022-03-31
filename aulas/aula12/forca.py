from random import choice
from string import ascii_letters

def get_secret_word() -> str:
    """Devolve uma palavra aleatória de uma lista em maiúsculo."""
    words_list = list()
    with open("palavras.txt", "r") as document:
        for word in document:
            word = word.strip().upper()
            words_list.append(word)
    return choice(words_list)


def read_input_player(missed_letters:list, correct_letters:list) -> str:
    """Lê uma letra do usuário e retorna em maiúsculo."""
    while True:
        user_letter = input("Digite uma letra: ").strip().upper()
        if user_letter in (missed_letters + correct_letters):
            print("Letra repetida! Tente de novo.")        
        elif len(user_letter) > 1:
            print("Digite apenas uma letra! Tente de novo.")
        elif user_letter not in ascii_letters:
            print("Não é uma letra! Tente de novo.")
        else:
            return user_letter


def guess_letter(user_letter: str, secret_word: str, missed_letters: list, correct_letters: list):
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""
    print()    
    index = 0
    if user_letter in secret_word:
        for letter in secret_word:
            if user_letter == letter:
                correct_letters[index] = user_letter
            index += 1
        return True
    else:
        missed_letters.append(user_letter)
        return False


def game_continue(missed_letters: list, attempts: int, correct_letters: list) -> bool:
    """Função que decide se jogo já encerrou ou não."""
    if len(missed_letters) < attempts and "_" in correct_letters:
        return True
    return False


def draw_hangman(errors: int) -> None:
    """Desenha forca de acordo com os erros"""
    print(" _______")
    print(" |     |")
    if errors > 0:
        print(" |     O")
    else:
        print(" |")
    if errors > 3:
        print(" |    ´|`")
    elif errors > 2:
        print(" |    ´| ")
    elif errors > 1:
        print(" |     | ")
    else:
        print(" |")
    if errors > 4:
        print(" |    ´ ")
    else:
        print(" |     ")
    print("------------")


def print_game_board(correct_letters: list, missed_letters: list, attempts: int) -> None:
    """Imprime a situação atual do jogo."""
    errors = len(missed_letters)
    if errors > 0:
        print(f"Você errou {errors} vezes: {missed_letters}")
    print(f"Você possui {attempts - errors} tentativas!")
    draw_hangman(errors)
    print("Palavra secreta: " + " ".join(correct_letters))


def game_score(secret_word: str, correct_letters: list) -> None:
    print(f"A palavra secreta é: {secret_word}")
    if "_" not in correct_letters:
        print("     Parabéns!            ")
        print("Você escapou da forca!    ")
        print("                          ")
        print(" _______                  ")
        print(" |     |                  ")
        print(" |                        ")
        print(" |               O        ")
        print(" |              ´|`       ")
        print("------------    ´ `       ")
        print("                          ")
    else:
        print("Suas tentativas acabaram. Você foi enforcado!")
        print(" _______")
        print(" |     |")
        print(" |     O")
        print(" |    ´|`")
        print(" |    ´ `")
        print("------------")