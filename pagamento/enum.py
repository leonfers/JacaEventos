from enumfields import Enum, EnumField

class StatusPagamento(Enum):
    PAGO = 'PAGO'
    NAO_PAGO = 'NAO_PAGO'


class StatusCupom(Enum):
    ATIVO = 'ATIVO'
    INATIVO = 'INATIVO'


class TipoCupom(Enum):
    SIMPLES = 'SIMPLES'
    AUTOMATICO = 'AUTOMATICO'
