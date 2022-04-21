"""
Escreva uma função que receba uma string e uma lista.
A função deve comparar a string passada com os elementos da lista, também passada como parâmetro.
Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

Resposta:
"""

def procura_na_lista(string,lista) ->bool:
    return string in lista

print(procura_na_lista("casa",["maçã","uva", "pera","casa"]))
print(procura_na_lista("casa",["maçã","uva", "pera","casas"]))