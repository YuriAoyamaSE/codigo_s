"""
Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª string: AATTCGAA
2ª string: TG
3ª string: AC
Resultado: AAAACCAA
"""

string1 = 'AATTCGAA'
string2 = 'TG'
string3 = 'AC'
resultado = []

for letra in string1:    
    if letra in string2:        
        resultado.append(string3[string2.index(letra)])
        continue
    resultado.append(letra)

resultado = "".join(resultado)
print(resultado)