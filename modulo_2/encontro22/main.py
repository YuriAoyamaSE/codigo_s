"""
How Bootcamps - Stone - /código[s]
Data: 05/05/2022
Autor: Maicon Franscico de Carvalho
Tema: JSON (JavaScript Object Notation)

JSON servepara padronizar, de uma forma simples e leve. Há outras formas mais eficientes, mas não tão difundidas como o JSON.

Usar um padrão facilita para a comunicação entre sistemas que usam diferentes linguagens. Pega um padrão de anotação (json) e, sabendo que a anotação está nesse padrão, é possível transformar em um objeto na linguagem do sistema. Esta metodologia se chama serialização.

No caso do python, a anotação json se transforma em um dicionário (dict) e para converter de python para json, é preciso estar na forma de dicionário também.
"""

import json

# Pegando um objeto json (maicon) e transformando em objeto de python (um dict)
maicon_json = '{"nome": "maicon", "idade": 35,"cidade": "curitiba"}'
maicon_python = json.loads(maicon_json)
print(type(maicon_json), maicon_json)
print(type(maicon_python),maicon_python)
print("\n")


# invertendo: transformando objeto python em json
class Pessoa():
    def __init__(self, nome, idade, cidade) -> None:
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

henrique_python = Pessoa('henrique', 35, 'rio de janeiro')
# é preciso usar o tipo dict para a serialização. Assim, usaremos o .__dict__, que irá transformar os atributos da classe em keys, valores em value.
henrique_json = json.dumps(henrique_python.__dict__)
print(type(henrique_python.__dict__), henrique_python.__dict__)
print(type(henrique_json),henrique_json)

# gerando o arquivo json
with open(r'modulo_2\aula21\arquivos_json\henrique.json', 'a+') as arquivo:
    arquivo.writelines(henrique_json)

with open(r'modulo_2\aula21\arquivos_json\henrique.json', 'r') as arquivo:
    arquivo.read()
