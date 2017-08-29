import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


class TesteTagUsuario(TestCase):


    def test_tag_sem_usuario(self):
        usuario_teste = Usuario()
        tag_sem_usuario = Tag_Usuario(usuario=usuario_teste)
        self.assertFalse(tag_sem_usuario.usuario.nome, '')
