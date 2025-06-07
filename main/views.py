from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, reverse, redirect
from urllib.parse import unquote

from django.views.decorators.http import require_POST

from .models import Filme, Pessoa, Genero, Aluguel

def home(request):
    query = request.GET.get("q")
    if query:
        filmes = Filme.objects.filter(titulo__icontains=query)
    else:
        filmes = Filme.objects.all()[:3]
    return render(request, 'main/home.html', {'filmes': filmes})

def top5(request):
    filmes = Filme.objects.all()[:5]
    return render(request, 'main/top5.html', context={'filmes': filmes})

def biografias(request):
    query = request.GET.get('q')
    if query:
        pessoas = Pessoa.objects.filter(nome__icontains=query)
    else:
        pessoas = Pessoa.objects.all()[:8]
    context = {
        'pessoas': pessoas,
        'query': query,
    }
    return render(request, 'main/biografias.html', context)

def biografia(request, nome):
    pessoa = get_object_or_404(Pessoa, nome=unquote(nome))
    return render(request, "main/biografia.html", {"pessoa": pessoa})

def genero(request, nome):
    genero = get_object_or_404(Genero, nome=unquote(nome))
    return render(request, 'main/genero.html', {'genero': genero})

def generos(request):
    generos = Genero.objects.all()[:8]
    return render(request, 'main/generos.html', {'generos': generos})

def filme(request, titulo):
    filme = get_object_or_404(Filme, titulo=unquote(titulo))
    return render(request, 'main/filme.html', {'filme': filme})

@login_required
def alugar(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    Aluguel.objects.create(usuario=request.user, filme=filme)
    return redirect(reverse('main:perfil'))


@login_required
def perfil(request):
    alugueis = Aluguel.objects.filter(usuario=request.user)
    return render(request, 'main/perfil.html', {'alugueis': alugueis})

@require_POST
def devolver(request, pk):
    Aluguel.objects.get(pk=pk).delete()
    return redirect(reverse('main:perfil'))


