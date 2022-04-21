
alunos = {
    "João Alves dos Santos": ["inglês","francês"], 
    "Maria Magalhães": ["inglês","francês"], 
    "Antônio da Silva Ferreira": ["inglês","francês"],
    "José Júnior Jarbas": ["inglês"],
    "Henrique da Silva Sauro": ["inglês","francês"],
    "Joaquina Ferreira da Silva": ["inglês","francês"],
    "Fabiana Aparecida Bianco": ["inglês"],
    "Marrone Gutierres": ["inglês","francês"],
    "Carlos Magno Farad": ["inglês"],
    "Antônio da Silva Júnior Amaral": ["inglês","francês"],
    "Fernanda Abdala Mohamed": ["francês"],
    "Abner Mignon Alib": ["francês"],
    "Alisson Figueiredo": ["francês"]
    }

apenas_ingles = []
apenas_frances = []
ambos_cursos = []
apenas_um_curso = []

for aluno in alunos:
    if ("inglês" in alunos[aluno]) and ("francês" not in alunos[aluno]):
        apenas_ingles.append(aluno)
    
    if ("inglês" not in alunos[aluno]) and ("francês" in alunos[aluno]):
        apenas_frances.append(aluno)

    if ("inglês" in alunos[aluno]) and ("francês" in alunos[aluno]):
        ambos_cursos.append(aluno)
    
apenas_um_curso = apenas_frances + apenas_ingles

print(f"Total de {len(alunos)} alunos matriculados na escola: ")
print(f"Há {len(apenas_ingles)} alunos matriculados apenas em inglês: ")
for aluno in apenas_ingles: print(" - ", aluno)
print(f"Há {len(apenas_frances)} alunos matriculados apenas em francês: ")
for aluno in apenas_frances: print(" - ", aluno)
print(f"Há {len(ambos_cursos)} alunos matriculados em ambos os cursos: ")
for aluno in ambos_cursos: print(" - ", aluno)
print(f"Há {len(apenas_um_curso)} alunos matriculados em apenas um curso (inglês ou francês, mas não em ambos): ")
for aluno in apenas_um_curso: print(" - ", aluno)


"""
# Resolução do facilitador:

alunos_ingles = {
    "João Alves dos Santos",
    "Maria Magalhães",
    "Antônio da Silva Ferreira",
    "José Júnior Jarbas",
    "Henrique da Silva Sauro",
    "Joaquina Ferreira da Silva",
    "Fabiana Aparecida Bianco",
    "Marrone Gutierres",
    "Carlos Magno Farad",
    "Antônio da Silva Júnior Amaral",
}

alunos_frances = {
    "João Alves dos Santos",
    "Antônio da Silva Ferreira",
    "Fernanda Abdala Mohamed",
    "Abner Mignon Alib",
    "Alisson Figueiredo",
    "Henrique da Silva Sauro",
    "Maria Magalhães",
    "Marrone Gutierres",
    "Joaquina Ferreira da Silva",
}

print(f"Resp 1) - {len(alunos_ingles.union(alunos_frances))}", end="\n\n")

print(f"Resp 2) - {len(alunos_ingles - alunos_frances)}. Os alunos são: {alunos_ingles - alunos_frances}", end="\n\n")

print(f"Resp 3) - {len(alunos_frances - alunos_ingles)}. Os alunos são: {alunos_frances - alunos_ingles}", end="\n\n")

print(
    f"Resp 4) - {len(alunos_ingles.intersection(alunos_frances))}. Os alunos são: {alunos_ingles.intersection(alunos_frances)}",
    end="\n\n",
)

print(f"Resp 5) - {len(alunos_ingles.symmetric_difference(alunos_frances))}")

"""