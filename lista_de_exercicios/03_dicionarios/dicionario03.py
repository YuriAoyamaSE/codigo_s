
materias = {"matemática": 81, "física": 83, "química": 87}
print(materias.get("matemática"))
def ordena_por_valor(dicionario):
    nova_ordem = {}
    for item in sorted(dicionario, key = dicionario.get, reverse=True):
        nova_ordem[item] = dicionario[item]
    return nova_ordem

print(ordena_por_valor(materias))
