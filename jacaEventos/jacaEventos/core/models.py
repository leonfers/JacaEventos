from django.db import models

from jacaEventos.usuario.models import Usuario
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

    nome = models.CharField('nome', max_length=30, unique=True, blank=True)
    dono = models.ForeignKey('usuario.Usuario', verbose_name="dono", related_name='meus_eventos',blank=True,null=True)
    descricao = models.TextField('descricao', max_length=256, blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2)
    tipo_evento = models.CharField(max_length=1, choices=TipoEvento.choices(),blank=True)

    def __str__(self):
        return self.nome

class Atividade(models.Model):

    nome = models.CharField('nome', max_length=30, unique=True, blank=True)
    descricao = models.TextField('descricao da atividade', blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2,default=0)
    evento = models.ForeignKey('core.Evento', verbose_name="atividades", related_name="atividades",default="")


class Instituicao(models.Model):

    nome = models.CharField('nome', max_length=30)
    tipo_de_relacionamento = models.TextField('tipo', blank=True)
    instituicao_relacionada = models.ForeignKey('core.Evento')


class Evento_Instituicao(models.Model):

    tipo_relacionamento = models.TextField('tipo', blank=True)
    instituicao = models.ForeignKey(Instituicao)
    instituicao_relacionada = models.ForeignKey(Evento,verbose_name="Instituicoes", related_name="instituicoes_relacionadas")

class Tag(models.Model):
    nome = models.CharField('Tag', max_length=30)

    class Meta:
        ordering = ['nome']

    def __unicode__(self):
        return self.nome



class Tag_Usuario(models.Model):
    tag = models.ForeignKey(Tag, related_name='associacao')
    usuario = models.ForeignKey(Usuario, related_name='associcao')




#class Tag_Evento(models.Model):
    #tag = models.ForeignKey(Tag, blank=True, default="")
    #evento = models.ForeignKey(Evento, blank=True, default="")



# Classes de Enum referente ao core
# info:
# para receber o enum na classes adicionar a seguinte linha:
# <Varivel_tipo> = models.CharField(max_length=1, choices=EscolhaEnum.choices())

#Query set Evento.objects.filter(dono_id=1)
#Query set Evento.atividades_do_evento.get_queryset()