import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TesteAtividade(TestCore):


    def test_validar_criacao_de_atividade(self):
        self.create_atividade()

