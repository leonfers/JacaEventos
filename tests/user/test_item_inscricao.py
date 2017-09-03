from tests.user.user import TestUser
from user.models import *
from utils.models import *
from core.models import *
from django.core.exceptions import ValidationError


class TesteItemInscricao(TestUser):
    # py manage.py dumpdata - o test_fixtures.json
    fixtures = ['test_fixtures.json']

    def test_criar_item_inscricao(self):
        self.inscricao()

    def test_verificar_atividade_pertence_ao_evento(self):
        item_inscricao = ItemInscricao.objects.get(id=1)
        self.assertEqual(item_inscricao.inscricao.evento, item_inscricao.atividade.evento)

    def test_verificar_atividade_nao_pertence_ao_evento(self):
        item_inscricao = ItemInscricao.objects.get(id=1)
        evento = Evento.objects.get(id=4)
        self.assertFalse(item_inscricao.inscricao.evento, evento)

    def test_nao_permitir_se_inscrever_em_uma_atividade_que_ja_esta_inscrito(self):
        inscricao = Inscricao.objects.get(id=1)
        atividade = inscricao.itens.get(id=1)
        atividade = atividade.atividade
        with self.assertRaises(ValidationError):
            ItemInscricao.objects.create(inscricao=inscricao, atividade=atividade)
