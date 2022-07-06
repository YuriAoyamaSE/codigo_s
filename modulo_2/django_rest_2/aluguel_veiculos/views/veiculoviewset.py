from rest_framework import viewsets
from aluguel_veiculos.models import Veiculo
from aluguel_veiculos.serializers.veiculo_serializer import VeiculoSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
