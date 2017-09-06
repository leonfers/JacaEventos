from django.contrib.auth.models import User
from django.test import TestCase
from core.models import *
from user.models import *
from utils.models import *
import datetime

NOME_EVENTO = "Festival de Musica de Pedro II"
NOME_TRILHA = "Violonistas em P2"
USUARIO_USERNAME = "will"


class TestCore(TestCase):
    def get_user_dono_evento(self):
        usuario = Usuario()
        usuario.username = USUARIO_USERNAME
        usuario.email = "will@gmail.com"
        usuario.nome = "Wildrimak"
        usuario.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
        usuario.save()
        self.usuario = usuario
        return usuario

    def get_dono_evento(self):
        return Usuario.objects.get(username=USUARIO_USERNAME)

    def get_evento(self):
        self.get_user_dono_evento()
        usuario = self.get_dono_evento()
        # criando um endereco para evento
        endereco = Endereco()
        endereco.pais = "Brasil"
        endereco.estado = "Piaui"
        endereco.logradouro = "Praca"
        endereco.numero = "N/A"
        endereco.cidade = "Teresina"
        endereco.bairro = "Macauba"
        endereco.cep = "64532-123"
        endereco.save()
        self.endereco = endereco

        evento = Evento()
        evento.nome = NOME_EVENTO
        evento.descricao = "Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura"
        evento.valor = 0
        evento.tipo_evento = TipoEvento.SEMINARIO

        # criando um periodo para evento
        periodo = Periodo()
        periodo.data_inicio = datetime.date.today()
        periodo.data_fim = datetime.date(2018, 1, 1)
        periodo.save()

        evento = Evento()
        evento.nome = "Festival de Musica de Pedro II"
        evento.descricao = "Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura"
        evento.valor = 0
        evento.tipo_evento = TipoEvento.SEMINARIO
        evento.periodo = periodo
        evento.endereco = endereco
        evento.dono = usuario
        evento.save()
        self.evento = evento
        return evento

    def get_evento(self):
        return Evento.objects.get(nome=NOME_EVENTO)

    def get_atividade(self):
        self.get_evento()
        evento = self.get_evento()
        # criando um espaco fisico e atrelando a um evento e atividade
        espaco = EspacoFisico()
        espaco.nome = "Teresina Hall"
        espaco.tipoEspacoFisico = TipoEspacoFisico.AR_LIVRE
        espaco.capacidade = 50
        espaco.evento = evento
        espaco.save()
        self.espaco = espaco

        # craindo um horario para atividade
        horario = Horario()
        horario.data = "2017-1-1"
        horario.hora_inicio = "20:00"
        horario.hora_fim = "22:00"
        horario.save()
        self.horario = horario

        # horario atividade
        data = datetime.date.today()
        hora_inicio = datetime.datetime.now().time()
        hora_fim = datetime.datetime.now().time()

        horario_atividade = HorarioAtividade.objects.create(data_inicio=data, data_fim=data, hora_inicio=hora_fim,
                                                            hora_fim=hora_fim)
        horario_atividade.save()
        self.horario_atividade = horario_atividade

        # criando atividade
        atividade = AtividadePadrao()
        atividade.nome = "Gilberto Gil"
        atividade.descricao = "Show do Gilberto Gil"
        atividade.valor = 0
        atividade.espaco_fisico = espaco
        atividade.evento = evento
        atividade.horario_atividade = horario_atividade
        atividade.save()
        self.atividade = atividade

    def get_pacote(self):
        self.get_trilha()
        evento = self.get_evento()
        trilha = self.get_trilha()

        # Criando usuario para cliente em plataforma
        usuario_inscrito = Usuario()
        usuario_inscrito.username = "Kassio"
        usuario_inscrito.email = "kassio@gmail.com"
        usuario_inscrito.nome = "Kassio"
        usuario_inscrito.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
        usuario_inscrito.save()
        self.usuario_inscrito = usuario_inscrito

        # criando uma inscricao
        inscricao = Inscricao()
        inscricao.status_inscricao = StatusInscricao.ATIVA
        inscricao.tipo_inscricao = TipoInscricao.PARCIAL
        inscricao.usuario = usuario_inscrito
        inscricao.evento = evento
        inscricao.save()
        self.inscricao = inscricao

        # adicionando uma trilha a uma inscricao
        trilha_inscricao = PacoteInscricao()
        trilha_inscricao.pacote = trilha
        trilha_inscricao.inscricao = inscricao
        trilha_inscricao.save()
        self.trilha_inscricao = trilha_inscricao

    def get_trilha(self):
        self.get_evento()
        evento = self.get_evento()
        # criando uma Trilha
        trilha = Trilha()
        trilha.nome = NOME_TRILHA
        trilha.valor = 0
        trilha.evento = evento
        trilha.save()
        self.trilha = trilha

    def get_trilha(self):
        return Trilha.objects.get(nome=NOME_TRILHA)

    def get_responsavel_trilha(self):
        self.get_trilha()
        trilha = self.get_trilha()
        usuario = trilha.evento.dono
        # definir um usuario responsavel pela trilha
        responsavel_trilha = ResponsavelTrilha()
        responsavel_trilha.responsavel = usuario
        responsavel_trilha.trilha = trilha
        responsavel_trilha.tipo_responsavel_trilha = "staff"
        self.responsavel_trilha = responsavel_trilha

    def create_evento(self):
        return Evento()

    def create_pacote(self):
        return Pacote()

    def create_usuario(self):
        return Usuario()

    def create_atividade(self):
        return Atividade()

    def create_trilha(self):
        return Trilha()

    def create_periodo(self):
        return Periodo()

    def create_atividade(self):
        return Atividade()

    def create_atividade_padrao(self):
        return AtividadePadrao()

    def create_atividade_administrativa(self):
        return AtividadeAdministrativa

    def create_atividade_continua(self):
        return AtividadeContinua()

    def create_tag(self):
        return Tag()

    def create_horario_atividade(self):
        return HorarioAtividade
