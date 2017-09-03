import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from user.models import *
from core.models import *

from tests.user.user import TestUser
from utils.models import Periodo


class TesteInscricao(TestUser):
    # py manage.py dumpdata - o test_fixtures.json
    fixtures = ['test_fixtures.json']

    def test_create_inscricao(self):
        self.create_inscricao()

#
#     def test_verificar_inscricao_evento(self):
#         self.inscricao()
#
#     # dando exception
#     def test_calcular_valor_correto_de_inscricao_dado_um_conjunto_de_atividades_adicionadas(self):
#         atividade = AtividadePadrao(valor=5.0)
#         evento_criado = Evento()
#         evento_criado.add_atividade(atividade)
#         inscricao = Inscricao(evento=evento_criado)
#         self.assertEqual(evento_criado.valor, inscricao.evento.valor)
#
#     #
#     # def test_nao_aceitar_incluir_inscricao_se_o_estado_do_evento_ja_for_ATIVO(self):
#     #     evento = Evento()
#     #     inscricao = Inscricao(status_inscricao='ativa')
#     #     self.assertFalse(inscricao.evento, evento)
#
#     def test_valor_total_de_uma_inscricao_por_evento_deve_ser_igual_ao_valor_evento(self):
#         usuario = Usuario(username="Will", email="teste@teste", nome="Will")
#
#         endereco = Endereco(pais="Brasil", estado="Piaui", logradouro="Praca", numero="N/A", cidade="Teresina",
#                             bairro="Macauba", cep="64532-123")
#         periodo = Periodo(data_inicio=datetime.date.today(), data_fim=datetime.date(2018, 1, 1))
#         evento = Evento(nome="Festival de Musica de Pedro II",
#                         descricao="Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura",
#                         valor=0, tipo_evento=TipoEvento.SEMINARIO, periodo=periodo, endereco=endereco, dono=usuario)
#         atividade = AtividadeAdministrativa(nome='credenciamento', descricao='abc', evento=evento)
#         inscricao = Inscricao(usuario=usuario, evento=evento)
#
#     def test_calculo_do_valor_final_de_uma_inscricao_e_o_somatorio_dos_itens_para_os_eventos_onde_a_inscricao_e_por_itens(
#             self):
#         """
#         O Calculo do valor final de um inscrição é o somatório dos itens para os eventos
#         onde a inscrição é por itens.
#         """
#
#     def test_calculo_do_valor_final_de_uma_inscricao_direta_deve_ser_especificado_no_proprio_evento(self):
#         """
#         Já para eventos de inscrição direto no evento o valor
#         será especificado direto no evento, incluindo os valores do eventos Satelites.
#         """
