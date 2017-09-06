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

    def test_criacao_evento_com_pacote(self):
        pacote = self.create_pacote()
        evento = self.create_evento()
        pacote.evento = evento
        self.assertEquals(pacote.evento, evento)
