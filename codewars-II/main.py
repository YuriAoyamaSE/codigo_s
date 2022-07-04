from arquivos_inicializacao import gerar_env, gerar_schema, gerar_table_cargos, gerar_table_funcionarios, gerar_table_holerites, preencher_cargos
from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario
from src.entities.holerite import Holerite


def menu_inicializacao():
    criando_env = input("""--------------------------------Menu de Inicialização--------------------------------
Para conectar ao sistema de banco de dados da máquina local é imprescindível a existência
de um arquivo .env com dados sensíveis. O arquivo estará seguro, pois está no rol do 
.gitignore. Caso já não tenha o arquivo, gostaria que o sistema crie um? (s/n) """)
    if criando_env == 's':
        gerar_env()

    criar_banco_dados = input("""-------------------------------------------------------------------------------------
Para o funcionamento do sistema, é necessária a existência de:
    => Schema 'codewars2'
    => Tabela 'funcionarios'
    => Tabela 'cargos'
    => Tabela 'holerites'
Gostaria que o sistema gere o Banco de Dados? (s/n) """)
    if criar_banco_dados == 's':
        gerar_schema()
        gerar_table_cargos()
        preencher_cargos()
        gerar_table_funcionarios()
        gerar_table_holerites()


def menu_principal():
    print("""----------------------Menu----------------------
[1] - Cadastrar novo funcionário
[2] - Procurar dados de um funcionário
[3] - Listar todos os funcionários
[4] - Excluir funcionário
[5] - Alterar dados de um funcionário
[6] - Gerar holerite de um funcionário
[7] - Gerar lista de holerites de um funcionário
[8] - Gerar lista de holerites de todos os funcionários
[0] - Sair""")
    return input()


def cadastrar_funcionario():
    print('-----------Cadastro de novo funcionário-----------')
    nome = input('Informe o nome: ')
    cpf = input('Informe o CPF (apenas números): ')
    data_admissao = input('Informe a data de admissão (aaaa-mm-dd): ')
    cargo = input('Informe o código do cargo: ')
    comissao = input('O funcionário receberá comissão? (s/n): ')
    comissao = True if comissao == 's' else False
    funcionario = Funcionario(nome, cpf, data_admissao, cargo, comissao)
    cadastro_funcionario.inclusao(funcionario)
    print('Cadastro efetuado com a matricula:', funcionario.matricula)


def checar_funcionario(matricula):
    funcionario = cadastro_funcionario.consulta(matricula)
    if funcionario:
        return funcionario
    else:
        print('Funcionário não encontrado')
        return None


def procurar_funcionario():
    print('-------------Procurar por funcionário-------------')
    matricula = int(input('Informe o número de matrícula: '))
    funcionario = checar_funcionario(matricula)
    if funcionario:
        for chave, valor in funcionario.items():
            print(f'{chave}: {valor}')


def listar_funcionarios():
    print('---------------Listar funcionários---------------')
    lista_funcionarios = cadastro_funcionario.listagem()
    for funcionario in lista_funcionarios:
        for chave, valor in funcionario.items():
            print(f'| {chave}: {valor}', end='')
        print()


def excluir_funcionario():
    print('---------------Excluir funcionário---------------')
    matricula = int(input('Informe o número de matrícula: '))
    funcionario = checar_funcionario(matricula)
    if funcionario:
        cadastro_funcionario.exclusao(matricula)


def alterar_funcionario():
    print('-----------Alterar dados de funcionário-----------')
    matricula = int(input('Informe o número de matrícula: '))
    funcionario = checar_funcionario(matricula)
    if funcionario:
        for chave, valor in funcionario.items():
            print(f'{chave}: {valor}')
        escolha = input(
            'Qual informação gostaria de alterar? Para sair, informe "0". ')
        alteracoes = {}
        while escolha != '0':
            if escolha in funcionario.keys():
                alteracoes[escolha] = input(f'{escolha}: ')
            else:
                print('Opção inválida.')
            escolha = input(
                'Qual informação gostaria de alterar? Para sair, informe "0". ')
        cadastro_funcionario.alteracao(matricula, alteracoes)


def holerite_funcionario():
    print('---------Imprimir holerite de funcionario----------')
    matricula = int(input('Informe o número de matrícula: '))
    if checar_funcionario(matricula):
        funcionario = cadastro_funcionario.retornar_funcionario(matricula)
        mes_ano = input('Informe o mês e ano da holerite: ')
        holerite = Holerite(funcionario)
        holerite.gerar_holerite(mes_ano, 2)
        holerite.imprimir_holerite()


def imprimir_lista_holerites(lista_de_holerites):
    print("Ainda a implementar")


def listar_holerites_individual():
    lista_holerites = []
    imprimir_lista_holerites(lista_holerites)


def listar_todas_holerites():
    lista_holerites = []
    imprimir_lista_holerites(lista_holerites)


if __name__ == '__main__':
    menu_inicializacao()
    cadastro_funcionario = CadastroFuncionario()
    while True:
        opcao = menu_principal()
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            procurar_funcionario()
        elif opcao == '3':
            listar_funcionarios()
        elif opcao == '4':
            excluir_funcionario()
        elif opcao == '5':
            alterar_funcionario()
        elif opcao == '6':
            holerite_funcionario()
        elif opcao == '7':
            listar_holerites_individual()
        elif opcao == '8':
            listar_todas_holerites()
        elif opcao == '0':
            break
        else:
            print('opção inválida, tente de novo.')

    print("""          
--------------------------------Programa encerrado--------------------------------
          """)
