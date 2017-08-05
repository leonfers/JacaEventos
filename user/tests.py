import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import *

class TestesPerfilUsuario(TestCase):


    def test_email_nao_nulo(self):
        email_nulo = Usuario(email = '')
        self.assertIs(email_nulo.verificar_email(), False)

    def test_nome_em_branco(self):
         nome_em_branco = Usuario(username='')
         self.assertIs(nome_em_branco.verificar_nome(), False)

    def test_data_de_entrada_futura(self):
        data_futura = timezone.now() + datetime.timedelta(days=days)
        self.assertIs(data_futura.verificar_data(), False)
