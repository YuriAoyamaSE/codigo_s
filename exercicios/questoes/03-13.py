"""
Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

     9 × C
 F = ----- + 32
       5
"""

temperatura_c = float(input("Digite a temperatura (°C):"))
temperatura_f = (9 * temperatura_c / 5) + 32

print(f"{temperatura_c}°C equivalem a {temperatura_f}°F")
