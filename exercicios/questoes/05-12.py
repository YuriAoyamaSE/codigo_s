"""
Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.
"""

deposito_inicial = float(input("Informe o valor do depósito inicial (R$): "))
deposito_mensal = float(input("Informe o valor do depósito mensal (R$): "))
tx_juros = float(input("Informe a taxa de juros (%): "))
montante = deposito_inicial

for mes in range(1,25):
    montante *= 1+(tx_juros/100)
    montante += deposito_mensal
    print(f"{mes}° mês - montante: R$ {round(montante,2):.2f}")
    
print(f"Total ganho com juros: R$ {round(montante - deposito_inicial - 24*deposito_mensal,2):.2f}")
