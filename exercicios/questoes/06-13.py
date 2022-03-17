"""
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
"""

T = [ -10, -8, 0, 1, 2, 5, -2, -4]

print(f"Menor temperatura: {min(T)}°C")
print(f"Maior temperatura: {max(T)}°C")
print(f"Temperatura média: {sum(T) / len(T)}°C")
