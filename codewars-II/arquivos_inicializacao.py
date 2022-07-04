from conexao_bd import cnx_sem_database, gerar_cnx


def gerar_env() -> None:
    dados = {'NAME': 'codewars2', 'USER': '',
             'PASSWORD': '', 'HOST': '', 'PORT': ''}
    print("--------------Dados para conexão com mySQL--------------")
    print("Por padrão do sistema, o nome do schema será 'codewars2'.")
    dados['USER'] = input("Informe o nome do usuário: ")
    dados['PASSWORD'] = input("Informe a senha do usuário: ")
    dados['HOST'] = input("Informe o host: ")
    dados['PORT'] = input("Informe a porta: ")
    with open('.env', 'w') as arquivo:
        for chave, valor in dados.items():
            arquivo.writelines(f"{chave}='{valor}'\n")


def gerar_schema() -> None:
    schema = "CREATE SCHEMA IF NOT EXISTS `codewars2` DEFAULT CHARACTER SET utf8mb3;"
    cnx = cnx_sem_database()
    cursor = cnx.cursor()
    cursor.execute(schema)
    cursor.close()
    cnx.close()


def gerar_table_cargos() -> None:
    cnx = gerar_cnx()
    cursor = cnx.cursor()
    comando = """USE codewars2;
    CREATE TABLE IF NOT EXISTS `codewars2`.`cargos` (
      `codigo` CHAR(2) NOT NULL,
      `descricao` VARCHAR(45) NOT NULL,
      `salario_base` VARCHAR(15) NOT NULL,
      `comissao` VARCHAR(5) NULL DEFAULT '0',
      PRIMARY KEY (`codigo`))
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8mb3;"""
    cursor.execute(comando)
    cursor.close()
    cnx.close()


def gerar_table_funcionarios() -> None:
    cnx = gerar_cnx()
    cursor = cnx.cursor()
    comando = """CREATE TABLE IF NOT EXISTS funcionarios (
      `matricula` INT NOT NULL AUTO_INCREMENT,
      `nome` VARCHAR(45) NOT NULL,
      `cpf` CHAR(11) NOT NULL,
      `data_admissao` CHAR(10) NOT NULL,
      `cargo` CHAR(2) NOT NULL,
      `comissao` TINYINT NOT NULL DEFAULT '0',
      PRIMARY KEY (`matricula`,`cpf`))
    ENGINE = InnoDB
    AUTO_INCREMENT=100000
    DEFAULT CHARACTER SET = utf8mb3;"""
    cursor.execute(comando)
    cursor.close()
    cnx.close()


def gerar_table_holerites() -> None:
    cnx = gerar_cnx()
    cursor = cnx.cursor()
    comando = """CREATE TABLE IF NOT EXISTS `codewars2`.`holerities` (
      `mes_ano` VARCHAR(20) NOT NULL,
      `matricula` VARCHAR(45) NOT NULL,
      `funcionario` VARCHAR(45) NULL,
      `data_admissao` VARCHAR(45) NULL,
      `cargo` VARCHAR(45) NULL,
      `salario_base` VARCHAR(45) NULL,
      `comissao` VARCHAR(45) NULL,
      `valor_comissao` VARCHAR(45) NULL,
      `total_vencimentos` VARCHAR(45) NULL,
      `faltas` VARCHAR(45) NULL,
      `valor_faltas` VARCHAR(45) NULL,
      `tx_inss` VARCHAR(45) NULL,
      `base_inss` VARCHAR(45) NULL,
      `valor_inss` VARCHAR(45) NULL,
      `tx_irrf` VARCHAR(45) NULL,
      `base_irrf` VARCHAR(45) NULL,
      `valor_irrf` VARCHAR(45) NULL,
      `total_descontos` VARCHAR(45) NULL,
      `base_fgts` VARCHAR(45) NULL,
      `valor_fgts` VARCHAR(45) NULL,
      `liquido_receber` VARCHAR(45) NULL,
      PRIMARY KEY (`mes_ano`, `matricula`));
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = utf8mb3;"""
    cursor.execute(comando)
    cursor.close()
    cnx.close()


def preencher_cargos() -> None:
    cnx = gerar_cnx()
    cursor = cnx.cursor()

    comando = "INSERT INTO codewars2.cargos(codigo, descricao, salario_base, comissao) VALUES (%s,%s,%s,%s)"
    dados = [('10', 'Cientista de Dados', '10200', '0.1'),
             ('20', 'Especialista em Business Intelligence', '7000', '0.08'),
             ('30', 'Desenvolvedor Mobile Sênior', '6700', '0.07'),
             ('31', 'Desenvolvedor Mobile Pleno', '3550', '0.06'),
             ('32', 'Desenvolvedor Júnior', '3000', '0.03'),
             ('50', 'Gerente de Projeto', '8900', '0.08')]

    cursor.executemany(comando, dados)
    cnx.commit()

    cursor.close()
    cnx.close()
