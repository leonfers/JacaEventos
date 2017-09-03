from tests.user.user import TestUser
from user.models import *
from utils.models import *
from core.models import *
from django.core.exceptions import ValidationError


class TesteItemInscricao(TestUser):
    def test_criar_item_inscricao(self):
        def test_criar_item_inscricao(self):
            ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)

        def test_verificar_atividade_pertence_ao_evento(self):
            item_inscricao = ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)

            self.assertEqual(item_inscricao.atividade.evento, item_inscricao.inscricao.evento)

        def test_verificar_atividade_nao_pertence_ao_evento(self):
            item_inscricao = ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)
            self.assertFalse(item_inscricao.inscricao.evento == self.evento)

        def test_nao_permitir_se_inscrever_em_uma_atividade_que_ja_esta_inscrito(self):
            item_inscricao = ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)
            with self.assertRaises(ValidationError):
                ItemInscricao.objects.create(inscricao=item_inscricao.inscricao, atividade=item_inscricao.atividade)
