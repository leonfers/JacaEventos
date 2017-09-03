import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from tests.user.user import TestUser
from user.models import *
from core.models import *


class TesteUsuario(TestUser):

    def test_create_usuario(self):
        usuario = self.create_user()
        # usuario = Usuario(username="Will", email="teste@teste", nome="Will")
        self.assertEqual(usuario.email, 'teste@teste')
        self.assertEqual(usuario.username, 'Will')
        self.assertEqual(usuario.nome, 'Will')

    def test_username_em_branco(self):
         usuario = self.usuario()
         usuario.username = ''
         self.assertEqual(usuario.username, '')

    def test_email_em_branco(self):
        usuario = self.usuario()
        usuario.email = ''
        self.assertEqual(usuario.email, '')

    def test_iniciar_Usuario_com_email_e_senha(self):
        usuario = self.usuario()
        usuario.email = "teste@teste"
        self.assertEqual(usuario.email, "teste@teste")

    def test_criacao_Lista_Vazia_de_Eventos_para_Usuario_recem_criado(self):
        usuario = self.usuario()
        sem_eventos = usuario.get_eventos()
        vazio = len(sem_eventos)
        self.assertEqual(vazio, 0)

    def test_criacao_Lista_Vazia_de_Inscricoes_para_Usuario_recem_criado(self):
        usuario = self.usuario()
        sem_inscricoes = usuario.get_inscricoes()
        vazio = len(sem_inscricoes)
        self.assertEqual(vazio, 0)
