from src.business.tributos import Tributos
from src.entities.funcionario import Funcionario
from conexao_bd import gerar_cnx


class Holerite():

    def __init__(self, funcionario: Funcionario):
        self.matricula = funcionario.matricula
        self.nome = funcionario.nome
        self.data_admissao = funcionario.data_admissao
        self.cargo = funcionario.cargo_descricao()
        self.salario_base = funcionario.cargo_salario_base()
        self.comissao = int(funcionario.cargo_comissao_valor()*100)
        self.valor_comissao = round(
            float(funcionario.cargo_salario_base()) * funcionario.cargo_comissao_valor(), 2)
        self.tributos = Tributos(funcionario)
        self.valor_inss = self.tributos.inss_recolhimento()
        self.valor_irrf = self.tributos.irrf_recolhimento()
        self.tx_inss = int(self.tributos.inss_aliquota * 100)
        self.tx_irff = int(self.tributos.irrf_aliquota * 100)
        self.total_vencimentos = self.tributos.vencimentos
        self.base_inss = self.tributos.vencimentos
        self.base_irrf = self.tributos.irrf_bc
        self.base_fgts = self.tributos.vencimentos
        self.valor_fgts = round(self.tributos.vencimentos * 0.08, 2)

    def gerar_holerite(self, mes_ano: str, faltas: int) -> None:
        self.mes_ano = mes_ano
        self.faltas = faltas
        self.valor_faltas = round(
            faltas * (self.salario_base * 0.75 / 22.5), 2)
        self.total_descontos = round(
            self.valor_inss + self.valor_faltas + self.valor_irrf, 2)
        self.liquido_receber = round(
            self.total_vencimentos - self.total_descontos, 2)

    def holerites_cadastradas(self) -> None:
        cnx = gerar_cnx()
        cursor = cnx.cursor()
        cursor.execute(
            f"SELECT * FROM cargos WHERE matricula = {self.matricula};")
        holerites_do_funcionario = cursor.fetchall()
        cursor.close()
        cnx.close()
        for holerite in holerites_do_funcionario:
            for chave, valor in holerite.items():
                print(f'| {chave}: {valor}', end='')
        print()

    def imprimir_holerite(self) -> None:
        print(f"""
__________________________________________________________________________________________       
Empresa XPTO Alimentos                          Recibo de Pagamento de Salário
Endereço: Rua XV de Novembro, 15, Centro        Mês de referência: {self.mes_ano}
CNPJ: 12.345.678/0001-00
==========================================================================================
Matricula     Nome do Funcionário       Data de Admissão        Função
{self.matricula}        {self.nome}             {self.data_admissao}            {self.cargo}
==========================================================================================
Código    Descrição                 Referência      Proventos         Descontos
   101    Salário Base                   22,50      R$ {self.salario_base}              
   203    Comissão                          {self.comissao}%      R$ {self.valor_comissao}
   303    Faltas                            {self.faltas}                           R$ {self.valor_faltas}
   973    INSS Folha                       {self.tx_inss}%                          R$ {self.valor_inss}
   978    IRRF Folha                       {self.tx_irff}%                         R$ {self.valor_irrf}
   
   
                                                    Total Vencimentos   Total Descontos
                                                    R$ {self.total_vencimentos}          R$ {self.total_descontos}  
   
SalárioBase  BaseCálc.INSS  BaseCálc.FGT  FGTSmês  BaseCálcIRRF     Líquido a Receber: 
R$ {self.salario_base}   R$ {self.base_inss}      R$ {self.base_fgts}   R$ {self.valor_fgts}  R$ {self.valor_irrf}       R$ {self.liquido_receber}
__________________________________________________________________________________________    
""")
