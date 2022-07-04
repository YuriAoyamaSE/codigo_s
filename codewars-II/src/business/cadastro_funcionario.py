from conexao_bd import gerar_cnx
from src.entities.funcionario import Funcionario


class CadastroFuncionario():

    def inclusao(self, funcionario: Funcionario) -> None:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        insert_query = "INSERT INTO funcionarios(nome,cpf,data_admissao,cargo,comissao) VALUES (%s,%s,%s,%s,%s)"
        insert_record = (funcionario.nome, funcionario.cpf, funcionario.data_admissao,
                         funcionario.cargo, funcionario.comissao)
        cursor.execute(insert_query, insert_record)
        cnx.commit()

        insert_query = f"SELECT matricula FROM funcionarios WHERE cpf = {funcionario.cpf};"
        cursor.execute(insert_query)
        funcionario.matricula = cursor.fetchall()[0][0]
        cursor.close()
        cnx.close()

    def consulta(self, numero_matricula) -> dict:
        lista_funcionarios = self.listagem()
        for funcionario in lista_funcionarios:
            if funcionario['matricula'] == numero_matricula:
                return (funcionario)
        return None
    
    def retornar_funcionario(self, numero_matricula) -> Funcionario:
        dados = self.consulta(numero_matricula)
        funcionario = Funcionario(dados['nome'], dados['cpf'], dados['data_admissao'],dados['cargo'],dados['comissao'],dados['matricula'])
        return funcionario

    def exclusao(self, numero_matricula) -> None:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        insert_query = "DELETE FROM funcionarios WHERE matricula = %s;"
        cursor.execute(insert_query, [numero_matricula])
        cnx.commit()
        cursor.close()
        cnx.close()

    def listagem(self):
        cnx = gerar_cnx()
        cursor = cnx.cursor(dictionary=True)
        insert_query = "SELECT * FROM funcionarios;"
        cursor.execute(insert_query)
        lista_funcionarios = cursor.fetchall()
        cursor.close()
        cnx.close()
        return lista_funcionarios

    def alteracao(self, numero_matricula, alteracoes: dict) -> None:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        for chave, valor in alteracoes.items():
            insert_query = f"UPDATE funcionarios SET {chave} = '{valor}' WHERE matricula = {numero_matricula};"
            cursor.execute(insert_query)
        cnx.commit()
        cursor.close()
        cnx.close()
