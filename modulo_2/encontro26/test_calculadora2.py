import unittest
from calculadora import *

class Test_calculadora(unittest.TestCase):
    
    def test_multiplicar(self):
        valor_a = 2
        valor_b = 2
        valor_esperado = 4
        
        resultado = multiplicar(valor_a,valor_b)
        
        self.assertTrue(resultado == valor_esperado)

    def test_multiplicar(self):
        a = 2
        b = 0

        with self.assertRaises(ZeroDivisionError):
            dividir(a,b)
