from django.db import models

import re

from django.db import models
from django.core import validators
from django.conf import settings
from jacaEventos.core.models import Evento
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
# Create your models here.

class Usuario(models.Model):

    username = models.CharField('Nome do Usuário', max_length=30)



class Inscricao(models.Model):

    status_inscricao = models.BooleanField('Inscrito/Não Inscrito', blank=True, default=True)
    usuario = models.ForeignKey(Usuario, verbose_name=('Usuario'), on_delete=models.CASCADE, related_name="minhas_inscricoes" ,blank=False, null=False)
    evento = models.ForeignKey(Evento, verbose_name=('Evento'))
    meus_eventos = models.ForeignKey('core.Evento', related_name='participantes', blank=True, null=True)


