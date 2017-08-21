import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import *

class TestePovoamento(TestCase):


    def inicio_testes(self):
        exec(open('povoar.py').read())


class ClassTesteEvento(TestCase):


    def test_nao_permitir_criar_evento_sem_nome_ou_dono(self):
        o_dono = Usuario(nome='Ele')
        evento = Evento(dono=o_dono)
        self.assertFalse(evento.nome, '')
        self.assertEqual(evento.dono.nome, 'Ele')
    
    def test_evento_criado_com_dono_e_conjunto_vazio_de_atividades(self):
        o_dono = Usuario(nome='Ele')
        evento = Evento(dono=o_dono)
        self.assertEqual(evento.dono.nome, 'Ele')
        """self.assertFalse(evento.get_atividades(), [])"""
    
    def test_evento_com_lista_vazia_de_relacionamento_com_empresas(self):
        evento = Evento()
        self.assertFalse(evento.get_instituicoes(), [])
    
    def test_campo_valor_em_branco(self):
        evento = Evento(valor='')
        self.assertEqual(evento.valor, '')
    
    def test_lista_instituicoes_em_branco(self):
        evento = Evento()
        self.assertFalse(evento.get_instituicoes(), [])


class ClasseTesteInstituiçao(TestCase):


    def test_campo_nomeInstituicao_em_branco(self):
        instituicao = Instituicao(nome='')
        self.assertFalse(instituicao.__str__(), '')


class ClasseTesteRelacionamentoEventoInstituicao(TestCase):


    def test_tipo_relacionamento_nao_estabelecido(self):
        relacionamento = EventoInstituicao(tipo_relacionamento='')
        self.assertFalse(relacionamento.tipo_relacionamento, '')
    

class ClasseTesteTag(TestCase):


    def test_tag_de_nome_em_branco(self):
        tag_de_nome_nula = Tag(nome='')
        self.assertFalse(tag_de_nome_nula.nome, '')
    

class ClasseTesteTagUsuario(TestCase):


    def test_tag_sem_usuario(self):
        usuario_teste = Usuario()
        tag_sem_usuario = Tag_Usuario(usuario=usuario_teste)
        self.assertEqual(tag_sem_usuario.usuario.nome, '')


class ClasseTesteTagEvento(TestCase):


    def test_tag_sem_evento(self):
        evento_teste = Evento()
        tag_sem_evento = Tag_Evento(evento=evento_teste)
        self.assertFalse(tag_sem_evento.evento.nome, '')


class ClasseTesteValores(TestCase):


    def test_atribuicao_de_lista_vazia_de_atividades_a_Evento_recem_criado(self):
        """
        Ver se na criacao do evento foram criada tambem lista de atividades vazia.
        """
        evento = Evento()
        """
        self.assertFalse(evento.get_atividades(), [])
        """
    
    def test_atribuicao_de_lista_vazia_de_relacionamentos_com_empresas_a_Evento_recem_criado(self):
        """
        Ver se na criacao do evento foram criada tambem lista de atividades vazia.
        """
        evento = Evento()
        self.assertFalse(evento.get_instituicoes(), [])
    
    def test_nao_permitir_Atividades_de_Eventos_distintos_na_mesma_Atividade_(self):
        """
        Ver se Atividades distintas se repetem.
        """
        atividade_repetida = Atividade(nome="Teste")
        evento = Evento()
        """
        self.assertFalse(atividade_repetida in evento.get_atividades())
        """
    
