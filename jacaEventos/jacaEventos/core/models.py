from django.db import models
from jacaEventos.utils import EscolhaEnum

# Create your models here.
class Atividade(models.Model):

    descricao = models.TextField('Descricao da atividade', blank=True)
    valor_da_atividade = models.DecimalField("Valor", max_digits=5, decimal_places=2)
    tipo_atividade = models.CharField(max_length=1, choices=EscolhaEnum.choices())


# Classes de Enum referente ao core
# info:
# para receber o enum na classes adicionar a seguinte linha:
# <Varivel_tipo> = models.CharField(max_length=1, choices=EscolhaEnum.choices())

class StatusEvento(EscolhaEnum):
    inscricoes_abertas = 0
    incricoes_fechado = 1
    encerrado = 2
    andamento = 4

class TipoAtividade(EscolhaEnum):
    palestra = 0
    minicurso = 1
    workshop = 2
    mesa_redonda = 3


class TipoEvento(EscolhaEnum):
    congresso = 0
    semana = 1
    seminario = 2

###