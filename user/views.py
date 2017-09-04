from django.conf import settings
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
    form_incricao_evento = InscricaoEventoForm
    form_checkin_evento = CheckinItemInscricaoEventoForm

    def post(self, request, *args, **kwargs):
        form_inscricao = self.form_incricao_evento(request.POST)
        # TODO chekin por fazer
        form_checkin = self.form_checkin_evento(request.POST)

        if form_inscricao.is_valid():
            inscricao = form_inscricao.save(commit=False)
            inscricao.usuario = request.user
            inscricao.evento = Evento.objects.get(id=self.kwargs['inscricao_evento_id'])
            inscricao.save()
            inscricao.add_inscricao_evento()
            # inscricao.registro_checkin_inscricao()

            return redirect(settings.CONCLUSAO_INSCRICAO)

    def get(self, request, *args, **kwargs):
        evento = Evento.objects.get(id=self.kwargs['inscricao_evento_id'])
        form_inscricao = self.form_incricao_evento()
        form_checkin = self.form_checkin_evento()

        context = {'evento': evento,
                   'espaco': EspacoFisico.objects.all(),
                   'form_incricao_evento': form_inscricao,
                   'form_checkin_evento': form_checkin}

        return render(request, 'inscricao/inscricao_evento.html', context)


class ConclusaoInscricao(TemplateView):
    template_name = 'inscricao/conclusao_inscricao.html'
