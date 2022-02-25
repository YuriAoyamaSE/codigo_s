"""
Modifique o o jogo da forca (Programa 7.2) de forma a escrever a palavra secreta caso o jogador perca.

sem acesso ao programa

gabarito:
"""

palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        # O r antes da string indica que seu conteúdo não deve ser processado
        # Desta forma, podemos usar os caracteres de \ e / sem confundi-los
        # com máscaras como \n e \t
        linha2 = r"  |   "
    elif erros == 3:
        linha2 = r" \|   "
    elif erros >= 4:
        linha2 = r" \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += r" /     "
    elif erros >= 6:
        linha3 += r" / \ "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
    