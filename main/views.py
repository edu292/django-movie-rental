from django.shortcuts import render, get_object_or_404
from urllib.parse import unquote

from .models import Filme, Pessoa, Genero

def home(request):
    filmes = Filme.objects.all()[:3]
    return render(request, 'main/home.html', {'filmes': filmes})

def top5(request):
    filmes = Filme.objects.all()[:5]
    return render(request, 'main/top5.html', context={'filmes': filmes})

def biografia(request, nome):
    pessoa = get_object_or_404(Pessoa, nome=unquote(nome))
    return render(request, "main/biografia.html", {"pessoa": pessoa})

def genero(request, nome):
    genero = get_object_or_404(Genero, nome=unquote(nome))
    return render(request, 'main/genero.html', {'genero': genero})