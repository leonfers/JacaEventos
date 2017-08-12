import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import *

class TestarPagamentos(TestCase):


    def test_pagamento_negativo(self):
        pagamento_invalido = Pagamento(valor_pagamento = 0)
        self.assertEqual(pagamento_invalido.valor_pagamento, 0)
    
    def test_pagamento_como_texto(self):
        teste_pagamento = "dinheiro"
        self.assertEqual(teste_pagamento, Pagamento.valor_pagamento)

        with self.assertRaises(TypeError):
            print ("Adição de caracteres não numéricos a pagamento.")
            
    def test_status_pagamento_em_espera(self):
        status_pagamento_invalido = Pagamento(status_pagamento=False)
        self.assertIs(status_pagamento_invalido.status_pagamento, False)
    
    def Calcular_valor_correto_de_quando_se_utilizar_um_cupom_promocional_individual(self):
        pagamento_feito = Pagamento()
        evento = Evento(valor=100.0)
        cupom_usado = Cupom(evento)
        pagamento_cupom = PagamentoCupom(pagamento=pagamento_feito, cupom=cupom_usado)
        
        self.assertEqual(pagamento_feito.valor_pagamento, evento - (evento * 0.2))
        

        