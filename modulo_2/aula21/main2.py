"""
já vimos com tipos primitivos, mas se ouver objeto dentro de objeto?
por exemplo, um atributo que é do tipo de outra classe criada

quando converter para json, haverá uma hierarquia diferente

"""

import json

class Veiculo():
    def __init__(self, marca, modelo) -> None:
        self.marca = marca
        self.modelo = modelo

class Pessoa():
    def __init__(self, nome, idade, cidade, veiculo: Veiculo) -> None:
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.veiculo = veiculo

chevete = Veiculo('GM','chevet')
maicon = Pessoa('maicon', 33, 'curitiba',chevete.__dict__)
maicon_json = json.dumps(maicon.__dict__)

with open(r'modulo_2\aula21\arquivos_json\maicon.json', 'a+') as arquivo:
    arquivo.writelines(maicon_json)
