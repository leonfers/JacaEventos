# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 01:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(blank=True, verbose_name='Data inicio')),
                ('data_fim', models.DateField(blank=True, verbose_name='Data fim')),
            ],
        ),
    ]
