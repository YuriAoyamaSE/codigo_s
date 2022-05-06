import csv

""" 
# note abaixo a formatação em lista para escrever no CSV
with open(r'modulo_2\aula21\arquivos_csv\pessoas.csv', 'w', newline='\n') as csvfile:
    arquivo_csv = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    arquivo_csv.writerow(['Spam']*5+['Baked Beans'])
    arquivo_csv.writerow(['teste01','teste02','teste03']) 
"""


class Pessoa():
    def __init__(self, nome, idade, cidade) -> None:
        self.nome = nome
        self.idade = idade
        self.cidade = cidade


pessoa1 = Pessoa('henrique', 35, 'rio de janeiro')
pessoa2 = Pessoa('joão', 18, 'boavista')
pessoa3 = Pessoa('paula', 22, 'bh')
pessoa4 = Pessoa('ash', 42, 'palet')
pessoa5 = Pessoa('pikachu', 52, 'mato')

pessoas = [pessoa1,pessoa2,pessoa3,pessoa4,pessoa5]

cabecalho = ['nome','idade','cidade']

# escrevendo o arquivo csv
with open(r'modulo_2\aula21\arquivos_csv\pessoas.csv', 'w', newline='\n', encoding='utf8') as csvfile:
    arquivo_csv = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    arquivo_csv.writerow(cabecalho)
    for pessoa in pessoas:
        arquivo_csv.writerow([pessoa.nome,pessoa.idade,pessoa.cidade])


# lendo o csv
"""
with open(r'modulo_2\aula21\arquivos_csv\pessoas.csv', 'r', encoding='utf8') as csvfile:
    arquivo_python = csv.reader(csvfile,delimiter=';')
    #1ª forma de imprimir:
    #print(list(arquivo_python))
    #2ª forma de imprimir:
    #for linha in arquivo_python:
    #    print(linha)

    for index, linha in enumerate(arquivo_python):
        if index == 0:      #pular o cabeçalho
            continue
        nome, idade, cidade = linha[0], linha[1], linha[2]
        print(f'A pessoa {nome} possui {idade} anos e mora na cidade de {cidade}') 
    """
with open(r'modulo_2\aula21\arquivos_csv\pessoas.csv', 'r', encoding='utf8') as csvfile:
    arquivo_python = csv.DictReader(csvfile,delimiter=';')
    for index, linha in enumerate(arquivo_python):
        if index == 0:
            continue        
        print(f'A pessoa {linha["nome"]} possui {linha["idade"]} anos e mora na cidade de {linha["cidade"]}')
