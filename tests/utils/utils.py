from django.contrib.auth.models import User
from django.test import TestCase
from utils.models import Periodo
import datetime


class TestUtils(TestCase):

    def create_periodo(self):
        periodo = Periodo.objects.create(data_inicio=datetime.date.today(), data_fim=datetime.date.today() + datetime.timedelta(1))
        return periodo

    def periodo(self):
        return Periodo()
