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

class Instituicao(models.Model):

    tipo_de_relacionamento = models.TextField('Nome da instituicao', blank=True)
    instituicao_relacionada = models.ForeignKey(Evento,verbose_name="Instituicoes_")


class Evento_Instituicao(models.Model):

    tipo_relacionamento = models.TextField('Tipo Relacionamento', blank=True)
    instituicao = models.ForeignKey(Instituicao)
    instituicao_relacionada = models.ForeignKey(Evento,verbose_name="Instituicoes", related_name="Instituicoes_relacionadas")


