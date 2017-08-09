from django import core
from django.db import models
import re
from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from enumfields import Enum, EnumField

from utils.EscolhaEnum import EscolhaEnum


class TipoResponsavelAtividade(Enum):
    NAO_VERIFICADO = 'nao_verificado'
    PRESENTE = 'presente'
    AUSENTE = 'ausente'

class StatusInscricao(Enum):
    ATIVA = 'ativa'
    INATIVA = 'INATIVA'

#####################################


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome do Usuário',
        max_length=30,
        unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
        'O nome do user so pode conter letras, digitos ou os''seguintes caracteres @/./+/-/_''invalid'
                                              )])

    email = models.EmailField('E-mail', unique=True)
    nome = models.CharField('Nome', max_length=100, blank=True)
    data_de_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)
    objects = UserManager()

    tags = models.ManyToManyField(
        'core.Tag',
        through="core.Tag_Usuario",
        related_name='tags_do_usuario'
    )

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
        return self.nome

    def get_inscricoes(self):
        return self.inscricoes.all()
    
    def get_eventos(self):
        return self.meus_eventos.all()


class Inscricao(models.Model):
    status_inscricao = EnumField("user.StatusInscricao", related_name="status_inscricao" , default="")
    usuario = models.ForeignKey(
        'Usuario',
        verbose_name=('user'),
        on_delete=models.CASCADE,
        related_name="inscricoes",
        blank=False,
        null=False
    )
    evento = models.ForeignKey('core.Evento', default="")

    atividades = models.ManyToManyField('core.Atividade', through="ItemInscricao")
    trilhas = models.ManyToManyField('core.Trilha', through="TrilhaInscricao")

    class Meta:
        verbose_name = 'Id de Inscricao'
        verbose_name_plural = 'Id das Inscricoes'

    def get_atividades(self):
        atividades = self.evento.atividades.all()
        return atividades

    def add_item_inscricao(self, id ):
        self.save()
        item_inscricao = ItemInscricao()
        item_inscricao.inscricao = self
        item_inscricao.atividade = self.get_atividades()[id]
        item_inscricao.save()

class CheckinAtividadeInscricao():
    horario = models.OneToOneField("utils.Horario", related_name="horario_checkin" , default="", on_delete="CASCADE")
    gerente = models.ForeignKey("user.Usuario", related_name="gerente_chekin" , default="")
    status = EnumField("user.StatusCheckIn", related_name="status_checkin" , default="")
    atividade = models.ForeignKey("core.Atividade" , related_name="checkin_atividade" ,default="")


class ItemInscricao(models.Model):
    inscricao = models.ForeignKey('Inscricao', blank=True, default="",related_name="itens")
    atividade = models.ForeignKey('core.Atividade', blank=True, default="")

class ResponsavelTrilha:
    titulo = models.CharField('Titulo', blank=True, default="")
    usuario = models.ForeignKey('user.Usuario',
                                verbose_name="usuario",
                                related_name="usuario")
    trilha = models.ForeignKey('Trilha', verbose_name="trilha" , related_name="trilha")

    class Meta:
        unique_together = ('atividade','inscricao',)
