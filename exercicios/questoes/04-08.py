"""
Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
"""

numero1 = float(input(f"Digite o 1º número: "))
numero2 = float(input(f"Digite o 2º número: "))
operacao = input("Escolha a operação: \nsoma (+) \nsubtração (-) \nmultiplicação (*) \ndivisão (/) \n")

def calcule(n1,n2,op):
    if op == "+":
       return n1 + n2
    elif operacao == "-":
       return n1 - n2
    elif operacao == "*":
       return n1 * n2
    elif operacao == "/":
       return n1 / n2
    else:
        return "Operação inválida"

print(f"Resultado: {calcule(numero1,numero2,operacao)}")
