from django.shortcuts import render
from django.views.generic import TemplateView, View
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from dataclasses import dataclass
from django.db import connection


# primeira a ser chamada, vai renderizar o chart.html
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chart.html')
      
      
# segunda a ser chamada, vai gerar os dados a serem mostrados dentro do chart
# chamada pela própria chart.html em 'endpoint'
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        numVagas = Vaga.objects.count()
        vagas = Vaga.objects.all().order_by('funcao')
        nomesVagas = Vaga.objects.values_list('funcao', flat=True).order_by('funcao')
        numCanditados = Candidato.objects.count()
        candidatos = Candidato.objects.all()
        listaNumCandidatos = []
        candComExperiencia = []

        #percorre todas vagas, guardando o número de candidatos
        for x in range(numVagas):
            nomeVAGA = vagas[x].funcao 
            counter = 0
            expCounter = 0
            for y in range(numCanditados): 
                if candidatos[y].vaga.funcao == nomeVAGA:
                    counter += 1
                    if candidatos[y].experiencia == '3 meses' or candidatos[y].experiencia == '6 meses' or candidatos[y].experiencia == '1 ano' or candidatos[y].experiencia == '2 anos' or candidatos[y].experiencia == '3 anos ou mais':
                    	expCounter += 1
                # if candidatos[y].vaga.experiencia == '3 meses' or candidatos[y].vaga.experiencia == '6 meses':
            listaNumCandidatos.append(counter)
            candComExperiencia.append(expCounter)  
        data = {
                "labels": nomesVagas,
                "listaNumCandidatos": listaNumCandidatos,
                "candComExperiencia": candComExperiencia,
        }
        return Response(data)

