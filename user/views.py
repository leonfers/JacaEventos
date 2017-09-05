from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView, TemplateView
from .forms import *
from core.models import Evento, EspacoFisico

User = get_user_model()


class RegistrarUsuario(FormView):
    template_name = 'login/registrar.html'
    form_class = RegistrarUsuarioForm

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data['senha1'])
        return redirect(settings.LOGIN_URL)


class PaginaInicial(TemplateView):
    template_name = 'inicio/pagina_inicial.html'


class InscricaoEvento(View):
    template_name = 'inscricao/inscricao_evento.html'

    def post(self, request, *args, **kwargs):
        form_inscricao_evento = InscricaoEventoForm(request.POST)
        # TODO chekin por fazer
        # form_checkin = CheckinItemInscricaoEventoForm(request.POST)
        if form_inscricao_evento.is_valid():
            inscricao = form_inscricao_evento.save(commit=False)
            # form_inscricao_evento.cleaned_data['evento'] = Evento.objects.get(id=self.kwargs['inscricao_evento_id'])
            # inscricao.usuario = request.user
            # inscricao.evento = Evento.objects.get(id=self.kwargs['inscricao_evento_id'])
            inscricao.save()
            inscricao.add_inscricao_evento()

        return HttpResponseRedirect('/minhas_inscricoes_em_eventos/')

    def get(self, request, *args, **kwargs):
        evento = Evento.objects.get(id=self.kwargs['inscricao_evento_id'])
        print(evento)
        form_inscricao = InscricaoEventoForm()
        # form_checkin = form_checkin_evento()

        context = {'evento': evento,
                   'espaco': EspacoFisico.objects.all(),
                   'form_incricao_evento': form_inscricao}

        return render(request, self.template_name, context)


class ConclusaoInscricao(TemplateView):
    template_name = 'inscricao/conclusao_inscricao.html'


class MinhasInscricoesEmEventos(View):
    template_name = 'inscricao/minhas_inscricoes_em_eventos.html'

    def get(self, request, *args, **kwargs):
        inscricoes = Inscricao.objects.all().filter(usuario=request.user)
        context = {'incricoes': inscricoes}
        return render(request, self.template_name, context)
