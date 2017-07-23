from django.db import models

# Create your models here.
class Atividade(models.Model):

    descricao = models.TextField('Descricao da atividade', blank=True)
    valor_da_atividade = models.DecimalField("Valor", max_digits=5, decimal_places=2)
