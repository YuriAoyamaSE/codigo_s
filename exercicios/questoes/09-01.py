"""Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo."""

















"""Gabarito:

import sys

# Verifica se o parâmetro foi passado
if len(sys.argv) != 2:  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-01.py nome_do_arquivo\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
    arquivo.close()

# Não esqueça de ler sobre encodings
# Dependendo do tipo de arquivo e de seu sistema operacional,
# ele pode não imprimir corretamente na tela.
"""