"""
Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as operações de soma e subtração para calcular o resultado.
"""

dividendo = int(input("Informe o valor do dividendo: "))
divisor = int(input("Informe o valor do divisor: "))
quociente = 0
resto = dividendo

while resto >= divisor:
    resto -= divisor
    quociente += 1

print(f"A divisão de {dividendo} por {divisor} resulta no quociente {quociente} e resto {resto}")
