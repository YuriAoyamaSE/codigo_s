"""
Bootcamp código[s]
Data: 08/03/2022
aula 05

tema: Estrutura de repetição - usando while
"""

fechamento = dict()

while True:
    nome_do_aluno = input("Informe o nome do aluno: ").title()
    numero_de_notas = int( input(f"Quantas notas de {nome_do_aluno} pretende cadastrar? "))
    fechamento[nome_do_aluno] =[]

    for i in range(numero_de_notas):
        nota = float(input(f"Informe a {i +1}ª nota de {nome_do_aluno}: "))
        fechamento[nome_do_aluno].append(nota)
    
    if input("Deseja cadastrar outro aluno? (s/n)? ").lower() != "s":
        break

for aluno, notas in fechamento.items():
    media = round(sum(notas)/len(notas),1)
    print(f"A média do aluno(a) {aluno} é {media}")
