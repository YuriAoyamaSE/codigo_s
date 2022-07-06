from rest_framework import viewsets
from aluguel_veiculos.models import Aluguel
from aluguel_veiculos.serializers.aluguel_serializer import AluguelSerializer

class AluguelViewSet(viewsets.ModelViewSet):
    queryset = Aluguel.objects.all()
    serializer_class = AluguelSerializer