import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from .core import TestCore


class TesteResponsavelTrilha(TestCore):
    def test_validar_criacao_de_responsavel_trilha(self):
        self.create_responsavel_trilha()

    def test_criacao_reponsavel_trilha_com_responsavel(self):
        responsavel_trilha = self.create_responsavel_trilha()
        usuario = self.create_usuario()
        responsavel_trilha.responsavel = usuario
        self.assertEquals(responsavel_trilha.responsavel, usuario)

    def test_cricao_responsavel_trilha_com_trilha(self):
        responsavel_trilha = self.create_responsavel_trilha()
        trilha = self.create_trilha()
        responsavel_trilha.trilha = trilha
        self.assertEquals(responsavel_trilha.trilha, trilha)
