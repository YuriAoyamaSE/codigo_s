"""
Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
"""

distancia = float(input("Digite distância da viagem (km): "))

if distancia <= 200:
    tarifa = 0.50
else:
    tarifa = 0.45

valor_passagem = distancia * tarifa

print(f"Valor da passagem: R$ {valor_passagem:.2f}")
