from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render, redirect
from .forms import RegistrarUsuario


def login_usuario(request):
    return render(request, 'login_usuario.html')

def registrar_usuario(request):
    User = get_user_model()
    template_name = 'registrar_usuario.html'
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['senha1'])
            login_usuario(request, user)
            return redirect('index.html')
    else:
        form = RegistrarUsuario()
    context = {'form' : form}

    return render(request, template_name, context)