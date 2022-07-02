from django.contrib import admin

from holerite.models import Cargo, Funcionario

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Cargo)
