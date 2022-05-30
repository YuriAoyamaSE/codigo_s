from unittest import TestCase
from src.entities.cliente import Cliente
from src.business.cadastro_cliente import CadastroCliente


class TestCadastroCliente(TestCase):

    def test_inserir_cliente(self):
        #dado
        cliente = Cliente('1', 'rua1', '2333-5656', 'maicon')
        cadastro = CadastroCliente()

        # quanto
        cadastro.inserir(cliente)
        resultado = cadastro.__lista

        # então
        self.assertTrue(resultado[-1].nome == 'Maicon')