from unittest import TestCase
from src.business.tributos import Tributos


class TestIrrf(TestCase):

    def test_parametros(self):
        # dado
        salario_base = 3000
        comissao = 90

        # quando
        tributo = Tributos(salario_base, comissao)
        resultado = tributo.irrf_parametros()

        # então
        self.assertTrue(
            resultado == {'bc': 2810.2, 'aliquota': 0.075, 'deducao': 142.8})

    def test_recolhimento(self):
        # dado
        salario_base = 3000
        comissao = 90

        # quando
        tributo = Tributos(salario_base, comissao)
        resultado = tributo.irrf_recolhimento()

        # então
        self.assertTrue(resultado == 67.96)
