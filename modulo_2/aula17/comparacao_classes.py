"""
How Bootcamps - Stone - /código[s]
Data: 19/04/2022
Autor: Henrique Junqueira Branco
Enunciado: POO - parte 3 - comparação entre objetos de classes próprias
"""


class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    # Define o comportamento de comparação
    def __eq__(self, other: object) -> bool:
        return (self.name == other.name) and (self.salary == other.salary)

    # greater than or equal (maior ou igual que)
    def __ge__(self, other) -> bool:
        return self.salary >= other.salary

    # less than or equal (menor ou igual que)
    def __le__(self, other) -> bool:
        return self.salary <= other.salary

    # greater than (maior que)
    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    # less than (menor que)
    def __lt__(self, other) -> bool:
        return self.salary < other.salary


emp1 = Employee("Joao", 2000)
emp2 = Employee("Joao", 3000)

print(emp1 == emp2)
print(emp1 >= emp2)
print(emp1 <= emp2)
print(emp1 > emp2)
print(emp1 < emp2)
