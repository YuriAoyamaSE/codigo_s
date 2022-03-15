"""
Em uma determinada país, as tarifas de táxi consistem em uma tarifa básica de R$4,00 mais R$0,25 para cada 140 metros percorridos. Escreva uma função que receba a distância percorrida (em quilômetros) como único parâmetro e retorna a tarifa total como único resultado. Escreva um programa que demonstre o uso da sua função.
"""

def calcula_tarifa_total (distancia_percorrida: float) -> float:
    tarifa_base = 4.00
    custo_do_segmento = 0.25
    km_do_segmento = 140/1000

    tarifa_total = tarifa_base + (distancia_percorrida / km_do_segmento) * custo_do_segmento

    return tarifa_total


distancia = float(input("Informe a distancia a ser percorrida pelo taxi (km): "))
print(f"Valor da tarifa total por corrida de {distancia:.2f}km: R$ {calcula_tarifa_total(distancia):.2f}")
