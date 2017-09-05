# METODOS DO FORMULARIO
import pycep_correios
from pycep_correios import CEPInvalido
from django.shortcuts import redirect
from django.conf import settings
from core.forms import RegistrarTagEventosForm, RegistrarGerentesForm, RegistrarEspacoFisicoEventoForm, \
    AssociarInstituicoesEventoForm, AdicionarEventosSateliteForm, RegistrarAtividadeContinuaForm, \
    RegistrarAtividadeAdministrativaForm, RegistrarAtividadePadraoForm, TrilhaAtividadeEventoForm
from utils.forms import PeriodoForm, HorarioForm, HorarioAtividadeForm
from django.http import HttpResponseRedirect


# formulario para registro de tags
def formulario_tag(evento, request):
    form_tag_evento = RegistrarTagEventosForm(request.POST)

    if form_tag_evento.is_valid():
        tag = form_tag_evento.save(commit=False)
        tag.save()
        # metodo para adicionar tag ao evento
        evento.add_tag(tag)
        form_tag_evento = RegistrarTagEventosForm()


# formulario para registro de gerentes
def formulario_gerente(evento, request):
    form_gerentes = RegistrarGerentesForm(request.POST)

    if form_gerentes.is_valid():
        gerente = form_gerentes.save(commit=False)
        gerente.evento = evento
        gerente.save()
        # form_gerentes = RegistrarGerentes()


# formulario para registro de atividade padrao
def formulario_atividade_padrao(evento, request):
    form_atividade_padrao = RegistrarAtividadePadraoForm(request.POST)
    form_horario_atividade = HorarioAtividadeForm(request.POST)

    if form_atividade_padrao.is_valid() and form_horario_atividade.is_valid():
        atividade_padrao = form_atividade_padrao.save(commit=False)
        # formulario horario da atividade
        horario_atividade = form_horario_atividade.save(commit=False)
        horario_atividade.save()

        atividade_padrao.evento = evento

        atividade_padrao.horario_atividade = horario_atividade
        atividade_padrao.save()
        # adicionando atividade registrada ao registro de eventos
        evento.add_atividade(atividade_padrao)


# formulario para registro de atividade administrativa
def formulario_atividade_administrativa(evento, request):
    form_horario_atividade = HorarioAtividadeForm(request.POST)
    form_atividade_administrativa = RegistrarAtividadeAdministrativaForm(request.POST)

    if form_atividade_administrativa.is_valid() and form_horario_atividade.is_valid():
        atividade_administrativa = form_atividade_administrativa.save(commit=False)
        # formulario horario atividade
        horario_atividade = form_horario_atividade.save(commit=False)
        horario_atividade.save()

        atividade_administrativa.evento = evento
        atividade_administrativa.horario_atividade = horario_atividade
        atividade_administrativa.save()
        # adicionando atividade registrada ao registro de eventos
        evento.add_atividade(atividade_administrativa)


# formulario para registro de atividade continua
def formulario_atividade_continua(evento, request):
    form_horario_atividade = HorarioAtividadeForm(request.POST)
    form_atividade_continua = RegistrarAtividadeContinuaForm(request.POST)

    if form_atividade_continua.is_valid() and form_horario_atividade.is_valid():
        atividade_continuna = form_atividade_continua.save(commit=False)
        # formulario horario atividade
        horario_atividade = form_horario_atividade.save(commit=False)
        horario_atividade.save()

        atividade_continuna.evento = evento
        atividade_continuna.horario_atividade = horario_atividade
        atividade_continuna.save()
        # adicionando atividade registrada ao registro de evento
        evento.add_atividade(atividade_continuna)


# formulario para registro de eventos satelite
def formulario_evento_satelite(evento, request):
    form_evento_satelite = AdicionarEventosSateliteForm(request.POST)

    if form_evento_satelite.is_valid():
        evento_satelite = form_evento_satelite.save(commit=False)
        evento_satelite.eventos = evento
        evento_satelite.save()


# formulario para registro de instituicoes relacionadas ao evento
def formulario_intituicao_evento(evento, request):
    form_instituicao_evento = AssociarInstituicoesEventoForm(request.POST)

    if form_instituicao_evento.is_valid():
        instituicao_evento = form_instituicao_evento.save(commit=False)
        instituicao_evento.evento_relacionado = evento
        instituicao_evento.save()


# formulario para registro de espacos fisicos do evento
def formulario_espaco_fisico(evento, request):
    form_espaco_fisico = RegistrarEspacoFisicoEventoForm(request.POST)

    if form_espaco_fisico.is_valid():
        espaco_fisico = form_espaco_fisico.save(commit=False)
        espaco_fisico.evento = evento
        espaco_fisico.save()


# # formulario para registro de periodo do evento
# def formulario_periodo( form_trilha_atividade, request ):
#     form_periodo = PeriodoForm( request.POST )
#
#     if form_periodo.is_valid():
#
#         trilha_atividade = form_trilha_atividade.save( commit=False )
#         trilha_atividade.save()
#
#         periodo = form_periodo.save( commit=False )
#         periodo.save()

# TODO
def formulario_trilhe_evento(request):
    form_trilha_atividade = TrilhaAtividadeEventoForm(request.POST)


# formulario para registrar um evento
def formulario_registrar_evento(form_periodo, form_endereco, form_add_evento, self):
    if form_periodo.is_valid() and form_endereco.is_valid() and form_add_evento.is_valid():
        endereco = form_endereco.save(commit=False)
        # metodo para consultar o cep
        adress = pycep_correios.consultar_cep(endereco.cep)
        endereco.cidade = adress['cidade']
        endereco.estado = adress['uf']
        endereco.logradouro = adress['end']
        endereco.bairro = adress['bairro']
        endereco.pais = "Brasil"
        endereco.numero = "3130"
        endereco.save()
        periodo = form_periodo.save(commit=False)
        periodo.save()
        # pega os dados preenchidos no formulario na opção de tipo evento
        tipo_evento = self.request.POST['tipo_evento']
        evento = form_add_evento.save(commit=False)
        evento.dono = self.request.user
        evento.tipo_evento = tipo_evento
        evento.periodo = periodo
        evento.endereco = endereco

        # tag_evento.save()
        evento.save()
