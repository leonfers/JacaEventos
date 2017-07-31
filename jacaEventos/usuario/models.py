from django import core
from django.db import models

import re

from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)


# Create your models here.



class Usuario(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome do Usuário', max_length=30, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      'O nome do usuario so pode conter letras, digitos ou os'
                                                                      'seguintes caracteres @/./+/-/_', 'invalid')])
    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100, blank=True)
    data_de_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)

    tags = models.ManyToManyField('core.Tag', through="core.Tag_Usuario", related_name='tags_do_usuario')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    def get_inscricoes(self):
        return self.inscricoes.all()
    
    def get_eventos(self):
        return self.meus_eventos.all()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'



class Inscricao(models.Model):

    status_inscricao = models.BooleanField('Inscrito/Não Inscrito', blank=True, default=True)
    usuario = models.ForeignKey(Usuario, verbose_name=('usuario'), on_delete=models.CASCADE, related_name="inscricoes",
                                blank=False, null=False)
    evento = models.ForeignKey('core.Evento', default="")
    atividade = models.ManyToManyField('core.Atividade', through="ItemInscricao")

    def get_ativiades(self):
        atividades = self.evento.atividades.all()
        return atividades


class ItemInscricao(models.Model):

    inscricao = models.ForeignKey('Inscricao', blank=True, default="")
    atividade = models.ForeignKey('core.Atividade', blank=True, default="")
