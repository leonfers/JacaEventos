from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth import user_logged_in
from user import views
from user.views import Registrar, PaginaInicial, ConclusaoInscricao

urlpatterns = [
    url('^registrar/$', Registrar.as_view(), name='registrar'), #alterado para class based view
    url('^pagina_inicial/$', PaginaInicial.as_view(), name='pagina_inicial'),

    url('^$', login, {'template_name': 'login/form_login.html'}, name='login'),
    # url('^', login, {'template_name': 'login_usuario.html'}, name='login_usuario'),
    url('^logout/', logout_then_login, {'login_url' : 'login'}, name='logout_usuario'),
    url('^inscricao_evento/(?P<inscricao_evento_id>\d+)$', views.inscricao_evento, name='inscricao_evento'),

    url('^conclusao_inscricao/$', ConclusaoInscricao.as_view(), name='conclusao_inscricao'),
]