"""
Escreva um programa que leia três números e que imprima o maior e o menor.
"""

numeros = []
for item in range(1,4):
    numeros.append(int(input(f"Digite o {item}º número: ")))

print(f"Maior número: {max(numeros)}")
print(f"Menor número: {min(numeros)}")
