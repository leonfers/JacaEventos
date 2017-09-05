import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TesteEvento(TestCore):


    def test_validar_criacao_do_evento(self):
        self.create_evento()

    def test_qtd_atividades(self):
        self.create_evento()
        evento = Evento.objects.get(nome="Festival de Musica de Pedro II")
        self.assertEqual(len(evento.atividades), 0,'quantidade deve ser 0 ao criar um evento')
