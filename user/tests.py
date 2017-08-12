import datetime
import pytest

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import *
from core.models import *

class TestesPerfilUsuario(TestCase):


    def func(x):
        return x + 1

    def test_answer():
        assert func(3) == 5

    def Iniciar_Usuario(self):
        Usuario.objects.create_user(email="teste@teste", senha="testando")
    
    def Criacao_Lista_Vazia_de_Evento_Para_Usuario_recem_criado(self):
        usuario = Usuario()
        self.assertTrue(usuario.get_eventos(self), [])
    
    def test_nao_permitir_criacao_de_Evento_sem_nome(self):
        
        Evento_sem_nome = Evento()
        self.assertEqual(Evento_sem_nome.nome,"")

    def test_email_nao_nulo(self):
        usuario = Usuario(email = '')
        self.assertIs(usuario.get_email_field_name, False)

    def test_username_em_branco(self):
         usuario = Usuario(username = '')
         self.assertFalse(usuario.username, '')


class TesteInscricao(TestCase):


    def Calcular_valor_correto_de_inscricao_dado_um_conjunto_de_atividades_adicionadas(self):
        
    """
    Atualiza o valor da inscricao conforme a adicao de novas atividades ao pacote do usuario.
    """
    atividade = Atividade(valor=5.0)
    evento_criado = Evento()
    evento_criado.add_atividade(self, atividade)
    inscricao = Inscricao(evento = evento_criado)
    
    self.assertEqual(evento_criado.valor, inscricao.evento.valor)
        
    

    


