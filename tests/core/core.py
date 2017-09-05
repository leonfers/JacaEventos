from django.contrib.auth.models import User
from django.test import TestCase
from core.models import *
from user.models import *
from utils.models import *
import datetime

NOME_EVENTO = "Festival de Musica de Pedro II"
NOME_TRILHA = "Violonistas em P2"

class TestCore(TestCase):

    def create_evento(self):
        usuario = Usuario()
        usuario.username = "will"
        usuario.email = "will@gmail.com"
        usuario.nome = "Wildrimak"
        usuario.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
        usuario.save()

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

    def get_evento(self):
        return Evento.objects.get(nome=NOME_EVENTO)

    def create_atividade(self):
        self.create_evento()
        evento = self.get_evento()
        # criando um espaco fisico e atrelando a um evento e atividade
        espaco = EspacoFisico()
        espaco.nome = "Teresina Hall"
        espaco.tipoEspacoFisico = TipoEspacoFisico.AR_LIVRE
        espaco.capacidade = 50
        espaco.evento = evento
        espaco.save()

        # craindo um horario para atividade
        horario = Horario()
        horario.data = "2017-1-1"
        horario.hora_inicio = "20:00"
        horario.hora_fim = "22:00"
        horario.save()

        # horario atividade
        data = datetime.date.today()
        hora_inicio = datetime.datetime.now().time()
        hora_fim = datetime.datetime.now().time()
        horario_atividade = HorarioAtividade.objects.create(data_inicio=data, data_fim=data, hora_inicio=hora_fim,
                                                            hora_fim=hora_fim)
        # criando atividade
        atividade = AtividadePadrao()
        atividade.nome = "Gilberto Gil"
        atividade.descricao = "Show do Gilberto Gil"
        atividade.valor = 0
        atividade.espaco_fisico = espaco
        atividade.evento = evento
        atividade.horario_atividade = horario_atividade
        atividade.save()

    def create_pacote(self):
        self.create_trilha()
        evento = self.get_evento()
        trilha = self.get_trilha()


        # Criando usuario para cliente em plataforma
        usuario_inscrito = Usuario()
        usuario_inscrito.username = "Kassio"
        usuario_inscrito.email = "kassio@gmail.com"
        usuario_inscrito.nome = "Kassio"
        usuario_inscrito.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
        usuario_inscrito.save()

        # criando uma inscricao
        inscricao = Inscricao()
        inscricao.status_inscricao = StatusInscricao.ATIVA
        inscricao.tipo_inscricao = TipoInscricao.PARCIAL
        inscricao.usuario = usuario_inscrito
        inscricao.evento = evento
        inscricao.save()

        # adicionando uma trilha a uma inscricao
        trilha_inscricao = PacoteInscricao()
        trilha_inscricao.pacote = trilha
        trilha_inscricao.inscricao = inscricao
        trilha_inscricao.save()

    def create_trilha(self):
        self.create_evento()
        evento = self.get_evento()
        # criando uma Trilha
        trilha = Trilha()
        trilha.nome = NOME_TRILHA
        trilha.valor = 0
        trilha.evento = evento
        trilha.save()

    def get_trilha(self):
        return Trilha.objects.get(nome=NOME_TRILHA )