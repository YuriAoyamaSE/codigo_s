
dividendo = int(input("Digite o primeiro número: "))
divisor = int(input("Digite o segundo número: "))

if dividendo % divisor == 0:
    status = "é"
else:
    status = "não é"

print(f"O número {dividendo} {status} divisível por {divisor}.")
