from django.contrib import admin

from .models import Vaga, Tag, VagaTag

class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'organizacao', 'tipo', 'criado_em')  # Campos a serem exibidos
    list_filter = ('tipo', 'criado_em')  # Filtros disponíveis
    search_fields = ('titulo', 'organizacao')  # Campos de pesquisa

admin.site.register(Vaga, VagaAdmin)

admin.site.register(Tag)
admin.site.register(VagaTag)
