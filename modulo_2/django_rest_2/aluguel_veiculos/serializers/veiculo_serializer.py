from rest_framework import serializers
from aluguel_veiculos.models.veiculo import Veiculo


class VeiculoSerializer(serializers.Serializer):

    class Meta():
        model = Veiculo
        fields = "__all__"
