"""
Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
"""

string1 = "AAACTBF"
string2 = "CBT"
string3 = "".join(set(string1) & set(string2))

print(string3)