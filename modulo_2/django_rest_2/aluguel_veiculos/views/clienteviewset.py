from rest_framework import viewsets
from aluguel_veiculos.models import Cliente
from aluguel_veiculos.serializers.cliente_serializer import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
