from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
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
def meus_eventos(request):
    return render(request, 'meus_eventos.html')


@login_required
def registrar_eventos(request):
    template_name = 'evento/form_registrar.html'

    if request.method == 'POST':
        form_add_evento = RegistrarEvento(request.POST)
        form_periodo = PeriodoForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

        if form_add_evento.is_valid() and form_periodo.is_valid and form_endereco:
            # tag_evento = form_tag_evento.save(commit=False)
            # tag_evento.evento.add_tag(request.user)
            endereco = form_endereco.save(commit=False)
            endereco.save()

            periodo = form_periodo.save(commit=False)
            periodo.save()

            tipo_evento = request.POST['tipo_evento']

            evento = form_add_evento.save(commit=False)
            evento.dono = request.user
            evento.tipo_evento = tipo_evento
            evento.periodo = periodo
            evento.endereco = endereco

            # tag_evento.save()
            evento.save()
            return redirect(settings.REGISTRAR_EVENTO) #resolver problema do redirecionamento

    else:
        form_add_evento = RegistrarEvento()
        form_periodo = PeriodoForm()
        form_endereco = EnderecoForm()

    context = { 'form_evento': form_add_evento, 'form_periodo' : form_periodo, 'form_endereco' : form_endereco}

    return render(request, template_name, context)

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

@login_required
def exibir_evento(request, eventos_id):
    template_name = 'evento/exibir_evento.html'
    evento = Evento.objects.get(id=eventos_id)

    form_gerentes = RegistrarGerentes(request.POST)
    form_tag_evento = RegistrarTagEventos(request.POST)
    form = RegistrarAtividades(request.POST)
    form_periodo = PeriodoForm(request.POST)
    form_instituicao_evento = AssociarInstituicoesEvento(request.POST)

    if request.method == 'POST':
        # TODO AINDA POR FAZER
        if form_instituicao_evento.is_valid():
            instituicao_evento = form_instituicao_evento.save(commit=False)
            # instituicao_evento.evento_relacionado = evento
            # evento.add_instituicao(instituicao_evento)
            instituicao_evento.save()

            form_instituicao_evento = AssociarInstituicoesEvento()

        if form_periodo.is_valid() and form.is_valid():
            periodo = form_periodo.save(commit=False)
            periodo.save()
            atividades = form.save(commit=False)
            atividades.periodo = periodo
            evento.add_atividade(atividades)
            atividades.save()

            form = RegistrarAtividades()
            form_periodo = PeriodoForm()

        if form_gerentes.is_valid():
            gerente = form_gerentes.save(commit=False)
            gerente.evento = evento
            gerente.save()

            form_gerentes = RegistrarGerentes()


        if form_tag_evento.is_valid():
            tag = form_tag_evento.save(commit=False)
            tag.save()
            evento.add_tag(tag)

            form_tag_evento = RegistrarTagEventos()

    else:
        form_gerentes = RegistrarGerentes()
        form = RegistrarAtividades()
        form_periodo = PeriodoForm()
        form_tag_evento = RegistrarTagEventos()
        form_instituicao_evento = AssociarInstituicoesEvento()

    context = {'form_atividades' : form, 'exibir_evento' : evento, 'form_periodo' : form_periodo, 'form_gerente' : form_gerentes,  'form_tag_evento' : form_tag_evento, 'form_instituicao_evento' : form_instituicao_evento}

    return render(request, template_name, context)


