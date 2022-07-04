from unittest import TestCase
from src.business.tributos import Tributos


class TestInss(TestCase):

    def test_faixa_1(self):
        # dado
        vencimentos = 1_100

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 82.50)

    def test_faixa_2(self):
        # dado
        vencimentos = 1_500

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 116.82)


    def test_faixa_3(self):
        # dado
        vencimentos = 3_000

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 269.00)

    def test_faixa_4(self):
        # dado
        vencimentos = 5_000

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 536.18)

    def test_acima_do_teto(self):
        # dado
        vencimentos = 8_000

        # quando
        tributo = Tributos(vencimentos)
        resultado = tributo.inss_recolhimento()

        # então
        self.assertTrue(resultado == 828.39)
