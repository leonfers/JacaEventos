import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from user.models import *
from core.models import *

#
# class TesteLogin(TestCase):
#     def test_resposta_de_status_a_registrar(self):
#         resposta = self.client.get(reverse('registrar'))
#         self.assertEqual(resposta.status_code, 200)
#
#
# class TesteInicio(TestCase):
#     def test_resposta_de_status_a_pagina_inicial(self):
#         resposta = self.client.get(reverse('pagina_inicial'))
#         self.assertEqual(resposta.status_code, 302)
