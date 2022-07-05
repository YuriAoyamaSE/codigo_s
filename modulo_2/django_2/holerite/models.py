import uuid
from django.db import models


class Cargo(models.Model):
    codigo = models.UUIDField(
        primary_key=True, default=uuid.uuid4)
    descricao = models.TextField()
    salario = models.FloatField()
    comissao = models.FloatField()

    def __str__(self) -> str:
        return self.descricao


class Funcionario(models.Model):
    matricula = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=11, null=True)
    dt_admissao = models.CharField(max_length=10, null=True)
    comissao = models.CharField(max_length=1, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
