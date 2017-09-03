from tests.user.user import TestUser
from user.models import *
from utils.models import *
from core.models import *
from django.core.exceptions import ValidationError


usuario = Usuario(username="will", email="will@gmail.com", nome="Wildrimak",
                       password="pbkdf2_sha256$36000$kG8PeNu2p4yf$TH6YRbpIXPoua4tOOkkubhD9Gdc8Oc850//xu8ykcEM=")
endereco = Endereco(pais="Brasil", estado="Piaui", logradouro="Praca", numero="N/A", cidade="Teresina",
                    bairro="Macauba", cep="64532-123")
periodo = Periodo(data_inicio=datetime.date.today(), data_fim=datetime.date(2018, 1, 1))
evento = Evento(nome="Festival de Musica de Pedro II",
                descricao="Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura",
                valor=0, tipo_evento=TipoEvento.SEMINARIO, periodo=periodo, endereco=endereco, dono=usuario)
atividade = AtividadeAdministrativa(nome="Credenciamento", descricao="Credenciamento dos participantes",
                                    evento=evento)
inscricao = Inscricao(usuario=usuario, evento=evento)


class TesteItemInscricao(TestUser):
    # py manage.py dumpdata - o test_fixtures.json
    fixtures = ['test_fixtures.json']

    def test_criar_item_inscricao(self):
        self.item_inscricao()

    def test_verificar_atividade_pertence_ao_evento(self):
        item_inscricao = self.item_inscricao()
        item_inscricao.incricao = inscricao
        item_inscricao.atividade = atividade
        item_inscricao.save()

        self.assertEqual(item_inscricao.atividade.evento, item_inscricao.inscricao.evento)

    def test_verificar_atividade_nao_pertence_ao_evento(self):
        item_inscricao = ItemInscricao.objects.get(id=1)
        evento = Evento.objects.get(id=4)
        self.assertFalse(item_inscricao.inscricao.evento == evento)

    def test_nao_permitir_se_inscrever_em_uma_atividade_que_ja_esta_inscrito(self):
        item_inscricao = self.item_inscricao()
        item = ItemInscricao.objects.get(id=1)
        atividade = item.atividade
        with self.assertRaises(ValidationError):
            ItemInscricao.objects.create(inscricao=item.inscricao, atividade=atividade)
