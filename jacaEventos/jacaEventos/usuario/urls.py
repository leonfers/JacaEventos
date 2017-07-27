from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout

from jacaEventos.usuario import views

urlpatterns = [
    url('^registrar/$', views.registrar_usuario, name='registrar_usuario'),
    url(r'^entrar/', login, {'template_name': 'login_usuario.html'}, name='login_usuario'),

]