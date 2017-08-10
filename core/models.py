from django.db import models
from user.models import Usuario
from utils.EscolhaEnum import EscolhaEnum
from enumfields import EnumField
from enumfields import Enum
from abc import ABCMeta

############ Enums###############
from utils.models import Horario, Endereco


class StatusEvento(Enum):
    INSCRICOES_ABERTAS = 'inscricoes_abertas'
    INSCRICOES_FECHADAS = 'incricoes_fechado'
    ENCERRADO = 'encerrado'
    ANDAMENTO = 'andamento'


class TipoAtividade(EscolhaEnum):
    PALESTRA = 'palestra'
    MINICURSO = 'minicurso'
    WORKSHOP = 'workshop'
    MESA_REDONDA = 'mesa_redonda'
    PADRAO = 'padrao'


class TipoEvento(Enum):
    CONGRESSO = 'congresso'
    SEMANA = 'semana'
    SEMINARIO = 'seminario'
    PADRAO = 'padrao'

class TipoInstituicao(Enum):
    APOIO = 'apoio'
    PATROCINIO = 'patrocinio'
    REALIZACAO = 'realizacao'
    PADRAO = 'padrao'

class CategoriaAtividade(Enum):
    LOCAL = 'local'
    SATELITE = 'satelite'

class TipoResponsavel(Enum):
    PALESTRANTE = 'palestrantes'
    PROFESSOR = 'professor'
    STAFF = 'staff'
    PADRAO = 'padrao'

class StatusAtividade(Enum):
    ATIVA = 'ativa'
    INATIVA = 'inativa'



class TipoEspacoFisico(Enum):
    SALA = 'sala'
    LABORATORIO = 'laboratorio'
    AUDITORIO = 'auditorio'
    PREDIO = 'predio'
    AR_LIVRE = 'ar_livre'
    PADRAO = 'padrao'

class TipoGerencia(Enum):
    DONO = 'dono'
    STAFF = 'staff'
    PADRAO = 'padrao'


#####################################
class Evento(models.Model):
    nome = models.CharField('nome', max_length=30, unique=True, blank=True)
    descricao = models.TextField('descricao', max_length=256, blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2, default=0)
    tipo_evento = EnumField(TipoEvento,default=TipoEvento.PADRAO)
    endereco = models.ForeignKey('utils.Endereco' , related_name="endereco_do_evento")
    periodo = models.ForeignKey('utils.periodo' , related_name="periodo_do_evento")
    dono = models.ForeignKey(
        'user.Usuario',
        verbose_name="dono",
        related_name='meus_eventos',
        blank=True, null=True)

    gerentes = models.ManyToManyField(
      'user.Usuario',
      related_name="gerentes_do_evento",
      through="GerenciaEvento")

    tags_do_evento = models.ManyToManyField(
        'core.Tag',
        through="core.Tag_Evento",
        related_name='tags_do_evento')


    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nome

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
        return EventoInstituicao.objects.all().filter(evento_relacionado = self)

    def get_valor(self):
        valor = 0
        atividades = self.get_atividades()
        for i in range(len(atividades)):
            valor += atividades[i].valor
        return valor

    def add_instituicao(self,instituicao,tipo_relacionamento):
        try:
            self.save()
            instituicao.save()

            evento_instituicao = EventoInstituicao()
            evento_instituicao.tipo_relacionamento = tipo_relacionamento
            evento_instituicao.evento_relacionado = self
            evento_instituicao.instituicao = instituicao

            evento_instituicao.save()
            return True

        except Exception as e:
            print("Falha ao adicionar Instituicao ")
            return False

class EventoSatelite():
    eventos = models.ForeignKey("core.Evento", related_name="evento_satelite" , default="")


class Atividade(models.Model):
    nome = models.CharField('nome', max_length=30, unique=True, blank=True)
    descricao = models.TextField('descricao da atividade', blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2,default=0)
    evento = models.ForeignKey('core.Evento', verbose_name="atividades", related_name="atividades" ,default="")
    periodo = models.ForeignKey('utils.Periodo',
                                verbose_name="periodo",
                                related_name="periodo",
                                default="")
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.nome

class AtividadeSimples(Atividade):
    horario = models.ForeignKey('utils.Horario' ,related_name="horario_atividade_simples")

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


class AtividadeAdministrativa(Atividade):

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


class Trilha(models.Model):

    nome = models.CharField('nome', max_length= 40)
    valor = models.DecimalField('valor', max_digits=5, decimal_places=2, default=0)
    evento = models.ForeignKey('core.Evento' ,
                               related_name="evento_trilha",
                               verbose_name="evento")
    responsaveis = models.ManyToManyField(
        'user.Usuario',
        through="ResponsavelTrilha",
        related_name="responsavel_trilha")
    class meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'

class TrilhaInscricao(models.Model):

    trilha = models.ForeignKey('core.Trilha' ,
                               related_name="trilha_Inscricao",
                               verbose_name="trilha_inscricao")
    inscricao = models.ForeignKey('user.Inscricao',
                               related_name="inscricao_trilha_Inscricao",
                               verbose_name="trilha_incricao")


class ResponsavelTrilha(models.Model):
    responsavel = models.ForeignKey("user.Usuario",
                                    related_name="usuario_responsavel_trilha",
                                    default="")
    trilha = models.ForeignKey("core.Trilha",
                                  related_name="trilha_dirigida",
                                  default="")
    tipo_responsavel_trilha = models.CharField(max_length=30)




class GerenciaEvento(models.Model):
    gerente = models.ForeignKey("user.Usuario" ,
                                related_name="usuario_gerente" ,
                                default="")
    evento = models.ForeignKey("core.Evento",
                                related_name="evento_gerente",
                                default="")
    tipo_gerente = EnumField(TipoGerencia, max_length=25, default=TipoGerencia.PADRAO)

class ResponsavelAtividade(models.Model):
    responsavel = models.CharField('nome', max_length=30, unique=True, blank=True)
    descricao = models.CharField('descricao', max_length=500, unique=True, blank=True)
    atividade = models.ForeignKey("core.Atividade",
                                related_name="atividade_dirigida",
                                default="")
    tipo_responsavel = models.CharField(max_length=1, choices=EscolhaEnum.choices())

class Instituicao(models.Model):
    nome = models.CharField('nome', max_length=30 , default="")
    class Meta:
        verbose_name = 'Instituicao'
        verbose_name_plural = 'Instituicoes'

    def __str__(self):
        return self.nome


class EventoInstituicao(models.Model):
    tipo_relacionamento = EnumField(TipoInstituicao, default=TipoInstituicao.PADRAO)

    instituicao = models.ForeignKey('core.Instituicao',verbose_name="Evento",
                                    related_name="evento_instituicao",
                                    default="")

    evento_relacionado = models.ForeignKey(Evento,
        verbose_name="Evento",
        related_name="evento_relacionado",
        default="")

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


class EspacoFisico(models.Model):
    nome = models.TextField('nome', max_length=30 , default="")
    tipoEspacoFisico = EnumField(TipoEspacoFisico , default=TipoEspacoFisico.PADRAO)
    capacidade = models.DecimalField("capacidade", max_digits=5, decimal_places=0 ,default=0)
    evento = models.ForeignKey("core.Evento",related_name="espaco_do_evento", default="")
    atividade = models.ForeignKey("core.Atividade",related_name="espaco_da_atividade", default="")


