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

    def test_verificar_inscricao_evento(self):
        self.create_inscricao()

    def test_calcular_valor_correto_de_inscricao_dado_um_conjunto_de_atividades_adicionadas(self):
        inscricao = Inscricao.objects.create(usuario=self.user, evento=self.evento)
        evento = self.evento
        evento.add_atividade(self.atividade)
        self.assertEqual(evento.valor, inscricao.evento.valor)

    def test_nao_aceitar_incluir_inscricao_se_o_estado_do_evento_ja_for_ANDAMENTO(self):
        evento = self.evento
        evento.status = StatusEvento.ANDAMENTO
        inscricao = Inscricao.objects.create(usuario=self.user,
                                             evento=evento)
        # self.assertTrue(inscricao.evento, evento)

    def test_valor_total_de_uma_inscricao_por_evento_deve_ser_igual_ao_valor_evento(self):
        inscricao = Inscricao(usuario=self.user, evento=self.evento)
        self.assertTrue(inscricao.evento.valor == self.evento.valor)

# def test_calculo_do_valor_final_de_uma_inscricao_direta_deve_ser_especificado_no_proprio_evento(self):
#         """
#         Já para eventos de inscrição direto no evento o valor
#         será especificado direto no evento, incluindo os valores do eventos Satelites.
#         """
