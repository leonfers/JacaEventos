import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TesteEvento(TestCore):
    def test_validar_criacao_evento(self):
        self.create_evento()

    def test_criar_evento_status_em_andamento(self):
        evento = self.create_evento()
        evento.status = StatusEvento.ANDAMENTO
        self.assertTrue(evento.status, StatusEvento.ANDAMENTO)

    def test_criar_evento_com_tipo_congresso(self):
        evento = self.create_evento()
        evento.tipo_evento = TipoEvento.CONGRESSO
        self.assertTrue(evento.tipo_evento, TipoEvento.CONGRESSO)

    def test_criar_evento_com_dono(self):
        evento = self.create_evento()
        usuario = self.create_usuario()
        evento.dono = usuario
        self.assertTrue(evento.dono, usuario)

    def test_qtd_atividades(self):
        evento = self.create_evento()
        self.assertEqual(len(evento.atividades), 0, "O evento deve comecar com 0 atividades")

    def test_criacao_evento_com_periodo(self):
        evento = self.create_evento()
        periodo = self.create_periodo()
        evento.periodo = periodo
        self.assertEqual(evento.periodo, periodo)

    def test_criacao_evento_com_dono(self):
        evento = self.create_evento()
        usuario = self.create_usuario()
        evento.dono = usuario
        self.assertEqual(evento.dono, usuario)

    def test_evento_com_descricao_em_branco(self):
        evento = self.create_evento()
        evento.descricao = ''
        self.assertEqual(evento.descricao, '')

    def test_criando_evento_com_status_inscricoes_abertas(self):
        evento = self.create_evento()
        evento.status = StatusEvento.INSCRICOES_ABERTAS
        self.assertEqual(evento.status, StatusEvento.INSCRICOES_ABERTAS)

    def test_criando_evento_com_valor_igual_zero(self):
        evento = self.create_evento()
        evento.valor = 0
        self.assertEqual(evento.valor, 0)
