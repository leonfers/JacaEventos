import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


def test_tag_sem_evento(self):
    evento_teste = Evento()
    tag_sem_evento = Tag_Evento(evento=evento_teste)
    self.assertFalse(tag_sem_evento.evento.nome, '')