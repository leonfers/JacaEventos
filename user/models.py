from django import core
from django.db import models
import re
from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nome do Usuário', max_length=30, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                                      'O nome do user so pode conter letras, digitos ou os'
                                                                      'seguintes caracteres @/./+/-/_', 'invalid')])

    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100, blank=True)
    data_de_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)
    objects = UserManager()

    tags = models.ManyToManyField('core.Tag', through="core.Tag_Usuario", related_name='tags_do_usuario')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome or self.username

    def get_username(self):
        return self.username

    def get_nome_completo(self):
        return str(self)

    def get_inscricoes(self):
        return self.inscricoes.all()
    
    def get_eventos(self):
        return self.meus_eventos.all()


class Inscricao(models.Model):
    status_inscricao = models.BooleanField('Inscrito/Não Inscrito', blank=True, default=True)
    usuario = models.ForeignKey(
        'Usuario',
        verbose_name=('user'),
        on_delete=models.CASCADE,
        related_name="inscricoes",
        blank=False,
        null=False
    )
    evento = models.ForeignKey('core.Evento', default="")

    atividade = models.ManyToManyField('core.Atividade', through="ItemInscricao")

    class Meta:
        verbose_name = 'Id de Inscricao'
        verbose_name_plural = 'Id das Inscricoes'

    def __str__(self):
        return self.usuario

    def get_ativiades(self):
        atividades = self.evento.atividades.all()
        return atividades

    def add_item_inscricao(self, ):
        self.save()
        itemI_inscricao = ItemInscricao()
        itemI_nscricao = self


class ItemInscricao(models.Model):
    inscricao = models.ForeignKey('Inscricao', blank=True, default="")
    atividade = models.ForeignKey('core.Atividade', blank=True, default="")
