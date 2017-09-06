import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TestePacote(TestCore):
    def test_validar_criacao_pacote(self):
        self.create_pacote()

    def test_criacao_pacote_com_nome_em_branco(self):
        pacote = self.create_pacote()
        pacote.nome = ""
        self.assertEquals(pacote.nome, "")

    def test_criacao_pacote_com_evento(self):
        pacote = self.create_pacote()
        evento = self.create_evento()
        pacote.evento = evento
        self.assertEquals(pacote.evento, evento)

    def test_criacao_pacotes_com_valor_zero(self):
        pacote = self.create_pacote()
        pacote.valor = 0
        self.assertEquals(pacote.valor, 0)

    def test_cricao_pacote_com_evento_errado(self):
        pacote = self.create_pacote()
        evento_um = self.create_evento()
        evento_dois = self.create_evento()
        pacote.evento = evento_um
        self.assertFalse(pacote.evento, evento_dois)