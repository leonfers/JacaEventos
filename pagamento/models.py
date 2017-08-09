from django.db import models
# Create your models here.
from enumfields import Enum, EnumField


class StatusPagamento(Enum):
    PAGO = 'PAGO'
    NAO_PAGO = 'NAO_PAGO'

class StatusCupom(Enum):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'

class TipoCupom(Enum):
    SIMPLES = 'SIMPLES'
    AUTOMATICO = 'AUTOMATICO'

############################################################

class Pagamento(models.Model):
    status = EnumField(StatusPagamento, max_length=25, default=StatusPagamento.NAO_PAGO)
    usuario_recebimento = models.ForeignKey("user.Usuario" , related_name="recebido_usuario" , default="")
    inscricao = models.ForeignKey("user.Inscricao" , related_name="de_incricao" , default="")
    periodo = models.OneToOneField(
        'utils.Periodo',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cupons = models.ManyToManyField('pagamento.Cupom', through="PagamentoCupon" , default="")
    valor_pagamento = models.DecimalField("valor pagamento", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'


    def __str__(self):
        return self.valor_pagamento;

class PagamentoCupon(models.Model):
    pagamento = models.ForeignKey("pagamento.Pagamento" , related_name="pagamento_cupon" , default="")
    cupon = models.ForeignKey("pagamento.Cupom" , related_name="cupon_de_pagamento" , default="")

class Cupom(models.Model):
    codigo_do_cupom =  models.CharField('cupom', max_length=100, blank=True)
    porcentage = models.DecimalField("porcentagem_desconto", max_digits=2, decimal_places=2)
    status = EnumField(StatusCupom, max_length=25, default=StatusCupom.ATIVO)
    tipo = EnumField(TipoCupom, max_length=25, default=TipoCupom.SIMPLES)
    periodo =  models.OneToOneField(
        'utils.Periodo',
        on_delete=models.CASCADE,
        primary_key=True,
        )
    lista_de_cupons = models.ForeignKey('core.Evento', related_name='meus_cupons', blank=True, null=True)

    class Meta:
        verbose_name = 'Cupom'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.Cupons

    def receberDesconto(self, valor):
        return valor*self.porcentagem

