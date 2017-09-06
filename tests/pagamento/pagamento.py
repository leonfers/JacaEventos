from django.test import TestCase
from user.models import *
from utils.models import *
from core.models import *
from pagamento.models import *

NOME_EVENTO = "Festival de Musica de Pedro II"


# instanciando classes para facilitar testes
class TestPagamento(TestCase):
    def get_cupom(self):
        usuario = Usuario()
        usuario.username = "will"
        usuario.email = "will@gmail.com"
        usuario.nome = "Wildrimak"
        usuario.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
        usuario.save()

        evento = Evento()
        evento.nome = NOME_EVENTO
        evento.descricao = "Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura"
        evento.valor = 0
        evento.tipo_evento = TipoEvento.SEMINARIO

        endereco = Endereco()
        endereco.pais = "Brasil"
        endereco.estado = "Piaui"
        endereco.logradouro = "Praca"
        endereco.numero = "N/A"
        endereco.cidade = "Teresina"
        endereco.bairro = "Macauba"
        endereco.cep = "64532-123"
        endereco.save()

        periodo = Periodo()
        periodo.data_inicio = datetime.date.today()
        periodo.data_fim = datetime.date(2018, 1, 1)
        periodo.save()

        evento.periodo = periodo
        evento.endereco = endereco
        evento.dono = usuario
        evento.save()

        # criando um cupom
        cupom = Cupom()
        cupom.evento = evento
        cupom.porcentagem = 10
        cupom.tipo = TipoCupom.SIMPLES
        cupom.save()

    def get_pagamento(self):
        self.get_cupom()
        evento = Evento.objects.get(nome=NOME_EVENTO)
        cupom = Cupom.objects.all()[0]
        # Criando usuario para cliente em plataforma
        usuario_inscrito = Usuario()
        usuario_inscrito.username = "Kassio"
        usuario_inscrito.email = "kassio@gmail.com"
        usuario_inscrito.nome = "Kassio"
        usuario_inscrito.password = "pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM="
        usuario_inscrito.save()

        # criando uma inscricao
        inscricao = Inscricao()
        inscricao.status_inscricao = StatusInscricao.ATIVA
        inscricao.tipo_inscricao = TipoInscricao.PARCIAL
        inscricao.usuario = usuario_inscrito
        inscricao.evento = evento
        inscricao.save()

        pagamento = Pagamento.objects.create(usuario_recebimento=evento.dono, inscricao=inscricao,
                                             cupom_codigo=cupom.codigo)

    def create_pagamento(self):
        return Pagamento()

    def create_cupom(self):
        return Cupom()

