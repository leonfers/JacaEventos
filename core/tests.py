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


    def test_campo_dono_em_branco(self):
        evento = Evento(dono='')
        self.assertEqual(evento.get_dono(), '')
    
    def test_campo_valor_em_branco(self):
        evento = Evento(valor='')
        self.assertEqual(evento.get_valor(), '')
    
    def test_lista_instituicoes_em_branco(self):
        evento = Evento()


class ClasseTesteInstituiçao(TestCase):


    def test_campo_nomeInstituicao_em_branco(self):
        instituicao = Instituicao(nome='')
        self.assertFalse(instituicao.__str__(), '')


class ClasseTesteRelacionamentoEventoInstituicao(TestCase):


    def test_tipo_relacionamento_nao_nulo(self):
        relacionamento = Evento_Instituicao(tipo_relacionamento='')
        self.assertFalse(relacionamento.tipo_relacionamento, '')
    

class ClasseTesteTag(TestCase):


    def test_tag_de_nome_em_branco(self):
        tag_de_nome_nula = Tag(nome='')
        self.assertFalse(tag_de_nome_nula.nome, '')
    

class ClasseTesteTagUsuario(TestCase):


    def test_tag_sem_usuario(self):
        tag_sem_usuario = Tag_Usuario(usuario='')
        self.assertFalse(tag_sem_usuario.usuario, '')


class ClasseTesteTagEvento(TestCase):


    def test_tag_sem_evento(self):
        tag_sem_evento = Tag_Evento(evento='')
        self.assertFalse(tag_sem_evento.evento, '')


class ClasseTesteValores(TestCase):


    def Atribuicao_de_lista_vazia_de_atividades_a_Evento_recem_criado(self):
        """
        Ver se na criacao do evento foram criada tambem lista de atividades vazia.
        """
        evento = Evento()
        self.assertEqual(evento.get_atividades(self), [])
    
    def Atribuicao_de_lista_vazia_de_relacionamentos_com_empresas_a_Evento_recem_criado(self):
        """
        Ver se na criacao do evento foram criada tambem lista de atividades vazia.
        """
        evento = Evento()
        self.assertEqual(evento.get_instituicoes(self), [])
    
    def Nao_permitir_Atividades_de_Eventos_distintos_na_mesma_Atividade_(self):
        """
        Ver se Atividades distintas se repetem.
        """
        atividade_repetida = Atividade(nome="Teste")
        evento = Evento()
        self.assertFalse(atividade_repetida in evento.get_atividades())
    
