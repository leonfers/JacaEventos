from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import FormView, TemplateView, ListView
from pycep_correios import CEPInvalido

from core.helpers import formulario_atividade_padrao, formulario_atividade_administrativa, \
    formulario_atividade_continua, formulario_tag, formulario_gerente, formulario_evento_satelite, \
    formulario_intituicao_evento, formulario_espaco_fisico, formulario_registrar_evento
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
        context = { 'form_evento': form_add_evento,
                    'form_periodo': form_periodo,
                    'form_endereco': form_endereco }
        return render( request, self.template_name, context )

    def post(self, request, *args, **kwargs):
        form_add_evento = self.form_add_evento( request.POST )
        form_periodo = self.form_periodo( request.POST )
        form_endereco = self.form_endereco( request.POST )

        if formulario_registrar_evento(form_periodo, form_endereco, form_add_evento, self):
            return redirect( settings.PAGINA_INICIAL )
        else:
            return redirect( self.template_name )


class RegistrarInstituicoes(View):
    template_name = 'instituicoes/form_registrar.html'
    form_instituicoes = RegistrarInstituicoesForm

    def post(self, request, *args, **kwargs):
        form_instituicoes = self.form_instituicoes( request.POST )

        if form_instituicoes.is_valid():
            institu = form_instituicoes.save( commit = False )
            institu.save()
            return redirect( settings.PAGINA_INICIAL )

    def get(self, request, *args, **kwargs):
        form_instituicoes = RegistrarInstituicoesForm()
        context = { 'form_instituicoes': form_instituicoes }
        return render(request, self.template_name, context)


class MeusEventos(View):
    template_name = 'evento/meus_eventos.html'

    def get(self, request, *args, **kwargs):
        context = { 'meus_eventos': request.user.get_eventos() }
        return render( request, self.template_name, context )


class ExibirEvento(ListView):
    template_name = 'evento/exibir_evento.html'

    def post(self, request, *args, **kwargs):
        evento = Evento.objects.get( id = self.kwargs['eventos_id'] )
        print('TIpo', type(evento))

        form_horario = HorarioForm(request.POST)
        # CHAMA OS METODOS DO ARQUIVO HELPERS
        formulario_gerente(evento, request)
        formulario_atividade_padrao(form_horario, evento, request)
        formulario_atividade_administrativa(form_horario, evento, request)
        formulario_atividade_continua(form_horario, evento, request)
        formulario_tag(evento, request)
        formulario_evento_satelite(evento, request)
        formulario_intituicao_evento(evento, request)
        formulario_espaco_fisico(evento, request)
        # formulario_periodo( evento, request )

        # TODO AINDA POR FAZER

        return HttpResponseRedirect('/eventos/'+self.kwargs['eventos_id'])

    def get(self, request, *args, **kwargs):

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

        context = {'form_evento_satelite': form_evento_satelite,
               'form_horario': form_horario,
               'atividade_continua': form_atividade_continua,
               'atividade_administrativa': form_atividade_administrativa,
               'atividade_padrao': form_atividade_padrao,
               'exibir_evento': Evento.objects.get( id=self.kwargs['eventos_id'] ),
               'form_periodo': form_periodo,
               'form_gerente': form_gerentes,
               'form_tag_evento': form_tag_evento,
               'form_instituicao_evento': form_instituicao_evento,
               'form_espaco_fisico': form_espaco_fisico,
               'espacos': EspacoFisico.objects.all()}

        return render(request, self.template_name, context)

class ParticiparEvento( View ):
    template_name = 'evento/participar_evento.html'
    def get(self, request, *args, **kwargs):
        context = { 'eventos': Evento.objects.all() }
        return render( request, self.template_name, context )
