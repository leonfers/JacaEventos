from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login
from user.views import RegistrarUsuario, PaginaInicial, ConclusaoInscricao, InscricaoEvento, MinhasInscricoesEmEventos

urlpatterns = [
    # urls relacionadas ao login de usuario
    url("^$", login, {"template_name": "login/form_login.html"}, name="login"),
    url("^logout/", logout_then_login, {"login_url": "login"}, name="logout_usuario"),
    url("^registrar/$", RegistrarUsuario.as_view(), name="registrar"),

    # pagina inicial do app
    url("^pagina_inicial/$", PaginaInicial.as_view(), name="pagina_inicial"),

    # urls relacionadas a interacao entre evento e usuario
    url("^inscricao_evento/(?P<inscricao_evento_id>[\d-]+)$", InscricaoEvento.as_view(), name="inscricao_evento"),
    url("^conclusao_inscricao/$", ConclusaoInscricao.as_view(), name="conclusao_inscricao"),
    url("^minhas_inscricoes_em_eventos/$", MinhasInscricoesEmEventos.as_view(), name="minhas_inscricoes_em_eventos"),
]
