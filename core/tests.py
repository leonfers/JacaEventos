import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from .models import *

"""
class TestePovoamento(TestCase):
    def inicio_testes(self):
        exec(open('povoar.py').read())
"""

class TesteEvento(TestCase):


    def test_validar_criacao_do_evento(self):
        o_dono = Usuario(nome='Ele')
        endereco_evento = Endereco(pais='Brasil', cidade='Ipanema', bairro='Dirceu', logradouro='Rua das avenidas',
        numero='41',cep='44522-98', estado='Piaui')
        periodo_evento = Periodo(data_inicio='2017-08-14',data_fim='2017-08-18')
        evento = Evento(dono=o_dono, nome="Evento inicial", tipo_evento='padrao',
         endereco=endereco_evento, periodo=periodo_evento)
        self.assertEqual(evento.periodo, periodo_evento)
        self.assertEqual(evento.endereco, endereco_evento)
        self.assertEqual(evento.dono.nome, 'Ele')
        self.assertEqual(evento.nome, 'Evento inicial')
        self.assertTrue(evento.tipo_evento, 'padrao', "Todos os testes passaram com êxito!")
    
    def test_evento_criado_com_dono_e_conjunto_vazio_de_atividades(self):
        o_dono = Usuario(nome='Ele')
        evento = Evento(dono=o_dono)
        sem_atividades = evento.get_atividades()
        vazio = len(sem_atividades)
        self.assertEqual(evento.dono.nome, 'Ele')
        self.assertEqual(vazio, 0)
    
    def test_evento_com_lista_vazia_de_relacionamento_com_instituicoes(self):
        evento = Evento()
        sem_instituicoes = evento.get_instituicoes()
        vazio = len(sem_instituicoes)
        self.assertEqual(vazio, 0)

    def test_nao_permitir_Atividades_de_Eventos_distintos_na_mesma_Atividade(self):
        atividade_repetida = Atividade(nome="Teste")
        evento = Evento()
        self.assertFalse(atividade_repetida in evento.get_atividades())


class TesteInstituicao(TestCase):


    def test_campo_nome_Instituicao_em_branco(self):
        instituicao = Instituicao(nome='Nova')
        self.assertEqual(instituicao.__str__(), 'Nova')


class TesteRelacionamentoEventoInstituicao(TestCase):


    def test_tipo_relacionamento_nao_estabelecido(self):
        relacionamento = EventoInstituicao(tipo_relacionamento='')
        self.assertFalse(relacionamento.tipo_relacionamento, '')

    def test_validar_relacionamento(self):
        evento = Evento()
        instituicao = Instituicao(nome="Teste")
        relacionamento = EventoInstituicao(instituicao=instituicao, evento_relacionado=evento)
        self.assertEqual(relacionamento.evento_relacionado, evento)
        self.assertEqual(relacionamento.instituicao, instituicao)
    

class TesteTag(TestCase):


    def test_tag_de_nome_em_branco(self):
        tag_de_nome_nula = Tag(nome='')
        self.assertFalse(tag_de_nome_nula.nome, '')
    

class TesteTagUsuario(TestCase):


    def test_tag_sem_usuario(self):
        usuario_teste = Usuario()
        tag_sem_usuario = Tag_Usuario(usuario=usuario_teste)
        self.assertFalse(tag_sem_usuario.usuario.nome, '')


class TesteTagEvento(TestCase):


    def test_tag_sem_evento(self):
        evento_teste = Evento()
        tag_sem_evento = Tag_Evento(evento=evento_teste)
        self.assertFalse(tag_sem_evento.evento.nome, '')