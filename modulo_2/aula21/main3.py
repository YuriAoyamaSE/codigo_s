

maicon_json = ''

# with open() possui valor padrão 'rt', que é read e text
with open(r'modulo_2\aula21\arquivos_json\maicon.json') as file: 
    maicon_json = file.read()

print(maicon_json)

