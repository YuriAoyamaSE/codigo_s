
numero = input("Informe o número: ")

if numero == numero[::-1]:
    status = "é palíndromo"
else:
    status = "não é palíndromo"

print(f"O número {numero} {status}.")
