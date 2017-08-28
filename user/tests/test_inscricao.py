import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from user.models import *
from core.models import *


class TesteInscricao(TestCase):


    def test_calcular_valor_correto_de_inscricao_dado_um_conjunto_de_atividades_adicionadas(self):
        atividade = Atividade(valor=5.0)
        evento_criado = Evento()
        evento_criado.add_atividade(atividade)
        inscricao = Inscricao(evento = evento_criado)
        self.assertEqual(evento_criado.valor, inscricao.evento.valor)
    
    def test_nao_aceitar_incluir_inscricao_se_o_estado_do_evento_ja_for_ATIVO(self):
        evento = Evento()
        inscricao = Inscricao(status_inscricao='ativa')
        self.assertFalse(inscricao.evento, evento)
    
