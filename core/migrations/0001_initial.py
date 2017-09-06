# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 16:15
from __future__ import unicode_literals

import core.enum
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True, verbose_name='nome')),
                ('descricao', models.TextField(blank=True, verbose_name='descricao da atividade')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=7, verbose_name='valor')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='AtividadePacote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='EspacoFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(default='', max_length=30, verbose_name='nome')),
                ('tipoEspacoFisico', enumfields.fields.EnumField(default='padrao', enum=core.enum.TipoEspacoFisico, max_length=10)),
                ('capacidade', models.DecimalField(decimal_places=0, default=0, max_digits=5, verbose_name='capacidade')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True, verbose_name='nome')),
                ('descricao', models.TextField(blank=True, max_length=256, verbose_name='descricao')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='valor')),
                ('tipo_evento', enumfields.fields.EnumField(default='padrao', enum=core.enum.TipoEvento, max_length=10)),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de entrada')),
                ('status', enumfields.fields.EnumField(default='inscricoes_abertas', enum=core.enum.StatusEvento, max_length=19)),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='EventoInstituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_relacionamento', enumfields.fields.EnumField(default='padrao', enum=core.enum.TipoInstituicao, max_length=10)),
            ],
            options={
                'verbose_name': 'Relacionamento_Instituicao_Evento',
                'verbose_name_plural': 'Relacionamentos_Instituicao_Evento',
            },
        ),
        migrations.CreateModel(
            name='EventoSatelite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GerenciaEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_gerente', enumfields.fields.EnumField(default='padrao', enum=core.enum.TipoGerencia, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=30, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'Instituicao',
                'verbose_name_plural': 'Instituicoes',
            },
        ),
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='nome')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='valor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PacoteInscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ResponsavelAtividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(blank=True, max_length=30, unique=True, verbose_name='nome')),
                ('descricao', models.CharField(blank=True, max_length=500, unique=True, verbose_name='descricao')),
                ('tipo_responsavel', enumfields.fields.EnumField(default='padrao', enum=core.enum.TipoResponsavel, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsavelTrilha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_responsavel_trilha', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='TagEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Relacionamento_Tag_Evento',
                'verbose_name_plural': 'Relacionamentos_Tag_Tag',
            },
        ),
        migrations.CreateModel(
            name='TagUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tag_de_usuario', to='core.Tag')),
            ],
            options={
                'verbose_name': 'Relacionamento_Tag_Usuario',
                'verbose_name_plural': 'Relacionamentos_Tag_Usuario',
            },
        ),
        migrations.CreateModel(
            name='AtividadeAdministrativa',
            fields=[
                ('atividade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Atividade')),
            ],
            options={
                'verbose_name': 'AtividadeNeutra',
                'verbose_name_plural': 'AtividadesNeutra',
            },
            bases=('core.atividade',),
        ),
        migrations.CreateModel(
            name='AtividadeContinua',
            fields=[
                ('atividade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Atividade')),
            ],
            options={
                'verbose_name': 'AtividadeContinua',
                'verbose_name_plural': 'AtividadesContinuas',
            },
            bases=('core.atividade',),
        ),
        migrations.CreateModel(
            name='AtividadePadrao',
            fields=[
                ('atividade_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Atividade')),
            ],
            options={
                'verbose_name': 'Atividade Padrao',
                'verbose_name_plural': 'Atividades Padrao',
            },
            bases=('core.atividade',),
        ),
        migrations.CreateModel(
            name='Trilha',
            fields=[
                ('pacote_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Pacote')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.pacote',),
        ),
    ]
