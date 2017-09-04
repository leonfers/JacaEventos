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

    def test_nome_em_branco(self):
        usuario = self.usuario()
        usuario.nome = ''
        self.assertEqual(usuario.nome, '')

    def test_iniciar_usuario_com_email_e_senha(self):
        usuario = self.usuario()
        usuario.email = "teste@teste"
        usuario.password = '123'
        self.assertEqual(usuario.email, "teste@teste")
        self.assertEqual(usuario.password, "123")

    def test_criacao_lista_vazia_de_eventos_para_usuario_recem_criado(self):
        usuario = self.usuario()
        sem_eventos = usuario.get_eventos()
        vazio = len(sem_eventos)
        self.assertEqual(vazio, 0)

    def test_criacao_lista_vazia_de_Inscricoes_para_usuario_recem_criado(self):
        usuario = self.usuario()
        sem_inscricoes = usuario.get_inscricoes()
        vazio = len(sem_inscricoes)
        self.assertEqual(vazio, 0)

