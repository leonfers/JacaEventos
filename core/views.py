from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pycep_correios import CEPInvalido
from .forms import *
import pycep_correios
from user.models import Usuario
from core.models import Evento
from user.models import Usuario
from utils.forms import *
from django.conf import settings

# @login_required
# def meus_eventos(request):
#     return render(request, 'meus_eventos.html')

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
            # print(endereco.cep)
            try:
                adress = pycep_correios.consultar_cep(endereco.cep)
                print (adress)
                endereco.cidade = adress['cidade']
                endereco.estado = adress['uf']
                endereco.logradouro = adress['end']
                endereco.bairro = adress['bairro']
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
                return redirect(settings.REGISTRAR_EVENTO)  # resolver problema do redirecionamento

            except CEPInvalido as exc:
                print(exc)
                redirect(template_name)
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
    form_evento_satelite = AdicionarEventosSatelite(request.POST)

    form_periodo = PeriodoForm(request.POST)
    form_instituicao_evento = AssociarInstituicoesEvento(request.POST)
    form_trilha_atividade = TrilhaAtividadeEvento(request.POST)

    form_atividade_padrao = RegistrarAtividade(request.POST)
    form_atividade_administrativa = RegistrarAtividadeAdministrativa(request.POST)
    form_atividade_continua = RegistrarAtividadeContinua(request.POST)

    form_horario = HorarioForm(request.POST)

    if request.method == 'POST':

        formulario_atividade_padrao(form_atividade_padrao,form_horario, form_periodo, evento)
        formulario_atividade_administrativa(form_atividade_administrativa, form_horario, form_periodo, evento)
        formulario_atividade_continua(form_atividade_continua, form_horario, form_periodo, evento)
        formulario_tag(form_tag_evento, evento)
        formulario_gerente(form_gerentes, evento)

        formulario_evento_satelite(form_evento_satelite, evento)

        formulario_intituicao_evento(form_instituicao_evento, evento)
        # TODO AINDA POR FAZER

        if form_periodo.is_valid() and form_trilha_atividade.is_valid():
            trilha_atividade = form_trilha_atividade.save(commit=False)
            trilha_atividade.save()

            periodo = form_periodo.save(commit=False)
            periodo.save()

            form_periodo = PeriodoForm()


    else:
        form_gerentes = RegistrarGerentes()
        form_periodo = PeriodoForm()
        form_tag_evento = RegistrarTagEventos()
        form_instituicao_evento = AssociarInstituicoesEvento()
        form_evento_satelite = AdicionarEventosSatelite(request.POST)
        form_atividade_padrao = RegistrarAtividade()
        form_atividade_administrativa = RegistrarAtividadeAdministrativa()
        form_atividade_continua = RegistrarAtividadeContinua()

        form_horario = HorarioForm()

    context = {'form_evento_satelite': form_evento_satelite, 'form_horario': form_horario,'atividade_continua': form_atividade_continua ,'atividade_administrativa': form_atividade_administrativa ,'atividade_padrao' : form_atividade_padrao, 'exibir_evento' : evento, 'form_periodo' : form_periodo, 'form_gerente' : form_gerentes,  'form_tag_evento' : form_tag_evento, 'form_instituicao_evento' : form_instituicao_evento}

    return render(request, template_name, context)




# METODOS DO FORMULARIO
def formulario_tag(form_tag_evento, evento):
    if form_tag_evento.is_valid():
        tag = form_tag_evento.save(commit=False)
        tag.save()
        evento.add_tag(tag)
        form_tag_evento = RegistrarTagEventos()

def formulario_gerente(form_gerentes, evento):
    if form_gerentes.is_valid():
        gerente = form_gerentes.save(commit=False)
        gerente.evento = evento
        gerente.save()
        # form_gerentes = RegistrarGerentes()

def formulario_atividade_padrao(form_atividade_padrao, form_horario, form_periodo, evento):
    if form_atividade_padrao.is_valid() and form_horario.is_valid():
        atividade_padrao = form_atividade_padrao.save(commit=False)
        horario = form_horario.save(commit=False)
        periodo = form_periodo.save(commit=False)
        periodo.save()
        horario.save()
        atividade_padrao.horario = horario
        atividade_padrao.evento = evento
        atividade_padrao.periodo = periodo
        atividade_padrao.save()
        evento.add_atividade(atividade_padrao)

def formulario_atividade_administrativa(form_atividade_administrativa, form_horario, form_periodo, evento):
    if form_atividade_administrativa.is_valid() and form_horario.is_valid():
        atividade_administrativa = form_atividade_administrativa.save(commit=False)
        horario = form_horario.save(commit=False)
        periodo = form_periodo.save(commit=False)
        periodo.save()
        horario.save()
        atividade_administrativa.horario = horario
        atividade_administrativa.evento = evento
        atividade_administrativa.periodo = periodo
        atividade_administrativa.save()
        evento.add_atividade(atividade_administrativa)

def formulario_atividade_continua(form_atividade_continua, form_horario, form_periodo, evento):
    if form_atividade_continua.is_valid() and form_horario.is_valid():
        atividade_continuna = form_atividade_continua.save(commit=False)
        horario = form_horario.save(commit=False)
        periodo = form_periodo.save(commit=False)
        periodo.save()
        horario.save()
        atividade_continuna.horario = horario
        atividade_continuna.evento = evento
        atividade_continuna.periodo = periodo
        atividade_continuna.save()
        evento.add_atividade(atividade_continuna)

def formulario_evento_satelite(form_evento_satelite, evento):
    if form_evento_satelite.is_valid():
        evento_satelite = form_evento_satelite.save(commit=False)
        evento_satelite.eventos = evento
        evento_satelite.save()

def formulario_intituicao_evento(form_instituicao_evento, evento):
    if form_instituicao_evento.is_valid():
        instituicao_evento = form_instituicao_evento.save(commit=False)
        instituicao_evento.evento_relacionado = evento
        instituicao_evento.save()
        # evento.add_instituicao(instituicao_evento)

        form_instituicao_evento = AssociarInstituicoesEvento()