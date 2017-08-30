from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from pagamento.models import *
from core.models import *
from utils.models import *


def test_pagamento_negativo(self):
    pagamento_invalido = Pagamento(valor_pagamento = 0)
    self.assertEqual(pagamento_invalido.valor_pagamento, 0)

def test_status_pagamento_em_espera(self):
    status_pagamento_invalido = Pagamento(status='NAO_PAGO')
    self.assertEqual(status_pagamento_invalido.status, 'NAO PAGO')

def test_calcular_valor_correto_de_quando_se_utilizar_um_cupom_promocional_individual(self):
    pagamento_feito = Pagamento(valor_pagamento=80.0)
    evento = Evento(valor=100.0)
    cupom = Cupom(porcentagem=0.20, evento = evento)
    pagamento_cupom = PagamentoCupom(pagamento=pagamento_feito, cupom=cupom)
    self.assertEqual(pagamento_feito.valor_pagamento, evento.valor - cupom.receberDesconto(evento.valor))