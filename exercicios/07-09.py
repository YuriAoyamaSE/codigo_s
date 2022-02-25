"""
Modifique o Programa 7.2 para utilizar listas de strings para desenhar o boneco da forca.
Você pode utilizar uma lista para cada linha e organizá-las em uma lista de listas.
Em vez de controlar quando imprimir cada parte, desenhe nessas listas, substituindo o elemento a desenhar.

Exemplo:

>>> linha = list("X------")
>>> linha
['X', '-', '-', '-', '-', '-', '-']
>>> linha[6] = "|"
>>> linha
['X', '-', '-', '-', '-', '-', '|']
>>> "".join(linha)
'X-----|'
"""