"""
Bootcamp código[s]
Data: 24/02/2022
aula 04 

tema: Condições (if, else, elfi ...)
"""

aluno = input("Digite o nome do aluno(a): ")
quantidade_de_notas = int( input("Quantas notas você gostaria de cadastrar? "))
nota = []
media_minima = 8
media_para_recuperacao = 7

for contador in range(0, quantidade_de_notas):
    nota.append(float(input(f"Digite a {contador+1}ª nota: ")))

media_do_aluno = sum(nota)/quantidade_de_notas

print(f"A média das notas de {aluno} é {round(media_do_aluno,2)}")

if media_do_aluno >= media_minima:
    status = "aprovado"
elif media_do_aluno >= media_para_recuperacao:
    status = "em recuperação"
else:
    status = "reprovado" 

print(f"{aluno.title()} está {status}")
