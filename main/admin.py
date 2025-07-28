from django.contrib import admin
from .models import Filme, Genero, Pessoa, Aluguel

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    filter_horizontal = ['genero']
    search_fields = ['titulo']
    list_filter = ['genero']
    autocomplete_fields = ('direcao', 'elenco')
    exclude = ['slug']

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    exclude = ['slug']

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    exclude = ['slug']

admin.site.register(Aluguel)
