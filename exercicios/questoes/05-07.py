"""
Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
"""
inicio = int(input("Defina o início da tabuada: "))
fim = int(input("Defina o fim da tabuada: "))
for multiplicador in range(inicio,fim+1):
    print(f"3x{multiplicador} = {multiplicador * 3}")
