# Generated by Django 4.0.5 on 2022-07-02 14:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('codigo', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('descricao', models.TextField()),
                ('salario', models.FloatField()),
                ('comissao', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('matricula', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, null=True)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('dt_admissao', models.CharField(max_length=10, null=True)),
                ('comissao', models.CharField(max_length=1, null=True)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='holerite.cargo')),
            ],
        ),
    ]