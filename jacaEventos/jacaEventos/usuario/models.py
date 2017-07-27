from django.db import models

import re

from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
# Create your models here.

class Usuario(models.Model):

    username = models.CharField('Nome do Usuário', max_length=30, unique=True)
    nome = models.CharField("Nome", max_length=30)
    email = models.EmailField("E-Mail", unique=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)


class Inscricao(models.Model):

    status_inscricao = models.BooleanField('Inscrito/Não Inscrito', blank=True, default=True)
    usuario = models.ForeignKey(Usuario, verbose_name=('usuario'), on_delete=models.CASCADE, related_name="inscricoes" ,blank=False, null=False)
    evento = models.ForeignKey('core.Evento', default="")
    atividade = models.ManyToManyField('core.Atividade',through="ItemInscricao")

    def get_ativiades(self):

        atividades = self.evento.atividades.get_queryset()
        return atividades

class ItemInscricao(models.Model):

        inscricao = models.ForeignKey('Inscricao', blank=True, default="")
        atividade = models.ForeignKey('core.Atividade',blank=True, default="")