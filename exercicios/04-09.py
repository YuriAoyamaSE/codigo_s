"""
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""

valor_casa = float(input(f"Informe o valor da casa: R$ "))
salario = float(input(f"Informe seu salário: R$ "))
prazo = int(input(f"Informe em quanto anos planeja a quitação: "))

prestacao = valor_casa/(prazo*12)

print(f"\nO pagamento é de {prazo*12} prestações de R$ {prestacao:.2f}.\n")

if prestacao < salario*0.3:
    print("Seu emprétimo bancário foi aprovado!")
else:
    print("Infelizmente, seu emprétimo bancário não foi aprovado.")
