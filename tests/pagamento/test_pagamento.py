import unittest
from .pagamento import TestPagamento
from pagamento.models import *
import datetime
from django.core.exceptions import ValidationError


class PagamentoTeste(TestUtils):


    def test_criar_pagamento(self):
        self.criar_pagamento()

    def test_criar_pagamento_com_valor_inferior_ao_de_evento(self):
        pagamento = self.pagamento()
        pagamento.valor_pagamento -= 20
        with self.assertRaises(ValidationError):
            pagamento.save()

    def test_nao_permitir_relacao_cupom_com_evento_quando_esse_for_AUTOMATICO(self):
        relacionamento = TestPagamento.criar_relacionamento_pagamento_cupom()
        relacionamento.cupom.tipo = TipoCupom.AUTOMATICO
        with self.assertRaises(ValidationError):
            relacionamento.save()

    def test_invalidar_inscricao_enquanto_aguarda_pagamento(self):
        pagamento = TestPagamento.pagamento()
        self.assertEquals(pagamento.status, StatusPagamento.NAO_PAGO)
        self.assertEquals(pagamento.inscricao.status_inscricao, StatusInscricao.INATIVA)

    def test_validar_relacao_pagamento_cupom(self):
        relacionamento = TestPagamento.criar_relacionamento_pagamento_cupom()
        with self.assertRaises(ValidationError):
            relacionamento.save()

    def test_avaliar_valor_pos_desconto(self):
        relacionamento = TestPagamento.criar_relacionamento_pagamento_cupom()
        self.assertEquals(relacionamento.pagamento, relacionamento.cupom.evento.valor)

    def test_validar_cupom(self):
        cupom = TestPagamento.criar_cupom()
        self.assertEquals(len(cupom.codigo_do_cupom), 14)