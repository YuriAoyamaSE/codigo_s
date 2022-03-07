
import string

placa = input("Informe o número da placa veicular: ")
padrao_antigo = False
if len(placa) == 8:
    if placa[0] and placa[1] and placa[2] in string.ascii_letters:
        if placa[3] == "-":
            if  placa[4] and placa[5] and placa[6] and placa[7] in string.digits:
                padrao_antigo = True

print(padrao_antigo)
