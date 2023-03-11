from django.shortcuts import render
from django.http import HttpResponse
from .service.qualidade_ar import listar_todos

# Create your views here.

def index(request):

    # Page from the theme 
    return render(request, 'pages/index.html', { "lista_qualidade_ar": listar_todos()})
