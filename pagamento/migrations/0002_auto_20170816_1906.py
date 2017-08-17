# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 22:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('user', '0001_initial'),
        ('pagamento', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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