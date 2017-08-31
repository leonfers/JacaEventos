from django.conf.urls import url
from django.contrib.auth.views import login, logout, logout_then_login
from user.views import Registrar, PaginaInicial, ConclusaoInscricao, InscricaoEvento

urlpatterns = [
    url('^registrar/$', Registrar.as_view(), name='registrar'),
    url('^pagina_inicial/$', PaginaInicial.as_view(), name='pagina_inicial'),
    url('^$', login, {'template_name': 'login/form_login.html'}, name='login'),
    url('^logout/', logout_then_login, {'login_url' : 'login'}, name='logout_usuario'),
    url('^inscricao_evento/(?P<inscricao_evento_id>[\d-]+)$', InscricaoEvento.as_view(), name='inscricao_evento'),
    url('^conclusao_inscricao/$', ConclusaoInscricao.as_view(), name='conclusao_inscricao'),
]