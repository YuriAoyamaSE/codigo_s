"""
Faça um programa que calcule o aumento de um salário. Ele deve 
solicitar o valor do salário e a porcentagem do aumento. Exiba 
o valor do aumento e do novo salário.
"""

salario = float(input("Digite seu salário: "))
aumento = float(input("digite seu aumento (em %): "))

novo_salario = salario*(100+aumento)/100

print(f"Novo salário é de R$ {novo_salario:7.2f}")
