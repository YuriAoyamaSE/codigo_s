def reverta_numeros(numero: int) -> int:
    numero_revertido = str(numero)[::-1]
    return int(numero_revertido)

print(reverta_numeros(123456789))
