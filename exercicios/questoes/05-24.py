"""
Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.
"""

numero = int(input("Digite um número: "))
numero_abs = abs(numero)
primo = True

if numero_abs in [0,1]:
    primo = False
else:
    for i in range (2,numero_abs):
        if numero_abs % i == 0:
            primo = False
    
if primo:
    print(f"O numero {numero} é primo.")
else:
    print(f"O numero {numero} não é primo.")
