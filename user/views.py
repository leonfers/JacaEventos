from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, TemplateView
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from pycep_correios import CEPInvalido

from .forms import *
import pycep_correios
from user.models import Usuario
from core.models import Evento, EspacoFisico
from user.models import Usuario
from utils.forms import PeriodoForm, EnderecoForm

User = get_user_model()

class Registrar(FormView):
    template_name = 'login/registrar.html'
    form_class = RegistrarUsuarioForm

    def form_valid(self, form):
        print('entrou')
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data['senha1'])
        return redirect(settings.LOGIN_URL)

class PaginaInicial(TemplateView):
    template_name = 'inicio/pagina_inicial.html'

#
# class InscricaoEvento(View):
#     template_name = 'inscricao/inscricao_evento.html'
#     form_incricao_evento = InscricaoEventoForm
#     form_checkin_evento = CheckinItemInscricaoEventoForm
#
#
#     def post(self, request, *args, **kwargs):
#
#         form_inscricao = self.form_incricao_evento(request.POST)
#         form_checkin = self.form_checkin_evento(request.POST)
#         if form_inscricao.is_valid():
#             inscricao = form_inscricao.save(commit=False)
#             inscricao.usuario = request.user
#             inscricao.evento = Evento.objects.get(id=1)
#             inscricao.save()
#             return redirect(settings.PAGINA_INICIAL)
#
#     def get(self, request, *args, **kwargs):
#
#         evento = get_object_or_404( Evento, id = self.args )
#
#         # print('Evento : ', evento)
#
#         form_inscricao = self.form_incricao_evento()
#         form_checkin = self.form_checkin_evento()
#
#         return render(request, 'inscricao/inscricao_evento.html',
#                       {
#                           # 'evento': evento,
#                         'espaco': EspacoFisico.objects.all(),
#                         'form_incricao_evento': form_inscricao,
#                         'form_checkin_evento': form_checkin}
#                       )
#

# falta refatorar inscricao evento
@login_required
def inscricao_evento(request, inscricao_evento_id):
    template_name = 'inscricao/inscricao_evento.html'

    if request.method == 'POST':
        form_incricao_evento = InscricaoEventoForm(request.POST)
        form_checkin_evento = CheckinItemInscricaoEventoForm(request.POST)

        if form_incricao_evento.is_valid():
            inscricao = form_incricao_evento.save(commit=False)
            inscricao.usuario = request.user
            inscricao.evento = Evento.objects.get(id=inscricao_evento_id)
            inscricao.save()

            inscricao.add_item_inscricao()
            # inscricao.registro_checkin_inscricao()
            return redirect(settings.CONCLUSAO_INSCRICAO)

    else:
        form_incricao_evento = InscricaoEventoForm()
        form_checkin_evento = CheckinItemInscricao()

    context = {'evento' : Evento.objects.get(id=inscricao_evento_id),
               'espaco' : EspacoFisico.objects.all(),
               'form_incricao_evento' : form_incricao_evento,
               'form_checkin_evento' : form_checkin_evento}

    return render(request, template_name, context)


class ConclusaoInscricao(TemplateView):
    template_name = 'inscricao/conclusao_inscricao.html'