"""
Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
A ordem dos caracteres da terceira string não é importante.
"""

string1= 'CTA'
string2= 'ABC'
string3 = "".join(set(string1) ^ set(string2))

print(string3)