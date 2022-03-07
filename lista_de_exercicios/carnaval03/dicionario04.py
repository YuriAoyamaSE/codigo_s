
dicionario_de_cores = {1: "vermelho", 2: "azul", 3: "marrom"}

def tamanho_das_strings(dicionario):
    novo_dict = dicionario
    for item in dicionario:
        novo_dict[item] = len(dicionario[item])
    return novo_dict

print(tamanho_das_strings(dicionario_de_cores))
