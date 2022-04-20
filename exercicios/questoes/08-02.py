"""
Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
Valores esperados:
múltiplo(8, 4) == True
múltiplo(7, 3) == False
múltiplo(5, 5) == True

Resposta:
"""

def testar_multiplo(a,b):
    return a % b == 0

print(testar_multiplo(4,2))
print(testar_multiplo(5,2))
print(testar_multiplo(75,5))
