dividendo = 1
divisor = 0

try:
    dividendo/divisor
except AttributeError as ex:
    print("ERRO ARITMÉTICO")
except ZeroDivisionError as ex_zero:
    print(f"ERROR: {ex_zero.args[0]}. Altere o divisor.")
except BaseException:
    print('Outros erros')
