from enumfields import Enum, EnumField


class TipoResponsavelAtividade(Enum):
    NAO_VERIFICADO = "nao_verificado"
    PRESENTE = "presente"
    AUSENTE = "ausente"


class StatusInscricao(Enum):
    ATIVA = "ativa"
    INATIVA = "INATIVA"


class TipoInscricao(Enum):
    COMPLETA = "COMPLETA"
    PARCIAL = "PARCIAL"


class StatusCheckIn(Enum):
    VERIFICADO = "VERIFICADO"
    NAO_VERIFICADO = "NAO_VERIFICADO"
    AUSENTE = "AUSENTE"
