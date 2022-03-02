"""
Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
"""

numero1 = int(input("Informe o primeiro numero: "))
numero2 = int(input("Informe o segundo numero: "))
resto = numero1
quociente = 0

print(f"{numero1} % {numero2} => ", end="")

while resto >= numero2:
    resto -= numero2
    quociente += 1
    print(numero2,end="")
    if resto >= numero2:
        print(" | ", end="")
    else: 
        print(" | ", resto)

print(f"Quociente = {quociente}")
print(f"Resto = {resto}")
