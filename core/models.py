from django.db import models
from user.models import Usuario
from utils.EscolhaEnum import EscolhaEnum
from abc import ABCMeta

############ Enums###############
from utils.models import Horario


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


class CategoriaAtividade(EscolhaEnum):
    LOCAL = 0
    SATELITE = 1

class TipoResponsavelAtividade(EscolhaEnum):
    palestrantes = 0
    professor = 1
    staff = 3

class StatusAtividade(EscolhaEnum):
    ativa = 0
    inativa = 1

class TipoEspacoFisico(EscolhaEnum):
    sala = 0
    laboratorio = 1
    auditorio = 2
    predio = 3
    ar_livre = 4

class TipoGerenciaEvento(EscolhaEnum):
    dono = 0
    staff = 1


#####################################
class Evento(models.Model):
    nome = models.CharField('nome', max_length=30, unique=True, blank=True)
    dono = models.ForeignKey(
        'user.Usuario',
        verbose_name="dono",
        related_name='meus_eventos',
        blank=True, null=True)
    gerentes = models.ManyToManyField('core.GerenciaEvento' , related_name="gerentes_do_evento")
    descricao = models.TextField('descricao', max_length=256, blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2)
    tipo_evento = models.CharField(max_length=1, choices=TipoEvento.choices() ,blank=True)

    tags_do_evento = models.ManyToManyField(
        'core.Tag',
        through="core.Tag_Evento",
        related_name='tags_do_evento')

    eventos_satelite = models.ManyToManyField(
        'core.Evento',
        related_name='evento_satelite')


    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nome

    def get_tipo(self):
        tipo = int(self.tipo_evento)
        return TipoEvento(tipo).name()

    def get_dono(self):
        return self.dono.nome

    def get_atividades(self):
        return self.atividades.all()

    def add_atividade(self,atividade):
        try:
            self.save()
            atividade.evento = self
            atividade.save()
            return True

        except Exception as e:
            print("Falha ao adicionar atividade")
            return False

    def get_tags(self):
        return self.tags_do_evento.all()

    def add_tag(self,tag):
        try:
            self.save()
            tag.save()
            tag_evento = Tag_Evento()
            tag_evento.tag = tag
            tag_evento.evento = self
            tag_evento.save()
            return True

        except Exception as e:
            print("Falha ao adicionar TAG ")
            return False

    def get_instituicoes(self):
        return Evento_Instituicao.objects.all().filter(evento_relacionado = self)

    def add_instituicao(self,instituicao,tipo_relacionamento):
        try:
            self.save()
            instituicao.save()

            evento_instituicao = Evento_Instituicao()
            evento_instituicao.tipo_relacionamento = tipo_relacionamento
            evento_instituicao.evento_relacionado = self
            evento_instituicao.instituicao = instituicao

            evento_instituicao.save()
            return True

        except Exception as e:
            print("Falha ao adicionar Instituicao ")
            return False


class Atividade(models.Model):
    nome = models.CharField('nome', max_length=30, unique=True, blank=True)
    descricao = models.TextField('descricao da atividade', blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2,default=0)
    evento = models.ForeignKey('core.Evento', verbose_name="atividades", related_name="atividades")

    trilha = models.ManyToManyField("core.Trilha" ,
                                    related_name="trilha",
                                    verbose_name="trilha")


    periodo = models.ForeignKey('utils.Periodo',
                                verbose_name="periodo",
                                related_name="periodo",
                                default="")
    class Meta:
        #abstract = True
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.nome

'''
class AtividadeSimples(Atividade):

    class Meta:
        verbose_name = 'AtividadeSimples'
        verbose_name_plural = 'Atividades Simples'

class AtividadeContinua(Atividade):

    class Meta:
        verbose_name = 'AtividadeContinua'
        verbose_name_plural = 'AtividadesContinuas'

    def add_horario(self , horario):
        self.save()
        horario.atividade = self


class AtividadeNeutra(Atividade):

    valor = 0

    class Meta:
        verbose_name = 'AtividadeNeutra'
        verbose_name_plural = 'AtividadesNeutra'

    def add_horario(self , horario):
        self.save()
        horario.atividade = self

    def __setattr__(self, valor):
        if hasattr(self, valor):
            raise Exception("Esta atividade e obrigatoriamente gratuita")

        self.__dict__[valor] = 0
'''


class Trilha(models.Model):

    nome = models.CharField('nome', max_length= 40)
    valor = models.DecimalField('valor', max_digits=5, decimal_places=2, default=0)
    evento = models.ForeignKey('core.Evento' ,
                               related_name="evento_trilha",
                               verbose_name="evento")
    class meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'


class GerenciaEvento(models.Model):
    gerente = models.ForeignKey("user.Usuario" ,
                                related_name="usuario_gerente" ,
                                default="")
    evento = models.ForeignKey("user.Evento",
                                related_name="evento_gerente",
                                default="")
    tipo_gerente = models.CharField(max_length=1, choices=EscolhaEnum.choices())


class Instituicao(models.Model):
    nome = models.CharField('nome', max_length=30 , default="")
    class Meta:
        verbose_name = 'Instituicao'
        verbose_name_plural = 'Instituicoes'

    def __str__(self):
        return self.nome


class Evento_Instituicao(models.Model):
    tipo_relacionamento = models.CharField('tipo', max_length=40 , default="")

    instituicao = models.ForeignKey('core.Instituicao',verbose_name="Evento",
                                    related_name="evento_instituicao",
                                    default="")
    evento_relacionado = models.ForeignKey(Evento,
        verbose_name="Evento",
        related_name="evento_relacionado",
        default=0)

    class Meta:
        verbose_name = 'Relacionamento_Instituicao_Evento'
        verbose_name_plural = 'Relacionamentos_Instituicao_Evento'

    def __str__(self):
        return self.instituicao.__str__()


class Tag(models.Model):
    nome = models.CharField('Tag', max_length=30)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.nome


class Tag_Usuario(models.Model):
    tag = models.ForeignKey(Tag, related_name='tag_de_usuario', default="")
    usuario = models.ForeignKey(Usuario, related_name='tag_de_usuario' , default="")

    class Meta:
        verbose_name = 'Relacionamento_Tag_Usuario'
        verbose_name_plural = 'Relacionamentos_Tag_Usuario'

    def __str__(self):
        return self.tag.__str__() + self.usuario.__str__()


class Tag_Evento(models.Model):
    tag = models.ForeignKey(Tag, related_name='tag_de_evento', default="")
    evento = models.ForeignKey(Evento, related_name='tag_de_evento', default="")

    class Meta:
        verbose_name = 'Relacionamento_Tag_Evento'
        verbose_name_plural = 'Relacionamentos_Tag_Tag'

    def __str__(self):
        return (" relacionamento : " + self.tag.nome() + self.evento.nome())


# Classes de Enum referente ao core
# info:
# para receber o enum na classes adicionar a seguinte linha:
# <Varivel_tipo> = models.CharField(max_length=1, choices=EscolhaEnum.choices())

#Query set Evento.objects.filter(dono_id=1)
#Query set Evento.atividades_do_evento.get_queryset()