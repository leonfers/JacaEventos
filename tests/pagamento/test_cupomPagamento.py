import unittest
from .pagamento import TestPagamento
from pagamento.models import *
import datetime
from django.core.exceptions import ValidationError


class CupomPagamentoTeste(TestPagamento):


    def test_validar_relacao_pagamento_cupom(self):
        relacionamento = self.criar_relacionamento_pagamento_cupom()
        with self.assertRaises(ValidationError):
            relacionamento.save()

    def test_avaliar_valor_pos_desconto(self):
        relacionamento = self.criar_relacionamento_pagamento_cupom()
        valor_extra = relacionamento.cupom.evento.valor/4
        print ("O valor no rel e ", relacionamento.cupom.evento.valor)
        self.assertEquals(relacionamento.pagamento.valor_pagamento, relacionamento.cupom.evento.valor + valor_extra)