from django.contrib import admin

from .models import Filme, Genero, Pessoa, Aluguel

admin.site.register(Filme)
admin.site.register(Genero)
admin.site.register(Pessoa)
admin.site.register(Aluguel)
