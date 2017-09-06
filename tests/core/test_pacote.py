import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TestePacote(TestCore):
    # def test_validar_criacao_de_pacote(self):
    #     self.get_pacote()

    def test_validar_criacao_pacote(self):
        self.create_pacote()
