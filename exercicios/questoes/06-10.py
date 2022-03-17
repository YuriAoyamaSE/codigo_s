"""
Modifique o programa do Exercício 6.9 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde p e a posição onde v foram encontrados.

Obs.: igual por ter já implementado a mais....
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
    