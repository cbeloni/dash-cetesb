from django.shortcuts import render
from django.http import HttpResponse
from .service.qualidade_ar import listar_todos, listar_detalhes

# Create your views here.

def index(request):
    detalhes, nome_detalhes = listar_detalhes()
    # Page from the theme 
    return render(request, 'pages/index.html', { "lista_qualidade_ar": listar_todos(),
                                                 "detalhes": detalhes,
                                                 "nome_detalhes":nome_detalhes})
