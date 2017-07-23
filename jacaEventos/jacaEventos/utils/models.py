from django.db import models

# Create your models here.
class Periodo(models.Model):

    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    data_fim = models.DateField("Data fim", blank=True, null=False)
