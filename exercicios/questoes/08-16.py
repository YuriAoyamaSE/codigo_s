"""
Escreva um generator capaz de gerar a série dos números primos.

Resposta:
"""

def gerador_primos(n):
    primos = [2]

    for i in range(1,n):
        teste = primos[i-1] + 1
        while True:
            check = []
            for numero in primos:
                check.append(teste % numero)
                if teste % numero == 0:
                    teste += 1
                    continue
            if all(check):
                primos.append(teste)
                break
    
    return primos

print(gerador_primos(20))
