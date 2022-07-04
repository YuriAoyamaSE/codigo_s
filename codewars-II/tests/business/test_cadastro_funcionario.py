from unittest import TestCase
from src.business.cadastro_funcionario import CadastroFuncionario
from conexao_bd import gerar_cnx


class TestCadastroFuncionario(TestCase):

    @classmethod
    def setUpClass(self):
        # dado
        self.cadastro1 = CadastroFuncionario(
            'fulano1', '12345678900', '2022-06-06', '10', True)
        self.cadastro2 = CadastroFuncionario(
            'fulano2', '22345678900', '2022-07-06', '30', True)
        self.cadastro3 = CadastroFuncionario(
            'fulano3', '32345678900', '2022-08-06', '50', False)
        self.cadastro1.inclusao()
        self.cadastro2.inclusao()
        self.cadastro3.inclusao()

    def test_inclusao(self):
        # dado
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cadastro4 = CadastroFuncionario(
            'fulano4', '42345678900', '2022-09-06', '10', False)
        cursor.execute("SELECT * FROM funcionarios")
        cursor.fetchall()
        rows_inicial = cursor.rowcount

        # quando
        cadastro4.inclusao()
        cnx.commit()
        cursor.execute("SELECT * FROM funcionarios")
        cursor.fetchall()
        rows_final = cursor.rowcount
        resultado = rows_inicial + 1
        cursor.close()
        cnx.close()

        # então
        self.assertTrue(resultado == rows_final)

    def test_exclusao(self):
        # dado
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        listagem = cursor.fetchall()
        rows_inicial = cursor.rowcount
        matricula = listagem[0][0]

        CadastroFuncionario.exclusao(matricula)
        cnx.commit()
        cursor.execute("SELECT * FROM funcionarios")
        cursor.fetchall()
        rows_final = cursor.rowcount
        resultado = rows_inicial - 1
        cursor.close()
        cnx.close()

        # então
        self.assertTrue(resultado == rows_final)

    def test_consulta(self):
        # dado
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        listagem = cursor.fetchall()
        rows_inicial = cursor.rowcount
        matricula = listagem[0][0]

        # quando
        CadastroFuncionario.exclusao(matricula)
        cnx.commit()
        cursor.execute("SELECT * FROM funcionarios")
        cursor.fetchall()
        rows_final = cursor.rowcount
        resultado = rows_inicial - 1
        cursor.close()
        cnx.close()

        # então
        self.assertTrue(resultado == rows_final)

    def test_alteracao(self):
        # dado
        cnx = gerar_cnx()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM funcionarios ORDER BY matricula DESC LIMIT 1;")
        funcionario_dict = cursor.fetchall()[0]
        matricula = funcionario_dict['matricula']
        funcionario_update = {'matricula': matricula, 'nome': 'ALTERADO', 'cpf':'99999999999', 'data_admissao': '5555-55-55', 'cargo': '10', 'comissao': 0}

        # quando
        CadastroFuncionario.alteracao(matricula, {'nome': 'ALTERADO', 'cpf':'99999999999', 'data_admissao': '5555-55-55', 'cargo': '10', 'comissao': 0})
        cnx.commit()
        resultado = CadastroFuncionario.consulta(matricula)        
        cursor.close()
        cnx.close()

        # então
        self.assertTrue(resultado == funcionario_update)

    def test_listagem(self):
        # dado
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM funcionarios")
        cursor.fetchall()
        rows_final = cursor.rowcount

        # quando
        listagem = CadastroFuncionario.listagem()
        resultado = len(listagem)
        cursor.close()
        cnx.close()

        # então
        self.assertTrue(resultado == rows_final)
