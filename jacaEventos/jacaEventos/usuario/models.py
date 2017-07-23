from django.db import models

import re

from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
# Create your models here.

class Usuario(models.Model):

	username = models.CharField('Nome do Usuário', max_length=30, unique=True,
		validators = [validators.RegexValidator(re.compile('^[\w.@+-]+$'),'O nome do usuario so pode conter letras, digitos ou os' 
			'seguintes caracteres @/./+/-/_', 'invalid')])
	email = models.EmailField('E-mail', unique=True)
	name = models.CharField('Nome', max_length=100, blank=True)
	is_active = models.BooleanField('Esta ativo', blank=True,default=True)
	is_staff = models.BooleanField('É da equipe', blank=True, default=True)
	date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)



	class Meta:

		verbose_name = 'Usuário'
		verbose_name_plural = 'Usuários'

class Inscricao(models.Model):

    status_inscricao = models.BooleanField('Inscrito/Não Inscrito', blank=True, default=True)

