import unittest
from .pagamento import TestPagamento
from pagamento.models import *
import datetime
from django.core.exceptions import ValidationError


class PagamentoTeste(TestPagamento):


    def test_criar_pagamento(self):
        pagamento = self.criar_pagamento()
        self.assertTrue(pagamento.save())

    def test_criar_pagamento_com_valor_inferior_ao_de_evento(self):
        pagamento = self.criar_pagamento()
        pagamento.valor_pagamento -= pagamento.valor_pagamento * 0.5
        with self.assertRaises(ValidationError):
            pagamento.save()

    def test_invalidar_inscricao_enquanto_aguarda_pagamento(self):
        pagamento = self.manter_status_inscricao_INATIVA_enquanto_aguarda_pagamento()
        self.assertEqual(pagamento.status, StatusPagamento.NAO_PAGO)
        self.assertEqual(pagamento.inscricao.status_inscricao, StatusInscricao.INATIVA)
