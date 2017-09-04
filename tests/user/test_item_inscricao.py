from tests.user.user import TestUser
from user.models import *
from utils.models import *
from core.models import *
from django.core.exceptions import ValidationError


class TesteItemInscricao(TestUser):
    def test_criar_item_inscricao(self):
        ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)

    def test_verificar_atividade_pertence_ao_evento_inscrito(self):
        item_inscricao = ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)
        self.assertEqual(item_inscricao.atividade.evento, item_inscricao.inscricao.evento)

    def test_inscricao_inativa(self):
        inscricao = self.inscricao
        inscricao.status_inscricao = StatusInscricao.INATIVA
        with self.assertRaises(ValidationError):
            item_inscricao = ItemInscricao.objects.create(inscricao=inscricao, atividade=self.atividade)
            item_inscricao.save()

    def test_verificar_atividade_nao_pertence_ao_evento(self):
        new_inscricao = Inscricao(usuario=self.new_user, evento=self.new_evento)
        with self.assertRaises(ValidationError):
            new_inscricao.save()

    def test_nao_permitir_se_inscrever_em_uma_atividade_que_ja_esta_inscrito(self):
        item_inscricao = ItemInscricao.objects.create(inscricao=self.inscricao, atividade=self.atividade)
        with self.assertRaises(ValidationError):
            ItemInscricao.objects.create(inscricao=item_inscricao.inscricao, atividade=item_inscricao.atividade)
