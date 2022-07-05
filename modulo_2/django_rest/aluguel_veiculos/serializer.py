from rest_framework import serializers
from aluguel_veiculos.models import Cliente, Veiculo


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url', 'nome', 'endereco',
                  'telefone', 'cpf', 'cnpj', 'tipo']


class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Veiculo
        fields = ['placa', 'km', 'bagageiro', 'portas', 'tipo']
