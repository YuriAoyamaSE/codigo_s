
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
