from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from aluguel_veiculos.views.clienteviewset import ClienteViewSet
from aluguel_veiculos.views.veiculoviewset import VeiculoViewSet
from aluguel_veiculos.views.aluguelviewset import AluguelViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet, basename='Clientes')
router.register(r'veiculo', VeiculoViewSet, basename='Veiculos')
router.register(r'aluguel', AluguelViewSet, basename='aluguel')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
