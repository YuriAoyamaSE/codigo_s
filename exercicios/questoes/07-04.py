"""
Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x
"""

string = 'TTAAC'

for letra in set(string):
    print(f"{letra}: {string.count(letra)}x")
