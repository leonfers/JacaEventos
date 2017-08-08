from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login, logout, logout_then_login
from django.contrib.auth import user_logged_in
from user import views

urlpatterns = [
    url('^registrar/$', views.registrar, name='registrar'),
    url('^pagina_inicial/$', views.pagina_inicial, name='pagina_inicial'),
    url('^meus_eventos/$', views.meus_eventos, name='meus_eventos'),
    url('^meus_eventos/(?P<eventos_id>\d+)$', views.exibir_evento, name='exibir_evento'),
    url('^registrar_evento/$', views.registrar_eventos, name='registrar_eventos'),
    url('^registrar_instituicoes/$', views.registrar_instituicoes, name='registrar_instituicoes'),
    url('^$', login, {'template_name': 'login/form_login.html'}, name='login'),
    # url('^', login, {'template_name': 'login_usuario.html'}, name='login_usuario'),
    url('^logout/', logout_then_login, {'login_url' : 'login'}, name='logout_usuario')

]