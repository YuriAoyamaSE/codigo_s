from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from aluguel_veiculos.views.cliente_viewset import ClienteViewset
from aluguel_veiculos.views.veiculo_viewset import VeiculoViewset
from aluguel_veiculos.views.aluguel_viewset import AluguelViewSet

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewset, basename='Clientes')
router.register(r'veiculo', VeiculoViewset, basename='Veiculos')
router.register(r'aluguel', AluguelViewSet, basename='aluguel')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
