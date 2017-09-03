from django.contrib.auth.models import User
from django.test import TestCase
from pagamento.models import *
from utils.models import *

import datetime

NAO_PAGO = 'NAO_PAGO'
inscricao = Inscricao()
evento = Evento(nome='Parque', valor=100.0)
inscricao.evento = evento
valor = 80.0
porc = 0.20
hora = '22:00:15'
usuario = Usuario(nome='Carlos', username='Carl', email='ju@go.com', data_de_entrada=datetime.date.today())
inscricao = Inscricao(status_inscricao=StatusInscricao.INATIVA, tipo_inscricao=TipoInscricao.PARCIAL, usuario=usuario, evento=evento)
periodo = Periodo.objects.create(data_inicio=datetime.date.today() + datetime.timedelta(20), data_fim=datetime.date.today() + datetime.timedelta(50))

class TestPagamento(TestCase):


    def criar_pagamento(self):
        pagamento = Pagamento(status=NAO_PAGO, usuario_recebimento=usuario, inscricao=inscricao, data=datetime.date.today(), valor_pagamento=valor, hora=hora)
        inscricao.evento = evento
        return pagamento

    def manter_status_inscricao_INATIVA_enquanto_aguarda_pagamento(self):
        pagamento = self.criar_pagamento()
        if (pagamento.status == StatusPagamento.NAO_PAGO):
            pagamento.inscricao.status_inscricao = StatusInscricao.INATIVA
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
    ######################
    def criar_cupom(self):
        cupom_cod = Cupom()
        codigo = cupom_cod.gerar_codigo_cupom()
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES, codigo_do_cupom=codigo,
                      evento=evento, periodo=periodo)
        return cupom

    def criar_cupom_sem_porcentagem_de_desconto(self):
        cupom = Cupom(status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES, evento=evento,
                      periodo=periodo)
        return cupom

    def criar_cupom_sem_status(self):
        cupom = Cupom(porcentagem=porc, tipo=TipoCupom.SIMPLES, evento=evento, periodo=periodo)
        return cupom

    def criar_cupom_sem_tipo(self):
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, evento=evento, periodo=periodo)
        return cupom

    def criar_cupom_sem_evento_relacionado(self):
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES,
                      periodo=periodo)
        return cupom

    def criar_cupom_sem_periodo(self):
        cupom = Cupom(porcentagem=porc, status=StatusCupom.ATIVO, tipo=TipoCupom.SIMPLES,
                      evento=evento)
        return cupom

    def cupom(self):
        return Cupom()
    ##################
    def criar_relacionamento_pagamento_cupom(self):
        relacionamento = PagamentoCupom(pagamento=self.criar_pagamento(), cupom=self.criar_cupom())
        relacionamento.cupom.evento.valor = relacionamento.cupom.evento.valor - relacionamento.cupom.receberDesconto(relacionamento.cupom.evento.valor)
        return relacionamento

    def pagamento_cupom(self):
        return  PagamentoCupom()