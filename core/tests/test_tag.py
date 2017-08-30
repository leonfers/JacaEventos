import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


def test_tag_de_nome_em_branco(self):
    tag_de_nome_nula = Tag(nome='')
    self.assertEqual(tag_de_nome_nula.nome, '')