"""
Exercício de desafio: calcular distânciaentre dois pontos no formato (t1,g1) e (t2,g2), que são as latitudes e longitudes dos dois pontos.
A distância entre dois pontos pode ser encontrada pela fórmula (em km):

distancia = 6371,01 x arccos(sen(t1) x sen(t2) + cos(t2) x cos(g1-g2))

6371,01 é o raio médio da terra em quilometros.

caueira: -11.15269397886806, -37.19865085061151
al: -9.67927571350236, -35.86276944824701
google: 221km
"""

from math import radians, acos, cos, sin

print('Digite as coordenadas na formatação "latitude, longitude" em graus.')
t1, g1 = map(radians, map(float, (input("Coordenadas do ponto 1: ").split(","))))
t2, g2 = map(radians, map(float, (input("Coordenadas do ponto 2: ").split(","))))

distancia = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))

print(f"Distância entre os dois pontos (km): {round(distancia,2)}")

"""
resolução 01:

from math import radians, acos, cos, sin

t1 = radians(float(input("Insira a latitude do ponto 1 (graus): ")))
g1 = radians(float(input("Insira a longitude do ponto 1 (graus): ")))
t2 = radians(float(input("Insira a latitude do ponto 2 (graus): ")))
g2 = radians(float(input("Insira a longitude do ponto 2 (graus): ")))

distancia = 6371.01 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))

print(f"Distância entre os dois pontos (km): {round(distancia,2)}")
"""