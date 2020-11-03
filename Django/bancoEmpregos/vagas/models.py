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

	(u'Dispensavel', u'Dispensável'),
	(u'3 meses', u'3 meses'),
	(u'6 meses', u'6 meses'),
	(u'1 ano', u'1 ano'),
	(u'2 anos', u'2 anos'),
	(u'3 anos ou mais', u'3 anos ou mais'),
)

GENERO_CHOICES =(

	(u'Feminino', u'Feminino'),
	(u'Masculino', u'Masculino'),
	(u'Outro', u'Outro'),
)



class Contratante(models.Model):
	nome 			= models.CharField(max_length=200)
	cnpj 			= models.CharField(max_length=200)
	telefone		= models.CharField(max_length=200)
	endereco		= models.CharField(max_length=200)
	def __str__(self):
		return self.nome
	class Meta:
		ordering = ['nome']


class AreaAtuacao(models.Model):
	nome 			= models.CharField(max_length=200)
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'Área de Atuação'
		verbose_name_plural = 'Áreas de Atuação'
		ordering = ['nome']


class Vaga(models.Model):
	funcao 			= models.CharField(max_length=200)
	area 			= models.ForeignKey(AreaAtuacao, on_delete=models.CASCADE, null=True, related_name='area_fk')
	requisitos 		= models.CharField(max_length=200)
	experiencia		= models.CharField(max_length=200, choices=TEMPO_EXPERIENCIA)
	salario			= models.IntegerField()
	data_incricao	= models.DateField(verbose_name=u'Data limite de Inscrição')
	contratante 	= models.ForeignKey(Contratante, on_delete=models.CASCADE, null=True, related_name='contratante_fk')
	def __str__(self):
		return self.funcao
	class Meta:
		ordering = ['funcao']



class Candidato(models.Model):
	nome 			= models.CharField(max_length=200)
	cpf 			= models.CharField(max_length=200)
	idade 			= models.IntegerField()
	genero 			= models.CharField(max_length=200, choices=GENERO_CHOICES)
	telefone		= models.CharField(max_length=200)
	endereco		= models.CharField(max_length=200)
	email 			= models.CharField(max_length=200, null=True)
	vaga 			= models.ForeignKey(Vaga, on_delete=models.CASCADE, null=True, related_name='candidatos')
	experiencia		= models.CharField(max_length=200, choices=TEMPO_EXPERIENCIA, verbose_name=u'Experiência na vaga')
	def __str__(self):
		return self.nome
	class Meta:
		ordering = ['nome']