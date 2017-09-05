import datetime
import pytest
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from utils.models import *
from core.models import *


class TesteEspacoFisico(TestCase):


    def test_controle_espaco_fisico(self):
        evento = Evento(nome="Teste")
        evento.save()
        atividade = AtividadePadrao(nome="Poker")
        atividade.espaco_fisico = espaco
        espaco = EspacoFisico(nome = 'nome', tipoEspacoFisico = 'padrao', capacidade = 9999, evento = evento)
        espaco.save()
        atividade.espaco_fisico = espaco
        self.assertFalse(espaco.tipoEspacoFisico == '')

    def test_impedir_que_atividades_ocorram_no_mesmo_espaco_fisico_com_tempos_sobrepostos(self):
        evento = Evento(nome="Teste")
        horario_definido= Horario(data = '2017-09-15', hora_inicio = '12:30:00', hora_fim = '22:30:00')
        atividade = AtividadePadrao(nome="Poker", horario=horario_definido)
        atividade_secundaria = AtividadePadrao(nome="Xadrez", horario=horario_definido)
        espaco = EspacoFisico(nome='nome', tipoEspacoFisico='padrao', capacidade=9999, evento=evento)
        atividade.espaco_fisico = espaco
        atividade_secundaria.espaco_fisico = espaco

        evento.add_atividade(atividade);
        evento.add_atividade(atividade_secundaria)

    def test_permitir_usuario_usar_um_espaco_fisico_dentro_de_um_espaco_fisico(self):
        evento = Evento(nome="Teste")
        atividade = AtividadePadrao(nome="Poker")
        espaco = EspacoFisico(nome='nome', tipoEspacoFisico='padrao', capacidade=9999, evento=evento,
                              atividade=atividade)
        espaco_interno = EspacoFisico(nome='Interno', tipoEspacoFisico='padrao', capacidade=99, evento=evento,
                              atividade=atividade)
        self.assertTrue(espaco_interno in espaco)
        """
        Ex.: O Usuário cria um espaço físico IFPI. Depois criar um espaço Físico
        Prédio B e indica que ele é no IFPI. Depois cria um Laboratório B3-18 e indica
        que fica no espaço físico Prédio B)
        """
