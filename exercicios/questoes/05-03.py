"""
Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.
"""

from time import sleep

for segundo in range(10,-1,-1):
    print(segundo)
    sleep(1)

print("Fogo!")
