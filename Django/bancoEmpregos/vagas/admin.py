from django.contrib import admin
from .models import *


class CandidatoAdmin(admin.ModelAdmin):
	list_display = ['nome', 'vaga', 'experiencia','telefone'] 
	search_fields = ['nome', 'email', 'cpf', 'telefone', 'endereco']
	def queryset(self, request):
		qs = super(CandidatoAdmin, self).queryset(request)
		return qs.order_by("nome")

admin.site.register(Vaga)
admin.site.register(AreaAtuacao)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Contratante)
