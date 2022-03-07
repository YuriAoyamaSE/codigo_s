numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    status = "par"
else:
    status = "impar"

print(f"O número {numero} é {status}.")
