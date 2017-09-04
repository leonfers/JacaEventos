from enumfields import Enum, EnumField


class StatusEvento(Enum):
    INSCRICOES_ABERTAS = 'inscricoes_abertas'
    INSCRICOES_FECHADAS = 'incricoes_fechado'
    ENCERRADO = 'encerrado'
    ANDAMENTO = 'andamento'


class TipoAtividade(Enum):
    PALESTRA = 'palestra'
    MINICURSO = 'minicurso'
    WORKSHOP = 'workshop'
    MESA_REDONDA = 'mesa_redonda'
    PADRAO = 'padrao'


class TipoEvento(Enum):
    CONGRESSO = 'congresso'
    SEMANA = 'semana'
    SEMINARIO = 'seminario'
    PADRAO = 'padrao'


class TipoInstituicao(Enum):
    APOIO = 'apoio'
    PATROCINIO = 'patrocinio'
    REALIZACAO = 'realizacao'
    PADRAO = 'padrao'


class CategoriaAtividade(Enum):
    LOCAL = 'local'
    SATELITE = 'satelite'


class TipoResponsavel(Enum):
    PALESTRANTE = 'palestrantes'
    PROFESSOR = 'professor'
    STAFF = 'staff'
    PADRAO = 'padrao'


class StatusAtividade(Enum):
    ATIVA = 'ativa'
    INATIVA = 'inativa'


class TipoEspacoFisico(Enum):
    SALA = 'sala'
    LABORATORIO = 'laboratorio'
    AUDITORIO = 'auditorio'
    PREDIO = 'predio'
    AR_LIVRE = 'ar_livre'
    PADRAO = 'padrao'


class TipoGerencia(Enum):
    DONO = 'dono'
    STAFF = 'staff'
    PADRAO = 'padrao'
