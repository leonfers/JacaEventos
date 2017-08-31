from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth import user_logged_in
from user import views

urlpatterns = [
    url('^registrar/$', views.registrar, name='registrar'),
    url('^pagina_inicial/$', views.pagina_inicial, name='pagina_inicial'),
    url('^$', login, {'template_name': 'login/form_login.html'}, name='login'),
    # url('^', login, {'template_name': 'login_usuario.html'}, name='login_usuario'),
    url('^logout/', logout_then_login, {'login_url' : 'login'}, name='logout_usuario'),
    url('^inscricao_evento/(?P<inscricao_evento_id>\d+)$', views.inscricao_evento, name='inscricao_evento'),
    url('^conclusao_inscricao/$', views.conclusao_inscricao, name='conclusao_inscricao'),
]