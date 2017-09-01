import unittest
from .utils import TestUtils
import datetime
from django.core.exceptions import ValidationError


class UtilsTeste(TestUtils):
    def test_create_periodo(self):
        self.create_periodo()

    def test_criar_periodo_data_inicio_menor_que_data_atual(self):
        periodo = self.periodo()
        periodo.data_inicio = datetime.date.today() - datetime.timedelta(1)
        periodo.data_fim = datetime.date.today()
        with self.assertRaises(ValidationError):
            periodo.save()

    def test_criar_periodo_data_fim_maior_que_data_inicio(self):
        periodo = self.periodo()
        periodo.data_inicio = datetime.date.today()
        periodo.data_fim = datetime.date.today() - datetime.timedelta(1)
        with self.assertRaises(ValidationError):
            periodo.save()
