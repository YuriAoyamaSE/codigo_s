"""
Faça um programa que solicite o preço de uma mercadoria e o percentual
de desconto. Exiba o valor do desconto e o preço a pagar.
"""

preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o desconto (%): "))

valor_do_desconto = preco*desconto/100
preco_a_pagar = preco - valor_do_desconto

print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Valor a pagar: R$ {preco_a_pagar:.2f}")
