from django.test import TestCase
from user.models import *
from utils.models import Periodo


class TestUser(TestCase):
    def create_user(self):
        usuario = Usuario(username="Will", email="teste@teste", nome="Will")
        return usuario

    def usuario(self):
        return Usuario()

    def create_item_inscricao(self):
        item_inscricao = ItemInscricao()
        return item_inscricao

    def item_inscricao(self):
        return ItemInscricao()

    def create_inscricao(self):
        inscricao = Inscricao
        return inscricao

    def inscricao(self):
        return Inscricao()

    def create_checkin(self):
        checkin = CheckinItemInscricao
        return checkin
