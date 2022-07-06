from pkg_resources import require
from rest_framework import serializers
from aluguel_veiculos.models.cliente import Cliente


class ClienteSerializer(serializers.Serializer):
    cnpj = serializers.CharField(require=False)
    
    class Meta():
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        if (data.get('tipo') == 'PJ') and (data.get('cnpj') == None):
            raise serializers.ValidationError({'CNPJ': 'Pessoa jurídica deve incluir CNPJ'})
        return data
    
    # def validate_tipo(self, tipo):
    #     if (tipo == 'PJ') and (self.cnpj == None):
    #         raise serializers.ValidationError('Pessoa jurídica deve incluir CNPJ')
    #     return tipo
    
    