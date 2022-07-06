from rest_framework import serializers
from aluguel_veiculos.models.aluguel import Aluguel

class AluguelSerializer(serializers.Serializer):

    class Meta():
        model = Aluguel
        fields = "__all__"
