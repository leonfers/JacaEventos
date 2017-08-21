from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pycep_correios import CEPInvalido

from .forms import *
import pycep_correios
from user.models import Usuario
from core.models import Evento
from user.models import Usuario
from utils.forms import PeriodoForm, EnderecoForm

User = get_user_model()

def registrar(request):
    template_name = 'login/registrar.html'
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)

        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['senha1'])
            return redirect(settings.LOGIN_URL)
    else:
        form = RegistrarUsuario()
    context = {'form' : form}

    return render(request, template_name, context)


@login_required
def pagina_inicial(request):
    return render(request, 'inicio/pagina_inicial.html')

@login_required
def inscricao_evento(request, inscricao_evento_id):
    template_name = 'inscricao/inscricao_evento.html'
    context = {'evento' : Evento.objects.get(id=inscricao_evento_id)}
    return render(request, template_name, context)
