
lista_str = ["1", "7", "99", "15"]
lista_inteiros = [1,2,3,45,67,8,9,10]

def converte_para_int(lista):
    return list(map(int, lista))

def converte_para_str(lista):
    return list(map(str,lista))

print(lista_str)
print(converte_para_int(lista_str))

print(lista_inteiros)
print(converte_para_str(lista_inteiros))
