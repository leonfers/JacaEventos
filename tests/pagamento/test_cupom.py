import unittest
from .pagamento import TestPagamento
from pagamento.models import *
import datetime
from django.core.exceptions import ValidationError


class CupomTeste(TestPagamento):


    def test_nao_permitir_relacao_cupom_com_evento_quando_esse_for_AUTOMATICO(self):
        relacionamento = self.criar_relacionamento_pagamento_cupom()
        relacionamento.cupom.tipo = TipoCupom.AUTOMATICO
        with self.assertRaises(ValidationError):
            relacionamento.save()

    def test_validar_cupom(self):
        cupom = self.criar_cupom()
        self.assertEquals(len(cupom.codigo_do_cupom), 14)