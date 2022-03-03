"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
"""

deposito_inicial = float(input("Informe o valor do depósito inicial (R$): "))
tx_juros = float(input("Informe a taxa de juros (%): "))
montante = deposito_inicial

for mes in range(1,25):
    montante *= 1+(tx_juros/100)
    print(f"{mes}° mês - montante: R$ {round(montante,2):.2f}")

print(f"Total ganho com juros: R$ {round(montante - deposito_inicial,2):.2f}")
