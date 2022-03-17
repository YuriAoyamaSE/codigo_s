"""
Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.
"""

L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar:"))
v = int(input("Digite o segundo valor a procurar:"))
posicao_p = None
posicao_v = None

for x in range(len(L)):
    if L[x] == p:
        posicao_p = x
    elif L[x] == v:
        posicao_v = x

if posicao_p != None:
    print(f"{p} achado na posição {posicao_p}")
else:
    print(f"{p} não encontrado")
if posicao_v != None:
    print(f"{v} achado na posição {posicao_v}")
    if posicao_p != None:
        if posicao_p < posicao_v:
            primeiro = p
        elif posicao_p > posicao_v:
            primeiro = v
        else:
            primeiro = "ambos"
        print(f"Encontrado primeiro: {primeiro}")
else:
    print(f"{v} não encontrado")
