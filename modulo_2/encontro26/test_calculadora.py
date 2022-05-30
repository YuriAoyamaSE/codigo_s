import unittest
from calculadora import *

class TestCalculadora(unittest.TestCase):
    
    def test_somar_geral(self):
        # Given
        valor_a = 1
        valor_b = 2

        # When
        resultado = somar(valor_a,valor_b)

        # 
        self.assertTrue(resultado == 3)

    def test_somar_inteiros(self):
        valor_a = 1
        valor_b = 2
        valor_esperado = 3
        resultado = somar(valor_a,valor_b)
        self.assertEqual(type(resultado), int)

    def test_subtrair(self):
        valor_a = 3
        valor_b = 2
        valor_esperado = 1
        resultado = subtrair(valor_a,valor_b)
        self.assertAlmostEqual(resultado, valor_esperado)

    def test_dividir(self):
        valor_a = 2
        valor_b = 2
        valor_esperado = 1
        resultado = dividir(valor_a,valor_b)
        self.assertTrue(resultado == valor_esperado)

    def test_multiplicar(self):
        valor_a = 2
        valor_b = 2
        valor_esperado = 4
        resultado = multiplicar(valor_a,valor_b)
        self.assertTrue(resultado == valor_esperado)

