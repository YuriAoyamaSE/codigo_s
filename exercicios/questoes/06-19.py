"""
Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• os valores comuns às duas listas
• os valores que só existem na primeira
• os valores que existem apenas na segunda
• uma lista com os elementos não repetidos das duas listas.
• a primeira lista sem os elementos repetidos na segunda
"""

lista01 = {1,3,4,6,9,11,20}
lista02 = {1,3,5,7,9,11,13}

print(f"Lista 01: {lista01}")
print(f"Lista 02: {lista02}")
print(f"Valores comuns às duas listas: {lista01 & lista02}")
print(f"Valores que só existem na lista 01: {lista01 - lista02}")
print(f"Valores que só existem na lista 02: {lista02 - lista01}")
print(f"Elementos não repetidos das duas listas: {lista01 ^ lista02}")
print(f"Lista 01 sem elementos da Lista 02: {lista01 - lista02}")
