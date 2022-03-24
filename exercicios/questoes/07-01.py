"""
Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""

string1 = "AABBEFAATT"
string2 = "BE"

print(f"{string2} encontrado na posição {string1.find(string2)} de {string1}")
