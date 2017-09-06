from enumfields import Enum, EnumField
from django.db import models
from user.models import *
from core.models import *
from localflavor.br.br_states import STATE_CHOICES
import datetime
from django.core.exceptions import ValidationError
import random
import string
from pagamento.enum import *
from django.core.exceptions import ObjectDoesNotExist


class Pagamento(models.Model):
    status = EnumField(StatusPagamento, default=StatusPagamento.NAO_PAGO, blank=False, null=False)
    usuario_recebimento = models.ForeignKey("user.Usuario", related_name="recebido_usuario", default="", blank=False,
                                            null=False)
    data = models.DateField("Data de entrada", auto_now_add=True, blank=False, null=False)
    hora = models.TimeField("Hora", blank=False, null=False)
    valor = models.DecimalField("valor pagamento", max_digits=8, decimal_places=2, blank=False, null=False)

    inscricao = models.OneToOneField("user.Inscricao",
                                  related_name="de_incricao",
                                  default="", blank=False, null=False)

    cupom_codigo = models.CharField("cupom", max_length=100, blank=True, null=True)

    def validar_cupom(self):
        try:
            self.inscricao.evento.cupom_do_evento.filter(status="ATIVO").get(codigo=self.cupom_codigo)
        except ObjectDoesNotExist:
            self.cupom_codigo = None
            raise ValidationError("Não existe nenhum cupom para esse evento ou o cupom informado nao é valido.")

    def invalidar_inscricao_enquanto_aguarda_pagamento(self):
        
        if self.status == StatusPagamento.NAO_PAGO and self.inscricao.evento.status == StatusEvento.ANDAMENTO:
            self.inscricao.status_inscricao = StatusInscricao.INATIVA

    def cupom_evento(self):
        try:
            cupom = self.inscricao.evento.cupom_do_evento.filter(status="ATIVO").get(codigo=self.cupom_codigo)
            return cupom
        except ObjectDoesNotExist:
            raise ValidationError("Voce nao possue nenhum cupom")

    def atualizar_valor(self):
        try:
            if self.cupom_evento().codigo == self.cupom_codigo:
                cupom = self.cupom_evento()
                valor = valor_pagamento = cupom.porcentagem * 100 / self.inscricao.evento.valor
                total = self.inscricao.evento.valor
                self.valor = float(total - valor)
        except ZeroDivisionError:
            self.valor = self.inscricao.evento.valor

    def clean(self):
        super(Pagamento, self).clean()
        # self.validar_pagamento()
        self.validar_cupom()
        self.invalidar_inscricao_enquanto_aguarda_pagamento()

    def save(self, *args, **kwargs):
        self.valor = self.inscricao.evento.valor
        self.data = datetime.date.today()
        self.hora = datetime.datetime.now().time()
        self.status = StatusPagamento.PAGO
        self.full_clean()
        self.atualizar_valor()
        super(Pagamento, self).save()


class Cupom(models.Model):
    codigo = models.CharField("cupom", max_length=100, blank=False, null=False, unique=True)
    porcentagem = models.DecimalField("porcentagem", max_digits=2, decimal_places=0, default=0, blank=False, null=False)
    status = EnumField(StatusCupom, max_length=25, default=StatusCupom.ATIVO, blank=False, null=False)
    tipo = EnumField(TipoCupom, max_length=25, default=TipoCupom.SIMPLES, blank=False, null=False)

    evento = models.ForeignKey("core.Evento",
                               related_name="cupom_do_evento",
                               default="", blank=False, null=False)

    periodo = models.OneToOneField("utils.Periodo",
                                   on_delete=models.CASCADE,
                                   primary_key=True, blank=False,
                                   null=False)


    def gerar_codigo_cupom(self):
        caracters_validos = string.ascii_uppercase + string.digits
        faixa_char = 4
        num_divisoes = 3
        chave_cupom = ""
        for x in range(num_divisoes):
            chave_cupom += """""".join(random.choice(caracters_validos) for y in range(faixa_char))
            if x < num_divisoes - 1:
                chave_cupom += "-"
        return chave_cupom


    def save(self, *args, **kwargs):
        self.codigo = self.gerar_codigo_cupom()
        self.periodo = self.evento.periodo
        self.full_clean()
        super(Cupom, self).save()

    class Meta:
        verbose_name = "Cupom"
        verbose_name_plural = "Pagamentos"

    def __str__(self):
        return self.codigo
