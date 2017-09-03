from django.db import models
from user.models import Usuario
from utils.EscolhaEnum import EscolhaEnum
from enumfields import EnumField
from enumfields import Enum
from polymorphic.models import PolymorphicModel
from utils.models import Horario, Endereco, Observado
from core.enum import *
import datetime
from django.core.exceptions import ValidationError


class Evento(models.Model):
    nome = models.CharField('nome', max_length=30, unique=True, blank=False)
    descricao = models.TextField('descricao', max_length=256, blank=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2, default=0)
    tipo_evento = EnumField(TipoEvento, default=TipoEvento.PADRAO)
    data_criacao = models.DateTimeField('Data de entrada', auto_now_add=True, )
    status = EnumField(StatusEvento, default=StatusEvento.INSCRICOES_ABERTAS, max_length=19)

    endereco = models.ForeignKey('utils.Endereco',
                                 related_name="endereco_do_evento")

    periodo = models.ForeignKey('utils.periodo',
                                related_name="periodo_do_evento")

    periodo_de_inscricao = models.ForeignKey('utils.periodo',
                                             related_name="inscricoes_evento",
                                             blank=True, null=True)

    dono = models.ForeignKey('user.Usuario', verbose_name="dono",
                             related_name='meus_eventos',
                             blank=False, null=False)

    gerentes = models.ManyToManyField('user.Usuario',
                                      related_name="gerentes_do_evento",
                                      through="GerenciaEvento")

    tags_do_evento = models.ManyToManyField('core.Tag',
                                            through="core.Tag_Evento",
                                            related_name='tags_do_evento')

    @property
    def atividades(self):
        return Atividade.objects.all()

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return self.nome

    def get_dono(self):
        return self.dono.nome

    def get_atividades(self):
        return self.atividades.all()

    def get_agenda(self):
        data = datetime.date.today()
        tamanho = len(self.atividades)
        dict = {}
        for i in range(tamanho):
            for j in range(len(self.atividades[i].horarioAtividade.get_dias_atividade())):
                if data == self.atividades[i].horarioAtividade.get_dias_atividade()[str(j)]:
                    dict[str(i)] = self.atividades[i].horarioAtividade.hora_inicio
        return dict

    def add_atividade(self, atividade):
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

    def get_gerentes(self):
        return self.gerentes.all()

    def add_tag(self, tag):
        try:

            tag_evento = Tag_Evento()
            tag_evento.tag = tag
            tag_evento.evento = self
            tag_evento.save()
            return True

        except Exception as e:
            print("Falha ao adicionar TAG ")
            return False

    def get_instituicoes(self):
        return EventoInstituicao.objects.all().filter(evento_relacionado=self)

    def get_valor(self):
        valor = 0
        atividades = self.get_atividades()
        for i in range(len(atividades)):
            valor += atividades[i].valor
        return valor

    def add_instituicao(self, instituicao, tipo_relacionamento):
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


class Agenda(models.Model):
    evento = models.ForeignKey('core.Evento', related_name="agenda")
    item_agenda = models.ManyToManyField('utils.Horario',
                                         through="core.ItemAgenda",
                                         related_name='horarios')


class ItemAgenda(models.Model):
    agenda = models.ForeignKey('core.Agenda', related_name="itens_agenda")
    horario = models.ForeignKey('utils.Horario')


class EventoSatelite(models.Model):
    eventos = models.ForeignKey("core.Evento", related_name="evento_satelite", default="")


class Atividade(PolymorphicModel, Observado):
    nome = models.CharField('nome', max_length=30, unique=True, blank=False)
    descricao = models.TextField('descricao da atividade', blank=True)
    trilhas = models.ManyToManyField(
        'core.Trilha',
        through="AtividadeTrilha",
        related_name="trilha_atividade")
    horarioAtividade = models.ForeignKey('core.HorarioAtividade', blank=True, null=True)
    valor = models.DecimalField("valor", max_digits=5, decimal_places=2, default=0)
    evento = models.ForeignKey('core.Evento', verbose_name="atividades", related_name='polymorphic_myapp.mymodel_set+',
                               null=False)
    periodo = models.ForeignKey('utils.Periodo',
                                verbose_name="periodo",
                                related_name="periodo",
                                default="")
    trilhas = models.ManyToManyField('core.Trilha',
                                     through="AtividadeTrilha",
                                     related_name="trilha_atividade")

    @staticmethod
    def atividades_tipo(tipo):
        return Atividade.objects.filter().instance_of(tipo)

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    @staticmethod
    def atividades_tipo(tipo):
        return Atividade.objects.filter().instance_of(tipo)

    def __str__(self):
        return self.nome


class HorarioAtividade(models.Model):
    data_inicio = models.DateField("Data inicio", blank=True, null=False)
    data_fim = models.DateField("Data fim", blank=True, null=False)
    hora_inicio = models.TimeField("Hora inicio", blank=True, null=False)
    hora_fim = models.TimeField("Hora Fim", blank=True, null=False)

    def get_dias_atividade(self):
        dias = self.data_fim - self.data_inicio
        dias = dias.days
        dict = {}
        for i in range(dias + 1):
            dict[str(i)] = self.data_inicio + datetime.timedelta(i)

        return dict


class AtividadePadrao(Atividade):
    horario = models.ForeignKey('utils.Horario',
                                related_name="horario_atividade_simples")

    class Meta:
        verbose_name = 'Atividade Padrao'
        verbose_name_plural = 'Atividades Padrao'


class AtividadeContinua(Atividade):
    class Meta:
        verbose_name = 'AtividadeContinua'
        verbose_name_plural = 'AtividadesContinuas'

    def add_horario(self, horario):
        self.save()
        horario.atividade = self


class AtividadeAdministrativa(Atividade):
    valor = 0

    class Meta:
        verbose_name = 'AtividadeNeutra'
        verbose_name_plural = 'AtividadesNeutra'

    def add_horario(self, horario):
        self.save()
        horario.atividade = self


class Trilha(models.Model):
    nome = models.CharField('nome', max_length=40)
    valor = models.DecimalField('valor', max_digits=5, decimal_places=2, default=0)

    evento = models.ForeignKey('core.Evento',
                               related_name="evento_trilha",
                               verbose_name="evento")

    responsaveis = models.ManyToManyField('user.Usuario',
                                          through="ResponsavelTrilha",
                                          related_name="responsavel_trilha")

    atividades = models.ManyToManyField('core.Atividade',
                                        through="AtividadeTrilha",
                                        related_name="atividade_trilha")

    class meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'

    def __str__(self):
        return self.nome


class TrilhaInscricao(models.Model):
    trilha = models.ForeignKey('core.Trilha',
                               related_name="trilha_Inscricao",
                               verbose_name="trilha_inscricao")

    inscricao = models.ForeignKey('user.Inscricao',
                                  related_name="inscricao_trilha_Inscricao",
                                  verbose_name="trilha_incricao")


class ResponsavelTrilha(models.Model):
    tipo_responsavel_trilha = models.CharField(max_length=30)

    responsavel = models.ForeignKey("user.Usuario",
                                    related_name="usuario_responsavel_trilha",
                                    default="")

    trilha = models.ForeignKey("core.Trilha",
                               related_name="trilha_dirigida",
                               default="")


class GerenciaEvento(models.Model):
    tipo_gerente = EnumField(TipoGerencia, max_length=25, default=TipoGerencia.PADRAO)

    gerente = models.ForeignKey("user.Usuario",
                                related_name="usuario_gerente",
                                default="")

    evento = models.ForeignKey("core.Evento",
                               related_name="evento_gerente",
                               default="")


class ResponsavelAtividade(models.Model):
    responsavel = models.CharField('nome', max_length=30, unique=True, blank=True)
    descricao = models.CharField('descricao', max_length=500, unique=True, blank=True)
    tipo_responsavel = EnumField(TipoResponsavel, default=TipoResponsavel.PADRAO)

    atividade = models.ForeignKey("core.Atividade",
                                  related_name="atividade_dirigida",
                                  default="")


class Instituicao(models.Model):
    nome = models.CharField('nome', max_length=30, default="")

    class Meta:
        verbose_name = 'Instituicao'
        verbose_name_plural = 'Instituicoes'

    def __str__(self):
        return self.nome


class EventoInstituicao(models.Model):
    tipo_relacionamento = EnumField(TipoInstituicao, default=TipoInstituicao.PADRAO)

    instituicao = models.ForeignKey('core.Instituicao', verbose_name="Instituição",
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
    tag = models.ForeignKey(Tag,
                            related_name='tag_de_usuario',
                            default="")

    usuario = models.ForeignKey(Usuario,
                                related_name='tag_de_usuario',
                                default="")

    class Meta:
        verbose_name = 'Relacionamento_Tag_Usuario'
        verbose_name_plural = 'Relacionamentos_Tag_Usuario'

    def __str__(self):
        return self.tag.__str__() + self.usuario.__str__()


class Tag_Evento(models.Model):
    tag = models.ForeignKey(Tag,
                            related_name='tag_de_evento',
                            default="")

    evento = models.ForeignKey(Evento,
                               related_name='tag_de_evento',
                               default="")

    class Meta:
        verbose_name = 'Relacionamento_Tag_Evento'
        verbose_name_plural = 'Relacionamentos_Tag_Tag'

    def __str__(self):
        return (" relacionamento : " + self.tag.nome() + self.evento.nome())


class AtividadeTrilha(models.Model):
    atividade = models.ForeignKey("core.Atividade",
                                  related_name="atividades_de_trilha",
                                  default="")
    trilha = models.ForeignKey("core.Trilha", related_name="trilhas_de_atividade",
                               default="")


class EspacoFisico(models.Model):
    nome = models.TextField('nome', max_length=30, default="")
    tipoEspacoFisico = EnumField(TipoEspacoFisico, default=TipoEspacoFisico.PADRAO)
    capacidade = models.DecimalField("capacidade", max_digits=5, decimal_places=0, default=0)

    evento = models.ForeignKey("core.Evento",
                               related_name="espaco_do_evento",
                               default="")

    atividade = models.ForeignKey("core.Atividade",
                                  related_name="espaco_da_atividade",
                                  default="")

    def __str__(self):
        return self.nome
