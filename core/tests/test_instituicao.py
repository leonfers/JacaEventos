import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


class TesteInstituicao(TestCase):


    def test_campo_nome_Instituicao_em_branco(self):
        instituicao = Instituicao(nome='Nova')
        self.assertEqual(instituicao.__str__(), 'Nova')