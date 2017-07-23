from django.conf.urls import url, include
from django.contrib import admin
from .views import index,register

urlpatterns = [

    url(r'^$', index, name='home'),

]
