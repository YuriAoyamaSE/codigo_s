"""
Ver pasta: aluguel_veículos
"""

a = 1

b= 0

try:
    a/b
except ZeroDivisionError as ex:
    print(f"ERROR: {ex.args[0]}. Altere o divisor.")
