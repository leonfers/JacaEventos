from django.db import models

import re

from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
# Create your models here.

class Usuario(models.Model):

    username = models.CharField('Nome do Usuário', max_length=30)



class Inscricao(models.Model):

    status_inscricao = models.BooleanField('Inscrito/Não Inscrito', blank=True, default=True)
    usuario = models.ForeignKey(Usuario, verbose_name=('Usuario'), on_delete=models.CASCADE, related_name="minhas_inscricoes" ,blank=False, null=False)
    minhas_incricoes = models.ForeignKey('usuario.Usuario', related_name='minhas_incricoes')


