from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout, logout_then_login

from jacaEventos.usuario import views

urlpatterns = [
    url('^registrar/$', views.registrar, name='registrar'),
    url('^pagina_inicial/$', views.pagina_inicial, name='pagina_inicial'),
    url('^$', login, {'template_name': 'login.html'}, name='login'),
    # url('^', login, {'template_name': 'login_usuario.html'}, name='login_usuario'),
    url('^logout/', logout_then_login, {'login_url' : 'login'}, name='logout_usuario')
]