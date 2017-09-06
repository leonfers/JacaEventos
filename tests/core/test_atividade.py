import datetime
from django.utils import timezone
from utils.models import *
from user.models import *
from core.models import *
from core.enum import *
from .core import TestCore


class TesteAtividade(TestCore):
    def test_validar_criacao_de_atividade(self):
        self.create_atividade()

    def test_criacao_atividade_continua(self):
        self.create_atividade_continua()

    def test_criacao_atividade_administrativa(self):
        self.create_atividade_administrativa()

    def test_create_atividade_padrao(self):
        self.create_atividade_padrao()

    def test_atividade_sem_descricao(self):
        atividade = self.create_atividade()
        atividade.descricao = ''
        self.assertEquals(atividade.descricao, '')

    def test_atividade_com_evento(self):
        atividade = self.create_atividade()
        evento = self.create_evento()
        atividade.evento = evento
        self.assertEquals(atividade.evento, evento)

    def test_atividade_com_data(self):
        atividade = self.create_atividade()

        data = datetime.date.today()
        hora_fim = datetime.datetime.now().time()
        horario_atividade = HorarioAtividade.objects.create(data_inicio=data, data_fim=data, hora_inicio=hora_fim,
                                                            hora_fim=hora_fim)
        horario_atividade.save()
        atividade.horario_atividade = horario_atividade



