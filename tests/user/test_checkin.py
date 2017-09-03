from tests.user.user import TestUser
from user.models import *
from core.models import *
from utils.models import *
import datetime


class TesteInscricao(TestUser):
    def test_create_checkin(self):
        self.create_checkin()

    def test_checkin_com_data_anterior_a_atual(self):
        checkin = CheckinItemInscricao(data=datetime.date(2014, 1, 1), hora="10:00:00", status=StatusCheckIn.VERIFICADO,
                                       gerente=self.evento.dono)
        with self.assertRaises(ValidationError):
            checkin.save()

    def test_checkin_com_status_NAO_VERIFICADO(self):
        checkin = self.checkin()
        checkin.status = StatusCheckIn.NAO_VERIFICADO
        self.assertTrue(StatusCheckIn.NAO_VERIFICADO, 'NAO_VERIFICADO')

    def test_checkin_gerente(self):
        checkin = self.checkin()
        checkin.gerente = self.new_user
        self.assertTrue(checkin.gerente, self.new_user)

