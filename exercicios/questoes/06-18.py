"""
Escreva um programa que gere um dicionário, em que cada chave seja
um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida.
Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}
"""

frase = "O rato roeu a roupa do rei de Roma"
dicionario = dict()

for letra in frase:
    if letra != " ":
        if letra in dicionario.keys():
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1

print(dicionario)
