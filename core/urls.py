from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

from jacaEventos.core import views

urlpatterns = [
    url('^$', views.index_deslogado, name='index_deslogado'),
]