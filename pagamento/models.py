from django.db import models
# Create your models here.


class Pagamento(models.Model):
    status_pagamento = models.BooleanField('Pago/Não Pago', blank=True, default=True)
    periodo = models.OneToOneField(
        'utils.Periodo',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    valor_pagamento = models.DecimalField("valor pagamento", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'


    def __str__(self):
        return self.valor_pagamento;


class Cupom(models.Model):
    codigo_do_cupom =  models.CharField('cupom', max_length=100, blank=True)
    porcentage = models.DecimalField("porcentagem_desconto", max_digits=2, decimal_places=2)
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

