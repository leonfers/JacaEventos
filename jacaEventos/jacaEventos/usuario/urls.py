from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout, logout_then_login

from jacaEventos.usuario import views

urlpatterns = [
    url('^registrar/$', views.registrar_usuario, name='registrar_usuario'),
    url('^entrar/', login, {'template_name': 'login_usuario.html'}, name='login_usuario'),
    # url('^sair/', logout_then_login, {'login_url' : '/login_usuario'}, name='logout_usuario')
]