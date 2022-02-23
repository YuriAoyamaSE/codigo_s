"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""

qt_cigarros_diaria = int(input("Quantos cigarros fuma por dia? "))
qt_anos = int(input("Há quantos anos fuma? "))

minutos = 10 * qt_cigarros_diaria * 365 * qt_anos

dias = int(minutos/60/24)

print(f"Dias de vida perdidos por fumar: {dias}")
