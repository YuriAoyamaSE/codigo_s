import json

with open(r'modulo_2\aula21\arquivos_json\caracteres.json') as file:
    dicionario = json.loads(file.read())


print(dicionario)

print(dicionario['en'])

class Veiculo():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

    def __str__(self) -> str:
        return self.marca

    def __repr__(self) -> str:
        pass

veiculo = Veiculo('fusca', 'wv')

print(veiculo)



