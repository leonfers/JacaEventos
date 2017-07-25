from django.db import models
from jacaEventos.utils.EscolhaEnum import EscolhaEnum

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

class Evento(models.Model):

    nome_do_evento = models.CharField('Nome do Evento', max_length=30, unique=True, blank=True)
    dono = models.ForeignKey('usuario.Usuario', verbose_name="Dono", related_name='meus_eventos',blank=True,null=True)
    descricao = models.TextField('Descricao do evento', max_length=256, blank=True)
    tipo_evento = models.CharField(max_length=1, choices=TipoEvento.choices(),blank=True)

class Atividade(models.Model):

    nome_doa_atividade = models.CharField('Nome da Atividade', max_length=30, unique=True, blank=True)
    descricao = models.TextField('Descricao da atividade', blank=True)
    periodo = models.OneToOneField(
        'utils.Periodo',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    valor_da_atividade = models.DecimalField("Valor", max_digits=5, decimal_places=2)
    atividades_evento = models.ForeignKey('core.Evento', verbose_name="Atividades", related_name="Atividades_do_evento")

                                          

class Instituicao(models.Model):

    nome = models.CharField('Nome da instituiçao', max_length=30)
    tipo_de_relacionamento = models.TextField('tipo_de_relacionamento', blank=True)
    instituicao_relacionada = models.ForeignKey('core.Evento')


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

#Query set Evento.objects.filter(dono_id=1)