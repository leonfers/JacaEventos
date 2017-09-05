import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TesteEvento(TestCore):


    def test_validar_criacao_do_evento(self):
        self.create_evento()

    def test_qtd_atividades(self):
        evento = Evento.objects.get(nome="Festival de Musica de Pedro II")
        print (evento)

    # def test_evento_criado_com_dono_e_conjunto_vazio_de_atividades(self):
    #     o_dono = Usuario(nome='Ele')
    #     evento = Evento(dono=o_dono)
    #     sem_atividades = evento.get_atividades()
    #     vazio = len(sem_atividades)
    #     self.assertEqual(evento.dono.nome, 'Ele')
    #     self.assertEqual(vazio, 0)
    #
    # def test_evento_com_lista_vazia_de_relacionamento_com_instituicoes(self):
    #     evento = Evento()
    #     sem_instituicoes = evento.get_instituicoes()
    #     vazio = len(sem_instituicoes)
    #     self.assertEqual(vazio, 0)
    #
    # def test_nao_permitir_Atividades_de_Eventos_distintos_na_mesma_Atividade(self):
    #     atividade_repetida = AtividadePadrao(nome="Teste")
    #     evento = Evento()
    #     self.assertFalse(atividade_repetida in evento.get_atividades())
    #
    # def test_mudanca_de_comportamentos_que_sejam_observados_por_outros_componentes(self):
    #     o_dono = Usuario(nome='Ele')
    #     endereco_evento = Endereco(pais='Brasil', cidade='Ipanema', bairro='Dirceu', logradouro='Rua das avenidas',
    #                                numero='41', cep='44522-98', estado='Piaui')
    #     periodo_evento = Periodo(data_inicio='2017-08-14', data_fim='2017-08-18')
    #     evento = Evento(dono=o_dono, nome="Evento inicial", tipo_evento='padrao',
    #                     endereco=endereco_evento, periodo=periodo_evento)
    #     evento_novo = evento.periodo.data_inicio='2017-08-10'
    #     self.assertFalse(evento != evento_novo, "Informações de evento foram modificadas.")
    #
    # def test_apenas_evento_satelite_pode_ser_adicionado_sozinho_a_inscricao(self):
    #     """
    #     Em caso de Eventos Satélites será possível se inscrever isoladamente em
    #     eventos que são satélites de eventos principais, porém não será permitido se
    #     inscrever apenas no evento Principal.
    #     """
    #     evento_novo = Evento(nome='evento')
    #     evento_extra = Evento(nome='evento grande')
    #     evento_satelite = EventoSatelite(eventos=evento_extra)
    #     usuario = Usuario(nome='Usuario')
    #     atividade = AtividadePadrao(nome='Atividade')
    #     trilha = Trilha(id=1, nome = 'trilha', valor = 15.00, evento = evento_novo)
    #     trilhaSatelite = Trilha(id=2, nome='trilha', valor=15.00, evento=evento_extra)
    #     inscricao = Inscricao(id=1, status_inscricao = 'ativa', usuario = usuario, evento = evento_novo)
    #     self.assertFalse(TrilhaInscricao(trilha, inscricao))
    #     self.assertTrue(TrilhaInscricao(trilhaSatelite, inscricao))
    #
    #
    #
    #
    #
    #
   