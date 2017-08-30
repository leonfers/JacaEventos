import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from user.models import *
from core.models import *


class TesteUsuario(TestCase):


    def test_validacao_cadastro_usuario(self):
        usuario = Usuario(username="Will", email="teste@teste", nome="Will")
        self.assertEqual(usuario.email, 'teste@teste')
        self.assertEqual(usuario.username, 'Will')
        self.assertEqual(usuario.nome, 'Will')

    def test_iniciar_Usuario_com_email_e_senha(self):
        usuario = Usuario(email="teste@teste")
        self.assertEqual(usuario.email, "teste@teste")
    
    def test_criacao_Lista_Vazia_de_Eventos_para_Usuario_recem_criado(self):
        usuario = Usuario()
        sem_eventos = usuario.get_eventos()
        vazio = len(sem_eventos)
        self.assertEqual(vazio, 0)
    
    def test_criacao_Lista_Vazia_de_Inscricoes_para_Usuario_recem_criado(self):
        usuario = Usuario()
        sem_inscricoes = usuario.get_inscricoes()
        vazio = len(sem_inscricoes)
        self.assertEqual(vazio, 0)