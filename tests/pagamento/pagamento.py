from django.contrib.auth.models import User
from django.test import TestCase
from pagamento.models import *
from utils.models import *

import datetime

NAO_PAGO = 'NAO_PAGO'
inscricao = Inscricao()
valor = 55.50
porc = 0.20
periodo = Periodo.objects.create(data_inicio=datetime.date.today(), data_fim=datetime.date.today() + datetime.timedelta(1))

class TestPagamento(TestCase):


    def criar_pagamento(self):
        pagamento = Pagamento(status=NAO_PAGO, usuario_recebimento=usuario, inscricao=inscricao, data=datetime.date.today(), valor_pagamento=valor)
        return pagamento

    def criar_pagamento_sem_status(self):
        pagamento = Pagamento(usuario_recebimento=usuario, inscricao=inscricao, data=datetime.date.today(), valor_pagamento=valor)
        return pagamento

    def criar_pagamento_sem_usuario_recebimento(self):
        pagamento = Pagamento(status=NAO_PAGO, inscricao=inscricao, data=datetime.date.today(), valor_pagamento=valor)
        return pagamento

    def criar_pagamento_sem_inscricao(self):
        pagamento = Pagamento(status=NAO_PAGO, usuario_recebimento=usuario, data=datetime.date.today(), valor_pagamento=valor)
        return pagamento

    def criar_pagamento_sem_data(self):
        pagamento = Pagamento(status=NAO_PAGO, usuario_recebimento=usuario, inscricao=inscricao, valor_pagamento=valor)
        return pagamento

    def criar_pagamento_sem_valor_definido(self):
        pagamento = Pagamento(status=NAO_PAGO, usuario_recebimento=usuario, inscricao=inscricao, data=datetime.date.today())
        return pagamento

    def pagamento(self):
        return Pagamento()

    def criar_cupom(self):
        evento = Evento()
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES,
                      evento=evento, periodo=periodo)
        return cupom

    def criar_cupom_sem_porcentagem_de_desconto(self):
        evento = Evento()
        cupom = Cupom(status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES, evento=evento,
                      periodo=periodo)
        return cupom

    def criar_cupom_sem_status(self):
        evento = Evento()
        cupom = Cupom(porcentagem=porc, tipo=TipoCupom.SIMPLES, evento=evento, periodo=periodo)
        return cupom

    def criar_cupom_sem_tipo(self):
        evento = Evento()
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, evento=evento, periodo=periodo)
        return cupom

    def criar_cupom_sem_evento_relacionado(self):
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES,
                      periodo=periodo)
        return cupom

    def criar_cupom_sem_periodo(self):
        evento = Evento()
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES,
                      evento=evento)
        return cupom


    def cupom(self):
        return Cupom()

    def criar_relacionamento_pagamento_cupom(self):

        relacionamento = PagamentoCupom(pagamento=self.criar_pagamento(), cupom=self.criar_cupom())
        return relacionamento

    def pagamento_cupom(self):
        return  PagamentoCupom()