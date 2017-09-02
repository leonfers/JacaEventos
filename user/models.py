import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from enumfields import Enum, EnumField
from utils.models import Observado
from user.enum import *
from django.db.models import Q
from core.models import *
from django.core.exceptions import ValidationError


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome do Usuário',
        max_length=30,
        unique=True,
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

    @property
    def inscrever(self):
        return Evento.objects.all().filter(~Q(dono=self.dono))


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

    def validate_periodo_inscricao(self):
        if self.evento.status != StatusEvento.INSCRICOES_ABERTAS:
            return ValidationError("Periodo de inscricoes ja encerrou")

    def clean(self):
        super(Inscricao, self).clean()
        self.validate_periodo_inscricao()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Inscricao, self).save()


class CheckinItemInscricao(models.Model):
    data = models.DateField('Data de entrada', auto_now_add=True)
    hora = models.TimeField("Hora", blank=True, null=False, default="00:00")
    gerente = models.ForeignKey("user.Usuario", related_name="gerente_chekin", default="")
    status = EnumField(StatusCheckIn, default=StatusCheckIn.NAO_VERIFICADO)

    gerente = models.ForeignKey("user.Usuario",
                                related_name="gerente_chekin",
                                default="")

    def validate_gerente_chekin(self):
        if self.status == StatusCheckIn.VERIFICADO and self.gerente == "":
            raise ValidationError('Gerente nao Informado')
        if self.status == StatusCheckIn.NAO_VERIFICADO and self.gerente != "":
            raise ValidationError('Status do Checkin nao foi alterado')

    def clean(self):
        super(CheckinItemInscricao, super).clean()
        self.validate_gerente_chekin()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(CheckinItemInscricao, self).save()


class ItemInscricao(models.Model):
    inscricao = models.ForeignKey('Inscricao',
                                  blank=True, default="",
                                  related_name="itens")

    atividade = models.ForeignKey('core.Atividade',
                                  blank=True, default="")

    checkin = models.ForeignKey('CheckinItemInscricao',
                                default="", null=True)

    def validate_atividade_existente(self):
        for atividade in self.inscricao.atividade.atividades:
            if atividade == self.atividade:
                raise ValidationError('Voce ja se inscreveu nessa atividade')

    def validate_atividade_evento(self):
        pass

    def validate_conflito_horario_atividade(self):
        pass

    def clean(self):
        super(ItemInscricao, self).clean()
        self.validate_atividade_existente()

    def save(self):
        self.full_clean()
        super(ItemInscricao, self).save()
