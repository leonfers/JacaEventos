from django.db import models
from jacaEventos.utils.models import Periodo


# Create your models here.
class Atividade(models.Model):

    descricao = models.TextField('Descricao da atividade', blank=True)
    valor_da_atividade = models.DecimalField("Valor", max_digits=5, decimal_places=2)

class Evento(models.Model):

    descricao = models.TextField('Descricao do evento', blank=True)
    periodo = models.OneToOneField(
        Periodo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    meus_eventos = models.ForeignKey('usuario.Usuario', related_name='meus_eventos', blank=True, null=True)
    administrador_evento = models.ForeignKey('usuario.Usuario',verbose_name="Administrador")
