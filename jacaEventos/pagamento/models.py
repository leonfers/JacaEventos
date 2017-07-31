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


class Cupom(models.Model):

    codigo_do_cupom =  models.CharField('cupom', max_length=100, blank=True)
    periodo =  models.OneToOneField(
        'utils.Periodo',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    lista_de_cupons = models.ForeignKey('core.Evento', related_name='meus_cupons', blank=True, null=True)
