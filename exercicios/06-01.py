"""
Modifique o Programa 6.2 para ler 7 notas em vez de 5.

Sem acesso ao programa.

Gabarito:
"""

notas = [0, 0, 0, 0, 0, 0, 0]  # Ou [0] * 7
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota {x}:"))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma/x:5.2f}")
