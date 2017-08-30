import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


def test_permitir_concomitancia_de_atividades(self):
        """
        Agenda: Deve ser possível gerar a agenda do evento:
        o Com atividades ordenadas por dia/horário, considerando Espaço Físico, Trilha,
        Tags etc.
        """