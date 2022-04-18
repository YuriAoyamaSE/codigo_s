"""
How Bootcamps - Stone - /código[s]
Data: 14/04/2022
Autor: Henrique Junqueira Branco
Tema: Introdução a programação orientada a objetos 

Atributos não-públicos: usa apenas 1 underscore.
Atributos "Privados": usa 2 underscores. Para chamar, deve usar "_nomeDaClasse__atributo"
"""

from pessoas import Funcionario
    
funcionario1 = Funcionario("João", "da Silva")
funcionario2 = Funcionario("Antônio", "Andrade da Silva",2_000)
funcionario3 = Funcionario("Sérgio", "Ramos Figueiredo", 2_500)


funcionario1.dar_aumento()
funcionario1.dar_aumento()
funcionario2.dar_aumento()


print("funcionario1: ", funcionario1.salario_atual)
print("funcionario2: ", funcionario2.salario_atual)
print("funcionario3: ", funcionario3.salario_atual)



