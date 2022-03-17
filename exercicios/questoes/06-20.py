"""
Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
• os elementos que não mudaram
• os novos elementos
• os elementos que foram removidos
"""

original = {1,3,4,6,9,11,20}
modificado = {1,3,5,7,9,11,13}

print(f"Lista original: {original}")
print(f"Lista modificada: {modificado}")
print(f"Elementos mantidos: {original & modificado}")
print(f"Elementos novos: {modificado - original}")
print(f"Elementos removidos: {original - modificado}")
