"""
Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes.

Sem acesso. Gabarito:
"""

def valida_entrada(mensagem, opções_válidas):
    opções = opções_válidas.lower()
    while True:
        escolha = input(mensagem)
        if escolha.lower() in opções:
            break
        print("Erro: opção inválida. Redigite.\n")
    return escolha

# Exemplo:print(valida_entrada("Escolha uma opção:", "abcde"))
#
# Questão extra: o que acontece se o usuário digitar mais de uma opção?
# Por exemplo, ab.

"""versão 2:
import random

n = random.randint(1, 10)
tentativas = 0
while tentativas < 3:
    x = int(input("Escolha um número entre 1 e 10: "))
    if (x == n):
        print("Você acertou!")
        break
    else:
        print("Você errou.")
    tentativas += 1
"""

"""versão 3:
def valida_opções(validas):
    validas = validas.lower()
    while True:
        opção = input("Digite uma opção:").lower()
        if opção in validas:
            return opção
        print("Opção inválida, por favor escolha novamente.")
"""