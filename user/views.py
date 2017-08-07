from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from user.models import Usuario
from core.models import Evento
from user.models import Usuario

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
def meus_eventos(request):
    return render(request, 'meus_eventos.html')


@login_required
def registrar_eventos(request):
    template_name = 'evento/form_registrar.html'

    if request.method == 'POST':
        form_add_evento = RegistrarEvento(request.POST)
        form_tag_evento = AdicionarTagEmEventos(request.POST)

        if form_add_evento.is_valid():
            # tag_evento = form_tag_evento.save(commit=False)
            # tag_evento.evento.add_tag(request.user)

            evento = form_add_evento.save(commit=False)
            evento.dono = request.user

            # tag_evento.save()
            evento.save()
            return redirect(settings.REGISTRAR_EVENTO)

    else:
        form_tag_evento = AdicionarTagEmEventos()
        form_add_evento = RegistrarEvento()
    context = { 'form_evento': form_add_evento, 'form_adicionar_tag' : form_tag_evento}

    return render(request, template_name, context)

#
# @login_required
# def registrar_eventos(request):
#     template_name = 'evento/form_registrar.html'
#
#     if request.method == 'POST':
#         form_add_evento = RegistrarEvento(request.POST)
#         if form_add_evento.is_valid():
#             evento = form_add_evento.save(commit=False)
#             evento.dono = request.user
#             evento.save()
#             return redirect(settings.REGISTRAR_EVENTO)
#     else:
#         form_add_evento = RegistrarEvento()
#     context = { 'form_evento': form_add_evento }
#     return render(request, template_name, context)


@login_required
def registrar_instituicoes(request):
    template_name = 'instituicoes/form_registrar.html'

    if request.method == 'POST':
        form = RegistrarInstituicoes(request.POST)

        if form.is_valid():
            instituicoes = form.save(commit=False)
            instituicoes.save()
            form = RegistrarInstituicoes()
    else:
        form = RegistrarInstituicoes()
    context = {'form_instituicoes': form}
    return render(request, template_name, context)


@login_required
def meus_eventos(request):
    template_name = 'evento/meus_eventos.html'

    context = {'meus_eventos' : request.user.get_eventos()}

    return render(request, template_name, context)