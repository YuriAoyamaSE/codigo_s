class CriandoError(Exception):
    pass

dividendo = 1
divisor = 0

try:
    if dividendo ==1:
        raise CriandoError('deu erro')
    dividendo/divisor
except AttributeError as ex:
    print("ERRO ARITMÉTICO")
except ZeroDivisionError as ex_zero:
    print(f"ERROR: {ex_zero.args[0]}. Altere o divisor.")
except Exception as ex:
    print(ex.args[0])
except BaseException:
    print('Outros erros')


# criando uma classede erro única:
class NumberError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def adicao(a,b)-> int:
    if (a<0) or (b<0):
        raise NumberError('Valor Negativo')
    return a+b

try:
    resultado = adicao(1,1)
    print(resultado)
    resultado = adicao(1,-1)
    print(resultado)
except Exception as ex:
    print(ex.args[0])
