import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import *

class TestarPagamentos(TestCase):


    def pagamento_negativo(self):
        pagamento_invalido = Pagamento(valor_pagamento = 0)
        self.assertIs(pagamento_invalido.avaliar_pagamento(), False)
    
    def status_pagamento_em_espera(self):
        status_pagamento_invalido = Pagamento(status_pagamento='False')
        self.assertIs(status_pagamento_invalido.avaliar_status_pagamento(), True)