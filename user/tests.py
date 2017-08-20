import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import *
from core.models import *


class TestesViewLogin(TestCase):


    def test_resposta_de_status_a_registrar(self):
        resposta = self.client.get(reverse('registrar'))
        self.assertEqual(resposta.status_code, 200)
    

class TestesViewInicio(TestCase):


    def test_resposta_de_status_a_pagina_inicial(self):
        resposta = self.client.get(reverse('pagina_inicial'))
        self.assertEqual(resposta.status_code, 302)
    
    
class TestesPerfilUsuario(TestCase):


    def test_iniciar_Usuario_com_email_e_senha(self):
        usuario = Usuario(email="teste@teste")
        self.assertFalse(Usuario.email, None)
    
    def test_criacao_Lista_Vazia_de_Evento_para_Usuario_recem_criado(self):
        usuario = Usuario()
        self.assertEqual(usuario.get_eventos(), [])
    
    def test_criacao_Lista_Vazia_de_Inscricoes_para_Usuario_recem_criado(self):
        usuario = Usuario()
        self.assertEqual(usuario.get_inscricoes(), [])
    
    def test_nao_permitir_criacao_de_Evento_sem_nome(self): 
        Evento_sem_nome = Evento()
        self.assertEqual(Evento_sem_nome.nome,"")

    def test_email_nao_nulo(self):
        usuario = Usuario(email = '')
        self.assertFalse(usuario.email, '')

    def test_username_em_branco(self):
         usuario = Usuario(username = '')
         self.assertTrue(usuario.username, '')


class TesteInscricao(TestCase):


    def test_calcular_valor_correto_de_inscricao_dado_um_conjunto_de_atividades_adicionadas(self):  
        """
        Atualiza o valor da inscricao conforme a adicao de novas atividades ao pacote do usuario.
        """
        atividade = Atividade(valor=5.0)
        evento_criado = Evento()
        evento_criado.add_atividade(atividade)
        inscricao = Inscricao(evento = evento_criado)
        
        self.assertEqual(evento_criado.valor, inscricao.evento.valor)
    
    def test_nao_aceitar_incluir_inscricao_se_o_estado_ja_for_ATIVO(self):
        """
        Verifica o status_inscricao comparando se e ativa, e se for retorna erro.
        """  
        inscricao = Inscricao(status_inscricao="ativa")
        self.assertEqual(inscricao.status_inscricao, "ativa")
    

    


