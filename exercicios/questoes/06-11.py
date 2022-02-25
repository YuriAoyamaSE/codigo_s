"""
Modifique o Programa 6.6 usando for. Explique por que nem todos os while podem ser transformados em for.

Sem acesso ao programa
Gabarito:
"""

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
for e in L:
    print(e)
# O primeiro while não pôde ser convertido em for porque
# o número de repetições é desconhecido no início.
