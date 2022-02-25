"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

salario = float(input("Digite salário do funcionário: "))

if salario > 1250:
    aumento = salario * .10
else:
    aumento = salario * .15

print(f"Aumento de R$ {aumento:.2f} \nSalário total: R$ {salario+aumento:.2f}")
