import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import *
from core.models import *

class TestarPagamentos(TestCase):


    def test_pagamento_negativo(self):
        pagamento_invalido = Pagamento(valor_pagamento = 0)
        self.assertEqual(pagamento_invalido.valor_pagamento, 0)
            
    def test_status_pagamento_em_espera(self):
        status_pagamento_invalido = Pagamento(status='NAO_PAGO')
        self.assertTrue(status_pagamento_invalido.status, 'NAO PAGO')
    
    def test_calcular_valor_correto_de_quando_se_utilizar_um_cupom_promocional_individual(self):
        pagamento_feito = Pagamento(valor_pagamento=80.0)
        evento = Evento(valor=100.0)
        cupom_usado = Cupom(evento)
        pagamento_cupom = PagamentoCupom(pagamento=pagamento_feito, cupom=cupom_usado)
        
        self.assertEqual(pagamento_feito.valor_pagamento, evento.valor - (evento.valor * 0.2))
        

        