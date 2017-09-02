import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from user.models import *
from core.models import *
#
#
from tests.user.user import TestUser


class TesteInscricao(TestUser):
    def test_create_inscricao(self):
        self.create_inscricao()

    # dando exception
    def test_calcular_valor_correto_de_inscricao_dado_um_conjunto_de_atividades_adicionadas(self):
        atividade = AtividadePadrao(valor=5.0)
        evento_criado = Evento()
        evento_criado.add_atividade(atividade)
        inscricao = Inscricao(evento=evento_criado)
        self.assertEqual(evento_criado.valor, inscricao.evento.valor)

    # def test_nao_aceitar_incluir_inscricao_se_o_estado_do_evento_ja_for_ATIVO(self):
    #     evento = Evento()
    #     inscricao = Inscricao(status_inscricao='ativa')
    #     self.assertFalse(inscricao.evento, evento)

    def test_calculo_do_valor_final_de_uma_inscricao_e_o_somatorio_dos_itens_para_os_eventos_onde_a_inscricao_e_por_itens(
            self):
        """
        O Calculo do valor final de um inscrição é o somatório dos itens para os eventos
        onde a inscrição é por itens.
        """

    def test_calculo_do_valor_final_de_uma_inscricao_direta_deve_ser_especificado_no_proprio_evento(self):
        """
        Já para eventos de inscrição direto no evento o valor
        será especificado direto no evento, incluindo os valores do eventos Satelites.
        """
