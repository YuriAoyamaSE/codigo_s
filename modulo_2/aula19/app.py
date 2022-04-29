from src.business.cadastro_cliente import CadastroCliente
from src.entities.entity import Entity
from src.entities.cliente import Cliente
from src.entities.pessoa_fisica import PessoaFisica
from src.entities.pessoal_juridica import PessoaJuridica


def print_cliente(cliente: Cliente) -> None:
    print(cliente.id)
    print(cliente.endereco)
    print(cliente.telefone)
    print(cliente.nome)


cliente01 = Cliente("1",'rua retrô',"3222-4333",'josival')
clientepf = PessoaFisica('2','av 43','088-0078-5065','000.555.666-22','torival')
clientepj = PessoaJuridica('3','alameta tesouro','2455-8515','12.56.485.21/0001-15', 'Já É Ltda')

clientes = [cliente01, clientepf, clientepj]

for cliente in clientes:
    print_cliente(cliente)

cadastro01 = CadastroCliente()
entidade01 = Entity('Vende-Tudo')
cadastro01.inserir(entidade01)

