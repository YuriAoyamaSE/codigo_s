"""
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
"""

numeros = []

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero != 0:
        numeros.append(numero)
    else:
        break

print("Quantidade de números digitados:", len(numeros))
print("Soma: ", sum(numeros))
print(f"Média: {sum(numeros)/len(numeros):10.2f}")
