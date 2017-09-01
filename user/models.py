
import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from enumfields import Enum, EnumField
from utils.models import Observado
from user.enum import *

class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nome do Usuário', max_length=30, unique=True,
                                validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                'O nome do user so pode conter letras, digitos ou os''seguintes caracteres @/./+/-/_'
                                'invalid')])
    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100, blank=False)
    data_de_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    tags = models.ManyToManyField('core.Tag',
                                  through="core.Tag_Usuario",
                                  related_name='tags_do_usuario')


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome or self.username

    def get_username(self):
        return self.username

    def get_nome_completo(self):
        return self.nome

    def get_inscricoes(self):
        return self.inscricoes.all()
    
    def get_eventos(self):
        return self.meus_eventos.all()


class Inscricao(models.Model):
    status_inscricao = EnumField(StatusInscricao, default=StatusInscricao.ATIVA)
    tipo_inscricao = EnumField(TipoInscricao, default=TipoInscricao.PARCIAL)

    usuario = models.ForeignKey('Usuario',
                                verbose_name=('user'),
                                on_delete=models.CASCADE,
                                related_name="inscricoes",
                                blank=False, null=False)

    evento = models.ForeignKey('core.Evento',
                               default="")

    atividades = models.ManyToManyField('core.Atividade',
                                        through="ItemInscricao")

    trilhas = models.ManyToManyField('core.Trilha',
                                     through="core.TrilhaInscricao")


    class Meta:
        verbose_name = 'Id de Inscricao'
        verbose_name_plural = 'Id das Inscricoes'

    def get_atividades(self):
        atividades = self.evento.atividades.all()
        return atividades

    def add_item_inscricao(self):
        for atividade in self.get_atividades():
            item_inscricao = ItemInscricao()
            item_inscricao.inscricao = self
            item_inscricao.atividade = atividade
            item_inscricao.save()

   # def registro_checkin_inscricao(self):
   #     checkin_inscricao = CheckinItemInscricao()
   #     checkin_inscricao.gerente = self.evento.dono
   #     checkin_inscricao.save()


class CheckinItemInscricao(models.Model):
    data = models.DateField('Data de entrada', auto_now_add=True)
    hora = models.TimeField("Hora", blank=True, null=False, default="00:00")
    status = EnumField(StatusCheckIn, default=StatusCheckIn.NAO_VERIFICADO)

    gerente = models.ForeignKey("user.Usuario",
                                related_name="gerente_chekin",
                                default="")


class ItemInscricao(models.Model):
    inscricao = models.ForeignKey('Inscricao',
                                  blank=True, default="",
                                  related_name="itens")

    atividade = models.ForeignKey('core.Atividade',
                                  blank=True, default="")

    checkin = models.ForeignKey('CheckinItemInscricao',
                                default="" , null=True)