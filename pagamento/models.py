from enumfields import Enum, EnumField
from django.db import models
from pagamento.enum import *


class Pagamento(models.Model):
    status = EnumField(StatusPagamento, default=StatusPagamento.NAO_PAGO)
    data = models.DateField('Data de entrada', auto_now_add=True)
    hora = models.TimeField("Hora", blank=True, null=False)
    valor_pagamento = models.DecimalField("valor pagamento", max_digits=5, decimal_places=2)

    inscricao = models.ForeignKey("user.Inscricao",
                                  related_name="de_incricao",
                                  default="")

    usuario_recebimento = models.ForeignKey("user.Usuario",
                                            related_name="recebido_usuario",
                                            default="")

    cupons = models.ManyToManyField('pagamento.Cupom',
                                    through="PagamentoCupom" ,
                                    default="")

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.valor_pagamento;


class PagamentoCupom(models.Model):
    pagamento = models.ForeignKey("pagamento.Pagamento" ,
                                  related_name="pagamento_cupom" ,
                                  default="")

    cupom = models.ForeignKey("pagamento.Cupom",
                              related_name="cupom_de_pagamento" ,
                              default="")


class Cupom(models.Model):
    codigo_do_cupom =  models.CharField('cupom', max_length=100, blank=True)
    porcentagem = models.DecimalField("porcentagem", max_digits=2, decimal_places=0 , default=0)
    status = EnumField(StatusCupom, max_length=25, default=StatusCupom.ATIVO)
    tipo = EnumField(TipoCupom, max_length=25, default=TipoCupom.SIMPLES)

    evento = models.ForeignKey('core.Evento',
                               related_name="cupom_do_evento" ,
                               default="")

    periodo =  models.OneToOneField('utils.Periodo',
                                    on_delete=models.CASCADE,
                                    primary_key=True)


    class Meta:
        verbose_name = 'Cupom'
        verbose_name_plural = 'Pagamentos'

    def __str__(self):
        return self.Cupons

    def receberDesconto(self, valor):
        return valor*self.porcentagem