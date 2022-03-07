
alunos_e_notas = {"Theodoro": 20, "Márcia": 50, "Júnior": 80}
nota_max = max(alunos_e_notas.values())
nota_min = min(alunos_e_notas.values())

for key in alunos_e_notas:
    if alunos_e_notas[key] == nota_max:
        print(f"Nota máxima - > {key} : {nota_max}")
    if alunos_e_notas[key] == nota_min:
        print(f"Nota mínima - > {key}: {nota_min}")
