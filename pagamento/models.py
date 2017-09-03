from enumfields import Enum, EnumField
from django.db import models
from user.models import *
from core.models import *
from localflavor.br.br_states import STATE_CHOICES
import datetime
from django.core.exceptions import ValidationError
import random
import string

class StatusPagamento(Enum):
    PAGO = 'PAGO'
    NAO_PAGO = 'NAO_PAGO'


class StatusCupom(Enum):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'


class TipoCupom(Enum):
    SIMPLES = 'SIMPLES'
    AUTOMATICO = 'AUTOMATICO'


class Pagamento(models.Model):
    status = EnumField(StatusPagamento, default=StatusPagamento.NAO_PAGO, blank=False, null=False)
    usuario_recebimento = models.ForeignKey("user.Usuario" , related_name="recebido_usuario" , default="", blank=False, null=False)
    inscricao = models.ForeignKey("user.Inscricao" , related_name="de_incricao" , default="", blank=False, null=False)
    data = models.DateField('Data de entrada', auto_now_add=True, blank=False, null=False)
    hora = models.TimeField("Hora", blank=False, null=False)
    cupons = models.ManyToManyField('pagamento.Cupom', through="PagamentoCupom" , default="", blank=True)
    valor_pagamento = models.DecimalField("valor pagamento", max_digits=5, decimal_places=2, blank=False, null=False)

    def validar_pagamento(self):
        if self.valor_pagamento <= self.inscricao.evento.valor:
            raise ValidationError('Valor de pagamento insuficiente.')

    def invalidar_inscricao_enquanto_aguarda_pagamento(self):
        if self.status == StatusPagamento.NAO_PAGO and self.inscricao.evento.status == StatusEvento.ANDAMENTO:
            self.inscricao.status_inscricao = StatusInscricao.INATIVA

    def clean(self):
        super(Pagamento, self).clean()
        self.validar_pagamento()
        self.invalidar_inscricao_enquanto_aguarda_pagamento()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Pagamento, self).save()


    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.valor_pagamento;


class PagamentoCupom(models.Model):
    pagamento = models.ForeignKey("pagamento.Pagamento" , related_name="pagamento_cupom" , default="", blank=False, null=False)
    cupom = models.ForeignKey("pagamento.Cupom" , related_name="cupom_de_pagamento" , default="", blank=False, null=False)

    def validar_relacao_pagamento_cupom(self):
        if self.cupom.status == StatusCupom.INATIVO:
            raise ValidationError('O cupom nao esta disponivel para uso.')

    def validar_relacao_pagamento_cupom_quando_tipo_AUTOMATICO(self):
        if self.cupom.tipo == TipoCupom.AUTOMATICO:
            raise ValidationError('O cupom automatico nao pode se relacionar diretamente com o pagamento.')

    def avaliar_valor_pos_desconto(self):
        if self.pagamento != self.cupom.evento.valor:
            raise ValidationError('O valor pos desconto nao esta de acordo.')

    def clean(self):
        super(PagamentoCupom, self).clean()
        self.validar_relacao_pagamento_cupom()
        self.avaliar_valor_pos_desconto()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(PagamentoCupom, self).save()


class Cupom(models.Model):
    codigo_do_cupom =  models.CharField('cupom', max_length=100, blank=False, null=False) #Algoritmo que crie um
    porcentagem = models.DecimalField("porcentagem", max_digits=2, decimal_places=0 , default=0, blank=False, null=False)
    status = EnumField(StatusCupom, max_length=25, default=StatusCupom.ATIVO, blank=False, null=False)
    tipo = EnumField(TipoCupom, max_length=25, default=TipoCupom.SIMPLES, blank=False, null=False)
    evento = models.ForeignKey('core.Evento', related_name="cupom_do_evento" , default="", blank=False, null=False)
    periodo =  models.OneToOneField(
        'utils.Periodo',
        on_delete=models.CASCADE,
        primary_key=True, blank=False, null=False
        )

    def atualizar_valor_com_desconto(self):
        desconto = self.receberDesconto(self.evento.valor)
        self.evento.valor = self.evento.valor - desconto

    def gerar_codigo_cupom(self):
        caracters_validos = string.ascii_uppercase + string.digits
        faixa_char = 4
        num_divisoes = 3
        chave_cupom = ''
        for x in range(num_divisoes):
            chave_cupom += ''.join(random.choice(caracters_validos) for y in range(faixa_char))
            if x < num_divisoes - 1:
                chave_cupom += '-'
        return chave_cupom

    def validar_cupom(self):
        chave_cupom = self.gerar_codigo_cupom()
        self.codigo_do_cupom = chave_cupom
        if len(self.codigo_do_cupom) != 14:
            raise ValidationError('A chave utilizada nao e valida.')

    def usar_cupom_automatico(self):
        self.tipo = TipoCupom.AUTOMATICO
        self.evento.valor -= self.receberDesconto(self.evento.valor)

    def clean(self):
        super(Cupom, self).clean()
        self.validar_cupom()
        self.atualizar_valor_com_desconto()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Cupom, self).save()


    class Meta:
        verbose_name = 'Cupom'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.Cupons

    def receberDesconto(self, valor):
        return valor*self.porcentagem