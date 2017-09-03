# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 17:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarioatividadecontinua',
            name='atividade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Atividade', to='core.AtividadeContinua', verbose_name='Atividade'),
        ),
    ]