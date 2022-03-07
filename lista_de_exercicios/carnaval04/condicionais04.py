
ano = int(input("Informe o ano: "))

if ano % 400 == 0:
    status = "é bissexto"
elif ano % 100 == 0:
    status = "não é bissexto"
elif ano % 4 == 0:
    status = "é bissexto"
else:
    status = "não é bissexto"

print(f"O ano {ano} {status}.")
