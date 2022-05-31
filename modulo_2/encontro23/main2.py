dividendo = 1
divisor = 0

try:
    #dividendo/divisor
    if divisor == 0:
        raise AttributeError('Divisor inválido')

    dividendo/divisor
    
except ZeroDivisionError as ex:
    print(f"ERROR: {ex.args[0]}. Altere o divisor.")
# Não cai no exception por causa do raise, que vem antes da divisão

"""
Pode usar o BaseException se quiser generalizar, pois é a classe mãe maior de todos os tipos de exceções.
Por exemplo:
- ZeroDivisionError herda de ArithmeticError
- ArithmeticError herda de Exception
- Exception herda de BaseException
"""