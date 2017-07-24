from django.db import models
from jacaEventos.jacaEventos.utils.EscolhaEnum import EscolhaEnum
from jacaEventos.jacaEventos.utils.models import Periodo

class Evento(models.Model):

    
    descricao = models.TextField('Descricao da atividade', blank=True)
    valor_da_atividade = models.DecimalField("Valor", max_digits=5, decimal_places=2)
    tipo_atividade = models.CharField(max_length=1, choices=EscolhaEnum.choices())
    atividades_diponiveis = models.ForeignKey('usuario.Inscricao', related_name='atividades_disponiveis', blank=True, null=True)
    atividades_evento = models.ForeignKey('core.Evento',verbose_name="Atividades", related_name="Atividades_do_evento")
    descricao = models.TextField('Descricao do evento', blank=True)
    periodo = models.OneToOneField(
        Periodo,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Evento(models.Model):

    meus_eventos = models.ForeignKey('usuario.Usuario', related_name='meus_eventos', blank=True, null=True)
    administrador_evento = models.ForeignKey('usuario.Usuario',verbose_name="Administrador")
    atividades_diponiveis = models.ForeignKey('usuario.Inscricao', related_name='atividades_disponiveis', blank=True,
                                              null=True)
    atividades_evento = models.ForeignKey('core.Evento', verbose_name="Atividades", related_name="Atividades_do_evento")

class Atividade(models.Model):


    descricao = models.TextField('Descricao da atividade', blank=True)
    periodo = models.OneToOneField(
        Periodo,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    valor_da_atividade = models.DecimalField("Valor", max_digits=5, decimal_places=2)
                                          

class Instituicao(models.Model):

    nome = models.CharField('Nome da instituiçao', max_length=30)
    tipo_de_relacionamento = models.TextField('tipo_de_relacionamento', blank=True)
    instituicao_relacionada = models.ForeignKey(Evento,verbosename="Instituicoes")


class Evento_Instituicao(models.Model):

    tipo_relacionamento = models.TextField('Tipo Relacionamento', blank=True)
    instituicao = models.ForeignKey(Instituicao)
    instituicao_relacionada = models.ForeignKey(Evento,verbose_name="Instituicoes", related_name="Instituicoes_relacionadas")

class Tag(models.Model):

    nome_tag = models.CharField('Tag', max_length=30)
    tag_evento = models.ForeignKey('core.Evento',verbose_name="tags_evento", related_name="tags_evento")
    tag_interesse = models.ForeignKey('usuario.Usuario',verbose_name="tags_interesse", related_name="tags_usuario")
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
