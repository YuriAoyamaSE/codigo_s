from math import sqrt

lado1 = float(input("Informe a medida do 1º lado do triângulo: "))
lado2 = float(input("Informe a medida do 2º lado do triângulo: "))
lado3 = float(input("Informe a medida do 3º lado do triângulo: "))

s = (lado1 + lado2 + lado3)/2

area = sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))

print(f"A área do triângulo é {area:.2f}")
