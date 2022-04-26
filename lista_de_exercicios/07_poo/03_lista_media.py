"""
Exercício 3:  
Infelizmente  a  classe  nativa  do  Python  list  não  tem  alguns  cálculos  muito 
utilizados: médias. Construa uma classe chamada ListaPersonalizada que herde 
todas as funcionalidades da classe nativa e acrescente os cálculos de média 
simples e ponderada.
"""

class ListaPersonalizada(list):
    def media(self):
        media = 0
        for item in self:
            item = int(item)
            media+=item
        media /= len(self)
        return media

numero = ListaPersonalizada("1234")
print(numero.media())

