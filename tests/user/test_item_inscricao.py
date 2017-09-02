from tests.user.user import TestUser
from user.models import *
from core.models import *


class TesteItemInscricao(TestUser):
    def test_create_item_inscricao(self):
        self.create_item_inscricao()

    # def test_verificar_atividades_repetirdas_item_inscricao(self):
    #     item_inscricao = self.item_inscricao
    #     usuario = Usuario(username="Will", email="teste@teste", nome="Will")
    #     evento = Evento()
    #     inscricao = Inscricao()
    #     atividade = AtividadeAdministrativa(nome='credenciamento', descricao='abc', evento=evento)
    #     item_inscricao(inscricao=inscricao, atividade=atividade)
    #     item_inscricao(inscricao=inscricao, atividade=atividade)
    #     with self.assertRaises(ValidationError):
    #         item_inscricao.save()
