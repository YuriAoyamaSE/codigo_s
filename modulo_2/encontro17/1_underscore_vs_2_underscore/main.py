#sobre a diferença entre usar _ e __ no atributoda classe 

from one_underscore import *
#quando importa com *, o python ignora função que começa com _

ex1 = One()
print(ex1._private_attr)

# _private_function()

# ---

# Usar __ em herança (evitar conflito entre os atributos das classes)
from two_underscores import *

d2 = TwoChild()
print(d2.__private_attr)
# print(dir(d2))