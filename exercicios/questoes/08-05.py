"""
Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7.

Sem acesso. Gabarito:
"""
def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None


L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
