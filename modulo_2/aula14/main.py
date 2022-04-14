"""
How Bootcamps - Stone - /código[s]
Data: 12/04/2022
Autor: Henrique Junqueira Branco
Tema: Introdução a programação orientada a objetos 

    'Objeto é a materialização de uma classe' => instâncias da classe

    quem é o self? é um objeto genérico. Por exemplo, o self seria o funcionario1, funcionario2, etc
"""
from pessoas import Funcionario

    
funcionario1 = Funcionario("João", "da Silva")
funcionario2 = Funcionario("Antônio", "Andrade da Silva",2_000)
funcionario3 = Funcionario("Sérgio", "Ramos Figueiredo", 2_500)


funcionario1.dar_aumento()
funcionario1.dar_aumento()
funcionario2.dar_aumento()


print("funcionario1: ", funcionario1._salario_atual)
print("funcionario2: ", funcionario2._salario_atual)
print("funcionario3: ", funcionario3._salario_atual)


