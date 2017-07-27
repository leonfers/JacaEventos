from django.shortcuts import render

# Create your views here.

def index_deslogado(request):
    return render(request, 'index_deslogado.html')

