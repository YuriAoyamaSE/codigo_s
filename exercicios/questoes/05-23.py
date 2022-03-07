"""
Escreva um programa que leia um número e verifique se é ou não um número primo.
Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
Se o resto de uma dessas divisões for igual a zero, o número não é primo.
Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
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
