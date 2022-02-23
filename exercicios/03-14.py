"""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

distancia_percorrida = float(input("Digite a distância Percorrida (km): "))
dias_alugados = int(input("Informe quantos dias de aluguel foram contratados: "))

diaria = 60
custo_km = 0.15

preco_a_pagar = distancia_percorrida * custo_km + dias_alugados * diaria

print(f"Preço a pagar: R$ {preco_a_pagar:.2f}")
