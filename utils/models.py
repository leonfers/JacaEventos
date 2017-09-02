from django.db import models
from localflavor.br.br_states import STATE_CHOICES
import datetime
from django.core.exceptions import ValidationError
from django.core import validators
import re


class Periodo(models.Model):
    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    data_fim = models.DateField("Data fim", blank=True, null=False)

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'

    def validate_periodo(self):
        if self.data_inicio < datetime.date.today():
            raise ValidationError('Periodo tem que ser maior que a data atual')
        if self.data_fim < self.data_inicio:
            raise ValidationError('Data final tem que ser maior ou igual a data inicial')

    def clean(self):
        super(Periodo, self).clean()
        self.validate_periodo()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Periodo, self).save()

    def str(self):
        return self.data_inicio.str() + " para " + self.data_fim.str()


class Endereco(models.Model):
    pais = models.TextField(blank=False, null=False)
    cidade = models.TextField(blank=False, null=False)
    bairro = models.TextField(blank=False, null=False)
    logradouro = models.TextField(blank=True, null=False)
    numero = models.TextField(blank=False, null=False)
    cep = models.CharField(max_length=9, blank=False, validators=[
        validators.RegexValidator(re.compile(r'^\d{8}$|^\d{5}-\d{3}$'),
                                  message='Informe um cep valido no formato 88888888 ou 88888-888', code='invalid')])
    estado = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = 'Endereco'
        verbose_name_plural = 'Enderecos'

    def str(self):
        return self.pais

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Endereco, self).save()


class Horario(models.Model):
    data = models.DateField("Data inicio", blank=True, null=True)
    hora_inicio = models.TimeField("Hora inicio", blank=True, null=False)
    hora_fim = models.TimeField("Hora Fim", blank=True, null=False)

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horario'

    def str(self):
        return self.hora_inicio.str() + "  para  " + self.hora_fim.str()


class HorarioAtividadeContinua(Horario):
    atividade = models.ForeignKey("core.AtividadeContinua",
                                  verbose_name="Atividade",
                                  related_name="Atividade",
                                  default="")

    class Meta:
        verbose_name = 'Horario_da_atividdade'
        verbose_name_plural = 'Horarios_da_ativiade '


class Observador(models.Model):
    observado = models.ForeignKey("utils.Observador",
                                  verbose_name='Observador',
                                  related_name='Observador',
                                  default="")

    def atualizar(self):
        return "sobrescreva"


class Notificador(Observador):
    class Meta:
        verbose_name = 'Notificador'
        verbose_name_plural = 'notificadores '

    def atualizar(self, msg):
        "enviar email para usuarios da atividade"
        return true


class Observado(models.Model):
    def addObservador(self, observador):
        observador.observado = self
        return true

    def removeObservador(self, observador):
        observador.observado = null
        return true

    def notificar(self, msg):
        for observador in self.Observador:
            observador.atualizar(msg)


class MsgFactory():
    def gerar_msg_simples(self, atributo):
        msg = MsgSimples()
        msg.atual = String(atributo)
        return msg

    def gerar_msg_completa(self, atributo):
        msg = MsgCompleta()
        msg.atual = String(atributo)
        msg.data = datetime.now()
        return msg


class MsgSimples(models.Model):
    atual = models.TextField(default="")

    def str(self):
        return "novo " + self.atual + "."


class MsgCompleta(MsgSimples):
    data = models.DateTimeField(null=False)
    anterior = models.TextField(default="")

    def str(self):
        return "Data :" + self.data + " Estado antigo :" + self.anterior + " Estado atual :" + self.atual + "."
