from tests.user.user import TestUser
from user.models import *
from utils.models import *
from core.models import *


class TesteItemInscricao(TestUser):
    def test_create_item_inscricao(self):
        self.create_item_inscricao()

    def test_verificar_atividades_repetidas_item_inscricao(self):
        item_inscricao = self.item_inscricao()
        item_inscricao2 = self.item_inscricao()

        usuario = Usuario(username="Will", email="teste@teste", nome="Will")

        endereco = Endereco(pais="Brasil", estado="Piaui", logradouro="Praca", numero="N/A", cidade="Teresina",
                            bairro="Macauba", cep="64532-123")
        periodo = Periodo(data_inicio=datetime.date.today(), data_fim=datetime.date(2018, 1, 1))
        evento = Evento(nome="Festival de Musica de Pedro II",
                        descricao="Evento criado no intuito de promover o turismo em pedro II alem de disseminar cultura",
                        valor=0, tipo_evento=TipoEvento.SEMINARIO, periodo=periodo, endereco=endereco, dono=usuario)
        atividade = AtividadeAdministrativa(nome='credenciamento', descricao='abc', evento=evento)
        inscricao = Inscricao(status_inscricao=StatusInscricao.ATIVA, tipo_inscricao=TipoInscricao.PARCIAL,
                              usuario=usuario, evento=evento)
        # item_inscricao = self.item_inscricao

        item_inscricao.inscricao = inscricao
        item_inscricao.atividade = atividade

        item_inscricao2.inscricao = inscricao
        item_inscricao2.atividade = atividade

        with self.assertRaises(ValidationError):
            item_inscricao.save()
            item_inscricao2.save()
