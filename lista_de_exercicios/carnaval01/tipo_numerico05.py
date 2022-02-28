
numero_str ="1234" ### input("Informe um número de 4 dígitos: ")
soma = 0

for digito in numero_str:
    soma += int(digito)

print(f"{numero_str[0]} + {numero_str[1]} + {numero_str[2]} + {numero_str[3]} = {soma}")
