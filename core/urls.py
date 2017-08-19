from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

from core import views

urlpatterns = [
    url('^meus_eventos/$', views.meus_eventos, name='meus_eventos'),
    url('^meus_eventos/(?P<eventos_id>\d+)$', views.exibir_evento, name='exibir_evento'),
    url('^registrar_evento/$', views.registrar_eventos, name='registrar_eventos'),
    url('^registrar_instituicoes/$', views.registrar_instituicoes, name='registrar_instituicoes'),
    url('^participar_evento/$', views.participar_evento, name='participar_evento'),
]