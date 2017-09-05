# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-05 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagamento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='inscricao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='de_incricao', to='user.Inscricao'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='usuario_recebimento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='recebido_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cupom',
            name='evento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cupom_do_evento', to='core.Evento'),
        ),
    ]
