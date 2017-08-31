# METODOS DO FORMULARIO
import pycep_correios
from pycep_correios import CEPInvalido
from django.conf import settings
from django.http import request
from django.shortcuts import redirect

from core.forms import RegistrarTagEventosForm, RegistrarGerentesForm, RegistrarEspacoFisicoEventoForm, \
    AssociarInstituicoesEventoForm, AdicionarEventosSateliteForm, RegistrarAtividadeContinuaForm, \
    RegistrarAtividadeAdministrativaForm, RegistrarAtividadeForm, TrilhaAtividadeEventoForm
from utils.forms import PeriodoForm, HorarioForm


def formulario_tag(form_tag_evento, evento):
    form_tag_evento = RegistrarTagEventosForm(request.POST)
    if form_tag_evento.is_valid():
        tag = form_tag_evento.save(commit=False)
        tag.save()
        evento.add_tag(tag)
        form_tag_evento = RegistrarTagEventosForm()

def formulario_gerente(form_gerentes, evento):
    form_gerentes = RegistrarGerentesForm(request.POST)
    if form_gerentes.is_valid():
        gerente = form_gerentes.save(commit=False)
        gerente.evento = evento
        gerente.save()
        # form_gerentes = RegistrarGerentes()

def formulario_atividade_padrao(form_horario, form_periodo, evento):
    form_atividade_padrao = RegistrarAtividadeForm(request.POST)
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

def formulario_atividade_administrativa(form_horario, form_periodo, evento):
    form_atividade_administrativa = RegistrarAtividadeAdministrativaForm(request.POST)
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

def formulario_atividade_continua(form_horario, form_periodo, evento):
    form_atividade_continua = RegistrarAtividadeContinuaForm(request.POST)
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

def formulario_evento_satelite(evento):
    form_evento_satelite = AdicionarEventosSateliteForm(request.POST)
    if form_evento_satelite.is_valid():
        evento_satelite = form_evento_satelite.save(commit=False)
        evento_satelite.eventos = evento
        evento_satelite.save()

def formulario_intituicao_evento(evento):
    form_instituicao_evento = AssociarInstituicoesEventoForm(request.POST)
    if form_instituicao_evento.is_valid():
        instituicao_evento = form_instituicao_evento.save(commit=False)
        instituicao_evento.evento_relacionado = evento
        instituicao_evento.save()
        # evento.add_instituicao(instituicao_evento)
        return redirect(settings.REALIZAR_INSCRICAO)

def formulario_espaco_fisico(evento):
    form_espaco_fisico = RegistrarEspacoFisicoEventoForm(request.POST)
    if form_espaco_fisico.is_valid():
        espaco_fisico = form_espaco_fisico.save(commit=False)
        espaco_fisico.evento = evento
        espaco_fisico.save()

def formulario_periodo(form_periodo, evento, form_trilha_atividade):
    form_periodo = PeriodoForm(request.POST)
    if form_periodo.is_valid() and form_trilha_atividade.is_valid():
        trilha_atividade = form_trilha_atividade.save(commit=False)
        trilha_atividade.save()

        periodo = form_periodo.save(commit=False)
        periodo.save()

        form_periodo = PeriodoForm()

#TODO
def formulario_trilhe_evento():
    form_trilha_atividade = TrilhaAtividadeEventoForm(request.POST)


def formulario_registrar_evento(form_periodo, form_endereco, form_add_evento, self):

    if form_periodo.is_valid() and form_endereco.is_valid() and form_add_evento.is_valid():
        endereco = form_endereco.save(commit=False)
        try:
            adress = pycep_correios.consultar_cep(endereco.cep)
            print(adress)
            endereco.cidade = adress['cidade']
            endereco.estado = adress['uf']
            endereco.logradouro = adress['end']
            endereco.bairro = adress['bairro']
            endereco.save()

            periodo = form_periodo.save(commit=False)
            periodo.save()

            tipo_evento = self.request.POST['tipo_evento']

            evento = form_add_evento.save(commit=False)
            evento.dono = self.request.user

            evento.tipo_evento = tipo_evento
            evento.periodo = periodo
            evento.endereco = endereco

            # tag_evento.save()
            evento.save()
            return True

        except CEPInvalido as exc:
            print(exc)
            return False
