from django.conf import settings
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrarUsuario
from jacaEventos.usuario.models import Usuario

User = get_user_model()

def registrar_usuario(request):
    template_name = 'registrar_usuario.html'
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
def get_usuario_logado(request):
    return request.user.usuario
