from django.db import models
from jacaEventos.utils.models import Periodo
# Create your models here.
class Pagamento(models.Model):

    status_pagamento = models.BooleanField('Pago/Não Pago', blank=True, default=True)
    periodo = models.OneToOneField(
        Periodo,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Cupom(models.Model):

    codigo_do_cupom =  models.CharField('cupom', max_length=100, blank=True)
    periodo =  models.OneToOneField(
        Periodo,
        on_delete=models.CASCADE,
        primary_key=True,
    )