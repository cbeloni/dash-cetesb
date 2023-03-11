from django.shortcuts import render
from django.http import HttpResponse
from .service.qualidade_ar import QualidadeAr

# Create your views here.

def index(request):

    qualidade_santo_andre = QualidadeAr(nome="Santo André",
                                        situacao_rede="A",
                                        tipo_rede="A",
                                        data="2023-03-11 10:00:00.000",
                                        qualidade="N1 - BOA")
    qualidade_capao = QualidadeAr(nome="Capão Redondo",
                                        situacao_rede="A",
                                        tipo_rede="A",
                                        data="2023-03-11 10:00:00.000",
                                        qualidade="N1 - BOA")
    qualidade_carapicuiba = QualidadeAr(nome="Carapicuíba",
                                        situacao_rede="A",
                                        tipo_rede="A",
                                        data="2023-03-11 10:00:00.000",
                                        qualidade="N1 - BOA")
    qualidade_ibirapuera = QualidadeAr(nome="Ibirapuera",
                                        situacao_rede="A",
                                        tipo_rede="A",
                                        data="2023-03-11 12:00:00.000",
                                        qualidade="Não coletado")

    lista_qualidade_ar = []
    lista_qualidade_ar.append(qualidade_santo_andre)
    lista_qualidade_ar.append(qualidade_capao)
    lista_qualidade_ar.append(qualidade_carapicuiba)
    lista_qualidade_ar.append(qualidade_ibirapuera)

    # Page from the theme 
    return render(request, 'pages/index.html', { "lista_qualidade_ar": lista_qualidade_ar})
