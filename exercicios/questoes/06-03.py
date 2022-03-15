"""
Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""

def unir_elementos_unicos(lista_a: list, lista_b: list) -> list:
    output = set()
    for item in lista_a + lista_b:
        output.add(item)
    return output

lista01 = [1,2,3,4,"a","h"]
lista02 = [1,2,"a", "b", "c", 'd']

print(unir_elementos_unicos(lista01,lista02))
