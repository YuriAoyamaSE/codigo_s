from math import log10

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))

soma = a + b
print(f"A soma de A e B dá: {soma}")

diferenca = b - a
print(f"A diferença quando se subtrai B de A dá: {diferenca}")

multiplicacao = a * b
print(f"O produto (multiplicação) entre A e B dá: {multiplicacao}")

quociente = a // b
print(f"O quociente (parte inteira da divisão) quando se divide A por B dá: {quociente}")

resto = a % b
print(f"O resto da divisão entre A e B dá: {resto}")

logaritmo = log10(a)
print(f"O resultado de log10 de A dá: {logaritmo}")

exponecial = a ** b
print(f"O resultado de A elevado a B dá: {exponecial}")
