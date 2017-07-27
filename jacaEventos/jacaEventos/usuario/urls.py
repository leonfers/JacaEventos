from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from jacaEventos.usuario import views

urlpatterns = [
    url('^$', views.login_usuario, name='login_usuario'),
    url('^registrar/$', views.registrar_usuario, name='registrar_usuario'),
]