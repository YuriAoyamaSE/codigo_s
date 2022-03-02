"""
Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""

numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))
soma = 0

print(numero1, "x2", numero2, "=", end=" ")

for i in range(numero2):
    soma += numero1
    print(numero1,end="")
    if i == numero2 - 1:
        print(" = ", end="")
    elif i < numero2 - 1:
        print(" + ", end="")

for j in range(numero1):
    print(numero2,end="")
    if j == numero1 -1:
        print(" = ", end="")
    elif j < numero1 -1:
        print(" + ", end="")

print(soma)
