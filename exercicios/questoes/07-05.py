"""
Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados da primeira.
1ª string: AATTGGAA
2ª string: TG
3ª string: AAAA
"""

string1= 'AATTGGAA'
string2= 'TG'
string3 = []

for letra in string1:
    if letra != string2[0] and letra != string2[1]:
        string3.append(letra)

string3 = "".join(string3)

print(string3)