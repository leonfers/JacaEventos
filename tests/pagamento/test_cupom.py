from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from pagamento.models import *
from core.models import *
from utils.models import *


class TesteCupons(TestCase):


    def test_alterar_status_do_cupom_quando_expirar_periodo_do_evento(self):
        periodo = Periodo(data_inicio='2017-08-20', data_fim='2017-08-24')
        cupom = Cupom(periodo)
        dias = periodo.data_fim.split('-')
        days = 30
        if (timezone.now().day > int(dias[2])):
            self.assertEqual(cupom.status, 'INATIVO')
        else:
            self.assertEqual(cupom.status, 'ATIVO')
    
    def test_tipo_cupom_SIMPLES(self):
        cupom_teste = Cupom(tipo='SIMPLES')
        self.assertEqual(cupom_teste.tipo, 'SIMPLES')
    
    def test_tipo_cupom_AUTOMATICO(self):
        cupom_teste = Cupom(tipo='AUTOMATICO')
        self.assertEqual(cupom_teste.tipo, 'AUTOMATICO')