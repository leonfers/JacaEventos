from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

from core import views
from core.views import RegistrarEvento, RegistrarInstituicoes, MeusEventos, ParticiparEvento

urlpatterns = [
    url('^eventos/$', MeusEventos.as_view(), name='meus_eventos'),
    url('^eventos/(?P<eventos_id>\d+)$', views.exibir_evento, name='exibir_evento'),
    url('^registrar_evento/$', RegistrarEvento.as_view(), name='registrar_eventos'),
    url('^registrar_instituicoes/$', RegistrarInstituicoes.as_view(), name='registrar_instituicoes'),
    url('^participar_evento/$', ParticiparEvento.as_view(), name='participar_evento'),
]