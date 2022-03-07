"""
Escreva um programa que calcule a raiz quadrada de um número.
Utilize o método de Newton para obter um resultado aproximado.
Sendo n o número a obter a raiz quadrada, considere a base b=2.
Calcule p usando a fórmula p=(b+(n/b))/2.
Agora, calcule o quadrado de p.
A cada passo, faça b=p e recalcule p usando a fórmula apresentada.
Pare quando a diferença absoluta entre n e o quadrado de p for menor que 0,0001.
"""

n = float(input("Digite o número: "))
b = 2
while True:
    p=(b+(n/b))/2
    b = p
    if abs(n - p**2) < 0.0001:
        break

print(f"A raiz quadrada de {n} é aproximadamente {p}")
