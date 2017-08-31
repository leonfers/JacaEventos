from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, TemplateView
from pycep_correios import CEPInvalido

from core.helpers import formulario_atividade_padrao, formulario_atividade_administrativa, \
    formulario_atividade_continua, formulario_tag, formulario_gerente, formulario_evento_satelite, \
    formulario_intituicao_evento, formulario_espaco_fisico, formulario_periodo
from .forms import *
import pycep_correios
from user.models import Usuario
from core.models import Evento
from user.models import Usuario
from utils.forms import *
from django.conf import settings

class RegistrarEvento(View):
    template_name = 'evento/form_registrar.html'

    form_add_evento = RegistrarEventoForm
    form_periodo = PeriodoForm
    form_endereco = EnderecoForm

    def get(self, request, *args, **kwargs):

        form_add_evento = self.form_add_evento()
        form_periodo = self.form_periodo()
        form_endereco = self.form_endereco()

        context = { 'form_evento': form_add_evento, 'form_periodo': form_periodo, 'form_endereco': form_endereco }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form_add_evento = self.form_add_evento
        form_periodo = self.form_periodo
        form_endereco = self.form_endereco

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

                tipo_evento = request.POST['tipo_evento']

                evento = form_add_evento.save(commit=False)
                evento.dono = request.user

                evento.tipo_evento = tipo_evento
                evento.periodo = periodo
                evento.endereco = endereco

                # tag_evento.save()
                evento.save()

                redirect(self.template_name)

            except CEPInvalido as exc:
                print(exc)
                redirect(self.template_name)

class RegistrarInstituicoes(View):
    template_name = 'instituicoes/form_registrar.html'

    form_instituicoes = RegistrarInstituicoesForm

    def post(self, request, *args, **kwargs):
        form_instituicoes = self.form_instituicoes(request.POST)

        if form_instituicoes.is_valid():
            institu = form_instituicoes.save(commit=False)
            institu.save()
            return redirect(settings.PAGINA_INICIAL)

    def get(self, request, *args, **kwargs):

        form_instituicoes = RegistrarInstituicoesForm()
        context = {'form_instituicoes': form_instituicoes}

        return render(request, self.template_name, context)

class MeusEventos(View):
    template_name = 'evento/meus_eventos.html'

    def get(self, request, *args, **kwargs):
        context = {'meus_eventos': request.user.get_eventos()}
        return render(request, self.template_name, context)

@login_required
def exibir_evento(request, eventos_id):
    template_name = 'evento/exibir_evento.html'
    evento = Evento.objects.get(id=eventos_id)

    if request.method == 'POST':

        form_horario = HorarioForm(request.POST)

        # CHAMA OS METODOS DO ARQUIVO HELPERS
        formulario_atividade_padrao(form_horario, evento)
        formulario_atividade_administrativa(form_horario, evento)
        formulario_atividade_continua(form_horario, evento)
        formulario_tag(evento)
        formulario_gerente(evento)
        formulario_evento_satelite(evento)
        formulario_intituicao_evento( evento )
        formulario_espaco_fisico( evento )
        formulario_periodo( evento )

        # TODO AINDA POR FAZER

    else:

        form_gerentes = RegistrarGerentesForm()
        form_periodo = PeriodoForm()
        form_tag_evento = RegistrarTagEventosForm()
        form_instituicao_evento = AssociarInstituicoesEventoForm()
        form_evento_satelite = AdicionarEventosSateliteForm(request.POST)
        form_atividade_padrao = RegistrarAtividadeForm()
        form_atividade_administrativa = RegistrarAtividadeAdministrativaForm()
        form_atividade_continua = RegistrarAtividadeContinuaForm()
        form_horario = HorarioForm()
        form_espaco_fisico = RegistrarEspacoFisicoEventoForm()

    context = {'form_evento_satelite': form_evento_satelite, 'form_horario': form_horario,'atividade_continua': form_atividade_continua ,'atividade_administrativa': form_atividade_administrativa ,
               'atividade_padrao' : form_atividade_padrao, 'exibir_evento' : evento, 'form_periodo' : form_periodo, 'form_gerente' : form_gerentes,
               'form_tag_evento' : form_tag_evento, 'form_instituicao_evento' : form_instituicao_evento, 'form_espaco_fisico' : form_espaco_fisico,
               'espacos' : EspacoFisico.objects.all()}

    return render(request, template_name, context)

class ParticiparEvento(View):
    template_name = 'evento/participar_evento.html'
    def get(self, request, *args, **kwargs):
        context = {'eventos': Evento.objects.all()}
        return render(request, self.template_name, context)
