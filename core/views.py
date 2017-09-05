from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from core.helpers import formulario_atividade_padrao, formulario_atividade_administrativa, \
    formulario_atividade_continua, formulario_tag, formulario_gerente, formulario_evento_satelite, \
    formulario_intituicao_evento, formulario_espaco_fisico, formulario_registrar_evento
from .forms import *
from core.models import Evento
from utils.forms import *
from django.conf import settings
from pycep_correios import CEPInvalido
from django.http import HttpResponse


class RegistrarEvento(View):
    template_name = 'evento/form_registrar.html'

    def get(self, request, *args, **kwargs):
        form_add_evento = RegistrarEventoForm
        form_periodo = PeriodoForm
        form_endereco = EnderecoForm

        context = {'form_evento': form_add_evento,
                   'form_periodo': form_periodo,
                   'form_endereco': form_endereco}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form_add_evento = RegistrarEventoForm(request.POST)
        form_periodo = PeriodoForm(request.POST)
        form_endereco = EnderecoForm(request.POST)

        formulario_registrar_evento(form_periodo, form_endereco, form_add_evento, self)

        context = {'form_evento': form_add_evento,
                   'form_periodo': form_periodo,
                   'form_endereco': form_endereco}

        if form_periodo.is_valid() and form_endereco.is_valid() and form_add_evento.is_valid():
            return redirect(settings.PAGINA_INICIAL)

        else:
            return render(request, self.template_name, context)


class RegistrarInstituicoes(View):
    template_name = 'instituicoes/form_registrar.html'
    form_instituicoes = RegistrarInstituicoesForm

    def post(self, request, *args, **kwargs):
        form_instituicoes = self.form_instituicoes(request.POST)

        if form_instituicoes.is_valid():
            instituicoes = form_instituicoes.save(commit=False)
            instituicoes.save()
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


class ExibirDetalhesEvento(View):
    template_name = 'evento/exibir_detalhes_evento.html'

    def post(self, request, *args, **kwargs):
        # metodo para receber o id que foi mandado para a url
        evento = Evento.objects.get(id=self.kwargs['eventos_id'])

        # metodos estao contidas no arquivo helpers
        formulario_gerente(evento, request)
        formulario_atividade_padrao(evento, request)
        formulario_atividade_administrativa(evento, request)
        formulario_atividade_continua(evento, request)
        formulario_tag(evento, request)
        formulario_evento_satelite(evento, request)
        formulario_intituicao_evento(evento, request)
        formulario_espaco_fisico(evento, request)

        # TODO AINDA POR FAZER

        return HttpResponseRedirect('/eventos/exibir_evento=' + self.kwargs['eventos_id'])

    def get(self, request, *args, **kwargs):
        # criando os formularios de exibir evento
        form_gerentes = RegistrarGerentesForm()
        form_tag_evento = RegistrarTagEventosForm()
        form_instituicao_evento = AssociarInstituicoesEventoForm()
        form_evento_satelite = AdicionarEventosSateliteForm()
        form_atividade_padrao = RegistrarAtividadePadraoForm()
        form_atividade_administrativa = RegistrarAtividadeAdministrativaForm()
        form_atividade_continua = RegistrarAtividadeContinuaForm()
        form_espaco_fisico = RegistrarEspacoFisicoEventoForm()
        form_horario_atividade = HorarioAtividadeForm()

        context = {'form_evento_satelite': form_evento_satelite,
                   'form_horario_atividade': form_horario_atividade,
                   'atividade_continua': form_atividade_continua,
                   'atividade_administrativa': form_atividade_administrativa,
                   'atividade_padrao': form_atividade_padrao,
                   'exibir_evento': Evento.objects.get(id=self.kwargs['eventos_id']),
                   'form_gerente': form_gerentes,
                   'form_tag_evento': form_tag_evento,
                   'form_instituicao_evento': form_instituicao_evento,
                   'form_espaco_fisico': form_espaco_fisico,
                   'espacos': EspacoFisico.objects.all()}

        return render(request, self.template_name, context)


class ParticiparEvento(View):
    template_name = 'evento/participar_evento.html'

    def get(self, request, *args, **kwargs):
        context = {'eventos': Evento.objects.all().filter(~Q(dono=request.user))}
        return render(request, self.template_name, context)
