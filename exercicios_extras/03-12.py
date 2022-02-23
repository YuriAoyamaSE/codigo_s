"""
Escreva um programa que calcule o tempo de uma viagem de carro. 
Pergunte a distância a percorrer e a velocidade média esperada 
para a viagem.
"""

distancia = float(input("Digite a distancia a ser percorrida (km): "))
velocidade = float(input("Digite a velocidade média esperada(km/h): "))

horas = distancia / velocidade
minutos = (horas - int(horas)) * 60
segundos = (minutos - int(minutos)) * 60

print(f"O tempo esperado da viagem é de {int(horas)}:{int(minutos)}:{int(segundos)}")
