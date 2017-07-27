from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import render, redirect
from .forms import RegistrarUsuario

User = get_user_model()

def registrar_usuario(request):

    template_name = 'registrar_usuario.html'
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['senha1'])
            return redirect('index_deslogado.html')
    else:
        form = RegistrarUsuario()
    context = {'form' : form}

    return render(request, template_name, context)