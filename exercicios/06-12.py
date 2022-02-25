"""
Altere o Programa 6.11 de forma a imprimir o menor elemento da lista.

Sem acesso ao programa
Gabarito:
"""

L = [4, 2, 1, 7]
mínimo = L[0]
for e in L:
    if e < mínimo:
        mínimo = e
print(mínimo)
