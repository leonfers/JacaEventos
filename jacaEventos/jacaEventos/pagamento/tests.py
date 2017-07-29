import datetime

from django.utils import timezone
from django.test import TestCase

from jacaEventos.pagamento.models import Cupom, Pagamento

# Create your tests here.
class ModeloDeTesteParaPagamento(TestCase):
    def test_negar_caso_valor_seja_negativo(self):
        pagamento = Pagamento(valor_pagamento = -1)
        self.assertIs(pagamento.avaliar_valor_pagamento(), False)

class ModeloDeTesteParaCupom(TestCase):
    def test_avaliar_se_codigo_cupom_nao_e_nulo(self):
        cupom = Cupom(codigo_do_cupom = "")
        self.assertIs(cupom.avaliar_codigo_cupom(), False)