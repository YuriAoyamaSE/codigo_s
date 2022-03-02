"""
Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
"""

from time import sleep

numero_final = int(input("Digite o numero final da contagem: "))

for segundo in range(1,numero_final + 1, 2):
    print(segundo)
    sleep(0.5)

print("Fim!")
