import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from user.models import *
from core.models import *

from tests.user.user import TestUser
from utils.models import Periodo


class TesteInscricao(TestUser):
    def test_create_inscricao(self):
        self.create_inscricao()

    def test_criar_inscricao_com_status_ativo(self):
        inscricao = self.create_inscricao()
        inscricao.status_inscricao = StatusInscricao.ATIVA
        self.assertTrue(inscricao.status_inscricao.ATIVA, StatusInscricao.ATIVA)

    def test_criar_inscricao_com_tipo_parcial(self):
        inscricao = self.create_inscricao()
        inscricao.tipo_inscricao = TipoInscricao.PARCIAL
        self.assertTrue(inscricao.tipo_inscricao.PARCIAL, TipoInscricao.PARCIAL)


    def test_valor_total_de_uma_inscricao_por_evento_deve_ser_igual_ao_valor_evento(self):
        inscricao = Inscricao(usuario=self.user, evento=self.new_evento)
        inscricao.save()
        self.assertEqual(True, inscricao.evento.valor == self.evento.valor)



