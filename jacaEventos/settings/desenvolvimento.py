# coding: utf-8
from .base import *

DEBUG = True

# Em caso de macOS: rodar o comando abaixo para o Python encontrar as bibliotecas
# export DYLD_FALLBACK_LIBRARY_PATH=/Library/PostgreSQL/<numero_versao_postgres>/lib:$DYLD_FALLBACK_LIBRARY_PATH
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jaca',
        'USER': 'postgres',
        'PASSWORD': 'admin',
    }
}