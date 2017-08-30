import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


def test_tipo_relacionamento_nao_estabelecido(self):
    relacionamento = EventoInstituicao(tipo_relacionamento='')
    self.assertEqual(relacionamento.tipo_relacionamento, None)

def test_validar_relacionamento(self):
    evento = Evento()
    instituicao = Instituicao(nome="Teste")
    relacionamento = EventoInstituicao(instituicao=instituicao, evento_relacionado=evento)
    self.assertEqual(relacionamento.evento_relacionado, evento)
    self.assertEqual(relacionamento.instituicao, instituicao)