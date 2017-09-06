import unittest
from .pagamento import TestPagamento
import datetime
from django.core.exceptions import ValidationError

class CupomTeste(TestPagamento):

    def test_create_cupom(self):
        self.create_cupom()