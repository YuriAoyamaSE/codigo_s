from tabnanny import verbose
from django.contrib import admin
from aluguel_veiculos.models import Veiculo, Cliente, Aluguel


class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco', 'telefone', 'tipo', 'cpf')
    # exclude = ('cnpj')
    list_display = ('nome', 'tipo', 'cpf')


class AluguelAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'veiculo')


class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa',)


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Veiculo, VeiculoAdmin)
admin.site.register(Aluguel, AluguelAdmin)
