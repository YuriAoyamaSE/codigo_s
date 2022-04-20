"""
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.

O que são anagramas? https://pt.wikipedia.org/wiki/Anagrama
"""

def gera_substrings(palavra):
    palavra_em_lista = list(palavra)
    lista_de_substrings = []
    for final in range(1, len(palavra_em_lista)+1):
        for inicio in range(0, final):
            lista_de_substrings.append(palavra[inicio:final])
    return lista_de_substrings

def procure_anagramas(lista_de_strings):
    lista_de_anagramas = []    
    for posicao1 in range(0, len(lista_de_strings)-1):
        item1 = lista_de_strings[posicao1]
        lista1 = list(item1)
        lista1.sort()

        for posicao2 in range(posicao1+1, len(lista_de_strings)):
            item2 = lista_de_strings[posicao2]
            lista2 = list(item2)
            lista2.sort()
            
            if lista1 == lista2:
                lista_de_anagramas.append([item1, item2])

    return lista_de_anagramas

while True:    
    print("Procurar número de pares de substrings que são anagramas.")
    palavra = input("Digite a palavra desejada: ").strip()
    substrings = gera_substrings(palavra)
    anagramas = procure_anagramas(substrings)

    print("Palavra: ", palavra)
    print("Conjunto dos anagramas pares: ", anagramas)
    print("Total de pares que são anagramas: ", len(anagramas))
    print("\nDeseja fazer outro teste? (s/n) ")

    if input() != "s":
        break

print("\n----- Programa encerrado -----\n")
