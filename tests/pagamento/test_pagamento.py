import unittest
from .pagamento import TestPagamento
from pagamento.models import *
from pagamento.enum import *
import datetime
from django.core.exceptions import ValidationError

class PagamentoTeste(TestPagamento):

    def test_create_cupom(self):
        self.get_pagamento()

    def test_criar_pagamento_com_status_nao_pago(self):
        pagamento = self.create_pagamento()
        pagamento.status = StatusPagamento.NAO_PAGO
        self.assertEquals(pagamento.status,StatusPagamento.NAO_PAGO)

    def test_criar_pagamento_com_data_e_hora(self):
        pagamento = self.create_pagamento()
        data = datetime.date.today()
        hora = datetime.datetime.now().time()
        pagamento.data = data
        pagamento.hora = hora
        self.assertEquals(pagamento.data, data)
        self.assertEquals(pagamento.hora, hora)

