"""
Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5, 6) == 6
máximo(2, 1) == 2
máximo(7, 7) == 7

Resposta:
"""

def bigger_number(*number):
    return max(number)

print(bigger_number(1,2,3,4,5))
print(bigger_number(1,2,3))