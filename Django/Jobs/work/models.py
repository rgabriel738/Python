from django.db import models
from django.utils.html import format_html
import re
import codecs
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
import os
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
import math

CATEGORIAS_TRABALHO = (

	(u'Nao Possui', u'Não Possui'),
	(u'Administracao', u'Administração'),
	(u'Alimentacao', u'Alimentação'),
	(u'Artes', u'Artes'),
	(u'Direito', u'Direito'),
	(u'Economia', u'Economia'),
	(u'Educacao', u'Educação'),
	(u'Engenharia', u'Engenharia'),
	(u'Logistica', u'Logística'),
	(u'Marketing', u'Marketing'),
	(u'Mecanica', u'Mecânica'),
	(u'Moda', u'Moda'),
	(u'Negocios', u'Negócios'),
	(u'Producao', u'Produção'),
	(u'Saude', u'Saúde'),
	(u'Seguranca', u'Segurança'),
	(u'Tecnologia da Informacao', u'Tecnologia da Informação'),
	(u'Turismo', u'Turismo'),
	(u'Vendas', u'Vendas'),	
)


TEMPO_EXPERIENCIA = (

	(u'Nao Necessario', u'Não Necessário'),
	(u'3 meses', u'3 meses'),
	(u'6 meses', u'6 meses'),
	(u'1 ano', u'1 ano'),
	(u'2 anos', u'2 anos'),
	(u'3 anos ou mais', u'3 anos ou mais'),
)


class Contratante(models.Model):
	nome 			  = models.CharField(max_length=200)
	cnpj 			  = models.CharField(max_length=200)
	telefone		= models.CharField(max_length=200)
	endereco		= models.CharField(max_length=200)
	def __str__(self):
		return self.nome



class Vaga(models.Model):
	funcao 			  = models.CharField(max_length=200)
	categoria		  = models.CharField(max_length=200, choices=CATEGORIAS_TRABALHO)
	requisitos 		= models.CharField(max_length=200)
	experiencia		= models.CharField(max_length=200, choices=TEMPO_EXPERIENCIA)
	salario			= models.CharField(max_length=200)
	data_incricao	= models.DateField(verbose_name=u'Data limite de Inscrição')
	contratante 	= models.ForeignKey(Contratante, on_delete=models.CASCADE, null=True, related_name='vagas')
	inscricoes 		= models.IntegerField(null=True)
	def __str__(self):
		return self.funcao



class Candidato(models.Model):
	nome 			  = models.CharField(max_length=200)
	cpf 			  = models.CharField(max_length=200)
	telefone		= models.CharField(max_length=200)
	endereco		= models.CharField(max_length=200)
	vaga 			  = models.ForeignKey(Vaga, on_delete=models.CASCADE, null=True, related_name='candidatos')
	def __str__(self):
		return self.nome
