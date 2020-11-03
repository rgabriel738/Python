from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from dataclasses import dataclass
from django.db import connection
from django.utils.html import format_html
from django.views.decorators.clickjacking import xframe_options_exempt


#primeira a ser chamada, vai renderizar o chart.html
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')
      
      
#segunda a ser chamada, vai gerar os dados a serem mostrados dentro do chart, chamada pela própria chart.html
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        numVagas = Vaga.objects.count()
        vagas = Vaga.objects.all()
        nomesVagas = Vaga.objects.values_list('funcao', flat=True).order_by('funcao')
        numCanditados = Candidato.objects.count()
        candidatos = Candidato.objects.all()
        listaNumCandidatos = []
        #percorre todas vagas, guardando o número de candidatos
        for x in range(numVagas):
            nomeVAGA = vagas[x].funcao 
            counter = 0
            for y in range(numCanditados): 
                if candidatos[y].vaga.funcao == nomeVAGA:
                    counter += 1
            listaNumCandidatos.append(counter)  
        data = {
                "labels": nomesVagas,
                "listaNumCandidatos": listaNumCandidatos,
        }
        return Response(data)
      
