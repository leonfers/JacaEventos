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
    valor = models.DecimalField("valor", max_digits=8, decimal_places=2, default=0)
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
                                            through="core.TagEvento",
                                            related_name='tags_do_evento')

    @property
    def atividades(self):
        return Atividade.objects.all().filter(evento=self)

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
        return self.get_agenda_dia(data)

    def get_agenda_dia(self, data):

        tamanho = len(self.atividades)
        dict = {}
        agenda_hoje = {}
        atividades = self.atividades
        for i in range(tamanho):
            for j in range(len(atividades[i].horario_atividade.get_dias_atividade())):
                if data == self.atividades[i].horario_atividade.get_dias_atividade()[str(j)]:
                    dict[str(self.atividades[i])] = str(self.atividades[i].horario_atividade.hora_inicio) + " " + str(
                        self.atividades[i].horario_atividade.hora_fim)
                    agenda_hoje[str(str(data))] = dict
        return agenda_hoje

    def add_atividade(self, atividade):
        for atv in self.atividades:
            if atv.checar_conflito(atividade):
                return False
            else:
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
            tag_evento = TagEvento()
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


class EventoSatelite(models.Model):
    eventos = models.ForeignKey("core.Evento", related_name="evento_satelite", default="")


class Atividade(PolymorphicModel):
    nome = models.CharField('nome', max_length=30, unique=True, blank=False)
    descricao = models.TextField('descricao da atividade', blank=True)
    valor = models.DecimalField("valor", max_digits=7, decimal_places=2, default=0)

    evento = models.ForeignKey('core.Evento',
                               verbose_name="atividades",
                               related_name='polymorphic_myapp.mymodel_set+',
                               null=False)

    espaco_fisico = models.ForeignKey('core.EspacoFisico',
                                      related_name="espaco_atividade")

    trilhas = models.ManyToManyField('core.Pacote',
                                     through="AtividadePacote",
                                     related_name="pacote_atividade")

    horario_atividade = models.ForeignKey('utils.HorarioAtividade', blank=False, null=False)

    @staticmethod
    def atividades_tipo(tipo):
        return Atividade.objects.filter().instance_of(tipo)

    def validate_horario_atividade(self):
        periodo_evento = self.evento.periodo
        if self.horario_atividade.data_inicio < periodo_evento.data_inicio:
            self.horario_atividade.delete()
            raise ValidationError("A data de inicio da atividade deve ser igual ou maior a data de inicio do evento")
        if self.horario_atividade.data_fim > periodo_evento.data_fim:
            raise ValidationError("A data fim da atividade deve ser menor ou igual a data final do evento")

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    @staticmethod
    def atividades_tipo(tipo):
        return Atividade.objects.filter().instance_of(tipo)

    def __str__(self):
        return self.nome


class AtividadePadrao(Atividade):
    class Meta:
        verbose_name = 'Atividade Padrao'
        verbose_name_plural = 'Atividades Padrao'

    def checar_conflito(self, atividade):
        if isinstance(atividade, AtividadeContinua):
            for horario_atv in atividade:
                if (
                                    self.horario_atividade.hora_inicio <= horario_atv.hora_inicio <= self.horario_atividade.hora_fim and self.horario_atividade.data == horario_atv.data) or (
                                self.horario_atividade.hora_fim >= horario_atv.hora_fim >= self.horario_atividade.hora_inicio):
                    raise Exception('conflito', 'conflito de horario para atividade no mesmo espaco fisico')
                    return True
                else:
                    return False

        elif isinstance(atividade, AtividadePadrao):
            if (
                                self.horario_atividade.hora_inicio <= atividade.horario_atividade.hora_inicio <= self.horario_atividade.hora_fim and self.horario_atividade.data == atividade.horario_atividade.data) or (
                            self.horario_atividade.hora_fim >= atividade.horario_atividade.hora_fim >= self.horario_atividade.hora_inicio):
                raise Exception('conflito', 'conflito de horario para atividade no mesmo espaco fisico')
                return True
            else:
                return False
        else:
            return False


class AtividadeContinua(Atividade):
    class Meta:
        verbose_name = 'AtividadeContinua'
        verbose_name_plural = 'AtividadesContinuas'

    def add_horario(self, horario):
        self.save()
        horario.atividade = self

    def checar_conflito(self, atividade):
        if isinstance(atividade, AtividadeContinua):
            for horario_atv in self.horario:
                for horario_atividade in atividade.horario_atividade:
                    if (
                                        horario_atividade.hora_inicio <= horario_atv.hora_inicio <= horario_atividade.hora_fim and horario_atividade.data == horario_atv.data) or (
                                    horario_atividade.hora_fim >= horario_atv.hora_fim >= horario_atividade.hora_inicio):
                        raise Exception('conflito', 'conflito de horario para atividade no mesmo espaco fisico')
                        return True
                    else:
                        return False

        elif isinstance(atividade, AtividadePadrao):
            for horario_atv in self.horario:
                if (
                                    atividade.horario_atividade.hora_inicio <= horario_atv.hora_inicio <= atividade.horario_atividade.hora_fim and atividade.horario_atividade.data == horario_atv.data) or (
                                atividade.horario_atividade.hora_fim >= horario_atv.hora_fim >= atividade.horario_atividade.hora_inicio):
                    raise Exception('conflito', 'conflito de horario para atividade no mesmo espaco fisico')
                    return True
                else:
                    return False
        else:
            return False


class AtividadeAdministrativa(Atividade):
    class Meta:
        verbose_name = 'AtividadeNeutra'
        verbose_name_plural = 'AtividadesNeutra'

    def add_horario(self, horario):
        self.save()
        horario.atividade = self

    def checar_conflito(self, atividade):
        return False


class Pacote(PolymorphicModel):
    nome = models.CharField('nome', max_length=40)
    valor = models.DecimalField('valor', max_digits=8, decimal_places=2, default=0)

    evento = models.ForeignKey('core.Evento',
                               verbose_name="pacote",
                               related_name='polymorphic_myapp.mymodel_set+',
                               null=False)

    atividades = models.ManyToManyField('core.Atividade',
                                        through="AtividadePacote",
                                        related_name="atividade_trilha")


class Trilha(Pacote):
    responsaveis = models.ManyToManyField('user.Usuario',
                                          through="ResponsavelTrilha",
                                          related_name="responsavel_trilha")

    class meta:
        verbose_name = 'Trilha'
        verbose_name_plural = 'Trilhas'

    def __str__(self):
        return self.nome


class PacoteInscricao(models.Model):
    pacote = models.ForeignKey('core.Pacote',
                               related_name="pacote_Inscricao",
                               verbose_name="trilha_inscricao")

    inscricao = models.ForeignKey('user.Inscricao',
                                  related_name="inscricao_pacote_Inscricao",
                                  verbose_name="pacote_incricao")


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


class TagUsuario(models.Model):
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


class TagEvento(models.Model):
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


class AtividadePacote(models.Model):
    atividade = models.ForeignKey("core.Atividade",
                                  related_name="atividades_de_pacote",
                                  default="")
    pacote = models.ForeignKey("core.Pacote", related_name="pacote_de_atividade",
                               default="")


class EspacoFisico(models.Model):
    nome = models.TextField('nome', max_length=30, default="")
    tipoEspacoFisico = EnumField(TipoEspacoFisico, default=TipoEspacoFisico.PADRAO)
    capacidade = models.DecimalField("capacidade", max_digits=5, decimal_places=0, default=0)

    evento = models.ForeignKey("core.Evento",
                               related_name="espaco_do_evento",
                               default="")

    def __str__(self):
        return self.nome
